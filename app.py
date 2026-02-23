"""
Procore Reports - Streamlit Dashboard
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from sample_data import SAMPLE_RFIS, SAMPLE_SUBMITTALS, SAMPLE_DAILY_LOGS

st.set_page_config(page_title="Procore Reports", layout="wide")

st.title("Procore Reports")
st.caption("RFI aging, submittal status, and manpower tracking")

tab1, tab2, tab3 = st.tabs(["RFI Aging", "Submittals", "Manpower"])

# RFI Aging
with tab1:
    st.subheader("RFI Aging Report")
    
    today = datetime.now()
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
            "RFI #": rfi["number"],
            "Subject": rfi["subject"],
            "Status": rfi["status"].upper(),
            "Ball In Court": rfi.get("ball_in_court", {}).get("name", "Unknown"),
            "Due Date": due_date,
            "Days Open": days_open,
            "Overdue": "YES" if is_overdue else ""
        })
    
    df_rfi = pd.DataFrame(rfi_data).sort_values("Days Open", ascending=False)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total RFIs", len(df_rfi))
    col2.metric("Open", len(df_rfi[df_rfi["Status"] == "OPEN"]))
    col3.metric("Overdue", len(df_rfi[df_rfi["Overdue"] == "YES"]))
    
    st.dataframe(df_rfi, use_container_width=True, hide_index=True)

# Submittals
with tab2:
    st.subheader("Submittal Status Report")
    
    sub_data = []
    for sub in SAMPLE_SUBMITTALS:
        sub_data.append({
            "Submittal #": sub["number"],
            "Title": sub["title"],
            "Spec Section": sub.get("spec_section", ""),
            "Status": sub["status"].upper().replace("_", " "),
            "Submitted By": sub.get("submitted_by", {}).get("name", "Unknown"),
            "Due Date": sub.get("due_date", "")
        })
    
    df_sub = pd.DataFrame(sub_data)
    
    status_counts = df_sub["Status"].value_counts()
    cols = st.columns(len(status_counts))
    for i, (status, count) in enumerate(status_counts.items()):
        cols[i].metric(status, count)
    
    st.dataframe(df_sub, use_container_width=True, hide_index=True)

# Manpower
with tab3:
    st.subheader("Weekly Manpower Report")
    
    mp_data = []
    total_manpower = 0
    weather_delays = 0
    
    for log in SAMPLE_DAILY_LOGS:
        day_total = sum(m["headcount"] for m in log.get("manpower", []))
        total_manpower += day_total
        if log.get("weather_delay"):
            weather_delays += 1
        
        mp_data.append({
            "Date": log["log_date"],
            "Weather": log.get("weather", ""),
            "Delay": "YES" if log.get("weather_delay") else "",
            "Headcount": day_total,
            "Notes": log.get("notes", "")
        })
    
    df_mp = pd.DataFrame(mp_data)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Days Logged", len(SAMPLE_DAILY_LOGS))
    col2.metric("Total Manpower", total_manpower)
    col3.metric("Weather Delays", weather_delays)
    
    st.dataframe(df_mp, use_container_width=True, hide_index=True)

st.divider()
st.caption("Demo data - connect to Procore API for live project data")
