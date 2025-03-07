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

