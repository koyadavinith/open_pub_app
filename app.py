import streamlit as st
import os
import pandas as pd
import time
from matplotlib import image
from pub_locations import show_pub_locations
from nearest_pubs import show_nearest_pubs

st.set_page_config(layout="wide")  # Set the page configuration

def main():
    # Add a sidebar to navigate between pages
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Pub Locations", "Nearest Pubs"))

    # Display the selected page based on the user's choice
    if page == "Home":
        show_home_page()
    elif page == "Pub Locations":
        show_pub_locations()
    elif page == "Nearest Pubs":
        show_nearest_pubs()

def show_home_page():
    #Load data
    FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
    dir_of_interest = os.path.join(FILE_DIR1,"open_pubs_clean.csv")
    pub_img = os.path.join(FILE_DIR1,"pub.jpeg")

    st.title(':white[TO FIND THE NEAREST PUBS IN UK]')
    st.subheader( " My self : ***:green[Koyada Vinith]***")
    st.snow()


    st.subheader(":red[You can reach me]")

    col1,col2,col3=st.columns(3, gap='small')
    with col1:
        st.subheader("[LinkedIn](https://www.linkedin.com/in/koyadavinith/)")
    with col2:
        st.subheader("[GitHub](https://github.com/koyadavinith)")



    df = pd.read_csv(dir_of_interest)

    #Page Heading
    st.header("🍾All Pubs Information in United Kingdom🍸")

    with st.expander(label='Click Here to see the dataset overview',expanded=False):
        img1 = image.imread(pub_img)
        st.image(img1)
        st.balloons()
        st.dataframe(df)


    #Unique Bars and Local Authorities
    unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

    option=st.radio(label="Select below options to see total count",
                    options=unique,label_visibility="visible", horizontal=True)

    if option=='Number of Pubs':
        st.subheader(f"Total Pubs in UK: :blue[{df['name'].nunique()}]")
    elif option=='Number of Postal Code':
        st.subheader(f"Total Post Codes in UK: :blue[{df['postcode'].nunique()}]")
    else:
        st.subheader(f"Total Local Authorities in UK :blue[{df['local_authority'].nunique()}]")

    st.subheader(":red[🥂🍹Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind and stories to be told🥂🍹.]")

if __name__ == "__main__":
    main()
