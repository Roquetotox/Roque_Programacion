//Ejercicio de presentacion
let nombre = "Roque"
let edad = 16;
let curso = "Curso de programacion"
console.log("Hola me llamo",nombre,"tengo",edad,"y etoy viendo el ",curso   )
//calculadora que da los resultados con los numeros predeterminados
let a = 10;
let b = 15;
let suma = a + b;
let resta = a - b;
let multiplicacion =a*b;
let division = a / b;
let modulo = a % b;
let exponenciacion = a ** b;
console.log(`Suma: ${suma}`);
console.log(`Resta: ${resta}`);
console.log(`Multiplicación: ${multiplicacion}`);
console.log(`División: ${division}`);
console.log(`Módulo: ${modulo}`);   
console.log(`Exponenciación: ${exponenciacion}`);

//calculadora que da el resultado del numeo que ingrese el usuario
let dato = Number(prompt("Por favor, ingresa un dato:"));
let dato2 = Number(prompt("Por favor, ingresa un dato:"));

let suma2 = dato + dato2;
let resta2 = dato - dato2;
let multi = dato * dato2;
let div = dato / dato2;
let mod = dato % dato2;

console.log(`Las operaciones son: ${suma2} ${resta2} ${multi} ${div} ${mod}`);
//calculadora con condicionales
const num1 = parseFloat(prompt("Ingresa el primer número:"));
const num2 = parseFloat(prompt("Ingresa el segundo número:"));
const operacion = prompt("Elige una operación (suma, resta, multiplicacion, division, modulo, potencia):");


const primerNumero = parseFloat(prompt("Ingresa el primer número:"));
const segundoNumero = parseFloat(prompt("Ingresa el segundo número:"));
const operacionElegida = prompt("Elige una operación (suma, resta, multiplicacion, division, modulo, potencia):");

let calculoFinal;


if (operacionElegida.toLowerCase() === 'suma') {
 alert(`El resultado de la suma es: ${calculoFinal}`);
} else if (operacionElegida.toLowerCase() === 'resta') {
 calculoFinal = primerNumero - segundoNumero;
 alert(`El resultado de la resta es: ${calculoFinal}`);
} else if (operacionElegida.toLowerCase() === 'multiplicacion') {
     calculoFinal = primerNumero * segundoNumero;
 alert(`El resultado de la multiplicación es: ${calculoFinal}`);
} else if (operacionElegida.toLowerCase() === 'division') {
 if (segundoNumero === 0) {
 alert("Error: No se puede dividir por cero.");
 } else {
 calculoFinal = primerNumero / segundoNumero;
 alert(`El resultado de la división es: ${calculoFinal}`);
 }
} else if (operacionElegida.toLowerCase() === 'modulo') {
 if (segundoNumero === 0) {
 alert("Error: No se puede calcular el módulo con cero.");
 } else {
 calculoFinal = primerNumero % segundoNumero;
 alert(`El resultado del módulo es: ${calculoFinal}`);
 }
} else if (operacionElegida.toLowerCase() === 'potencia') {
 calculoFinal = primerNumero ** segundoNumero;
 alert(`El resultado de la potencia es: ${calculoFinal}`);
} else {
 alert("Operación no válida. Por favor, revisa la ortografía.");
}

//calculadora con switch
const numero1 = parseFloat(prompt("Ingresa el primer numero:"));
const numero2 = parseFloat(prompt("Ingresa el segundo numero:"));
const operacionSeleccionada = prompt("Elige una operación (suma, resta, multiplicacion, division, modulo, potencia):");

let resultadoFinal;
let mensajeCompleto;


switch (operacionSeleccionada.toLowerCase()) {
    case 'suma':
        resultadoFinal = numero1 + numero2;
        mensajeCompleto = `El resultado de la suma es: ${resultadoFinal}`;
        break;
    case 'resta':
        resultadoFinal = numero1 - numero2;
        mensajeCompleto = `El resultado de la resta es: ${resultadoFinal}`;
        break;
    case 'multiplicacion':
        resultadoFinal = numero1 * numero2;
        mensajeCompleto = `El resultado de la multiplicación es: ${resultadoFinal}`;
        break;
    case 'division':
        if (numero2 === 0) {
            mensajeCompleto = "Error: No se puede dividir por cero.";
        } else {
            resultadoFinal = numero1 / numero2;
            mensajeCompleto = `El resultado de la division es: ${resultadoFinal}`;
        }
        break;
    case 'modulo':
        if (numero2 === 0) {
            mensajeCompleto = "Error: No se puede calcular el módulo con cero.";
        } else {
            resultadoFinal = numero1 % numero2;
            mensajeCompleto = `El resultado del modulo es: ${resultadoFinal}`;
        }
        break;
    case 'potencia':
        resultadoFinal = numero1 ** numero2;
        mensajeCompleto = `El resultado de la potencia es: ${resultadoFinal}`;
        break;
    default:
        mensajeCompleto = "Operación no válida. Por favor, revisa la ortografía.";
}


alert(mensajeCompleto);







