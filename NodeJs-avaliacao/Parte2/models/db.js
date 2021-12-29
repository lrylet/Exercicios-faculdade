const Sequelize = require('sequelize');

const sequelize = new Sequelize('forms', 'root', '178cabello12', {
  host: 'localhost',
  dialect: 'mysql'
});

sequelize.authenticate().then(function(){
  console.log('Conectado ao Banco de Dados com êxito.')
}).catch(function(erro){
  console.log7('Erro ao se conectar!' + erro)
})

module.exports = {
  Sequelize: Sequelize,
  sequelize: sequelize
}
