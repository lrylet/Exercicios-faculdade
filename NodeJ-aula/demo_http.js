var http = require('http');

// cria um objeto de servidor
http.createServer(function (req, res) {
    res.write('Hello World!'); // escreve uma resposta ao client
    res.end();  // finaliza a resposta
}).listen(8080);  //Indica onde será a porta, no caso, 8080

