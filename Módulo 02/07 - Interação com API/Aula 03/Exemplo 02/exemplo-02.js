
async function procurar(){
   let resposta = await fetch("menssagem.txt")
   let convertido = await resposta.text()

   console.log(resposta)
   alert(convertido)
  
   
}
                                  
procurar()


