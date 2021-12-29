var fs = require('fs');

// Coloca o conteúdo no final do arquivo 
// que será aberto

fs.appendFile('mynewfile1.txt', ' Esse é meu texto.', function (err){
    if (err) throw err;
    console.log('Atualizado!');
});