var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'lelelos10@gmail.com',
    pass: '178cabello12'
  }
});

var mailOptions = {
  from: 'lelelos10@gmail.com',
  to: 'losdsousa@gmail.com',
  subject: 'Enviando email com NodeJs',
  text: 'Testando. É fácil.'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});