function validateForm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm-password').value;

    if (username.trim() === '') {
        alert('Please enter your username');
        return false;
    }
    if (email.trim() === '') {
        alert('Please enter your email');
        return false;
    }

    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailPattern.test(email)) {
        alert('Please provide a valid email address');
        return false;
    }

    if (password.trim() === '') {
        alert('Please enter your password');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return false;
    }
    return true;
}