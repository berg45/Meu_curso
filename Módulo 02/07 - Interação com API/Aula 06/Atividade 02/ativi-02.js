async function conssecionaria(){
    let buscar = await fetch("carros.json")
    let carros = await buscar.json()

    
    let divLista = document.getElementById("lista-card")

    for (let x of carros){
        divLista.innerHTML +=`
        
        <div class = "card">
            <h2>${x.marca}</h2>
            <img src="${x.img}"  width="350" height="300">
            <p>${x.modelo}</p>
            <p>${x.ano}</p>
            <p>${x.opcionais}</p>   
        
        </div>
        `
    }

}
conssecionaria()        
        
        
      