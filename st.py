import streamlit as st

st.title('Example title')
st.title('Example title more')
st.title('Example title more more')

file_uploader = st.file_uploader("Upload your File", type=['txt'])

if file_uploader is not None:
    st.write('Upload')


