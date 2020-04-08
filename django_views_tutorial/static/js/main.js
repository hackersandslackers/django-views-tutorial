document.addEventListener("DOMContentLoaded", function() {
    let disabledLinks = document.getElementsByClassName('disabled');

    for (let i = 0, len = disabledLinks.length; i < len; i++) {
        disabledLinks[i].addEventListener('click', function (e) {
            e.preventDefault();
        });
    }
});