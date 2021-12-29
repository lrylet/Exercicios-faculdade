function validacao (){
    var nome = document.getElementById("nome-form")
    if (nome.value  == "" || nome.value.length < 10){
        nome.classList.add("erro")
        document.getElementById("erro-nome").style.display="inline"
    } else {
        nome.classList.remove("erro")
        document.getElementById("erro-nome").style.display="none"
    }

    
    var endereco = document.getElementById("endereco-form")
    if (endereco.value  == "" ){
        endereco.classList.add("erro")
        document.getElementById("erro-address").style.display="inline"
    } else {
        endereco.classList.remove("erro")
        document.getElementById("erro-address").style.display="none"
    }


    var cep = document.getElementById("cep-forms")
    if (cep.value  == "" || cep.value.length < 9){
        cep.classList.add("erro")
        document.getElementById("erro-cep").style.display="inline"
    } else {
        cep.classList.remove("erro")
        document.getElementById("erro-cep").style.display="none"
    }

    var cpf = document.getElementById("cpf-forms")
    if (cpf.value  == "" || cpf.value  == "111.111.111-11" || cpf.value  == "222.222.222-22" ||  cpf.value  == "333.333.333-33" ||  cpf.value  == "444.444.444-44" ||  cpf.value  == "555.555.555-55" ||  cpf.value  == "666.666.666-66" ||  cpf.value  == "777.777.777-77" ||  cpf.value  == "888.888.888-88" ||  cpf.value  == "999.999.999-99" ||  cpf.value  == "000.000.000-00" || cpf.value.length < 14 || !validarCPF(cpf.value) ){
        cpf.classList.add("erro")
        document.getElementById("erro-cpf").style.display="inline"
    }
    else {
        cpf.classList.remove("erro")
        document.getElementById("erro-cpf").style.display="none"
    }

    var bday = document.getElementById("nascimento")
    if (bday.value == ""|| bday.value.length == 8){
        bday.classList.add("erro")
        document.getElementById("erro-bday").style.display="inline"
    }
    else{
        bday.classList.remove("erro")
        document.getElementById("erro-bday").style.display="none"
    } document.getElementById("idade").innerHTML="A sua idade até o final do ano atual será "+ calculaIdade(new Date(nascimento.value))

}   

    function postMask(p, mask) {
        let i = p.value.length;
            let exit = mask.substring(1, 0);
                let text = mask.substring(i)
                if (text.substring(0, 1) != exit) {
                    p.value += text.substring(0, 1);
                }
        }

    function removeChar(e) {
        console.log(e);
            if (e.charCode > 47 && e.charCode < 58) {
                e.preventDefault();
            }
    }

    function calculaIdade(data) { 
        let agora = new Date()
        return Math.floor(((agora.getFullYear() - data.getFullYear()) * 12 + agora.getMonth() - data.getMonth())/12)
    
      }


    function validarCPF(cpf) {
        console.log(cpf);
        cpf = cpf.split('.').join('').split('-').join('');
      
        digitoUm = false;
        digitoDois = false;
        soma = 0;
        contador = 10;
      
        for(i=0; i < cpf.length - 2; i++) {
          soma += cpf[i] * (contador - i);
        }
      
        if ((soma * 10 % 11) == cpf[9]) {
          digitoUm = true;
        }
      
        soma = 0
        for(i=0; i < cpf.length - 1; i++) {
          soma += cpf[i] * (contador + 1 - i);
        }
      
        if ((soma * 10 % 11) == cpf[10]) {
          digitoDois = true;
        }
      
        if (digitoUm && digitoDois) {
          console.log('cpf válido');
          return true;
        }
        else {
          console.log('cpf inválido');
          return false;
        }
      }

    //  USO DA PROVA

    function pforms (){
        var tamanhoF = document.forms;
    }

    