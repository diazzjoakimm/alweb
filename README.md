# Alweb

Sitio web de Alweb en HTML, CSS y JavaScript puros. No usa Python ni ningún servidor.

Todas las consultas terminan en WhatsApp: los botones y el formulario abren un chat con el número configurado.

## Estructura

```
alweb/
├── netlify.toml            Le dice a Netlify que publique la carpeta public
└── public/
    ├── index.html          Página principal (acá están todos los textos)
    ├── 404.html            Página de error
    └── static/
        ├── css/style.css   Estilos y colores
        ├── js/main.js      Menú móvil, modo oscuro y formulario
        └── img/            portada.jpg y favicon.svg
```

## Verlo en tu compu

Abrí `public/index.html` con doble clic.

## Publicarlo

```bash
git add .
git commit -m "Cambios"
git push
```

Netlify (conectado a este repo, Publish directory `public`, Build command vacío) se actualiza solo.

## Qué cambiar

1. **Textos:** en `public/index.html`.
2. **WhatsApp:** buscá `541138599781` en `public/index.html` y cambialo en todos los lugares. El número que se ve en pantalla (`+54 911 3859 9781`) también está ahí.
3. **Colores:** al principio de `public/static/css/style.css`.
4. **Imagen de la portada:** reemplazá `public/static/img/portada.jpg` por otra con el mismo nombre.
5. **Año del pie de página:** está escrito en `public/index.html`, al final.
