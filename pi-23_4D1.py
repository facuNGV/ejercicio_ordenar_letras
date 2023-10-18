"""" 
Realizar un programa que ordenes las letras de una palabra según el siguiente
criterio:

La nueva palabra se debe componer de

Primero todas las letras minúsculas ordenadas de menor a mayor.
Luego todas las letras mayúsculas ordenadas de menor a mayor.
Todos los dígitos impares ordenados de menor a mayor.
Todos los dígitos pares ordenados de menor a mayor.
La palabra OrDenar1234 debería formar la siguiente nueva palabra según el
criterior anterior: --> aenrrDO1324

IMPORTANTE: Los métodos que le serán útil para determinar si un caracter es una
letra minúscula, mayúscula o si es un dígito/número los debe investigar por su cuenta.
"""
print("Ordenar caracteres")
objetivo = input("Ingrese palabra de entrada:\n")

resultado = ""

lista_objetivo = []
pre_resultado = []
lista_minusculas = []
lista_mayusculas = []
lista_impares = []
lista_pares = []

#convertir palabra en lista
for i in objetivo:
    lista_objetivo.append(i)

#ordena caracteres de menor a mayor
while len(lista_objetivo) != 0:
  min_caracter = "}"
  for i in lista_objetivo:
    if i < min_caracter:
      min_caracter = i
  pre_resultado.append(min_caracter)
  lista_objetivo.remove(min_caracter)

#lista de minusculas
for minusc in pre_resultado:
  minusc_int = False
  for j in range(10):
    j = str(j)
    if minusc == j:
      minusc_int = True
  if minusc_int == False:
    if minusc.islower() == True:
      lista_minusculas.append(minusc)

#lista de mayusculas
for may in pre_resultado:
  may_int = False
  for j in range(10):
    j = str(j)
    if may == j:
      may_int = True
  if may_int == False:
    if may.isupper() == True:
      lista_mayusculas.append(may)









