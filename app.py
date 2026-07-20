from flask import Flask, render_template

app = Flask(__name__)

IMG_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises"

CLIENTE = "Sofía Gómez"
FRASE = "Cada repetición de hoy es un paso hacia la versión más fuerte de ti misma."

LUNES = {
    "slug": "index",
    "dia": "Lunes",
    "titulo": "Rutina de Piernas (fuerte)",
    "subtitulo": "Nivel intermedio · Día de piernas completo",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "8 minutos",
        "detalle": "5 minutos de caminadora o bicicleta a ritmo suave, seguido de sentadillas sin peso y zancadas para activar la cadera y las rodillas antes de cargar peso.",
    },
    "bloques": [
        {
            "nombre": "Cuádriceps",
            "ejercicios": [
                {
                    "nombre": "Sentadilla en máquina Smith",
                    "series": "4 series x 10 repeticiones",
                    "descanso": "90 seg. de descanso entre series",
                    "instrucciones": "Coloca la barra sobre la espalda alta (no sobre el cuello), pies al ancho de los hombros. Baja controlando hasta que los muslos queden paralelos al piso, y sube empujando con los talones. Aumenta el peso cada semana si la técnica es correcta.",
                    "carpeta": "Smith_Machine_Squat",
                },
                {
                    "nombre": "Prensa de piernas",
                    "series": "4 series x 12 repeticiones",
                    "descanso": "90 seg. de descanso entre series",
                    "instrucciones": "Siéntate en la prensa con los pies al ancho de los hombros sobre la plataforma. Baja el peso controlando hasta formar un ángulo de 90 grados en la rodilla, y empuja de vuelta sin trabar las rodillas del todo arriba.",
                    "carpeta": "Leg_Press",
                },
                {
                    "nombre": "Extensión de cuádriceps en máquina",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Siéntate en la máquina con las piernas bajo el cojín. Extiende las rodillas hasta estirar las piernas por completo, aprieta el cuádriceps arriba, y baja despacio sin soltar el peso de golpe.",
                    "carpeta": "Leg_Extensions",
                },
                {
                    "nombre": "Zancada con mancuernas",
                    "series": "3 series x 10 repeticiones por pierna",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie con una mancuerna en cada mano (usa más peso que en sesiones anteriores). Da un paso adelante y baja hasta que la rodilla trasera casi toque el piso. Empuja con el talón delantero para volver, y alterna de pierna.",
                    "carpeta": "Dumbbell_Lunges",
                },
            ],
        },
        {
            "nombre": "Femoral y glúteo",
            "ejercicios": [
                {
                    "nombre": "Peso muerto rumano con mancuernas",
                    "series": "4 series x 10 repeticiones",
                    "descanso": "90 seg. de descanso entre series",
                    "instrucciones": "De pie, sostén una mancuerna en cada mano frente a los muslos. Baja las mancuernas deslizándolas por las piernas, empujando la cadera hacia atrás y con la espalda recta, hasta sentir el estiramiento en el femoral. Sube apretando los glúteos.",
                    "carpeta": "Stiff-Legged_Dumbbell_Deadlift",
                },
                {
                    "nombre": "Curl femoral en máquina",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Acuéstate boca abajo en la máquina, con el cojín justo debajo de las pantorrillas. Flexiona las rodillas llevando el cojín hacia los glúteos con control, y baja despacio a la posición inicial.",
                    "carpeta": "Lying_Leg_Curls",
                },
                {
                    "nombre": "Hip thrust con barra",
                    "series": "4 series x 10 repeticiones",
                    "descanso": "90 seg. de descanso entre series",
                    "instrucciones": "Espalda apoyada en un banco, barra sobre la cadera (usa la barra con peso, aumentando gradualmente respecto a sesiones anteriores). Empuja la cadera hacia arriba apretando fuerte los glúteos hasta que el torso quede paralelo al piso, y baja controlando.",
                    "carpeta": "Barbell_Hip_Thrust",
                },
            ],
        },
        {
            "nombre": "Pantorrillas",
            "ejercicios": [
                {
                    "nombre": "Elevación de talones de pie",
                    "series": "4 series x 15 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie en la máquina, con los hombros bajo las almohadillas y las puntas de los pies en la plataforma. Sube los talones lo más alto posible, aguanta un segundo arriba, y baja despacio estirando bien.",
                    "carpeta": "Standing_Calf_Raises",
                },
                {
                    "nombre": "Elevación de talones sentada",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Sentada en la máquina, con los muslos bajo el cojín y las puntas de los pies apoyadas en la plataforma. Levanta los talones lo más alto posible apretando la pantorrilla, y baja despacio.",
                    "carpeta": "Seated_Calf_Raise",
                },
            ],
        },
    ],
    "enfriamiento": {
        "nombre": "Enfriamiento y estiramiento",
        "duracion": "8 minutos",
        "detalle": "Estira cuádriceps, femorales, glúteos y pantorrillas al terminar, sosteniendo cada estiramiento 25-30 segundos.",
    },
    "notas": [
        "Toma agua antes, durante y después de la rutina.",
        "Si sientes dolor articular (no solo cansancio muscular), detente y avísale a tu entrenador/a.",
        "Aumenta el peso de forma progresiva: si terminas todas las series con buena técnica y te sobran fuerzas, la próxima vez sube un poco la carga.",
        "Es una rutina exigente: respetá los tiempos de descanso entre series para poder rendir en el siguiente ejercicio.",
    ],
}

DIAS = [LUNES]

PAGINAS_NAV = [
    {"slug": "index", "dia": "", "titulo": "Lunes"},
    {"slug": "progreso", "dia": "", "titulo": "Mi Progreso (fotos)"},
]


def con_imagenes(rutina):
    for bloque in rutina["bloques"]:
        for ej in bloque["ejercicios"]:
            carpeta = ej["carpeta"]
            ej["img1"] = f"{IMG_BASE}/{carpeta}/0.jpg"
            ej["img2"] = f"{IMG_BASE}/{carpeta}/1.jpg"
    return rutina


def nav_para(slug_activo):
    return [{**p, "activo": p["slug"] == slug_activo} for p in PAGINAS_NAV]


def render_dia(dia):
    return render_template(
        "index.html",
        rutina=con_imagenes(dia),
        cliente=CLIENTE,
        frase=FRASE,
        nav=nav_para(dia["slug"]),
    )


@app.route("/")
@app.route("/index.html")
def index():
    return render_dia(LUNES)


@app.route("/progreso")
@app.route("/progreso.html")
def progreso():
    return render_template(
        "progreso.html",
        cliente=CLIENTE,
        nav=nav_para("progreso"),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
