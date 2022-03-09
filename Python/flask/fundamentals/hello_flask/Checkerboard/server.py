from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows= 8, columns = 8, color1="black", color2 = "red")

@app.route('/<int:columns>')
def columns_only(columns):
    return render_template("index.html", rows = 8, columns=columns,color1="black", color2 = "red")

@app.route('/<int:rows>/<int:columns>')
def squares(rows,columns):
    return render_template("index.html",rows=rows,columns=columns,color1="black", color2 = "red")

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def checkerit(rows,columns,color1,color2):
    return render_template("index.html",rows=rows,columns=columns,color1=color1,color2=color2)

if __name__=="__main__":     
    app.run(debug=True)
