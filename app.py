from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append({'description': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['description'] = request.form['task']
    return redirect(url_for('index'))

@app.route('/clear_completed')
def clear_completed():
    global tasks
    tasks = [task for task in tasks if not task['completed']]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
