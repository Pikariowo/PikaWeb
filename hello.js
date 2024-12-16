function openAlert() {
    document.getElementById('customAlert').style.display = 'flex';
}

function closeAlert() {
    document.getElementById('customAlert').style.display = 'none';
}

window.onload = function() {
    openAlert();
};
