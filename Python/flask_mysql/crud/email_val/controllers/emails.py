from flask import render_template, session, redirect, request
from email_val import app
from email_val.models.email import Email

#index page
@app.route('/')
def index():
    return render_template('index.html')

#check existing emails and save them
@app.route('/process',methods=['POST'])
def check_emails():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')


#successful email
@app.route('/success')
def email_success():
    return render_template('success.html',all_emails=Email.all_emails())

#delete email
@app.route('/destroy/<int:id>')
def destroy_email(id):
    data= {
        'id':id
    }
    Email.destroy(data)
    return redirect('/')