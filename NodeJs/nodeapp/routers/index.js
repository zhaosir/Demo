url = require("url");
util = require("util");

function Index(){
	this.exec = function(route,req,res){
		res.statusCode = 200;
		querystr = url.parse(req.url,true).query;
		console.log("querystr id : " + querystr["id"]);
		console.log("querystr name : " + querystr["name"]);
		
		post = "";
		req.on('data',function(chunk){
			post += chunk;
		});
		req.on('end',function(){
			//console.log("form data : " + post);
			var querystring = require("querystring");
			var form = querystring.parse(post,true);
			console.log("form data : " + form['age']);
			//res.end("This is <h1>Index Page</h1>");
		});
		res.setHeader("Content-Type","text/html");
		res.end("This is <h1>Index Page</h1>");
	}
}

module.exports = new Index();
