var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'Olá, conteúdo!', function (err){
    if (err) throw err;
    console.log('Salvo!');
});