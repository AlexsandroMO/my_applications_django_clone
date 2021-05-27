console.log('Entrou')
//https://www.devmedia.com.br/calendario-em-jquery-criando-calendarios-com-datepicker/37458
//https://social.msdn.microsoft.com/Forums/pt-BR/4c8a79ae-6d77-43db-b813-684b049b64d7/como-fao-para-esconder-uma-coluna-de-uma-tabela-com-javascript?forum=webgeralpt

//https://stackoverflow.com/questions/17605296/document-onclick-not-working - Actions jquery


//Calendário
$(function() {
    $("#id_date_contract").datepicker({dateFormat: 'dd/mm/yy'});
});














//-----------------------




/* $('.trash-fa').click(function() {

    let r = confirm("Você Deseja Realmente Cancelar essa Atividade!?");
    if (r == true){
        console.log('foi')
        //window.history.go(-1)
        window.location.href = '/'
    }else{
        console.log('N foi')
    }

}); */






/* 
var baseUrl   = 'http://127.0.0.1:8000/';
//var deleteBtn  = $('trash-fa')
var deleteBtn  = $('#p-id')
//var delLink  = $('.delete-btn');

$(deleteBtn).on('click', function(e){
    e.preventDefault();

    // id = document.getElementById("p-id").firstChild.nodeValue
    id = document.getElementById("p-id").firstChild.nodeValue
    //id = document.querySelectorAll('.trash-fa').firstChild.nodeValue

    let delLink = 'http://127.0.0.1:8000/'      //$(this).attr('href');

    console.log(id)
    

    let result = confirm('Quer realmente deletar esta tarefa?');
    
    if(result){
        window.location.href = delLink + 'delete_segur/' + id;
    }
});  
 */
//document.getElementById(id).firstChild.nodeValue;



// function marcarTodos(marcardesmarcar){
//     $('.marcar').each(function () {
//         this.checked = marcardesmarcar;
//     });
// }


// let checkbox = document.getElementById('termos_de_contrato');
// if(checkbox.checked) {
//     console.log("O cliente marcou o checkbox");
// } else {
//     console.log("O cliente não marcou o checkbox");
// }

// console.log('vamos!: ', document.getElementsByName('_selected_action'))
// let option_test = document.getElementsByName('_selected_action')
// console.log('>>>>>',option_test.length)

// for (let i=0; i<option_test.length; i++){
//     if (option_test[i].checked){
//         console.log('Eita')
//     }
// }



/* let checkbox = document.getElementById('termos_de_contrato');
if(checkbox.checked) {
    console.log("O cliente marcou o checkbox");
} else {
    console.log("O cliente não marcou o checkbox");
} */



/* 



 */



/*  ocultar()

document.getElementById('esconde-test').addEventListener('click', ocultar, false);
document.getElementById('click-show').addEventListener('click', mostrar, false);

function ocultar(evt) {
	document.getElementById("hide-field-col").style.display = "none"; 
    document.getElementById("hide-field-cel").style.display = "none";
}

*/

/* 
//Manipulando as colunas
function ocultaColumn (colIndex) {
    var table = document.getElementById('esconde-test');
    for (var r = 0; r < table.rows.length; r++)
        table.rows[r].cells[colIndex].style.display = 'none';
}
function mostraColumn (colIndex) {
    var table = document.getElementById('esconde-test');
    for (var r = 0; r < table.rows.length; r++)
        table.rows[r].cells[colIndex].style.display = '';
} */




//CPF
// let valorcpf = document.getElementById('cpf-cnpj');
// console.log('===>: ', valorcpf)

// let valorcpf = document.querySelectorAll('.field-cpf')
// let cpf = document.getElementById('cpf-cnpj');
// console.log('===>: ', valorcpf)
// console.log('===>: ', cpf)
//let valorcpf = document.querySelectorAll('#cpf-cnpj')
// for (let i = 0; i < 9; i++){
//     console.log('===: ', valorcpf.value)
// }












// function ValidaCPF(){   

//     let
//     var ao_cpf = document.forms.form1.ao_cpf.value; 
//     var cpfValido = /^(([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}))$/;     
    
//     if (cpfValido.test(ao_cpf) == false)    {  
//        //alert("invalido");
//        console.log('foi')
//        var valorValido = document.getElementById("cpf-cnpj").value = "???????";
//     }else{
//         console.log('não foi')
//     }
// }








// var descendentes = document.querySelectorAll("#_save");

// descendentes.addEventListener("click", function (e) {
//         console.log('press')
//         alert('O elemento clicado foi o ' + this.innerHTML);
//     })


/* 
function limpa_formulario_cep() {
        //Limpa valores do formulário de cep.
        document.getElementById('rua').value=("");
        document.getElementById('bairro').value=("");
        document.getElementById('cidade').value=("");
        document.getElementById('estado').value=("");
        
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('rua').value=(conteudo.logradouro);
        document.getElementById('bairro').value=(conteudo.bairro);
        document.getElementById('cidade').value=(conteudo.localidade);
        document.getElementById('estado').value=(conteudo.uf);
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulario_cep();
        alert("CEP não encontrado.");
        document.getElementById('cep').value=("");
    }
}
    
function pesquisacep(valor) {

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep !== "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if(validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('rua').value="...";
            document.getElementById('bairro').value="...";
            document.getElementById('cidade').value="...";
            document.getElementById('estado').value="...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = '//viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            limpa_formulario_cep();
            alert("Formato de CEP inválido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulario_cep();
    }
}

function formatar(mascara, documento){
var i = documento.value.length;
var saida = mascara.substring(0,1);
var texto = mascara.substring(i);

if (texto.substring(0,1) != saida){
        documento.value += texto.substring(0,1);
}

}

function idade (){
var data=document.getElementById("dtnasc").value;
var dia=data.substr(0, 2);
var mes=data.substr(3, 2);
var ano=data.substr(6, 4);
var d = new Date();
var ano_atual = d.getFullYear(),
    mes_atual = d.getMonth() + 1,
    dia_atual = d.getDate();
    
    ano=+ano,
    mes=+mes,
    dia=+dia;
    
var idade=ano_atual-ano;

if (mes_atual < mes || mes_atual == mes_aniversario && dia_atual < dia) {
    idade--;
}
return idade;
} 


function exibe(i) {


    
document.getElementById(i).readOnly= true;
    
    


}

function desabilita(i){

 document.getElementById(i).disabled = true;    
}
function habilita(i)
{
    document.getElementById(i).disabled = false;
}


function showhide()
{
   var div = document.getElementById("newpost");
   
   if(idade()>=18){

div.style.display = "none";
}
else if(idade()<18) {
div.style.display = "inline";
}

}



 */