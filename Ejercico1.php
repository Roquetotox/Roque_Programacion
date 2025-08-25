<?php

// creamos la variable de pares y impares
$pares = 0;
$impares = 0;

// Recorre los numeros del 1 al 50
for ($i = 1; $i <= 50; $i++) {
    // Usamos el operador modulo para verificar si es par
    if ($i % 2 == 0) {
        // incrementa el contador de pares
        $pares++;
    } else {
        // Incrementa el contador de impares
        $impares++;
    }
}

// imprime los resultados
echo "La cantidad de números pares en el rango del 1 al 50 es: " . $pares ."<br>" ;
echo "La cantidad de números impares en el rango del 1 al 50 es: " . $impares;