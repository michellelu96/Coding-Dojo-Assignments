from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = 'hi'



@app.route('/')
def count():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 1
    return render_template("index.html",count=session['visit'])

@app.route('/',methods=['POST'])
def reset():
    if request.method == "POST":
        session.clear()
    return redirect('/')
        
# would only add one... could'nt get to work
#@app.route('/',methods=['GET'])
#def add():
#    nums= request.form['quantity']
#    if request.method ==  'GET':
#        session['visit'] += nums
#    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    
