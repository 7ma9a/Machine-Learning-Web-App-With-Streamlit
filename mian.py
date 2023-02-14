import streamlit as st
st.title("Streamlit Example")

st.write("""
# Explore different classifier
Which one is the best?
""")
dataset_names = st.selectbox("Select dataset",("Iris","Breast Cancer","ًWine Dataset"))
st.write(dataset_names)
