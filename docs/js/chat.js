const API_URL = "https://common-rats-starting-nokia.trycloudflare.com";

const $ = (id) => document.getElementById(id);
let agenteActual = "pablo";
let enviando = false;

const NOMBRES = {
  pablo:   { nombre: "Pablo",   cargo: "Director Adjunto",      emoji: "P" },
  ernesto: { nombre: "Ernesto", cargo: "Contador Jefe Digital",  emoji: "E" },
  marta:   { nombre: "Marta",   cargo: "Asesora Legal",          emoji: "M" },
  camilo:  { nombre: "Camilo",  cargo: "Ingeniero Agronomo",     emoji: "C" },
  celia:   { nombre: "Celia",   cargo: "Coordinadora Academica", emoji: "C" },
  julian:  { nombre: "Julian",  cargo: "Director Comercial",     emoji: "J" },
  ruben:   { nombre: "Ruben",   cargo: "Jefe de Mantenimiento",  emoji: "R" },
};

function agregarBurbuja(texto, tipo) {
  const burbuja = document.createElement("div");
  burbuja.className = "mensaje-burbuja " + tipo;
  burbuja.textContent = texto;
  $("chat-mensajes").appendChild(burbuja);
  $("chat-mensajes").scrollTop = $("chat-mensajes").scrollHeight;
  return burbuja;
}

async function enviarMensaje(e) {
  e.preventDefault();
  if (enviando) return;
  const input = $("chat-input");
  const texto = input.value.trim();
  if (!texto) return;
  enviando = true;
  input.value = "";
  $("chat-enviar").disabled = true;
  agregarBurbuja(texto, "user");
  const cargando = agregarBurbuja("Pensando...", "assistant cargando");
  try {
    const res = await fetch(API_URL + "/agentes/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ agente: agenteActual, mensaje: texto })
    });
    const data = await res.json();
    cargando.remove();
    if (!res.ok) {
      agregarBurbuja("Error: " + (data.detail || "no se pudo responder"), "assistant");
    } else {
      agregarBurbuja(data.respuesta, "assistant");
    }
  } catch (err) {
    cargando.remove();
    agregarBurbuja("Error de conexion. Intenta de nuevo.", "assistant");
  }
  enviando = false;
  $("chat-enviar").disabled = false;
  input.focus();
}

function cambiarAgente(id) {
  agenteActual = id;
  const info = NOMBRES[id];
  $("agente-nombre").textContent = info.nombre;
  $("agente-cargo").textContent = info.cargo;
  $("agente-emoji").textContent = info.emoji;
  document.querySelectorAll(".agente-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.agente === id);
  });
  const cont = $("chat-mensajes");
  cont.innerHTML = "";
  agregarBurbuja("Hola, soy " + info.nombre + ". " + info.cargo + ". En que puedo ayudarte?", "assistant");
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".agente-btn").forEach(b => {
    b.addEventListener("click", () => cambiarAgente(b.dataset.agente));
  });
  $("chat-form").addEventListener("submit", enviarMensaje);
  $("chat-input").focus();
});
