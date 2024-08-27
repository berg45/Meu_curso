function buscarCEP() {
    const cep = document.getElementById('cep').value.replace(/\D/g, '');
    if (cep !== "") {
        const url = `https://viacep.com.br/ws/${cep}/json/`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.getElementById('endereco').value = data.logradouro;
                    document.getElementById('bairro').value = data.bairro;
                } else {
                    alert("CEP não encontrado!");
                }
            })
            .catch(error => {
                console.error('Erro ao buscar o CEP:', error);
            });
    }
}
