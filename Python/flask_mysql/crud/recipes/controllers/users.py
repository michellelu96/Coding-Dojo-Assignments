from recipes import app
from flask_bcrypt import Bcrypt
from flask import redirect,session,request,flash,render_template
from recipes.models.user import User
from recipes.models.recipe import Recipe
bcrypt = Bcrypt(app)


#main page
@app.route('/')
def index():
    return render_template('index.html')


#register +validation
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if not User.validate_register(request.form):
            print("invalid")
            return redirect('/')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email": request.form['email'],
            "password" : pw_hash}
        id =User.save(data)
        session['user_id'] = id
        return redirect("/success")
    return redirect('/')

#check logins+ validation
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
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
    return render_template('dashboard.html',user_info=User.get_by_id(data),all_recipes=Recipe.all_recipes(),user_recipes=User.get_all_user(data))

#logout the user
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')