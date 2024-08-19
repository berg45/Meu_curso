async function buscar(){
    //await para(stop) a execuçâo do programa aguardando
    // o resultado do comando fetch().
    let procura = await fetch("lista-produtos.json")
    let produtos = await procura.json()

    let divlista = document.getElementById("lista-card")

    for(let produto of produtos){
        divlista.innerHTML += `
           <div class="card" data-id="${produto.id}">
               <h3>${produto.nome}</h3>
               <img src="${produto.img}" width="250" height="200">
               <p>${produto.descricao}</p>
               <div class="valores">
                   <span class="valorCom">R$ ${(produto.valorComDesconto.toFixed(2)).replace(".", ",")}</span>
                   <span class="valorSem">R$ ${(produto.valorSemDesconto.toFixed(2)).replace(".", ",")}</span>
               </div>
            </div>

        `
    }

}

buscar()