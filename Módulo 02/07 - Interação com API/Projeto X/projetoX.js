async function buscar(){
    let achar = await fetch("lista-produtos.json")
    let produtos = await achar.json()

    let divLista = document.getElementById("lista-card")

  
    
    for(let produto of produtos){
        divLista.innerHTML += `
        <div class="card" data-id="${produto.id}">
        <h3>${produto.nome}</h3>
        <img src="${produto.img[0]}" width="250" height="200">
        <p>${produto.descricao}</p>
            <div class="valores">
                <span class="valorCom"> R$ ${produto.valorComDesconto.toFixed(2).replace("." , ",")}</span>
                <span class="valorSem"> R$ ${produto.valorSemDesconto.toFixed(2).replace("." , ",")}</span>
            </div>
        
        </div>
        
        `
    }
   

    
    /*/ parte 2/*/

    let procurar = await fetch("new-lista.json")
    let newList = await procurar.json()

    let divLista2 = document.getElementById("nova-lista")

    for( let nova of newList){
        divLista2.innerHTML +=` 
        <div class="card" data-id="${nova.id}">
        <div class="card">
           <h3>${nova.nome}</h3>
           <img src="${nova.img[0]}" width="250" height="200">
           <p>${nova.descricao}</p>
           <div class="valores">
                <span class="valorCom">R$ ${nova.valorComDesconto.toFixed(2).replace("." , ",")}</span>
                <span class="valorSem">R$ ${nova.valorSemDesconto.toFixed(2).replace("." , ",")}</span>
           </div>
        </div>
        `
    }
    

    let divsCards = document.getElementsByClassName("card")
    for(let card of divsCards){
        card.addEventListener("click" , clicou)
    }
            
    
}

function clicou(){
    let elementoId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?produto-id=" + elementoId
}

buscar()