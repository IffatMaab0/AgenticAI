import streamlit as st

st.title("Talk Like a Dev")
if st.button("I am Programmer"):
    st.success("Let's talk code")
lang_love=st.checkbox("Do you love programming?") 
if lang_love:
    st.write("The Chat is going to be interesting!")
Dev_Type=st.radio("What's your technical domain",["Web Developer","Data Scientist","Syber Security","Agentic AI"]) 
lang=st.selectbox("Favorite Programming Language: ",["Python","Java Script","C Sharp", "C++","Java"])
energy=st.slider("How much of your energy you put in coding", 0,100,50)  
st.write(f"{energy}, That's enough, if you are doing honestly")
st.number_input("How many languages you have learnt so far", min_value = 0 , max_value = 50, step= 1)
name=st.text_input("What's your good name?")
if name:
    st.write(f"{name}, it's interesting to know more about you")
dob= st.date_input("When did you start coding?" , min_value = 2000 , max_value = 2050)    
          
