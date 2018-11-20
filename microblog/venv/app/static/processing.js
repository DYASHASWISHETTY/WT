count=0;
			/*The user agent fires a popstate event when the user navigates through their history, whether backwards or forwards, provided it isn’t taking the user away from the current page. */
			window.onpopstate=restore;
			
			function restore(e){
				
				var rest=e.state;
				document.getElementById("fileToUpload").value=rest.fname;
			}
			function push()
			{
				
   			 var myData = "This is my data string."
    			 $.post("/index", {"myData": myData})
					
			var hist=new Object();
			hist["fname"]=document.getElementById("fileToUpload").value;
			history.pushState(hist,"XHR History","http://127.0.0.1:5000/home.html?count="+count++);
			}	

 function push1()
    {
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    console.log("success  :)");
                }
            }
        }
    
        req.open('POST', '/index1');
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        var un = document.getElementById('user').value;
        var password = document.getElementById('fileToUpload').value;
        var postVars = 'username='+un +'&fileToUpload='+password;
	//var postVars = un + "#" + password;
        req.send(postVars);

        }
