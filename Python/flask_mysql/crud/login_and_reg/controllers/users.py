from login_and_reg import app
from flask_bcrypt import Bcrypt
from flask import redirect,session,request,flash,render_template
from login_and_reg.models.user import User
bcrypt = Bcrypt(app)

#main page
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/success')
    return render_template('register.html')


#register user
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        print("invalid")
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash}
    user_id =User.save_user(data)
    session['user_id'] = user_id
    return redirect("/success")

#validate and login user
@app.route('/login', methods=['POST'])
def login():
    data = { 
            "email" : request.form["email"] 
            }
    user= User.get_by_email(data)
    if not User.validate_login(request.form):
        return redirect('/')
    session['user_id']= user.id
    return redirect('/success')

#user dashboard, successful login!
@app.route('/success')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    return render_template('welcome.html',user_info=User.get_by_id(data))

#logout user!
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


