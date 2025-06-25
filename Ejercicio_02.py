# 02
# FUNCIONES Y ALCANCE

"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

 * - Comprueba si puedes crear funciones dentro de funciones.

 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

 * - Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
 * DIFICULTAD EXTRA (opcional):

 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
        - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.

        - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.

        - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.

        - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.

 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 
 """

# Función sin parámetros ni retorno
def funcion_sin_parametros():
    print("Función sin parámetros ni retorno")

# Función con un parámetro
def funcion_con_parametro(nombre):
    print(f"Hola, {nombre}")

# Función con varios parámetros y con retorno
def funcion_con_retorno(a, b):
    return a + b

# Función dentro de otra función
def funcion_externa():
    print("Estoy en la función externa")

    def funcion_interna():
        print("Estoy en la función interna")

    funcion_interna()

# Variables global y local
x = 10  # Variable global

def mostrar_variables():
    x = 5  # Variable local
    print("Variable local x:", x)

# Función con dificultad extra: FizzBuzz personalizado
def fizzbuzz(palabra1, palabra2):
    contador_numeros = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(palabra1 + palabra2)
        elif i % 3 == 0:
            print(palabra1)
        elif i % 5 == 0:
            print(palabra2)
        else:
            print(i)
            contador_numeros += 1
    return contador_numeros

# --- Ejecución y pruebas ---

# Llamamos a la función sin parámetros ni retorno
funcion_sin_parametros()

# Llamamos a la función con parámetro
funcion_con_parametro("Juan")

# Llamamos a la función con retorno y mostramos el resultado
resultado_suma = funcion_con_retorno(3, 7)
print("Resultado de la suma:", resultado_suma)

# Llamamos a la función externa que contiene otra función
funcion_externa()

# Mostramos variable local y global
mostrar_variables()
print("Variable global x:", x)

# Usamos una función ya creada en Python: len()
texto = "Hola"
print("Longitud de texto:", len(texto))

# Ejecutamos la función fizzbuzz y mostramos cuántas veces se imprimió un número
veces_numeros = fizzbuzz("Fizz", "Buzz")
print("Se imprimieron números", veces_numeros, "veces")




    