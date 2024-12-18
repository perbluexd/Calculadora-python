# -*- coding: utf-8 -*-

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Operaciones matemáticas
def suma():
    a = obtener_numero("Ingresa el primer número para la suma: ")
    b = obtener_numero("Ingresa el segundo número para la suma: ")
    return f"La suma es: {a + b}"

def resta():
    a = obtener_numero("Ingresa el primer número para la resta: ")
    b = obtener_numero("Ingresa el segundo número para la resta: ")
    return f"La resta es: {a - b}"

def multiplicacion():
    a = obtener_numero("Ingresa el primer número para la multiplicación: ")
    b = obtener_numero("Ingresa el segundo número para la multiplicación: ")
    return f"La multiplicación es: {a * b}"

def division():
    a = obtener_numero("Ingresa el primer número para la división: ")
    while True:
        b = obtener_numero("Ingresa el segundo número para la división: ")
        if b == 0:
            print("El divisor no puede ser 0. Por favor, intenta de nuevo.")
        else:
            break
    return f"La división es: {a / b}"

# Menú principal
def menu():
    while True:
        opcion = input("""
        Te presento las opciones disponibles en nuestra calculadora:
            1. suma
            2. resta
            3. multiplicación
            4. división
            5. salir
        Por favor, selecciona una opción: """).lower()
        
        if opcion == "1" or opcion == "suma":
            print(suma())
        elif opcion == "2" or opcion == "resta":
            print(resta())
        elif opcion == "3" or opcion == "multiplicación":
            print(multiplicacion())
        elif opcion == "4" or opcion == "división":
            print(division())
        elif opcion == "5" or opcion == "salir":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
    
    
