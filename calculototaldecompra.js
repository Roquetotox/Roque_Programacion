const nombreProducto = "Tablet 10 pulgadas";
let precio = 450.99;
let stock = 25;
const envioGratis = true;
const cantidadComprada = 2; 
const impuesto = 0.07; 
let subtotal = precio * cantidadComprada;
let totalFinal = subtotal + (subtotal * impuesto);

console.log("Subtotal:", subtotal.toFixed(2));
console.log("Total final (incluyendo 7% de impuesto):", totalFinal.toFixed(2));