$(document).ready(function() {
    // Initialize the side navigation (for mobile)
    $('.sidenav').sidenav({ edge: "right" });

    // Initialize modals
    $('.modal').modal();

    // Initialize collapsible effect
    $('.collapsible').collapsible();

    // Initialize form select effect
    $('select').formSelect();

    // Initialize the slider only if it exists
    if ($('.slider').length) {
        $('.slider').slider({
            fullWidth: true,   // Enable full width
            indicators: true,  // Show the indicators (dots) for each slide
            interval: 6000,    // Time between slide transitions (in milliseconds)
            height: 400        // Height of the slider
        });
    }

    // Check for the flash modal trigger and open the modal if it exists
    if ($('#flash-modal-trigger').length) {
        $('#flash-modal').modal('open');
    }
});


