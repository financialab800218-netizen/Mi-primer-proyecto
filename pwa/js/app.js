// ============================================
// TutorIA Cuba - PWA
// ============================================

const API_URL = "https://game-belongs-benz-sri.trycloudflare.com";

const $ = (id) => document.getElementById(id);

function mostrarMensaje(texto, tipo) {
  const el = $("mensaje");
  el.textContent = texto;
  el.className = "mensaje " + tipo;
}

function limpiarMensaje() {
  const el = $("mensaje");
  el.className = "mensaje hidden";
  el.textContent = "";
}

function guardarSesion(token, usuario) {
  localStorage.setItem("token", token);
  localStorage.setItem("usuario", JSON.stringify(usuario));
}

function obtenerToken() {
  return localStorage.getItem("token");
}

// ============================================
// Cambio de pestanas
// ============================================

function activarTab(cual) {
  const tabLogin = $("tab-login");
  const tabRegistro = $("tab-registro");
  const formLogin = $("form-login");
  const formRegistro = $("form-registro");

  if (cual === "login") {
    tabLogin.classList.add("active");
    tabRegistro.classList.remove("active");
    formLogin.classList.remove("hidden");
    formRegistro.classList.add("hidden");
  } else {
    tabRegistro.classList.add("active");
    tabLogin.classList.remove("active");
    formRegistro.classList.remove("hidden");
    formLogin.classList.add("hidden");
  }
  limpiarMensaje();
}

// ============================================
// Login
// ============================================

async function hacerLogin(e) {
  e.preventDefault();
  limpiarMensaje();

  const email = $("login-email").value.trim();
  const password = $("login-password").value;
  const boton = e.target.querySelector("button[type=submit]");

  boton.disabled = true;
  boton.textContent = "Entrando...";

  try {
    const res = await fetch(API_URL + "/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (!res.ok) {
      throw new Error(data.detail || "Error al entrar");
    }

    guardarSesion(data.token, data.usuario);
    mostrarMensaje("Bienvenido, " + data.usuario.nombre, "success");

    setTimeout(() => {
      window.location.href = "app.html";
    }, 800);

  } catch (err) {
    mostrarMensaje(err.message, "error");
    boton.disabled = false;
    boton.textContent = "Entrar";
  }
}

// ============================================
// Registro
// ============================================

async function hacerRegistro(e) {
  e.preventDefault();
  limpiarMensaje();

  const nombre = $("reg-nombre").value.trim();
  const email = $("reg-email").value.trim();
  const password = $("reg-password").value;
  const boton = e.target.querySelector("button[type=submit]");

  boton.disabled = true;
  boton.textContent = "Creando...";

  try {
    const res = await fetch(API_URL + "/auth/registro", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, nombre, password })
    });

    const data = await res.json();

    if (!res.ok) {
      throw new Error(data.detail || "Error al crear cuenta");
    }

    guardarSesion(data.token, data.usuario);
    mostrarMensaje("Cuenta creada. Bienvenido!", "success");

    setTimeout(() => {
      window.location.href = "app.html";
    }, 800);

  } catch (err) {
    mostrarMensaje(err.message, "error");
    boton.disabled = false;
    boton.textContent = "Crear cuenta";
  }
}

// ============================================
// Invitado y arranque
// ============================================

function entrarComoInvitado() {
  localStorage.setItem("invitado", "1");
  window.location.href = "app.html";
}

document.addEventListener("DOMContentLoaded", () => {
  $("tab-login").addEventListener("click", () => activarTab("login"));
  $("tab-registro").addEventListener("click", () => activarTab("registro"));
  $("form-login").addEventListener("submit", hacerLogin);
  $("form-registro").addEventListener("submit", hacerRegistro);
  $("btn-invitado").addEventListener("click", entrarComoInvitado);

  if (obtenerToken()) {
    window.location.href = "app.html";
  }
});
