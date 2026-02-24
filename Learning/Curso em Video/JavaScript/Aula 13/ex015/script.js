function verificar () {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("[ERRO] Verifique os dados e tente novamente!")
    } else {
        var fsexm = document.querySelector('div#mas')
        var fsexf = document.querySelector('div#fem')
        var idade = ano - Number(fano.value)
        var genero = document.getElementById('mas' || 'fem')
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsexf = genero ) {
            genero = 'Mulher'
        } else if (fsexm = genero) {
            genero = 'Homem'
        }
        res.innerHTML = `Detectanos ${genero} com ${idade} anos.`
    }
        
}
    
