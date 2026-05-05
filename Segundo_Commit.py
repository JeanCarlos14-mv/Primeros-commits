print("Validacion de estudiate")

estudiantes = ["Jean Carlos", "Jose Luis", "Alberto", "Pedro", "Maria", "Candy"]

presente = ["Jean Carlos", "Jose Luis", "Alberto"]

for estudiante in estudiantes:
    if estudiante in presente:
        print(f"El estudiante {estudiante} esta presente")

    else:
        print(f"El estudiante {estudiante} esta ausente")
