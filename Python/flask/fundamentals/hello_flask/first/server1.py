from timeit import repeat
from flask import Flask 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response    # Run the app in debug mode.
# import statements, maybe some other routes
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello " + name.capitalize() + "!"

@app.route('/repeat/<int:num>/<repeat>')
def say_hello(num,repeat):
    return f"<p>{repeat}</p>" * num

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
