# 01_OPERADORES Y ESTRUCTURAS DE CONTROL
"""

 * EJERCICIO:

 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: 
 
 Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 
 * DIFICULTAD EXTRA (opcional):

 * Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 
 """

# Aritmeticos

a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
potencia = a ** b

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")

# Lógicos
x = True
y = False
and_result = x and y
or_result = x or y
not_result = not x      

print(f"AND: {and_result}")
print(f"OR: {or_result}")
print(f"NOT: {not_result}")

# Comparación

num1 = 10
num2 = 20

igual = num1 == num2
diferente = num1 != num2
mayor = num1 > num2
menor = num1 < num2
mayor_igual = num1 >= num2
menor_igual = num1 <= num2

print(f"Igual: {igual}")
print(f"Diferente: {diferente}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Mayor o igual: {mayor_igual}")
print(f"Menor o igual: {menor_igual}")

# Asignación

c = 30
c += 5  # c = c + 5
c -= 3  # c = c - 3
c *= 2  # c = c * 2
c /= 4  # c = c / 4
c %= 3  # c = c % 3     
print(f"Asignación: {c}")

# Identidad

is_a = (c is not None)
is_not_a = (c is None)  
print(f"Es no nulo: {is_a}")
print(f"Es nulo: {is_not_a}")

# Pertenencia
lista = [1, 2, 3, 4, 5]
pertenece = 3 in lista
no_pertenece = 6 not in lista
print(f"Pertenece: {pertenece}")
print(f"No pertenece: {no_pertenece}")

# Bitwise
bit_a = 0b1010  # 10 en binario
bit_b = 0b1100  # 12 en binario
bit_and = bit_a & bit_b
bit_or = bit_a | bit_b
bit_xor = bit_a ^ bit_b
bit_not = ~bit_a    
bit_left_shift = bit_a << 2  # Desplazamiento a la izquierda
bit_right_shift = bit_a >> 2  # Desplazamiento a la derecha
print(f"AND bitwise: {bin(bit_and)}")
print(f"OR bitwise: {bin(bit_or)}")
print(f"XOR bitwise: {bin(bit_xor)}")
print(f"NOT bitwise: {bin(bit_not)}")
print(f"Left Shift: {bin(bit_left_shift)}")
print(f"Right Shift: {bin(bit_right_shift)}")


for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)