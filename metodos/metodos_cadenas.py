cadena1 = "Hola,Soy,Juans" 
cadena2 = "Gracias por aprender Python conmigo"
#Método 1). dir muestra todos los metodos de una cadena
#resultado = "los pollitos dicen".upper() #Convierte todas las letras en mayúsculas
#print(resultado)
#resultado = cadena1.lower() #Convierte todas las letras en minúsculas
#print(resultado)
#primera_letra_mayus = cadena1.capitalize() #Convierte la primera letra en mayúscula
#print(primera_letra_mayus)
#busqueda_find = cadena1.find("a") #Busca la palabra dentro de la cadena
#print(busqueda_find)
#busqueda_index = cadena1.index("a") #Busca la palabra dentro de la cadena
#print(busqueda_index)
#es_numerico = cadena1.isnumeric() #Busca numeros dentro de la cadena o entero
#print(es_numerico)
#es_alfanumerico = cadena1.isalpha()
#print(es_alfanumerico)
#contar_coincidencias = cadena1.count("a")
#print(contar_coincidencias)
#contar_caracteres = len(cadena1) #len no es un método, es una función por eso se pone así
#print(contar_caracteres)
#empieza_con = cadena1.startswith("H")
#print(empieza_con)
#termina_con = cadena1.endswith("n")
#print(termina_con)
#cadena_nueva = cadena1.replace("Hola", "Me llamo") #aquí recibe dos parámetros, en lugar de Hola, dirá: Me llamo
#print(cadena_nueva)
cadena_sepadara = cadena1.split(",") #Separa la cadena por comas
print(cadena_sepadara)
print(type(cadena_sepadara))
print(cadena_sepadara[0])

