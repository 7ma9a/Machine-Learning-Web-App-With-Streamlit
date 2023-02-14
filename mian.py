import streamlit as st
st.title("Streamlit Example")

st.write("""
# Explore different classifier
Which one is the best?
""")
dataset_names = st.sidebar.selectbox("Select dataset",("Iris","Breast Cancer","ًWine Dataset"))

classifier_name = st.sidebar.selectbox("Select Classifier",("KNN","SVM","Random Forest"))
