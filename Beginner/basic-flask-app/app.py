from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Õpi Flaski", "done": False},
    {"id": 2, "title": "Tee README", "done": False},
]
next_id = 3


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/hello/<name>")
def hello(name):
    return f"Tere, {name}!"


@app.route("/hello", methods=["GET", "POST"])
def hello_form():
    if request.method == "POST":
        name = request.form["username"]
        return render_template("hello.html", name=name)
    return render_template("form.html")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return render_template("tasks.html", tasks=tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    title = request.form["title"]
    tasks.append({"id": next_id, "title": title, "done": False})
    next_id += 1
    return redirect(url_for("get_tasks"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("get_tasks"))


@app.route("/tasks/<int:task_id>/done", methods=["POST"])
def toggle_task_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    return redirect(url_for("get_tasks"))


if __name__ == "__main__":
    app.run(debug=True)
