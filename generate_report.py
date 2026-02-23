"""
Generate reports from Procore data
"""

import pandas as pd
from datetime import datetime
import os

OUTPUT_DIR = "output"


def calculate_rfi_aging(rfis):
    """
    Calculate days open for each RFI
    Flag overdue items (past due date and still open)
    """
    today = datetime.now()
    rfi_data = []

    for rfi in rfis:
        created = datetime.fromisoformat(rfi["created_at"].replace("Z", ""))
        days_open = (today - created).days

        # Check if overdue
        due_date = rfi.get("due_date", "")
        is_overdue = False
        if due_date and rfi["status"] == "open":
            due = datetime.strptime(due_date, "%Y-%m-%d")
            is_overdue = today > due

        rfi_data.append({
            "RFI #": rfi["number"],
            "Subject": rfi["subject"],
            "Status": rfi["status"].upper(),
            "Ball In Court": rfi.get("ball_in_court", {}).get("name", "Unknown"),
            "Due Date": due_date,
            "Days Open": days_open,
            "Overdue": "YES" if is_overdue else ""
        })

    df = pd.DataFrame(rfi_data)
    df = df.sort_values("Days Open", ascending=False)

    # Save to CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "rfi_aging_report.csv")
    df.to_csv(output_path, index=False)
    print(f"RFI Aging Report saved to {output_path}")

    # Summary
    open_count = len(df[df["Status"] == "OPEN"])
    overdue_count = len(df[df["Overdue"] == "YES"])
    print(f"  Open: {open_count} | Overdue: {overdue_count}")

    return df


def submittal_status_summary(submittals):
    """
    Create submittal status breakdown
    """
    submittal_data = []

    for sub in submittals:
        submittal_data.append({
            "Submittal #": sub["number"],
            "Title": sub["title"],
            "Spec Section": sub.get("spec_section", ""),
            "Status": sub["status"].upper().replace("_", " "),
            "Submitted By": sub.get("submitted_by", {}).get("name", "Unknown"),
            "Due Date": sub.get("due_date", "")
        })

    df = pd.DataFrame(submittal_data)

    # Save to CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "submittal_status.csv")
    df.to_csv(output_path, index=False)
    print(f"Submittal Status Report saved to {output_path}")

    # Summary by status
    print("  Status breakdown:")
    for status, count in df["Status"].value_counts().items():
        print(f"    {status}: {count}")

    return df


def weekly_manpower_summary(daily_logs):
    """
    Generate weekly summary from daily logs
    """
    summary_data = []
    total_manpower = 0
    weather_delays = 0

    for log in daily_logs:
        day_total = sum(m["headcount"] for m in log.get("manpower", []))
        total_manpower += day_total

        if log.get("weather_delay"):
            weather_delays += 1

        summary_data.append({
            "Date": log["log_date"],
            "Weather": log.get("weather", ""),
            "Delay": "YES" if log.get("weather_delay") else "",
            "Total Headcount": day_total,
            "Notes": log.get("notes", "")
        })

    df = pd.DataFrame(summary_data)

    # Save to CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "weekly_manpower.csv")
    df.to_csv(output_path, index=False)
    print(f"Weekly Manpower Report saved to {output_path}")

    # Summary
    print(f"  Days logged: {len(daily_logs)}")
    print(f"  Total manpower: {total_manpower}")
    print(f"  Weather delays: {weather_delays}")

    return df


if __name__ == "__main__":
    from fetch_data import ProcoreClient

    # Initialize client (will use demo mode if no config)
    client = ProcoreClient()
    client.authenticate()

    print("\n" + "=" * 50)
    print("PROCORE REPORTS")
    print("=" * 50)

    # Fetch data
    rfis = client.get_rfis()
    submittals = client.get_submittals()
    daily_logs = client.get_daily_logs()

    # Generate reports
    print("\n[1] RFI AGING REPORT")
    calculate_rfi_aging(rfis)

    print("\n[2] SUBMITTAL STATUS REPORT")
    submittal_status_summary(submittals)

    print("\n[3] WEEKLY MANPOWER REPORT")
    weekly_manpower_summary(daily_logs)

    print("\n" + "=" * 50)
    print(f"Reports saved to /{OUTPUT_DIR}/")
    print("=" * 50)
