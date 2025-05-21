
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import load_and_clean_data

st.set_page_config(page_title="Solar Dashboard", layout="wide")

# Load data
df = load_and_clean_data()

# Sidebar Filters
st.sidebar.title("Filter Data")
countries = st.sidebar.multiselect(
    "Select countries", options=df["Country"].unique(), default=df["Country"].unique()
)
metric = st.sidebar.selectbox("Select metric", ["GHI", "DNI", "DHI"])

# Filtered Data
filtered_df = df[df["Country"].isin(countries)]

# Main
st.title(" Solar Energy Dashboard")
st.write("This dashboard allows you to compare solar irradiance across West African countries.")

# Boxplot
st.subheader(f"Boxplot of {metric}")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y=metric, ax=ax)
st.pyplot(fig)

# Top Summary Table
st.subheader(f"Average {metric} by Country")
summary = (
    filtered_df.groupby("Country")[metric]
    .agg(["mean", "median", "std"])
    .round(2)
    .reset_index()
)
st.dataframe(summary)
