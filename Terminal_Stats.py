import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

st.header("Terminal Statistics App")
excel_file = st.file_uploader("Upload Terminal Stats.")


@st.cache_data
def read_excel_file(excel_file):
    df = pd.read_excel(excel_file, sheet_name="Table")
    return df


if excel_file:
    df = read_excel_file(excel_file)
    st.write(df.columns)
    ctr_operators = df["Ctr_pLine"].sort_values().unique()
    selected_cOperators = st.sidebar.multiselect(
        "Container Operators", ctr_operators, ctr_operators
    )
    selected_df = df[df["Ctr_pLine"].isin(selected_cOperators)]
    st.subheader("Sample of the Terminal Stats Sheet")
    st.dataframe(selected_df.tail())
    YTD_Moves = selected_df["Grand_Total_Moves"].sum()
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Year to date: ")
    with col2:
        st.write("{:,}".format(YTD_Moves))
