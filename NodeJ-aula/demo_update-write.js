var fs = require('fs');

// Esse método do writeFile() apaga o conteúdo e
// coloca outro por cima.

fs.writeFile('mynewfile3.txt', 'Esse é o meu texto.', function (err) {
    if (err) throw err;
    console.log('Conteúdo substituído!');
});