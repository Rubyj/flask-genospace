$(function () {
//retrieve entities and names from entity endpoint and render into autocomplete when a user types
$( "#searchInput" ).autocomplete({
    source: function( request, response ) {
        $.ajax({
            dataType: "json",
            type : 'GET',
            url: '/entity?key=' + $('#searchInput').val(),
            success: function(data) {
                $('input.suggest-user').removeClass('ui-autocomplete-loading');  
                // hide loading image
		var entityNames = [];
		var entities = data.entities[0]
		for (entity in entities) {
			//Grab the current entity name and compare to search term 
			//Add to autocomplete if match
			entityName = entities[entity].name;

			if (entityName.toLowerCase().startsWith($('#searchInput').val().toLowerCase())){
				entityNames.push(entityName)
			}
		}
		console.log(data)
                response(entityNames);
            },
            error: function(data) {
                //$('input.suggest-user').removeClass('ui-autocomplete-loading');  
		console.log("autocomplete error");
            }
        });
    },
    minLength: 1,
    open: function() {},
    close: function() {},
    focus: function(event,ui) {},
    select: function(event, ui) {}
});
});
