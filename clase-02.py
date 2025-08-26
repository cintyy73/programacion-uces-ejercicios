number_01 = int(input("Ingrese un número: "))
number_02 = int(input("Ingrese un número: "))

name = input("Por favor ingerse su nombre: ")
surname = input("Por favor ingerse su apellido: ")
age = input("Por favor ingerse su edad: ")

# 01 - Pide al usuario su nombre y luego mostrarlo por pantalla.
print("1. Bienvenid@ ", name)

# 02 - Pide al usuario su nombre y luego mostrarlo en mayúsculas.
print("2.Bienvenid@ ", name.upper())

# 03 - Pide al usuario su nombre y luego mostrarlo en minúsculas.
print("3.Bienvenid@ ", name.lower())

# 04 - Pide al usuario su nombre y edad, y luego muestra un mensaje que diga "Hola [nombre], tienes [edad] años."
print("4.Hola ", name, " tienes2", age, " años" )

# 05 - Pide al usuario dos números y muestre la suma de ambos, por pantalla.
print("5. ", number_01, " + ", number_02, " = ", (number_01 + number_02))

# 06 - Pide al usuario dos números y muestra la resta del primero menos el segundo.
print("6. ", number_01, " - ", number_02, " = ", (number_01 - number_02))


# 07 - Pide al usuario dos números y muestra el producto de ambos.
print("7. ", number_01, " * ", number_02, " = ", (number_01 * number_02))

# 08 - Pide al usuario dos números y muestra el resultado de dividir el primero entre el segundo.
print("8. ", number_01, " / ", number_02, " = ", (number_01 / number_02))

# 09 - Pide al usuario un número y muestra su cuadrado.
print("9. ", number_01, " al cuadrado es = ", (number_01 ** 2))

# 10 - Pide al usuario un número y muestra su cubo.
print("10. ", number_01, " al cubo es = ", (number_01 ** 3))

# 11 - Pide al usuario su nombre y apellido, y luego muestra un mensaje que diga "Hola [nombre] [apellido]".
print(f"11.Hola {name} {surname}" )

# 12 - Pide al usuario su nombre y luego muestra la longitud de su nombre.
print(f"12.Hola tu nombre tiene  {len(name)} letras" )

# 13 - Pide al usuario su nombre y luego muestra las primeras tres letras de su nombre.
print(f"13.Las primeras 3 letras dde tu nombre son  {(name[:3])}" )

# 14 - Pide al usuario su nombre y luego muestra las últimas tres letras de su nombre.
print(f"14.Las ülltimas 3 letras de tu nombre son  {(name[-3:])}" )


# 15 - Pide al usuario su nombre y luego muestra su nombre al revés.
print(f"15.Así se vería tu nombre al revés {name[::-1]}" )

# 16 - Pide al usuario su nombre y luego muestra un mensaje que diga "Tu nombre tiene [n] letras", donde [n] es la cantidad de letras.
print(f"16.Hola tu nombre tiene  {len(name)} letras" )

# 17 - Pide al usuario su nombre y luego muestra un mensaje que diga "La primera letra de tu nombre es [letra]".
print(f"17.Las primera letra de tu nombre es {(name[0])}" )

# 18 - Pide al usuario su nombre y luego muestra un mensaje que diga "Tu nombre en mayúsculas es [nombre] y en minúsculas es [nombre]".
print(f"18.Hola tu nombre en mayuscuklas {name.upper()} y tu nombre en minúsculas es {name.lower()}")

# 19 - Pide al usuario dos números y verifica si el primero es mayor que el segundo. Muestra True o False.
print(f"19. El número {number_01} es mayor que {number_02} = ", number_01 > number_02)
# 20 - Pide al usuario dos números y verifica si son iguales. Muestra True o False.
print(f"20. El número {number_01} es igual que {number_02} = ", number_01 == number_02)
# 21 - Pide al usuario dos números y verifica si el primero es menor o igual que el segundo. Muestra True o False.
print(f"21. El número {number_01} es menor o igual que {number_02} = ", number_01 <= number_02)
# 22 - Pide al usuario un número y verifica si es positivo. Muestra True o False.
print(f"22. El número {number_01} es positivo = ", number_01 > 0)

# 23 - Pide al usuario un número y verifica si es par. Muestra True o False.
print(f"23. El número {number_01} es par = ", number_01 % 2 == 0)

# 24 - Pide al usuario un número y verifica si es impar. Muestra True o False.
print(f"24. El número {number_01} es impar = ", number_01 % 2 != 0)

# 25 - Pide al usuario un número y verifica si es múltiplo de 5. Muestra True o False.
print(f"25. El número {number_01} es múltiplo de 5 = ", number_01 % 5 == 0)

# 26 - Pide al usuario un número y verifica si está en el rango de 10 a 20 (inclusive). Muestra True o False.
print(f"26. El número {number_01} está netre 10 y 20 = ", number_01 <= 20 and number_01 >= 10)

# 27 - Pide al usuario dos números y verifica si ambos son positivos. Muestra True o False.
print(f"27. El número {number_01} y el número {number_02} son positivos = ", number_01 > 0 and number_02 > 0)
# 28 - Pide al usuario dos números y verifica si al menos uno es positivo. Muestra True o False.
print(f"28. Uno de estos números {number_01} - {number_02} son positivos = ", number_01 > 0 or number_02 > 0)

# 29 - Pide al usuario un número y verifica si no es cero. Muestra True o False.
print(f"29. El número {number_01} es distinto a cero = ", number_01 != 0 )

# 30 - Pide al usuario un número y verifica si es negativo o cero. Muestra True o False.
print(f"30. El número {number_01} es negativo o igual a cero = ", number_01 <= 0)

# 31 - Pide al usuario dos números y verifica si uno es positivo y el otro es negativo. Muestra True o False.
print(f"31. El número {number_01} y el número {number_02} son uno positivo y otro negativo = ", (number_01 > 0 and number_02 < 0) or (number_01 < 0 and number_02 > 0))

# 32 - Pide al usuario un número y verifica si es un número par y positivo. Muestra True o False.
print(f"32. El número {number_01} es par y positivo = ", number_01 % 2 == 0 and number_01>0)

# 33 - Pide al usuario un número y verifica si es un número impar o negativo. Muestra True o False.
print(f"33. El número {number_01} es impar o negativo = ", number_01 % 2 != 0 or number_01<0)
# 34 - Pide al usuario un número y verifica si es un número de una sola cifra (entre 0 y 9). Muestra True o False.
print(f"34. El número {number_01} esde una cifra = ", number_01 < 10 and number_01 >= 0)
# 35 - Pide al usuario un número y verifica si es un número de dos cifras (entre 10 y 99). Muestra True o False.

print(f"35. El número {number_01} está entre 10 y 99 = ", number_01 >= 10 and number_01 < 100)