import streamlit as st

st.title("Water Reminder 💧")
st.write("Don't forget to hydrate!")

if st.button("Remind Me!"):
    st.success("Go drink a glass of water now!")
