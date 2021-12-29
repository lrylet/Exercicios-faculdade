const db = require('./db');

const usuario = db.sequelize.define('forms', {
    id: {
        type: db.Sequelize.INTEGER, primaryKey: true, autoIncrement: true
    },
    nome: {
        type: db.Sequelize.STRING
    },
    email: {
        type: db.Sequelize.STRING
    },
    senha: {
        type: db.Sequelize.STRING
    },
    arquivo: {
        type: db.Sequelize.STRING
    },

})

usuario.sync({force: false})

module.exports = usuario;