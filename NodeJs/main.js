hello = require('./hello');
//hello = new Hello(); 
//Hello.world();
hello.setName('boy');
hello.sayHello();

n = {};
n1 = [
["/","./test"],
["/about","./about"]
];


//for(index in n1){
//	console.log(n1[index][0]);
//}

//console.log(n);
//console.log(n1);




var res = [];
function foo(){
	var i = 0;
	for(i;i<3;i++){
		res[i] = (function(j){
			//console.log(i);
			return function(){
				console.log(j);
			}
		})(i);
	}
}

foo();
for(var i = 0;i<res.length;i++){
	res[i]();
}

console.log("---------");
function test1(){
	var i = 0;
	return function(){
		return function(){
			console.log(i++);
		}
	}
}

c = test1();
c()();
t = new test1();
t()();


console.log("-----");

var name = "globle";

var person = function(){
	var name = "default";
	return {
		getName : function(){
			return name;		  
		},
		setName : function(newName){
			name = newName;
		}
	};
}();

console.log(person.name);
console.log(person.getName());
person.setName("tom");
console.log(person.getName());

console.log("------------");

function test2(x){
	var a = 0;
	a++;
	x++;
	var inner = function(){
		return a+x;
	};
	return inner;
}

var t2 = test2(1);
console.log(t2());
console.log(t2());
