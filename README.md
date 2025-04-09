# EventHub - College Event Management Platform 🎪

## Introduction 🚀
EventHub is a Python-based web application designed to streamline event management for college students. It provides separate interfaces for administrators and regular users, featuring event creation, winner announcements, and an Instagram-like display layout.

## Project Overview ✨
A Flask-powered web app that allows:
- 👨‍💼 *Admins* to create/manage events and winners
- 👩‍🎓 **Students** to view upcoming events and past winners
- 📱 Responsive design with Instagram-like card layouts
- 🔐 Authentication system with role-based access

## Key Features 🌟
- 🖼️ Image uploads for events
- 📅 Event scheduling and management
- 🏆 Winners announcement section
- 👥 User registration and authentication
- 📱 Mobile-friendly responsive design

## App Structure 🏗️
EventHub/
├── app.py                # Flask application entry point
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Uploaded event/winners images
├── templates/            # HTML templates
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

## Installation & Setup ⚙️

### Prerequisites
- Python 3.8+
- pip package manager
- Modern web browser

### Steps
1. **Clone the repository**
   git clone https://github.com/yourusername/EventHub.git
   cd EventHu

2. **Create virtual environment** (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**
   pip install -r requirements.txt

4. **Run the application**
   python app.py

5. **Access in browser**
   ```
   http://localhost:5000
   ```

## Screenshots 📸
*(Add your screenshots here after setup)*

## Folder Structure 📂
EventHub/
├── app.py                # Main Flask application
├── static/
│   ├── css/
│   │   └── style.css     # All CSS styles
│   ├── js/
│   │   ├── script.js     # Main JavaScript
│   │   ├── login.js      # Login functionality
│   │   └── register.js   # Registration functionality
│   └── images/           # Stores uploaded images
├── templates/
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── admin.html        # Admin dashboard
│   ├── user.html         # User dashboard
│   ├── events.html       # Events page
│   └── winners.html      # Winners page
└── README.md             # This documentation file
```

## Demo Credentials 🔑
- **Admin Account** 👨‍💼
  - Username: `admin`
  - Password: `admin123`

- **User Account** 👩‍🎓
  - Username: `user1`
  - Password: `user123`

## Technologies Used 💻
- 🐍 Python 3
- 🌶️ Flask
- 🗃️ localStorage/sessionStorage
- 💄 HTML5 & CSS3
- 🟨 JavaScript (ES6)
- 🎨 Responsive Design

## Author 👨‍💻
**Sathvik**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github)](https://github.com/yourusername)  

