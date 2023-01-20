import json
from flask import Flask, request



with open('users.json') as f:
    users = json.load(f)
    f.close()

with open('todos.json') as f:
    todos = json.load(f)
    f.close()


app = Flask(__name__)


@app.route('/users')
def get_users():
    return users

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    return users[user_id-1]

@app.route('/users/<int:user_id>/todo')
def get_todo_by_user_id(user_id):
    user_todos = []
    for todo in todos:
        if todo['userId'] == user_id:
            user_todos.append(todo)
    return user_todos

@app.route('/users', methods = ['POST'])
def criar_user():
    data = request.get_json()
    data['id'] = len(users) + 1
    users.append(data)
    return data, 201

@app.route('/todos')
def get_todos():
    return todos

@app.route('/todos/<int:todo_id>')
def get_todo_by_id(todo_id):
    return todos[todo_id-1]

@app.route('/todos/<int:todo_id>/user')
def get_user_by_todo_id(todo_id):
    user_id = todos[todo_id]['userId']
    return users[user_id-1]

@app.route('/todos', methods = ['POST'])
def criar_todos():
    data = request.get_json()
    data['id'] = len(todos) + 1
    todos.append(data)
    return data, 201





if __name__ == '__main__':
    app.run(debug=True, port = 5000)