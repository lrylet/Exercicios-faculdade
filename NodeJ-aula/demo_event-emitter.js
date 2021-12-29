var events = require('events');
var eventEmitter = new events.EventEmitter();

var myEventHandler = function() {
    console.log('Eu escuto um grito');
}
// Atribui o gerenciador à um evento;
eventEmitter.on('grito', myEventHandler);

// Ativa o evento em parâmetro, no caso, 'grito';
eventEmitter.emit('grito');