from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configuration for file uploads
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Dummy credentials
users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user1': {'password': 'user123', 'role': 'user'}
}

# Dummy data for events and winners
events = [
    {'id': 1, 'title': 'Tech Symposium', 'description': 'Annual technical symposium showcasing student projects', 
     'image': 'tech_symposium.jpeg', 'date': '2023-11-15'},
    {'id': 2, 'title': 'Cultural Fest', 'description': 'Inter-college cultural festival with music and dance competitions', 
     'image': 'cultural_fest.jpg', 'date': '2023-12-05'},
    {'id': 3, 'title': 'Sports Day', 'description': 'Annual sports competition between departments', 
     'image': 'sports_day.jpg', 'date': '2024-01-20'}
]

winners = [
    {'id': 1, 'event': 'Tech Symposium', 'winner': 'Rahul Sharma', 'position': '1st', 
     'image': 'tech_winner.jpeg', 'department': 'CSE'},
    {'id': 2, 'event': 'Cultural Fest', 'winner': 'Priya Patel', 'position': '1st', 
     'image': 'cultural_winner.webp', 'department': 'ECE'},
    {'id': 3, 'event': 'Sports Day', 'winner': 'Vikram Singh', 'position': '1st', 
     'image': 'sports_winner.webp', 'department': 'Mechanical'}
]

@app.route('/')
def home():
    if 'username' in session:
        if session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/admin')
def admin_dashboard():
    if 'username' not in session or session['role'] != 'admin':
        flash('You need to login as admin first', 'danger')
        return redirect(url_for('login'))
    return render_template('admin.html', events=events, winners=winners)

@app.route('/user')
def user_dashboard():
    if 'username' not in session:
        flash('You need to login first', 'danger')
        return redirect(url_for('login'))
    return render_template('user.html', events=events, winners=winners)

@app.route('/events')
def show_events():
    if 'username' not in session:
        flash('You need to login first', 'danger')
        return redirect(url_for('login'))
    return render_template('events.html', events=events)

@app.route('/winners')
def show_winners():
    if 'username' not in session:
        flash('You need to login first', 'danger')
        return redirect(url_for('login'))
    return render_template('winners.html', winners=winners)

@app.route('/add_event', methods=['POST'])
def add_event():
    if 'username' not in session or session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('login'))
    
    if 'image' not in request.files:
        flash('No image file provided', 'danger')
        return redirect(url_for('admin_dashboard'))
    
    file = request.files['image']
    if file.filename == '':
        flash('No selected image', 'danger')
        return redirect(url_for('admin_dashboard'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        new_event = {
            'id': len(events) + 1,
            'title': request.form['title'],
            'description': request.form['description'],
            'image': unique_filename,
            'date': request.form['date']
        }
        events.append(new_event)
        flash('Event added successfully!', 'success')
    else:
        flash('Allowed image types are: png, jpg, jpeg, gif', 'danger')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/delete_event/<int:event_id>')
def delete_event(event_id):
    if 'username' not in session or session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('login'))
    
    global events
    events = [event for event in events if event['id'] != event_id]
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/add_winner', methods=['POST'])
def add_winner():
    if 'username' not in session or session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('login'))
    
    new_winner = {
        'id': len(winners) + 1,
        'event': request.form['event'],
        'winner': request.form['winner'],
        'position': request.form['position'],
        'image': 'default_winner.jpg',
        'department': request.form['department']
    }
    winners.append(new_winner)
    flash('Winner added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/delete_winner/<int>winner_id>')
def delete_winner(winner_id):
    if 'username' not in session or session['role'] != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('login'))
    
    global winners
    winners = [winner for winner in winners if winner['id'] != winner_id]
    flash('Winner deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)