document.addEventListener('DOMContentLoaded', function () {
    const estadoSelect = document.getElementById('estado');
    const cidadeSelect = document.getElementById('cidade');

    estadoSelect.addEventListener('change', function () {
        const uf = this.value;

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

document.addEventListener('DOMContentLoaded', function() {
    const fotoInput = document.getElementById('foto');
    const fotoPreviewImg = document.getElementById('foto-preview-img');
    
    fotoInput.addEventListener('change', function(event) {
        const file = event.target.files[0];  // Pega o primeiro arquivo selecionado
        
        if (file) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                fotoPreviewImg.src = e.target.result;  // Define a URL da imagem para a prévia
                fotoPreviewImg.style.display = 'block';  // Exibe a imagem
            };
            
            reader.readAsDataURL(file);  // Lê o arquivo como URL de dados
        } else {
            fotoPreviewImg.style.display = 'none';  
        }
    });
});

