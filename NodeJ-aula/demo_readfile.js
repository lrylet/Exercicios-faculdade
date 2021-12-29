var http = require('http');
var fs = require('fs');

// Código usado para ler um arquivo de sistema

http.createServer(function(req, res){
    fs.readFile('demofile1.html', function(err, data){
        res.writeHead(200, {'Content-type': 'text/html'});
        res.write(data);
        return res.end();
    })
}).listen(8080);