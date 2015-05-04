function Contact(){
	this.exec = function(route,req,res){
		res.statusCode = 200;
		res.setHeader("Content-Type","text/html");
		res.end("This is <h1>Contact page</h1>");
	}
}

module.exports = new Contact();
