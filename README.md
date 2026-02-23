# Procore Reports

CLI tool to generate project reports from Procore data.

## Reports Generated

1. **RFI Aging Report** - Tracks days open, flags overdue items
2. **Submittal Status Report** - Status breakdown by submittal
3. **Weekly Manpower Report** - Daily headcount and weather delays

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run in demo mode (no API credentials needed)
python main.py --demo

# Run specific report
python main.py --demo --report rfi
```

## API Setup

1. Copy `config.example.py` to `config.py`
2. Add your Procore API credentials
3. Run without `--demo` flag

## Output

Reports saved to `/output/` as CSV files:
- `rfi_aging_report.csv`
- `submittal_status.csv`
- `weekly_manpower.csv`
