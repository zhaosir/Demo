var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/:age', function(req, res, next) {
  console.log("get param-------:%s,%s",req.query.q,req.param("q"));
  console.log("url param-------:%s",req.param("age"));
  res.render('index', { title: 'Express' });
});

var multipart = require('connect-multiparty');
var multipartMiddleware = multipart();

router.post('/',multipartMiddleware,function(req,res,next){
	console.log("post param------:%s",req.param('name'));
	console.log("body param------:%s",req.body.name);
	//res.render('index', { title: 'Express' });
	res.send(req.body);
});

module.exports = router;
