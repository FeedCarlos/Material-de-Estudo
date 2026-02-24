let comprar = ["banana","maça","arroz","feijão","ovo"]
let estoque = ["pipoca","banana","bolacha","ovo"]

//console.log(comprar)
comprar.sort()
comprar.length

console.log(`Preciso comprar o total de ${comprar.length} itens`)

/*while (comprar === 0 ) {
    console.log(comprar)
    comprar++
}*/

for (let compras in comprar){
    console.log(`A lista é ${compras} e os itens são ${comprar[compras]}`)
} for (let estoquehm in estoque){
    console.log(`O que tem em casa são ${estoquehm} e ${estoque[estoquehm]}`)
} 

