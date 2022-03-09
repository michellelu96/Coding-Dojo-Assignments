from dojos_and_ninjas import app
from flask import render_template, session, redirect, request
from dojos_and_ninjas.models.ninja import Ninja
from dojos_and_ninjas.models.dojo import Dojo

# create ninja page
@app.route("/ninjas")
def create_user_page():
    return render_template("new_ninja.html",all_dojos=Dojo.all_dojos())

#create new ninja
@app.route('/ninjas/new',methods=['POST'])
def new_ninja():
    print(request.form)
    Ninja.add_new_ninja(request.form)
    return redirect('/dojos')
