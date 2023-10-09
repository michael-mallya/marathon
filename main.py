from flask import Flask, render_template,request,redirect,flash 
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__,template_folder='website/templates',static_folder='website/static')
app.jinja_env.auto_reload = True
app.config["SECRET_KEY"]="kumamoto"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marathon.db"
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullName = db.Column(db.String(100))
    phoneNumber = db.Column(db.String(10))
    jersey = db.Column(db.String(10))
    kilometer = db.Column(db.String(10))
    package = db.Column(db.String(10))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
     return render_template('index.html')

@app.route("/donate")
def donate():
     return render_template('donate.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
     if request.method == 'POST':
        fullName = request.form['fullName']
        phoneNumber= request.form['phoneNumber']
        jersey = request.form['jersey']
        kilometer = request.form['kilometer']
        package = request.form["package"]
        new_values = User(fullName=fullName,phoneNumber=phoneNumber,jersey=jersey,kilometer=kilometer,package=package)
        db.session.add(new_values)
        db.session.commit()
        return "record created"
     return render_template('register.html') 

if __name__ == '__main__':
    app.run()