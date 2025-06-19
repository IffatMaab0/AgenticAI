import streamlit as st
from datetime import date
st.title("Lets Calculate your age..")

dob=st.date_input("Enter your Date of Birth: ", min_value= date(1900,1,1) , max_value= date(2050,12,31))

today=date.today()
age= today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age=age-1
   
st.success(f"your age is: {age}; You must be doing great, Good Luck!")    
