import streamlit as st
from streamlit import session_state

import functions
from functions import get_todos, write_todos

st.markdown("""
    <style>
    /* Global page adjustments */
    .block-container {
        max-width: 650px;
        padding-top: 2rem;
    }

    div.stButton > button:first-child {
        background-color: #22c55e;  /* Emerald green */
        color: white;
        border: none;
        height: 2.6em;
        border-radius: 6px;
        font-weight: 600;
        transition: 0.3s;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button:first-child:hover {
        background-color: #16a34a; /* darker on hover */
        transform: scale(1.02);
    }

    /* Text input focus effect */
    div[data-baseweb="input"] input {
        border: 2px solid #22c55e;
        border-radius: 6px;
    }

    /* Checkbox style */
    div[data-baseweb="checkbox"] label {
        font-size: 1rem !important;
        padding: 3px 0px;
    }
    </style>
""", unsafe_allow_html=True)


todos = get_todos()

def add_todos():
    raw = st.session_state.get('new_todo', '')
    todo = raw.strip()
    if not todo:
        st.toast("Nothing to add"); return
    if any(t.strip().lower() == todo.lower() for t in todos):
        st.toast("Already on your list"); return
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""
    st.toast("Added ✔️")

st.title("A To-Do Web App")
st.subheader("To-Do")
st.caption("Simple, fast, and pretty.")

c1, c2 = st.columns([1, 0.22])
with c1:
    st.text_input(
        "Enter your todo",
        placeholder="Add a To-Do...",
        key="new_todo",
        on_change=add_todos,
        label_visibility="collapsed"
    )
with c2:
    st.button("Add", use_container_width=True, on_click=add_todos)

st.write("")  # spacing
with st.container(height=525, border=True):
    if not todos:
        st.caption("Nothing here yet! Add your first task above.")
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo.strip(), key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.toast("Task completed!")
            st.rerun()

st.divider()
st.caption("Simple To-Do Thanks to Streamlit.")