import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transfrom your files between excel and CSV formats with built-in data cleaning and visualization")

uploadFiles = st.file_uploader("Upload the file to convert", type=["csv", "xlsx"], accept_multiple_files=True)

if uploadFiles:
    for file in uploadFiles:
        fileExt = os.path.splitext(file.name)[-1].lower()

        if uploadFiles == "csv":
            df = pd.read_csv(file)
        elif uploadFiles == "xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format {fileExt}")
            continue

        st.write(f"**File Name** {file.name}")
        st.write(f"**File Size** {file.size}")

        st.write("Preview the Head of Data Frame")
        st.dataframe(df.head())

        st.subheader("Data cleaning options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates for {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed!")
                
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df [numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")

        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        st.subheader("Data Visualization")