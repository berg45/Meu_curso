$(document) .ready(function(){
    $("#cep").blur(function () {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep != ""){
            var validacep = /^[0-9]{8}$/;
            if (validacep.test(cep)) {
                $("#endereco").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#estado").val("...");

                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
                    if (!("erro" in dados)) {
                        $("#endereco").val(dados.logradouro);
                        $("#bairro").val(dados.bairro);
                        $("#cidade").val(dados.localidade);
                        $("#estado").val(dados.uf);
                    }
                    else {
                        limpa_formulario_cep();
                        alert("cep não encontrado!")
                    }
                });
            }    
            else{
                limpa_formulario_cep();
                alert("formulario de CEP invalido");
            }
        }
        else{
           
            limpa_formulario_cep();

        }   
    });
    function limpa_formulario_cep(){
        
        $("#endereco").val("");
        $("#bairro").val("");
        $("#cidade").val("");
        $("#estado").val("");
        $('#numero').val("");
        $('#complemento').val("");
    }
})


