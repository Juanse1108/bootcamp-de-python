#Ejemplo de como funcionan los iteradores
#Crear una lista con algunos números
my_list = [1, 2, 3, 4]
#Obtener el iteador de la lista
#Uni iterador es un objeto que nos permite recorrer una colección (como una lista) uno por uno
my_iter = iter(my_list)
#Usar el iterador para acceder a los elementos de la lista
#la función next() nos da el siguiente elemento en la colección cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))
#Iterar cadenas de texto usando un iterador
text = "Hello World"
#Obtener el iterador de la cadena
#Un iterador es un objeto que nos permite recorrer una colección (como una cadena) uno por uno
text_iter = iter(text)
#Usar el iterador para acceder a los elementos de la cadena usando bucles for
for char in text_iter:
    print(char)
#Crear un iterador que genere número impares desde 1 hasta limite
#range(1, limite + 1,2) genera un iterador que va de 1 con saltos de 2 en 2, hasta que llegue a limite
odd_iter = iter(range(1, 10, 2))
#usar el iterador para recorrer y mostrar cada numero impar
for num in odd_iter:
    print(num)
#Definir una función generadora
def my_generator():
    #La palabra clave yield nos permite retornar un valor y pausar la función en ese punto
    yield 1 #primer valor que se retorna cuando se llama la función
    yield 2 #segundo valor que se retorna cuando se llama la función
    yield 3 #tercer valor que se retorna cuando se llama la función
#Usar un bucle for para iterar sobre la función generadora
for value in my_generator():
    print(value)
#Fibonacci
#La serie de fibonacci es una serie de números donde cada número es la suma de los dos anteriores [0 1 1 2 3 5 8 13 ...]
def fibonacci(limit):
    #inicializar los dos primeros números de la serie
    a, b = 0, 1
    #Continuar generando números mientras 'a' sea menor que 'limit'
    while a < limit:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)