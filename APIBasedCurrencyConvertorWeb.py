import streamlit as st   
import requests as re       ##for making HTTP requests

amount= st.number_input("Enter the amount ")


options = st.selectbox("Select the Country", ["BSD","SLE","KRW","JEP","USD","INR"])


if st.button("Convert"):
    url= "https://api.exchangerate-api.com/v4/latest/PKR"
    response= re.get(url)          ##connects to API server,receives JSON data


    if response.status_code==200:     ##200 → is a special code that means Success!

        data = response.json()             ##converts the response from a raw string into a Python dictionary.

        rate= data["rates"][options]       

        converted= rate * amount

        st.success(f"{amount} in PKR is equal to {converted: .2f} of {options}")


    else:
        st.error("Failed to fetch conversion rate")      ##if web server don't return 200
