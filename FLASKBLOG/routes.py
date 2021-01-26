from flask import render_template, url_for,flash,redirect,request
from FLASKBLOG import app, db, bcrypt
from FLASKBLOG.forms import RegistrationForm,LoginForm
from FLASKBLOG.models import User
import sqlite3 as sql

posts = [
    {
        'author':'Denis muriuki',
        'title':'Blog post 1',
        'content':'Global Macro',
        'date_posted':'July 24,2019'
    }
]



@app.route ("/")
@app.route ("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='about')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            username=request.form['username']
            email=request.form['email']
            password=request.form['hashed_password']

        
            with sql.connect("Site.db") as con:
                cur = con.cursor()

            cur.execute("INSERT INTO User (username,email,password) VALUES (?,?,?)",(username,email,password))

            con.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error insert operation"
        finally:
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        return render_template("register.html",title='Register',form=form )
        con.close()
    return render_template("register.html",title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    con = sql.connect("Site.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM User")

    rows = cur.fetchall()
    
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!','success')
    elif form.email.data == 'johndoe@test.com' and form.password.data == 'test1234':
                flash('You have been logged in!','success')
                return redirect(url_for('home'))
    else:
            flash('Login unsuccessful.please check username and password','danger')
    return render_template("login.html",title='Login',form=form )

