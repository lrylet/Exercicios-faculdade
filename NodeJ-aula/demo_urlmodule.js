// Usará a variável q para segmentar a URL e acrescentará propriedades (no caso, host, pathname, search e month são as propriedades de 'q') 
// e retornará ao usuário.

var url = require('url');
var adr = 'http://localhost:8080/default.htm?year=2017&month=february';
var q = url.parse(adr, true);

console.log(q.host);
console.log(q.pathname);
console.log(q.search);

var qdata = q.query;
console.log(qdata.month);
