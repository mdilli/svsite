
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

    /*
    Select text in autofocus fields (from avem).
   	*/
   	$('[autofocus]').each(function(k, elem) {
   		$(elem).select();
   	});

    /*
    Dropdown closes as soon as search field is clicked; prevent that (from avem).
   	 */
   	$('#menu-search-dropdown').click(function(event)
   	{
   		event.stopPropagation();
   	});

    /*
    When selecting a dropdown that has inputs, focus and select the first field (from avem).
   	 */
   	function focus_and_select_input(elem)
   	{
   		elem.select();
   		elem.focus();
   	}
   	$('.dropdown-toggle').click(function(event)
   	{
   		var inputs = $(this).parent().find('input');
   		if (inputs.length)
   		{
   			var input = inputs.first();
   			setTimeout(focus_and_select_input.bind(null, input), 0);
   		}
   	});

    /*
    Let ctrl+H open the search bar (from avem).
    http://stackoverflow.com/a/14180949/723090
   	 */
   	$(window).bind('keydown', function(event)
   	{
   		if (event.ctrlKey || event.metaKey) {
   			switch (String.fromCharCode(event.which).toLowerCase())
   			{
   				case 'h':
   					event.preventDefault();
   					var msdb = $('#menu-search-dropdown-button');
   					if (msdb.is(":visible"))
   					{
   						/* The search is in dropdown menu mode */
   						var input = $('#menu-search-dropdown').find('input').first();
   						msdb.click();
   					}
   					else
   					{
   						var msm = $('#menu-search-mainbar');
   						/* The search is in menubar mode, but it might be collapsed */
   						if ( ! msm.is(":visible"))
   						{
   							/* It's collapsed; probably the user doesn't have a ctrl key if their screen is this small... */
   							$('#menubar-toggle-collapse').click();
   						}
   						var input = msm.find('input').first();
   					}
   					setTimeout(focus_and_select_input.bind(null, input), 0);
   					break;
   			}
   		}
   	});
});


