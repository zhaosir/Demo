var http = require("http");
var url = require("url");

function start(route){
	function onRequest(request,response){
		var pathname = url.parse(request.url).pathname;
		console.log("request for " + pathname + " received");

		route(pathname);

		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write("i am start");
		response.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("server is started");
}

exports.start = start;
