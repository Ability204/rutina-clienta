from flask import Flask, render_template

app = Flask(__name__)

IMG_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises"

CLIENTE = "Sofía Gómez"
FRASE = "Cada repetición de hoy es un paso hacia la versión más fuerte de ti misma."

# Fotos de mujer con licencia CC BY 2.0 (Flickr, via Openverse), usadas donde encontramos
# una demostracion clara y profesional del ejercicio. El resto sigue con la base de
# demostraciones animadas (free-exercise-db), que solo tiene modelo masculino.
FOTO_SENTADILLA = {
    "url": "https://live.staticflickr.com/65535/54567905274_2831058e4c_b.jpg",
    "credito": '"A woman engages in a challenging workout, performing weighted squats..." por nenad53, CC BY 2.0',
}
FOTO_ZANCADA = {
    "url": "https://live.staticflickr.com/65535/54555431111_5064172ff0_b.jpg",
    "credito": '"Young woman performs weighted lunges in modern gym..." por nenadstojkovicart, CC BY 2.0',
}
FOTO_REMO = {
    "url": "https://live.staticflickr.com/65535/54555670278_61710d2879_b.jpg",
    "credito": '"A dedicated woman with long blonde hair performs a bent-over dumbbell row..." por nenadstojkovicart, CC BY 2.0',
}
FOTO_CURL = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/1/12/Woman_in_a_gym_sitting_on_the_floor_and_doing_dumbbell_curls.jpg",
    "credito": '"Woman in a gym sitting on the floor and doing dumbbell curls" por Shixart1985, CC BY 2.0',
}

DIA_1 = {
    "slug": "index",
    "dia": "Día 1",
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
            "ejercicios": [
                {
                    "nombre": "Sentadilla sin peso",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Párate con los pies al ancho de los hombros. Baja flexionando las rodillas y la cadera como si te fueras a sentar, con el pecho arriba. Baja solo hasta donde te sientas cómoda y vuelve a subir.",
                    "carpeta": "Bodyweight_Squat",
                    "foto": FOTO_SENTADILLA,
                },
                {
                    "nombre": "Zancada caminando",
                    "series": "2 series x 10 pasos por pierna",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Párate con los pies al ancho de la cadera. Da un paso largo hacia adelante y baja hasta que la rodilla trasera casi toque el piso. Vuelve a subir y sigue caminando alternando de pierna.",
                    "carpeta": "Bodyweight_Walking_Lunge",
                    "foto": FOTO_ZANCADA,
                },
                {
                    "nombre": "Puente de glúteo",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Acuéstate boca arriba con las rodillas flexionadas y los pies apoyados. Empuja con los talones y levanta la cadera apretando los glúteos arriba. Baja despacio y repite.",
                    "carpeta": "Butt_Lift_Bridge",
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
            "ejercicios": [
                {
                    "nombre": "Sentadilla con mancuernas",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Es la misma sentadilla de antes, pero ahora sostén una mancuerna liviana en cada mano, a los costados del cuerpo. Usa muy poco peso: el objetivo de hoy es familiarizarte con el movimiento usando mancuernas, no cargar peso.",
                    "carpeta": "Dumbbell_Squat",
                    "foto": FOTO_SENTADILLA,
                },
                {
                    "nombre": "Zancada con mancuernas",
                    "series": "2 series x 8 repeticiones por pierna",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie con el torso derecho, sostén una mancuerna liviana en cada mano a los costados. Da un paso adelante y baja como en la zancada sin peso, manteniendo el equilibrio. Vuelve al centro y repite alternando de pierna.",
                    "carpeta": "Dumbbell_Lunges",
                    "foto": FOTO_ZANCADA,
                },
            ],
        },
        {
            "nombre": "Cardio (bajo impacto)",
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

DIA_2 = {
    "slug": "dia2",
    "dia": "Día 2",
    "titulo": "Rutina de Espalda y Brazos",
    "subtitulo": "Nivel principiante · Segunda sesión",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "5 minutos",
        "detalle": "Círculos de brazos y hombros, y unos minutos de marcha suave en el lugar antes de empezar.",
    },
    "bloques": [
        {
            "nombre": "Espalda y brazos (con mancuernas livianas)",
            "ejercicios": [
                {
                    "nombre": "Remo con mancuerna a una mano",
                    "series": "2 series x 10 repeticiones por lado",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Apoya la rodilla y la mano de un lado sobre un banco o silla firme, con la espalda recta. Con la otra mano, sostén la mancuerna y tira hacia arriba llevando el codo hacia atrás, cerca del cuerpo. Baja controlando el movimiento y repite.",
                    "carpeta": "One-Arm_Dumbbell_Row",
                    "foto": FOTO_REMO,
                },
                {
                    "nombre": "Curl de bíceps con mancuernas",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, con una mancuerna en cada mano y los codos pegados al cuerpo, sube las mancuernas doblando los codos hasta la altura del hombro. Baja despacio sin mover los codos y repite.",
                    "carpeta": "Dumbbell_Bicep_Curl",
                    "foto": FOTO_CURL,
                },
                {
                    "nombre": "Extensión de tríceps de pie",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, sostén una mancuerna con ambas manos por encima de la cabeza con los brazos extendidos. Baja la mancuerna doblando los codos detrás de la cabeza, manteniendo los codos quietos, y vuelve a extender los brazos.",
                    "carpeta": "Standing_Dumbbell_Triceps_Extension",
                },
                {
                    "nombre": "Elevación lateral de hombros",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, con una mancuerna en cada mano a los costados del cuerpo, levanta los brazos hacia los lados hasta la altura del hombro, con un ligero doblez en el codo. Baja despacio y repite.",
                    "carpeta": "Side_Lateral_Raise",
                },
            ],
        },
    ],
    "enfriamiento": {
        "nombre": "Enfriamiento y estiramiento",
        "duracion": "5 minutos",
        "detalle": "Estira brazos, hombros y espalda alta al terminar, sosteniendo cada estiramiento unos 20 segundos.",
    },
    "notas": [
        "Toma agua antes, durante y después de la rutina.",
        "Si sientes dolor articular (no solo cansancio muscular), detente y avísale a tu entrenador/a.",
        "Usa el mismo peso liviano de la primera sesión o uno apenas mayor: hoy seguimos priorizando la técnica.",
        "Las piernas descansan hoy: es normal y necesario para que el músculo se recupere.",
    ],
}

DIAS = [DIA_1, DIA_2]


def con_imagenes(rutina):
    creditos = []
    for bloque in rutina["bloques"]:
        for ej in bloque["ejercicios"]:
            foto = ej.get("foto")
            if foto:
                ej["img1"] = foto["url"]
                ej["img2"] = foto["url"]
                if foto["credito"] not in creditos:
                    creditos.append(foto["credito"])
            else:
                carpeta = ej["carpeta"]
                ej["img1"] = f"{IMG_BASE}/{carpeta}/0.jpg"
                ej["img2"] = f"{IMG_BASE}/{carpeta}/1.jpg"
    rutina["creditos"] = creditos
    return rutina


def render_dia(dia):
    nav = [{"dia": d["dia"], "titulo": d["titulo"], "slug": d["slug"], "activo": d["slug"] == dia["slug"]} for d in DIAS]
    return render_template(
        "index.html",
        rutina=con_imagenes(dia),
        cliente=CLIENTE,
        frase=FRASE,
        nav=nav,
    )


@app.route("/")
@app.route("/index.html")
def index():
    return render_dia(DIA_1)


@app.route("/dia2")
@app.route("/dia2.html")
def dia2():
    return render_dia(DIA_2)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
