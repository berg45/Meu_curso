async function concessionaria(){
    let resultado = await fetch("carros.json")
    let carros = await resultado.json()


//alert("A marca é " + carros.marca + ", O modelo é " + carros.modelo + ", O ano é " + carros.ano
   // + " e a cor é " + carros.cor)
   //for( let x in carros)
    //    alert(carros[1].modelo)

    
         document.body.innerHTML = `
         <h1> A marca do carro é ${carros[2].marca}</h1>
         <p> O modelo é ${carros[2].modelo}</p>
         <p> O ano é ${carros[2].ano}</p>
         <p> A cor é ${carros[2].cor}</p>`
    

}

concessionaria()
