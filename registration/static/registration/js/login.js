//const formOpenBtn = document.querySelector("#form-open"),
//  home = document.querySelector(".home"),
//  formContainer = document.querySelector(".form_container"),
//  formCloseBtn = document.querySelector(".form_close"),
//  signupBtn = document.querySelector("#signup"),
//  loginBtn = document.querySelector("#login"),
//  pwShowHide = document.querySelectorAll(".pw_hide");
//
//formOpenBtn.addEventListener("click", () => home.classList.add("show"));
//formCloseBtn.addEventListener("click", () => home.classList.remove("show"));
//
//pwShowHide.forEach((icon) => {
//  icon.addEventListener("click", () => {
//    let getPwInput = icon.parentElement.querySelector("input");
//    if (getPwInput.type === "password") {
//      getPwInput.type = "text";
//      icon.classList.replace("uil-eye-slash", "uil-eye");
//    } else {
//      getPwInput.type = "password";
//      icon.classList.replace("uil-eye", "uil-eye-slash");
//    }
//  });
//});
//
//signupBtn.addEventListener("click", (e) => {
//  e.preventDefault();
//  formContainer.classList.add("active");
//});
//loginBtn.addEventListener("click", (e) => {
//  e.preventDefault();
//  formContainer.classList.remove("active");
//});


// Получаем элементы поля ввода пароля и иконку для скрытия/показа
const passwordField = document.querySelector('input[type="password"]');
const togglePassword = document.querySelector('.pw_hide');

// Добавляем обработчик события при нажатии на иконку
togglePassword.addEventListener('click', function() {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
});

// Получаем чекбокс и элемент для запоминания
const rememberCheckbox = document.getElementById('check');

// Проверяем, сохранены ли данные о запоминании
if (localStorage.getItem('rememberMe') === 'true') {
    rememberCheckbox.checked = true;
}

// Добавляем обработчик события при изменении состояния чекбокса
rememberCheckbox.addEventListener('change', function() {
    if (this.checked) {
        // Запоминаем состояние чекбокса в локальном хранилище
        localStorage.setItem('rememberMe', 'true');
    } else {
        // Удаляем данные о запоминании, если чекбокс не отмечен
        localStorage.removeItem('rememberMe');
    }
});



