
async function ver(){
    let achar = await fetch("frase.txt")
    let encontrado = await achar.text()

    console.log(encontrado)
    alert(encontrado)

}

ver()