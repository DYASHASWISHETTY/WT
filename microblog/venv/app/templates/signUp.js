$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				html = $.parseHTML(response, true);
        			$('body').html(html);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
