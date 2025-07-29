# 🚗 Car Rental Webpage Project

A simple and functional Car Rental Webpage built using **Flask (Python)** for backend, **SQLite** for database, and **HTML & CSS** for frontend. This project allows users to view available cars, sign up, log in, and book a car. It’s designed for learning and demo purposes.

---

## 🔍 Project Features

- 👤 User Signup and Login System
- 🚘 Display of Available Cars from the Database
- 📝 Car Booking Form with Customer Details
- 💾 Data Stored and Fetched using SQLite
- 🎨 Basic Styling with HTML and CSS (no frameworks used)
- 🧹 Simple and clean codebase, easy to understand for beginners

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Database:** SQLite
- **Others:** Jinja Templates (for rendering HTML with dynamic data)

---

## 📁 Project Structure

car-rental-webpage/
│
├── static/
│ └── style.css # CSS styles
│ └── images/ # Car images
│
├── templates/
│ └── home.html # Landing Page
│ └── login.html # Login Page
│ └── signup.html # Signup Page
│ └── cars.html # Available Cars Page
│ └── book.html # Booking Form Page
│ └── success.html # Confirmation Page
│
├── app.py # Main Flask App
├── config.py # Database Config
├── car_rental.db # SQLite Database
└── README.md # Project Description

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/car-rental-webpage.git
cd car-rental-webpage
2. Set Up a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
3. Install Dependencies
bash
Copy
Edit
pip install flask
4. Run the Flask App
bash
Copy
Edit
python app.py
5. Open in Browser
Visit: http://127.0.0.1:5000



