async function smartphone(){
    let resultado = await fetch("celular.json")
    let celular = await resultado.json()
    
    let divLista = document.getElementById("lista-card")

    for(let x in celular){
        divLista.innerHTML += `
            <div class = "card">
                <img src="${celular[x].img}"  width="250" height="auto"
                <h1>Celular  ${celular[x].marca}</h1>
                <P>Preço é; ${celular[x].preço}</P>
                <p>O modelo  ${celular[x].modelo}</p>
                <p>O armazenamento é ${celular[x].armazenamento}</p>   
                <p>A memoria ram é ${celular[x].memoriaRam}</p>
            </div>   
        `
    }


}
smartphone()