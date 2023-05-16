import streamlit as st
import pandas as pd
import numpy as np
import os

#Page heading
st.header("🍺🍸Check All Pubs by Location🍺🍸")

#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR1,"open_pubs_clean.csv")
df = pd.read_csv(dir_of_interest)

#Display Pub Locations by Zip Code, Local Authority
unique=['All','Post Code', 'Local Authority','Pub Name']

option=st.radio(label="Select Below Option to See the Available Pubs",
                options=unique, horizontal=False)

if option=='Post Code':
    selected=st.selectbox(label='Select the ZipCode',options=df['postcode'].unique())
    st.subheader(f"Total Pubs Found : {df[df['postcode']==selected].shape[0]}")
    st.map(data=df[df['postcode']==selected],  use_container_width=True)
elif option=='Pub Name':
    selected=st.selectbox(label='Select the Pub Name',options=df['name'].unique())
    st.subheader(f"Total Pubs Found : {df[df['name']==selected].shape[0]}")
    st.map(data=df[df['name']==selected],  use_container_width=True)
elif option=='Local Authority':
    selected=st.selectbox(label='Select Local Authority',options=df['local_authority'].unique())
    st.subheader(f"Total Pubs Found : {df[df['local_authority']==selected].shape[0]}")
    st.map(data=df[df['local_authority']==selected],  use_container_width=True)
else:
    st.subheader(f"Total Pubs Found : {df.shape[0]}")
    st.map(data=df,  use_container_width=True)