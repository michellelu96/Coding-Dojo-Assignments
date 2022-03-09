import random
from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = 'hi'

@app.route('/')
def page():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    if 'attempt' not in session:
        session['attempt'] = 0
    return render_template('index.html')

@app.route('/num',methods=['GET','POST'])
def guess():
    session['guess']= int(request.form['guess'])
    if session['attempt'] <=5:
        if session['guess'] > session['num']:
            session['alert']= "high"
            session['attempt']+=1
            return redirect('/')
        elif session['guess'] < session['num']:
            session['alert']= "low"
            session['attempt']+=1
            return redirect('/')
        elif session['guess'] == session['num']:
            session['alert']= 'right'
            session['attempt']+=1
            return redirect('/')
    elif session['attempt'] == 5:
        session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    
