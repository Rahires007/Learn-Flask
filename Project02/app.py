from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def About():
    return render_template('About.html')

@app.route('/Skills')
def Skills():
    Languages=["C","C++","Python","Java","C#","Sql"]
    Databases=["Mysql","Oracle"]
    Frameworks=["Django","Flask"]
    Library="React"
    WebTech=["HTML","CSS","JS"]
    Tools=["Vs Code","Git & Github ","Netlify & Vercel ","Virtual Box & Docker "]
    return render_template('Skills.html',Languages=Languages,Databases=Databases,Frameworks=Frameworks,Library=Library,WebTech=WebTech,Tools=Tools)

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')