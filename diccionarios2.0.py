numbers = {1:"uno", 2:"dos", 3:"tres"} #en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre" : "Juan",
               "apellidos" : "Tobar",
               "estatura" : 1.15,
               "esta feliz" : True}
print(information)
#del information ["apellidos"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Jheyson": {"Apellido": "Tobar",
                        "Altura": 1.15,
                        "Edad": 25,
                        "Teléfono": 333-333-3333,
                        "Signo Zodiacal": "Leo",
                        "Serie Favorita": "GOT",
                        "Canción favorita": "Me vale - Mana",
                        "Comida favorita": "hamburguesa",
                        "Lugar soñado vacaciones": "Dubai",
                        "Habilidad secreta": "no se",
                        "Pasatiempo":"videojuegos",
                        "Heroe o persona que admiras": "---",
                        "Libro que más me ha impactado": "---",
                        "Cenar con alguien": "---",
                        "Superpoder": "---",
                        "Que logro personal te enorgullese": "Aprender Python",},
            "Aurelio": {"Apellido": "Cheveroni",
                        "Altura": 1.20,
                        "Edad": 8}}
print(contacts)