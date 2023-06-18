import streamlit as st

# Set page title and description
st.set_page_config(page_title="About Us", page_icon=":bank:",
                   layout="wide", initial_sidebar_state="collapsed")
st.title("About XYZ Bank")
st.write("Welcome to XYZ Bank! We are a community-focused bank that has been serving our customers for over 50 years. Our mission is to provide our customers with the best possible banking experience and to support our local communities through charitable giving and volunteer work.")

# Display bank history
st.header("Our History")
st.write("XYZ Bank was founded in 1970 by John Smith, a local businessman who wanted to create a bank that put customers first. Over the years, we have grown to become one of the largest banks in the region, with branches in over 50 locations. We are proud of our history and the role we have played in supporting the growth and development of our communities.")

# Display bank leadership
st.header("Our Leadership")
st.write("At XYZ Bank, we are committed to providing our customers with the best possible service. Our leadership team is made up of experienced banking professionals who are dedicated to ensuring that our customers receive the support and guidance they need to achieve their financial goals. Meet our leadership team below:")

# Display leadership team photos and bios
st.container()
with st.expander("John Smith - CEO"):
    st.image("https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y29ycG9yYXRlJTIwbWFufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60", width=200)
    st.write("John Smith has been the CEO of XYZ Bank since its founding in 1970. With over 40 years of experience in banking, John is a respected leader in the industry and is known for his commitment to customer service and community involvement.")

with st.expander("Jane Doe - President"):
    st.image("https://images.unsplash.com/photo-1615136002804-166c5961414e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTR8fGNvcnBvcmF0ZSUyMG1hbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", width=200)
    st.write("Jane Doe joined XYZ Bank in 2005 and has served as President since 2015. With over 20 years of experience in banking, Jane is an expert in commercial lending and has helped many local businesses grow and thrive.")

with st.expander("Michael Johnson - Chief Financial Officer"):
    st.image("https://images.unsplash.com/flagged/photo-1553642618-de0381320ff3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGNvcnBvcmF0ZSUyMG1hbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", width=200)
    st.write("Michael Johnson has been the CFO of XYZ Bank since 2010. With a background in accounting and finance, Michael is responsible for managing the bank's finances and ensuring that we are able to provide our customers with the best possible rates and services.")