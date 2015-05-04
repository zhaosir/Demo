var http = require("http");
var router = require("./router");

router.addRoute('/',require('./routers/index'));
router.addRoute('/about',require('./routers/about'));
router.addRoute('/contact',require('./routers/contact'));

function onListend(){
	console.log("server listen at 8888");
}

function onConnected(request,response){
	router.handleRoute(request.url,request,response);
}

var server = http.createServer(onConnected);
server.listen(8888,onListend);


