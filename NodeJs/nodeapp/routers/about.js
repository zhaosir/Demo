function About(){
	this.exec = function(route,req,res){
		res.statusCode = 200;
		res.setHeader("Content-Type","text/html");
		res.end("This is <h1>About Me</h1>");
	}
}

module.exports = new About();
