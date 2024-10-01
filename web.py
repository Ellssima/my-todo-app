import streamlit as st
import function

todos = function.get_todos()
def add_todo():
     todo = st.session_state['new_todo'] + '\n'
     todos.append(todo)
     function.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity.')


for i, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=f'todo_{i}')
    if checkbox:
        todos.pop(i)
        function.write_todos(todos)
        if f'todo_{i}' in st.session_state:
            del st.session_state[f'todo_{i}']
        st.rerun()

st.text_input(label='Enter todo',  on_change=add_todo, key='new_todo', placeholder='Add new todo...',
              label_visibility='hidden')





