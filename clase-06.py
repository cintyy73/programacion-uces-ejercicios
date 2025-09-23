### Ejercicio 1 - resuelto
# Ingresar un número del 1 al 7 e imprimir el día correspondiente
dia = int(input("Ingrese un número del 1 al 7: "))
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido")

#ejercicio 6 clase 05
numbers = []
number = int(input("Ingrese un número: "))
if number % 2 == 0:
    for i in range(number):
        if i % 2 == 0 and i != 0:
            numbers.append(i)
    print(numbers)
else:
    print("El número ingresado no es par.")

### Ejercicio 2 - resuelto

# Menú de opciones con match-case
print("1. Sumar")
print("2. Restar")
opcion = int(input("Ingrese una opción: "))
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

match opcion:
    case 1:
        print("Resultado:", a + b)
    case 2:
        print("Resultado:", a - b)
    case _:
        print("Opción inválida")

### Ejercicio 3 - resuelto

# Verificar si una letra es vocal o consonante
letra = input("Ingrese una letra: ").lower()

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Es vocal")
    case _:
        print("Es consonante")

### Ejercicio 4

# 4. Ingresar un número del 1 al 12 y mostrar el nombre del mes correspondiente usando match case.
month = int(input("Ingrese el número del mes: "))
match month:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case _:
        print("Opción inválida")

### Ejercicio 5

# 5. Pedir un código de operación (A, B, C) y mostrar una descripción distinta para cada uno.
option = input("Ingrese A, B, C: ").upper()
match option:
    case "A":
        print("Estamos en verano")
    case "B":
        print("Estamos en otoño")
    case "C":
        print("Estamos en primavera")
    case _:
        print("Opción inválida")

### Ejercicio 6

# 6. Ingresar un número del 1 al 4 y mostrar una estación del año.
option = int(input("Ingrese un número del 1 al 4: "))
match option:
    case 1:
        print("Verano")
    case 2:
        print("Otoño")
    case 3:
        print("Primavera")
    case 4:
        print("Invierno")  # Corregido a invierno, ya que estaba repitiendo verano
    case _:
        print("Elige del 1 al 4")

### Ejercicio 7

# 7. Pedir al usuario una nota del 1 al 10 y mostrar si está aprobado, desaprobado o sobresaliente.
test = int(input("Ingrese su nota de 1 a 10: "))
match test:
    case 1 | 2 | 3 | 4 | 5 | 6:
        print("Desaprobado")
    case 7:
        print("Aprobado")
    case 8 | 9 | 10:
        print("Sobresaliente")
    case _:
        print("Nota fuera de rango")

### Ejercicio 8

# 8. Crear un sistema de clasificación de IMC usando match-case (bajo peso, normal, sobrepeso, obesidad).
try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura*altura)
    
    match True:
        case _ if imc < 18.5:
            print("Bajo peso")
        case _ if imc < 25:
            print("Peso normal")
        case _ if imc < 30:
            print("Sobrepeso")
        case _:
            print("Obesidad")
except ValueError:
    print("Por favor ingrese valores numéricos válidos")
except ZeroDivisionError:
    print("La altura no puede ser cero")

# se desea registrar la calificacion que 6 personas dan a una pelicula (entre 1 y10 )
#validar calificacion
#calcular el promedio de calificaiones
#contar cuantas personas pusieron una nota mayor a 7
#detectar si alguna persona puso 1  mostrar mensaje cirtica muy negativa
califications = 0
calification = 0
quantity = 6
count = 0
count_aprobed = 0
negative_values = 0
while count < quantity:
    try:
        calification = int(input(f"Ingrese calificación de persona {count+1} (1-10): "))
        if 1 <= calification <= 10:
            califications += calification
            count += 1

            if calification > 7:
                count_aprobed += 1

            if calification == 1:
                print("¡ALERTA! Crítica muy negativa")
                negative_values += 1
        else:
            print("Error: La calificación debe estar entre 1 y 10")
    except ValueError:
        print("Error: Debe ingresar un número entero")

if count > 0:
    promedio = califications / quantity
    print("Resultados:")
    print(f"Promedio de calificaciones: {promedio:.2f}")
    print(f"Personas que calificaron con más de 7: {count_aprobed}")
    print(f"Cantidad de críticas muy negativas: {negative_values}")
else:
    print("No se registraron calificaciones válidas")

### Ejercicio 9

# 9. Ingresar el nombre de una fruta y mostrar el precio por kilo. Usar al menos 4 frutas distintas.

fruit = input("¿Qué precio desea averiguar? ").lower()
match fruit:
    case "banana":
        print("$19.99")
    case "anana":
        print("$29.99")
    case "manzana":
        print("2 x $19.99")
    case "naranja":
        print("$15.99")
    case _:
        print("No tenemos stock de esa fruta")



### Ejercicio 10

# 10. Pedir un día de la semana y clasificarlo como día laboral o fin de semana.
dia = input("Ingrese un día de la semana: ").lower()
match dia:
    case "lunes" | "martes" | "miercoles" | "miércoles" | "jueves" | "viernes":
        print("Día laborable")
    case "sabado" | "sábado" | "domingo":
        print("Día no laborable")
    case _:
        print("Día no válido")

