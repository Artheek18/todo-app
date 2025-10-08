import streamlit as st
from streamlit import session_state

import functions
from functions import get_todos, write_todos

todos = get_todos()

def add_todos():
    todo = st.session_state.get('new_todo', '').strip()
    if not todo:
        st.toast("Nothing to add"); return

    todo = st.session_state['new_todo']
    todos.append(todo + "\n")
    functions.write_todos(todos)



#st.set_page_config(page_title="To-Do", page_icon="🗒️", layout="wide")
st.title("A To-Do Web App")
st.subheader("To-Do")
st.caption("Simple, fast, and pretty.")

st.text_input(label="Enter your todo", placeholder="Add a To-Do...",
              on_change=add_todos, key='new_todo')


with st.container(height=500, border=True):
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del session_state[todo]
            st.rerun()
