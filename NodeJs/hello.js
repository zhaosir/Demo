//exports.world = function(){
//	console.log('hello world');
//};

function Hello(){
	var name;
	this.setName = function(thyName){
		name = thyName;
	};
	this.sayHello = function(){
		console.log('say hello to ' + name);
	};
};
module.exports = new Hello();
