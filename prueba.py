nombre = input("Ingrese su nombre: ")
cedula = int(input("Ingrese su cédula: "))
correo = input("Ingrese su correo: ")
cantidad = int(input("Ingrese el número de hamburguesas a adquirir: "))

print("\nIngrese tipo de hamburguesa")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
tipo_hamburguesa = int(input("Ingrese la opción: "))

match tipo_hamburguesa:
    case 1:
        total = cantidad * 1.50
    case 2:
        total = cantidad * 2.50
    case 3:
        total = cantidad * 3.25
    case _:
        print("\nNo existe ese tipo de hamburguesa")
        print("Muchas gracias")
        exit()

print("\nIngrese forma de pago")
print("1) Tarjeta")
print("2) Efectivo")
pago = int(input("Ingrese la opción: "))

match pago:
    case 1:
        total_descuento = total * 1.05
    case 2:
        total_descuento = total
    case _:
        print("\nNo existe esa forma de pago")
        print("Muchas gracias")
        exit()

print(f"\nGenial {nombre}, el precio final es de: {total_descuento}")
print(f"La factura se enviará a su correo: {correo}")
