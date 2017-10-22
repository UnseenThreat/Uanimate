function onHoverButton(button){
	var animation = setInterval(darken,5);
	var darkness = 235;
	var fontColor = 0;
	function darken(){
		button.style.backgroundColor = "rgba(30,"+darkness+",30)";
		button.style.color = "rgb("+fontColor+", "+fontColor+", "+fontColor+")";
		if(darkness == 0)
			clearInterval(animation);
		if(fontColor < 255)
			fontColor+=15;
		darkness-=5;
	}
}
function onOverButton(button){
	var animation = setInterval(darken,5);
	var darkness = 0;
	var fontColor = 255;
	function darken(){
		button.style.backgroundColor = "rgba(30,"+darkness+",30)";
		button.style.color = "rgb("+fontColor+", "+fontColor+", "+fontColor+")";
		if(darkness == 235)
			clearInterval(animation);
		if(fontColor > 0)
			fontColor-=15;
		darkness+=5;
	}
}
function runEmoji(){
	console.log("wtf");
	var focus = document.getElementById("board");
	focus.style.visibility = "hidden";
}