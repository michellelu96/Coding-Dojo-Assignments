from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect("/user")


# get all users
@app.route("/user")
def all_users():
    users = User.get_all_users()
    print(users)
    return render_template("read_all.html", all_users=users)


# create user page
@app.route("/user/new")
def create_user_page():
    return render_template("create.html")


# create the new user
@app.route("/user/create", methods=["POST"])
def create():
    print(request.form)
    User.create_user(request.form)
    return redirect("/user")


# get one user to update
@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("update.html", user=user)


# show one person only
@app.route("/user/show/<int:id>")
def show(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("one_user.html", user=user)


# update the users
@app.route("/user/update", methods=["POST"])
def update():
    print(request.form)
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)
    return redirect("/user")


# delete the user
@app.route("/user/delete/<int:id>")
def delete_user(id):
    data = {"id": id}
    User.delete_user(data)
    return redirect("/user")

if __name__ == "__main__":
    app.run()
