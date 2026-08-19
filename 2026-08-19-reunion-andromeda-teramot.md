# Reunión Teramot — Andrómeda (Aurora / FID)

**Fecha:** 2026-08-19
**Participantes:**
- Lucio Rojas (Teramot)
- Franco Ferrero (Teramot — comercial)
- Sebastián Marcello (Andrómeda / Aurora — CEO, Lic. en Sistemas, contable)
- Nahuel (Andrómeda / Aurora — sistemas, especialista en n8n)

---

## Contexto

Reunión comercial entre Teramot y Andrómeda, empresa que desarrolla el ERP
**Andrómeda** (sistema de gestión administrativa multi-industria, con fuerte
desarrollo en la parte de producción). Andrómeda también arma tableros
(Power BI, tablas dinámicas) y ayuda a sus clientes a mejorar procesos y a
usar bien el sistema.

Lucio abre explicando qué es Teramot: una startup (origen en EE.UU., hoy en
Rosario) que vincula sistemas/ERPs con inteligencia artificial para facilitar
la explotación de datos. Trabaja de forma agnóstica al sistema (SAP, ERPs
locales como Andrómeda, o cualquier motor de base de datos), arma un warehouse,
provee infraestructura y busca democratizar el acceso a la información — que un
usuario de negocio genere sus propias vistas, tablas y dashboards desde un chat
conversacional.

---

## Demo (sobre el cliente Clínica/Química Molón)

Lucio muestra la plataforma Teramot usando datos del cliente **Química Molón**
(con permiso de Juan, consultor independiente que usa Teramot para dar servicio
a ese cliente).

**Estructura de la plataforma:**
- Cada cliente = un **workspace** (aislado a nivel infraestructura).
- Dentro del workspace, **proyectos** (pueden verse como áreas de la empresa).
- Dentro de los proyectos, se conectan diversas **fuentes**.

**Conectores disponibles:** bases de datos tradicionales (Postgres, MySQL,
SQL Server, Azure), buckets AWS, BigQuery, y conectores en desarrollo a
Salesforce, Monday, Airtable, SAP HANA.

**Caso Química Molón:** los datos estaban en SQL Server. Se creó un usuario de
vistas y se coordinó la conexión con el equipo de infraestructura. La vista
entregada tenía tres tablas: estadísticas de compra, estadísticas de venta y
resumen contable. Esa información se carga en AWS (tenant por cliente) y se
actualiza a diario mediante un cron.

**Conexión a Claude vía MCP:** se configura una URL y un token para vincular
las tablas del sistema con Claude. Teramot genera metadata a nivel columna
(descripción y tipo de dato) para que el modelo actúe como asesor de datos
sobre las tablas reales, entienda joins, claves primarias/foráneas y el
contexto de negocio.

**Flujo mostrado:**
1. Se rutea Claude al workspace y proyecto (Control de gestión).
2. Claude sugiere análisis posibles a partir de las tablas disponibles
   (rentabilidad por artículo, performance de vendedores, análisis de clientes,
   compras por proveedor, resultado contable mensual, margen por zona, etc.).
3. Claude genera nuevas vistas ("tablas gold") pasando a Teramot los
   requerimientos funcionales; Teramot construye el SQL y deja la tabla
   deployada en la infraestructura, con actualización según la fuente y linaje.
4. El usuario final consulta esas tablas directamente desde Claude (preguntas
   de negocio), sin consumir licencia extra de Teramot.

**Ejemplo de pregunta de negocio:** "¿Cuántos clientes concentran el 80% de la
facturación?" → respondió que el 79,9% (con la observación de Sebastián de que
detecta al consumidor final como cliente — una regla de negocio a refinar). Los
datos de venta cubrían ~8 meses de 2026 (limitados a pedido de Química Molón).

**Dashboards:** feature nueva. Claude genera un tablero (snapshot HTML), se lo
pasa a Teramot y queda como dashboard que se actualiza mirando las tablas gold.
Da un link público (permalink) que requiere login en Teramot y respeta los
roles/permisos del usuario. (En la demo el dashboard falló al renderizar,
posiblemente por un error en la creación de la gold table.)

**Gobernanza / roles:** administrador (crea y comparte), miembro (crea tablas),
solo lectura (solo consulta). Los workspaces están totalmente aislados entre sí.
Se pueden compartir tablas puntuales a un equipo con acceso solo-lectura.

**Seguridad:** certificación SOC, con auditoría cada seis meses.

**Otras vías de consumo:** conexión a Power BI vía export ODBC, y API con
documentación para construir páginas web o automatizaciones (n8n pega a las
tablas gold por API).

---

## Discusión comercial

**Modelo de negocio de Teramot:** es un SaaS (no consultoría), con pricing por
uso (cantidad de usuarios, vistas/tablas nuevas generadas, GB de almacenamiento
y procesamiento). A Teramot le es indiferente quién contrate:
- El cliente final (ej. Química Molón) conecta sus datos y explota desde Claude.
- Andrómeda trae a sus clientes, paga la licencia y lo revende como módulo de
  IA con su propio margen.
- Consultores de datos que usan Teramot para dar servicio.

**Marca blanca (Franco):** Andrómeda puede ofrecer Teramot como marca blanca,
como parte de su propio servicio, sin exponer la marca Teramot. El esquema de
pricing se arma en conjunto y, si se avanza, se coordina reunión con el jefe
del área comercial de Teramot.

**Ejemplo de propuesta:** ofrecer a un cliente un "módulo de IA" (ej. USD 500/mes),
donde Teramot cobra ~400 y Andrómeda retiene margen; o usarlo como herramienta
interna para acelerar la creación de reportes/tableros.

**Requisito técnico:** el usuario necesita una IA con soporte MCP (Claude o
ChatGPT sirven; Gemini no, porque no acepta MCP).

**Métricas de Teramot:** ~300 usuarios en cuentas B2B; producto en mercado
desde ~marzo (menos de un año). Química Molón es una cuenta con tres usuarios.

**Plan free:** disponible para probar sin límite; se pueden compartir CSVs o
conectar un módulo como se hizo con Química Molón (Juan estaría en plan free).

---

## Feedback y próximos pasos

- Sebastián lo ve muy interesante, aunque aún no tiene claro cómo lo
  implementaría (históricamente todos sus desarrollos son propios, pero está
  abierto a herramientas de terceros por el ritmo de cambios). Dudas sobre
  costos.
- **Acción (Teramot):** enviar material/información para compartir internamente
  con las distintas áreas de Andrómeda.
- **Acción (Andrómeda):** digerir la propuesta y evaluar internamente.
- Posible reunión posterior con el área comercial de Teramot para armar el
  esquema de pricing/marca blanca.
