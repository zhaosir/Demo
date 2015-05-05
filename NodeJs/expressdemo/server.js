var express = require("express");
var app = express();

app.get("/",function(req,res){
	res.send("hello express");		
});

var server = app.listen(8888,function(){
	console.log('listening on port %d',server.address().port);
});
