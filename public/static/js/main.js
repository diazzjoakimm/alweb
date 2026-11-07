/* Alweb: menú móvil, modo claro/oscuro, sección activa y formulario que abre WhatsApp. */
(function () {
  'use strict';

  var root = document.documentElement;

  /* ---------- Modo claro / oscuro ---------- */
  var temaBtn = document.getElementById('tema');

  function temaActual() {
    return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }

  if (temaBtn) {
    temaBtn.setAttribute('aria-pressed', String(temaActual() === 'dark'));
    temaBtn.addEventListener('click', function () {
      var nuevo = temaActual() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', nuevo);
      temaBtn.setAttribute('aria-pressed', String(nuevo === 'dark'));
      try { localStorage.setItem('tema', nuevo); } catch (e) { /* sin almacenamiento */ }
    });
  }

  /* ---------- Menú en celulares ---------- */
  var menu = document.getElementById('menu');
  var menuBtn = document.getElementById('menu-btn');

  function cerrarMenu() {
    if (!menu || !menuBtn) { return; }
    menu.classList.remove('open');
    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.setAttribute('aria-label', 'Abrir menú');
  }

  if (menu && menuBtn) {
    menuBtn.addEventListener('click', function () {
      var abierto = menu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(abierto));
      menuBtn.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
    });
    menu.addEventListener('click', function (ev) {
      if (ev.target.closest('a')) { cerrarMenu(); }
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') { cerrarMenu(); }
    });
  }

  /* ---------- Sección activa en el menú ---------- */
  var enlaces = {};
  document.querySelectorAll('.nav a.link').forEach(function (a) {
    enlaces[a.getAttribute('href').slice(1)] = a;
  });

  if ('IntersectionObserver' in window) {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (!e.isIntersecting) { return; }
        Object.keys(enlaces).forEach(function (id) {
          enlaces[id].classList.toggle('is-active', id === e.target.id);
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });

    Object.keys(enlaces).forEach(function (id) {
      var seccion = document.getElementById(id);
      if (seccion) { observador.observe(seccion); }
    });
  }

  /* ---------- Aparecer al hacer scroll ---------- */
  var revelar = document.querySelectorAll('.revela');
  if ('IntersectionObserver' in window) {
    var visor = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          visor.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revelar.forEach(function (el) { visor.observe(el); });
  } else {
    revelar.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Brillo que sigue al cursor en las tarjetas ---------- */
  document.querySelectorAll('.glow').forEach(function (tarjeta) {
    tarjeta.addEventListener('pointermove', function (ev) {
      var r = tarjeta.getBoundingClientRect();
      tarjeta.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
      tarjeta.style.setProperty('--my', (ev.clientY - r.top) + 'px');
    });
  });

  /* ---------- Inclinación 3D de la imagen de la portada ---------- */
  var foto = document.querySelector('[data-tilt]');
  if (foto && window.matchMedia('(hover: hover) and (prefers-reduced-motion: no-preference)').matches) {
    foto.addEventListener('pointermove', function (ev) {
      var r = foto.getBoundingClientRect();
      var x = (ev.clientX - r.left) / r.width - 0.5;
      var y = (ev.clientY - r.top) / r.height - 0.5;
      foto.style.transform = 'perspective(1000px) rotateY(' + (x * 8) + 'deg) rotateX(' + (-y * 8) + 'deg)';
    });
    foto.addEventListener('pointerleave', function () { foto.style.transform = ''; });
  }

  /* ---------- Formulario: arma el mensaje y abre WhatsApp ---------- */
  var form = document.getElementById('form-contacto');
  if (!form) { return; }

  var estado = document.getElementById('estado');
  var campos = ['nombre', 'mensaje'];

  function valor(id) {
    return document.getElementById('f-' + id).value.trim();
  }

  function limpiar() {
    campos.forEach(function (c) {
      var error = document.getElementById('e-' + c);
      var campo = document.getElementById('f-' + c);
      error.hidden = true;
      error.textContent = '';
      campo.removeAttribute('aria-invalid');
    });
    estado.textContent = '';
    estado.className = 'form-status';
  }

  function mostrarErrores(errores) {
    var primero = null;
    campos.forEach(function (c) {
      if (!errores[c]) { return; }
      var error = document.getElementById('e-' + c);
      var campo = document.getElementById('f-' + c);
      error.textContent = errores[c];
      error.hidden = false;
      campo.setAttribute('aria-invalid', 'true');
      if (!primero) { primero = campo; }
    });
    if (primero) { primero.focus(); }
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    limpiar();

    var nombre = valor('nombre');
    var tipo = valor('tipo');
    var mensaje = valor('mensaje');

    var errores = {};
    if (nombre.length < 2) { errores.nombre = 'Escribí tu nombre.'; }
    if (mensaje.length < 10) { errores.mensaje = 'Contanos tu proyecto en al menos 10 caracteres.'; }
    if (Object.keys(errores).length) {
      mostrarErrores(errores);
      estado.textContent = 'Revisá los campos marcados.';
      estado.className = 'form-status error';
      return;
    }

    var texto = 'Hola, soy ' + nombre + '. Quiero consultar por: ' + tipo.toLowerCase() + '.\n\n' + mensaje;
    var url = form.getAttribute('data-wa') + '?text=' + encodeURIComponent(texto);

    // Se abre con un enlace temporal para que el navegador lo trate como acción de la persona.
    var enlace = document.createElement('a');
    enlace.href = url;
    enlace.target = '_blank';
    enlace.rel = 'noopener';
    document.body.appendChild(enlace);
    enlace.click();
    enlace.remove();

    var manual = document.createElement('a');
    manual.href = url;
    manual.target = '_blank';
    manual.rel = 'noopener';
    manual.textContent = 'tocá acá';
    estado.textContent = 'Abriendo WhatsApp con tu mensaje. Si no se abrió, ';
    estado.appendChild(manual);
    estado.appendChild(document.createTextNode('.'));
    estado.className = 'form-status ok';
  });
})();
