# IMPORTING LIBRARIES
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
import streamlit as st

st.title('Predict Patient Survival based on helath details')
st.subheader('Upload the patient health data: (.csv)')
# creating a side bar
st.sidebar.info("Created By : Sandeep Kirwai")
# Adding an image to the side bar
st.sidebar.subheader("Contact Information : ")
col1, mid, col2 = st.sidebar.beta_columns([1, 1, 20])
with col1:
    st.sidebar.subheader("LinkedIn : ")
with col2:
    st.sidebar.markdown(
        "[![Linkedin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLsu_X_ZxDhuVzjTHvk4eZOmUDklreUExhlw&usqp=CAU)](https://www.linkedin.com/in/sandeep-kirwai-2888bb72/)")

col3, mid, col4 = st.sidebar.beta_columns([1, 1, 20])
with col3:
    st.sidebar.subheader("Github : ")
with col4:
    st.sidebar.markdown(
        "[![Github](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJGtP-Pq0P67Ptyv3tB7Zn2ZYPIT-lPGI7AA&usqp=CAU)](https://github.com/sndpkirwai)")

# if the user chooses to upload the data
file = st.file_uploader('Dataset')
# browsing and uploading the dataset (strictly in csv format)
dataset = pd.DataFrame()
flag = False

if file is not None:

    dataset = pd.read_csv(file)
    # flag is set to true as data has been successfully read
    flag = "True"
    st.header('**HIGGS BOSON DATA**')
    st.write(dataset.head())
    # dataset.drop("EventId", axis=1, inplace=True)

    st.subheader("Shape of dataset")
    st.write(dataset.shape)

