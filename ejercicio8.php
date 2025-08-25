<?php

// Bucle para iterar del 1 al 30
for ($i = 1; $i <= 30; $i++) {
    // Si el numero es multiplo de 3 y 5
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "MarTierra\n";
    // Si el numero es solo multiplo de 3
    } elseif ($i % 3 == 0) {
        echo "Mar\n";
    // si el numero es solo multiplo de 5
    } elseif ($i % 5 == 0) {
        echo "Tierra\n";
    // si el numero no es multiplo de 3 ni de 5
    } else {
        echo $i . "\n";
    }
}

?>