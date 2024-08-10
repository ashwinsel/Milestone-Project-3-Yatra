$(document).ready(function() {
    $('.sidenav').sidenav({ edge: "right" });
    $('.modal').modal();
    $('.parallax').parallax();

    // Check for the flash modal trigger and open the modal if it exists
    if ($('#flash-modal-trigger').length) {
        $('#flash-modal').modal('open');
    }
});
