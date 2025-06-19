import streamlit as st

st.title("Which language offers the highest level of human readability in programming?")

col1, col2= st.columns(2)

with col1:
    st.header("Python")
    st.image("https://admin.wac.co/uploads/Features_Of_Python_1_f4ccd6d9f7.jpg", width=200)

    vote1=st.button("Vote Python")

with col2:
    st.header("Java")
    st.image("https://miro.medium.com/v2/resize:fit:600/1*fOdb_ET1sOd4uZStK4E8HA.jpeg", width= 200)
    vote2=st.button("Vote Java")

if vote1:
    st.success("That's Correct")

elif vote2:
    st.success("you're wrong")

name=st.sidebar.text_input("Enter your name") 

expert=st.sidebar.selectbox("Programming Language you often work with?",["Python", "Java Script","C Sharp", "C++","Java"]) 

st.write(f"Welcome {name}! Glad to know your language choice of {expert}") 
 
with st.expander("Best way to learn coding"):
    st.write("""
1-Build small projects regularly.\n
2-Focus on logic, not just syntax.\n
3-Explore tutorials, docs, and communities\n
""")

       