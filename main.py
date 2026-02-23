#!/usr/bin/env python3
"""
Procore Reports CLI
Generate RFI aging, submittal status, and manpower reports
"""

import argparse
from fetch_data import ProcoreClient
from generate_report import (
    calculate_rfi_aging,
    submittal_status_summary,
    weekly_manpower_summary
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate reports from Procore project data"
    )
    parser.add_argument(
        "--report",
        choices=["all", "rfi", "submittals", "manpower"],
        default="all",
        help="Which report to generate (default: all)"
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Force demo mode with sample data"
    )

    args = parser.parse_args()

    # Initialize client
    client = ProcoreClient(demo_mode=args.demo if args.demo else None)
    client.authenticate()

    print("\n" + "=" * 50)
    print("PROCORE REPORTS")
    print("=" * 50)

    # Fetch data based on report type
    if args.report in ["all", "rfi"]:
        print("\n[1] RFI AGING REPORT")
        rfis = client.get_rfis()
        calculate_rfi_aging(rfis)

    if args.report in ["all", "submittals"]:
        print("\n[2] SUBMITTAL STATUS REPORT")
        submittals = client.get_submittals()
        submittal_status_summary(submittals)

    if args.report in ["all", "manpower"]:
        print("\n[3] WEEKLY MANPOWER REPORT")
        daily_logs = client.get_daily_logs()
        weekly_manpower_summary(daily_logs)

    print("\n" + "=" * 50)
    print("Reports saved to /output/")
    print("=" * 50)


if __name__ == "__main__":
    main()
