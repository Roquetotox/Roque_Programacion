#include <iostream>
#include <string>

// Definicion de la clase CuentaBancaria
class CuentaBancaria {
private:
    std::string numeroDeCuenta;
    std::string nombreDelTitular;
    double saldo;

public:
    // Constructor
    CuentaBancaria(std::string numCuenta, std::string titular) {
        numeroDeCuenta = numCuenta;
        nombreDelTitular = titular;
        saldo = 0.0;
        std::cout << "Cuenta creada para " << nombreDelTitular << "." << std::endl;
    }

    // Metodo para depositar
    void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            std::cout << "Deposito de $" << cantidad << " realizado. Saldo actual: $" << saldo << "." << std::endl;
        } else {
            std::cout << "Error: La cantidad a depositar debe ser positiva." << std::endl;
        }
    }

    // Metodo para retirar
    void retirar(double cantidad) {
        if (cantidad > 0) {
            if (cantidad <= saldo) {
                saldo -= cantidad;
                std::cout << "Retiro de $" << cantidad << " realizado. Saldo actual: $" << saldo << "." << std::endl;
            } else {
                std::cout << "Error: Fondos insuficientes para realizar el retiro." << std::endl;
            }
        } else {
            std::cout << "Error: La cantidad a retirar debe ser positiva." << std::endl;
        }
    }

    // Metodo para obtener el saldo (const)
    double obtenerSaldo() const {
        return saldo;
    }

    // Metodo para mostrar la informacion de la cuenta (const)
    void mostrarInformacion() const {
        std::cout << "\n--- Informacion de la Cuenta ---" << std::endl;
        std::cout << "Numero de cuenta: " << numeroDeCuenta << std::endl;
        std::cout << "Titular: " << nombreDelTitular << std::endl;
        std::cout << "Saldo actual: $" << saldo << std::endl;
        std::cout << "--------------------------------" << std::endl;
    }
};

int main() {
    // 1. Crear un objeto de la clase CuentaBancaria
    CuentaBancaria miCuenta("987654321", "Maria Lopez");

    // 2. Mostrar informacion inicial
    miCuenta.mostrarInformacion();

    // 3. Realizar un deposito
    miCuenta.depositar(750.0);

    // 4. Intentar un retiro con fondos insuficientes
    miCuenta.retirar(1000.0);

    // 5. Realizar un retiro valido
    miCuenta.retirar(150.0);

    // 6. Mostrar el estado final de la cuenta
    miCuenta.mostrarInformacion();

    return 0;
}