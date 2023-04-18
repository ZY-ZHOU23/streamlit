import streamlit as st

# python -m streamlit run app.py

st.title('Title of the Application')
st.markdown('something **bold**')

st.sidebar.title('title of sidebar')

side_check = st.sidebar.checkbox('Click Me')
if side_check:
    st.sidebar.write('Hello')

