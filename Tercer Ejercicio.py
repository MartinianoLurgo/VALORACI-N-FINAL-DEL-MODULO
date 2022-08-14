#3)  Crear un lista en Python denominado “Perro” que contenga los siguientes valores:
perro = [ 13,  "Puppy",  12/12/2012 , "Macho", 123]

#Que se corresponde con los datos de un perro de nuestra base de datos (Id_Perro, nombre,
#  fecha de nacimiento, sexo y dni# del dueño). Modificar la fecha de nacimiento por 13/12/2012
#  y reemplazar “dni del dueño” por 28957346 
id_del_perro = perro[4]
nombre = perro[1]
fecha_de_nacimiento = perro[2]
sexo = perro[3]
edad_del_perro= perro[0]

print(
"La id del perro es: ",id_del_perro,"\n"
"Nombre:",nombre,"\n"
"Fecha de nacimiento",fecha_de_nacimiento,"\n"
"Fecha de nacimiento modificada:",13/12/2012,"\n"
"sexo:",sexo,"\n"
"edad del perro:",edad_del_perro,"\n"
"DNI deñ dueño:",28957346 )

