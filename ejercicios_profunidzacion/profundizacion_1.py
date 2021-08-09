# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''


"""Para sumar 2 numeros
  int -- numero 1 a calcular
  int -- numero 2 a calcular
  return devuelve el resultado de la suma 
"""
def Suma(num_1, num_2):
  suma = num_1 + num_2
  return suma

"""Para Resta 2 numeros
  int -- numero 1 a calcular
  int -- numero 2 a calcular
  return devuelve el resultado de la suma 
"""
def Resta(num_1, num_2):
  resta = num_1 - num_2
  return resta

"""Para Multiplicar 2 numeros
  int -- numero 1 a calcular
  int -- numero 2 a calcular
  return devuelve el resultado de la Multiplicacion 
"""
def Multi(num_1, num_2):
  multi = num_1 * num_2
  return multi

"""Para Dividir 2 numeros
  int -- numero 1 a calcular
  int -- numero 2 a calcular
  return devuelve el resultado de la Dividision 
"""
def Division(num_1, num_2):
  division = num_1 / num_2
  return division

"""Para Saber la potencia/exponente de 2 numeros
  int -- numero 1 a calcular
  int -- numero 2 a calcular
  return devuelve el exponente  
"""
def Exponente_potencia(num_1, num_2):
  exponente_potencia = num_1 ** num_2
  return exponente_potencia


print('Seleccione una operacion : ')
print('SUMA (1) - RESTA (2) - MULTIPLICACION (3) - DIVISION (4) - EXPONENTE/POTENCIA (5) ')
while True:
  #Pedimos que ingrese el valor
  opcion_elegida = input('Ingrese el nro de la operacion elegida : ')

  #Corroborar si el nro elegido se encuentra entre las parametrizadas
  if opcion_elegida in ('1','2','3','4','5'):
    print('Ingrese primer número entero a operar:')
    numero_1 = int(input())
    print('Ingrese segundo número entero a operar:')
    numero_2 = int(input())

    if opcion_elegida== '1':
      print('se ha realizado la operación, La suma entre ', numero_1 ,' y ', numero_2, ' es ', Suma(numero_1, numero_2))
    elif opcion_elegida== '2':
      print('se ha realizado la operación, La resta entre ', numero_1 ,' y ', numero_2, ' es ', Resta(numero_1, numero_2))
    elif opcion_elegida== '3':
      print('se ha realizado la operación, La multiplicacion entre ', numero_1 ,' y ', numero_2, ' es ', Multi(numero_1, numero_2))
    elif opcion_elegida== '4':
      print('se ha realizado la operación, La division entre ', numero_1 ,' y ', numero_2, ' es ', Division(numero_1, numero_2))
    elif opcion_elegida== '5':
      print('se ha realizado la operación, el exponente entre ', numero_1 ,' y ', numero_2, ' es ', Exponente_potencia(numero_1, numero_2))
    break


  else:
    print('Opcion ingresada no existe')


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio