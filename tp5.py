alumnos={"Juan Pérez":{"dni":47457621, "fecha de nacimiento":"15/06/07", "tutor":"Bruno Pérez", "faltas":3, "amonestaciones":2}, "Olivia Sanchez":{"dni":48569878, "fecha de nacimiento":"15/06/08", "tutor":"Marta Escudero", "faltas":1, "amonestaciones":0}, "Nicolas Martinez":{"dni":46868556, "fecha de nacimiento":"05/12/06", "tutor":"Mauro Martinez", "faltas":3, "amonestaciones":0}, "Martina Salazar":{"dni":47055000, "fecha de nacimiento":"27/08/06", "tutor":"sofia Austerlitz", "faltas":6, "amonestaciones":1}, "Tomás Muñoz":{"dni":47888097, "fecha de nacimiento":"12/09/08", "tutor":"Miguel Muñoz", "faltas":0, "amonestaciones":2}, "Agustina Cornejo":{"dni":46123442, "fecha de nacimiento":"21/02/06", "tutor":"Maria Bambosi", "faltas":4, "amonestaciones":0},"Bautista Macchi":{"dni":48909152, "fecha de nacimiento":"23/01/08", "tutor":"Raul Macchi", "faltas":2, "amonestaciones":1}, "Andrea Guzman":{"dni":47142384, "fecha de nacimiento":"19/06/07", "tutor":"Alejandro Guzman", "faltas":1, "amonestaciones":3}, "Carlos Benavidez":{"dni":46990012, "fecha de nacimiento":"2225/07/06", "tutor":"Ines Larran", "faltas":0, "amonestaciones":0}, "Sofía García":{"dni":48006985, "fecha de nacimiento":"14/05/08", "tutor":"Rafael García", "faltas":4, "amonestaciones":0}, "Eduardo Rolón":{"dni":47001002, "fecha de nacimiento":"28/08/06", "tutor":"Micaela Gimenez", "faltas":9, "amonestaciones":2},  "Julieta Pacheco":{"dni":47234939, "fecha de nacimiento":"27/09/06", "tutor":"Florencia Cattaneo", "faltas":3, "amonestaciones":0}, "Gustavo Riveti":{"dni":47886431, "fecha de nacimiento":"24/04/07", "tutor":"Luciano Riveti", "faltas":5, "amonestaciones":4}, "Renata Varela":{"dni":46556531, "fecha de nacimiento":"04/10/06", "tutor":"Marcos Varela", "faltas":3, "amonestaciones":3}, "Pedro Brunelli":{"dni":46883787, "fecha de nacimiento":"06/07/06", "tutor":"Bianca Lemerte", "faltas":5, "amonestaciones":0}, "Manuela Calderón":{"dni":47987223, "fecha de nacimiento":"26/07/07", "tutor":"Matías Calderón", "faltas":1, "amonestaciones":0}, "Felix Landivar":{"dni":4734956, "fecha de nacimiento":"30/10/07", "tutor":"Mauricio Landivar", "faltas":0, "amonestaciones":0},"Felicitas Aliberti":{"dni":46886931, "fecha de nacimiento":"29/11/06", "tutor":"Diego Aliberti", "faltas":0, "amonestaciones":0}, "Ian Melia":{"dni":4765698, "fecha de nacimiento":"12/12/07", "tutor":"Mariana Cordoba", "faltas":2, "amonestaciones":0}, "Juana Vidal":{"dni":47003202, "fecha de nacimiento":"02/07/07", "tutor":"Carla Moreno", "faltas":2, "amonestaciones":0}, "Ignacio Tonini":{"dni":46889933, "fecha de nacimiento":"25/03/07", "tutor":"Juan Tonini", "faltas":4, "amonestaciones":3}}


while True:
    que_hacer=input("desea datos, expulsar, o agregar: ")
    nombre=input("ingrese el nombre del alumno: ")
   
    if que_hacer=="datos":
        if nombre in alumnos:
            print(alumnos[nombre])
            cambiar=input("desea cambiar algun dato?: ")
            if cambiar=="si":
                dato=input("elija el dato que quiere cambiar")
                nuevo_dato=input("introduzca", dato,"correcto/nuevo")
                alumnos[nombre[dato]]=nuevo_dato 
            
    elif que_hacer=="expulsar":
        expulsar=input("desea expulsar a este alumno?: ")
        if expulsar=="si":
            alumnos.pop(nombre)
            print(nombre, "fue expulsado")
    elif que_hacer=="agregar":
            agregar=input("desea agregar un alumno nuevo?: ")
            if agregar=="si":
                NA_datos={"dni":input("ingrese dni:"), "fecha de nacimiento":input("ingrese fecha de nacimiento: "), "tutor":input("ingrese nombre del tutor: ")}          
                alumnos[nombre]=NA_datos

    
   
   