import streamlit as st

st.title('CAMPUSx')

col1, col2 = st.columns(2)

with col1:
    st.image('mobile_logo1.png')
with col2:
    st.write("""lorem50sajd;ffffffffffffffffffff;uqrrrrrrrrrrrrrrrrrrrrrnafbbbbbbbbbbbbbbdhhhhhhhhhhhhhhhhhhueeeeeeeeeeeeeeeeyralf""")

st.header('courses offered')
st.subheader('data science and ML/AI')
st.subheader('data analysis')
st.subheader('SQL')

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")

option = st.sidebar.selectbox("Select 0ne",['teacher', 'student'])
btn = st.sidebar.button('select')

if btn:
    st.title('Hello '+ option)