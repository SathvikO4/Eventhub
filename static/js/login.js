document.addEventListener('DOMContentLoaded', function() {
    // Login form handler
    document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        const users = JSON.parse(localStorage.getItem('users'));
        
        if (users[username] && users[username].password === password) {
            // Store current user in sessionStorage
            sessionStorage.setItem('currentUser', JSON.stringify({
                username: username,
                role: users[username].role
            }));
            window.location.href = '/';
        } else {
            alert('Invalid username or password');
        }
    });
});