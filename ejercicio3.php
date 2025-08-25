<?php
// definamos el numero secreto y el contador de intentos
$numero_secreto = 7;
$intento = 0;

// Usamos el bucle while para intentar adivinar el numero
while ($intento != $numero_secreto) {
    //incrementa el contador de intentos
    $intento++;
    echo "Intentando adivinar... Intento número {$intento}\n";
}

// mensaje al adivinar el numero
echo "¡Felicidades! El número secreto es {$numero_secreto} y lo adivinaste en {$intento} intentos.\n";

?>