var http = require('http');
 http.createServer(function (req, res) {
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('Hello Node.js');
}).listen(8124, "10.0.177.30");

console.log('Server running at http://127.0.0.1:8124/');

