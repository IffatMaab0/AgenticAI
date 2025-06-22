import streamlit as st
from datetime import date
import pandas as pd
import os


## INTRO
st.title("Coding Journey")
st.text(" Logic will get you from A to Z; imagination will get you everywhere.")

##Import date
today = date.today()

## taking input from user
task = st.text_input("Enter Task")
understanding = st.text_area("What i understood")
confused = st.text_area("What confused me")

# File name where diary entries will be stored
file = "Coding_Diary.csv"

if st.button("Save Entry"):
    # If all fields are empty, show a warning
    if task.strip() == "" and understanding.strip() == "" and confused.strip() == "":
        st.warning("Write something, even intentions matter. So write what you decided to do but couldn't")
    else:
         # Create a new entry as a DataFrame
        entry = pd.DataFrame([{"Date": today,"Task Tried": task, "Understanding": understanding,"Confusion": confused}])

     # If file already exists, read old data and add new entry to it
    if os.path.exists(file):
        preData= pd.read_csv(file) 
        df = pd.concat([preData, entry], ignore_index= True)

    else:   
        # If file doesn't exist, this is the first entry    
        df = entry

    # Save updated data to CSV file    
    df.to_csv(file ,index= False)
    st.success("Progress Saved")

# Display section: Show entries if file exists    
if os.path.exists(file):
    st.subheader("Progress Report")
    df = pd.read_csv(file)

    for index, row in  df.iterrows():
        with st.expander(f"{row['Date']} - {row['Task Tried']}"):
            st.write(f"**Understanding:** {row['Understanding']}")
            st.write(f"**Confusion** {row['Confusion']}")

            # If delete button is clicked for this entry
            if st.button("Delete", key= f"Delete_{index}"):
                df = df.drop(index)
                df.to_csv(file, index= False)
                st.warning("Entry deleted")
                st.stop()       # Stop app to refresh and show change

# If file doesn't exist yet (no entries made)            
else:   
    st.info("No file founded")  

        


