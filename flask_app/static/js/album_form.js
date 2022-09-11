var urlCheckbox = document.querySelector('#url_checkbox')
var fileUpload = document.querySelector('#file_upload')
var urlUpload = document.querySelector('#url_upload')

urlCheckbox.addEventListener('click', function(){
    if (this.checked === true){
        showURL()
    } else {
        hideURL()
    }
})

function showURL(){
    urlUpload.classList.remove('hidden')
    fileUpload.classList.add('hidden')
}
function hideURL(){
    urlUpload.classList.add('hidden')
    fileUpload.classList.remove('hidden')
}