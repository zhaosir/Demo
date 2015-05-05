var fs = require('fs');
//fs.exists('test.txt',function(exists){
//	console.log(exists);		
//});

fs.writeFile('message.txt','hello',function(err){
	if (err) throw err;
	console.log('write ok');
});
