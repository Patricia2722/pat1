console.log("Javascript here!")
document.addEventListener('DOMContentLoaded', function () {
    const showRegisterForm = document.getElementById('showRegisterForm');
    const showLoginForm = document.getElementById('showLoginForm');
    const loginFormSection = document.getElementById('loginFormSection');
    const registerFormSection = document.getElementById('registerFormSection');

    // Show Register Form
    if (showRegisterForm) {
        showRegisterForm.addEventListener('click', function () {
            loginFormSection.style.display = 'none';
            registerFormSection.style.display = 'block';
        });
    }

    // Show Login Form
    if (showLoginForm) {
        showLoginForm.addEventListener('click', function () {
            registerFormSection.style.display = 'none';
            loginFormSection.style.display = 'block';
        });
    }
});
