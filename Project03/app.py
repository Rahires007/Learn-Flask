from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#Configure Database 
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///Students.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Connect database to Flask app
db=SQLAlchemy(app)

#Model Creation & Schema Creation
class Students(db.Model):
    Id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(100))
    Class=db.Column(db.String(100))
    City=db.Column(db.String(100))
    def __repr__(self):
        return self.Name

#Automatically Create Database
with app.app_context():
    db.create_all()

#Create Route & View for Dashboard 
#Read Data
@app.route('/')
def Dashboard():
    students=Students.query.all()
    return render_template('Dashboard.html',students=students)

#Add Students 
#Add Data
@app.route('/Form',methods=["GET","POST"])
def Form():
    if request.method=="POST":
        Id=request.form.get("Id")
        Name=request.form.get("Name")
        Class=request.form.get("Class")
        City=request.form.get("City")
        student=Students(Id=Id,Name=Name,Class=Class,City=City)
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    return render_template('Form.html')

#Delete Data
@app.route('/Delete/<int:Id>')
def Delete(Id):
    student=Students.query.get_or_404(Id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

#Edit Data
@app.route('/Edit/<int:Id>',methods=["GET","POST"])
def Edit(Id):
    student=Students.query.get_or_404(Id)
    if request.method=="POST":
        Name=request.form.get("Name")
        Class=request.form.get("Class")
        City=request.form.get("City")
        student.Name=Name
        student.Class=Class
        student.City=City
        db.session.commit()
        return redirect('/')
    else:
        return render_template('Edit.html',student=student)