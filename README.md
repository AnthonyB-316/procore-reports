# Procore Reports

Pulls RFIs, submittals, and daily logs from Procore and generates CSV reports. Built this to automate the weekly status reports I was doing manually on site.

## What it does

- **RFI Aging** - Shows how long each RFI has been open, flags overdue ones
- **Submittal Status** - Breakdown by status (approved, pending, rejected, etc.)
- **Manpower Summary** - Daily headcount from daily logs, weather delays

## Live Demo

[procore-reports.streamlit.app](https://procore-reports.streamlit.app)

## Usage

```bash
pip install -r requirements.txt

# web dashboard
streamlit run app.py

# CLI - demo mode (sample data, no API needed)
python main.py --demo

# CLI - specific report only
python main.py --demo --report rfi
```

## Connecting to Procore

Copy `config.example.py` to `config.py` and add your API credentials from the Procore developer portal. Then run without the `--demo` flag.

## Output

CSVs go to `/output/`:
- `rfi_aging_report.csv`
- `submittal_status.csv`
- `weekly_manpower.csv`
