# Please see the README for more information
# Written by Jun Han Huang, May 2023. 

import streamlit as st
import pandas as pd
import psycopg2 as pg
import os
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# Initialize Streamlit page
st.set_page_config(
    page_title="Bioreactor Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
 )

# Get environment variables
DBNAME = os.environ.get('POSTGRES_DB')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
USER = os.environ.get('POSTGRES_USER')
PORT = os.environ.get('POSTGRES_PORT')
HOST = os.environ.get('POSTGRES_HOST')

# establishes connection to postgres database, returns psycopg2 connection object.
@st.cache_resource
def init_connection():
    connection_URI = HOST+"://"+USER+":"+PASSWORD+"@postgres:"+PORT+"/"+DBNAME
    return pg.connect(connection_URI)


# Executes a SQL query upon the connected database
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query: str) -> pd.DataFrame:
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Takes in a dataframe as input and returns its converted csv string.
# Uses st.cache_data so not to re-run on every refresh.
@st.cache_data
def convert_df(df: pd.DataFrame) -> str:
    return df.to_csv().encode('utf-8')

if __name__ == '__main__':
    # connect to database
    conn = init_connection()

    # read and store database data
    temp_df = pd.DataFrame(run_query("SELECT * from " + '"CM_HAM_DO_AI1/Temp_value"' +";"), columns=['Time', 'Temperature'])
    ph_df = pd.DataFrame(run_query("SELECT * from " + '"CM_HAM_PH_AI1/pH_value"' +";"), columns=['Time', 'pH'])
    oxy_df = pd.DataFrame(run_query("SELECT * from " + '"CM_PID_DO/Process_DO"' +";"), columns=['Time', 'Oxygen'])
    psi_df = pd.DataFrame(run_query("SELECT * from " + '"CM_PRESSURE/Output"' +";"), columns=['Time', 'Pressure'])

    #----------mainpage----------
    st.title(":bar_chart: Bioreactor Metrics Dashboard")
    st.markdown("##")

    # set graph title and size
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(20)
    fig.suptitle('Bioreactor 1', fontsize=16)

    # plots for temperature
    ax1 = plt.subplot(221)
    # database returns time as a datetime object. We have to remove the uncessary date info before plotting.
    # this must be repeated for each plot.
    plt.plot(temp_df["Time"].dt.strftime('%H:%M'), temp_df["Temperature"])
    plt.tick_params('x')
    ax1.set_ylabel("Temperature (C)")

    # plots for pH
    ax2 = plt.subplot(222, sharex=ax1)
    plt.plot(ph_df["Time"].dt.strftime('%H:%M'), ph_df["pH"])
    plt.tick_params('x')
    ax2.set_ylabel("pH")

    # plots for oxygen
    ax3 = plt.subplot(223, sharex=ax1)
    plt.plot(oxy_df["Time"].dt.strftime('%H:%M'), oxy_df["Oxygen"])
    plt.tick_params('x')
    ax3.set_ylabel("Oxygen (%)")
    ax3.set_xlabel("Time in HH:MM")

    # plots for Pressure
    ax4 = plt.subplot(224, sharex=ax1)
    plt.plot(psi_df["Time"].dt.strftime('%H:%M'), psi_df["Pressure"])
    ax4.set_xlabel("Time in HH:MM")
    ax4.set_ylabel("Pressure (PSI)")
    
    # sets x-axis scale
    # our data is in the time range of 0-6 hours, so we use 360 minutes as the end of x-axis
    plt.xlim(0, 360)
    plt.xticks(np.linspace(0,360,12))
    st.pyplot(plt,use_container_width=False)


    #----------sidebar----------
    # convert from dataframe to .csv
    temp_csv = convert_df(temp_df)
    psi_csv = convert_df(psi_df)
    oxy_csv = convert_df(oxy_df)
    pH_csv = convert_df(ph_df)

    st.sidebar.header("Download Data as CSV:")
    # creates a download button for each metric.
    with st.sidebar:
        st.download_button(
            label="Download Temperature Data",
            data=temp_csv,
            file_name='temp_df.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Download pH Data",
            data=pH_csv,
            file_name='pH_df.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Download Oxygen Data",
            data=oxy_csv,
            file_name='oxy_df.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Download Pressure Data",
            data=psi_csv,
            file_name='psi_df.csv',
            mime='text/csv',
        )