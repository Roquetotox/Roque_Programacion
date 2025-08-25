<?php

//temperatura en grados Celsius
$temperatura = 15; 

// para clasificar la temperatura
if ($temperatura < 10) {
    echo "Fría";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "Templada";
} else {
    echo "Calurosa";
}

?>