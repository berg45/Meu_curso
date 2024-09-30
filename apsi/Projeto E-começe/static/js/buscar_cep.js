$(document).ready(function(){
    $("#cep").blur(function () {
        console.log('CEP field lost focus'); // Verifique se esta mensagem aparece
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
                    } else {
                        limpa_formulario_cep();
                        alert("CEP não encontrado!");
                    }
                });
            } else {
                limpa_formulario_cep();
                alert("Formato de CEP inválido");
            }
        } else {
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
});
