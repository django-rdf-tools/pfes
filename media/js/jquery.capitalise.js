// Revium jquery extensions
// Copyright (c) 2009 Revium pty ltd http://revium.com.au
// Licensed under the GPL licence:
// http://www.gnu.org/licenses/gpl.html

(function($) {
    // To capitalise text input when user types in (to make just the 1st symbol uppercase)
    // Developed by Evgeny Petrov, Revium
    // Ver 1.0, 24/11/2009
    $.fn.capitalise = function() {
        $(this).keyup(function() {
            var el = $(this);
            var value = "";
            if (el.length > 0) {
                value = el.val().toString().substr(0, 1).toUpperCase() + el.val().toString().substr(1).toLowerCase();
            }
            el.val(value);
        });
    }
})(jQuery);
