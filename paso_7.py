import os

# --- EDITA ESTO ---
NOMBRE = "Pablo Alvarado"
EQUIPO = "equipo-07"
# -------------------

ruta_anterior = f"pipeline/{EQUIPO}/paso_6.txt"
with open(ruta_anterior) as f:
    porcentaje = float(f.readline())

ruta_nueva = f"pipeline/{EQUIPO}/resultado_final.txt"
os.makedirs(os.path.dirname(ruta_nueva), exist_ok=True)
resumen = (
    f"Pipeline completo del {EQUIPO}.\n"
    f"Porcentaje final de 'objeto' segmentado: {porcentaje:.1f}%\n"
    f"Cerrado por: {NOMBRE}\n"
)
with open(ruta_nueva, "w") as f:
    f.write(resumen)

print(resumen)
print(f"Guardado en {ruta_nueva}")
print("Ahora: guarda, haz commit y push de SOLO ese archivo.")
