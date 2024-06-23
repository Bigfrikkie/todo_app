import pytest
import asyncio
from src.todo_app import TodoApp

@pytest.mark.asyncio
async def test_create_todo():
    app = TodoApp.new()
    todo_id = await app.create("Test todo")
    assert todo_id == 1
    assert app.todos[todo_id]["description"] == "Test todo"

@pytest.mark.asyncio
async def test_update_todo():
    app = TodoApp.new()
    todo_id = await app.create("Test todo")
    updated = await app.update(todo_id, "Updated test todo")
    assert updated is True
    assert app.todos[todo_id]["description"] == "Updated test todo"

@pytest.mark.asyncio
async def test_delete_todo():
    app = TodoApp.new()
    todo_id = await app.create("Test todo")
    deleted = await app.delete(todo_id)
    assert deleted is True
    assert todo_id not in app.todos

@pytest.mark.asyncio
async def test_complete_todo():
    app = TodoApp.new()
    todo_id = await app.create("Test todo")
    completed = await app.complete(todo_id)
    assert completed is True
    assert app.todos[todo_id]["completed_on"] is not None

@pytest.mark.asyncio
async def test_filter_partial_text_search():
    app = TodoApp.new()
    await app.create("Test todo one")
    await app.create("Another test todo")
    results = await app.filter("partial_text_search", "test")
    assert len(results) == 2

@pytest.mark.asyncio
async def test_filter_completed():
    app = TodoApp.new()
    await app.create("Test todo one")
    await app.create("Another test todo")
    await app.complete(1)
    results = await app.filter("completed")
    assert len(results) == 1
    assert results[0]["id"] == 1

@pytest.mark.asyncio
async def test_filter_todo():
    app = TodoApp.new()
    await app.create("Test todo one")
    await app.create("Another test todo")
    await app.complete(1)
    results = await app.filter("todo")
    assert len(results) == 1
    assert results[0]["id"] == 2
