let caract = ["a", "a", "b", "b", "c", "d"]

caract.sort()
caract.length
console.log(`A variavel composta tem ${caract.length} valores`)


/*for (let pos=0; pos < valores.length; pos++){
    //console.log(valores[pos])
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}
*/

for(let pos in caract){
    
    console.log(`A posição ${pos} tem o valor ${caract[pos]}`)
}

