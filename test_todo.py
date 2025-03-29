import pytest
from todo import ToDoList

def test_add_task():
    todo = ToDoList()
    todo.add_task("Buy milk")
    assert "Buy milk" in todo.get_tasks()

def test_remove_task():
    todo = ToDoList()
    todo.add_task("Buy milk")
    todo.remove_task("Buy milk")
    assert "Buy milk" not in todo.get_tasks()
