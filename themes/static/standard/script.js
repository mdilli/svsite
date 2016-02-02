
$(document).ready(function()
{
    /*
    Affix navigation to top of page after scrolling past the top menu.
    Based on http://www.bootply.com/69848
    */
    $('#header-main-affix').affix({
          offset: {
            top: $('#header-menu-top').height() + $('#header-image').height()
          }
    });
});


