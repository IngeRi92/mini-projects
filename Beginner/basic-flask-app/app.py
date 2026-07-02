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


if __name__ == "__main__":
    app.run(debug=True)