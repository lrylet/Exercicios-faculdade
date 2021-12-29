var fs = require('fs');

// Nome autoexplicativo

fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err){
    if (err) throw err;
    console.log('O arquivo foi renomeado!');
});