
window.addEventListener('scroll', function(event){
    let scroll = this.scrollY
    if (scroll > 10) darkenNav()
    else lightenNav()
})

function darkenNav(){
    let nav = document.querySelector('#navbar')
    let navTitle = document.querySelector('#nav_title')
    nav.classList.add('bg-secondary', 'text-white')
    navTitle.classList.remove('invisible')
}

function lightenNav(){
    let nav = document.querySelector('#navbar')
    let navTitle = document.querySelector('#nav_title')
    nav.classList.remove('bg-secondary', 'text-white')
    navTitle.classList.add('invisible')
}