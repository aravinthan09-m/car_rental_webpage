from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
from config import DATABASE
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        conn.close()

        if user:
            session['username'] = username
            flash('Login successful!')
            return redirect('/cars')
        else:
            flash('Invalid credentials. Try again.')
            return redirect('/login')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        user_exists = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user_exists:
            flash('Username already taken. Try another.')
            return redirect('/signup')
        
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        flash('Signup successful! Please login.')
        return redirect('/login')
    
    return render_template('signup.html')


@app.route('/cars')
def available_cars():
    conn = connect_db()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template('available_cars.html', cars=cars)

@app.route('/book/<int:car_id>', methods=['GET', 'POST'])
def book_car(car_id):
    # Add booking logic
    return render_template('book_car.html', car_id=car_id)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        conn = connect_db()
        conn.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        conn.execute('''CREATE TABLE cars (id INTEGER PRIMARY KEY, name TEXT, image TEXT, price TEXT)''')
        conn.execute('''CREATE TABLE bookings (id INTEGER PRIMARY KEY, car_id INTEGER, user TEXT, date TEXT)''')
        conn.execute("INSERT INTO cars (name, image, price) VALUES ('Honda City', 'honda.jpg', '₹1500/day')")
        conn.execute("INSERT INTO cars (name, image, price) VALUES ('Hyundai i20', 'i20.jpg', '₹1200/day')")
        conn.execute("INSERT INTO cars (name, image, price) VALUES ('Toyota Fortuner', 'fortuner.jpg', '₹2500/day')")
        conn.commit()
        conn.close()
    app.run(debug=True)
