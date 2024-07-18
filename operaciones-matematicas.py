#Operaciones matemáticas
a = 10
b = 3
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)   

print("suma: ", a + b)
print("resta: ", a - b)
print("multiplicacion: ", a * b)
print("division: ", a / b)
#En python el operador (%) devuelve el residuo de la división
print("modulo: ", a % b)
#El siguiente signo es el doble división y el resultado seria la parte entera
print("division entera: ", a // b)
#Potencias
print("potencia: ", a ** b)
a += 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a -= 2
print(a)

operacion_1 = 2 + 3 * 4
print(operacion_1)
operacion_2 = 2 + (3 * 4)
print(operacion_2)
operacion_3 = (2 + 3) * 4
print(operacion_3)
operacion_4 =(2 + 3) * (4 ** 2) / 8 - 1
print(operacion_4)