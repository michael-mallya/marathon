from flask import Flask, render_template,request,redirect,flash 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 
import africastalking
load_dotenv()
app=Flask(__name__,template_folder='website/templates',static_folder='website/static')
app.jinja_env.auto_reload = True
app.config["SECRET_KEY"]="kumamoto"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marathon.db"
db = SQLAlchemy(app)
# Initialize SDK
username = "afyayaakili"  # use 'sandbox' for development in the test environment
api_key = "21615bdc6aebdbeaeea2610e134f2bc34dd94aca4081300cf6556e52df4a47be"  # use your sandbox app API key
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS

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
        phoneNumber = request.form['phoneNumber']
        jersey = request.form['jersey']
        kilometer = request.form['kilometer']
        package = request.form["package"]
        
        # Validate and format the phone number to start with +255
        if not phoneNumber.startswith("+255"):
            phoneNumber = "+255" + phoneNumber
        
        new_values = User(fullName=fullName, phoneNumber=phoneNumber, jersey=jersey, kilometer=kilometer, package=package)
        db.session.add(new_values)
        db.session.commit()
        
        # Send an SMS notification
        message = f"Hello, you have registered with Afya ya akili marathon"
        response = sms.send(message, [phoneNumber])
        
        # Flash a message to indicate successful registration
        flash("Registration successful! You will receive an SMS notification shortly.")
        return redirect("/register")
    
    return render_template('register.html')
if __name__ == '__main__':
    import os
    from werkzeug.middleware.proxy_fix import ProxyFix

    workers = os.cpu_count() * 2 + 1 if os.cpu_count() else 1
    bind_address = "0.0.0.0:8000"

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
    app.run(host="0.0.0.0", port=8000)
