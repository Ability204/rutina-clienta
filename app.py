from flask import Flask, render_template

app = Flask(__name__)

IMG_BASE = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises"

CLIENTE = "Sofía Gómez"
FRASE = "Cada repetición de hoy es un paso hacia la versión más fuerte de ti misma."

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
                },
                {
                    "nombre": "Zancada con mancuernas",
                    "series": "2 series x 8 repeticiones por pierna",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie con el torso derecho, sostén una mancuerna liviana en cada mano a los costados. Da un paso adelante y baja como en la zancada sin peso, manteniendo el equilibrio. Vuelve al centro y repite alternando de pierna.",
                    "carpeta": "Dumbbell_Lunges",
                },
                {
                    "nombre": "Sentadilla sumo con mancuerna",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Sostén una mancuerna liviana con ambas manos frente a ti. Párate con los pies bien separados, más anchos que los hombros, y las puntas hacia afuera. Baja flexionando las rodillas siguiendo la línea de los pies, con el pecho arriba, y vuelve a subir empujando con los talones.",
                    "carpeta": "Plie_Dumbbell_Squat",
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
    "titulo": "Rutina de Espalda, Bíceps y Hombros",
    "subtitulo": "Nivel principiante · Segunda sesión",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "5 minutos",
        "detalle": "Círculos de brazos y hombros, y unos minutos de marcha suave en el lugar antes de empezar.",
    },
    "bloques": [
        {
            "nombre": "Espalda",
            "ejercicios": [
                {
                    "nombre": "Remo con mancuerna a una mano",
                    "series": "2 series x 10 repeticiones por lado",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Apoya la rodilla y la mano de un lado sobre un banco o silla firme, con la espalda recta. Con la otra mano, sostén la mancuerna y tira hacia arriba llevando el codo hacia atrás, cerca del cuerpo. Baja controlando el movimiento y repite.",
                    "carpeta": "One-Arm_Dumbbell_Row",
                },
                {
                    "nombre": "Remo con mancuernas a dos manos",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie, flexiona un poco las rodillas e inclina el torso hacia adelante manteniendo la espalda recta, con una mancuerna en cada mano colgando frente a ti. Tira de las dos mancuernas hacia arriba llevando los codos hacia atrás, y baja controlando el movimiento.",
                    "carpeta": "Bent_Over_Two-Dumbbell_Row",
                },
            ],
        },
        {
            "nombre": "Bíceps",
            "ejercicios": [
                {
                    "nombre": "Curl de bíceps con mancuernas",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, con una mancuerna en cada mano y los codos pegados al cuerpo, sube las mancuernas doblando los codos hasta la altura del hombro. Baja despacio sin mover los codos y repite.",
                    "carpeta": "Dumbbell_Bicep_Curl",
                },
                {
                    "nombre": "Curl martillo alternado",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, con una mancuerna en cada mano sostenida como si fuera un martillo (palmas mirándose entre sí), sube una mancuerna doblando el codo sin girar la muñeca. Baja y repite alternando de brazo.",
                    "carpeta": "Alternate_Hammer_Curl",
                },
            ],
        },
        {
            "nombre": "Hombros",
            "ejercicios": [
                {
                    "nombre": "Press de hombro con mancuernas de pie",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie con los pies al ancho de los hombros, sostén una mancuerna en cada mano a la altura de la cabeza, con los codos hacia afuera. Empuja las mancuernas hacia arriba hasta extender los brazos por completo, y baja despacio a la posición inicial.",
                    "carpeta": "Standing_Dumbbell_Press",
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

DIA_3 = {
    "slug": "dia3",
    "dia": "Día 3",
    "titulo": "Rutina de Pecho, Tríceps y Core",
    "subtitulo": "Nivel principiante · Tercera sesión",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "5 minutos",
        "detalle": "Círculos de brazos, un par de flexiones de rodillas en el piso y marcha suave en el lugar antes de empezar.",
    },
    "bloques": [
        {
            "nombre": "Pecho",
            "ejercicios": [
                {
                    "nombre": "Press de pecho con mancuernas",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Acostada boca arriba (en el piso o en una banca), con una mancuerna en cada mano a la altura del pecho y los codos hacia afuera. Empuja las mancuernas hacia arriba hasta casi juntarlas, y baja despacio a la posición inicial.",
                    "carpeta": "Dumbbell_Bench_Press",
                },
                {
                    "nombre": "Aperturas con mancuernas",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Acostada boca arriba con una mancuerna en cada mano, brazos extendidos arriba del pecho y un ligero doblez en los codos. Abre los brazos hacia los costados en forma de arco hasta sentir el estiramiento en el pecho, y vuelve a juntarlos arriba.",
                    "carpeta": "Dumbbell_Flyes",
                },
                {
                    "nombre": "Press de pecho en máquina",
                    "series": "3 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Sentada en la máquina de press de pecho, ajusta el asiento para que las agarraderas queden a la altura del pecho. Empuja hacia adelante extendiendo los brazos, y vuelve despacio a la posición inicial sin soltar el peso de golpe.",
                    "carpeta": "Leverage_Chest_Press",
                },
                {
                    "nombre": "Aperturas en máquina (pec deck)",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Siéntate en la máquina con la espalda apoyada y toma las agarraderas, con los brazos casi paralelos al piso. Junta las agarraderas al frente apretando el pecho, y vuelve despacio a la posición inicial estirando bien el pecho.",
                    "carpeta": "Butterfly",
                },
            ],
        },
        {
            "nombre": "Tríceps",
            "ejercicios": [
                {
                    "nombre": "Extensión de tríceps de pie",
                    "series": "2 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie, sostén una mancuerna con ambas manos por encima de la cabeza con los brazos extendidos. Baja la mancuerna doblando los codos detrás de la cabeza, manteniendo los codos quietos, y vuelve a extender los brazos.",
                    "carpeta": "Standing_Dumbbell_Triceps_Extension",
                },
                {
                    "nombre": "Fondos de tríceps en banco",
                    "series": "2 series x 10 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Siéntate en el borde de una silla o banco firme, con las manos apoyadas a los costados de la cadera y las piernas extendidas hacia adelante. Baja el cuerpo doblando los codos hacia atrás, y empuja con los brazos para volver a subir.",
                    "carpeta": "Bench_Dips",
                },
                {
                    "nombre": "Extensión de tríceps en polea (barra)",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie frente a la polea alta con una barra recta, codos pegados al cuerpo y antebrazos apuntando hacia arriba. Empuja la barra hacia abajo hasta extender los brazos por completo, y vuelve despacio sin mover los codos.",
                    "carpeta": "Triceps_Pushdown",
                },
                {
                    "nombre": "Extensión de tríceps en polea (cuerda)",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie frente a la polea alta con la cuerda, codos pegados al cuerpo. Empuja la cuerda hacia abajo separando las manos levemente al final del movimiento, y vuelve despacio a la posición inicial.",
                    "carpeta": "Triceps_Pushdown_-_Rope_Attachment",
                },
            ],
        },
        {
            "nombre": "Core",
            "ejercicios": [
                {
                    "nombre": "Plancha",
                    "series": "3 series x 20 segundos",
                    "descanso": "40 seg. de descanso entre series",
                    "instrucciones": "Apóyate en el piso sobre los antebrazos y las puntas de los pies, con el cuerpo en línea recta desde la cabeza hasta los talones. Mantén el abdomen contraído y sostén la posición sin dejar caer la cadera.",
                    "carpeta": "Plank",
                },
                {
                    "nombre": "Abdominales (crunch)",
                    "series": "2 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Acostada boca arriba con las rodillas flexionadas y los pies apoyados, manos apenas tocando la cabeza sin entrelazar los dedos. Levanta los hombros del piso contrayendo el abdomen, y baja despacio sin soltar de golpe.",
                    "carpeta": "Crunches",
                },
            ],
        },
        {
            "nombre": "Cardio en caminadora (20 minutos)",
            "ejercicios": [
                {
                    "nombre": "Caminadora · velocidad media",
                    "series": "10 minutos continuos",
                    "descanso": "Sin descanso, ritmo constante",
                    "instrucciones": "Súbete a la caminadora y camina a paso firme y rápido (velocidad media), sin llegar a trotar. Deberías poder hablar entrecortado pero no sostener una conversación larga.",
                    "carpeta": "Walking_Treadmill",
                },
                {
                    "nombre": "Caminadora · velocidad baja",
                    "series": "10 minutos continuos",
                    "descanso": "Sin descanso, ritmo constante",
                    "instrucciones": "Baja la velocidad a un paso suave y cómodo, para ir enfriando el cuerpo después del ritmo medio. Deberías poder hablar sin esfuerzo.",
                    "carpeta": "Walking_Treadmill",
                },
            ],
        },
    ],
    "enfriamiento": {
        "nombre": "Enfriamiento y estiramiento",
        "duracion": "5 minutos",
        "detalle": "Estira pecho, tríceps y espalda baja al terminar, sosteniendo cada estiramiento unos 20 segundos.",
    },
    "notas": [
        "Toma agua antes, durante y después de la rutina.",
        "Si sientes dolor articular (no solo cansancio muscular), detente y avísale a tu entrenador/a.",
        "En la plancha, prioriza mantener la cadera alineada por sobre aguantar más tiempo.",
        "Con esta sesión ya completaste piernas, espalda/brazos y pecho/core: la próxima semana puedes repetir el ciclo aumentando un poco el peso o las repeticiones.",
    ],
}

DIA_4 = {
    "slug": "dia4",
    "dia": "Día 4",
    "titulo": "Rutina de Femoral, Pantorrillas y Glúteos",
    "subtitulo": "Nivel principiante · Cuarta sesión",
    "calentamiento": {
        "nombre": "Calentamiento",
        "duracion": "5 minutos",
        "detalle": "Marcha suave en el lugar, círculos de cadera y estocadas suaves sin peso antes de empezar.",
    },
    "bloques": [
        {
            "nombre": "Femoral (isquiotibiales)",
            "ejercicios": [
                {
                    "nombre": "Peso muerto rumano con mancuernas",
                    "series": "3 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "De pie, sostén una mancuerna en cada mano frente a los muslos, con las rodillas ligeramente flexionadas. Baja las mancuernas deslizándolas por delante de las piernas, empujando la cadera hacia atrás y manteniendo la espalda recta, hasta sentir el estiramiento en la parte de atrás del muslo. Vuelve a subir apretando los glúteos.",
                    "carpeta": "Stiff-Legged_Dumbbell_Deadlift",
                },
                {
                    "nombre": "Curl femoral en máquina (acostada)",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Acuéstate boca abajo en la máquina de curl femoral, con el borde del cojín justo debajo de las pantorrillas. Flexiona las rodillas llevando el cojín hacia los glúteos, y baja despacio a la posición inicial.",
                    "carpeta": "Lying_Leg_Curls",
                },
                {
                    "nombre": "Curl femoral sentada",
                    "series": "3 series x 12 repeticiones",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "Siéntate en la máquina con la espalda apoyada, el cojín superior sobre los muslos y el cojín inferior detrás de las pantorrillas. Flexiona las rodillas llevando el cojín hacia abajo, y vuelve despacio a la posición inicial.",
                    "carpeta": "Seated_Leg_Curl",
                },
                {
                    "nombre": "Curl femoral de pie",
                    "series": "3 series x 12 repeticiones por lado",
                    "descanso": "45 seg. de descanso entre series",
                    "instrucciones": "De pie en la máquina, apoya el torso en el respaldo y coloca la parte de atrás de una pierna bajo el cojín. Flexiona la rodilla llevando el talón hacia el glúteo, y baja despacio. Completa las repeticiones y cambia de pierna.",
                    "carpeta": "Standing_Leg_Curl",
                },
            ],
        },
        {
            "nombre": "Pantorrillas",
            "ejercicios": [
                {
                    "nombre": "Elevación de talones sentada",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Sentada en la máquina, con los muslos bajo el cojín y las puntas de los pies apoyadas en la plataforma. Levanta los talones lo más alto posible apretando la pantorrilla, y baja despacio hasta estirar bien.",
                    "carpeta": "Seated_Calf_Raise",
                },
                {
                    "nombre": "Elevación de talones de pie",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "De pie en la máquina, con los hombros bajo las almohadillas y las puntas de los pies en la plataforma. Sube los talones lo más alto posible, y baja despacio controlando el movimiento.",
                    "carpeta": "Standing_Calf_Raises",
                },
            ],
        },
        {
            "nombre": "Glúteos",
            "ejercicios": [
                {
                    "nombre": "Patada de glúteo en el piso",
                    "series": "2 series x 15 repeticiones por lado",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "En el piso, apoyada en manos y rodillas (como en cuatro patas). Sin arquear la espalda, lleva una rodilla hacia atrás y arriba estirando la pierna, apretando el glúteo arriba. Baja controlando y repite antes de cambiar de lado.",
                    "carpeta": "Glute_Kickback",
                },
                {
                    "nombre": "Puente de glúteo a una pierna",
                    "series": "2 series x 10 repeticiones por lado",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Acostada boca arriba con las rodillas flexionadas, levanta una pierna llevando la rodilla al pecho. Empuja con el talón de la otra pierna y levanta la cadera, apretando el glúteo. Baja despacio y repite antes de cambiar de lado.",
                    "carpeta": "Single_Leg_Glute_Bridge",
                },
                {
                    "nombre": "Hip thrust con barra",
                    "series": "3 series x 10 repeticiones",
                    "descanso": "60 seg. de descanso entre series",
                    "instrucciones": "Siéntate en el piso con la espalda apoyada en un banco y la barra sobre la cadera (empieza solo con la barra, sin discos, para aprender el movimiento). Apoya los pies firmes en el piso y empuja la cadera hacia arriba apretando los glúteos, hasta que el torso quede paralelo al piso. Baja despacio y repite.",
                    "carpeta": "Barbell_Hip_Thrust",
                },
                {
                    "nombre": "Abducción de cadera en máquina",
                    "series": "3 series x 15 repeticiones",
                    "descanso": "30 seg. de descanso entre series",
                    "instrucciones": "Siéntate en la máquina de abducción con las piernas dentro de los cojines. Empuja las piernas hacia afuera separándolas, apretando el glúteo, y vuelve despacio a la posición inicial sin soltar de golpe.",
                    "carpeta": "Thigh_Abductor",
                },
            ],
        },
    ],
    "enfriamiento": {
        "nombre": "Enfriamiento y estiramiento",
        "duracion": "5 minutos",
        "detalle": "Estira femorales, pantorrillas y glúteos al terminar, sosteniendo cada estiramiento unos 20 segundos.",
    },
    "notas": [
        "Toma agua antes, durante y después de la rutina.",
        "Si sientes dolor articular (no solo cansancio muscular), detente y avísale a tu entrenador/a.",
        "En el peso muerto rumano, la espalda siempre recta: el movimiento sale de la cadera, no de la cintura.",
        "Con esta sesión completaste el cuerpo entero en 4 días: la próxima semana puedes repetir el ciclo aumentando un poco el peso o las repeticiones.",
    ],
}

DIAS = [DIA_1, DIA_2, DIA_3, DIA_4]

PAGINAS_NAV = [
    {"slug": "index", "dia": "Día 1", "titulo": "Rutina Inicial de Piernas y Cardio"},
    {"slug": "dia2", "dia": "Día 2", "titulo": "Rutina de Espalda, Bíceps y Hombros"},
    {"slug": "dia3", "dia": "Día 3", "titulo": "Rutina de Pecho, Tríceps y Core"},
    {"slug": "dia4", "dia": "Día 4", "titulo": "Rutina de Femoral, Pantorrillas y Glúteos"},
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
    return render_dia(DIA_1)


@app.route("/dia2")
@app.route("/dia2.html")
def dia2():
    return render_dia(DIA_2)


@app.route("/dia3")
@app.route("/dia3.html")
def dia3():
    return render_dia(DIA_3)


@app.route("/dia4")
@app.route("/dia4.html")
def dia4():
    return render_dia(DIA_4)


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
