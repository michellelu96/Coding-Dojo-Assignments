from flask import Flask, session
app = Flask(__name__,template_folder='templates')
app.secret_key = "hi"