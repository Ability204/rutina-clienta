from flask import Flask, render_template

app = Flask(__name__)

IMG_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises"

RUTINA = {
    "titulo": "Rutina Inicial de Piernas y Cardio",
    "subtitulo": "Nivel principiante · Primera semana",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "5 minutos",
        "detalle": "Marcha suave en el lugar y movilidad de tobillos, rodillas y cadera antes de empezar.",
    },
    "bloques": [
        {
            "nombre": "Piernas (suave)",
            "icono": "leg",
            "ejercicios": [
                {
                    "nombre": "Sentadilla sin peso",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Párate con los pies al ancho de los hombros. Baja flexionando las rodillas y la cadera como si te fueras a sentar, con el pecho arriba. Baja solo hasta donde te sientas cómoda y vuelve a subir.",
                    "carpeta": "Bodyweight_Squat",
                },
                {
                    "nombre": "Zancada caminando",
                    "series": "2 series x 10 pasos por pierna",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Párate con los pies al ancho de la cadera. Da un paso largo hacia adelante y baja hasta que la rodilla trasera casi toque el piso. Vuelve a subir y sigue caminando alternando de pierna.",
                    "carpeta": "Bodyweight_Walking_Lunge",
                },
                {
                    "nombre": "Puente de glúteo",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Acuéstate boca arriba con las rodillas flexionadas y los pies apoyados. Empuja con los talones y levanta la cadera apretando los glúteos arriba. Baja despacio y repite.",
                    "carpeta": "Bent-Knee_Hip_Raise",
                },
                {
                    "nombre": "Elevación de talones",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Párate con los pies al ancho de la cadera, apoyada en una pared o silla si hace falta. Levanta los talones despacio poniéndote de puntas, y baja controlando el movimiento.",
                    "carpeta": "Standing_Calf_Raises",
                },
            ],
        },
        {
            "nombre": "Iniciación con mancuernas",
            "icono": "dumbbell",
            "ejercicios": [
                {
                    "nombre": "Sentadilla con mancuernas",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Es la misma sentadilla de antes, pero ahora sostén una mancuerna liviana en cada mano, a los costados del cuerpo. Usa muy poco peso: el objetivo de hoy es familiarizarte con el movimiento usando mancuernas, no cargar peso.",
                    "carpeta": "Dumbbell_Squat",
                },
                {
                    "nombre": "Zancada con mancuernas",
                    "series": "2 series x 8 repeticiones por pierna",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie con el torso derecho, sostén una mancuerna liviana en cada mano a los costados. Da un paso adelante y baja como en la zancada sin peso, manteniendo el equilibrio. Vuelve al centro y repite alternando de pierna.",
                    "carpeta": "Dumbbell_Lunges",
                },
            ],
        },
        {
            "nombre": "Cardio (bajo impacto)",
            "icono": "cardio",
            "ejercicios": [
                {
                    "nombre": "Jumping jack suave",
                    "series": "3 series x 20 segundos",
                    "descanso": "40 seg. de descanso entre series",
                    "instrucciones": "De pie con los pies juntos y los brazos a los costados, abre las piernas y los brazos a la vez con un salto suave (o sin salto, solo abriendo y cerrando los pies) y vuelve a la posición inicial.",
                    "carpeta": "Star_Jump",
                },
                {
                    "nombre": "Subida al escalón con rodilla arriba",
                    "series": "2 series x 10 repeticiones por lado",
                    "descanso": "40 seg. de descanso entre series",
                    "instrucciones": "Usando un escalón bajo o cajón firme, sube con una pierna y lleva la otra rodilla hacia el pecho arriba del escalón. Baja controlando el movimiento y repite alternando de pierna.",
                    "carpeta": "Step-up_with_Knee_Raise",
                },
            ],
        },
    ],
    "enfriamiento": {
        "nombre": "Enfriamiento y estiramiento",
        "duracion": "5 minutos",
        "detalle": "Caminar suave y estirar cuádriceps, isquiotibiales y pantorrillas al terminar la rutina.",
    },
    "notas": [
        "Toma agua antes, durante y después de la rutina.",
        "Si sientes dolor (no solo cansancio muscular), detente y avísale a tu entrenador/a.",
        "Respira de forma constante durante cada ejercicio, sin cortar la respiración.",
        "En los ejercicios con mancuernas usa el peso más liviano que tengas (1-2 kg): hoy es para aprender la técnica, no para exigir el músculo.",
    ],
}


def con_imagenes(rutina):
    for bloque in rutina["bloques"]:
        for ej in bloque["ejercicios"]:
            carpeta = ej["carpeta"]
            ej["img1"] = f"{IMG_BASE}/{carpeta}/0.jpg"
            ej["img2"] = f"{IMG_BASE}/{carpeta}/1.jpg"
    return rutina


@app.route("/")
def index():
    return render_template("index.html", rutina=con_imagenes(RUTINA), cliente="Nombre de la clienta")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
