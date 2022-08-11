var x = 2;

if (x >= 2) {
    console.log("ES MAYOR O IGUAL A 2");
} else {
    console.log("ES MENOR A 2");
}

console.log(`El valor x es ${x}`)



var arreglo = ['perro', 'gato']
    ///  0          1

console.log(arreglo[0])

arreglo.push('tigre');

console.log(arreglo)

var objeto = {
    'nombre': 'Francisco',
    'apellido': 'Boisier',
    'edad': 37
}

console.log(objeto);
console.log(objeto.edad);


function saludar(nombre) {
    console.log("HOLA" + nombre);
    return "HOLA -----" + nombre;
}

var resultado = saludar("FRANCISCO")
console.log(resultado);