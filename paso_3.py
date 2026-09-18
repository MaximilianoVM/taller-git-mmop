import os

# --- EDITA ESTO ---
NOMBRE = "Jacqueline Barajas Gamas"
EQUIPO = "equipo-01"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_2.txt"
with open(ruta_anterior) as f:
    valores = [float(linea) for linea in f]

FACTOR_CONTRASTE = 1.3
ajustados = [min(v * FACTOR_CONTRASTE, 1.0) for v in valores]  # recorta a 1.0 máx

ruta_nueva = f"pipeline/{EQUIPO}/paso_3.txt"
os.makedirs(os.path.dirname(ruta_nueva), exist_ok=True)
with open(ruta_nueva, "w") as f:
    for v in ajustados:
        f.write(f"{v}\n")

print(f"{NOMBRE} ajustó el contraste (factor {FACTOR_CONTRASTE}).")
print(f"Guardado en {ruta_nueva}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")