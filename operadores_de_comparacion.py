es_igual_que = 5 == 6
print(es_igual_que)

es_diferente = 5 != 6
print(es_diferente)

es_mayor_que = 5 > 6
print(es_mayor_que)

es_mayor_igual_que = 5 >= 6
print(es_mayor_igual_que)

es_menor_que = 5 < 6
print(es_menor_que)

es_menor_igual_que = 5 <= 6
print(es_menor_igual_que)

#calculos combinados

a = 5
b = 10
c = 20
comparacion = a + b == c
print(comparacion)

#comparar usuarios

contrasena_almacenada = "Juan Tobar"
contrasena_escrita = "Juan Tobar"

print(contrasena_almacenada == contrasena_escrita) #True

contrasena_almacenada = "Juan Tobar"
contrasena_escrita = 'Juan Tobar'

print(contrasena_almacenada == contrasena_escrita) #True

contrasena_almacenada = "Juan Tobar"
contrasena_escrita = '''Juan Tobar'''

print(contrasena_almacenada == contrasena_escrita) #True