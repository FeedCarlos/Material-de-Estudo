/*let array = ['string', 1, true, ['array1'], ['array2']];
console.log(array[0]);*/

/*array.forEach(function(item, index){console.log(item, index)}); */

/*array.push([]);
console.log(array)*/

/*array.pop();
console.log(array);*/

/*console.log(array.indexOf(1));*/

let obejct = {String: 'string', number: 1, Boolean: true, Array: ['Array'], obejctInterno: { obejtctInterno: ("objeto interno")}};

console.log(obejct.obejctInterno);

var string = obejct.String;
console.log(string);

var array = obejct.Array;
console.log(array);

var {String, Boolean, obejctInterno} = obejct;
console.log(string, Boolean, obejctInterno);