# Reunión Teramot — Franco Corbalán (Milicic) · #2 Feedback de Dashboards

**Participantes:**
- Lucio Rojas (Teramot)
- Nicolas Andrade (Teramot — producto/ingeniería)
- Franco Corbalán (Milicic — analista funcional SAP)
- (Lotur / equipo Teramot)

**Contexto:** seguimiento tras probar la feature de Dashboards. Milicic corre
SAP + SAC; Franco tuvo que presentar el resultado a la gerencia (Martín — jefe,
David — gerente). Fecha: (no especificada en la transcripción; posterior a #1).

---

## Caso de uso

Franco construyó en Cloud/Teramot un tablero de **gestión de flotas/equipos**
(flotas iniciales, compras proyectadas, necesidad de equipo, uso y disponibilidad
de proyecto, horas, kilómetros). Flujo que usa: Teramot normaliza tablas y
entiende el negocio → gold tables → usa **Cloud como "diseñador de gráficos"**
para maquetar el artifact → quiere **deployarlo en Teramot** y publicarlo como
link auto-actualizable.

Al llevar el artifact de Cloud a la feature de Dashboards de Teramot, encontró
brechas (ver abajo). Comparó contra su stack actual (SAC conectado a SAP por
vistas CDS, refresco cada ~30 min).

---

## Roles y áreas afectadas

- **Analista funcional SAP (Franco):** entiende negocio, arma gold y maqueta con
  Cloud.
- **Analista de datos / BI:** en el proceso tradicional hace el maquetado y los
  gráficos (persona dedicada).
- **Programador:** vistas CDS sobre SAP.
- **Gerencia / directorio (Martín, David):** deciden; validan la parte visual.
- **Nuevo recurso "Teramot":** en 1–2 semanas entra una persona dedicada 100% a
  esto en Milicic.

---

## Qué opina de la feature de Dashboards (testimonios y valor)

**Lo muy positivo:**
- *"El análisis de datos la verdad que es impresionante"* — a nivel dato/normalización, excelente.
- La **publicación como link** con seguridad/roles de Teramot le encantó a su
  jefe Martín: reemplaza el plan B de armar una página web propia.
- El **agente embebido en el dashboard** para hacer preguntas: *"eso está muy
  bueno y es muy valioso"*.
- El **auto-refresh desde SAP** vía gold lo ve como ventaja real frente a SAC.
- **Ahorro de tiempo enorme:** el proceso tradicional (entender negocio + BI +
  CDS + validación en SAC) tarda **~1,5 a 2 meses** (indicadores grandes, hasta
  6 meses con idas y vueltas); con Teramot el análisis de datos baja a **~1
  semana**. Involucra 3 personas → 1 de negocio.

**Las reservas / bloqueantes (feedback de producto):**
- La feature generó **4 dashboards separados (uno por gold)**, con **distinta
  disposición/interfaz** que el artifact de Cloud, y **no copia el tablero tal
  como él lo construyó**. La primera ejecución trajo **tablas vacías / valores
  desarmados**.
- No puede unificarlos en **un solo link** para compartir — necesita ese
  dinamismo (tabs no alcanzan; quiere navegación/filtros).
- **Motivo técnico:** Teramot **sanitiza y elimina el JavaScript** por su sandbox
  de seguridad; el artifact de Cloud (cambio de pestañas, cálculos, filtros)
  corre en JS, por eso no se replica idéntico. Nicolás: la diferencia es sobre
  todo de **prompting + mapeo de data dinámica**, no de datos.
- **Veredicto de negocio, sin filtro:** *"Hoy en día, a Teramot como está, con
  los gráficos que me hizo, no le puedo ir a hablar a un gerente."* A la gerencia
  le convenció el gráfico del **artifact de Cloud**, no el de Teramot.

**Respuesta de Teramot (roadmap):**
- Dos correcciones ya en staging/testing (salen a producción en ~1–2 semanas):
  (1) **una gold por dashboard → poder usar varias gold en un mismo dashboard**;
  (2) pasar de HTML/CSS estático a **soportar scripts JavaScript** (sanitizados)
  para dashboards dinámicos/interactivos.
- Truco intermedio: pestañas visuales con CSS puro (sin JS).

---

## Señales de compra

- **Adopción en marcha:** ya presentó a la gerencia el artifact de Cloud como
  "cómo debería quedar" + lo que Teramot logra a nivel datos. Publicará sus
  tableros en Teramot para consumo.
- **Recurso dedicado:** en 1–2 semanas entra una persona 100% dedicada a Teramot
  en Milicic; Franco le pasará todo el contexto.
- **Expansión de alcance:** Lucio propone pensar Teramot también como herramienta
  de negocio (auditoría de cuentas a pagar, cobranzas, control y gestión) — hay
  **webinar de control y gestión la semana siguiente**, Franco lo lleva a Martín.
- **Caso de éxito / testimonio:** Franco acepta dar testimonio sobre el ahorro de
  tiempo (antes vs. con Teramot) para marketing, sujeto a OK de Martín. *"Soy
  testigo, lo probé, le veo cosas muy buenas."*
- Compromiso alto: seguirá reportando bugs/feedback por mail; le importa que la
  herramienta "sea funcional a Milicic".
- Va a compartir por WhatsApp el artifact (y ojalá el de SAP) para que Teramot lo
  use como referencia a replicar.

**Próximo paso comercial sugerido:** cerrar la prueba con una presentación de
cierre y escalar a conversación comercial con el jefe/gerencia una vez que salgan
las dos correcciones de la feature.
