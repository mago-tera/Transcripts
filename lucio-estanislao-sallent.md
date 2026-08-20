# Reunión Teramot — Estanislao Sallent (consultor / Inspectia)

**Participantes:**
- Lucio Rojas (Teramot)
- Estanislao Sallent (consultor de datos; dueño del software **Inspectia** — control de stock/ingresos para fábricas y empresas logísticas)

**Cliente del caso mostrado:** representante de venta B2B de Motorola (vende
flotas de teléfonos a empresas), con una nueva unidad de e-commerce B2B/B2C.

---

## Caso de uso

Estanislao usa Teramot como consultor para construir analítica sobre los datos
de su cliente (representante B2B de Motorola). Armó **dos tableros** apoyados en
~5 gold tables (optimizadas por performance, no una gold por join):

**1. Tablero de stock / reposición**
Conecta stock, venta y el árbol de productos (gama → familia → modelo → SKU).
Sobre esa base cargó conocimiento de negocio como datos y metodología:
- Proyección de venta y cálculo de semanas de venta por unidad (stock actual vs.
  proyección).
- Reglas de **reemplazo de SKU** (modelos que se llaman distinto pero son
  reemplazo: se agrupa por "posición" para no pedir un SKU quebrado cuando su
  demanda ya migró al reemplazo).
- Clasificación de estado: sano / por quebrar / sobre-stock.
- Cobertura de días objetivo (15–90 días) con burbujas por venta/mes y tamaño.
- Antigüedad del stock: capital inmovilizado, distribución por antigüedad,
  antigüedad por rotación, stock muerto (>1 año, rotación lenta) → gatillo para
  promos/cuotas y aceleración de rotación.
- Planificación semanal de compra (se pide los martes; el lunes entra la lista
  de lo que está en riesgo de quiebre).

**2. Tablero comercial (revisión semanal de KPIs)**
Ventas, unidades, órdenes, mejor mes, ticket promedio, precio promedio, empresas
registradas, clientes, performance mensual/semanal, empresas de alta con datos
transaccionales, aperturas por producto/familia/gama/posición, y financiación
(cuotas, pasarela, medios de pago, transacciones con dos tarjetas).

**Extensión planteada:** llevar a Teramot la gestión de la empresa entera (no
solo la unidad comercial) — cálculo de comisiones de vendedores (hoy ~2 días en
Excel), resultados financieros, cash — y, para sus propios clientes de Inspectia,
un módulo de gestión de stock ("dame tu ERP y tu WMS, me das unas tablas y te
devuelvo el análisis").

**Consumo:** interés en exponer los datos vía un bot dentro de su aplicación y
por WhatsApp (ej. el dueño de la fábrica pregunta "¿cuánto produjimos hoy?"),
usando Teramot como infraestructura/middleware del MCP en lugar de desarrollar
uno propio. Teramot ofrece dos caminos: los **dashboards nativos** (link con
login y roles de Teramot, con agente de preguntas embebido) o una **web propia**
que consuma la **API** de Teramot para más interactividad (filtros, simuladores,
alertas).

---

## Roles y áreas afectadas

- **Consultor de datos (Estanislao):** construye las vistas, gold tables y
  tableros; revende como servicio a sus clientes.
- **Equipo comercial / reposición:** usa el tablero de stock para planificar la
  compra semanal.
- **Dueño de fábrica / gerente de operaciones:** consulta producción diaria por
  bot/WhatsApp.
- **CFO / finanzas:** cálculo de comisiones y resultados financieros (hoy
  manuales en Excel).
- **Vendedores:** afectados por el cálculo de comisiones (2 días de Excel).
- **Análisis comercial:** semanas de venta por aperturas, cobertura de gama.

---

## Testimonios y valor

- "Me resuelve algo que yo ya estaba teniendo que hacer una aplicación y
  conectarlo y todo… me parece mucho más fácil este." — evita construir y
  mantener infraestructura propia (MCP, backend, front).
- **Retención de clientes** como principal driver: "no quiero ni siquiera ganar
  guita con ese módulo, lo que hago es retengo al cliente… un servicio más que lo
  doy yo y no otro."
- **Build vs. buy** (pitch de Lucio, aceptado por Estanislao): "en lo que vos
  tardaste en decirlo, con tu sueldo ya salió más caro que pagar una licencia";
  "¿yo si quiero me pongo a armar un Teramot 2? ¿Para qué lo voy a armar?".
- Reemplaza trabajo manual pesado (comisiones ~2 días en Excel, cruces de cash,
  gestión).
- Reconoce el problema de mantenimiento/soporte de hacerlo in-house: "lo hago
  porque puedo, pero después no le doy bola, no lo mantengo, se van a quejar,
  voy a tener que poner un recurso."
- Valora el manejo de accesos/seguridad de Teramot para publicar dashboards con
  datos de empresa (vs. exponer un artifact suelto).

**Dolor detectado (feedback de producto):** actualizar el artifact es costoso
(hay que rehacerlo, gasta créditos, el "live artifact" de Claude no está
resuelto); pide avisar cuando esté el **artifact interactivo con JavaScript**
(filtros/flujos). Teramot lo tiene en roadmap (~2 semanas para correr en JS).

---

## Señales de compra

- **Alta:** ya tiene los dos tableros armados y los va a **publicar en Teramot
  "ahora seguro" para que los empiecen a consumir**.
- Interés explícito en el modelo **marca blanca / módulo revendible**: "no sé
  cuánto me saldrá el servicio de Teramot… ponele 1000 dólares, pero a mis
  clientes les cobro 100; con 10 clientes ya me lo pagué."
- Pregunta activa por un **servicio B2B** para usar Teramot como infraestructura
  de su MCP (bot en app + WhatsApp).
- **Expansión proyectada:** meter la gestión de la empresa entera si el piloto
  funciona ("una vez que prueben que esto funciona, van a evaluar el otro").
- **Nueva oportunidad:** módulo de gestión de stock para sus clientes de
  Inspectia (ERP/WMS → análisis de reposición y rotación).
- Pide que le avisen cuando esté el artifact interactivo con JS.
- Abierto a una reunión de ~30 min con el ingeniero de IA de Teramot (más
  adelante, aún no priorizado).
- Alta confianza con el cliente mostrado ("tengo mucha confianza con ellos"),
  buen ambiente de relación con Teramot.
