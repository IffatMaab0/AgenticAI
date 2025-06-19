import streamlit as st
import pandas as pd

st.title("Coffee Sales Dashboard")
file = st.file_uploader("Upload your csv file ",type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
if file:
    st.subheader("Stats Summary of Coffe Sales")
    st.write(df.describe())    