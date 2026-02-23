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

    /* Card-style metrics */
    [data-testid="stMetric"] {
        background: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    [data-testid="stMetricValue"] {
        color: #2D3E50;
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
    [data-testid="stSidebar"] .stMarkdown {
        color: #fff;
    }
    [data-testid="stSidebar"] .stSelectbox label {
        color: #fff;
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
    st.metric("Active RFIs", "5")
    st.metric("Pending Submittals", "3")

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
            "Ball In Court": rfi.get("ball_in_court", {}).get("name", ""),
            "Due Date": due_date,
            "Days Open": days_open,
            "Overdue": "OVERDUE" if is_overdue else ""
        })

    df = pd.DataFrame(rfi_data).sort_values("Days Open", ascending=False)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total", len(df))
    col2.metric("Open", len(df[df["Status"] == "OPEN"]))
    col3.metric("Closed", len(df[df["Status"] == "CLOSED"]))
    col4.metric("Overdue", len(df[df["Overdue"] == "OVERDUE"]))

    st.markdown("####")

    # Style the dataframe
    def highlight_overdue(row):
        if row["Overdue"] == "OVERDUE":
            return ["background-color: #FFEBEE"] * len(row)
        return [""] * len(row)

    styled_df = df.style.apply(highlight_overdue, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

elif tool == "Submittals":
    st.markdown("## Submittals")

    sub_data = []
    for sub in SAMPLE_SUBMITTALS:
        sub_data.append({
            "#": sub["number"],
            "Title": sub["title"],
            "Spec Section": sub.get("spec_section", ""),
            "Status": sub["status"].upper().replace("_", " "),
            "Submitted By": sub.get("submitted_by", {}).get("name", ""),
            "Due Date": sub.get("due_date", "")
        })

    df = pd.DataFrame(sub_data)

    # Status counts
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Approved", len(df[df["Status"] == "APPROVED"]))
    col2.metric("Pending", len(df[df["Status"] == "PENDING"]))
    col3.metric("Revise & Resubmit", len(df[df["Status"] == "REVISE RESUBMIT"]))
    col4.metric("Rejected", len(df[df["Status"] == "REJECTED"]))

    st.markdown("####")

    def color_status(val):
        colors = {
            "APPROVED": "background-color: #E8F5E9; color: #2E7D32",
            "PENDING": "background-color: #FFF3E0; color: #E65100",
            "REVISE RESUBMIT": "background-color: #FFF8E1; color: #F57F17",
            "APPROVED AS NOTED": "background-color: #E3F2FD; color: #1565C0",
            "REJECTED": "background-color: #FFEBEE; color: #C62828"
        }
        return colors.get(val, "")

    styled_df = df.style.applymap(color_status, subset=["Status"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

else:  # Daily Log
    st.markdown("## Daily Log")

    mp_data = []
    total_workers = 0

    for log in SAMPLE_DAILY_LOGS:
        day_total = sum(m["headcount"] for m in log.get("manpower", []))
        total_workers += day_total

        mp_data.append({
            "Date": log["log_date"],
            "Weather": log.get("weather", ""),
            "Delay": "Yes" if log.get("weather_delay") else "",
            "Workers": day_total,
            "Notes": log.get("notes", "")
        })

    df = pd.DataFrame(mp_data)

    col1, col2, col3 = st.columns(3)
    col1.metric("Days Logged", len(df))
    col2.metric("Total Workers", total_workers)
    col3.metric("Weather Delays", len(df[df["Delay"] == "Yes"]))

    st.markdown("####")

    # Highlight delays
    def highlight_delay(row):
        if row["Delay"] == "Yes":
            return ["background-color: #FFF3E0"] * len(row)
        return [""] * len(row)

    styled_df = df.style.apply(highlight_delay, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

    # Trade breakdown for latest day
    st.markdown("#### Manpower by Trade (Latest)")
    latest = SAMPLE_DAILY_LOGS[-1]
    trade_df = pd.DataFrame(latest["manpower"])
    trade_df.columns = ["Trade", "Headcount"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(trade_df, use_container_width=True, hide_index=True)
    with col2:
        st.bar_chart(trade_df.set_index("Trade"))
