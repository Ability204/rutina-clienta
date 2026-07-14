const DB_NAME = "rutina_progreso";
const STORE_NAME = "fotos";

function abrirDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, 1);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        const store = db.createObjectStore(STORE_NAME, { keyPath: "id", autoIncrement: true });
        store.createIndex("fecha", "fecha");
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function guardarFoto({ fecha, nota, blob }) {
  const db = await abrirDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, "readwrite");
    tx.objectStore(STORE_NAME).add({ fecha, nota, blob, creado: Date.now() });
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

async function obtenerFotos() {
  const db = await abrirDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, "readonly");
    const request = tx.objectStore(STORE_NAME).getAll();
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function borrarFoto(id) {
  const db = await abrirDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, "readwrite");
    tx.objectStore(STORE_NAME).delete(id);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

function formatearFecha(fechaISO) {
  const [anio, mes, dia] = fechaISO.split("-");
  const meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
  return `${parseInt(dia, 10)} de ${meses[parseInt(mes, 10) - 1]} de ${anio}`;
}

async function renderGaleria() {
  const galeria = document.getElementById("galeria");
  const vacia = document.getElementById("galeria-vacia");
  const fotos = await obtenerFotos();

  if (fotos.length === 0) {
    vacia.style.display = "block";
    galeria.innerHTML = "";
    return;
  }
  vacia.style.display = "none";

  fotos.sort((a, b) => (a.fecha < b.fecha ? 1 : -1));

  const porFecha = {};
  for (const foto of fotos) {
    if (!porFecha[foto.fecha]) porFecha[foto.fecha] = [];
    porFecha[foto.fecha].push(foto);
  }

  galeria.innerHTML = "";
  for (const fecha of Object.keys(porFecha).sort((a, b) => (a < b ? 1 : -1))) {
    const grupo = document.createElement("div");
    grupo.className = "grupo-fecha";

    const titulo = document.createElement("h3");
    titulo.textContent = formatearFecha(fecha);
    grupo.appendChild(titulo);

    const grid = document.createElement("div");
    grid.className = "grid-fotos";

    for (const foto of porFecha[fecha]) {
      const tarjeta = document.createElement("div");
      tarjeta.className = "foto-tarjeta";

      const img = document.createElement("img");
      img.src = URL.createObjectURL(foto.blob);
      img.alt = `Foto del ${formatearFecha(foto.fecha)}`;
      tarjeta.appendChild(img);

      if (foto.nota) {
        const nota = document.createElement("p");
        nota.className = "foto-nota";
        nota.textContent = foto.nota;
        tarjeta.appendChild(nota);
      }

      const btnBorrar = document.createElement("button");
      btnBorrar.className = "foto-borrar";
      btnBorrar.type = "button";
      btnBorrar.textContent = "Eliminar";
      btnBorrar.addEventListener("click", async () => {
        if (confirm("¿Eliminar esta foto? No se puede deshacer.")) {
          await borrarFoto(foto.id);
          renderGaleria();
        }
      });
      tarjeta.appendChild(btnBorrar);

      grid.appendChild(tarjeta);
    }

    grupo.appendChild(grid);
    galeria.appendChild(grupo);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const fechaInput = document.getElementById("fecha-foto");
  fechaInput.value = new Date().toISOString().slice(0, 10);

  const form = document.getElementById("form-foto");
  const mensaje = document.getElementById("mensaje-guardado");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const fecha = fechaInput.value;
    const nota = document.getElementById("nota-foto").value.trim();
    const archivo = document.getElementById("input-foto").files[0];

    if (!archivo) return;

    await guardarFoto({ fecha, nota, blob: archivo });

    form.reset();
    fechaInput.value = new Date().toISOString().slice(0, 10);

    mensaje.textContent = "Foto guardada correctamente.";
    setTimeout(() => (mensaje.textContent = ""), 3000);

    renderGaleria();
  });

  renderGaleria();
});
