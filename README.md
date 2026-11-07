# Alweb

Sitio web de Alweb en HTML y JavaScript puros, con estilos en **Tailwind CSS v4**. No usa React, Python ni servidor.

Todas las consultas terminan en WhatsApp: los botones y el formulario abren un chat con el número configurado.

## Estructura

```
alweb/
├── package.json            Scripts de Tailwind (dev y build)
├── netlify.toml            Netlify corre npm run build y publica la carpeta public
├── src/
│   └── input.css           Paleta (variables) y componentes. Acá se configura Tailwind
└── public/
    ├── index.html          Página principal (textos y clases de Tailwind)
    ├── 404.html            Página de error
    └── static/
        ├── css/style.css   Se genera solo, no se edita ni se sube a git
        ├── js/main.js      Menú móvil, modo oscuro y formulario
        └── img/            portada.jpg y favicon.svg
```

## Trabajar en local

Necesitás Node 20 o superior.

```bash
npm install        # una sola vez
npm run dev        # genera el CSS y lo mantiene actualizado mientras editás
```

Con `npm run dev` andando, abrí `public/index.html` en el navegador. Para generar el CSS final una vez: `npm run build`.

## Publicarlo

```bash
git add .
git commit -m "Cambios"
git push
```

Netlify (Publish directory `public`, Build command `npm run build`, ambos ya definidos en `netlify.toml`) construye el CSS y publica solo.

## Qué cambiar

1. **Textos:** en `public/index.html`.
2. **WhatsApp:** buscá `541138599781` en `public/index.html` y cambialo en todos los lugares. El número visible (`+54 911 3859 9781`) también está ahí.
3. **Colores:** variables al principio de `src/input.css`. Hay un bloque para modo claro y otro para oscuro. En el HTML se usan como `bg-bg`, `text-muted`, `border-line`, `text-accent`.
4. **Imagen de la portada:** reemplazá `public/static/img/portada.jpg` por otra con el mismo nombre.
5. **Año del pie de página:** está escrito en `public/index.html`, al final.
