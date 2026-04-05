import streamlit as st
import pandas as pd
import plotly.express as px

# page title
st.title("Sample Data Dashboard")

# load data
df = pd.read_csv("data/NBA3.csv")

# show dataframe
st.subheader("Raw Data")
st.dataframe(df)

# dropdown selection
column = st.selectbox("Select a column to visualize", df.columns)
