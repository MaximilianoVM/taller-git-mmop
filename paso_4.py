import os

# --- EDITA ESTO ---
NOMBRE = "Jacqueline Barajas Gamas"
EQUIPO = "equipo-01"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_3.txt"
with open(ruta_anterior) as f:
    valores = [float(linea) for linea in f]

suavizados = []
for i in range(len(valores)):
    vecinos = valores[max(0, i - 1): i + 2]  # el valor y sus vecinos inmediatos
    suavizados.append(sum(vecinos) / len(vecinos))

ruta_nueva = f"pipeline/{EQUIPO}/paso_4.txt"
os.makedirs(os.path.dirname(ruta_nueva), exist_ok=True)
with open(ruta_nueva, "w") as f:
    for v in suavizados:
        f.write(f"{v}\n")

print(f"{NOMBRE} aplicó un suavizado simple (promedio con vecinos).")
print(f"Guardado en {ruta_nueva}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")