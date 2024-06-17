import streamlit as st
from uuid import uuid4
from typing import List
from streamlit_quill import st_quill

def text_editor(title: str, text: str, keywords: List[str]):
    with st.container():
        st.title(title)
        st_quill(text)
        st.multiselect(
            label="Keywords", options=keywords, default=keywords
        )


def text_visualiser(text: str, title: str, keywords: List[str]):
    with st.container():
        st.text_area(title, text, key=f"ta_{uuid4}")
        st.multiselect(
            label="Keywords", options=keywords, default=keywords
        )
