document.addEventListener('DOMContentLoaded', function () {
    const estadoSelect = document.getElementById('estado');
    const cidadeSelect = document.getElementById('cidade');

    estadoSelect.addEventListener('change', function () {
        const uf = estadoSelect.value;

        cidadeSelect.innerHTML = '<option value="">selecione uma cidade</option>';

        if (uf) {
            fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${uf}/municipios`)
                 .then(response => response.json())
                 .then(cidades => {
                    cidades.forEach(cidade => {
                        const option = document.createElement('option');
                        option.value = cidade.nome;
                        option.textContent = cidade.nome;
                        cidadeSelect.appendChild(option);
                
                    });
                 })
                 .catch(error => {
                    console.error('Erro ao buscar cidades;', error);
                 })
        }
    })

}) 