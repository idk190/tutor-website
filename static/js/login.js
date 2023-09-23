function admin_signin() {
    admin_password.style.display = 'block';
    student_username.style.display = 'none';
}

function student_signin() {
    admin_password.style.display = 'none';
    student_username.style.display = 'block';
}