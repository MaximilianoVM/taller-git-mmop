import os

# --- EDITA ESTO ---
NOMBRE = "TU NOMBRE AQUI"
EQUIPO = "equipo-01"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_5.txt"
with open(ruta_anterior) as f:
    binarios = [int(float(linea)) for linea in f]

total = len(binarios)
objeto = sum(binarios)
porcentaje = 100 * objeto / total

ruta_nueva = f"pipeline/{EQUIPO}/paso_6.txt"
os.makedirs(os.path.dirname(ruta_nueva), exist_ok=True)
with open(ruta_nueva, "w") as f:
    f.write(f"{porcentaje}\n")

print(f"{NOMBRE} contó las regiones: {objeto} de {total} píxeles son 'objeto'.")
print(f"Eso es un {porcentaje:.1f}% del total.")
print(f"Guardado en {ruta_nueva}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")
