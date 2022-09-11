// Variables
var modalCloseBtns = document.querySelectorAll('.modal-close-btn')
var modalBtn = document.querySelectorAll('.btn-modal')
var modalWrappers = document.querySelectorAll('.modal__wrapper')
var modalContainers = document.querySelectorAll('.modal__container')

// events
for (let container of modalContainers) {
    container.addEventListener('click', function(event){
        event.stopPropagation()
    })
}

for (let wrapper of modalWrappers) {
    wrapper.addEventListener('click', function(){
        closeModal(wrapper)
    })
}

for (let btn of modalBtn) {
    btn.addEventListener('click', function(){
        console.log("modal open btn");
        wrapperId = this.getAttribute('modal-id')
        wrapper = document.querySelector(`#${wrapperId}`)
        openModal(wrapper)
    })
}

for (let btn of modalCloseBtns) {
    btn.addEventListener('click', function(){
        wrapper = findWrapper(btn)
        closeModal(wrapper)
    }) 
}


// functions

function findWrapper(el){
    if (el.classList.contains('modal__wrapper')){
        return el
    } else {
        return findWrapper(el.parentElement)
    }
}

function closeModal(wrapper){
    wrapper.classList.add('hidden')
}

function openModal(wrapper){
    wrapper.classList.remove('hidden')
}