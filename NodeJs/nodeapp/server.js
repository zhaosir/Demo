var http = require("http");
var router = require("./router");

URLS = [
["/","./routers/index"],
["/about","./routers/about"],
["/contact","./routers/contact"]
];

//router.addRoute('/',require('./routers/index'));
//router.addRoute('/about',require('./routers/about'));
//router.addRoute('/contact',require('./routers/contact'));


for(index in URLS){
	router.addRoute(URLS[index][0],require(URLS[index][1]));
}

function onListend(){
	console.log("server listen at %d",server.address().port);
}

function onConnected(request,response){
	url = require("url");

//	var post = "";
//	request.addListener('data',function(chunk){
//		post += chunk;
//	});
//	request.addListener('end',function(){
//		console.log('postdata:'+post);
//	});
	route =  url.parse(request.url).pathname;
	router.handleRoute(route,request,response);
}

var server = http.createServer(onConnected);
server.listen(8888,onListend);


