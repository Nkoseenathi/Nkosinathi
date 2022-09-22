
function go_to(loc) {
	
  if(loc.includes(".")){
	  var type="text";
	  if(loc.includes(".mp4")||loc.includes(".ogg")||loc.includes(".webM")){
		  type = "video"
		  
	  }
	  else if(loc.includes(".jpg")||loc.includes(".png")||loc.includes(".webP")){
		  type = "image"
		  
	  }else if(loc.includes(".txt")||loc.includes(".html")||loc.includes(".xml")){
		  type = "text"
		  
	  }
	  
	  else if(loc.includes(".mp3")||loc.includes(".ogg")||loc.includes(".wav")){
		  type = "audio"
		  
	  }
	  document.location =`File.py?path=`+loc+`&typ=`+type
  
 
  }
  else{
	document.location =`GUI.py?path=`+loc}

}


function locate(loc) {

	document.location =`GUI.py?path=`+loc
  

}
function create() {
	document.location =`GUI.py?action=create`
}