# Alweb

Sitio web completo para un servicio de diseño web. Python (Flask) en el servidor, HTML con plantillas Jinja, CSS y JavaScript en archivos separados.

Todas las consultas terminan en WhatsApp: los botones de la página y el formulario abren un chat con el número configurado.

## Cómo correrlo

Necesitás Python 3.9 o más nuevo.

```bash
cd alweb
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrí http://127.0.0.1:5000 en el navegador.

Para desarrollar con recarga automática: `FLASK_DEBUG=1 python app.py` (en Windows PowerShell: `$env:FLASK_DEBUG=1; python app.py`).

Importante: el HTML usa plantillas, así que no se puede abrir `templates/index.html` con doble clic. Hay que correr `app.py`.

## Estructura

```
alweb/
├── app.py              Servidor: página principal, enlaces de WhatsApp, página 404
├── contenido.py        Textos, pros y contras, etapas, preguntas y datos de contacto
├── requirements.txt
├── templates/
│   ├── index.html      Página principal
│   ├── _casa.html      Ilustración de la portada (SVG)
│   └── 404.html        Página de error
└── static/
    ├── css/style.css   Estilos y paleta de colores
    ├── js/main.js      Menú móvil, modo claro/oscuro, formulario
    └── img/favicon.svg
```

## Qué cambiar

1. **WhatsApp:** en `contenido.py`, bloque `NEGOCIO`. El número actual es +54 11 3859 9781 (`541138599781`). Si el enlace no abre el chat, probá con `5491138599781`, que es el formato de celular argentino.
2. **Textos, pros y contras:** `contenido.py`.
3. **Colores:** al principio de `static/css/style.css` están las variables de la paleta. Hay tres bloques: modo claro, modo oscuro automático y modo oscuro manual. Si cambiás un color, cambialo en los tres.
4. **Textos de la portada:** en `templates/index.html`.

## Cómo llegan las consultas

- Los botones "Escribinos", "Pedir una propuesta", "Consultar por WhatsApp" y "Abrir chat" abren el chat de WhatsApp.
- El formulario arma un mensaje con el nombre, lo que necesita la persona y su descripción, y abre WhatsApp con ese texto listo para enviar. No se guarda nada en el servidor.

## Publicarlo

Para producción no uses `python app.py`. Instalá un servidor como gunicorn y corré:

```bash
pip install gunicorn
gunicorn -w 2 app:app
```

Ponelo detrás de Nginx o en un servicio de hosting que soporte Python, con HTTPS activado.
