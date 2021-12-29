const express = require('express');
const app = express();
const fs = require('fs');
const db = require('./models/db');
const bodyParser = require('body-parser')
const usuario = require('./models/usuario')
const exphbs = require('express-handlebars');
const hbs = exphbs.create({
    defaultLayout: 'main'
});
app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');

app.use(bodyParser.urlencoded({ extended: false}));
app.use(bodyParser.json());

app.use(express.static('resource'));
app.engine('html', require('ejs').renderFile);

app.post('/logar', function (req, res){
    let nome;
    let email;
    let senha;
    let arquivo;

    async function gerarNomeDoArquivo(){
        arquivo = await usuario.findAndCountAll().then(result =>{
            return result.count + 1;
        });

        nome = req.body.nome;
        email = req.body.email;
        senha = req.body.password;

        usuario.create({
            nome: nome,
            email: email,
            senha: senha

        }).then(function(){
            console.log('Usuário adicionado com sucesso.');
            res.redirect('/');
        }).catch(function(erro){
            console.log('Erro ao adicionar o usuário');
        });
    }

    gerarNomeDoArquivo();
});

app.post('/tryLogin', function(req, res){
    usuario.findAll({
        where:{
            email: req.body.email,
            senha: req.body.password
        }
    }).then(data => {
        if (data.length == 1) {
            usuario.findAll({}).then(data => {
                res.redirect('/principal')
            })
        }
        else {
            console.log('Erro no login');
            res.redirect('/');
        }
    });
});

    

app.get('/login', function(req, res){
    fs.readFile('login.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        return res.end();
      });
})

app.get('/', function(req, res){
    fs.readFile('login.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        return res.end();
      });
})

app.get('/cadastro', function(req, res){
    fs.readFile('cadastro.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        return res.end();
      });
})

app.get('/principal', function(req, res){
    usuario.findAll({raw: true}).then(data => {
        console.log(data)
        res.render(__dirname + '\\principal.html', {
        usuarios: JSON.stringify(data)
        });
    })
    
})


app.listen(8080, function(){
    usuario;
    console.log('Conectado ao servidor localhost:8080');
})