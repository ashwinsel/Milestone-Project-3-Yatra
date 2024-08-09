$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

$(document).ready(function() {
    // Check if there are flash messages
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                // Create a Materialize toast with high z-index
                M.toast({
                    html: '{{ message }}',
                    classes: 'amber darken-2 white-text',
                    displayLength: 4000,
                    completeCallback: function(){ 
                        console.log("Toast dismissed"); 
                    }
                });
            {% endfor %}
        {% endif %}
    {% endwith %}
});