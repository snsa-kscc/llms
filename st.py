import streamlit as st

st.title('Example title')

file_uploader = st.file_uploader("Upload your File", type=['txt'])

if file_uploader is not None:
    st.write('Upload')


