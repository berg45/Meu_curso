async function buscarDetalhes(){
    // Consumo do Json
    let busca = await fetch("lista-produtos.json")
    let produtos = await busca.json()

    // Criou um objeto URLSearch e passou
    // a coleta dos paramentros da URL nele.
    let parametros = new URLSearchParams(window.location.search)
    // Obteve do parametro "produto-id", o seu valor.
    let parametroID = parametros.get("produto-id")
    

    //Criou uma variavel vazia
    let indiceProd
    //usou o for para ID de cada produto é igual ao ID
    for(let x in produtos){
         //Verifica se o ID de cada produto é igual ao ID
         //coletado na URL da página no navegador
        if(produtos[x].id == parametroID){
              // Atribui á variável vazia, o valor x, que contém
              //o indeci do produto que corresponde ao ID da URL
            indiceProd = x
        }

    }

    // Adiciona ba TAG BODY do  HTML, um código HTML concatenado
    //com valores do objeto produto encontrado

    document.body.innerHTML = `
    <div class="detalhes">
        <h3>${produtos[indiceProd].nome}</h3>
        <img src="${produtos[indiceProd].img}" width="250" height="250"></>
        <p>${produtos[indiceProd].descricao}</p>

        <div class="valor">
            <span class="valorCo"> R$ ${(produtos[indiceProd].valorComDesconto.toFixed(2)).replace(".", ",")}</span>
            <span class="valorSe"> R$ ${(produtos[indiceProd].valorSemDesconto.toFixed(2)).replace(".", ",")}</span>
        </div>
    </div>
    `
    
    
}
buscarDetalhes()