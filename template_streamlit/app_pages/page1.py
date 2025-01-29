import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO

st.markdown("# Page 1 🎉")
st.markdown("Upload new Data")


@st.dialog("Upload CSV")
def upload_csv():
    st.write("Please upload a csv file")
    st.session_state.uploaded_file = st.file_uploader("CSV File", type=["csv", "tsv"], key="file_upload")
    if st.button("Submit"):
        st.rerun()


if st.button("upload csv"):
    upload_csv()

if "uploaded_file" in st.session_state and st.session_state.uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(st.session_state.uploaded_file)
    st.markdown(f"Newly Uploaded File: **{st.session_state.uploaded_file.name}**")
    st.dataframe(dataframe)


st.page_link("app_pages/home.py", label="Go Home")
