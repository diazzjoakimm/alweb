"""Servidor del sitio de Alweb (Flask).

Sirve la página principal. Todas las consultas terminan en WhatsApp: los botones
y el formulario abren un chat con el número que está en contenido.py.
"""
import os
from datetime import datetime
from urllib.parse import quote

from flask import Flask, render_template

import contenido as c

app = Flask(__name__)


def enlace_whatsapp(texto=""):
    """Devuelve el enlace al chat de WhatsApp, con un mensaje escrito si se indica."""
    url = "https://wa.me/" + c.NEGOCIO["whatsapp_numero"]
    if texto:
        url += "?text=" + quote(texto)
    return url


# Disponible en las plantillas como wa("Hola, quiero consultar por...")
app.jinja_env.globals["wa"] = enlace_whatsapp


@app.after_request
def cabeceras(respuesta):
    respuesta.headers.setdefault("X-Content-Type-Options", "nosniff")
    respuesta.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    return respuesta


@app.get("/")
def inicio():
    return render_template(
        "index.html",
        negocio=c.NEGOCIO,
        tipos=c.TIPOS_PROYECTO,
        pros=c.PROS,
        contras=c.CONTRAS,
        etapas=c.ETAPAS,
        compromisos=c.COMPROMISOS,
        faq=c.FAQ,
        anio=datetime.now().year,
    )


@app.errorhandler(404)
def no_encontrada(_error):
    return render_template("404.html", negocio=c.NEGOCIO), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
