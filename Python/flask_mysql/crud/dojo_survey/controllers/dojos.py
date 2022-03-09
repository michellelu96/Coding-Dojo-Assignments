from dojo_survey.models.dojo import Dojo
from dojo_survey import app
from flask import render_template,request, redirect,flash


#show main page
@app.route('/')
def index():
    return render_template('index.html')

#get and validate info
@app.route('/user/info',methods=['POST'])
def user_info():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    if len(name) < 3:
        flash("Name must be more than 3 letters")
        return redirect('/')
    if len(comments) < 3:
        flash("Comments must be more than 3 letters")
        return redirect('/')
    if len(comments) > 120:
        flash("Comments cannot be greater than 120 characters!")
        return redirect('/')
    return render_template('result.html', name=name, location=location, language=language, comments=comments)
