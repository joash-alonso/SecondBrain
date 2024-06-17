import streamlit as st
from components import text_visualiser, text_editor
import ollama


with st.form("Ask a question:"):
    question = st.text_area("Ask an LLM: ")
    submitted = st.form_submit_button("Generate Answer")
    if submitted:
        with st.spinner("Generating response..."):
            st.session_state.response = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    },
                ],
            )
        with st.spinner("Extracting Ideas..."):
            st.session_state.keywords = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "user",
                        "content": f"""Given the following text, extract the keywords and abstract ideas that can be found. Return a python dictionary with key being 'keywords' and value being the keywords.

                        Text: {st.session_state.response['message']['content']}
                        """,
                    },
                ],
            )

            st.write(st.session_state.keywords['message']['content'])

    if 'response' and 'keywords' in st.session_state:
        text_editor(question, st.session_state.response['message']['content'], keywords=st.session_state.keywords['message']['content'])

cols = st.columns(4)

if 'content' in st.session_state:
    for i in range(4):
        with cols[i]:
            text_visualiser(st.session_state.content, 'Title', ["keyword1", "keyword2", "keyword3"])
