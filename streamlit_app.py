import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------------- AUTO REFRESH ----------------
st_autorefresh(interval=2000, limit=100, key="refresh")

st.title("📊 Smart Attendance Dashboard")

# ---------------- DATE ----------------
date = datetime.now().strftime("%d-%m-%Y")

file_path = f"Attendance/Attendance_{date}.csv"

# ---------------- LOAD CSV ----------------
if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    st.success(f"Attendance for {date}")
    st.dataframe(df)

    st.info(f"Total Records: {len(df)}")

else:
    st.warning("No attendance recorded yet.")
    st.dataframe(pd.DataFrame(columns=["NAME", "TIME"]))