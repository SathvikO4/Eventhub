// Tab functionality
function openTab(tabName) {
    const tabContents = document.getElementsByClassName('tab-content');
    for (let i = 0; i < tabContents.length; i++) {
        tabContents[i].classList.remove('active');
    }
    
    const tabButtons = document.getElementsByClassName('tab-button');
    for (let i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove('active');
    }
    
    document.getElementById(tabName).classList.add('active');
    event.currentTarget.classList.add('active');
}

// Image preview functionality
document.addEventListener('DOMContentLoaded', function() {
    // Make event and winner cards clickable
    // Event cards
    const eventCards = document.querySelectorAll('.event-card');
    eventCards.forEach(card => {
        card.addEventListener('click', function() {
            const eventId = this.getAttribute('data-event-id');
            if (eventId) {
                window.location.href = `/event/${eventId}`;
            }
        });
    });

    // Winner cards
    const winnerCards = document.querySelectorAll('.winner-card');
    winnerCards.forEach(card => {
        card.addEventListener('click', function() {
            const winnerId = this.getAttribute('data-winner-id');
            if (winnerId) {
                window.location.href = `/winner/${winnerId}`;
            }
        });
    });

    // For event image preview
    const eventImageInput = document.querySelector('#add_event_form input[type="file"]');
    if (eventImageInput) {
        eventImageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    let preview = document.getElementById('event-image-preview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.id = 'event-image-preview';
                        preview.className = 'image-preview';
                        eventImageInput.parentNode.insertBefore(preview, eventImageInput.nextSibling);
                    }
                    preview.src = event.target.result;
                    preview.style.display = 'block';
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // For winner image preview
    const winnerImageInput = document.querySelector('#add_winner_form input[type="file"]');
    if (winnerImageInput) {
        winnerImageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    let preview = document.getElementById('winner-image-preview');
                    if (!preview) {
                        preview = document.createElement('img');
                        preview.id = 'winner-image-preview';
                        preview.className = 'image-preview';
                        winnerImageInput.parentNode.insertBefore(preview, winnerImageInput.nextSibling);
                    }
                    preview.src = event.target.result;
                    preview.style.display = 'block';
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const fileInputs = form.querySelectorAll('input[type="file"]');
            let isValid = true;
            
            fileInputs.forEach(input => {
                if (input.files.length > 0) {
                    const file = input.files[0];
                    const extension = file.name.split('.').pop().toLowerCase();
                    const allowedExtensions = ['jpg', 'jpeg', 'png', 'gif'];
                    
                    if (!allowedExtensions.includes(extension)) {
                        alert('Please upload only image files (jpg, jpeg, png, gif)');
                        isValid = false;
                    }
                    
                    if (file.size > 5 * 1024 * 1024) { // 5MB limit
                        alert('File size should be less than 5MB');
                        isValid = false;
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
});

// Flash message auto-hide
setTimeout(() => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.style.display = 'none';
    });
}, 5000);