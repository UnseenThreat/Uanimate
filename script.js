function onHoverButton(button){
	var animation = setInterval(darken,5);
	var darkness = 235;
	var fontColor = 0;
	function darken(){
		button.style.backgroundColor = "rgba(30,"+darkness+",30,1)";
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
		button.style.backgroundColor = "rgba(30,"+darkness+",30,1)";
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
function readTextFile(){
	var animation = setInterval(buffer,50);
	function buffer(){
		var file = '/home/lx_user/Documents/programming/web/uanimate/results.txt';
	    var rawFile = new XMLHttpRequest();
	    rawFile.open("GET", file, false);
	    rawFile.onreadystatechange = function ()
	    {
	        if(rawFile.readyState === 4)
	        {
	            if(rawFile.status === 200 || rawFile.status == 0)
	            {
	                var allText = rawFile.responseText;
	                console.log(allText);
	            	var s = allText.split(" ");
	            	var barHappy = document.getElementById("barHappy");
	            	var barSad = document.getElementById("barSad");
	            	var barAngry = document.getElementById("barAngry");
	            	var barFear = document.getElementById("barFear");
	            	var barSurprise = document.getElementById("barSurprise");

	            	barHappy.style.height = (parseFloat(s[0])/parseFloat(s[5]))+"%";
	            	barSad.style.height = (parseFloat(s[1])/parseFloat(s[5]))+"%";
	            	barAngry.style.height = (parseFloat(s[2])/parseFloat(s[5]))+"%";
	            	barFear.style.height = (parseFloat(s[3])/parseFloat(s[5]))+"%";
	            	barSurprise.style.height = (parseFloat(s[4])/parseFloat(s[5]))+"%";
	            }
	        }
	    }
	    rawFile.send(null);
	}
}