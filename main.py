print("=== Bienvenido al Gestor de Tareas ===\n")
print("[1] Agregar una tarea")
print("[2] Ver todas las tareas")

opcion = input("\nElige una opción: ")

if opcion == "1":
    with open("tareas.txt", "a") as archivo: 
        tarea = input("[+] Escribe una nueva tarea: ") 
        archivo.write(tarea + "\n") 
        print("[i] Tarea guardada.")
elif opcion == "2":
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("[!] No hay tareas registradas.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("[!] Aún no hay tareas registradas.")
else:
    print("[!] Opción no válida. Intenta nuevamente.")
