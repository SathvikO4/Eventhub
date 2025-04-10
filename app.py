from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configuration for file uploads
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy credentials
ADMIN_CREDENTIALS = {'username': 'admin', 'password': 'admin123'}
users = [{'username': 'user1', 'password': 'user123', 'name': 'Test User'}]

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', events=events, winners=winners, username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_CREDENTIALS['username'] and password == ADMIN_CREDENTIALS['password']:
            session['username'] = username
            session['is_admin'] = True
            return redirect(url_for('admin_dashboard'))
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                session['is_admin'] = False
                return redirect(url_for('index'))
        
        flash('Invalid credentials!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        
        if any(user['username'] == username for user in users):
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        users.append({'username': username, 'password': password, 'name': name})
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/admin')
def admin_dashboard():
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    return render_template('admin.html', events=events, winners=winners)

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        
        file = request.files['image']
        
        if file.filename == '':
            filename = 'default_event.jpg'
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                flash('Allowed image types are: png, jpg, jpeg, gif', 'danger')
                return redirect(request.url)
        
        new_event = {
            'id': len(events) + 1,
            'title': request.form['title'],
            'description': request.form['description'],
            'image': filename,
            'date': request.form['date']
        }
        events.append(new_event)
        flash('Event added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('add_event.html')

@app.route('/add_winner', methods=['GET', 'POST'])
def add_winner():
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        
        file = request.files['image']
        
        if file.filename == '':
            filename = 'default_winner.jpg'
        else:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                flash('Allowed image types are: png, jpg, jpeg, gif', 'danger')
                return redirect(request.url)
        
        new_winner = {
            'id': len(winners) + 1,
            'event': request.form['event'],
            'winner': request.form['winner'],
            'position': request.form['position'],
            'image': filename,
            'department': request.form['department']
        }
        winners.append(new_winner)
        flash('Winner added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    event_names = list(set(event['title'] for event in events))
    return render_template('add_winner.html', event_names=event_names)

@app.route('/delete_event/<int:event_id>')
def delete_event(event_id):
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    global events
    events = [event for event in events if event['id'] != event_id]
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/delete_winner/<int:winner_id>')
def delete_winner(winner_id):
    if 'username' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))
    
    global winners
    winners = [winner for winner in winners if winner['id'] != winner_id]
    flash('Winner deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/event/<int:event_id>')
def event_details(event_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        flash('Event not found!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('event_details.html', event=event)

@app.route('/winner/<int:winner_id>')
def winner_details(winner_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    winner = next((w for w in winners if w['id'] == winner_id), None)
    if not winner:
        flash('Winner not found!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('winner_details.html', winner=winner)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)