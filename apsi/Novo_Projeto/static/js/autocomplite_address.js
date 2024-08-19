$(document) .ready(function(){
    $("#zip_code").blur(function () {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep != ""){
            var validacep = /^[0-9]{8}$/;
            if (validacep.test(cep)) {
                $("#address").val("...");
                $("#neighborhood").val("...");
                $("#city").val("...");
                $("#state").val("...");

                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {
                    if (!("erro" in dados)) {
                        $("#address").val(dados.logradouro);
                        $("#neighborhood").val(dados.bairro);
                        $("#city").val(dados.localidade);
                        $("#state").val(dados.uf);
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
            //cep é inválido.
            limpa_formulario_cep();

        }   
    });
    function limpa_formulario_cep(){
        //limpa valores do formulario de cep.
        $("#address").val("");
        $("#neighborhood").val("");
        $("#city").val("");
        $("#state").val("");
        $('#number').val("");
        $('#complement').val("");
    }
})


