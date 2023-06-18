import streamlit as st

def show_contact_us_page():
    st.header("Contact Us")
    st.subheader("Address")
    st.write("Global Trust Bank, 4321 Bayview Street, Horizon City, NY, USA, 10001 - Where Banking Meets Excellence")
    st.write("")
    st.image("http://2.bp.blogspot.com/-3cGvU1mPhyE/UebnaRwBiPI/AAAAAAAAFsY/p70UtNw8-1c/s1600/IMG_0092.PNG", use_column_width=True)

    st.subheader("Telephone")
    st.write("+1 (123) 456-7890")

    st.subheader("Email")
    st.write("info@bankwebsite.com")

show_contact_us_page()
