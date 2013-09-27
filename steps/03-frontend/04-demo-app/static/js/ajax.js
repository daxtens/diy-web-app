function generateButton() {
    // get the JSON. TODO: handle errors
    $.getJSON('/slogan.json', function(data) {
	// callback when the data is returned
	// we set the slogan
	$(slogan).text(data.slogan);
    });
}

// when the document is loaded:
$(document).ready(function(){
    // wire up the generate button
    $('#generate').on('click', generateButton);
});

