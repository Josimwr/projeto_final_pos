from flask import Flask, request, render_template
import users
import todos

app = Flask(__name__)

users_api = users.Users()
todos_api = todos.Todos()

@app.route('/users')
def index():
    users = users_api.get_users()
    return render_template('users.html', users = users)

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = users_api.get_user_by_id(user_id)
    return render_template('user.html', user = user)

@app.route('/users/novo')
def novo_user():
    return render_template('novo_user.html')

@app.route('/users', methods = ['POST'])
def criar_user():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    user = {
        'name': name,
        'username': username,
        'email': email
    }
    users_api.criar_user(user)
    return 'Concluido'

@app.route('/todos')
def get_todos():
    todos = todos_api.get_todos()
    return render_template('todos.html', todos = todos)

@app.route('/todos/<int:todo_id>')
def get_todo_by_id(todo_id):
    todo = todos_api.get_todo_by_id(todo_id)
    return render_template('todo.html', todo = todo)

@app.route('/todos/novo')
def novo_todo():
    return render_template('novo_todo.html')

@app.route('/todos', methods = ['POST'])
def criar_todo():
    title = request.form['title']
    completed = request.form['completed']
    userId = request.form['userId']
    todo = {
        'userId': userId,
        'title': title,
        'completed': completed
    }
    todos_api.criar_todo(todo)
    return 'Concluido'



if __name__ == '__main__':
    app.run(debug=True, port = 5001)