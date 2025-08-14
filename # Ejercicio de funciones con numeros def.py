# Ejercicio de funciones con numeros definidos
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

print("Calculadora basica en Python")
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
print("\nResultados:")
print(f" + Suma: {sumar(num1, num2)}")
print(f" - Resta: {restar(num1, num2)}")
print(f" x Multiplicación: {multiplicar(num1, num2)}")
print(f" / División: {dividir(num1, num2)}")



