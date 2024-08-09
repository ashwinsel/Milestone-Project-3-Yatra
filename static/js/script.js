$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

$(document).ready(function() {
  // Initialize modal
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    // Open the modal if there are flash messages
    {% if messages %}
        var instance = M.Modal.getInstance($('#flash-modal'));
        instance.open();
    {% endif %}
});