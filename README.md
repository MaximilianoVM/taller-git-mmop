# Taller Git/GitHub — Repo de práctica

Bienvenido/a. Este repo es solo para practicar el flujo básico de Git/GitHub
usando la interfaz gráfica de VS Code (sin terminal). Sigue los pasos en orden.

## 0. Antes de empezar
- Ten una cuenta de GitHub lista.
- Ten VS Code instalado, con la extensión "GitHub Pull Requests and Issues"
  (opcional, no la vamos a usar hoy, pero no estorba).
- Asegúrate de que te hayan agregado como colaborador de este repo
  (revisa tu correo o notificaciones de GitHub).

## 1. Clonar el repo
1. Abre VS Code.
2. `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac) → escribe "Git: Clone".
3. Pega la URL de este repositorio (te la comparte el instructor).
4. Elige una carpeta local y ábrela cuando VS Code te lo pida.

## 2. El ejercicio: mini pipeline de "segmentación" (7 pasos)
Somos 7, así que cada quien corre un script distinto que hace una pequeña
transformación sobre datos dummy — y necesita el archivo que subió la
persona anterior. Es básicamente una versión juguete de los pasos que
usamos en el proyecto real (generar datos → normalizar → contraste →
suavizado → umbral/segmentación → contar regiones).

| Posición | Script | Qué hace |
|---|---|---|
| 1 | `paso_1.py` | Genera 20 "píxeles" dummy (0-255) |
| 2 | `paso_2.py` | Normaliza a escala 0-1 |
| 3 | `paso_3.py` | Ajusta contraste |
| 4 | `paso_4.py` | Suaviza (promedio con vecinos) |
| 5 | `paso_5.py` | Umbraliza / binariza (mini segmentación) |
| 6 | `paso_6.py` | Cuenta % de píxeles "objeto" |
| 7 | `paso_7.py` | Imprime el resumen final |

1. El instructor te da tu número de posición (1 a 7).
2. Copia el script que te corresponde dentro de la carpeta `scripts/` de
   tu clon local.
3. Edita las variables de arriba del script (`NOMBRE`, `EQUIPO`).
4. **Si no eres la posición 1**: antes de correr el script, haz pull para
   tener el archivo de quien te toca antes.
5. Corre el script (botón ▷ de VS Code o click derecho → "Run Python File").
6. Lee el mensaje que imprime — te dice qué archivo se creó.

## 3. Subir tu cambio (commit + push)
1. Abre el panel **Source Control** en VS Code (ícono de la ramita en la
   barra lateral izquierda, o `Ctrl+Shift+G`).
2. Vas a ver **solo tu archivo nuevo** listado en "Changes" (ej.
   `pipeline/equipo-01/paso_2.json`). Da click en el **+** para agregarlo
   al stage.
3. Escribe un mensaje corto, por ejemplo: `Agrego paso 2 de equipo-01`
4. Da click en el ✓ (Commit).
5. Da click en **Sync Changes** para subirlo a GitHub.
6. Avísale a la siguiente persona de tu equipo que ya puede hacer pull.

## 4. Ver el resultado final
Cuando la posición 7 corre `paso_7.py`, va a imprimir el resumen del
pipeline completo (`resultado_final.txt`) con el porcentaje final de
"objeto" segmentado.

## 5. Si algo sale mal
- **"Please commit your changes before merging"**: haz commit de tus
  cambios primero (paso 3), luego intenta sync de nuevo.
- **Conflicto (líneas con `<<<<<<<`, `=======`, `>>>>>>>`)**: levanta la
  mano, lo resolvemos juntos en pantalla. Es normal, le pasa a todos.
- **No aparece nada al hacer clone**: revisa que la URL sea correcta y que
  ya tengas acceso como colaborador.

## Reglas de convivencia para proyectos reales (no solo hoy)
- Haz **pull** antes de empezar a trabajar cada vez.
- Commits pequeños y frecuentes, no un commit gigante al final.
- El mensaje de commit dice **qué** cambiaste, no "cambios" o "asdf".
- Revisa tu `.gitignore` antes de tu primer commit para no subir datasets
  pesados, carpetas `__pycache__`, o archivos de configuración local.
