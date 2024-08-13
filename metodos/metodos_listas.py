lista = list ([1992,14,3,True]) #eliminé a hola y a Jheyson
#Nos devuelve la longitud de la lista(cantidad de caracteres)
cadena = "hola"
resultado = len(lista)
#Agregando un elemento a la lista
lista.append(4) #Agregué el 4
#Agregando un elemento en una posicion especifica
lista.insert(2, False) #Agregando el False en la posicion 2
#Agregando varios eleemntos a la lista
lista.extend([2011]) #Quité el tecnotutorialesJheysonGalvis
#Elimando un elemento de la lista
print(len(lista))
lista.pop(0)
print(len(lista))
lista.pop(-1)
#Eliminando un elemento de la lista por su valor
#lista.remove("tecnotuorialesJheysonGalvis")
#lista.remove("piscis")
#ordena los elementos de la lista mientras la lista tenga números y booleanos
#lista.sort()
print(lista)
#lista.sort(reverse=True)
#Verficiando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(14)
print(elemento_encontrado)