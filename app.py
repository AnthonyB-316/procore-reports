"""
Procore Reports - Streamlit Dashboard
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from sample_data import SAMPLE_RFIS, SAMPLE_SUBMITTALS, SAMPLE_DAILY_LOGS

st.set_page_config(page_title="Procore Reports", layout="wide", initial_sidebar_state="expanded")

# Procore-style CSS
st.markdown("""
<style>
    /* Procore orange header */
    .stApp > header {
        background-color: #F47E20;
    }

    /* Hide default header, use custom */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Procore header bar */
    .procore-header {
        background: linear-gradient(90deg, #2D3E50 0%, #1a2633 100%);
        padding: 12px 24px;
        margin: -1rem -1rem 1.5rem -1rem;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .procore-logo {
        color: #F47E20;
        font-size: 24px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .procore-project {
        color: #fff;
        font-size: 14px;
        opacity: 0.9;
    }

    /* Orange accent on tabs */
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        border-bottom-color: #F47E20;
        color: #F47E20;
    }

    /* Card-style metrics - main area */
    section[data-testid="stMain"] [data-testid="stMetric"] {
        background: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    section[data-testid="stMain"] [data-testid="stMetricValue"] {
        color: #2D3E50 !important;
    }
    section[data-testid="stMain"] [data-testid="stMetricLabel"] {
        color: #666 !important;
    }

    /* Table styling */
    .stDataFrame {
        border: 1px solid #e0e0e0;
        border-radius: 4px;
    }

    /* Status badges */
    .status-open { background: #FFF3E0; color: #E65100; padding: 2px 8px; border-radius: 3px; font-size: 12px; }
    .status-closed { background: #E8F5E9; color: #2E7D32; padding: 2px 8px; border-radius: 3px; font-size: 12px; }
    .status-overdue { background: #FFEBEE; color: #C62828; padding: 2px 8px; border-radius: 3px; font-size: 12px; font-weight: 600; }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #2D3E50;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #fff !important;
    }
    [data-testid="stSidebar"] [data-testid="stMetric"] {
        background: #3d4f61;
        border-radius: 4px;
        padding: 10px;
    }
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: #F47E20 !important;
    }
    [data-testid="stSidebar"] [data-testid="stMetricLabel"] p {
        color: #ccc !important;
    }
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: #3d4f61;
    }
    [data-testid="stSidebar"] .stSelectbox svg {
        fill: #fff;
    }
    [data-testid="stSidebar"] hr {
        border-color: #4a5d6f;
    }
</style>
""", unsafe_allow_html=True)

# Procore-style header
st.markdown("""
<div class="procore-header">
    <span class="procore-logo">procore</span>
    <span class="procore-project">Waldorf Astoria Renovation</span>
</div>
""", unsafe_allow_html=True)

# Calculate stats for sidebar
open_rfis = len([r for r in SAMPLE_RFIS if r["status"] == "open"])
pending_subs = len([s for s in SAMPLE_SUBMITTALS if s["status"] == "pending"])
latest_workers = sum(m["headcount"] for m in SAMPLE_DAILY_LOGS[-1].get("manpower", []))

# Sidebar - project info
with st.sidebar:
    st.markdown("### Project Tools")
    tool = st.selectbox("Select Report", ["RFIs", "Submittals", "Daily Log"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("**Project Info**")
    st.caption("Waldorf Astoria NYC")
    st.caption("301 Park Avenue")
    st.caption("New York, NY 10022")

    st.markdown("---")
    st.markdown("**Quick Stats**")
    st.metric("Open RFIs", open_rfis, help="Requests for Information awaiting response")
    st.metric("Pending Submittals", pending_subs, help="Shop drawings/samples awaiting approval")
    st.metric("Workers Today", latest_workers, help="Total trade workers on site today")

# Main content based on sidebar selection
today = datetime.now()

if tool == "RFIs":
    st.markdown("## RFIs")

    # Summary cards
    rfi_data = []
    for rfi in SAMPLE_RFIS:
        created = datetime.fromisoformat(rfi["created_at"].replace("Z", ""))
        days_open = (today - created).days
        due_date = rfi.get("due_date", "")
        is_overdue = False
        if due_date and rfi["status"] == "open":
            due = datetime.strptime(due_date, "%Y-%m-%d")
            is_overdue = today > due

        rfi_data.append({
            "#": rfi["number"],
            "Subject": rfi["subject"],
            "Status": rfi["status"].upper(),
            "Priority": rfi.get("priority", ""),
            "Ball In Court": rfi.get("ball_in_court", {}).get("name", ""),
            "Assignee": rfi.get("assignee", {}).get("name", ""),
            "Location": rfi.get("location", ""),
            "Created": created.strftime("%m/%d/%y"),
            "Due Date": due_date,
            "Days Open": days_open,
            "Cost Impact": rfi.get("cost_impact", ""),
            "Schedule": "Yes" if rfi.get("schedule_impact") == "Yes" else "",
            "Overdue": "OVERDUE" if is_overdue else ""
        })

    df = pd.DataFrame(rfi_data).sort_values("Days Open", ascending=False)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total", len(df), help="Total RFIs submitted on project")
    col2.metric("Open", len(df[df["Status"] == "OPEN"]), help="RFIs awaiting response from architect/engineer")
    col3.metric("Closed", len(df[df["Status"] == "CLOSED"]), help="RFIs with official responses")
    col4.metric("Overdue", len(df[df["Overdue"] == "OVERDUE"]), help="RFIs past their required response date")
    col5.metric("High Priority", len(df[df["Priority"] == "High"]), help="RFIs blocking critical path work")

    st.markdown("####")

    # Style the dataframe
    def style_overdue(val):
        if val == "OVERDUE":
            return "color: #C62828; font-weight: 600"
        return ""

    def style_status(val):
        if val == "OPEN":
            return "color: #E65100"
        elif val == "CLOSED":
            return "color: #2E7D32"
        elif val == "DRAFT":
            return "color: #757575"
        return ""

    def style_priority(val):
        if val == "High":
            return "color: #C62828; font-weight: 600"
        return ""

    styled_df = df.style.applymap(style_overdue, subset=["Overdue"]).applymap(style_status, subset=["Status"]).applymap(style_priority, subset=["Priority"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=450)

elif tool == "Submittals":
    st.markdown("## Submittals")

    sub_data = []
    for sub in SAMPLE_SUBMITTALS:
        sub_data.append({
            "#": sub["number"],
            "Rev": sub.get("revision", "0"),
            "Title": sub["title"],
            "Spec Section": sub.get("spec_section", ""),
            "Type": sub.get("type", ""),
            "Status": sub["status"].upper().replace("_", " "),
            "Responsible": sub.get("responsible_contractor", ""),
            "Submitted By": sub.get("submitted_by", {}).get("name", ""),
            "Approver": sub.get("approver", {}).get("name", ""),
            "Submitted": sub.get("submitted_date", ""),
            "Due Date": sub.get("due_date", ""),
            "Approved": sub.get("approved_date", ""),
            "Lead Time": sub.get("lead_time", "")
        })

    df = pd.DataFrame(sub_data)

    # Status counts
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total", len(df), help="Total submittals on project")
    col2.metric("Approved", len(df[df["Status"] == "APPROVED"]) + len(df[df["Status"] == "APPROVED AS NOTED"]), help="Cleared for fabrication/installation")
    col3.metric("Pending", len(df[df["Status"] == "PENDING"]), help="Awaiting architect/engineer review")
    col4.metric("Revise", len(df[df["Status"] == "REVISE RESUBMIT"]), help="Rejected - contractor must resubmit")
    col5.metric("Rejected", len(df[df["Status"] == "REJECTED"]), help="Does not comply with specs")

    st.markdown("####")

    def color_status(val):
        colors = {
            "APPROVED": "color: #2E7D32; font-weight: 600",
            "PENDING": "color: #E65100",
            "REVISE RESUBMIT": "color: #F57F17; font-weight: 600",
            "APPROVED AS NOTED": "color: #1565C0",
            "REJECTED": "color: #C62828; font-weight: 600"
        }
        return colors.get(val, "")

    styled_df = df.style.applymap(color_status, subset=["Status"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=450)

else:  # Daily Log
    st.markdown("## Daily Log")

    mp_data = []
    daily_counts = []
    all_deliveries = 0

    for log in SAMPLE_DAILY_LOGS:
        day_total = sum(m["headcount"] for m in log.get("manpower", []))
        daily_counts.append(day_total)
        all_deliveries += len(log.get("deliveries", []))

        trades = ", ".join([f"{m['trade']} ({m['headcount']})" for m in log.get("manpower", [])])
        deliveries = ", ".join(log.get("deliveries", [])) if log.get("deliveries") else ""
        visitors = ", ".join(log.get("visitors", [])) if log.get("visitors") else ""

        mp_data.append({
            "Date": log["log_date"],
            "Day": log.get("day", ""),
            "Hours": log.get("work_hours", ""),
            "Weather": log.get("weather", ""),
            "Delay": "Yes" if log.get("weather_delay") else "",
            "Workers": day_total,
            "Trades": trades,
            "Work Performed": log.get("work_performed", ""),
            "Deliveries": deliveries,
            "Visitors": visitors,
            "Notes": log.get("notes", "")
        })

    df = pd.DataFrame(mp_data)

    avg_workers = sum(daily_counts) // len(daily_counts) if daily_counts else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Days Logged", len(df), help="Total days with recorded daily logs")
    col2.metric("Avg Daily Workers", avg_workers, help="Average trade workers on site per day")
    col3.metric("Deliveries", all_deliveries, help="Total material deliveries recorded")
    col4.metric("Weather Delays", len(df[df["Delay"] == "Yes"]), help="Days with weather-related work stoppages")

    st.markdown("####")

    # Style delays
    def style_delay(val):
        if val == "Yes":
            return "color: #E65100; font-weight: 600"
        return ""

    styled_df = df.style.applymap(style_delay, subset=["Delay"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=350)

    # Trade breakdown for latest day
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Manpower by Trade (Latest)")
        latest = SAMPLE_DAILY_LOGS[-1]
        trade_df = pd.DataFrame(latest["manpower"])
        trade_df.columns = ["Trade", "Headcount", "Company"]
        st.dataframe(trade_df, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("#### Headcount Trend")
        trend_data = pd.DataFrame({
            "Date": [log["log_date"] for log in SAMPLE_DAILY_LOGS],
            "Workers": [sum(m["headcount"] for m in log.get("manpower", [])) for log in SAMPLE_DAILY_LOGS]
        })
        st.line_chart(trend_data.set_index("Date"))

# Footer
st.markdown("---")
st.caption("Procore Reports Dashboard | Built with Streamlit + Pandas | [GitHub](https://github.com/AnthonyB-316/procore-reports)")
