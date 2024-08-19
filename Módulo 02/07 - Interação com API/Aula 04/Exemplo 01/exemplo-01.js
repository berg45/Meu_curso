async function buscar(){
    let resposta = await fetch("exemplo.txt")
    let convertido = await resposta.text()

    //document.body.innerHTML = "<h1>" + convertido + "</h1>"


   let numeros = [1, 2, 3];
   for (let x in numeros){
    

   document.body.innerHTML += `
        <h1>  
        </h1>
            ${convertido} 
        <P>
           ${numeros[x]}
        </p>
    `
   }

}
buscar()
