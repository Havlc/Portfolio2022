$("ul.todo").on("click", "li", function(){
	$(this).toggleClass("done");
});

$("ul.todo").on("click", "li span", function(event){
	$(this).parent().fadeOut(500,function(){
		$(this).remove();
	});
	event.stopPropagation();
});

$("input[type='text']").keypress(function(event){
	if(event.which===13){
		let todoText = $(this).val();
		$(this).val("");
		$("ul.todo").append('<li><span><i class="fas fa-trash-alt"></i></span> '+todoText+"</li>");
	}
})

$("#plus").on("click",function(){
	$("input[type='text']").fadeToggle(1000);
})



