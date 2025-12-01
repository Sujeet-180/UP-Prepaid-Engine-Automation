# Documentation Index

Complete documentation for the UP Prepaid Engine Automation Framework.

## 📚 Main Documentation

### [README.md](../README.md)
**Main project documentation**
- Overview and features
- Installation instructions
- Quick start guide
- Project structure
- Configuration
- Troubleshooting
- Best practices

### [QUICK_START.md](../QUICK_START.md)
**Get started in 5 minutes**
- Quick installation
- First test run
- Common workflows
- Tips and tricks

---

## 📖 Detailed Guides

### [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
**Comprehensive API reference**
- All public functions and classes
- Parameters and return types
- Usage examples
- Data models
- Error handling

**Covers:**
- Core Modules (account.py, Download_Ledger.py)
- Formula Validation (Formula_101, 102, 103)
- Test Plans (PE_101, Incremental_Trigger)

### [FORMULA_GUIDE.md](FORMULA_GUIDE.md)
**Formula validation details**
- Calculation formulas
- Validation logic
- Tolerance and comparison
- Troubleshooting

**Three validation levels:**
- Formula_101: Basic flat rates
- Formula_102: Max demand penalties
- Formula_103: Tiered rates with lifeline

### [TEST_PLAN_GUIDE.md](TEST_PLAN_GUIDE.md)
**Test case execution guide**
- Test execution workflow
- Database operations
- API integration
- Excel report generation
- All test cases reference

**Covers:**
- 5-step test execution process
- Data generation algorithms
- API endpoints and payloads
- Troubleshooting common issues

### [EXAMPLES.md](EXAMPLES.md)
**Practical code examples**
- Quick start examples
- Core module usage
- Formula validation
- Test plan customization
- Advanced recipes
- Automation scripts
- Integration examples

**13+ working examples** covering all use cases

---

## 🚀 Quick Reference

### Installation
```bash
pip install -r requirements.txt
python verify_installation.py
```

### Basic Usage
```bash
# Run test
python Test_Plan/PE_101.py

# Extract data
python account.py

# Download ledger
python Download_Ledger.py

# Validate
python Formula/Formula_101.py
```

---

## 📂 Documentation Structure

```
docs/
├── INDEX.md                    # This file
├── API_DOCUMENTATION.md        # Complete API reference
├── FORMULA_GUIDE.md           # Formula validation guide
├── TEST_PLAN_GUIDE.md         # Test execution guide
└── EXAMPLES.md                # Code examples

Root directory:
├── README.md                   # Main documentation
├── QUICK_START.md             # Quick start guide
├── requirements.txt           # Python dependencies
└── verify_installation.py     # Setup verification
```

---

## 🎯 By Task

### I want to...

#### ...get started quickly
→ [QUICK_START.md](../QUICK_START.md)

#### ...understand the project
→ [README.md](../README.md)

#### ...look up a function
→ [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

#### ...understand formulas
→ [FORMULA_GUIDE.md](FORMULA_GUIDE.md)

#### ...run test cases
→ [TEST_PLAN_GUIDE.md](TEST_PLAN_GUIDE.md)

#### ...see code examples
→ [EXAMPLES.md](EXAMPLES.md)

#### ...troubleshoot issues
→ [README.md#troubleshooting](../README.md#troubleshooting)
→ [FORMULA_GUIDE.md#troubleshooting](FORMULA_GUIDE.md#troubleshooting)
→ [TEST_PLAN_GUIDE.md#troubleshooting](TEST_PLAN_GUIDE.md#troubleshooting)

#### ...extend functionality
→ [EXAMPLES.md#custom-extensions](EXAMPLES.md#custom-extensions)

#### ...automate testing
→ [EXAMPLES.md#automation-scripts](EXAMPLES.md#automation-scripts)

---

## 📊 By Component

### Core Modules

| Module | API Docs | Examples |
|--------|----------|----------|
| account.py | [Link](API_DOCUMENTATION.md#accountpy) | [Link](EXAMPLES.md#core-module-examples) |
| Download_Ledger.py | [Link](API_DOCUMENTATION.md#download_ledgerpy) | [Link](EXAMPLES.md#core-module-examples) |

### Formula Validation

| Module | Guide | API Docs | Examples |
|--------|-------|----------|----------|
| Formula_101 | [Link](FORMULA_GUIDE.md#formula_101-basic-validation) | [Link](API_DOCUMENTATION.md#formula_101py) | [Link](EXAMPLES.md#formula-validation-examples) |
| Formula_102 | [Link](FORMULA_GUIDE.md#formula_102-advanced-validation) | [Link](API_DOCUMENTATION.md#formula_102py) | [Link](EXAMPLES.md#formula-validation-examples) |
| Formula_103 | [Link](FORMULA_GUIDE.md#formula_103-complete-validation) | [Link](API_DOCUMENTATION.md#formula_103py) | [Link](EXAMPLES.md#formula-validation-examples) |

### Test Plans

| Component | Guide | API Docs | Examples |
|-----------|-------|----------|----------|
| PE_101 | [Link](TEST_PLAN_GUIDE.md#pe_101-basic-test-case) | [Link](API_DOCUMENTATION.md#pe_101py) | [Link](EXAMPLES.md#test-plan-examples) |
| Incremental Trigger | [Link](TEST_PLAN_GUIDE.md#incremental-trigger) | [Link](API_DOCUMENTATION.md#incremental_triggerpy) | [Link](EXAMPLES.md#test-plan-examples) |

---

## 🔍 Search by Topic

### Configuration
- [API Endpoints](../README.md#api-endpoints)
- [Database Setup](../README.md#database-configuration)
- [Formula Parameters](../README.md#formula-parameters)

### Formulas
- [Basic Formulas](FORMULA_GUIDE.md#formula_101-basic-validation)
- [Advanced Formulas](FORMULA_GUIDE.md#formula_102-advanced-validation)
- [Tiered Rates](FORMULA_GUIDE.md#formula_103-complete-validation)
- [Lifeline Switch](FORMULA_GUIDE.md#lifeline-switch-mechanism)

### Database
- [Tables Used](TEST_PLAN_GUIDE.md#tables-used)
- [Data Generation](TEST_PLAN_GUIDE.md#step-2-fill-daily-load-data)
- [Best Practices](TEST_PLAN_GUIDE.md#best-practices)

### APIs
- [Account Creation](TEST_PLAN_GUIDE.md#1-account-creation-api)
- [Ledger Trigger](TEST_PLAN_GUIDE.md#2-daily-ledger-trigger-api)
- [Data Fetch](TEST_PLAN_GUIDE.md#3-mdms-data-fetch-apis)

### Automation
- [Scheduled Tests](EXAMPLES.md#example-11-scheduled-test-runner-cron)
- [Batch Processing](EXAMPLES.md#example-8-parallel-test-execution-sequential)
- [Custom Scripts](EXAMPLES.md#automation-scripts)

---

## 📝 Documentation Standards

All documentation follows these standards:
- **Markdown format** for readability
- **Code examples** with syntax highlighting
- **Step-by-step instructions** where applicable
- **Error handling** guidance
- **Best practices** sections
- **Cross-references** between documents

---

## 🤝 Contributing

### Adding Documentation

1. Follow existing format and style
2. Include code examples
3. Add cross-references
4. Update this index
5. Test all code examples

### Documentation Checklist

- [ ] Clear title and description
- [ ] Table of contents
- [ ] Code examples tested
- [ ] Links verified
- [ ] Formatting consistent
- [ ] Updated INDEX.md

---

## 📈 Version History

### Version 1.0 (December 2025)
- Initial comprehensive documentation
- 5 main documentation files
- 100+ pages of content
- 13+ working examples
- Complete API reference
- Formula validation guide
- Test execution guide

---

## 🆘 Getting Help

1. **Check Documentation**
   - Start with [QUICK_START.md](../QUICK_START.md)
   - Search this index for your topic
   - Review relevant guides

2. **Check Logs**
   - All modules create detailed logs in `logs/`
   - Check for error messages and stack traces

3. **Review Examples**
   - [EXAMPLES.md](EXAMPLES.md) has working code
   - Adapt examples to your use case

4. **Troubleshooting Guides**
   - [Main Troubleshooting](../README.md#troubleshooting)
   - [Formula Troubleshooting](FORMULA_GUIDE.md#troubleshooting)
   - [Test Plan Troubleshooting](TEST_PLAN_GUIDE.md#troubleshooting)

---

## 📞 Support

For issues, questions, or contributions:
- Check documentation first
- Review logs in `logs/` directory
- Test with [verify_installation.py](../verify_installation.py)

---

**Last Updated:** December 2025  
**Framework Version:** 1.0

---

[← Back to README](../README.md)
