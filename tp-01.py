# Ejercicio 1: Registro de temperaturas
max_temp = 0
max_dia = 0
suma_temp = 0
supera_30 = 0
bajo_15 = 0
for i in range(7):
    temp = int(input(f"Ingrese la temperatura máxima por cada día: "))
    suma_temp += temp
    if i == 0 or temp > max_temp:
        max_temp = temp
        max_dia = i + 1
    if temp > 30:
        supera_30 += 1
    if temp < 15:
        bajo_15 += 1
print(f"La temperatura más alta fue {max_temp}° el día {max_dia}")
print(f"El promedio fue {suma_temp/7}")
print(f"Días con más de 30°: {supera_30}")
print(f"Días con menos de 15°: {bajo_15}")

# Ejercicio 2: Notas de Alumnos
suma_notas = 0
aprobados = 0
desaprobados = 0
max_nota = None
max_cantidad = 0
hubo_uno = False
for i in range(5):
    nota = int(input(f"Ingrese la nota del alumno (1-10): "))
    while nota < 1 or nota > 10:
        print("Error: la noat debe estar entre 1 y 10.")
        nota = int(input(f"Ingrese la nota del alumno (1-10): "))
    suma_notas += nota
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1
    if i == 0 or nota > max_nota:
        max_nota = nota
        max_cantidad = 1
    elif nota == max_nota:
        max_cantidad += 1
    if nota == 1:
        hubo_uno = True
print(f"Promedio general: {suma_notas/5:.2f}")
print(f"Aprobados: {aprobados}, Desaprobados: {desaprobados}")
print(f"Nota más alta: {max_nota}, cantidad de alumnos: {max_cantidad}")
if hubo_uno:
    print("Hubo al menos un UNO")

# Ejercicio 3: Juego de adivinanza numérica
secreto = 32
acertado = False
for intento in range(1,8):
    num = int(input(f"Intento {intento}/7 - Adivina el número: "))
    if num == secreto:
        print("¡Correcto!")
        acertado = True
        break
    elif num > secreto:
        print("Demaasiado alto")
    else:
        print("Demasiado bajo")
if not acertado:
    print(f"Perdiste. El número {secreto}")
