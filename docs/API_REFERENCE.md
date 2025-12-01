# UP Prepaid Engine Automation – API & Component Reference

This document captures every public entry point that ships with the repository: utility scripts (`account.py`, `Download_Ledger.py`), the formula validation suite (`Formula/Formula_*.py`), the automated end-to-end test plans (`Test_Plan/PE_*.py`), and task triggers (`Test_Plan/Incremental_Trigger.py`). Each section lists the callable APIs, the parameters they expect, return values, side effects, and runnable examples.

---

## 1. Runtime Environment & Conventions

- **Python**: 3.10+ with `pandas`, `numpy`, `requests`, `openpyxl`, `psycopg2`, and `openpyxl` available in the active environment.
- **Filesystem layout**:
  - `Result_File/`: Excel workbooks emitted by every `PE_x` test run (`Report_PE_<id>.xlsx`).
  - `Consumer_details.csv`: CSV produced by `account.py` and consumed by `Download_Ledger.py`.
  - `logs/`: All scripts write rotating log files here (e.g., `logs/PE_101.log`).
- **Execution style**: all scripts are directly runnable with `python <path/to/script>.py`. Each exposes functions/classes that can also be imported programmatically.

---

## 2. Consumer Detail Extraction – `account.py`

### Purpose
Scans every `Result_File/Report_PE_*.xlsx`, reads the **Consumer Details** sheet, and flattens the key-value rows into a normalized CSV (`Consumer_details.csv`).

### Configuration Constants
| Name | Description |
| --- | --- |
| `RESULT_FOLDER` | Directory containing the Excel reports (`Result_File`). |
| `SHEET_NAME` | Sheet expected in every workbook (`Consumer Details`). |
| `OUTPUT_CSV` | Destination file name (`Consumer_details.csv`). |
| `REQUIRED_COLUMNS` | Case-insensitive set of fields extracted from the sheet. |

### Public API
| Function | Description | Arguments | Returns/Side Effects |
| --- | --- | --- | --- |
| `get_report_identifier(filename: str) -> str` | Strips extension to produce a stable report identifier (e.g., `Report_PE_101`). | `filename`: base file name. | `str` identifier used throughout the pipeline. |
| `extract_consumer_details(excel_file: str) -> pandas.DataFrame` | Reads a single workbook, maps required key/value pairs, and logs missing parameters. | `excel_file`: absolute or relative path. | Single-row `DataFrame` with `Report_ID` + required columns. Missing values are set to `None`. |
| `process_all_reports() -> pandas.DataFrame` | Iterates through every `Report_PE_*.xlsx`, invokes `extract_consumer_details`, and concatenates the results. | None (uses module constants). | Combined `DataFrame`. Logs progress, warnings, and total record counts. |
| `save_to_csv(df: pandas.DataFrame, output_file: str)` | Writes the aggregated dataframe to disk. | `df`: data to persist; `output_file`: custom file path. | Writes UTF-8 CSV; prints saved columns. |
| `main()` | CLI entry point that orchestrates processing + saving and prints a summary. | None | Produces `Consumer_details.csv` if data exists. |

### Usage
Run end-to-end collection:
```bash
python account.py
```
Embed inside other tooling:
```python
from account import process_all_reports, save_to_csv
summary_df = process_all_reports()
if not summary_df.empty:
    save_to_csv(summary_df, "artifacts/consumer_snapshot.csv")
```

---

## 3. Ledger Download – `Download_Ledger.py`

### Purpose
Consumes `Consumer_details.csv`, calls the Remote Prepaid Ledger API for every `(accountId, meterSrno)` pair, and writes one worksheet per report (`Prepaid_Ledger_Report.xlsx`).

### Configuration Constants
| Name | Description |
| --- | --- |
| `API_URL` | Base REST endpoint (`https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/`). |
| `CSV_FILE` | Source CSV path (defaults to `Consumer_details.csv`). |
| `REQUIRED_FIELDS` | Sorted subset of JSON keys copied into Excel sheets. |

### Public API
| Function | Description | Arguments | Returns/Side Effects |
| --- | --- | --- | --- |
| `read_consumer_details() -> list[tuple[str, str, str]]` | Loads `Consumer_details.csv`, validates required columns, and supplies `(Report_ID, accountId, meterSrno)` triples in order. | None | List of tuples (strings); warns about missing/empty rows. |
| `fetch_and_save_data()` | For every consumer triple, calls `API_URL`, normalizes the response, and writes sheets named after `Report_ID`. Also compiles an `Errors` sheet summarizing HTTP issues or empty responses. | Uses module constants; optional CLI args by editing constants. | Creates/overwrites `Prepaid_Ledger_Report.xlsx` in the current directory. Returns `None` but prints success/error counts. |

### Usage
Minimal CLI run after generating `Consumer_details.csv`:
```bash
python Download_Ledger.py
```
Embed to fetch specific accounts:
```python
from Download_Ledger import read_consumer_details, fetch_and_save_data
consumers = read_consumer_details()
print(f"Preparing to query {len(consumers)} ledgers")
fetch_and_save_data()
```

---

## 4. Formula Validation Suite – `Formula/Formula_101.py`, `_102.py`, `_103.py`

Each module defines a specialized `PrepaidLedgerComparison` class that re-computes ledger metrics and reconciles them with API responses.

### Shared Class API (`PrepaidLedgerComparison`)
| Method | Responsibility |
| --- | --- |
| `__init__(self)` | Declares the tariff-specific constants (rates, thresholds, account IDs, date ranges) and logging destinations. |
| `fetch_prepaid_ledger_data(self) -> pandas.DataFrame` | Calls the configured API endpoint, coerces timestamps, filters by the target month, and sorts chronologically. |
| `calculate_expected_values(self, df) -> pandas.DataFrame` | Applies the module’s tariff logic to compute expected EC/FC/ED/penalty values and running balances for each day. Adds `expected_*` columns. |
| `compare_values(self, df) -> pandas.DataFrame` | Compares every actual vs. expected column against a 0.01 tolerance, flags mismatches per row, and logs per-column health. |
| `generate_comparison_report(self, df, filename)` | Persists a curated Excel workbook (`Prepaid_Ledger` sheet) combining actual values, expected values, and status per row. |
| `run_comparison(self)` | High-level orchestrator: fetch → calculate → compare → export. Logs PASS/FAIL. |

### Module-Specific Behavior
| Module | Scenario | Notable Config |
| --- | --- | --- |
| `Formula_101` | Baseline EC/FC/ED computation for ST=10 (normal load up to 75% MD). | Fixed EC rate, FC capped at 75% contracted load, simple rebate logic. |
| `Formula_102` | Tariffs with max demand penalties, FC adjustments, and ED recalculations. | Tracks historical max demand, recomputes FC adjustment and Excess Demand Penalty (EDP) for >75% or >100% MD. |
| `Formula_103` | Life-line switch scenarios with tiered EC & FC rates and switch-charge amortization. | Handles tiered EC slabs, FC life-line switch deductions, EC/FC life-line recovery over 3 days, and complex rebate math. |

### Usage
Run a formula check end-to-end:
```bash
python Formula/Formula_101.py
```
Programmatic execution:
```python
from Formula.Formula_103 import PrepaidLedgerComparison
report = PrepaidLedgerComparison()
report.run_comparison()
```
To test alternative accounts or windows, subclass or monkey-patch the relevant attributes before calling `run_comparison()`.

---

## 5. Automated Test Plans – `Test_Plan/PE_<id>.py`

There are 125 deterministic regression plans covering service types 10–225. Every file shares the same helper API but bakes in distinct constants (`SUPPLY_TYPECODE`, load, flags, PF behavior, etc.) at the top of the script.

### Shared Helper Functions (per `PE_x`)
| Function | Description | Key Inputs | Side Effects |
| --- | --- | --- | --- |
| `create_account()` | Calls the MDMS account onboarding API (`initial_master_sync`) using randomly generated metadata seeded by each script’s constants. | Module-level constants (supply type, load, opening balance, etc.). | Returns a dict with `accountId`, `meterSrno`, `meterInstalldate`, `badgeNumber`, and the submitted payload. Writes to `logs/PE_<id>.log`. |
| `fill_daily_load_data(account_data)` | Connects to PostgreSQL (`validation_rules`) and inserts synthetic cumulative energy rows into `dailyload_vee_validated` covering the full billing window. | `account_data` from `create_account()`, DB credentials, daily load ceilings (`END_WH`, `MD_W`). | Inserts `total_days` rows via `psycopg2`, commits/rolls back on error. |
| `fill_profile_instant_data(account_data)` | Generates instantaneous MD profiles and inserts them into `profile_instant_vee`. | Reuses `account_data`, MD thresholds, and DB credentials. | Inserts one row per day with ramped MD_W/MD_VA values. |
| `trigger_prepaid_ledger(account_id)` | Invokes `daily_ledger_task` for `account_id` and yesterday’s date (URL-encoded). | `account_id` string. | Issues GET to `https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/...`, logs status. |
| `fetch_daily_load_data(meter_srno)` | Calls MDMS `/dailyloads` API to retrieve the newly inserted load samples for reporting. | `meter_srno`. | Returns list of JSON rows; warns on empty responses. |
| `fetch_profile_instant_data(meter_srno)` | Calls MDMS `/profileinstant` API to capture instantaneous metrics. | `meter_srno`. | Returns list of JSON rows; warns on empty responses. |
| `generate_excel_report(account_data)` | Assembles `Report_PE_<id>.xlsx` with **Summary**, **Consumer Details**, **Daily Load**, and **Profile Instant** sheets. | `account_data`, helper fetchers above. | Writes the workbook under `Result_File/`. |
| `main()` | Runs Steps 1–5 sequentially with logging and short-circuiting on failure. | None. | Produces a new result workbook + logs. |

> **Note:** Because the helper implementations are identical, you can safely import one `PE_x` module and reuse its functions in bespoke harnesses. The difference between files is limited to the constants (tariff, limits, feature flags) and docstring metadata.

### Running an Individual Test Plan
```bash
python Test_Plan/PE_101.py        # runs the ST=10 baseline scenario
python Test_Plan/PE_150.py        # runs ST=20 MMC season 2 (>4kW)
```
Typical orchestration when chaining with downstream utilities:
1. Execute the desired `PE_x` module(s) to populate `Result_File/Report_PE_xxx.xlsx`.
2. Run `python account.py` to consolidate consumer details into CSV.
3. Run `python Download_Ledger.py` to download ledger data for the produced accounts.
4. Run the appropriate `Formula/Formula_x.py` validator if deeper reconciliation is required.

### Test Case Matrix
The table below enumerates every `PE_x` script and its documented focus area. Use the ID to locate the matching file under `Test_Plan/`.

| Test Case | Scenario Focus |
| --- | --- |
| `PE_101` | To verify prepaid ledger calculation for ST = 10 (normal 10A), With Consumption = up to 100 kWh and MD = upto 75%. |
| `PE_102` | To verify prepaid ledger calculation for ST = 10 (normal 10A), With Consumption = up to 100 kWh and MD = upto 150% |
| `PE_103` | To verify prepaid ledger calculation for ST = 10 (lifeline switch), With Consumption = up to 400 kWh and MD = below 75% |
| `PE_104` | To verify prepaid ledger calculation for ST = 10 (lifeline switch), With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_105` | To verify prepaid ledger calculation for ST = 10 (lifeline switch - less than 3 days of the month) |
| `PE_106` | To verify prepaid ledger calculation for ST = 10 (lifeline switch 3 month scanarios) |
| `PE_107` | To verify prepaid ledger calculation for ST = 10 (lifeline switch 4 month scanarios) |
| `PE_108` | To verify prepaid ledger calculation for ST = 10 (normal 10B), With Consumption = up to 400 kWh and MD = below 75% |
| `PE_109` | To verify prepaid ledger calculation for ST = 10 (normal 10B), With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_110` | To verify prepaid ledger calculation for ST = 10 (normal 10A with green energy) |
| `PE_111` | To verify prepaid ledger calculation for ST = 10 (lifeline switch with green energy) |
| `PE_112` | To verify prepaid ledger calculation for ST = 10 (normal 10A with meter installation in mid of the month) |
| `PE_113` | To verify prepaid ledger calculation for ST = 10 (kVA to kW Conversion) |
| `PE_114` | To verify prepaid ledger calculation for ST = 10 (BHP to kW Conversion) |
| `PE_115` | To verify prepaid ledger calculation for ST = 10 (normal 10A with FPPAS) |
| `PE_116` | To verify prepaid ledger calculation for ST = 10 (lifeline switch with FPPAS) |
| `PE_117` | To verify prepaid ledger calculation for ST = 10 with PF Surcharge |
| `PE_118` | To verify prepaid ledger calculation for ST = 10 with PF Surcharge |
| `PE_119` | To verify prepaid ledger calculation for ST = 17 (normal 17A), With Consumption = up to 100 kWh and MD = upto 75%. |
| `PE_120` | To verify prepaid ledger calculation for ST = 17 (normal 17A), With Consumption = up to 100 kWh and MD = upto 150% |
| `PE_121` | To verify prepaid ledger calculation for ST = 17 (lifeline switch), With Consumption = up to 400 kWh and MD = below 75% |
| `PE_122` | To verify prepaid ledger calculation for ST = 17 (lifeline switch), With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_123` | To verify prepaid ledger calculation for ST = 17 (lifeline switch - less than 3 days of the month) |
| `PE_124` | To verify prepaid ledger calculation for ST = 17 (lifeline switch 3 month scanarios) |
| `PE_125` | To verify prepaid ledger calculation for ST = 17 (lifeline switch 4 month scanarios) |
| `PE_126` | To verify prepaid ledger calculation for ST = 17 (normal 17B), With Consumption = up to 400 kWh and MD = below 75% |
| `PE_127` | To verify prepaid ledger calculation for ST = 17 (normal 17B), With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_128` | To verify prepaid ledger calculation for ST = 17 (normal 17A with green energy) |
| `PE_129` | To verify prepaid ledger calculation for ST = 17 (lifeline switch with green energy) |
| `PE_130` | To verify prepaid ledger calculation for ST = 17 (normal 17A with meter installation in mid of the month) |
| `PE_131` | To verify prepaid ledger calculation for ST = 17 (kVA to kW Conversion) |
| `PE_132` | To verify prepaid ledger calculation for ST = 17 (BHP to kW Conversion) |
| `PE_133` | To verify prepaid ledger calculation for ST = 17 (normal 10A with FPPAS) |
| `PE_134` | To verify prepaid ledger calculation for ST = 17 (lifeline switch with FPPAS) |
| `PE_135` | To verify prepaid ledger calculation for ST = 17 with PF Surcharge |
| `PE_136` | To verify prepaid ledger calculation for ST = 17 with PF Surcharge |
| `PE_137` | To verify prepaid ledger calculation for ST = 11 With Consumption = up to 400 kVAh and MD = upto 150% |
| `PE_138` | To verify prepaid ledger calculation for ST = 11 with green energy |
| `PE_139` | To verify prepaid ledger calculation for ST = 11 (kW to kVA Conversion) |
| `PE_140` | To verify prepaid ledger calculation for ST = 11 (BHP to kVA Conversion) |
| `PE_141` | To verify prepaid ledger calculation for ST = 12 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_142` | To verify prepaid ledger calculation for ST = 14 With Consumption = up to 400 kVAh and MD = upto 150% |
| `PE_143` | To verify prepaid ledger calculation for ST = 15 With Consumption = up to 400 kVAh and MD = upto 150% |
| `PE_144` | To verify prepaid ledger calculation for ST = 18 With Consumption = up to 400 kVAh and MD = upto 150% |
| `PE_145` | To verify prepaid ledger calculation for ST = 19 With Consumption = up to 400 kVAh and MD = upto 150% |
| `PE_146` | To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW) |
| `PE_147` | To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW with FPPAS) |
| `PE_148` | To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW) |
| `PE_149` | To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW) |
| `PE_150` | To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW) |
| `PE_151` | To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW) |
| `PE_152` | To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW) |
| `PE_153` | To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW) |
| `PE_154` | To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW) |
| `PE_155` | To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW) |
| `PE_156` | To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW) |
| `PE_157` | To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW) |
| `PE_158` | To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW) |
| `PE_159` | To verify prepaid ledger calculation for ST = 24B With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_160` | To verify prepaid ledger calculation for ST = 24C With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_161` | To verify prepaid ledger calculation for ST = 24D With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_162` | To verify prepaid ledger calculation for ST = 25 (Powerlooom Below 5kW - Urban) |
| `PE_163` | To verify prepaid ledger calculation for ST = 26 (Powerlooom Below 5kW - Rural) |
| `PE_164` | To verify prepaid ledger calculation for ST = 27 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_165` | To verify prepaid ledger calculation for ST = 28 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_166` | To verify prepaid ledger calculation for ST = 33 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_167` | To verify prepaid ledger calculation for ST = 34 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_168` | To verify prepaid ledger calculation for ST = 35 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_169` | To verify prepaid ledger calculation for ST = 36 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_170` | To verify prepaid ledger calculation for ST = 37 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_171` | To verify prepaid ledger calculation for ST = 38 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_172` | To verify prepaid ledger calculation for ST = 40 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_173` | To verify prepaid ledger calculation for ST = 40A With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_174` | To verify prepaid ledger calculation for ST = 41 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_175` | To verify prepaid ledger calculation for ST = 41A With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_176` | To verify prepaid ledger calculation for ST = 42 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_177` | To verify prepaid ledger calculation for ST = 42A With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_178` | To verify prepaid ledger calculation for ST = 43 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_179` | To verify prepaid ledger calculation for ST = 44 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_180` | To verify prepaid ledger calculation for ST = 45 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_181` | To verify prepaid ledger calculation for ST = 46 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_182` | To verify prepaid ledger calculation for ST = 47 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_183` | To verify prepaid ledger calculation for ST = 48 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_184` | To verify prepaid ledger calculation for ST = 51 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_185` | To verify prepaid ledger calculation for ST = 52 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_186` | To verify prepaid ledger calculation for ST = 53 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_187` | To verify prepaid ledger calculation for ST = 54 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_188` | To verify prepaid ledger calculation for ST = 55 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_189` | To verify prepaid ledger calculation for ST = 56 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_190` | To verify prepaid ledger calculation for ST = 57 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_191` | To verify prepaid ledger calculation for ST = 58 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_192` | To verify prepaid ledger calculation for ST = 60 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_193` | To verify prepaid ledger calculation for ST = 60 (seasonal benefits) With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_194` | To verify prepaid ledger calculation for ST = 61 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_195` | To verify prepaid ledger calculation for ST = 63 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_196` | To verify prepaid ledger calculation for ST = 64 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_197` | To verify prepaid ledger calculation for ST = 62T (ToU - season 1) |
| `PE_198` | To verify prepaid ledger calculation for ST = 62T (ToU - season 2) |
| `PE_199` | To verify prepaid ledger calculation for ST = 65 (Powerlooom Above 5kW - Rural) |
| `PE_200` | To verify prepaid ledger calculation for ST = 66 (Powerlooom Above 5kW - Rural) |
| `PE_201` | To verify prepaid ledger calculation for ST = 67 (Powerlooom Above 5kW - Urban) |
| `PE_202` | To verify prepaid ledger calculation for ST = 68 (Powerlooom Above 5kW - Urban) |
| `PE_203` | To verify prepaid ledger calculation for ST = 72 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_204` | To verify prepaid ledger calculation for ST = 73 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_205` | To verify prepaid ledger calculation for ST = 74 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_206` | To verify prepaid ledger calculation for ST = 75 With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_207` | To verify prepaid ledger calculation for ST = 76R With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_208` | To verify prepaid ledger calculation for ST = 76U With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_209` | To verify prepaid ledger calculation for ST = 77R With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_210` | To verify prepaid ledger calculation for ST = 77U With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_211` | To verify prepaid ledger calculation for ST = 92 (Weekly minimum charge) |
| `PE_212` | To verify prepaid ledger calculation for ST = 93 (Weekly minimum charge) |
| `PE_213` | To verify prepaid ledger calculation for ST = 94 (Weekly minimum charge) |
| `PE_214` | To verify prepaid ledger calculation for ST = 95 (Weekly minimum charge) |
| `PE_215` | To verify prepaid ledger calculation for ST = 92 (Weekly minimum charge + Temporary Consumer) |
| `PE_216` | To verify prepaid ledger calculation for ST = 93 (Weekly minimum charge + Temporary Consumer) |
| `PE_217` | To verify prepaid ledger calculation for ST = 94 (Weekly minimum charge + Temporary Consumer) |
| `PE_218` | To verify prepaid ledger calculation for ST = 95 (Weekly minimum charge + Temporary Consumer) |
| `PE_219` | To verify prepaid ledger calculation for ST = 92 (3rd year ownward EC rate increase 10%) |
| `PE_220` | To verify prepaid ledger calculation for ST = 11A With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_221` | To verify prepaid ledger calculation for ST = 11B With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_222` | To verify prepaid ledger calculation for ST = 11C With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_223` | To verify prepaid ledger calculation for ST = 11F With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_224` | To verify prepaid ledger calculation for ST = 11G With Consumption = up to 400 kWh and MD = upto 150% |
| `PE_225` | To verify prepaid ledger calculation for ST = 11H With Consumption = up to 400 kWh and MD = upto 150% |

---

## 6. Incremental Trigger – `Test_Plan/Incremental_Trigger.py`

| Function | Description |
| --- | --- |
| `trigger_incremental_task() -> bool` | Fires `https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/` and returns `True` on HTTP 200. Logs responses to `logs/Incremental_Trigger.log`. |

Usage:
```bash
python Test_Plan/Incremental_Trigger.py
```
Programmatic call:
```python
from Test_Plan.Incremental_Trigger import trigger_incremental_task
if not trigger_incremental_task():
    raise RuntimeError("Incremental task failed")
```

---

## 7. Putting It All Together – Recommended Workflows

1. **Generate synthetic accounts and meter data** using the relevant `PE_x` modules (Section 5). This creates source reports under `Result_File/` and activity logs under `logs/`.
2. **Aggregate consumer metadata** by running `python account.py`. The resulting `Consumer_details.csv` lists every account ID/meter pair for downstream automation.
3. **Download ledger outputs** for each consumer via `python Download_Ledger.py`. The Excel workbook includes a sheet per test case and an optional `Errors` sheet for failed calls.
4. **Validate tariff math** with the formula suite, e.g., `python Formula/Formula_102.py`. Investigate mismatches by opening the generated Excel workbook and cross-referencing the logs.
5. **Trigger incremental workflows** (if required) using `python Test_Plan/Incremental_Trigger.py`.

Keep this reference handy while onboarding new contributors or wiring these scripts into CI so that each automation step and public API surface remains unambiguous.
