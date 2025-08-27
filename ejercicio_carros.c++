#include <iostream>
#include <string>


class Carro {
public:
    std::string marca;
    std::string modelo;
    int anio;
    int velocidad;

    void acelerar(int aumento) {
        velocidad += aumento;
    }

    void frenar(int decremento) {
        velocidad -= decremento;
        if (velocidad < 0) {
            velocidad = 0;
        }
    }

    void mostrarInfo() {
        std::cout << "Marca: " << marca << ", Modelo: " << modelo << ", Anio: " << anio << ", Velocidad: " << velocidad << " km/h" << std::endl;
    }
};

int main() {

    Carro miFerrari;
    Carro miHonda;

    
    miFerrari.marca = "Ferrari";
    miFerrari.modelo = "488 GTB";
    miFerrari.anio = 2021;
    miFerrari.velocidad = 0;

    
    miHonda.marca = "Honda";
    miHonda.modelo = "Civic";
    miHonda.anio = 2022;
    miHonda.velocidad = 0;

   
    std::cout << "Informacion del Ferrari:" << std::endl;
    miFerrari.acelerar(100);
    miFerrari.mostrarInfo();

    
    std::cout << "\nInformacion del Honda:" << std::endl;
    miHonda.acelerar(60);
    miHonda.frenar(20);
    miHonda.mostrarInfo();

    return 0;
}