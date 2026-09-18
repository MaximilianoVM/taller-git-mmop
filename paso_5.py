import os

# --- EDITA ESTO ---
NOMBRE = "TU NOMBRE AQUI"
EQUIPO = "equipo-01"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_4.txt"
with open(ruta_anterior) as f:
    valores = [float(linea) for linea in f]

UMBRAL = 0.5
binarios = [1 if v > UMBRAL else 0 for v in valores]  # 1 = "objeto", 0 = "fondo"

ruta_nueva = f"pipeline/{EQUIPO}/paso_5.txt"
os.makedirs(os.path.dirname(ruta_nueva), exist_ok=True)
with open(ruta_nueva, "w") as f:
    for v in binarios:
        f.write(f"{v}\n")

print(f"{NOMBRE} binarizó los valores con umbral {UMBRAL} (1=objeto, 0=fondo).")
print(f"Resultado: {binarios}")
print(f"Guardado en {ruta_nueva}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")


