async function buscarDetalhes(){
    
    let parametros = new URLSearchParams(window.location.search)
    let parametroID = parametros.get("produto-id")

    let busca
    if(parametroID >= 7){
        busca = await fetch("new-lista.json")
    }else{
        busca = await fetch("lista-produtos.json")
    }
    
    let produtos = await busca.json()

    let indiceProd
    for(let x in produtos){
         
        if(produtos[x].id == parametroID){
            indiceProd = x
        }
   }

   document.getElementById("conteiner-main").innerHTML += `
    <div class="conteiner">
        <div class="plural">
            <div class="dados">
                <h3>${produtos[indiceProd].nome}</h3>
                <img src="${produtos[indiceProd].img[0]}" id="frame" width="300" height="350">
                <div class="miniaturas" id="minis">  </div>
                <p class="descrit">${produtos[indiceProd].descricao}</p>
            </div>

            <div class="valor">
                <span class="valorCo"> R$ ${produtos[indiceProd].valorComDesconto.toFixed(2).replace(".", ",")}</span>
                <span class="valorSe"> R$ ${produtos[indiceProd].valorSemDesconto.toFixed(2).replace(".", ",")}</span>
                <button class="comprar" onclick="comprar()" style="background-color: green" ><a href="longin.html">comprar</a></button>
                <button class="comprar" onclick="adicionar()" style="background-color: blu" ><a href="carrinho.html">adicionar ao carrinho</a></button>
                
            </div>
        </div>
    </div>

    <div class="detalhes">
        <h3>${produtos[indiceProd].dados}</h3>
    </div>
   
    `
  

    let divMini = document.getElementById("minis")
    for(let y of produtos[indiceProd].img){
        divMini.innerHTML +=`
        <img src="${y}" class="mini" width="80" height="80" style="border: 1px solid #000 ; border-radius: 10px">
        
          `

    }

    let pequenas = document.getElementsByClassName("mini")
    for(let e of pequenas){
        e.addEventListener("mouseover", deslize)
    }

function deslize(){
    document.getElementById("frame").src = this.src
    
}

    
}
buscarDetalhes()