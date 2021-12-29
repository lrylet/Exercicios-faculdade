var http = require('http');

http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'}); // O 200 indica que está "ok", e o segundo argumento é a formatação do cabeçalho
    res.write(req.url); // Retorna ao usuário o que vem depois de "localhost:8080/""
    res.end();
}).listen(8080);
