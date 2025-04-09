// User management using localStorage
document.addEventListener('DOMContentLoaded', function() {
    // Initialize default users if not exists
    if (!localStorage.getItem('users')) {
        const defaultUsers = {
            'admin': { password: 'admin123', role: 'admin' },
            'user1': { password: 'user123', role: 'user' }
        };
        localStorage.setItem('users', JSON.stringify(defaultUsers));
    }

    // Login form handler
    document.getElementById('loginForm')?.addEventListener('submit', function(e) {
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

    // Registration form handler
    document.getElementById('registerForm')?.addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('reg-username').value;
        const password = document.getElementById('reg-password').value;
        const role = document.getElementById('reg-role').value;
        
        const users = JSON.parse(localStorage.getItem('users') || {});
        
        if (users[username]) {
            alert('Username already exists');
            return;
        }
        
        users[username] = { password: password, role: role };
        localStorage.setItem('users', JSON.stringify(users));
        alert('Registration successful! Please login.');
        document.getElementById('reg-username').value = '';
        document.getElementById('reg-password').value = '';
    });

    // Image preview functionality (from previous implementation)
    const imageInput = document.getElementById('image');
    if (imageInput) {
        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                let previewContainer = document.getElementById('image-preview-container');
                if (!previewContainer) {
                    previewContainer = document.createElement('div');
                    previewContainer.id = 'image-preview-container';
                    previewContainer.style.marginTop = '10px';
                    imageInput.parentNode.appendChild(previewContainer);
                }
                
                previewContainer.innerHTML = '';
                const preview = document.createElement('img');
                preview.src = URL.createObjectURL(file);
                preview.style.maxWidth = '200px';
                preview.style.maxHeight = '200px';
                preview.style.borderRadius = '4px';
                preview.style.marginTop = '10px';
                previewContainer.appendChild(preview);
            }
        });
    }
});

// Toggle forms in admin dashboard
function toggleForm(formId) {
    const form = document.getElementById(formId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}

// Confirm before deleting
function confirmDelete() {
    return confirm('Are you sure you want to delete this?');
}