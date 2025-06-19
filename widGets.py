import streamlit as st      # Importing Streamlit library for building the web app

st.title("Talk Like a Dev")      # Main title of the app

# Button for(press/click)
if st.button("I am Programmer"):
    st.success("Let's talk code")

# Checkbox to ask if user loves programming    
lang_love=st.checkbox("Do you love programming?") 
if lang_love:
    st.write("The Chat is going to be interesting!")

# Radio buttons to select from given options
Dev_Type=st.radio("What's your technical domain",["Web Developer","Data Scientist","Syber Security","Agentic AI"]) 

# Dropdown to select favorite programming language
lang=st.selectbox("Favorite Programming Language: ",["Python","Java Script","C Sharp", "C++","Java"])

# Slider to rate energy level dedicated to coding
energy=st.slider("How much of your energy you put in coding", 0,100,50)
st.write(f"{energy}, That's enough, if you are doing honestly")

# Number input for total languages learned
st.number_input("How many languages you have learnt so far", min_value = 0 , max_value = 50, step= 1)

# Text input to get user's name
name=st.text_input("What's your good name?")
if name:
    st.write(f"{name}, it's interesting to know more about you")

##for date of birth    
dob= st.date_input("When did you start coding?" , min_value = 2000 , max_value = 2050)    
          
