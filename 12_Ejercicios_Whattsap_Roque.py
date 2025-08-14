#Primer Ejercicio Calculadora de propinas
costo=float(input("Ingresa el costo de la comida: "))
propina = 0.15
Montopropina =costo * propina
total = costo + propina
print ("Costo de la comida:", costo)
print ("Propina (15%):", Montopropina)
print ("Total a pagar:", total)
#Segundo ejercicio Informacion Personal 
# El usuario ingresa su nombre
Nombre = str(input("Ingrese su Nombre"))
# El usuario ingresa su edad
Edad = int(input("Ingrese su edad"))
# El usuario ingresa la ciudad en la que vive
Ciudad = str (input("Ingrese la ciudad donde vive"))
# Es enviado un texto con los datos del usuario
print(f"Hola {Nombre} Bienvenido a Diversilandia, Segun tus datos tienes {Edad} años y vives en la ciudad de {Ciudad}. Bienvenido a esta nueva aventura y espero que la pases bien! ")

#Tercer ejercicio de Conversor de tempreratura
# Se le pide al usuario ingresar la temperatura en grados celsius
celsius = float(input("Ingresa la temperatura en Grados Celsius"))
# Se realiza la formula para convertir grados Celsius en Grados Fahrenheit
Fahrenheit = (celsius*9/5)+32
# Se le da al usuario el Resultado de la formula
print(f"Los {celsius} Grados celsius es la temperatura de {Fahrenheit} Grados Fahrenhei")
#Cuarto Ejercicio
# Ingresa el año de tu nacimiento
AñodeN = int(input("Ingrese tu año de nacimiento"))
# Año actual
AñoA = 2025
# La edad del usuario es el resultado de la resta del año actual con el año de su nacimiento

Edad = AñoA - AñodeN
#Si el usuario es mayor o igual que 18 dira verdadero, si el usuario es menor que 18 dira que es falso

Mayor = Edad>= 18
print("Eres mayor de edad?", Mayor)
#Ejercicio 5
base = float(input("Ingresa la base del rectangulo"))
altura = float(input("Ingrese la altura del rectangulo"))
area= base*altura
perimetro = 2 *(base+altura)
print("Area del rectangulo:", area)
print("perimetro del rectangulo:", perimetro)

#Ejercicio 6 Clasificador de numeros + y -
#LE PIDE AL USUARIO QUE INGRESE UN NUMERO
numero = float(input("Ingresa un numero: "))
#SI EL NUMERO ES MAYOR QUE 0 ES POSITIVO
if numero > 0:
    print("El numero es positivo.")
    # SI EL NUMERO ES MENOR A 0 ES NEGATIVO
elif numero < 0:
    print("El numero es negativo.")
    # SI EL USUARIO ESCRIBE EL NUMERO 0 LE DIRA QUE EL NUMERO ES 0 YA QUE 0 NO ES NI POSITIVO NI NEGATIVO, ES 0

else:
    print("El numero es cero.")

#Ejercicio 7  acceso a fiesta exclusiva

edad = float(input("Ingrese su edad"))
esta_en_la_lista = True
if edad >= 18 and esta_en_la_lista:
    print("Bienvenido a la fiesta,eres mayor de edad y estas en la lista de invitado. Pasala bien")
else:
    print("Acceso Denegado,Eres menor de edad y no estas en la lista de invitados")

#Ejercicio 8 sistema de calificaciones
# se le solicita la nota al usuario
nota = int(input("Ingresa tu nota (0-100): "))
# ahora se convierte de nota a letra
#si la nota es mayor o igual que 90 tiene A
if nota >= 90:
    print("Felicidades, tienes la calificacion: A")
    # Si la nota es mayor o igual que 80 tiene B
elif nota >= 80:
    print("Felicidades tienes la calificacion: B")
    #Si la nota es mayor o igual a 70 tiene C
elif nota >= 70:
    print("Tienes : C de calificacion")
# si la nota es mayor o igual que 60 tiene D
elif nota >= 60:
    print("No estuvo mal pero tienes que mejorar, Tienes de Calificacion: D")
    #Si la nota esta por debajo de 60 tiene F
else:
    print("Trata de esforzarte para la proxima Tienes : F")

#Ejercicio 9 descuento en tienda

#Se le solicita el precio de su compra
precio = float(input("Ingresa el precio de tu compra ($): "))

# calculamos el descuento
if precio >= 100:
    descuento = 0.20
elif precio >= 50:
    descuento = 0.10
else:
    descuento = 0.0
# precio final
precio_final = precio - (precio * descuento)

# Se le muestra al cliente el precio final
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Precio final: ${precio_final}")

# Ejercicio 10 verificador de año bisiesto

# se le pide al usuario que ingrese el año
año = int(input("Ingresa un año: "))

# Verificamos si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    #Aqui necesite ayuda de chat gpt para que me ayude con la formula para saber si es bisiesto o no es bisiesto

    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

# Ejercicio 11 suma de elementos con bucle for
# Creaamos una lista de numeros
numeros = [4, 7, 2, 9, 5]

# creamos una variable para acumularla suma
suma_total = 0

# Recorremos la lista con un bucle for
for numero in numeros:
    suma_total += numero

# mostramos el resultado
print("✅ La suma de los elementos es:", suma_total)

#Ejercicio 12 juego de adivinar con bucle while

# definimos el numero secreto
numero_secreto = 8

print("Adivina el numero secreto (entre 1 y 10)")

while True:
    intento = int(input("Ingresa tu numero: "))
    
    if intento == numero_secreto:
        print("Correcto, Has adivinado el numero.")
        break
    elif intento < numero_secreto:
        print("Muy bajoo, Intenta de nuevo")
    else:
        print("Muy alto, Intenta de nuevo")








