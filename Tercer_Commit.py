print("Calculo de nota final")

# Nombre del estudiante

nombre_estudiante = input("nombre de estudiante: ")

# P = periodo

p1 = int(input("periodo 1: "))
p2 = int(input("periodo 2: "))
p3 = int(input("periodo 3: "))
p4 = int(input("periodo 4: "))

nota_final = (p1 + p2 + p3 + p4) / 4

print(f"El estudiante {nombre_estudiante} tiene un promedio de {round(nota_final)}")
