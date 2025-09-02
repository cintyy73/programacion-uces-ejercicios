num = int(input("Ingrese un número: "))
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número "))

# 1.Pide al usuario dos números y verifica si el primero es mayor que el segundo. Muestra True o False.
print("1. el primero es mayor que el segundo.", num2, "=", num1 > num2)

# 2.Pide al usuario dos números y verifica si son iguales. Muestra True o False.
print("2. son iguales: ", num1 == num2)

# 3.Pide al usuario dos números y verifica si el primero es menor o igual que el segundo. Muestra True o False.
print("3. primero es menor o igual que el segundo: ", num1 <= num2)

# 4.Pide al usuario un número y verifica si es positivo. Muestra True o False.
print("4- es positivo =", num > 0)

# 5.Pide al usuario un número y verifica si es par. Muestra True o False.
print("5. es par: ", num % 2 == 0)

# 6.Pide al usuario un número y verifica si es impar. Muestra True o False.
print("6- es impar =", num % 2 != 0)

# 7.Pide al usuario un número y verifica si es múltiplo de 5. Muestra True o False.
print("7- es múltiplo de 5 =", num % 5 == 0)

# 8.Pide al usuario un número y verifica si está en el rango de 10 a 20 (inclusive). Muestra True o False.
print("8está entre 10 y 20 =", 10 <= num <= 20)

# 9.Pide al usuario dos números y verifica si ambos son positivos. Muestra True o False.
print("9. Ambos son positivos =", num1 > 0 and num2 > 0)

# 10.Pide al usuario dos números y verifica si al menos uno es positivo. Muestra True o False.
print("10. Al menos uno es positivo =", num1 > 0 or num2 > 0)

# 11.Pide al usuario un número y verifica si no es cero. Muestra True o False.
print("11- es distinto de cero =", num != 0)

# 12.Pide al usuario un número y verifica si es negativo o cero. Muestra True o False.
print("12- es negativo o cero =", num <= 0)

# 13.Pide al usuario dos números y verifica si uno es positivo y el otro es negativo. Muestra True o False.
print(
    "13-- Uno es positivo y el otro negativo =",
    (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0),
)

# 14.Pide al usuario un número y verifica si es un número par y positivo. Muestra True o False.
print("14- es par y positivo =", num % 2 == 0 and num > 0)

# 15.Pide al usuario un número y verifica si es un número impar o negativo. Muestra True o False.
print("15- es impar o negativo =", num % 2 != 0 or num < 0)

# 16.Pide al usuario un número y verifica si es un número de una sola cifra (entre 0 y 9). Muestra True o False.
print("16- es de una sola cifra =", 0 <= num < 10)

# 17.Pide al usuario un número y verifica si es un número de dos cifras (entre 10 y 99). Muestra True o False.
print("17- es de dos cifras =", 10 <= num < 100)

# 18.Escribir un programa que pida un número y determine si es positivo, negativo o cero.
if num > 0:
    print("18- es positivo")
elif num < 0:
    print("18- es negativo")
else:
    print("18- es cero")

# 19.Crear un programa que pida tres números y muestre cuál es el mayor.
print("19. El mayor es:", max(num1, num2, num3))

# 20.Pedir al usuario 5 números y contar cuántos son pares.
pares = 0
for i in range(5):
    num = int(input(f"220 - Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
print("20. Cantidad de pares:", pares)

# 21.Pedir al usuario 10 números y sumar solo los impares.
suma_impares = 0
for i in range(10):
    num = int(input(f"Ingrese un número {i+1}: "))
    if num % 2 != 0:
        suma_impares += num
print("21. Suma de impares:", suma_impares)

# 22.Contar cuántos números menores a 50 hay en una lista dada.
lista = [1, 27, 38, 4, 51, 60, 12, 49, 100, 3]
menores_50 = sum(1 for x in lista if x < 50)
print("22. Números menores a 50:", menores_50)

# 23.Sumar todos los múltiplos de 3 en un rango de 1 a 100.
suma_mult_3 = sum(x for x in range(1, 101) if x % 3 == 0)
print("23. Suma de múltiplos de 3 entre 1 y 100:", suma_mult_3)

# 24.Contar cuántas palabras tienen más de 5 letras en una lista de palabras.
palabras = ["manzana", "sol", "computadora", "casa", "universidad", "perro", "gato"]
mas_5 = sum(1 for palabra in palabras if len(palabra) > 5)
print("24. Palabras con más de 5 letras:", mas_5)

# 25.Escribir un programa que pida un número y muestre si es par o impar.
if num % 2 == 0:
    print("25- es par")
else:
    print("25- es impar")


# 26.Contar cuántos números primos hay en un rango de 1 a 50.

# ?



# 27.Crear un programa que calcule el promedio de 10 números ingresados por el usuario.
suma = 0
for i in range(10):
    num = int(input(f"Ingrese un número {i+1}: "))
    suma += num
print("27. Promedio:", suma / 10)

# 28.Pedir al usuario su edad y decir si es niño (menor de 12), adolescente (12-17), adulto (18-64) o anciano (65+).
edad = int(input(" 28 - Ingrese su edad: "))
if edad < 12:
    print("28. Niño")
elif edad < 18:
    print("28. Adolescente")
elif edad < 65:
    print("28. Adulto")
else:
    print("28. Anciano")

# 29.Contar cuántos alumnos sacaron más de 90 en un examen.
notas = [95, 87, 92, 78, 100, 65, 91, 89, 93, 88]
mas_90 = sum(1 for nota in notas if nota > 90)
print("29. Alumnos con nota mayor a 90:", mas_90)

# 30.Pedir números al usuario hasta que ingrese un número negativo, luego mostrar la suma de todos los positivos ingresados.
suma = 0
while True:
    num = int(input("se sumna sus ingresos hasta que un número negativo terminar): "))
    if num < 0:
        break
    suma += num
print("30. Suma de positivos ingresados:", suma)

# 31.Escribir un programa que cuente cuántas vocales hay en una palabra ingresada por el usuario.
palabra = input("31 - Ingrese una palabra: ").lower()
vocales = sum(1 for letra in palabra if letra in "aeiou")
print("31. Cantidad de vocales:", vocales)

# 32.Pedir 5 números y determinar cuántos son mayores que el promedio de los cinco.
numeros = []
for i in range(5):
    num = int(input(f"Ingrese un número {i+1}: "))
    numeros.append(num)
prom = sum(numeros) / 5
mayores = sum(1 for n in numeros if n > prom)
print("32. Mayores que el promedio:", mayores)

# 33.Sumar todos los números entre 1 y 1000 que sean divisibles por 5.
suma = 0
for x in range(1, 1001):
    if x % 5 == 0:
        suma += x
print("33. Suma de números divisibles por 5 entre 1 y 1000:", suma)
