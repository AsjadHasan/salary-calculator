import streamlit as st
import pandas as pd
from datetime import datetime, time

st.set_page_config(page_title="Work Time & Salary Calculator", layout="wide")

st.title("⏱️ Work Time & Salary Calculator")

# Sidebar inputs for rates
st.sidebar.header("Settings")
regular_rate = st.sidebar.number_input("Regular Hourly Rate (¥)", value=1350, step=50)
overtime_rate = st.sidebar.number_input("Overtime Hourly Rate (¥)", value=1687, step=50)

st.subheader("Daily Work Entry")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Regular Work")
    in_time = st.time_input("In Time", value=time(9, 15))
    out_time = st.time_input("Out Time", value=time(17, 0))

with col2:
    st.markdown("### Overtime Work")
    ot_in = st.time_input("Overtime In Time", value=time(17, 30))
    ot_out = st.time_input("Overtime Out Time", value=time(19, 30))

# Calculations
reg_hours = max(0.0, (datetime.combine(datetime.today(), out_time) - datetime.combine(datetime.today(), in_time)).total_seconds() / 3600.0)
ot_hours = max(0.0, (datetime.combine(datetime.today(), ot_out) - datetime.combine(datetime.today(), ot_in)).total_seconds() / 3600.0)

reg_salary = reg_hours * regular_rate
ot_salary = ot_hours * overtime_rate
total_salary = reg_salary + ot_salary

st.markdown("---")
st.subheader("📊 Calculation Summary")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Regular Hours", f"{reg_hours:.2f} hrs")
m2.metric("Overtime Hours", f"{ot_hours:.2f} hrs")
m3.metric("Regular Salary", f"¥{reg_salary:,.0f}")
m4.metric("Overtime Salary", f"¥{ot_salary:,.0f}")

st.success(f"### Total Daily Earnings: ¥{total_salary:,.0f}")
