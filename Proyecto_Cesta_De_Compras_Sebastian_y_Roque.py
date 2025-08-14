# simulador de cesta de compras
cesta = [] #aqui se guarda todo lo que el usuario va agregando

def mostrar_menu():
    # Muestra las opciones del menu cada vez
    print("\nMENU PRINCIPAL")
    print("1. Agregar producto")
    print("2. Mostrar cesta")
    print("3. Eliminar producto")
    print("4. Calcular total")
    print("5. Renunciar")

def agregar_producto():
    # pide el nombre y el precio del producto
    nombre = input("Escribe el nombre del producto rapido que se acaban, la vaina esta arrecha: ")
    try:
        precio = float(input("Escribe el precio del producto: "))
        cesta.append({"nombre": nombre, "precio": precio}) #lo guarda en la lista
        print("El producto se agrego correctamente, que mas te vais a llevar.")
    except:
        # si el precio no es un numero,manda un mensaje de error
        print("error, ese no es el precio del producto.")

def mostrar_cesta():
    #muestra lo que hay en la cesta
    if len(cesta) == 0:
        print("la cesta esta mas vacia que la vaina.")
    else:
        print("Esto es todo lo que llevais en la cesta:")
        for i, producto in enumerate(cesta):
            # muestra cada producto con su precio
            print(f"{i+1}. {producto['nombre']} - ${producto['precio']}")

def eliminar_producto(): #busca el producto por el nombre y lo eliminaa
    nombre = input("Escribe el nombre del producto que ya no te quereis llevar: ")
    encontrado = False
    for producto in cesta:
        if producto["nombre"].lower() == nombre.lower():
            cesta.remove(producto) # saca de la list4
            print("el producto se elimino de tu cesta.")
            encontrado = True
            break
    if not encontrado: #si no encuentra avisa que no lo encontro
        print("no se encontro ese producto.")

def calcular_total():
    #suma los precios y muestra el total
    total = 0
    for producto in cesta:
        total += producto["precio"]
    print(f"total que teneis que pagar sin chiguireo: ${total}")

# aqui mantemos el programa corriendo gracias al bucle
while True:
    mostrar_menu()
    opcion = input("Elige una opcion (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_cesta()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        calcular_total()
    elif opcion == "5":
        #mensaje de chao
        print("gracias por usar el programa, estamos bien,vuelve pronto.")
        break
    #si el usuario pone algo que no esta en el menu ps
    else:
        print("Opcion invalida, intenta otra vez.")

