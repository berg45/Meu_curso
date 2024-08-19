//async function sabedoria(){
  //  let estava = await fetch("reflexção.txt")
  //    let principio = await estava.text()

  //  console.log(principio)
  //  alert(principio)
//}
//sabedoria()


async function sabio(){
    let homem = await fetch("reflexção.txt")
    let sensato = await homem.text()

    console.log(sensato)
    alert(sensato)

}

sabio()