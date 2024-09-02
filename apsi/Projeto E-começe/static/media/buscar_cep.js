document.addEventListener('DOMContentLoaded', function () {
    const cepInput = document.querySelector('#id_cep');  // ID do campo CEP
    const enderecoInput = document.querySelector('#id_endereço');  // ID do campo endereço
    const bairroInput = document.querySelector('#id_bairro');  // ID do campo bairro
    const cidadeInput = document.querySelector('#id_cidade');  // ID do campo cidade
    const estadoInput = document.querySelector('#id_estado');  // ID do campo estado

    cepInput.addEventListener('blur', function () {
        const cep = cepInput.value.replace(/\D/g, '');  // Remove caracteres não numéricos

        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        enderecoInput.value = data.logradouro;
                        bairroInput.value = data.bairro;
                        cidadeInput.value = data.localidade;
                        estadoInput.value = data.uf;
                    } else {
                        alert('CEP não encontrado.');
                    }
                })
                .catch(error => {
                    console.error('Erro ao consultar o CEP:', error);
                });
        } else {
            alert('CEP inválido.');
        }
    });
});
