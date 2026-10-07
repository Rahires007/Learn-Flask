from flask import Flask,render_template

app=Flask(__name__)

#Rendering HTML Templates using render_template function
@app.route('/')
def Home():
    return render_template('Home.html')

#Rendering message as responce
@app.route('/response')
def Response():
    return "Welcome !... "
