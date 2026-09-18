import os

# --- Esto---
NOMBRE = "Mario estubo qui"
EQUIPO = "equipo-01"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_1.txt"
with open ( ruta_anterior) as f:
    pixeles = [float ( linea) for linea in f]

normalizados = [p / 255 for p in pixeles]

ruta_nueva = f"pipeline/{EQUIPO}/paso_2.txt"
os.makedirs ( os.path.dirname ( ruta_nueva ) , exist_ok=True)
with open ( ruta_nueva, "w") as f:
    for v in normalizados:
        f.write ( f"{v}\n")

print ( f"{NOMBRE} normalizó los valores a escala 0-1.")
print ( f"Ejemplo: {pixeles[0]} -> {normalizados[0]:.3f}")
print ( f"Guardado en {ruta_nueva}")
print ( "Ahora: guarda, haz commit y push de SOLO ese archivo.")
