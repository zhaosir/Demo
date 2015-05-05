url = require("url");
util = require("util");
formidable = require("formidable");

function Index(){
	this.exec = function(route,req,res){
		res.statusCode = 200;
		querystr = url.parse(req.url,true).query;
		console.log("querystr id : " + querystr["id"]);
		console.log("querystr name : " + querystr["name"]);
		var fields = {},
			file = {};
		var form = new formidable.IncomingForm();
		form.uploadDir = '/tmp';
		form.on("field",function(field,value){
			if (form.type == "multipart"){
				if(field in fields){
					if(util.isArray(fields[field]) == false){
						fields[field] = [fields[field]]
					}
					fields[field].push(value);
					return;
				}
			}
			fields[field] = value;
		})
		//.on("file",function(field,file){
		
		//})
		.on("end",function(){
			for(var i in fields){
				console.log("fields : " + i + "=" + fields[i])	
			}
		});
		if (req.method == "POST"){
			form.parse(req);
		}
	//	post = "";
	//	req.on('data',function(chunk){
	//		post += chunk;
	//	});
	//	req.on('end',function(){
	//		//适用于 Content-Type = application/x-www-form-urlencoded
	//		//console.log("form data : " + post);
	//		var querystring = require("querystring");
	//		var form = querystring.parse(post);
	//		for(var i in form){
	//			console.log("<form data> : " + i + " = "  + form[i] +'\r\n</form data>');
	//		}
	//		//res.end("This is <h1>Index Page</h1>");
	//	});
		res.setHeader("Content-Type","text/html");
		res.end("This is <h1>Index Page</h1><form action='/' method='POST'><input type='text' name='uname'/><input type='submit' value='sbumit'/></form>");
	}
}

module.exports = new Index();
