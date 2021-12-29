var fs = require('fs');

// Método único para deletar arquivos

fs.unlink('mynewfile2.txt', function (err) {
    if (err) throw err;
    console.log('Arquivo deletado!');
});