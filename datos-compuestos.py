#EL primer tipo de dato compuesto que veremos será la lista

lista = ["Juan Tobar","tecnotutoriales Jheyson Galvis", True, 1.15]
print(lista[1])
lista[3] = "Tobar"
print(lista[3])

# La tupla es una lista que no se puede modificar

tupla = ("Juan Tobar","tecnotutoriales Jheyson Galvis", True, 1.15)
print(tupla[1])
#tupla[1] = "Tips TC al paso"
#print(tupla[1])

# Creando un conjunto o set
# Un conjunto no admite elementos duplicados

conjunto = {"Juan Tobar","tecnotutoriales Jheyson Galvis", True, 1.15, 1.15}
print(conjunto)

# Creando un diccionario
dicccionario = {
    "nombre": "Juan Tobar",
    "canal de youtube": "tecnotutoriales Jheyson Galvis",
    "certificado": True,
    "estatura": 1.15
}

print(dicccionario["certificado"])
print(dicccionario["nombre"])
print(dicccionario["estatura"])
print(dicccionario["canal de youtube"])

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print() 
