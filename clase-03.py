# suma = 0
# n_1 = int(input("ingrese un número "))
# n_2 = int(input("ingrese un número "))
# n_3 = int(input("ingrese un número "))
# n_4 = int(input("ingrese un número "))
# n_5 = int(input("ingrese un número "))
# n_6 = int(input("ingrese un número "))

# 01 - Armar un algoritmo para que  permita ingresar 5 números y calcular la suma de todos ellos. Mostrar el resultado por pantalla.
# 02 - Modificar el algoritmo anterior para que  permita ingresar un sexto número y calcule la suma de los 3 primeros y la multiplicación de los 3 últimos números

# suma =   n_1 + n_2 + n_3 + n_4 + n_5
# suma_2 = n_1 + n_2 + n_3
# mult = n_4 * n_5 * n_6
# print(suma, suma_2, mult)

# 03 - Armar un algoritmo para que  permita ingresar 3 números y muestre por pantalla la suma de ellos, luego ingresar 2 números y mostrar por pantalla la resta de ellos. Con los resultados obtenidos imprimir la suma.
# suma =   n_1 + n_2 + n_3
# resta = n_4 - n_5
# print(suma, resta)

# 04 - Armar un algoritmo que  permita leer el nombre, edad y peso de una persona y posteriormente imprimirla. Validar los datos de entrada y solicitar al usuario si quiere realizar otro ingreso.

# edad = int(input("ingrese su edad "))

# nombre = str(input("ingrese su nombre ")).strip()
# peso = int(input("ingrese su peso"))

# print(f"{nombre}: edad: {edad} peso: {peso}")

# continua= int(input("ingrese 1 si desea realizar otro proceso o 0 para salir"))
# if continua == 1:
#     edad = int(input("ingrese su edad "))
#     nombre = str(input("ingrese su nombre "))
#     peso = int(input("ingrese su peso "))
#     print(f"{nombre}: edad: {edad} peso: {peso}")
# else:
#     print('muchas gracias')


# 05 - Armar un algoritmo que, dado dos valores de entrada, imprima siempre la división del mayor entre el menor.
# cociente = 0

# if n_1 > n_2:
#     cociente = n_1 / n_2
# else:
#     cociente =  n_2 / n_1
# print(cociente)

# 06 - Armar un algoritmo que lea de entrada tres  números y que indique cual es el mayor de ellos. Mostrar el resultado por pantalla e impresora.

# if n_1 > n_2 > n_3 :
#     print(f"{n_1} es mayor")
# elif n_2 > n_3 :
#     print(f"{n_2} es mayor")
# elif n_3 > n_2 :
#     print(f"{n_3} es mayor")


# 07 - Armar un algoritmo que permita ingresar dos números positivos e imprimir la suma. Verificar que sean positivos, en caso contrario mostrar por pantalla un mensaje de error y volver a pedir el número.
suma = 0
n_1 = int(input("ingrese un número positivo "))

if n_1 > 0:
    n_2 = int(input("ingrese un número "))
    if n_2 > 0:
        suma = n_1 + n_2
        print(suma)
else:
    print(" el número debe ser positivo")
n_2 = int(input("ingrese un número positivo "))


# 08 - Modificar el algoritmo anterior para que el usuario pueda realizar otra suma sin finalizar el programa.

# suma = 0
# n_1 = int(input("ingrese un número positivo "))

# if n_1 > 0:
#     n_2 = int(input("ingrese un número "))
#     if n_2 > 0:
#         suma = n_1 + n_2
#         print(suma)
# else:
#     print(" el número debe ser positivo")

# 09 - Armar un algoritmo que pida la edad y el sexo; imprimir el Sexo y si puede votar o no. Pueden votar los mayores de 18 años.

# 10 - Armar un algoritmo que intercambie el valor entre dos datos. Ejemplo, si A=2 y B=5, deberá mostrar B=2 y A=5. Las variables se ingresan por teclado.


# 11 - Armar un algoritmo que pida el N.º. de legajo, nombre, apellido, curso, año y tres notas de un alumno. Mostrar en la pantalla el promedio de las tres notas con los datos del alumno. Validar las notas entre 1-10.


# 12 - Modificar el algoritmo anterior para que   permita al usuario calcular el promedio de otro alumno y también permita mostrar el resultado por pantalla o por impresora.


# 13 - Armar un algoritmo que permita ingresar por teclado el Código, Descripción y Cantidad en Stock de un artículo de librería y que pueda imprimirse. Verificar que el código se encuentre entre 100 y 998, la descripción sea distinta que espacio y el stock se encuentre entre 0-99. El programa finaliza cuando el usuario ingresa como código el 999.

# 14 - Hacer un algoritmo que lea dos números N1 y N2, si N1 es mayor que N2 que muestre la suma de los dos números, si N1 es menor que N2 muestre el producto de los dos números, si son iguales ingresar un tercer número y determinar cuál es el mayor.


# 15 - Hacer un algoritmo que lea un número N si este es mayor o igual a 100  muestre el triple del número y si es menor que 100 muestre el cuadrado del número. Si es igual que cero sumarle 100 y verificar las condiciones anteriores.


# 16 - Hacer un algoritmo que lea un número N si este es par se incrementa en un 20 %  y si N es impar hay un decremento del 5 %  . Mostrar el nuevo valor de N por pantalla. El programa finaliza cuando el usuario ingresa un número mayor a 100.

# 17 - Armar un algoritmo que pida 30 números y muestre la suma y el promedio de dichos números.

# 18 - Armar un algoritmo para imprimir la suma de los números del 1 al 100.

# 19 - Armar un algoritmo que sume los primeros 50 números y que los imprima.

# 20 - Armar un algoritmo que reciba como entrada un cierto valor numérico y genere como salida N veces la palabra “HOLA” por impresora.


# 21 - Armar un algoritmo que obtenga el sueldo neto de un trabajador cuyo sueldo base se obtiene por teclado y teniendo en cuenta que si ese sueldo es mayor a $ 200.000 y menor $ 500.000 tiene una retención del 10%, si es mayor o igual a $ 500.000 la retención es del 5% en caso contrario es de 3%.

# 22 - Armar un algoritmo   donde nos calcule el dinero total a devolver cuando se pide un crédito bancario. Teniendo en cuenta el estado civil del usuario a la hora de pedir el crédito. TOTAL=PRESTADO*ESTADO      CIVIL      (CASADO=10%,      SOLTERO=40%,      VIUDO=5%0, DIVORCIADO=30%, SEPARADO=40%)


# 23 - Armar un algoritmo que sume los valores que se van introduciendo por teclado mientras que el usuario no introduzca cero. Debemos ir mostrando el subtotal de cada valor
