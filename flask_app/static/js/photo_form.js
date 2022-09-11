var urlCheckboxPhoto = document.querySelector('#url_checkbox_photo')
var fileUploadPhoto = document.querySelector('#file_upload_photo')
var urlUploadPhoto = document.querySelector('#url_upload_photo')

urlCheckboxPhoto.addEventListener('click', function(){
    if (this.checked === true){
        showURL()
    } else {
        hideURL()
    }
})

function showURL(){
    urlUploadPhoto.classList.remove('hidden')
    fileUploadPhoto.classList.add('hidden')
}
function hideURL(){
    urlUploadPhoto.classList.add('hidden')
    fileUploadPhoto.classList.remove('hidden')
}