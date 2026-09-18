import os
import random

# --- EDITA ESTO ---
NOMBRE = "TU NOMBRE AQUI"
EQUIPO = "equipo-01"
# -------------------

# Generamos una "imagen" muy simplificada: 20 intensidades de pixel (0-255)
pixeles = [random.randint(0, 255) for _ in range(20)]

ruta = f"pipeline/{EQUIPO}/paso_1.txt"
os.makedirs(os.path.dirname(ruta), exist_ok=True)
with open(ruta, "w") as f:
    for p in pixeles:
        f.write(f"{p}\n")

print(f"{NOMBRE} generó {len(pixeles)} píxeles dummy: {pixeles}")
print(f"Guardado en {ruta}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")