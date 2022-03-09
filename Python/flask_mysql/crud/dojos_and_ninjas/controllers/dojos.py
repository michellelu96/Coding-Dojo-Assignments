from dojos_and_ninjas import app
from flask import render_template, session, redirect, request
from dojos_and_ninjas.models.dojo import Dojo

# show all dojos
@app.route("/")
@app.route("/dojos")
def all_dojo():
    return render_template("all_dojos.html", all_dojos=Dojo.all_dojos())


# add a dojo
@app.route("/add_dojo", methods=["POST"])
def add():
    Dojo.add_dojo(request.form)
    return redirect("/dojos")


@app.route("/dojos/<int:id>")
def ninja_in_dojo(id):
    data = {
        'id':id
    }
    return render_template('all_ninjas_in_dojo.html',dojo=Dojo.get_dojo_ninjas(data))