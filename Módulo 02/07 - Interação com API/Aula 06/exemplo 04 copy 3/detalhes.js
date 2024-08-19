async function buscarDetalhes(){

    let busca = await fetch("lista-produtos.json")
    let produtos = await busca.json()

    let paramentros = new URLSearchParams(window.location.search)
    let parametroID = paramentros.get("produto-id")

    let indiceProd
    for(let x in produtos){
        if(produtos[x].id == parametroID){
            indiceProd = x
        }
    }

    document.body.innerHTML = `
    <div class="detalhes">
        <h3>${produtos[indiceProd].nome}</h3>
        <img src="${produtos[indiceProd].img}" widtm="250" height="250">
        <p>${produtos[indiceProd].descricao}</p>
        <div class="valores">
             <span class="valorCo">R$ ${produtos[indiceProd].valorComDesconto.toFixed(2).replace("." , ",")}</span>
             <span class="valorSe">R$ ${produtos[indiceProd].valorSemDesconto.toFixed(2).replace("." , ",")}</span>
        </div>
    </div>
    
    `
}

buscarDetalhes()