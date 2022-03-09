Bootstrap Things
---
---
* copy this into the head of html files
    * link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"

* Useful Bootstrap commands



Python
---
---
Python indents and spacing matter!

functions are made with
```python
def function_name():    <---optional arguments to pass in
    return
```


OOP (object oriented programming)

```python
class testclass:                        <--- all classes start with "class" followed by a given name
    def __init__(self, t, w, bal):      <--- classes all start with the constructor, what initializes the class always including "self" and any additional arguments which can default
        self.test = t                   <--- all attributes of classes start with "self." then whatever you want to call the parameter of the class
        self.we = w
        self.balance = bal

    def mytest(self):                   <--- functions always indented of the class and including the "self arguement" which = the instance of the class calling it
        pass                            <--- we can add a "pass" to the function to skip it untill we add things to it


    @classmethod                        <--- class methods always start with "@classmethod" they are just functions of the class that can run in different ways with different arguments
    def method(cls, variable):          <--- always including "cls" which = the self of the instance calling it redirected to constructor function
        return cls(4, 2, variable - 15)

user1 = testParent(1,3,20)              <--- setting the variable to the left = to the value of the right, user1 is the holder of the instance of the object testclass
user2 = testParent.tax(50)              <--- a function returns what it becomes, the .tax becomes (4,2,num) so the whole statement becomes user2 = testparent(4,2,num)
```


Flask
---
---
Server Creation

1. To create a flask server
2. create file structure
    * server.py
    * templates
        * html files here
    * statics
        * images
        * css
            * stylesheets
3. open git bash in directory
4.  type "pipenv install flask"
5.  type "pipenv shell" to start virtual environment
6.   type " 'filename'.py " to start local server

```python
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'anything here'   <---- used to store session data on local pc

@app.route('/')     <--- url address for function
def index():        <--- function to be executed on route
    return render_template('index.html')        <--- return of function, render the html at address


@app.route('/action', methods=['post'])
def reset():
    return redirect('/')        <--- redirect to a page, used for post actions to avoid resubmitting of data
```

Useful things in flask


---
1. session data is a stored dictionary of values that persists and holds data ***session['key_name']***
2. get data from forms by using request ***request.form['key_name']*** and set = to session['key_name']
    * if getting data from forms make sure route have ***methods=['post']***

```python
@app.route('/url_name', methods=['post'])
```
3. when in html use **jinja** syntax to pass data to and from the server
    * {{ double curly }} for data to be replaced by the back end
    * {% curly with percent %} for javascript functions run in the html
        * functions must end with the {% end %} {% endif %} {% endfor %} ect.. to end a function

4. variables must be initalized before being used in server by setting equal to a start value or by a function appending the key: value pair
5. session data can be .pop() .clear() .append()



MySql
---
---
Database commands
(while in the boldened database)
1. SELECT (to select the type of column of data)
2. INSERT (to add data into database)
```
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');
```
3. UPDATE (to modify values in a table, state WHERE to only update those entries
```
UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
```
4. DELETE (to delete entries from tables, add WHERE or else all data will be deleted)
    * if errors deleting add (SET SQL_SAFE_UPDATES = 0;)
```
DELETE FROM table_name WHERE condition(s)
```

MySql Functions
---
1. CONCAT(column_name1 ,column_name2) AS <-- replaces heading with--> Something FROM table_name

2.  CONCAT_WS('something between', column_name) <--adds value in between all listed items

3. LENGTH(column_name) <-- returns length of character in item

4. LOWER() <-- lowercase all values

5. HOUR(column_name) <-- returns the hour in a 24hr system

6. DAYNAME() <-- name of day

7. MONTH() <-- number of month

8. NOW() <-- time as of function run

9. DATE_FORMAT(column_name, 'date/time functions') from https://www.w3schools.com/sql/func_mysql_date_format.asp


JOIN
1. to join tables together
```
    SELECT table_name FROM parent_table JOIN child_table ON parent_table.id = child_table.foreign_id
```
* to join multiple tables add the JOIN child_table ON parent_table.id = child_table.foreign_id using the next tables in the lineup


Server Modularization
---
---
run cmd in directory
```
pipenv install flask pymysql
```
File structure
---
* project_name_app
    * config
        * mysqlconnection.py    <-- database query handler
    * controllers
        * modelname(s).py       <-- routing file for table/class
    * models
        * modelname             <-- file containing class (of table)
    * static
        * css/images/javascript subfolders
    * templates
        * containing html files
    * __ init __.py
* server.py


starter files in each section
---

mysqlconnection.py
---
```python
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database


class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
# establish the connection to the database
        self.connection = connection
# the method to query the database

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close()
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection

def connectToMySQL(db):
    return MySQLConnection(db)
```

controller
---
```python
# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.(model name goes here) import (class in model goes here)


@app.route('/')
def index():
    users = User.get_all()                                      <-- assigns the function of the class to the variable
    return render_template('index.html', my_users=users)        <-- assigns the variable to a variable we can use on the rendered page


@app.route('/create', methods=['post'])
def save():
    data = {                                            <-- assigns the data collected in the form on the page to a dictionary object 
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.save(data)                                     <-- runs the function on the class, passing in the data we just got from the form

    return redirect('/')


@app.route('/add')
def add_new_user():
    return render_template('add_new_user.html')


@app.route('/delete/<int:id>')          <-- takes the int value from the url
def delete_user(id):                    <-- passes the int value we captured from the url route
    data = {"id": id}                   <-- makes a dictionary of the key we want with the value of what we passed in
    User.delete_user(data)              <-- runs the .classmethod passing in the data dictionary we just made
    return redirect('/')


@app.route('/edit_user/<int:id>', methods=['post'])     <-- post from the html to the server
def edit_existing_user(id):
    data = {                                            <-- passing in data from forms and url capture
        "id" : id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.edit(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_user(id):
    print('editing')
    data = {'id':id}
    return render_template('edit_user.html', user=User.get_one(data))


@app.route('/show/<int:id>')
def show_user(id):
    data = {
        "id" :id
    }
    return render_template('show_user.html', single_user=User.get_one(data))
```

Models
---
```python
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB                                <-- links to the name of the currrent database to easily change all models to use a new database at same time
class User:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(MyCustomDB).query_db(query)                                <-- MyCustomDB is the name I chose as the variable that ties all 
    # Create an empty list to append our instances of users
        my_users = []                                                                       <-- can be any name for variable
    # Iterate over the db results and create instances of users with cls.
        for row in results:                                                                 <-- loops over the individual dictionaries from the database query
            my_users.append( cls(row) )                                                     <-- appends them to the list variable
        print('from the get all method')
        return my_users                                                                     <-- returns the list of dictionaries 


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name, email ,created_at , updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def delete_user(cls, data):                                     <-- data passed in from the route is an dictionary containing key: value pairings that can be used in queries
        print("delete is running")
        query = "DELETE FROM users WHERE id = %(id)s"               <-- SQL injection and sanitization, %(some value)s takes the value from the key in the data passed in
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def edit(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s'
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        return cls(results[0])                                          <-- returns the result of the query at the 1st index position in the list which is the dictionary of row 1
```

Templates
---
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>
</head>

<body>
    <h1>All Users</h1>

    {% for row in my_users %}                               <-- loops over the list of dictionaries that was passed in from the routing file in its return statement
    <p>ID: {{row.id}}</p>                                   <-- links to the current iteration in the loop of the dictionary in the list with its .attribute
    <p>First Name: {{row.first_name}}</p>
    <p>Last Name: {{row.last_name}}</p>
    <p>Occupation: {{row.email}}</p>
    <a href="/show/{{row.id}}">Show</a>
    <a href="/edit/{{row.id}}">Edit</a>
    <a href="/delete/{{row.id}}">Delete</a>
    
    <hr>
    {% endfor %}

    <a href="/add">Add new user</a>




</body>

</html>
```

dunder init
---
```python
# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"          <-- literally anything

MyCustomDB = 'users_schema'         <-- reference source for the name of the current database all model files can use
```

server.py
---
```python
# ...server.py
from flask_app import app
from flask_app.controllers import controller name(s)


if __name__ == "__main__":
    app.run(debug=True)
```


Validation
---
---
```python
@staticmethod           <-- not related to any class
def validate(data)
    is_valid = True

    if len(data["name"]) < some number:     <-- checks the length of the data
        is_valid = False
        flash("flash message","flash message label")
    
    if data["number"].isnumeric():
        if int(data["number"]) < 0:
            is_valid = False
    else is_valid = False

    if len(data["other value"]) < some number:
        is_valid = False

    return is_valid
```


```python
@app.route('/',methods=['post'])
def validation():
    if not Class.validate(request.form):            <-- if Class.validate(request.form) == False
        return render_template('/same page')

    function if is valid = true
    return 
```

```html
{% with messages = get_flashed_messages("flash message label") %}       <-- catergory_filer =       (if wanting to only include certain labels)
    {% if messages %}
        {% for message in messages %}
        <p>{{message}}</p>
        {% endfor %}
    {% endif %}
{% endwith %}
```
Valid patterns
---
* using regular expressions from the the regex module
* import re (into the models file)
```python
from flask_app.models.user import User
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')





    
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

```


Password hashing
---
1. pipenv install flask-bcrypt
2. into the class files
    * from flask_bcrypt import Bcrypt
    * from flask_app import app
    * bcrypt = Bcrypt(app)

3. use in class methods involving saving to database
```python
@classmethod
def savefunction(cls,data)
    password variable = bcrypt.generate_password_hash(data["password"])
    user variable = {
        "first_name": data["first_name"],
        "password": password variable,
    }
    query =
    return connectToMySQL(database name).query_db( query, user variable )
```
Login
---
```python
@classmethod
def validate_login(cls, data):
user_in_db = User.get_by_email(data)

if not user_in_db:
    flash("invalid Email/Password")
    return False

if not bcrypt.check_password_hash(user_in_db.password, data["password"]):
    flash("invalid Email/Password")
    return False

return True
```