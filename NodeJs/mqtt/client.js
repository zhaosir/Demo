var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://127.0.0.1:1883');

client.on('connect',function(){
	client.subscribe('test');
	client.publish('test','hello')
});

client.on('message',function(topic,message){
	console.log(message.toString())
	client.end()
});

client.on('reconnect',function(){
	console.log('reconnect');		
});

client.on('close',function(){
	console.log('close');		
});
