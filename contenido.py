"""Contenido del sitio.

Editá este archivo para cambiar textos y datos de contacto.
No hace falta tocar el HTML: las plantillas leen todo desde acá.
"""

NEGOCIO = {
    "titulo": "Alweb",
    "nombre": "Alweb",
    "sufijo": "Diseño web",
    "descripcion": (
        "Diseñamos y programamos sitios web para negocios y profesionales: "
        "páginas de presentación, sitios institucionales y tiendas online."
    ),
    "whatsapp_visible": "+54 911 3859 9781",
    # Solo números, con código de país, para armar el enlace de WhatsApp.
    # Si el enlace no abre el chat, probá con 5491138599781 (formato de celular argentino).
    "whatsapp_numero": "541138599781",
}

TIPOS_PROYECTO = [
    "Una página de presentación",
    "Un sitio institucional",
    "Una tienda online",
    "Rediseñar mi sitio actual",
    "Todavía no lo sé",
]

# Pros de tener la página y lo que se deja pasar al no tenerla.
# Cada punto tiene un título corto y una explicación de una línea.
PROS = [
    {
        "titulo": "Te encuentran en Google",
        "texto": "Quien busca lo que ofrecés te encuentra, aunque todavía no te conozca.",
    },
    {
        "titulo": "Atiende las 24 horas",
        "texto": "Tu página muestra qué hacés y cómo trabajás mientras vos estás ocupado o descansando.",
    },
    {
        "titulo": "Transmite confianza",
        "texto": "Un negocio con página propia se ve más serio y más profesional para quien lo busca.",
    },
    {
        "titulo": "Todo en un solo lugar",
        "texto": "Servicios, fotos y contacto en un link que compartís por WhatsApp, Instagram o con un QR.",
    },
    {
        "titulo": "Las consultas llegan a tu WhatsApp",
        "texto": "Quien quiere contratarte te escribe con un toque, con el mensaje ya armado.",
    },
    {
        "titulo": "Es tuya y crece con vos",
        "texto": "No dependés de las reglas de una red social, y podés sumar servicios o una tienda cuando quieras.",
    },
]

CONTRAS = [
    {
        "titulo": "Tus clientes no te encuentran",
        "texto": "Quien busca en Google lo que ofrecés termina en la página de otro.",
    },
    {
        "titulo": "Solo atendés en tu horario",
        "texto": "Quien te busca de noche o el fin de semana no encuentra nada y se va con la competencia.",
    },
    {
        "titulo": "Parecés menos confiable",
        "texto": "Hoy mucha gente busca un negocio en internet antes de escribirle, y sin página no te ve.",
    },
    {
        "titulo": "Tu información está dispersa",
        "texto": "Fotos en un lado, datos en otro y contacto en otro, y cada cliente tiene que armar el rompecabezas.",
    },
    {
        "titulo": "Respondés lo mismo una y otra vez",
        "texto": "Las mismas preguntas por mensaje, todos los días, que una página explica sola.",
    },
    {
        "titulo": "Dependés de las redes",
        "texto": "Si cambia el algoritmo o se bloquea tu cuenta, perdés tu vitrina.",
    },
]

ETAPAS = [
    {
        "nombre": "Terreno",
        "duracion": "1 a 3 días",
        "texto": "Charlamos sobre tu negocio, a quién le hablás y qué querés que haga la pagina. Nos dejas las ideas y colores claros y un precio cerrado.",
    },
    {
        "nombre": "Planos",
        "duracion": "4 a 5 días",
        "texto": "organizo la pagina y ordeno tus textos e imágenes. Lo revisás antes de que se diseñe nada.",
    },
    {
        "nombre": "Obra",
        "duracion": "1 a 2 semanas",
        "texto": "Diseñamos y programamos. Te mostramos avances reales en un enlace de prueba y lo vamos ajustando con vos.",
    },
    {
        "nombre": "Entrega",
        "duracion": "2 días",
        "texto": "Publicamos tu pagina, probamos en celulares y computadoras, y te mandamos el link y QR de tu pagina.",
    },
]

COMPROMISOS = [
    {
        "titulo": "Precio cerrado antes de empezar",
        "texto": "Recibís una propuesta escrita con alcance, plazos y valor. Si el proyecto cambia, lo conversamos antes de cobrar un peso más.",
    },
    
    {
        "titulo": "Respuesta en 24 horas hábiles",
        "texto": "Cada consulta tiene respuesta de una persona real, durante el proyecto y después de la entrega.",
    },
]

FAQ = [
    {
        "pregunta": "¿Cuánto cuesta un sitio?",
        "respuesta": "Depende del tipo de proyecto y de lo que necesites. Escribinos por WhatsApp contando qué querés lograr y te pasamos un presupuesto cerrado.",
    },
    {
        "pregunta": "¿Cuánto tarda hacer un sitio?",
        "respuesta": "Una página de presentación puede estar lista en 7 a 10 días. Un sitio institucional lleva alrededor de 3 semanas y una tienda online entre 5 y 6. Los tiempos dependen de qué tan rápido nos pases textos e imágenes.",
    },
    {
        "pregunta": "¿Tengo que tener los textos y las fotos listos?",
        "respuesta": "No hace falta. Podemos ayudarte a ordenar y escribir los textos, y a elegir qué fotos usar. Si no tenés fotos propias, te orientamos para conseguir buen material.",
    },
    {
        "pregunta": "¿Voy a poder editar el sitio yo mismo?",
        "respuesta": "Sí. Te dejamos un panel para cambiar textos, imágenes y productos, y una capacitación corta para que lo uses con seguridad.",
    },
    {
        "pregunta": "¿Cómo se paga?",
        "respuesta": "Trabajamos con una seña del 35% para empezar y el 65% restante al entregar. Aceptamos cualquier tipo de transeferencia.",
    },
]
