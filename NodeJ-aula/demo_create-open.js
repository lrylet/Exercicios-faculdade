//Usando outro método, o fs.open()

var fs = require('fs');

fs.open('mynewfile2.txt', 'w', function (err, file) {
    if (err) throw err;
    console.log ('Salvo!');
});

// o segundo argumento como 'w', significa 'writing'
// e será aberto apenas para escrever.
// e criará um novo arquivo caso não exista

