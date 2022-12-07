
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
	  document.location =`File.py?path=.`+loc+`&typ=`+type
  
 
  }
  else{
	document.location =`GUI.py?action=path&path=.`+loc}

}


function locate(loc) {

	document.location =`GUI.py?action=path&path=`+loc
  

}
function createUser() {
	document.location =`GUI.py?action=create`
}

function rename(oname){
	
	var temp = oname.split(".")
	var extenstion =""
	if (temp.length>1){
		extenstion = "."+temp[temp.length-1]
	}
	let name = prompt("Enter new name")
	if(!(name==null || name=="")){
		document.location =`GUI.py?action=rename&nname=`+name+extenstion+`&name=.`+oname
	}
	}
	
function fdelete(name){
	
	document.location =`GUI.py?action=delete&name=.`+name
	
}

function move(name){
	
	document.location =`GUI.py?action=move&name=`+name
	
}

function download(name){
	
	document.location =`Download.py?name=.`+name
	
}

function copy(name){
	
	document.location =`GUI.py?action=copy&name=`+name
	
}

function create(path){
	
    let name = prompt("Enter Folder name")
	document.location =`GUI.py?action=createD&name=`+name+`&path=`+path
	
}

function logout(){
	
	let logout = confirm("Are you sure you want to logout?");	
	if(logout == true)
		document.location =`GUI.py`
	
}

