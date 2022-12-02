import streamlit as st
import openai
from ml_backend import ml_backend

st.title("Team Swastha | A Semantic Search Tool for Medical Literature")
st.text("by Dhruv Shrivastava, Pranay Panigrahi, Shrey Choudhary")

st.markdown(""" 

# About
 
## This is a search tool for medical literature powered by GPT-3 and PubMed.
## The app scrapes full-text data from PubMed, feeds it to a fine-tuned version of GPT-3 which performs semantic search depending on the query provided by the user.

""")

st.markdown("# Semantic Search")

backend = ml_backend()

with st.form(key="form"):
    prompt = st.text_input("Enter your medical query")
    st.text(f"(Example: Can Paracetamol cause Drowsiness?)")


   
    submit_button = st.form_submit_button(label='Search')

    if submit_button:
        with st.spinner("Processing results via PubMed"):
            output = backend.generate_email(prompt)
        st.markdown("# Output:")
        st.subheader(output)

       
