# Reunión Teramot — Franco Corbalán (Milicic) · #1 Power BI y feature de Dashboards

**Participantes:**
- Lucio Rojas (Teramot)
- Lotar Baigorria (Teramot)
- Franco Corbalán (Milicic — analista funcional SAP)

**Contexto:** Milicic corre SAP + **SAC (SAP Analytics Cloud)**. Franco arma
indicadores para el directorio. Fecha: (no especificada en la transcripción;
reunión anterior a la #2).

---

## Caso de uso

Franco ya usa Teramot para el análisis de tablas y la generación rápida de
indicadores, validando que los resultados sean correctos. El objetivo de la
reunión es resolver **cómo publicar y automatizar** un indicador (KPI "rígido"
para directorio) que se alimente de tablas gold actualizadas desde SAP.

Se discuten tres caminos:
1. **Conexión a Power BI** (ya disponible en Teramot, vía export ODBC). Limitante:
   Power BI sirve para consultar/DAX pero no dibuja el dashboard solo — obliga a
   tener una persona (o IA asistida) maquetando, con las dos pantallas a mano.
2. **Feature de Dashboards de Teramot** (en desarrollo, demo en vivo por Lotar):
   con una o varias gold, desde el MCP o la página, se genera un dashboard
   informativo (histograma, torta, etc.) que se actualiza a medida que se
   actualizan los datos, y se publica como URL.
3. **API de Teramot**: generar una API key y armarse un front (React) propio que
   consuma las gold, con un modelo Anthropic embebido para dibujar dashboards
   (lo mismo que hace Teramot internamente).

Lucio plantea la tesis de **dos grupos de solución**: (a) KPIs estáticos de
gestión (dashboard publicado y auto-actualizado) y (b) tablas gold + modelo con
MCP a libre disposición de cada usuario de negocio para preguntas abiertas,
patrones, predicción, optimización.

---

## Roles y áreas afectadas

- **Analista funcional SAP (Franco y equipo):** entiende las tablas/negocio y
  arma el análisis funcional.
- **Analista de datos / BI:** maqueta el KPI y genera los gráficos.
- **Programador:** crea las vistas CDS sobre SAP que consumen los gráficos.
- **Directorio / gerencia (Martín — jefe, David — gerente):** consumidores
  finales de los indicadores; a quienes hay que "venderles" la herramienta.
- **Usuarios de negocio (ej. Alejandro):** reciben el link del indicador.

---

## Testimonios y valor

- **Comparación de tiempos (el gran driver):** el proceso actual en SAP para un
  indicador puede tardar **hasta 6 meses** (analista funcional → BI maqueta →
  programador hace CDS → validación en SAC). Con Teramot, la parte de análisis
  funcional / entender la unidad de negocio se resolvió en **~3 días**. *"Los dos
  puntos te va a parecer una locura… lo hicimos en tres días."*
- **Validación de datos:** Franco corroboró resultados y "a nivel dato está muy
  bueno".
- **Primer cliente al que se le muestra la feature en vivo** — feedback valioso
  para producto (Lotar: *"serías el primer cliente al que le mostramos esto"*).
- Valora que el dashboard se publique como URL, se actualice solo desde SAP vía
  gold, y la autoservicio por API (Lucio le pegó a la API sin ayuda de devs para
  una automatización de alertas en n8n).

**Dolor / bloqueante detectado:** no puede **publicar el artifact de Cloud** ni
lograr que se **automatice** con las tablas gold — justo lo que necesita. Probó
el chat interno de Teramot para generar dashboards y no lo logró. La feature de
Dashboards resolvería esto pero aún no está en producción general.

---

## Señales de compra

- **Alta urgencia:** le pidieron **presentar esto a la gerencia** (Martín/David);
  necesita algo para mostrar el viernes siguiente.
- Pide activamente acceso anticipado a la feature (Lucio ofrece soltarla en un
  feature flag / soporte particular en ~1 semana).
- Va a **adelantar en paralelo** la integración por API para una página web.
- Reconoce el ahorro brutal de tiempo/personas (de 3 personas + meses a 1 persona
  de negocio + días).
- Abierto a compartir cómo lo implementa (útil como referencia para Teramot).
- Lucio pide encuadrar la prueba con inicio/cierre y luego pasar a una
  conversación comercial con su jefe.
