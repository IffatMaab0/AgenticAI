import streamlit as st

st.title("Hello Programmer!")
st.subheader("Programming Language...")
st.text("Leo's first interective app")


lang=st.selectbox("Choose your favorite language",["Python", "Java Script","C Sharp", "C++","Java"])

st.write(f"You Choose {lang}. Good!")
st.success("your choice has been considered")
