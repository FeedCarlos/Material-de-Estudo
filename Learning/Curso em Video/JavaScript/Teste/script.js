var msg = document.getElementById('msg')
var data = new Date ()
var hora = data.getHours ()
var min = data.getMinutes ()
var second = data.getSeconds ()
var daynow = data.getDay()
var monthnow = data.getMonth()
var yearnow = data.getFullYear()
date.innerHTML = (`${daynow}/${monthnow}/${yearnow}`) 
msg.innerHTML = (`Agora são ${hora}:${min}:${second}`)


function Verificar () {
    var idade = document.getElementById('txtage')
    var res = document.getElementById('res')
    var i = Number(idade.value)
    if (idade.value.length == 0) {
        window.alert("Bota tua idade cabaço")
    } else if (i >= 18) {
        res.innerHTML = ("Já pode levar kacete da politia")
    } else if (i <= 17) {
        res.innerHTML = ("Kacete só do tio ainda")
    }
    
}
