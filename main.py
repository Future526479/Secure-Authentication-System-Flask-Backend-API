from flask import Flask, render_template, session, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bcrypt import Bcrypt
import sqlite3
import os

# APP CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret-key")
crypt = Bcrypt(app)

# DATABASE CONNECTION
def get_db():
    return sqlite3.connect('Database.db')

# DATABASE SETUP
with get_db() as con:
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS UserInfo (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            email TEXT,
            password TEXT
        )
    ''')
    con.commit()

# FORMS
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

# DATABASE HELPERS
def get_user_by_email(email):
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM UserInfo WHERE email = ?", (email,))
    output = cur.fetchone()
    con.close()
    return output 

# LOGIN ROUTE
@app.route('/', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        Email = form.email.data
        Password = form.password.data
        user = get_user_by_email(Email)
        if user and crypt.check_password_hash(user[4], Password):
            session["user_id"] = user[0]
            session["user_name"] = user[1]
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password", "danger")
    return render_template('login.html', form=form)

# REGISTER ROUTE
@app.route('/Sign', methods=['POST','GET'])
def Sign():
    form = RegisterForm()
    if form.validate_on_submit():
        Name = form.name.data
        Surname = form.surname.data
        Email = form.email.data
        Password = form.password.data
        if get_user_by_email(Email):
            flash("Email already exists", "warning")
            return redirect(url_for("Sign"))
        hashed_password = crypt.generate_password_hash(Password).decode("utf-8")
        con = get_db()    
        cur = con.cursor()
        cur.execute("""INSERT INTO UserInfo (name, surname, email, password) VALUES (?,?,?,?)""", (Name, Surname, Email, hashed_password))     
        con.commit()
        con.close()
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))
    return render_template("Sign.html", form=form)

# DASHBOARD (PROTECTED)
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("Dashboard.html", name=session["user_name"])

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

# RUN SERVER
if __name__ == '__main__':
    app.run()