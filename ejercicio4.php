<?php

// Creamos la variable para que acumule la suma
$suma_impares = 0;

// recorre los numeros del 1 al 100
for ($i = 1; $i <= 100; $i++) {
    // comprabamos que el numero actual sea impar
    if ($i % 2 != 0) {
        // si es impar,sumarlo a la variable acumuladora
        $suma_impares += $i;
    }
}

// mostrar el resultado final
echo "La suma de todos los números impares del 1 al 100 es: {$suma_impares}\n";

?>