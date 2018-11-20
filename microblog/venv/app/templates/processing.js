 function do_ajax() {
        var req = new XMLHttpRequest();
        var result = document.getElementById('user');
        req.onreadystatechange = function()
        {
          if(this.readyState == 4 && this.status == 200) {
            console.log("sucess");
          } else {
            console.log("error");
          }
        }
        req.open('POST', '/index1', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("user=" + document.getElementById('user').value);
    }	
/*
	count=0;
console.log("Hello");
			/*The user agent fires a popstate event when the user navigates through their history, whether backwards or forwards, provided it isn’t taking the user away from the current page. 
			window.onpopstate=restore;
			
			function restore(e){
				
				var rest=e.state;
				document.getElementById("fileToUpload").value=rest.fname;
			}
			function push()
			{
				
   			 var myData = "This is my data string."
			 console.log(myData);
    			 $.post("/index", {"myData": myData})
					
			var hist=new Object();
			hist["fname"]=document.getElementById("fileToUpload").value;
			history.pushState(hist,"XHR History","http://127.0.0.1:5000/home.html?count="+count++);
			}	
*/
