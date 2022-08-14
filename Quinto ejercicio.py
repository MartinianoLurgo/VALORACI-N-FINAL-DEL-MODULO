#5)Crear una tupla en Python con el nombre de “Historial” la cual contenga los siguientes valores:

historial={2350, 5960, 23000, 1000, 8900}

#Que representa montos de atención en pesos por 
#diferentes servicios/consultas de la mascota “Puppy”. 
#Calcular el monto total gastado a lo largo del tiempo
#por atención de “Puppy”. Si el gasto efectuado es menor 
#a 30000, mostrar en pantalla dicho resultado, caso
#contrario mostrar el mensaje “Gastos por encima de lo presupuestado”.
for i in historial:
        if i>3000:
            print("Gastos por encima de lo presupuestado")
            print(i)
        else:
            print("gastos por debajo de lo presupuestado")
            print(i)
