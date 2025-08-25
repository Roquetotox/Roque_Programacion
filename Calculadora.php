<?php

// funcion para sumar los 2 numeros
function sumar($num1, $num2) {
    return $num1 + $num2;
}

// funcion para restar los 2 numeros
function restar($num1, $num2) {
    return $num1 - $num2;
}

// funcion para multiplicar los 2 numeros
function multiplicar($num1, $num2) {
    return $num1 * $num2;
}

// funcion para dividir los 2 numeros
function dividir($num1, $num2) {
    if ($num2 == 0) {
        return "Error: No se puede dividir por cero.";
    } else {
        return $num1 / $num2;
    }
}

// bucle principal para que la calculadora siga funcionando
do {
    // Menu de opciones
    echo "\n--- Calculadora Interactiva ---\n";
    echo "Elige una operación:\n";
    echo "1. Sumar\n";
    echo "2. Restar\n";
    echo "3. Multiplicar\n";
    echo "4. Dividir\n";
    echo "5. Salir\n";
    
    // captura la opción del usuario
    $opcion = readline("Introduce el numero de la operacion: ");
    
    // Si la opcion es "5", salimos del bucle
    if ($opcion == 5) {
        echo "Gracias por usar la calculadora. Saliendo...\n";
        break;
    }

    // Si la opcion no es "5", pedimos los numeros
    if ($opcion >= 1 && $opcion <= 4) {
        $numero1 = (float) readline("Introduce el primer numero: ");
        $numero2 = (float) readline("Introduce el segundo numero: ");

        switch ($opcion) {
            case 1:
                $resultado = sumar($numero1, $numero2);
                echo "Resultado: " . $numero1 . " + " . $numero2 . " = " . $resultado . "\n";
                break;
            case 2:
                $resultado = restar($numero1, $numero2);
                echo "Resultado: " . $numero1 . " - " . $numero2 . " = " . $resultado . "\n";
                break;
            case 3:
                $resultado = multiplicar($numero1, $numero2);
                echo "Resultado: " . $numero1 . " * " . $numero2 . " = " . $resultado . "\n";
                break;
            case 4:
                $resultado = dividir($numero1, $numero2);
                echo "Resultado: " . $numero1 . " / " . $numero2 . " = " . $resultado . "\n";
                break;
        }
    } else {
        echo "Opcion no valida por favor elige un numero del 1 al 5.\n";
    }

} while (true);
?>