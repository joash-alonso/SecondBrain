import streamlit as st
from content import TITLE, EDIT_REDIRECT_TEXT, REVIEW_REDIRECT_TEXT, INSTRUCTIONS_REDIRECT_TEXT

st.set_page_config(page_title="Second Brain", page_icon="🧠", layout="wide")

st.markdown(
    f"<h1 style='text-align: center; color: white;'>{TITLE}</h1>",
    unsafe_allow_html=True,
)


col_left, col_center, col_right = st.columns([1, 1, 1])

with col_left:
    st.markdown(
        f"<h2 style='text-align: center; color: white;'>{EDIT_REDIRECT_TEXT}</h2>",
        unsafe_allow_html=True,
    )
    edit = st.button("Build Your Brain")
    if edit:
        st.switch_page("pages/01_Build_Your_Brain.py")


with col_center:
    st.markdown(
        f"<h2 style='text-align: center; color: white;'>{REVIEW_REDIRECT_TEXT}</h2>",
        unsafe_allow_html=True,
    )
    connections = st.button("See The Connections")
    if connections:
        st.switch_page("pages/02_See_The_Connections.py")


with col_right:
    st.markdown(
        f"<h2 style='text-align: center; color: white;'>{INSTRUCTIONS_REDIRECT_TEXT}</h2>",
        unsafe_allow_html=True,
    )
    instructions = st.button("Instructions")
    if connections:
        st.switch_page("pages/03_Instructions.py")
