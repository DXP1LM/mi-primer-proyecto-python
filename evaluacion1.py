print("---Evaluación física, Ingrse sus datos---")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
peso = float(input("Peso (kg): "))
horas_ejercicio = float(input("Hras de ejercicio x semana: "))

calorias_quemadas = horas_ejercicio * 350


if edad < 18:
    categoria_edad = "Juvenil"
else:
    categoria_edad = f"Adulto ({edad})"

if horas_ejercicio >= 3:
    estado_actividad = "Activo fisicamente"
else:
    estado_actividad = "Requiere mas actividad física"

print("---------->")
print("     RESUMEN DE EVALUACIÓN FÍSICA")
print("---------->")
print(f"Nombre : {nombre}")
print(f"Peso: {peso:.2f} kg")
print(f"Kcal. quemadas x semana: {calorias_quemadas:.2f} kcal")
print(f"{categoria_edad}")
print(f"{estado_actividad}")
print("---------->")