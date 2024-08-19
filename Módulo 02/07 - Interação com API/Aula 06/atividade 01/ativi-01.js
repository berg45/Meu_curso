async function loja(){
    let buscar = await fetch("notebook.json")
    let notebook = await buscar.json()

    let divLista = document.getElementById("lista-card")

  

    for(let x of notebook){
        divLista.innerHTML +=`
        <div class = "card">
            <img src="${x.img}"  width="250" height="200"
            <p> ${x.marca}</p>
            <p> ${x.modelo}</p>
            <p>Processador ${x.processador}</p>
            <p>Valor é R$ ${x.valor}</p>
        </div>
        `

    }
      
}
loja()