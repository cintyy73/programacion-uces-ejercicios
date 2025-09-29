# Ejercicio Nº1: Control de Gastos Semanal 
# Una persona quiere llevar un registro de sus gastos diarios en transporte durante una semana (7 días).
# ●Ingresar el gasto de transporte de cada día.
# ●Validar que el gasto ingresado no sea un número negativo.
# ●Calcular el gasto total de la semana.
# ●Determinar cuál fue el día de mayor gasto.
# ●Informar si algún día el gasto superó los $1500.

value = 0
total_value =0
max_value = 0
max_day = 0
sup = 0

for i in range(1, 8):
  value = int(input(f"ingrese gastos del día {i} "))
  if value > 0 :
    total_value += value
    if value > max_value :
      max_value = value
      max_day = i
    if value > 1500 :
      sup += 1
  else:
    print(f"ingrese un valor válido para gastos del día {i} ")

print(f"Día de mayor gasto {max_day} ")
print(f"Mayor gasto {max_value} ")
print(f"Total semanal de gastos {total_value} ")
print(f" {sup} días los gastos fueron mayores a $1500 ")


# Ejercicio Nº2: Registro de Temperaturas 
# Se necesita registrar la temperatura máxima de 5 ciudades diferentes en un día.
# ●Ingresar el nombre y la temperatura máxima de cada ciudad.
# ●Validar que la temperatura se encuentre en un rango razonable (por ejemplo, entre -10 y 45 grados).
# ●Calcular la temperatura promedio entre todas las ciudades.
# ●Encontrar la ciudad con la temperatura más alta.
# ●Contar cuántas ciudades tuvieron una temperatura superior a 30 grados.
city_name = ""
city_temp = 0
temp_prom = 0
city_max_temp = 0
city_max_name = ""
count_max = 0
total_temp = 0

for i in range(1, 6):
    name = input(f"ingrese la ciudad a registrar ")
    value = int(input(f"ingrese la temperatura de {name} "))

    while value < -10 or value > 45:
      print(f"ingrese una temperatura valida para  {name} ")
      value = int(input(f"ingrese la temperatura de {name} "))

    total_temp += value

    if city_max_temp < value :
      city_max_temp = value
      city_max_name = name

    if value > 30 :
      count_max += 1

temp_prom = total_temp / 5  
print(f"{city_max_name} registró la máxima temperatuira con un valor de {city_max_temp}, en los útlimos 5 días el promedio de temperaturas fue de {temp_prom}, con {count_max} días superiores a 30°")


# Ejercicio Nº3: Encuesta de Satisfacción 
# Un restaurante realiza una encuesta a 8 clientes para evaluar la calidad del servicio, pidiéndoles una puntuación del 1 al 5.
# ●Ingresar la puntuación de cada uno de los 8 clientes.
# ●Validar que la puntuación esté entre 1 y 5.
# ●Calcular el puntaje promedio de satisfacción.
# ●Contar cuántos clientes dieron la máxima puntuación (5).
# ●Detectar si algún cliente dio una puntuación de 1 y, si es así, mostrar el mensaje: "Cliente muy insatisfecho".

count_max = 0
prom= 0
total = 0
count_min = 0

for i in range (1, 9):
  value = int(input("ingrese su califiocaión"))
  while value < 1 or value > 5 :
    print("ingrese una califiocaión válida entre 1 y 5 puntos")
    value = int(input("ingrese su califiocaión"))
  
  total += value
  
  if value == 1:
    count_min +=1

  if value == 5:
    count_max +=1
prom = total / 8

print(f"El promedio de claificación es de  {prom}, con {count_max} puntuaciones máximas y {count_min} clientes muy insatisfechos")
  



# Ejercicio Nº4: Control de Producción en Fábrica 
# Una fábrica quiere controlar la producción de un artículo específico durante 6 días.
# ●Ingresar la cantidad de unidades producidas cada día.
# ●Validar que la cantidad de unidades no sea menor a 0.
# ●Calcular el total de unidades producidas en los 6 días.
# ●Determinar el día de menor producción.
# ●Informar si la producción total superó las 10,000 unidades.
value = 0
total = 0
min_value = None
day_min_value = 0

is_sup = False

for i in range(1, 7):
  value = int(input(f"ingrese cantidad de unindades producidas el día {i}"))
  while value < 0 :
     print("ingrese una cantidad válida de unidades producidas")
     value = int(input(f"ingrese cantidad de unindades producidas el día {i}"))

    
  total += value
  if total > 10000:
    is_sup = True
    print("la producción supera los 10000 unidades")

  if min_value is None or value < min_value:
    min_value = value
    day_min_value = i
  
print(f"total producido = {total}, el {day_min_value} fue el dia de menor produccion con {min_value} unidades producidas")
if is_sup == True :
  print("la producción superó los 10000 unidades")


# Ejercicio Nº5: Registro de Edades de Estudiantes 
# Se necesita registrar la edad de los 10 estudiantes de un curso para obtener algunas estadísticas.
# ●Ingresar la edad de cada estudiante.
# ●Validar que la edad sea una edad válida para un estudiante (por ejemplo, entre 17 y 99 años).
# ●Calcular el promedio de edad del curso.
# ●Encontrar la edad del estudiante mayor y del estudiante menor.
# ●Contar cuántos estudiantes son mayores de 25 años.
age = 0
total = 0
max_age = 0
max_student = 0
min_age = None
min_student = 0
count_sup_25 = 0

for i in range (1,11):
  age = int(input(f"Ingrese la edad del estudiante {i} "))
  while age < 17 or age > 99:
    print(f"Ingrese una edad válida para el estudiante {i} ")
    age = int(input(f"Ingrese la edad del estudiante {i} "))

  total += age

  if age > 25 :
    count_sup_25 +=1

  if age > max_student :
    max_student = i
    max_age = age

  if min_age is None or age < min_age :
    min_student = i
    min_age = age


print(f"promedio de edad del curso {total / 10 }, {max_student} es el amyor con {max_age} años, {min_student} es el menor con {min_age} años")