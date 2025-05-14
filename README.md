# 🇳🇵 Nepali Utility CLI Toolkit

A command-line tool built in Python for common Nepali utilities:

- 📅 AD ↔ BS Calendar Conversion
- 🆔 NID Number Format Validation
- 🔤 Unicode ↔ Preeti Converter
- ⚡ Power Schedule (Load Shedding) Lookup

## 🔧 Installation

```bash
pip install -e .


🧪 Usage

nepcli convert-date --from AD --date 2025-05-14
nepcli validate-nid --nid 209876543210
nepcli convert-text --from unicode --text "नेपाल"
nepcli power-schedule --ward 2
