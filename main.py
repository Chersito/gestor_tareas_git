print("Hola Mundo")

with open("tareas.txt", "a") as archivo: 
    tarea = input("Escribe una nueva tarea: ") 
    archivo.write(tarea + "\n") 
    print("Tarea guardada.")

print("\nTus tareas:") 

with open("tareas.txt", "r") as archivo: 
    print(archivo.read())
