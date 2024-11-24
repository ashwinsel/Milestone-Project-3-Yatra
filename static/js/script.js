$(document).ready(function () {
    
    $('.sidenav').sidenav({ edge: "right" });

    
    $('.modal').modal();

    
    $('.collapsible').collapsible();

    
    $('select').formSelect();

    // Inspired by CofeeKing Prject by Hitesh Choudhary
    if ($('.slider').length) {
        $('.slider').slider({
            fullWidth: true,    // Enable full width
            indicators: true,   // Show the indicators (dots) for each slide
            interval: 6000,     // Time between slide transitions (in milliseconds)
            height: 400         // Height of the slider
        });
    }

    
    if ($('#flash-modal-trigger').length) {
        $('#flash-modal').modal('open');
    }

    
    $('.delete-btn').on('click', function () {
        return confirm("Are you sure you want to delete this site? This action cannot be undone.");
    });

    
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        
        const classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        const classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };

        // Ensure the hidden select is required
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }

        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            const selectWrapper = $(this).parent(".select-wrapper");

            // When the select value changes, validate it
            selectWrapper.on("change", function () {
                const selectedItem = $(this).children("ul").children("li.selected:not(.disabled)");

                if (selectedItem.length > 0) {
                    $(this).children("input").css(classValid);
                } else {
                    $(this).children("input").css(classInvalid);
                }
            });
        }).on("click", function () {
            const selectWrapper = $(this).parent(".select-wrapper");
            const selectedItem = selectWrapper.children("ul").children("li.selected:not(.disabled)");

            // Check the background color to determine if it's valid
            if (selectedItem.css("background-color") === "rgba(0, 0, 0, 0.03)") {
                selectWrapper.children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    const parentSelect = $(this).parent(".select-wrapper").children("select");

                    // On focus out, if the required select is not valid, mark as invalid
                    if (parentSelect.prop("required") && $(this).css("border-bottom") !== "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                });
            }
        });
    }

    // Adapted from TaskManager Project by Code Institute, Tim Nelson
    $('.datepicker').datepicker({
        format: 'dd.mm.yyyy',  // Set your desired date format
        defaultDate: new Date(),
        setDefaultDate: true,
        autoClose: true
    });
});