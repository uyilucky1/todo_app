import streamlit as st
import functions



st.title('This a todo app')

todos = functions.get_todo_list()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todo_list(todos)


st.button('Click me')



for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='enter your task', on_change=add_todo, key='new_todo')

