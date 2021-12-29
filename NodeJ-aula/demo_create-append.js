// // Código para criar novos arquivos.
// Existem três tipos, sendo esses: fs.appendFile(), 
// fs.open() e o fs.writeFile().

var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Olá, conteúdo!', function (err){
    if (err) throw err;
    console.log ('Salvo!');
});
