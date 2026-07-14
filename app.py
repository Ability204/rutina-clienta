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
                    "instrucciones": "Parate con los pies al ancho de los hombros. Bajá flexionando rodillas y cadera como si te fueras a sentar, con el pecho arriba. Bajá solo hasta donde te sientas cómoda y volvé a subir.",
                    "carpeta": "Bodyweight_Squat",
                },
                {
                    "nombre": "Zancada caminando",
                    "series": "2 series x 10 pasos por pierna",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Parate con los pies al ancho de cadera. Dá un paso largo hacia adelante y bajá hasta que la rodilla trasera casi toque el piso. Volvé a subir y seguí caminando alternando de pierna.",
                    "carpeta": "Bodyweight_Walking_Lunge",
                },
                {
                    "nombre": "Puente de glúteo",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Acostate boca arriba con las rodillas flexionadas y los pies apoyados. Empujá con los talones y levantá la cadera apretando los glúteos arriba. Bajá despacio y repetí.",
                    "carpeta": "Bent-Knee_Hip_Raise",
                },
                {
                    "nombre": "Elevación de talones",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Parate con los pies al ancho de cadera, apoyada en una pared o silla si hace falta. Levantá los talones despacio poniéndote en puntas de pie, y bajá controlando el movimiento.",
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
                    "instrucciones": "Es la misma sentadilla de antes, pero ahora sostené una mancuerna liviana en cada mano, a los costados del cuerpo. Usá muy poco peso: el objetivo hoy es ir agarrándole la mano al movimiento con mancuernas, no cargar peso.",
                    "carpeta": "Dumbbell_Squat",
                },
                {
                    "nombre": "Zancada con mancuernas",
                    "series": "2 series x 8 repeticiones por pierna",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Parada con el torso derecho, sostené una mancuerna liviana en cada mano a los costados. Dá un paso adelante y bajá como en la zancada sin peso, manteniendo el equilibrio. Volvé al centro y repetí alternando de pierna.",
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
                    "instrucciones": "Parada con los pies juntos y brazos al costado, abrí piernas y brazos a la vez con un salto suave (o sin salto, solo abriendo y cerrando los pies) y volvé a la posición inicial.",
                    "carpeta": "Star_Jump",
                },
                {
                    "nombre": "Subida al escalón con rodilla arriba",
                    "series": "2 series x 10 repeticiones por lado",
                    "descanso": "40 seg. de descanso entre series",
                    "instrucciones": "Usando un escalón bajo o cajón firme, subí con una pierna y llevá la otra rodilla al pecho arriba del escalón. Bajá controlando y repetí alternando de pierna.",
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
        "Tomá agua antes, durante y después de la rutina.",
        "Si sentís dolor (no solo cansancio muscular), parate y avisale a tu entrenador/a.",
        "Respirá de forma constante durante cada ejercicio, sin cortar la respiración.",
        "En los ejercicios con mancuernas usá el peso más liviano que tengas (1-2 kg): hoy es para aprender la técnica, no para exigir el músculo.",
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
