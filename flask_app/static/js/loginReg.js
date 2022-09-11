var showLoginBtn = document.querySelector('#show-login-btn')
var showRegisterBtn = document.querySelector('#show-register-btn')
var loginForm = document.querySelector('#login-form')
var registerForm = document.querySelector('#register-form')
var registerPic = document.querySelector('#register-pic')
var loginPic = document.querySelector('#login-pic')

showRegisterBtn.addEventListener('click', function(){
    registerPic.classList.add('translate-y-[100%]')
    showLoginBtn.classList.remove('hidden')
    showRegisterBtn.classList.add('hidden')
})

showLoginBtn.addEventListener('click', function(){
    registerPic.classList.remove('translate-y-[100%]')
    showLoginBtn.classList.add('hidden')
    showRegisterBtn.classList.remove('hidden')
})
