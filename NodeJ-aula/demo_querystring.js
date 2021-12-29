var http = require('http');
var url = require('url');

http.createServer(function (req, res){
    res.writeHead(200, {'Content-type':'text/html'});
    var q = url.parse(req.url, true).query; // 'parse' analisa uma string e constrói um valor ou objeto descrito pela string
    var txt = q.year + " - " + q.month;
    res.end(txt);
}).listen(8080);