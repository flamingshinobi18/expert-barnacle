import streamlit as st

# Set the title of the page and center it
st.set_page_config(page_title="World Bank", page_icon=":bank:", layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 50px;'>World Bank</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-size: 40px;'>A Leading Financial Institution</h2>", unsafe_allow_html=True)

st.write("##")
st.write("##")
st.write("##")


# Set the background image and opacity
st.markdown(
    """
    <style>
        body {
            background-image: url('https://c4.wallpaperflare.com/wallpaper/718/734/522/reflection-sea-hong-kong-night-vector-hd-wallpaper-preview.jpg');
            background-size: cover;
            opacity: 0.7;
        }

        .footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
            margin-top: 50px;
        }

        .button {
            font-size: 1.2em;
            font-weight: bold;
            color: white;
            background-color: #0077c2;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            margin-right: 20px;
            cursor: pointer;
        }

        .button:hover {
            background-color: #005c99;
        }

        .button:active {
            transform: translateY(2px);
        }

        .section {
            margin-top: 50px;
            margin-bottom: 50px;
        }

        .section-header {
            font-size: 2.5em;
            font-weight: bold;
            color: #0077c2;
            margin-bottom: 20px;
        }

        .section-text {
            font-size: 1.2em;
            line-height: 1.5;
            color: #333;
        }

        .section-image {
            max-width: 100%;
            height: auto;
            margin-top: 20px;
        }

        .video {
            max-width: 100%;
            height: auto;
            margin-top: 50px;
        }

        .caption {
            font-size: 0.8em;
            color: #999;
            margin-top: 10px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the navigation bar
nav_options = ["Home", "About Us", "Projects", "Contact Us"]
nav_choice = st.sidebar.selectbox("Navigate", nav_options)

#


# Display the appropriate content based on the user's choice
#if nav_choice == "Home":
   # st.header("Welcome to our Bank")
    #st.write("This is the home page of my website.")
#elif nav_choice == "About Us":
   # st.header("About Us")
   # st.write("This is the About Us page.")
#elif nav_choice == "Project":
   # st.header("Project")
   # st.write("This is the Project page.")
#else:
    #st.header("Contact Us")
    #st.write("This is the Contact Us page.")

# Set the main body of the page
import streamlit as st

import streamlit as st

st.write("""
<span style="font-size:28px; font-weight:bold">Welcome to World Bank</span><br><br>
<span style="font-size:22px">We are a leading financial institution dedicated to helping our customers achieve their financial goals.</span><br><br>
<span style="font-size:22px">At World Bank, we offer a wide range of services, including:</span><br><br>
""", unsafe_allow_html=True)

# Deposit Accounts

st.write("""
<div style="text-align: center;">
<span style="font-size:24px; font-weight:bold;">Deposit Accounts</span><br><br>
<span style="font-size:20px;">Choose from our range of deposit accounts to suit your savings goals and financial needs.</span>
</div><br>
""", unsafe_allow_html=True)
st.write("##")

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://cdn.pixabay.com/photo/2017/09/07/08/54/money-2724241__340.jpg' width='400' alt='Money'>"
    "</div>",
    unsafe_allow_html=True,
)


st.write("##")
st.write("##")
st.write("##")

# Loans

st.write("""
<div style="text-align: center">
<span style="font-size:24px; font-weight:bold">Loans</span><br><br>
<span style="font-size:20px">Get the financing you need with our flexible and competitive loan options.</span>
</div><br>
""", unsafe_allow_html=True)
st.write("##")

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://cdn.pixabay.com/photo/2020/02/18/08/35/finance-4858797_960_720.jpg' width='400' alt='Money'>"
    "</div>",
    unsafe_allow_html=True,
)
st.write("##")
st.write("##")
st.write("##")

# Credit Cards

st.write("""
<div style="text-align: center">
<span style="font-size:24px; font-weight:bold">Credit Cards</span><br><br>
<span style="font-size:20px">Choose from our range of credit cards and enjoy a host of benefits and rewards.</span>
</div><br>
""", unsafe_allow_html=True)
st.write("##")

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://cdn.pixabay.com/photo/2017/03/13/17/26/ecommerce-2140603__340.jpg' width='400' alt='Money'>"
    "</div>",
    unsafe_allow_html=True,
)
st.write("##")
st.write("##")
st.write("##")



# Financial Planning and Wealth Management

st.write("""
<div style="text-align: center">
<span style="font-size:24px; font-weight:bold">Financial Planning and Wealth Management</span><br><br>
<span style="font-size:20px">Take control of your financial future with our comprehensive financial planning and wealth management services.</span>
</div><br>
""", unsafe_allow_html=True)
st.write("##")

st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://cdn.pixabay.com/photo/2017/05/04/16/37/meeting-2284501__340.jpg' width='400' alt='Money'>"
    "</div>",
    unsafe_allow_html=True,
)
st.write("##")
st.write("##")
st.write("##")

# Footer
st.write("""
<div style="text-align: center">
<span style="font-size:20px">Our team of experienced professionals is here to help you make informed decisions about your finances and provide personalized solutions to meet your unique needs.</span><br><br>
<span style="font-size:20px">Thank you for choosing World Bank. We look forward to helping you achieve your financial goals.</span>
</div>
""", unsafe_allow_html=True)









# Add buttons for different services
#st.write("")
#st.write("")
#st.write("")
#st.button("Services")
#st.write("")
#st.button("Payment Transfer")
#st.write("")
#st.button("Fixed Deposit")
#st.write("")
#st.button("E-Service")
#st.write("")
#st.button("My Account")