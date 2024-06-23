import asyncio
from datetime import datetime
from typing import List, Dict, Optional

class TodoApp:
    def __init__(self):
        self.todos: Dict[int, Dict] = {}
        self.current_id = 1

    @staticmethod
    def new():
        return TodoApp()

    async def create(self, description: str) -> int:
        todo_id = self.current_id
        self.todos[todo_id] = {
            "id": todo_id,
            "description": description,
            "created_on": datetime.now(),
            "completed_on": None
        }
        self.current_id += 1
        return todo_id

    async def update(self, todo_id: int, description: Optional[str] = None) -> bool:
        if todo_id in self.todos:
            if description is not None:
                self.todos[todo_id]["description"] = description
            return True
        return False

    async def delete(self, todo_id: int) -> bool:
        if todo_id in self.todos:
            del self.todos[todo_id]
            return True
        return False

    async def complete(self, todo_id: int) -> bool:
        if todo_id in self.todos:
            self.todos[todo_id]["completed_on"] = datetime.now()
            return True
        return False

    async def filter(self, criteria: str, value: Optional[str] = None) -> List[Dict]:
        if criteria == "partial_text_search":
            return [todo for todo in self.todos.values() if value.lower() in todo["description"].lower()]
        elif criteria == "completed":
            return [todo for todo in self.todos.values() if todo["completed_on"] is not None]
        elif criteria == "todo":
            return [todo for todo in self.todos.values() if todo["completed_on"] is None]
        return []
