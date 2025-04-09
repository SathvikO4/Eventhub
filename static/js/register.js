document.addEventListener('DOMContentLoaded', function() {
    // Initialize default users if not exists
    if (!localStorage.getItem('users')) {
        const defaultUsers = {
            'admin': { password: 'admin123', role: 'admin' },
            'user1': { password: 'user123', role: 'user' }
        };
        localStorage.setItem('users', JSON.stringify(defaultUsers));
    }

    // Registration form handler
    document.getElementById('registerForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const role = document.getElementById('role').value;
        
        const users = JSON.parse(localStorage.getItem('users'));
        
        if (users[username]) {
            alert('Username already exists');
            return;
        }
        
        users[username] = { password: password, role: role };
        localStorage.setItem('users', JSON.stringify(users));
        
        // Auto-login after registration
        sessionStorage.setItem('currentUser', JSON.stringify({
            username: username,
            role: role
        }));
        
        window.location.href = '/';
    });
});