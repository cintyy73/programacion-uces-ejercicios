# 1- Ingresar números hasta que se ingrese un número negativo. Mostrar cuántos #números se ingresaron (sin contar el negativo).

count = 0
while True:
    num = int(input("ingrese un número "))
    if num < 0:
        break
    count += 1

print("numeros ingresados = ", {count})

# 2- Adivinar un número secreto (ej: 7). Si acierta, mostrar '¡Correcto!' y salir # con break. Si no, seguir preguntando.

secret = 7
num1 = 0
while True:
    num1 = int(input("Adivina en que número estoy pensando"))
    if num1 == secret:
        print("Correcto")
        break
if num1 != secret:
    num1 = input("incorrecto tenés otro intento")

# 3 - Leer letras hasta que se ingrese la letra 'x'.

letra = "x"
while True:
    letra = input("ingresa una letra")
    if letra == "x":
        print("Correcto")
        break
    else:
        letra = input("incorrecto tenés otro intento")


# 4 - Sumar números hasta que la suma supere 100. Mostrar la suma final y cuántos #números se ingresaron.
total = 0
count = 0
while True:
    num = int(input("ingrese un número"))
    total += num
    if total > 99:
        break
    else:
        count += 1

print("numeros ingresados = ", {count})

# 4 - Sumar números hasta que la suma supere 100. Mostrar la suma final y cuántos #números se ingresaron.
total = 0
count = 0
while True:
    num = int(input("ingrese un número"))
    total += num
    if total > 100:
        break
    else:
        count += 1


print("numeros ingresados = ", {count}, "suma total = ", {total})

# 5 - Repetir el ingreso de contraseñas hasta acertar la correcta ('python123').
password = "1234"
invalid = 3
input_password = ""


while invalid > 0:
    input_password = input("Ingrese su contraseña")
    if password == input_password:
        print("Bienvenido!")
        break
    else:
        invalid -= 1
        if invalid > 0:
            input_password = input(
                f"Contraña incoprrecta! Ingrese nuevamente su contraseña, le quedan {invalid} intentos"
            )
        else:
            print("Usuario bloqueado!")

# 6 - Validar ingreso de número par. Luego, mostrar todos los pares desde 2 hasta ese número.

numbers = []
number = 0
while True:
    number = int(input("ingrese un número"))
    numbers.append(number)
    if number % 2 != 0:
        break
print(numbers)

# 7 - Validar que el número ingresado sea mayor que 10. Contar cuántos múltiplos de 3 hay entre 1 y ese número.
number = int(input("Ingrese un número: "))

if number > 10:
    count = 0
    i = 1

    while i <= number:
        if i % 3 == 0:
            count += 1
        i += 1

    print(f"Cantidad de múltiplos de 3 entre 1 y {number}: {count}")
else:
    print("El número debe ser mayor que 10.")

# 8 - Ingresar 5 números y decir cuántos fueron mayores a 50.
i = 0
numbers = []
count = 0

while i < 5:
    n = int(input("ingrese un nùmero"))
    numbers.append(n)
    i += 1

for number in numbers:
    if number > 50:
        count += 1
print(f"{count} numeros son mayores a 50")

# 9 - Validar que el usuario ingrese un número entre 1 y 20. Luego mostrar cuenta regresiva desde ese número hasta 1.

while True:
    num = int(input("Ingrese un número entre 1 y 20"))

    if 1 <= num <= 20:
        while num >= 1:
            print(num)
            num -= 1
        break
    else:
        print("Error: El número debe estar entre 1 y 20. Intente nuevamente.")

# 10 - Adivinar número del 1 al 10, con máximo 3 intentos.
intentos = 3
secret = 6

while intentos > 0:
    number = int(input(f"Adivina el número tenes {intentos} intentos "))
    intentos -= 1
    if number == secret:
        print("correcto!!")
        break
    elif intentos > 0:
        print("Incorrecto. Intenta nuevamente.")
if intentos == 0 and number != secret:
    print("game-over")
