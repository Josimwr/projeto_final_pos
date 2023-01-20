import requests

class Todos:
    base_url = 'http://localhost:5000/todos'

    def get_todos(self):
        return requests.get(self.base_url).json()

    def get_todo_by_id(self, todo_id):
        return requests.get(f"{self.base_url}/{todo_id}").json()

    def criar_todo(self, todo):
        return requests.post(self.base_url, json = todo).json()