# Grupo Ayudin <> Teramot

**Fecha:** 2026-09-04T14:30  
**Duracion:** ~77 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** pablo.barbarelli@grupoayudin.com, christian.schiavo@grupoayudin.com, federico.viola@grupoayudin.com, Gabriel Puertas, Agustin Garcia  
**Externos:** pablo.barbarelli@grupoayudin.com, christian.schiavo@grupoayudin.com, federico.viola@grupoayudin.com  
**Archivo origen:** Grupo Ayudin _ Teramot - 2026-09-04 14_30 GMT-03_00/Grupo Ayudin _ Teramot_ 2026_09_04 14_30 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Demostración de Teramot con conectores MCP y análisis de datosDemostración y conectividad inicialGabriel Puertas presentó una demostración técnica utilizando archivos Excel y bases de datos SAP mediante protocolos de contexto de modelo. El sistema generó capas de datos estructuradas y consultas SQL automáticas para evaluar márgenes de ganancia.Análisis y casos de usoChristian Schiavo validó la precisión de los resultados mediante definiciones de margen bruto y correlaciones de gastos comerciales. Se discutió la gestión de tokens y la publicación de tableros interactivos para el equipo directivo.Licenciamiento y propuesta comercialAgustin Garcia detalló los roles de usuario y la infraestructura en Amazon Web Services. Pablo Barbarelli y Christian Schiavo evaluaron el plan inicial de Software como Servicio por 400 dólares mensuales para iniciar una prueba piloto.

### Decisiones

Requiere más debate
Adopción propuesta del plan Starter SaaS Se propuso utilizar el plan Starter en la versión SaaS por $400 mensuales con 5 usuarios member y 5 viewers para pruebas iniciales, quedando pendiente de revisión y aprobación interna.
Acordada
Estructura de usuarios con roles Member y Viewer Se acordó implementar un esquema de permisos que distingue entre usuarios Member con capacidad de conexión MCP y edición, y usuarios Viewer con acceso de solo lectura.

### Próximos pasos

[Gabriel Puertas] Validar calculos: Validar los cálculos de margen bruto (gross margin) del archivo de muestra comparándolos con los números reales proporcionados para verificar la precisión del modelo.
[Agustin Garcia] Enviar propuesta: Preparar la orden de magnitud y la propuesta comercial detallando las opciones para el modelo de software como servicio y la instalación local considerando los perfiles de usuario.
[Pablo Barbarelli, Christian Schiavo] Activar plan: Comunicar a Agustin Garcia la decisión de activar el plan inicial de software como servicio la próxima semana.
[Christian Schiavo, Pablo Barbarelli] Configurar conexiones: Definir las vistas y la estructura de los datos para la ingesta y la recurrencia necesarias en el inicio del proyecto.

### Detalles

Inicio de la reunión y demostración de la prueba de concepto: La reunión inicia con los saludos de Agustín Garcia, Gabriel Puertas, Christian Schiavo y Pablo Barbarelli, junto con el aviso de Fede Viola sobre su retiro anticipado por otro compromiso. Gabriel Puertas, cofundador y director de operaciones de Teramot, comparte su pantalla para presentar una demostración de la tecnología utilizando un archivo Excel proporcionado previamente por Christian Schiavo (00:00:07).
Conectores de datos y actualización desde un almacén de datos: Gabriel Puertas explica que, aunque la demostración utiliza un archivo Excel, la herramienta está diseñada para conectarse directamente a un almacén de datos (data warehouse), permitiendo actualizaciones dinámicas y periódicas, ya sea de forma horaria, incremental o diaria. Pablo Barbarelli consulta sobre los requerimientos de replicación, a lo que se responde que la integración optimiza el uso de información preexistente y facilita la incorporación de fuentes adicionales como sistemas de gestión de relaciones con clientes (CRM) e informes externos (00:02:56).
Procesamiento de capa de datos y uso de protocolo MCP: Tras cargar el archivo en una capa inicial (capa bronce), Gabriel Puertas muestra cómo la tecnología genera automáticamente una capa limpia (capa silver) mediante agentes que interpretan la información, gestionan valores nulos y crean metadatos (00:05:04). Para interactuar con los datos, se emplea un conector de protocolo de contexto de modelo (MCP por sus siglas en inglés) que permite utilizar la herramienta con diferentes proveedores de modelos de lenguaje grande (LLM), utilizando en la prueba una cuenta personal de la herramienta Claude (00:07:27).
Generación de capas de datos y consultas mediante inteligencia artificial: Mediante el conector MCP, la interfaz de inteligencia artificial analiza las tablas disponibles y construye la capa final solicitada, estructurando una tabla de pérdidas y ganancias (P&L) con dimensiones de marca, categoría, unidad de mantenimiento de stock (SKU), material, canal, subcanal y gerencia (00:10:23). Christian Schiavo y Pablo Barbarelli validan el proceso en el cual la herramienta actúa como intérprete para generar consultas estructuradas en SQL y descripciones detalladas de cada paso ejecutado (00:12:09).
Revisión de resultados y casos de uso analíticos: Durante la revisión de los resultados generados para un mes específico de datos, Christian Schiavo señala que los datos son simulados, pero destaca la utilidad de resolver preguntas complejas que los tableros tradicionales no cubren de forma inmediata. Pablo Barbarelli y Christian Schiavo discuten la necesidad de responder interrogantes específicas sobre rentabilidad y márgenes de ganancia por canal sin depender de desarrollos manuales previos (00:17:02).
Conexión directa con bases de datos SAP: Gabriel Puertas presenta un ejemplo alternativo donde la herramienta se conecta directamente con sistemas SAP, interpretando vistas complejas, realizando uniones (joins) y generando estructuras de datos unificadas (00:19:25). Se destaca que este flujo permite controlar el acceso a la información mediante roles de usuario y mantener la trazabilidad de los cambios realizados en las fuentes de verdad (00:22:07).
Iteración de consultas y corrección de inconsistencias: Pablo Barbarelli consulta sobre cómo se gestionan las inconsistencias en los resultados obtenidos desde SAP. Gabriel Puertas explica que el proceso de depuración se realiza mediante la interacción directa con el modelo de lenguaje, el cual edita y ajusta las consultas automáticamente al detectar anomalías específicas en los datos, operando de manera similar a la programación asistida (00:25:48).
Interacción de usuarios ejecutivos y gestión de conocimiento: Respecto a la interacción de directivos con la herramienta, Gabriel Puertas recomienda configurar proyectos específicos con vistas acotadas en lugar de dar acceso directo a bases complejas (00:27:52). Asimismo, se explica la funcionalidad de almacenamiento de contexto, la cual permite registrar criterios empresariales específicos de cálculo, como la determinación del indicador de resultados antes de intereses, impuestos, depreciación y amortización (EBITDA) o la distribución de costos de marketing (00:29:04).
Publicación de tableros y automatizaciones adicionales: Gabriel Puertas demuestra la capacidad de transformar los resultados en un tablero interactivo basado en código HTML, el cual se publica dentro de la plataforma para mantenerse conectado a la fuente de datos en tiempo real y compartirse con perfiles sin permisos de edición (00:31:29). Adicionalmente, se menciona la posibilidad de integrar estos flujos con herramientas de automatización como N8N para generar alertas operativas de inventario o resúmenes automatizados (00:34:14).
Evaluación de usabilidad y análisis de margen bruto: Christian Schiavo reflexiona sobre la usabilidad de la herramienta, señalando que la creación de tableros requiere un nivel avanzado, pero valora positivamente la capacidad de realizar preguntas de negocio directas y obtener indicadores complejos (00:37:07). Para evaluar la precisión, Christian Schiavo proporciona una definición de negocio específica para el margen bruto (beneficio bruto dividido entre ventas netas) junto con datos de referencia para el mes de julio (00:38:31).
Análisis de marcas y rendimiento por gerencia: A partir de las preguntas orientadas, la herramienta procesa los datos y genera hallazgos detallados sobre el margen bruto, identificando que las diferencias de rendimiento entre gerencias se explican principalmente por el peso de las marcas comercializadas y las estructuras de precios por canal (00:42:07). Christian Schiavo confirma la validez de los resultados y destaca que estos análisis iniciales permiten profundizar rápidamente en el desempeño comercial (00:43:12).
Correlación de gastos comerciales y canibalización: Christian Schiavo plantea una consulta avanzada sobre la correlación entre el gasto comercial en marketing y exhibición (trade spending) y las ventas netas en diferentes canales y cadenas (00:44:23). Se discute también la capacidad de la herramienta para identificar fenómenos complejos como la canibalización de productos, facilitando que el equipo comercial evalúe el impacto real de los lanzamientos y las promociones (00:46:25).
Resultados de gasto comercial y gestión de tokens: El sistema procesa la correlación del gasto comercial, mostrando cómo este se descuenta entre las ventas brutas y netas, y detallando la concentración del gasto en hipermercados frente al canal de comercio electrónico (00:48:34). Ante la consulta sobre los costos operativos de los modelos de lenguaje, Gabriel Puertas sugiere utilizar las suscripciones personales o de equipo de cada usuario (como Claude o GPT) para acotar y controlar el gasto en tokens de manera eficiente (00:49:43).
Modelo de licenciamiento y roles de usuario: Pablo Barbarelli y Christian Schiavo estructuran el caso de uso para el equipo directivo utilizando una suscripción combinada con la plataforma Teramot y conectores MCP (00:54:04). Agustín Garcia detalla el esquema de licenciamiento, especificando que los usuarios con rol de miembro ("member") tienen capacidad de conexión y edición mediante MCP, mientras que los usuarios con rol de visualizador ("viewer") operan bajo un esquema de solo lectura, manteniendo una jerarquía estricta de permisos sobre la información disponible (00:55:11).
Roles de usuario y permisos del sistema: Agustin Garcia detalló la distinción entre usuarios miembros, quienes pueden generar y modificar datos para madurar el modelo (como gerentes o analistas que elaboran reportes), y usuarios visualizadores, quienes únicamente consultan la información sin modificarla para prevenir errores operativos. Pablo Barbarelli y Christian Schiavo evaluaron que esta estructura permite una participación activa de los líderes mientras protege los datos frente a modificaciones accidentales (00:58:57).
Arquitectura de datos y almacenamiento: Christian Schiavo planteó la integración de 15 tablas (con métricas de costos de fabricación, ventas, dotación de personal, costos de materiales y logística) para proporcionar una perspectiva global a la junta directiva (01:01:13). Christian Schiavo explicó que esto requiere un nuevo almacén de datos independiente de la fuente principal de la verdad de la compañía debido a las complejas reglas de negocio de SAP (01:02:36). Agustin Garcia indicó que la plataforma opera sobre una infraestructura en la nube de Amazon Web Services con certificación SOC 2 y auditorías bianuales, ofreciendo modalidades de Software como Servicio o despliegue local en la infraestructura propia del cliente (01:03:51).
Modelos de licenciamiento y costos del servicio: Agustin Garcia explicó que el modelo de Software como Servicio incluye límites definidos de almacenamiento y procesamiento por una tarifa mensual, mientras que la instalación local requiere que el cliente provea su propio almacenamiento y capacidad de procesamiento (01:04:57). Asimismo, Agustin Garcia señaló que el servicio contempla sesiones de incorporación (onboarding) y soporte continuo del equipo de éxito del cliente para optimizar la estructura de datos y garantizar la eficiencia en la conexión con el protocolo MCP (01:06:18).
Plan de pruebas inicial y propuesta comercial: Pablo Barbarelli solicitó una propuesta económica que contemple tanto el formato de Software como Servicio como la instalación local, sugiriendo un esquema inicial de cinco usuarios miembros y cinco visualizadores. Christian Schiavo propuso ejecutar una prueba piloto a menor escala con el área de tecnología utilizando dos o tres tablas durante un periodo de uno a dos meses (01:08:42). En respuesta, Agustin Garcia recomendó iniciar con el plan inicial (starter) en Software como Servicio por un valor de 400 dólares mensuales, advirtiendo que migrar posteriormente a una infraestructura local podría resultar más costoso. Pablo Barbarelli expresó su preferencia por el modelo de Software como Servicio para evitar sobrecargar al equipo de infraestructura (01:10:02).
Conectividad de datos y escalabilidad futura: Agustin Garcia y Christian Schiavo analizaron los mecanismos de ingesta de datos, sugiriendo el uso de vistas o archivos en formato Excel para demostrar valor rápidamente, dado que Christian Schiavo está estructurando las 15 tablas con identificadores de cliente uniformes (01:12:14). Ante consultas de Pablo Barbarelli sobre los límites de capacidad y el salto hacia planes empresariales de 2000 dólares, Agustin Garcia confirmó la viabilidad de establecer planes intermedios y aseguró que la plataforma operará sin inconvenientes de capacidad hacia el presupuesto del año 2027 (01:13:19). Gabriel Puertas participó de forma remota en el cierre de la sesión mientras se trasladaba a buscar a un familiar (01:14:40).

---

## Transcripcion

**Agustin Garcia**: Buenas, buenas.

**Gabriel Puertas**: Bueno, bueno,

**Agustin Garcia**: Hola, Cristian.

**Christian Schiavo**: Buenas tardes. ¿Qué tal, Agustín Gabriel?

**Agustin Garcia**: Todo muy bien.

**Gabriel Puertas**: Cristian. ¿Todo bien?

**Agustin Garcia**: Vos bien por suerte.

**Christian Schiavo**: ¿Todo muy bien ustedes? Bueno,

**Gabriel Puertas**: Tranquilo.

**Christian Schiavo**: me alegro.

**Agustin Garcia**: Todo tranquilo.

**Christian Schiavo**: Bueno, estupendo. Ah, vemos si viene Pablo. Ya pingueo

**Agustin Garcia**: Ahí está.

**Gabriel Puertas**: ¿Hay alguien? Lo acepté.

**Fede Viola**: Hola, ¿cómo están?

**Christian Schiavo**: también.

**Agustin Garcia**: Hola, F, ¿cómo estás? Muy bien vos.

**Fede Viola**: Muy bien. Yo solo avisarles, no voy a interrumpir después, eh, que unos minutos antes de 30 me voy a bajar porque tengo otra que a la que subirme, pero no los vuelvo a interrumpiramos.

**Gabriel Puertas**: Der.

**Agustin Garcia**: Vale, ningún problema. Gracias por avisar.

**Christian Schiavo**: buscar el set de datos enos y

**Agustin Garcia**: Ahí está Pablo.

**Pablo Barbarelli**: ¿Cómo andan?

**Christian Schiavo**: tal, Pablo

**Agustin Garcia**: Todo muy bien. Vos alegro.

**Pablo Barbarelli**: Todo muy bien, tranquilo. Bueno,

**Christian Schiavo**: Ahí está.

**Pablo Barbarelli**: estamos todos. Cris Fede, eh, usted de lado de ustedes ausán, Gabi.

**Agustin Garcia**: Estamos todos. Eh, no sé si lo conocían a Gabriel,

**Gabriel Puertas**: Ha.

**Agustin Garcia**: Gabriel Puertas es uno de los founders de Teramot y Chief Operating Officer de la empresa. E así que bueno, ya lo puse al tanto de nuestras conversaciones, de de la idea de avanzar con la prueba de concepto, con la demo. Así que que bueno, no sé si tienen alguna duda, o si no ya alargamos.

**Christian Schiavo**: Vamos para adelante.

**Pablo Barbarelli**: Ansiosos, ansiosos por la realar.

**Agustin Garcia**: Pand.

**Christian Schiavo**: Ah.

**Gabriel Puertas**: Dale. Bueno, esperen, voy compartiendo pantalla mientras tanto. Tengo dos opciones que queremos compartir con ustedes. Una es si quieren que larguemos de cero y porque obviamente esto es demo y es tecnología, así que yo ya probé, pero si quieren les muestro lo que yo probé y cómo lo hizo o un poco mejor. Eh, lo vemos lo vemos en vivo cómo funciona y les voy contando cómo pasa.

**Pablo Barbarelli**: Sí,

**Gabriel Puertas**: Me parece que vamos por ahí porque ya cargó todo,

**Pablo Barbarelli**: tenemos No.

**Gabriel Puertas**: así que vamos por ahí. Yeah.

**Pablo Barbarelli**: Si tenemos tiempo. A mí me gustaría entender el proceso, pero pero como digo

**Gabriel Puertas**: Dale, dale, dale.

**Fede Viola**: Eh,

**Gabriel Puertas**: Bueno, nosotros esta demo la vamos a hacer con un con un Excel que ustedes no pasaron, pero ustedes imagínense todo esto conectando bases de datos, o sea, no cambia mucho porque a la larga datos son datos, pero pero digo, el esfuerzo es pensar esto como bueno, una vez que yo hice un conector en una base de datos, yo ese conector ya lo tengo actualizándose todos los días y y yo voy a poder trabajar con esto de forma dinámica.

**Pablo Barbarelli**: Y ahí te hago la te hago la S,

**Gabriel Puertas**: Yo acá en Dale.

**Pablo Barbarelli**: eh te hago la primera pregunta,

**Gabriel Puertas**: Sí, sí.

**Pablo Barbarelli**: justo hoy hablamos con fe en relación a eso. Digo, este producto vamos a ver ahora lo que lo que sí requiere que se vaya replicando la información de, supongamos este Excel, que es la una de las vistas que tenemos en nuestro data warehouse con información financiera, es requerimiento ir replicando información o se puede hacer streaming de esa información y cómo debería

**Gabriel Puertas**: No, o sea,

**Pablo Barbarelli**: ser el

**Gabriel Puertas**: si vos le si nosotros el la herramienta está diseñada para pegarle al warehouse, en el caso de ustedes,

**Pablo Barbarelli**: Claro,

**Gabriel Puertas**: en realidad la herramienta está diseñada incluso para la gente que no tiene warehouse,

**Pablo Barbarelli**: sí,

**Gabriel Puertas**: pero si tiene un warehouse mejor.

**Pablo Barbarelli**: sí me acuerdo La primera presentación que vimos era un armar un un warehouse con con un par de me acuerdo.

**Gabriel Puertas**: Claro, claro.

**Pablo Barbarelli**: Sí.

**Gabriel Puertas**: Pero si ustedes ya tienen un warehouse, eh, es como que vos le pegá a ese y nada, vos después definís un un una frecuencia de de actualización que puede ser incluso horaria, qué sé yo,

**Pablo Barbarelli**: Sí.

**Gabriel Puertas**: que que tenés dos formas.

**Pablo Barbarelli**: M.

**Gabriel Puertas**: Si vos warehouse lo tenés preparado para que nosotros hagamos incremental, nosotros nos podemos traer las novedades, si no podemos discutir una estrategia de incrementalidad con ustedes o si no yo hago dams una vez

**Pablo Barbarelli**: Claro,

**Gabriel Puertas**: por día del warehouse, que eso no suele ser lo más lógico, pero pero bueno, es una opción también, digamos,

**Pablo Barbarelli**: clarísimo.

**Gabriel Puertas**: o cada x cantidad de tiempo. Y un poco la idea es qué le pasa históricamente a los warehouse. Es que nunca tenés todo lo que vos necesitas en el warehouse.

**Gabriel Puertas**: ponerle,"Tengo el warehouse que replica el IRP, pero resulta que mi CRM todavía no está." Entonces,

**Pablo Barbarelli**: Y los maestros.

**Gabriel Puertas**: la idea es conectar acá también el CRM,

**Pablo Barbarelli**: Claro.

**Gabriel Puertas**: conectar los de Excels, conectar, no sé, el informe que te manda la consultora que va a ver los locales, a ver cómo está la cosa, qué s yo, no sé, también lo cargas acá. Dependiendo el proyecto y la persona, pregunto la idea, digamos. Lo bueno del Excel que ustedes me pasaron es que con esto podemos entender todo el proceso qué es lo que hace y en definitiva va a ser lo mismo para cualquier fuente de datos. Ah,

**Christian Schiavo**: Oh.

**Gabriel Puertas**: así que bueno,

**Pablo Barbarelli**: Bien.

**Gabriel Puertas**: nosotros acá cargamos lo que me pasó Cristian, que era un Excel. Yo en particular no lo miré al Excel, pero pero bueno, lo subimos. Una vez que yo lo subo, lo siguiente que ocurre es muy parecido al proceso de de armar un warehouse. O sea, yo tomo eso como una capa bronce y voy a construir automáticamente una sil una silver. Esa silver se hace agénticamente, o sea, yo paso de bronce a silver haciendo sanitizaciones y lo que más importante genero metadata.

**Gabriel Puertas**: Este es, si se fijan, yo lo que les mostré, subí el Excel, es una capa bronce. Acá lo que le estoy mostrando, ustedes están viendo, ¿no? Sí. Eh, la ya el mismo archivo, mantenemos el nombre, pero en una capa silver. ¿Y qué cambió? Primero, yo los agentes interpretaron de qué venía la información, tipo representa unique sales recording varios product, no sé. Eh, y si yo expando, que esto es importante, es esta es la query que pasó de bronce a silvers, digamos. Es importante para nosotros transmitirla porque si esto termina siendo una fuente de verdad tenemos que entender. Si vos miras rápido acá lo único que hizo fue algún manejo de nulos y creo que no mucho más, digamos. Está está matando algunos nulos, digamos. Se ve que no era una tabla que haya necesitado mucho procesamiento, pero detectó que hay hay valores que nada para para declararlos como nulo, ¿no?

**Pablo Barbarelli**: Claro,

**Gabriel Puertas**: Y lo que más interesante es esto que es interpretó de qué es, perdón, yo voy a tratar de aumentar esto. Los veo, perdonen,

**Pablo Barbarelli**: estamos metidos entr monitor.

**Gabriel Puertas**: perdonar a si saco acá y queda

**Pablo Barbarelli**: H

**Christian Schiavo**: Ahí va.

**Gabriel Puertas**: más. Bueno, interpretó qué es cada columna. Eso si ustedes conectan ponerle el warehouse, eso va a pasar con cada tabla y con cada columna del warehouse. Ponerle cargar este archivo. Tomó, o sea, todo este proceso habrá tomado 4 o 5 minutos. Nada, si eso hay, digamos, obviamente que no es lineal, ¿no? Pero digo, si el warehouse tiene más tablas, hay procesos corren en paralelo, pero me va tomo un poco más de tiempo y se genera esta información. Esta información obviamente nosotros la presentamos. interesante para leer y entender, pero es con la que se basan después los modelos cuando yo quiero construir la última capa que

**Christian Schiavo**: Mhm.

**Gabriel Puertas**: venía siendo el pedido de coso. ¿Cómo funciona esto? Eh, perdón, acá acto seguido, ¿cómo es la forma de usar Teramot? Al menos lo que nosotros entendemos que es la forma más inteligente es una vez que yo ya ingesté todos los datos, yo ya los tengo todos en una capa silver, eh nosotros tenemos generado un conector MCP para utilizarlo con cualquier otro proveedor de LLM. Entonces, yo en particular uso Cloud y esperen que subo esto.

**Gabriel Puertas**: Acá venimos con Cloud y yo ya tengo hecho el conector. Este conector, eh, este conector de Teramot. Nada, si nos vamos si nos vamos al instructivo, nosotros tenemos acá un instructivo para todos.

**Fede Viola**: M.

**Christian Schiavo**: Oi,

**Gabriel Puertas**: Lo podemos usar con Clpt, pero también, no sé, con Cloud Code o conectarlo con los agentes GitHub o incluso después les cuento un poco más, pero pod hacerlo con N8N y todo ese tipo de cosas que hace automatizaciones. Este es el más sencillo, generar un un conector custom. Pegas esto y esto va a utilizar la misma autentificación que tenemos en Teramod. O sea, si bien vos podés tener puesto el conector de Teramod, solamente vas a ver los proyectos en los cuales vos estás logue y autorizado. Entonces, funciona de esa forma y se autentifica de la misma forma. Entonces, yo vengo acá, le voy a decir con y vamos al WordPace. dos pongo dos porque el uno era el que yo probé, digamos, ese ahí va a tener un proyecto eh permitir hace mucho yo cambié de cuenta la de la acá estoy usando el cloud personal, eh, si revisab porque quería que la prueba sea lo más fiel posible porque si yo uso la otra va a utilizar lo que ya aprendió de la anterior Cloud.

**Gabriel Puertas**: Eh, producción reviso en detalle tabla resultado. Me preguntó no vamos a hacer con esos datos que me pidiera. Lo que voy a hacer es, perdón, acá, no, acá lo tengo al mail de Cristian. Si yo le copió el mail de Cristian. Ahí está. Le pegué directamente tu mail, Cristian. Ahí lo que va a pasar nuestro MCP, ahora esto así de molesto solamente al principio, eh tiene como un set de tools que le permite hacer queries, explorar algunos datos, traer algunos datos así. y específico como y además acceder al a la metadata que nosotros ya generamos. Entonces, ah, bueno, porque habla del archivo junto. Bueno, no sé por qué hizo eso, pero bueno, lo va a ver en los datos, eh, y va lo que lo que va a terminar haciendo es él entender qué es lo que tiene que construir para hacer la última capa de esa capa gol, que era el proceso que le habían pedido, ¿no? Si ustedes ustedes quizás son más técnicos pueden abrir acá y lo que está haciendo es buen la típica coso.

**Pablo Barbarelli**: Yeah.

**Gabriel Puertas**: Acá se fijó la las tool que tiene que tiene disponibles, eligió explorar las tablas, se dio cuenta que está la tabla cargada esta que que tenemos.

**Gabriel Puertas**: Eh, acá está haciendo alguna, piensen en el proceso de ingeniería de datos típico.

**Pablo Barbarelli**: Sí,

**Gabriel Puertas**: ¿Haces alguna fuer exploratoria para entender de qué va? Y acá ya viene con las preguntas. Eh, ¿qué entregable armo primero? La POC, tabla de cascada de cuenta navegable por dimensión. Sí, es primero y esto si ustedes quieren contesten ustedes. Eh, me pregunta por marca, categoría, CKU, material, por canal, subanal, por gerencia, todas con drill down.

**Fede Viola**: Ah,

**Gabriel Puertas**: No falta de respuesta, le mando todas.

**Christian Schiavo**: Esta

**Pablo Barbarelli**: Ah, sí, sí, dale.

**Gabriel Puertas**: Le mando todas. Acá lo que él está haciendo ya sabe porque el el MCP viene con algunas

**Fede Viola**: Pero

**Gabriel Puertas**: instrucciones, lo que está haciendo es eh ya entiende que qué es lo que puede resolver con Teramot y está creando una nueva tabla que ya desagrega todo y cumple con lo que él interpretó que le pedía Christian. Eh,

**Christian Schiavo**: esta partecita es de única ¿Ves? Este es el armado, digamos, de la capa, de la triple capa que hablas vos y estoy llegando a una capa de reporting donde después le voy a hacer n preguntas esa capa de reporting.

**Gabriel Puertas**: vos, o sea, lo que es de única vez es la carga de la información y la generación de esa capa silver. Después vos, ¿qué pasa? Yo fui, yo fui analista y nada, vos tenés armado tu dashord, pero nunca la pregunta que quiere el CEO es exactamente el dashword que vos tenés.

**Pablo Barbarelli**: La que tenés. Nunca la que tenés. Claro,

**Gabriel Puertas**: Claro.

**Pablo Barbarelli**: ya.

**Gabriel Puertas**: Entonces ahí lo que vas a hacer vos es crear nuevas tablas asociadas a lo que vos estás vinculando.

**Christian Schiavo**: entiendo.

**Gabriel Puertas**: Esas tablas le podés hacer las que sean, después borrarlas, mantenerlas,

**Christian Schiavo**: Sí, sí,

**Gabriel Puertas**: no sé.

**Christian Schiavo**: sí. Él está haciendo como un intérprete. Hace un intérprete,

**Gabriel Puertas**: Claro,

**Christian Schiavo**: hace una query por cada pregunta que vos haciendo y la va guardando.

**Gabriel Puertas**: claro. Lo interesante de eso, yo le puedo preguntar, no sé, cómo vienen los costos, qué sé yo, que una pregunta puntual me la va a responder, pero acá el el la POC la entendió como,"Che, tengo que armar una tabla nueva y después sobre eso voy a armar un dashboard que me dé la visibilidad de de todo eso." Ya.

**Christian Schiavo**: Ok.

**Gabriel Puertas**: A ver qué me dijo. ¿Qué queda armado con esto? una tabla de pianel en formato largo donde cada filado de resultado encargado eh encadenado por orden de volumen,

**Fede Viola**: es

**Gabriel Puertas**: gross sale, net sale, total code. A ver, le voy a preguntar qué ruta eh okay, si yo me vengo a Teréram estos chicos me están me

**Fede Viola**: para la empresa

**Gabriel Puertas**: están deployando versiones nuevas en las demos, no pasa nada. That's estudio.

**Fede Viola**: Ah.

**Gabriel Puertas**: Y acá tengo la tabla nueva que creó. Esta es la que acaba de crear Cloud. ¿Cómo es la la query con la que acaba de crear? Así se ve que hizo como no sé qué hizo.

**Christian Schiavo**: Sí, sí,

**Gabriel Puertas**: Hizo un group buy.

**Christian Schiavo**: sí.

**Gabriel Puertas**: Bueno, de todo eso acá la podemos ver a la tabla si quieres ver los números tal cual. Y acá esto que es bastante, digamos, a mí me resulta bastante importante porque piensen que esto no es necesariamente una herramienta técnica, o sea, no todo el mundo lee SQL. Acá tiene como una descripción de de lo que hizo. Entonces, por ejemplo, las instrucciones. Validar la capacidad de la herramienta.

**Gabriel Puertas**: Esta era la la esta era la PO. Necesito una tabla PNL, cascada de cuentas navegable por dimensión con drill down. El Pel viene en formato largo. El campo orden define la secuencia de la cascada y debe usarse para ordenar filtrar las cuentas. Volumen 1, grosel 7, no sé de dónde. Yo entiendo que esto es inferible de los datos que nos pasaron a ustedes.

**Christian Schiavo**: Sí, obvio. Sí, yo le di todas las cuentas del PNL y le puse un ID adelante como para que sea el sorteo de

**Gabriel Puertas**: Ahí va.

**Christian Schiavo**: la de la visualización sea más fácil.

**Gabriel Puertas**: Eh, fijas. Y después gerencia acá 4.7 de NUL. Bueno, en fin, ahí terminó. Esta es la tabla que terminó. Ahora yo le voy a avisar a CL que ya terminó. Ya terminó. Vamos a revisar

**Fede Viola**: Ahora no está todo cabado, pero no se laquina.

**Gabriel Puertas**: ahí la sigue mirando.

**Fede Viola**: 15 bajarte elito para acá baja 15 cilindros se abre y este jugar

**Gabriel Puertas**: La cacada cierra exacto. contra el plan original. A ver, un down y está haciendo pruebas,

**Fede Viola**: Bueno,

**Gabriel Puertas**: está haciendo checks. Bueno, está pro contribution. No sé si estos números le hacen sentido.

**Christian Schiavo**: No, porque está todo sofucado.

**Gabriel Puertas**: Ah.

**Christian Schiavo**: Pero sabes que yo lo que te iba a proponer para eso era trabajar el Excel rápidamente con los datos que te envié y bueno, validar alguno, algún dato,

**Gabriel Puertas**: Dale.

**Christian Schiavo**: que s

**Pablo Barbarelli**: ¿Qué historia teníamos,

**Gabriel Puertas**: Eh

**Pablo Barbarelli**: Cris, en el archivo año actual o algo más?

**Christian Schiavo**: no yo le mandé le mandé eh volumen y monto sí de eh julio de julio de un mes.

**Pablo Barbarelli**: Ah, ok.

**Christian Schiavo**: Sí,

**Pablo Barbarelli**: Ok.

**Christian Schiavo**: e julio. La idea era en el en el mismo periodo que sepa agrupar la

**Fede Viola**: He.

**Christian Schiavo**: información tanto por la jerarquía de producto como por la jerarquía de canal. Entonces digo, bueno, me tiene que me tendría que responder para un canal determinado cuál es el gross profit.

**Pablo Barbarelli**: Sí.

**Christian Schiavo**: con el. Oke.

**Pablo Barbarelli**: No, estaría bueno hacer algunas preguntas, digo, a nivel cuál es un poco lo que decía recién Gabi, digo, ¿cuál es el el dolor que siempre tenemos salir corriendo atrás de la de la construcción de vistas de un informe de para responder preguntas que no podemos responder porque no tenemos la vista prearmada?

**Pablo Barbarelli**: No es un poco el caso de uso. Eh, tenemos varias ya vistas preparadas. eh poder responder cualquier pregunta, ¿no? Entonces, si yo quiero saber, che, pará, cuál es el el conj gross profit,

**Christian Schiavo**: Ese

**Pablo Barbarelli**: eh, o el o el canal menos rentable,

**Gabriel Puertas**: A ver.

**Pablo Barbarelli**: esas cosas así rápidamente, eh, o cosas que se me que no que en el reporting habitual no están.

**Christian Schiavo**: y

**Pablo Barbarelli**: Eso, eso está, ¿no? porque lo buscas,

**Gabriel Puertas**: Ah.

**Pablo Barbarelli**: pero algo así que que nos permita rápidamente ver si puede terminar Eh,

**Christian Schiavo**: por la la idea, perdón, eh ir de menos a más. Yo yo le iría iría pidiéndole un gross profit, no sé, de un canal y después vamos a ir pidiéndole lo último que sería que correlacione determinadas cosas que vos no tenés en un reporte una correlación lineal que te diga cada vez que sucede de A pasa a B o que tenga un índice de correlación entre estas dos variables del tanto por co. Entonces, pero no,

**Pablo Barbarelli**: ahí necesitaríamos más meses, me parece, para que lo pueda

**Gabriel Puertas**: Pero esperen,

**Christian Schiavo**: pero ponele, yo quiero saber el tres pending, ¿cómo juega?

**Christian Schiavo**: ¿Cómo se correlaciona el trade pending con las ventas de la de los skills de una categoría? Si puse más tres pending en una categoría, puse más en otra, en un canal determinado. A ver qué nivel de correlación hay por L.

**Pablo Barbarelli**: Sí, está perfecto.

**Christian Schiavo**: Pero

**Pablo Barbarelli**: Está perfecto.

**Gabriel Puertas**: Pero ahí le hago una consulta ustedes, porque ahí Pablo decía algo que era interesante. ¿Qué tienen o o de dónde está?

**Pablo Barbarelli**: Todo esto viaja de SAPA data feeder, que es

**Gabriel Puertas**: Bueno, a ver, esperen, déjenme que yo voy a hacer algo. Espero que no me rete Agustín, pero digo, yo voy a cancher un poco. Nosotros tenemos una demo, porque nosotros tenemos clientes que le pegan derecho a SAP. Derecho a SAP quiere decir, yo levanto tablas, eh, perdón, este no, porque lo estuve usando hoy y estaba todo medio caído. Bueno, este está medio caído, pero no importa. Este le pega derecho a SAP, interpreta directamente las vistas. como son el SAP, o sea, el si ustedes se fijan en el esquema,

**Pablo Barbarelli**: Sí, sí.

**Gabriel Puertas**: fíjense que SA es asesino como como interpreta,

**Pablo Barbarelli**: Sí,

**Fede Viola**: Ah.

**Pablo Barbarelli**: sí.

**Gabriel Puertas**: pero tiene capacidad de interpretar eso. O sea, quizás ustedes deberían pensar como la posibilidad de incluso un generador de esas vistas de atrás, pues no es que necesita tanta, o sea, lo motores que infieren esta información que nosotros tenemos dentro de Teramot son motores de cloud. Nosotros usamos modelo, o sea, intentamos usar los mejores modelos y conocen de esa entienden de esa estructura. Entonces van a pod poder inferir y vos sobre esto le podés pedir lo mismo. Hagamos el cross,

**Christian Schiavo**: M.

**Gabriel Puertas**: pero desde SAP. Y ahí tiene algunas cosas, o sea, yo no sé si ustedes trabajaron con SAP, pero digo, eh, o sea, digo como si trabajaron directamente con SAP, SAP lo podés configurar como como sea.

**Fede Viola**: de

**Gabriel Puertas**: Entonces también existe la posibilidad de que, digamos, ¿cómo decirle? Habl un ejemplo. Hay cuestiones de de la formación de de esa base de datos que no se pueden inferir. No sé el ejemplo. Eh, vamos a calcular la elevida, todos sabemos lo que es el Levida, pero cada empresa tiene su criterio de cómo calcular el evid cosa. Le doy un ejemplo bastante macro. Ustedes con esto tienen la posibilidad de agregar, digamos, conocimiento específico del de la empresa de ustedes exactamente cómo se calculan ciertas cosas para que el resto de la gente que está utilizando esta herramienta, el agente tenga ese insight de de cómo se calculó.

**Gabriel Puertas**: Yo le yo, o sea, les quise mostrar esto de de SAP particularmente porque tiene capacidad, o sea, si vos conectas eh SAP directo, va a tener capacidad de hacer hacer vistas. Fíjense acá, justamente esto estábamos haciendo un PNL y acá eh la query un poco más compleja. ¿Por qué? porque hizo joins, hizo hizo tiene algunos condicionales y todo más. Eh, acá tenemos un linish, no sé nada. Este PNL lo hizo de tres tablas de SAP que se llaman

**Pablo Barbarelli**: Sí, son las son las que son las que tienen que Sí.

**Christian Schiavo**: típico de SC.

**Gabriel Puertas**: C y lo que sea. Claro, tal cual.

**Fede Viola**: el regalo.

**Christian Schiavo**: Sí.

**Fede Viola**: Eh,

**Gabriel Puertas**: Y y de nuevo vos,

**Fede Viola**: jugar.

**Gabriel Puertas**: o sea, acá tiene las mismas las mismas descripciones y todo y los mismos criterios. Y esto a mí me resulta super importante porque esta esta vista que ustedes crearon, este pianel, vamos a suponer que ustedes lo definen como la fuente de verdad. Este conector nada, una vez por día va, mira los datos de SAP, se traen las novedades y actualiza hasta la tabla Gold. Ustedes pueden darle a otra persona de ayudín, no sé, alguien de finanzas, generarle un proyecto en Teram cuya fuente de datos es esta Gold.

**Gabriel Puertas**: O sea, ustedes controlaron cómo se armó, no le dan SAP a todo el mundo, sino que controlan con la misma lógica que arman un WHub, ¿no? Controlan eso y ya tienen la vista lista para para entregar y esa vista la pueden la pueden editar,

**Christian Schiavo**: Mm.

**Gabriel Puertas**: cambiarla, hacer lo que ustedes quieran, digamos. Incluso tenemos la posibilidad de auditar quién hizo cambios y qué cambios hizo. Eso es importante porque si las tablas terminan siendo fuente de verdad, es importante manejar. Y nada, tenemos una lógica de roles de usuario para para definir quién puede solamente consumir esa información y además quién puede editar esa información, ¿no? Pero bueno, nada, me pareció interesante mostrarle esto.

**Pablo Barbarelli**: Está es importante el punto de es importante el punto de SA. Hoy tenemos, creo que es un caso de uso también nos puede llegar a a repercutir positivamente. Hoy hoy el ejemplo de lo que pasó, Cris era contra una tabla del data warehouse. Lo que teníamos en Data Warehouse que tenemos SAP y tenemos todo lo que no está en SAP, es decir, también eh información que crece cara por archivo de presupuesto, información de fuentes externas, sistema transacional del industrial. Tenemos un un montón de información en Dota Warehouse que hace sentido hoy eh toda esa capa de negocio y lógica y analítica que se armó

**Christian Schiavo**: Ah.

**Pablo Barbarelli**: poder consumirla. Pero me parece también interesante esto de eh analizar también el caso de uso que podría servir ir directo a SAP para alguna cuestión en particular o que también tienes obviamente la capacidad para hacerlo.

**Christian Schiavo**: Sí.

**Gabriel Puertas**: Está bien lo interesante de eso, Pablo, y esto, Uy, espero que que que Agu se se tape. Bueno, que no me rete, pero no importa. Después que me reta, pero no importa. A lo que digo es, vos podés pegarle derecho a SAP.

**Agustin Garcia**: Sedas.

**Gabriel Puertas**: Vos podés pegarle derecho a SAP y que ustedes que son los que arman el warehouse, si queréis usarlo como un prototipado, ¿entendés? O sea,

**Pablo Barbarelli**: Claro.

**Gabriel Puertas**: vos decís,

**Pablo Barbarelli**: Sí, sí.

**Gabriel Puertas**: vamos a ver exactamente cuál es la vista que quiera.

**Pablo Barbarelli**: un interpretador del modelo de datos para después poder construir más rápido.

**Gabriel Puertas**: Claro. Y vos, vos lo tenés acá. O sea, de hecho,

**Pablo Barbarelli**: Sí,

**Gabriel Puertas**: nosotros estamos pensando en si vos ponés un token de GitHub que te replique todo lo que vos hiciste en tu cuenta de GitHub. Fue,

**Pablo Barbarelli**: claro.

**Christian Schiavo**: Mhm.

**Pablo Barbarelli**: Todo, todo,

**Gabriel Puertas**: o sea,

**Pablo Barbarelli**: todo el repositorio.

**Gabriel Puertas**: claro, no son nuestras las fuer que ustedes hacen.

**Pablo Barbarelli**: No,

**Gabriel Puertas**: Entonces, digo,

**Pablo Barbarelli**: claro.

**Gabriel Puertas**: vos te la puedes llevar y eventualmente decir,"Che, la verdad que esta vista es la que la gente consume. Se la saco a Teramo, la pongo en el warehouse y después y después la gente la consume de ahí." Yo lo que

**Pablo Barbarelli**: Y ahí te hago varias preguntas para ver para para orientarnos,

**Gabriel Puertas**: creo sí,

**Pablo Barbarelli**: entender y orientarnos y consultas. Estas queries, armaste un query contra SAPC para armar el PNLN. No, tomemos este ejemplo. El resultado no te dio no tiene inconsistencias. No, no, no fue encontraste problemas.

**Gabriel Puertas**: ahí va.

**Pablo Barbarelli**: ¿Cómo es la el el el lación

**Gabriel Puertas**: Ah, loaz, o sea, le pedí a CL nos ha pasado,

**Pablo Barbarelli**: cómo es intereración? Oké,

**Gabriel Puertas**: nos ha pasado tipo decirle, qué sé yo, eh, te cuento un caso, no sé, en una droguería grande, esta gente maneja maneja deuda con clientes, qué sé yo, y estábamos armando un un una tabla que tenía deudas, se la más o menos la misma dinámica que con Cristian.

**Gabriel Puertas**: Le pegamos el pedido. Clud hizo cuando lo muestra el tipo dice,

**Christian Schiavo**: M.

**Gabriel Puertas**: "Che, mira esa esa tabla, esa ese cliente que aparece al principio, ni un pedo no nos debe esa cantidad guita." Le escribimos así a Cloud,"Che, revisar porque esto no hay un punto acá que está mal." Cloud revisa y se da cuenta que hay una columna que tenía una M para cuando era consignación. Eso es lo que yo digo que que muchas veces,

**Pablo Barbarelli**: Sí, madurez. Madurez.

**Gabriel Puertas**: o sea, depende de la persona que estaba haciendo la base de datos en ese momento, qué sinapsis tuvo para poner una M a la consignación y eso lo tenía que sacar y y lo que hace

**Pablo Barbarelli**: Sí, sí,

**Gabriel Puertas**: Cloud es editar la query, o sea,

**Pablo Barbarelli**: claro. O sea,

**Gabriel Puertas**: edita la query.

**Pablo Barbarelli**: la iteración es vía vía cloud.

**Gabriel Puertas**: Claro,

**Pablo Barbarelli**: Ahora

**Gabriel Puertas**: pensá como pensal ese proceso, pensalo como si estuvieses baicodeando pero con datos. Entonces,

**Pablo Barbarelli**: si yo se lo quiero dar a si yo le quiero una herramienta le Teramot a al SEO de la compañía,

**Gabriel Puertas**: sí.

**Pablo Barbarelli**: eh cómo te imaginas que debería ser eh yo no quiero que es un una persona que tiene 60 3 años, pero tiene muchas preguntas y es muy le gusta, necesita data todo el tiempo, ¿no?

**Gabriel Puertas**: Bien.

**Pablo Barbarelli**: ¿Cómo sería la interacción con Teramo del CO?

**Gabriel Puertas**: Yo en ese caso yo lo que haría sería le armaría un proyecto acá, que es el proyecto de él. Yo controlo las vistas que les pongo, no ni en pedo le pongo SAP porque Claud le va a empezar a preguntar cosas quizá más específica, pero nada, vos más o menos sabés que mira él, mira, no sé, como el flujo de caja,

**Pablo Barbarelli**: Bien. Sí,

**Gabriel Puertas**: mira la deuda la producción,

**Pablo Barbarelli**: sí.

**Gabriel Puertas**: las ventas, qué sé yo, no sé, y vos le ponés esas vistas. Ahí depende la persona si le queré explicar o no que que él puede armarse nuevas vistas, pero Claud lo va a entender en ese sentido. O sea, a nosotros, yo te cuento un poco de nuestra evolución de producto, nosotros hace 4 años estamos laborando con esto y todo el motor de Teramod que arma

**Christian Schiavo**: Ok.

**Gabriel Puertas**: estas quer que limpia los datos, prácticamente no cambió.

**Gabriel Puertas**: O sea, cambió un poco en la medida que van mejorando los modelos, pero lo que realmente nos cambió eh fue el hecho de conectarlo a MCP,

**Pablo Barbarelli**: MCP MC GR Sí, sí,

**Gabriel Puertas**: porque lo que nos pasaba a nosotros es que la gente no sabía dar instrucciones de lo que quería.

**Pablo Barbarelli**: claro, claro.

**Gabriel Puertas**: Entonces, por más instrucciones, por más modelo que vos tengas, las instrucciones son malas, no funcionaba. Lo que tiene esta herramienta como cloud es que son muy buenas para interpretar lo que quiere ese CO y darse vuelta y y dar buenas instrucciones y generar todo esto. Eh, yo creo que sería una buena prueba, o sea, si esa persona es dada a consumir, no tenemos casos así. Hay otro, hay otro que que lo que les pasa es que calculan algo y dicen,"Uy, esto está buenísimo, pero necesito validar." Se claro,

**Pablo Barbarelli**: Estará bien. Bien tam elh

**Gabriel Puertas**: se dan vuelta y te dicen,"Che, Pablo, Fíjate esto, fíjate si está bien ahí en ese caso. Yo prefiero que lo tenga Pablo, no el CO. Con tal vos sabes que el flaco te manda una pregunta y y vos se la vas a hac al toque, ¿entendés? Eh,

**Pablo Barbarelli**: Hol

**Gabriel Puertas**: pero nada, es es la dinámica. Esto está para que lo use cualquiera. No requeréis ser técnico, ¿no? Ni nada por el estilo, ¿eh? qué sé yo. Y lo que yo les mostraba de de del knowledge este, yo creo que eso es eso es s super útil en el ejemplo que vos diste del CEO, porque vos acá en cierta forma podés editar eh esos esas cosas que solamente se saben en Ayudín. No sé, acá no sé,

**Pablo Barbarelli**: Sí, sí,

**Gabriel Puertas**: distribuimos el costo de marketing de esta forma.

**Pablo Barbarelli**: el contexto. contexto para Claro.

**Gabriel Puertas**: Claro, esto técnicamente está hecho para que lo edite Cloud. O sea, vos fíjate que nosotros acá el flaco dijo, acá encontró algo. Mira, dice,"Hay filas sin asignar que suman 300000 para atrás. Eh, son la tabla mantiene un arma, que s yo le voy a decir, mira, guarda todo lo que prendimos en el iconos. Ahí lo que va a hacer es guardar. Y yo hay algo que todavía no les mostré que es s superútil cuando esto termine, que es la posibilidad de que vos te puedes armar un dao.

**Gabriel Puertas**: O sea, vos le decías a Cloud,"Okay, me gustó, me gustó esa tabla que armamos, está buena, la entendí, qué sé yo, es la que quiero." Y y ahora le decís,"Bueno, okay, vamos a armar un dasor que tenga tal o cual set de información." Eso va a funcionar muy parecido a los artifact que arma Cloud,

**Pablo Barbarelli**: Te tiene ser un artefacto si no se no se vuelve a Sí,

**Gabriel Puertas**: solo que en realidad es código HTML,

**Pablo Barbarelli**: sí, sí, sí.

**Gabriel Puertas**: pero el detalle es que vos ese código HTML lo podés publicar en Teramod. ¿Por qué publicarlo en Theramot? Porque así vos lo tenés conectado con la fuente de datos. Entonces ese dasor ahora cada vez que voy a actualizar los datos se va a actualizar y a esos dat lo podés compartir con gente que por ahí no tiene permiso de edición.

**Pablo Barbarelli**: Mucho.

**Gabriel Puertas**: O sea, es simplemente el que te consume el dashor nada más. ¿Me explico? Entonces yo poner le digo,"Okay, okay, vamos aar y publicar." Ahora, mientras se pone creativo armando el dashboard, yo les muestro, eh. Ah, y acá habíamos cambiado de us.

**Gabriel Puertas**: Vamos a ayudos. Era este. Acá me cargó el conocimiento de lo que nosotros aprendimos. Nada, acá puede haber detalles que que vos digas,"Che, no, mira lo que pasa siempre en SAP, no sé, en una tabla Los ID están como numéricos, en el otro empiezan con 00. Entonces dice, bueno, o lo o lo normalizado o cada vez que vas yoñar esta tabla con esta otra, te tenes que acordar de esto, cosas por el estilo. Eh, eso puede ser lo más específico que que haga falta, pero bueno, eso si ya te queda. Eh, mientras tanto, vamos a ver qué está haciendo Cloud a todo esto. Bueno, ahí me armó un preview de este dashor. Cuando lo termine le decimos nada, publicar lo enteramos y ahí te va a quedar te va a quedar conectado. Y te armó el caminito.

**Christian Schiavo**: Oh.

**Gabriel Puertas**: Decime si lo publico. Tal cual. publicar al digamos la mayor utilidad que nosotros le vemos a esto eh tiene que ver con bajar un poco el backlock de del área de datos porque vos siempre en mi opinión siempre las distintas áreas tienen algo alguien que se da un poco más de maña con con la info y arma los reporteres y vos le podés entregar esto.

**Pablo Barbarelli**: es un entregable más de service que en lugar de que se creen sus propios reportes, eh,

**Gabriel Puertas**: Claro.

**Pablo Barbarelli**: es una forma de ser el service preguntando y respondiendo o o haciendo reportes como lo vamos ahora o pero 100% decí es no ser cuello botella del área de alta.

**Gabriel Puertas**: Claro. Y lo que yo veo es que hay algunas áreas que que tienen, digamos, a ¿Dónde era esto? Acá dater era este, ¿no? Era este. No con acá. ¿Vos qué podés hacer con esto? Si hay alguien que lo vos podés pensar en ciertas automatizaciones con esto. ¿Qué quiere decir eso? Eh, suponte que vos tenés eh un área que maneja, no sé, stocks o stock de clientes o cosas por el estilo. Vos podrías armar una tabla que monitoree esos stocks, ¿entendés? Como vos ya te estás actualizando todos los días, decís,"Bueno, yo tengo yo tengo las ventas, tengo el stock inicial, ¿cómo va bajando? Defino unos estoques de seguridad." Bueno, eso en definitiva va a terminar haciendo una tabla. ¿Vos qué podés hacer con eso? Si alguien de esa área se se maneja un poco más, esa tabla que vive en Teramod, que se actualiza todos los días, vos la podés consumir con distintas otras fuentes de información, o sea, la podés consumir vía API,

**Gabriel Puertas**: la podés consumir, no sé, conectarla en Power BI y podes hacer lo que quieras. Vos podrías utilizar una herramienta tipo N8N que automatiza flujo y decir,"Bueno, yo le pongo un a esa tabla le pongo un API y cada Right. que uno de los valores va bajando el stock, automatiza un correo haciendo un pedido, una alerta o no sé lo que sea. Eh, tenemos casos que hacen como esto, un brief, los comerciales mandan por WhatsApp un valor y de repente tienen un brief de de ese cliente que van a visitar en ese momento, le cuenta toda la historia como se la quiere contar el área comercial. Ahí lo que yo te digo, eso es eso es muy automatizable y la verdad que agrega muchísimo valor. O sea, ¿por qué te comento esto? Porque la digamos el primer paso la reportería, que es lo que vimos acá. No sé si se habrá publicado ya el o no. Este me debe estar preguntando. Sí. Eh, bueno, ahí me está guardando el dashor. El primer paso la reportería que que vos le decís, bueno, te armaste un das esto es tan rápido para hacer los das para contestar esas preguntas que para mí lo interesante es el paso que sigue. ¿Cómo va a seguir una vez que ya respondiste la pregunta?

**Gabriel Puertas**: ¿Cómo sigue que te está quedando sin esto? ¿Que estás haciendo yo? Y eso es superútil, digamos, no sé.

**Pablo Barbarelli**: Sí, sí, obviamente.

**Gabriel Puertas**: Mientras va terminando, ¿tienen alguna duda de tipo sistema, seguridad, lo que sea?

**Christian Schiavo**: No, al principio yo quería que hacer el ejercicio, ¿viste? Como te decía, ir de menos a más, porque me me tengo que ir imaginando cómo la persona va a hacer usabilidad de esto.

**Pablo Barbarelli**: Mhm.

**Christian Schiavo**: No me imagino a priori hacer tableros es un nivel avanzado porque vos tendrías que validar que lo que está haciendo está bien y todo eso. Me imagino, no sé, no no me imagino que un táctico se ponga a hacer tableros hoy. Posiblemente sí. Después tendría que hacer los cachap, digamos, con eh el el costo de hacer el tablero, ¿no? Sí veo a el que no discuto y arriba de la mesa, por lo menos yo, es el de hacerle preguntas que no son que salen de la tabla que ya está preparada para hacerlo bien fácil y después eh que encuentre inside, ¿no? Porque acá la palabra es inside, ¿no?

**Gabriel Puertas**: Sí.

**Christian Schiavo**: cosas que digamos puedo hacer o el equipo puede hacer o la persona ya lo pensó y el Insight sale de correlaciones, como te decía, de decirle,"Che, mira, yo quiero el cross margin." El cross margin de cuál y no sé,

**Christian Schiavo**: mira, en este mes quién quién tuvo mejor cross margin rápidamente, ¿no? Porque quiero evitar acá lo que se trata es de aproximar el dato o la información al usuario. Oye, el usuario por ahí la tiene, pero tiene que abrir el reporte y hacerlo. Distinto sería y algo que es pagable es decirle,"Che, decime quién es el que está vendiendo menos." Así.

**Gabriel Puertas**: Sí.

**Christian Schiavo**: Uy. Bueno, listo, che. Y y ¿qué queres? get sales. Okay. Gross profit, ¿no? ¿Quién está vendiendo menos en volumen y quién está vendiendo barato, porque vender mucho es fácil, vender con buena con buen profit es saludable, digamos, para la compañía. Entonces, se tendría que dar cuenta a través de ese plano, por ejemplo, que yo te pasé, cuál de las gerencias, por eso ya el ejercicio, si querés, te lo mando acá y ya te doy los números. es eh quiero saber eh por gerencia, ¿sí? Eh, el gross margin, gross margin porcentual y se lo voy a poner un poquito difícil. ¿Para qué? Para decirle gross margin es net sale dividido gross profit. Eso es una definición de negocio.

**Christian Schiavo**: Vamos a ponerle una definición de negocio para que sepa que gross margin es es gross profit,

**Gabriel Puertas**: Net se dividido No.

**Christian Schiavo**: perdón, al revés, gross profit dividido net sales. net sales, eso te da te da lo que lo que te lo que le contribuye cada producto por por punto de venta y en este momento canal, digamos, a la compañía en el mes de julio. Esa es una pregunta más que viste, trivial para el CEO. Ahí te lo dejo acá también y te voy a dejar los números cuánto dan. Creo que esto tiene a una un chat. Ahí está, mira. Te voy a pasar el la captura de lo que daría eso. A ver si me deja pegar.

**Gabriel Puertas**: En ese sentido, lo que es eh análisis de resultado y propuesta de valor, qué sé yo, a mi criterio es donde Cloud la rompe totalmente. digamos,

**Christian Schiavo**: Ahí está.

**Gabriel Puertas**: porque ahí al que al que termina haciendo los análisis nos ha pasado de, no sé, tipo acá hay nosotros rosarios, acá hay una una serie,

**Christian Schiavo**: Perfecto.

**Gabriel Puertas**: acá hay una serialera que le tiró el CEO, le dijo,"Ah, bueno, todo muy lindo, quiero ganar plata, quiero ganar más plata el mes que viene, el semestre que viene quiero ganar más plata." Y bueno,

**Christian Schiavo**: Eso es eso.

**Gabriel Puertas**: por eso y entonces lo que empezó a hacer es empezó a hacer un análisis de las ventas, calculó el lifetime value de los clientes, se dio cuenta que el lifetime value explotaba cuando compraban no sé qué combinación de de

**Christian Schiavo**: Claro,

**Gabriel Puertas**: producto.

**Christian Schiavo**: es eso,

**Gabriel Puertas**: para ese tipo de preguntas, esto vuela y yo.

**Christian Schiavo**: eso. Sí. Los números son esos. Mira, ahí está. Perfecto. A ver. Eres interior, eres un 30 y un 33 en interior. Perfecto. Un supermercado lo tenés en 31. Está perfecto. Mayor. Bueno, esa es la 30. Perfecto. Listo. Esto es la primer pregunta que se haría. Che, ¿cómo andan las gerencias? Lo llama al flaco al gerente.

**Gabriel Puertas**: Ev.

**Christian Schiavo**: Al gerente de mayorista le dice,"Che, 30,

**Pablo Barbarelli**: M.

**Christian Schiavo**: no sé. Yeah. 30 puntos está regalado, tu objetivo es 40, lo hablamos el otro día. Decime. Bueno, bájame a ver, diría, ¿no?

**Christian Schiavo**: Por otra cosa. Decime cuáles son las cómo estás trabajando las categorías en ese en ese mayorista y ahí podr hacerme lo el gross profit, o sea,

**Gabriel Puertas**: A ver,

**Christian Schiavo**: el gross march de las categorías dentro de mayorista.

**Gabriel Puertas**: pero dejalo. Vamos a ver los insight que nos tiró. Eh, uno, el ranking real es apretado y las cifras llamativas son ruido contable. Entre las tres gerencias que mueven el negocio, INT 87% solo tres puntos.

**Christian Schiavo**: Exacto, exacto.

**Gabriel Puertas**: Las hijas de extremo no son performance, son sin gerencia, export y otros.

**Christian Schiavo**: Claro.

**Gabriel Puertas**: Eh, implicaciones para la pobre, lo que separa la gerencia, el mix de marca, no la eficiencia. El GM porcentual de cada gerencia está casi enteramente explicado por por qué marcas vende, porque los márgenes por marcas son muy distintos. Marca Selton 58%in 315.

**Christian Schiavo**: Exacto.

**Gabriel Puertas**: Eh, vamos a ver el Inside 3. La misma marca rinde distinto distinto según la gerencia. ¡Upa! Este este es más más complejo, digamos.

**Pablo Barbarelli**: M botón

**Gabriel Puertas**: Este, claro, esto es lo más accionable.

**Christian Schiavo**: Claro.

**Gabriel Puertas**: Mirando a Judí, misma marca, distinto margen por gerencia. Ajudin en SPM 31% en mayorista 26.9 cu 4 puntos con diferencia del mismo producto POET igual que la misma marca tenga cuatro

**Christian Schiavo**: Alô.

**Gabriel Puertas**: puntos menos de margen mayorista que en supermercado apunta estructura de precio y descuento por canal. Resumen ejecutivo, el margen bruto de negocio está sano y homogéneo entre gerencias. La palanca de margen no es reducir costo de una gerencia, sino el mix, elevar el peso de Celton y Mortimer y entender por qué Audin pierde cuatro puntos de mayorista. Uh, rebotón. Bueno,

**Christian Schiavo**: Claro.

**Gabriel Puertas**: no, no, eso para ese claro,

**Christian Schiavo**: Y este es para empezar. Es para empezar, ¿entendés? Porque yo ya sabía esta tabla.

**Gabriel Puertas**: porque

**Pablo Barbarelli**: Sí, la mayoría de las cosas estos puntos ya ya hasta la deben saber,

**Christian Schiavo**: Así, así. Claro.

**Pablo Barbarelli**: pero pero bueno digo y así se puede

**Christian Schiavo**: Sal.

**Gabriel Puertas**: sí,

**Pablo Barbarelli**: Sí.

**Gabriel Puertas**: pero lo que yo digo es cuando vos le aportas mayor cantidad de información y le hacés estas preguntas de bien orientadas, pero a nivel general, Cloud tiene mucha capacidad para ir buscar y filtrar y decir,"Ah, eso Yo no lo había pensado, ¿entendés?

**Gabriel Puertas**: Y y qué sé yo.

**Christian Schiavo**: Mhm.

**Gabriel Puertas**: Esta que te digo, el CO que nos pidió ganar más plata, que le calculó el stand value, nosotros tuvos que explicar el tipo que era el tram value,

**Christian Schiavo**: Obvio.

**Gabriel Puertas**: ¿entendés? Pero el tipo se lo calculó y le dijo,"Esto tenés que tenés que apuntar a que tales comerciales vendan estos productos porque no lo están vendiendo y si lo venden dos los clientes se quedan y eso te estimo y te va a ganar tanto." Digamos,

**Christian Schiavo**: Mm.

**Gabriel Puertas**: una locura el tipo. Yo creo que lo interesante, no sé cómo quieren seguir, pero lo interesante sería que lo prueben funcionalmente más.

**Christian Schiavo**: Sí, sí, sí. Yeah. Ahora, una última. Esta esta es la básica para mí.

**Gabriel Puertas**: Dale, dale, dale, dale. Vamos con la última.

**Christian Schiavo**: La última es correlacióname el trade spending.

**Gabriel Puertas**: Va, pueden ser otra.

**Christian Schiavo**: Vas a encontrar que una cosa y ya te digo cómo se llama porque

**Gabriel Puertas**: Decime exactamente lo que le queres preguntar.

**Christian Schiavo**: Sí, sí, quiero saber cómo cómo influye el trade de spending para que vos te des una idea.

**Christian Schiavo**: Es cuánta plata vos le ponés a la categoría en un canal, en un punto de en una cadena. Sí.

**Gabriel Puertas**: Creo que

**Christian Schiavo**: ¿Cuánta plata vos le pones promocionalmente en exhibición y todo eso? ¿Y cómo se relaciona eso con el net sale?

**Gabriel Puertas**: está bien. Quiero saber cóo.

**Christian Schiavo**: Y necesito hacer una evaluación de eso en todo julio para todas las cadenas, todos los canales,

**Gabriel Puertas**: Claro.

**Christian Schiavo**: porque quiero saber, che, vos, porque vos ya me dijiste algo antes, me dijiste,"Che, este flaco está cuatro puntos abajo en mayorista, che, pero está gastando mucha maguita en supermercado y solamente vende cuatro puntos. y me se me está yendo la rentabilidad por el trade spending, para que te una idea, es una variable que te pega mucho los costos, eh,

**Gabriel Puertas**: marketing sería marketing.

**Christian Schiavo**: exacto. Es el marketing,

**Pablo Barbarelli**: El C la porta.

**Christian Schiavo**: el gasto en marketing que vos le pones va directo al al estado de resultado, pero la correlación no la tenemos. Yo yo no lo hago, o sea, digo, yo podría ponerlo en un reporte la correlación y pero digo, ahí está el chiste de esto. Digo, tendría que esto como correlación se me es una de las de las variables que se me ocurre.

**Christian Schiavo**: Después hay un montón. El otro día nos pusimos a jugar con la canibalización y sacamos cosas superinesantes,

**Gabriel Puertas**: Claro.

**Christian Schiavo**: pero capaz que esto si le tiro los números ya directamente me saca la canibalización de un pack con respecto a un producto de línea de toque.

**Gabriel Puertas**: Sí. Y y lo mejor de todo que no necesitan, para mí es una nueva forma de trabajar, porque vos decís, ¿quién es el responsable de la canibalización? Me imagino que por eso quiere decir, estoy vendiendo más poet y por eso vendo menos ayudín, me imagino.

**Christian Schiavo**: Sí.

**Gabriel Puertas**: Pero digo,

**Christian Schiavo**: ponerle que saqué un pack donde tenía tenía una lavandina y va con otro producto versus la

**Gabriel Puertas**: claro, ahí va.

**Christian Schiavo**: lavandina sola que va solita. Lanzo el pack y dejo de vender la bandina y vendí el pack. Si el pack me hizo reventar lavandina o o se comió la lavandina que ya venía

**Gabriel Puertas**: Claro,

**Christian Schiavo**: vendiendo.

**Gabriel Puertas**: tal cual. Pero bueno, lo interesante que ese análisis ya directamente lo puede hacer el responsable de eso, el comercial, ¿entendés? Entonces, eh es como decir, loco, ¿no te diste cuenta que estaba canibalizando

**Christian Schiavo**: Y bueno, sí, acá hay un punto que el que va a comprar primero esto, esto va de arriba para abajo, no sé si coincide para acá,

**Gabriel Puertas**: Sí.

**Christian Schiavo**: o sea, el primero que el pibe que hizo la suite es el CEO y es crack con esto, entiende todo. Entonces, él le va a hacer las primeras preguntas y lo va a domesticar muy bien y después va a hacer más preguntas que que si nosotros no le ponemos la fuente no se las va a explicar, pero vamos a a sacarle la Claro,

**Pablo Barbarelli**: emp cruzar información. Claro.

**Christian Schiavo**: claro. Y nosotros si le ponemos todo el datawarecout, él va a poder ver el M por N y los otros también van a poder ver el M por N. Y ahí creo que es donde está lo rico de de esto que está mostrando.

**Gabriel Puertas**: Bueno, este me dice,

**Christian Schiavo**: Este es un service avanzadísimo por lo que estoy viendo.

**Pablo Barbarelli**: A ver qué dice esto.

**Gabriel Puertas**: a ver, Eh, yo tengo un canal. El nivel más fino de cliente cargado es su canal. La palabra cadena de negocio se mapea acá a su canal. Hipermercado supermercado y canal.

**Christian Schiavo**: Exact.

**Gabriel Puertas**: Con eso el análisis queda completo. Antes que nada, el proyecto tiene un único mes cargado, julio, así que todo lo de abajo ya es julio y una nota de lectura.

**Gabriel Puertas**: El trading es una traducción deducción que ocurre entre gross sales y net sales, o sea, ya está descontado entre dentro del net sales.

**Pablo Barbarelli**: Hello

**Gabriel Puertas**: Por eso el rate muesto es ts sobre gross sales. Está bieno.

**Christian Schiavo**: Esa es verdad. Sí.

**Gabriel Puertas**: Ahí vamos. Eh, muestro ambos canal. Bueno, este es lo ambos dos por su canal.

**Christian Schiavo**: Ajá. Claro, vos fíjate que el tipo en e-commerce no usa nada de tres spending. Sí. Y es donde la relación le da en realidad da negativa porque el tr pending resta, digamos.

**Gabriel Puertas**: Claro.

**Christian Schiavo**: Sí, pero la relación te da bueno ahí 50 30 ta ta ta ta, 35 en hipermercado.

**Gabriel Puertas**: Y ahí me tiró algunos.

**Christian Schiavo**: En hipermercado, bueno, en hipermercado es donde más más usa que solo el 56. Bueno, nada, igual es ofuscado, ¿no? Los números, o sea,

**Gabriel Puertas**: Sí, sí,

**Christian Schiavo**: que puede estar dando cualquier pelotudez,

**Gabriel Puertas**: no importa.

**Christian Schiavo**: pero digo, la relación es eso y está bien lo que está diciendo. Así, o sea, modern trailer.

**Pablo Barbarelli**: Conceptualmente está insight es el gran consumidor de trade, claramente concentra

**Christian Schiavo**: Mm.

**Pablo Barbarelli**: el epicentro 60% del trile.

**Christian Schiavo**: Claro.

**Pablo Barbarelli**: TR

**Gabriel Puertas**: me tiene una propuesta que este le gusta le gusta Consum Tokens. dice,

**Christian Schiavo**: Claro.

**Gabriel Puertas**: "¿Cre que abre el hipermercado por marca SKU para ver dónde está yendo ese o que compare trade spending contra gross margin para ver qué canales todavía dejan contribución

**Christian Schiavo**: Exacto.

**Gabriel Puertas**: positiva y ahí es seguís

**Christian Schiavo**: Viajas.

**Gabriel Puertas**: digamos ahí el CEO te va a p*****

**Christian Schiavo**: Lógico. Sí, sí, sí, sí, sí. Bueno, y no sin toques.

**Gabriel Puertas**: cuando se quede sin sin consumo

**Christian Schiavo**: Por eso ahora el segundo drill de esto es la balanza de estar preguntando

**Pablo Barbarelli**: Yeah.

**Christian Schiavo**: y cómo vos tenés ya alguna mensura de todo esto, decir,"Che,

**Gabriel Puertas**: No.

**Christian Schiavo**: mira este este ejemplo que hicimos, puedo mensurar Да. en una cantidad de tokens, por lo menos así, porque así ya tenemos un

**Gabriel Puertas**: No, mira, nosotros justo con con Agustín venimos hablando mucho eso. Nosotros para nosotros la mejor forma de consumir esto es que vos tengas tus propios seats de cloud, GPT o el que sea, pueden tener un acuerdo con quien sea y nosotros te conectas ahí y usas esos modelos.

**Christian Schiavo**: Sí,

**Gabriel Puertas**: ¿Por qué?

**Christian Schiavo**: sí.

**Gabriel Puertas**: Porque vos acotá muy bien el el el gasto, o sea, yo esta es mi cuenta personal. Creo que yo yo pago la de $ y nada,

**Christian Schiavo**: Obvio.

**Gabriel Puertas**: si me paso en un momento me sale un cartel, me dice,"Vas a tener que esperar 2 horas porque te clites diarios,

**Christian Schiavo**: Claro. Sí, sí, sí.

**Gabriel Puertas**: análisis mensual." Claro.

**Christian Schiavo**: Que pt igual. Sí.

**Gabriel Puertas**: Entonces vos decís,"Bueno, si tengo un power user, le pongo la de 100 o lo pongo en una premium seat que me empieza a consumir crédito, pero no a todo el mundo. Entonces yo acoté muy bien quién y cómo gasto." Y además y además es la mejor

**Christian Schiavo**: Ah, está bien, está

**Gabriel Puertas**: forma porque ese token de por la aplicación es varios

**Pablo Barbarelli**: está subvencionado,

**Gabriel Puertas**: órdenes de magnitud que si vos me decís,"Che, te doy la AP Key y subimos así.

**Pablo Barbarelli**: no te come, te come, te come vivo, ¿no? Por eso digo,

**Gabriel Puertas**: Es lo que digo.

**Pablo Barbarelli**: hoy hoy tenemos estamos sacando algunas licencias de Teams de Cloud, como para empezar a compartir con algunos usuarios.

**Pablo Barbarelli**: Eh, entonces entiendo que esto no es vía API, no es vía token, que es lo que el mundo le teme cuando de repente te llega una factura por

**Christian Schiavo**: Ok.

**Pablo Barbarelli**: hacer alguna prueba que no no tenías no tenías en cuenta. El límite es el propio límite de cada usuario de cabuseo

**Gabriel Puertas**: Si ahí Pablo es nosotros estamos

**Pablo Barbarelli**: pro.

**Gabriel Puertas**: preparados para que funcione como ustedes prefieran que funcione. O sea, si ustedes tienen una, no sé, un acuerdo con Antropic que tiene, no sé, con el Mercado Pago tiene tiene una cosa así,

**Pablo Barbarelli**: Sí. Bueno,

**Gabriel Puertas**: entonces yo tengo yo tengo tokens.

**Pablo Barbarelli**: pues

**Gabriel Puertas**: Claro. Entonces, bueno, nada, nosotros podemos hacer que esto funcione con tu AP Gey.

**Christian Schiavo**: Hm.

**Gabriel Puertas**: Vos podés controlar quién quién consume, cuánto consumió,

**Pablo Barbarelli**: bueno,

**Gabriel Puertas**: son habilitados.

**Pablo Barbarelli**: pero la otra vez estuve en la charla con Merolivre y gastan 15 trillones de token por mes.

**Gabriel Puertas**: Claro. Bueno, sí, sí, sí, sí.

**Pablo Barbarelli**: ese número,

**Gabriel Puertas**: Es más,

**Pablo Barbarelli**: pero no no es nuestro caso ni va a ser

**Gabriel Puertas**: es más, controlan quién quién usa y quién no usa.

**Gabriel Puertas**: Es terrible.

**Pablo Barbarelli**: Sígual

**Gabriel Puertas**: Tan tan tan desquiciado. Igual para mí va por buen camino.

**Christian Schiavo**: Está bien. Es por ahí. Va por ahí. Por ahí.

**Gabriel Puertas**: Va por ahí. Eh,

**Christian Schiavo**: Eh,

**Gabriel Puertas**: hoy hoy, bueno, se nos va medio tarde, pero no importa. el

**Christian Schiavo**: dale.

**Pablo Barbarelli**: nosotros estamos medio.

**Christian Schiavo**: Estamos bien, estamos bien.

**Pablo Barbarelli**: Sí, nosotros con este tema podemos estar todo el día, así que quede tranquilo que

**Gabriel Puertas**: No, pero le digo que yo creo que a futuro, esto es más polémico hoy viene con eso, no es creatividad mía, lo escuché en un podcast, creo que a futuro el que va a pagar los tokens van a ser los empleados y este ahí tiré más problemas.

**Pablo Barbarelli**: ya Puść

**Gabriel Puertas**: Voy a decir, bueno, voy a decir yo te doy,

**Christian Schiavo**: Puede ser,

**Gabriel Puertas**: vamos al ejemplo, no, yo te doy teramón,

**Christian Schiavo**: puede ser.

**Gabriel Puertas**: yo te dejo que vos uses o ch o cloud, no me van con modelo chino. Yo eso que pero te lo ten que pagar vos. Y si y bueno, si vos estás en la fácil de decir,"No, yo ni pedo, no uso eso,

**Pablo Barbarelli**: Pero paraá,

**Gabriel Puertas**: no pagará,

**Pablo Barbarelli**: de hecho,

**Gabriel Puertas**: pero otro que lo va a pagar y va a crecer más que vos porque va a ser más inteligente.

**Pablo Barbarelli**: los primeros meses de este año o fin de fin de año pasado hasta hace poco, todo lo que hice con el laburo lo hice con mi club pagado por mí y lo pagaba y lo

**Gabriel Puertas**: Olvidaste,

**Christian Schiavo**: Totalmente.

**Gabriel Puertas**: olvidas,

**Pablo Barbarelli**: pagaba con ganas porque me resolvía y me aceleraba todo. Entonces, digo, no, no. Sí,

**Gabriel Puertas**: olvidaste el de esto cuesta menos que Netflix." Entonces digo,

**Pablo Barbarelli**: sí.

**Gabriel Puertas**: yo en mi anterior vida, ahora obvio que usamos esto, nosotros el 98% del código que que entra enteramos está está hecho por por agentes, pero digo el mi anterior vida, yo sin duda si hubiese tenido esto pagaba pero pagaba el premium se pagaba $00.

**Christian Schiavo**: Oh.

**Gabriel Puertas**: Asumo laurame.

**Pablo Barbarelli**: 100% 100% che y yendo al

**Christian Schiavo**: Ok.

**Pablo Barbarelli**: eh al al caso de uso o para tratar, como decía Cris también para tratar de mencionar. Está claro entonces que dentro de una suscripción de 20 horas de de dentro de Teams del Teams Club que podemos ya tener, eh el equipo directivo, que es un poco lo que queremos empezar a pensar, ¿no?

**Pablo Barbarelli**: Digo, un servicio para equipo directivo, que se responde a las preguntas con todo lo que Cris viene abugurando en el último año haciendo eh con toda la lógica de que le estamos poniendo a nuestra capa analítica de de dentro de grupo Yi, ¿no? Entonces, ¿cómo sería? O sea, hoy sería la conexión con a través de Cloud con conectándose vía MSP a a Teramod y ahí empezar a hacer las eh las todas las personas que que tengan acceso van a tener que tener también, entiendo yo, un usuario de Teramot o acceso de Teramot, en donde si yo somos 10 usuarios, tenemos Teramot y voy publicando artefactos, entiendo yo que lo debería poder compartir aquello que generé con valor y no quiero estar haciéndolo todo el tiempo Ya lo tengo publicado dentro de la espacio de Teramo y lo puedo compartir entre el director de finanzas con con la de comercial y la de venta y marketing y listo y a lo mejor ahí no ya ya no tengo que estar rearmándolo todo el tiempo o mismo ir consumiéndolo o actualizándose cada vez que quiero, ¿no? E corríjame si estoy siguiendo en lo correcto.

**Christian Schiavo**: Está perfecto.

**Pablo Barbarelli**: Eh,

**Agustin Garcia**: estás en lo correcto. La idea es vos eh digamos en un setup eh con el equipo de customer van a definir un poco la estrategia de la estructura organizacional para que digamos porque después qué te va a pasar,

**Gabriel Puertas**: He.

**Agustin Garcia**: cada grupo de usuario puede tener acceso a un nivel de información distinto. Tal vez las cabezas no, pero los equipos operativos sí. Entonces eh digamos tal vez comercial no tiene por qué ver costo y viceversa o cualquiera sea la situación. Entonces ahí se arma la estructura de usuarios.

**Christian Schiavo**: Mhm.

**Agustin Garcia**: Y en función de esa estructura de usuarios que para mantener la jerarquía de permisos, después eh cada usuario puede publicar los dashboard que hagan. Esos dashboard se van actualizando, automáticamente se actualizan las fuentes de datos y eso se comparte entre grupos de usuarios. Entonces, digamos, vos vas a tener esos usuarios member que tienen la capacidad de conectarse con el MCP, hacer todo esto que vimos, publicar dashboard, modificarlos y pa pa pa pa. Y después también tenés un esquema de usuarios viewer, por así decirlo, que son los que solo entran a ver la información del dashboard sin posibilidad de modificarlo, ¿se entiende?

**Christian Schiavo**: Mhm.

**Agustin Garcia**: Entonces, esos son los dos esquemas usuales.

**Gabriel Puertas**: Ok.

**Agustin Garcia**: Entonces, suponete que vos tenés 10 usuarios internos que necesitas que tengan MCP. Fantástico. Bueno, vas a necesitar 10 usuarios member de Teramot. Ahora, tal vez esos 10 usuarios son líderes y tienen, suponete que 10 usuarios más en cada equipo, entonces vas a necesitar 10 licencias viewer.

**Agustin Garcia**: Fantástico. Listo. Entonces, vas a tener un usuario por cada área eh member que tenga la conexión en CP. Después vas a tener 10 usuarios adicionales más que sean usuarios viewer que puedan ver y

**Christian Schiavo**: Ha.

**Agustin Garcia**: no solo ver eh digamos la información, sino también conversar con la información. Ahora,

**Pablo Barbarelli**: Ah,

**Agustin Garcia**: solo van a Sí,

**Pablo Barbarelli**: eso el viewer puede conversar.

**Agustin Garcia**: solo van a poder conversar con los datos que tienen disponible. Sí, por eso la estructura jerárquica de usuarios, ¿entendés?

**Pablo Barbarelli**: Pero conversa a través de Teramot.

**Agustin Garcia**: con el agente con el agente que está embido teramot, que digamos es un agente de bajo poder que tiene un alcance

**Gabriel Puertas**: No. O o perdón o si vos creés que ese usuario viewer

**Agustin Garcia**: determinado.

**Gabriel Puertas**: tiene un seat de de cloud, lo consume vía cloud, o sea, no pasa nada.

**Pablo Barbarelli**: No entendí, sorry.

**Agustin Garcia**: No, no, pero claro, no, el usuario viewer no está pensado para que tenga conexión MCP,

**Gabriel Puertas**: Ah, está.

**Agustin Garcia**: está pensado para que sea read only.

**Gabriel Puertas**: Perdón,

**Pablo Barbarelli**: Ah,

**Gabriel Puertas**: perdón.

**Pablo Barbarelli**: eso es claro, claro.

**Pablo Barbarelli**: Okay,

**Agustin Garcia**: Entonces,

**Pablo Barbarelli**: claro.

**Agustin Garcia**: solo consulta los datos porque es muy común que digamos que vos tengas usuarios que pueden generar, modificar y y tengas usuarios que solo lectura. Eh, entonces esa es la idea.

**Pablo Barbarelli**: Consulta todo ese conocimiento que fuimos armando y escribiendo cuando Gabi le decía desde

**Agustin Garcia**: Sí.

**Pablo Barbarelli**: Cloud que,"Che, esto grabo, que me interesa que ya ya te lo aprendas.

**Christian Schiavo**: Eso.

**Pablo Barbarelli**: El viewer eh cuando lo consulta, cuando puede hacer esas consultas, consume también de ese conocimiento o es

**Gabriel Puertas**: Sí, lo voy a tener en cuenta. Sí, sí, sí, sí.

**Christian Schiavo**: Okay. Bueno,

**Gabriel Puertas**: Lo va a tener en cuenta para responder. Sí.

**Pablo Barbarelli**: como que como que podés ir eh no no está bien,

**Gabriel Puertas**: No lo va a poder editar.

**Pablo Barbarelli**: pero digo como que los usuarios member irían a madurando al modelo constantemente y todos los viewers podrían aprovechar ese es ese crecimiento.

**Christian Schiavo**: sería un user, sería el el digamos el ese la cabeza del equipo que puede trabajar

**Gabriel Puertas**: Ah.

**Christian Schiavo**: tipo member y todo lo demás. Yeah.

**Agustin Garcia**: Mira. Mira, lo que nos pasa en otros clientes es, digamos, generalmente ese usuario member, es un gerente, un director que mete mucho mano, un líder o un analista que arma,

**Gabriel Puertas**: un líder o un analista.

**Agustin Garcia**: viste, digamos, los reportes y todo eso y el resto viewer, porque inclusive también hasta depende dónde, ¿no?

**Pablo Barbarelli**: Ok.

**Agustin Garcia**: Pero también tenés directores que no no están para meter ese tipo de mano porque aparte pueden hacer cagadas.

**Christian Schiavo**: Claro,

**Agustin Garcia**: Entonces le das un usuario viewer que conversa con los datos y digamos que con eso safas.

**Christian Schiavo**: obvio. le sirve.

**Agustin Garcia**: Ahora capaz que tenés de los dos tipos. Bueno, a uno le das usuario viewer y al otro le das usuario member y con eso lo resolvés y vas viendo también un poco cómo va madurando cada equipo, cada persona con la implementación de este tipo de tecnología.

**Christian Schiavo**: Yo tengo una preguntita ahí, Pablo.

**Pablo Barbarelli**: Sí,

**Christian Schiavo**: Eh,

**Pablo Barbarelli**: sí, sí.

**Christian Schiavo**: ¿qué tenemos? O sea, el tema de seguridad me quedó claro. Además, me quedó en la memoria el concepto de workspace que vos me dijiste, Agustín, el otro día, que es parecido a lo de los espacios que nosotros tenemos hoy día en Datafier.

**Agustin Garcia**: Correcto.

**Christian Schiavo**: Para que vos teas una idea, vamos a pensar que tenemos unas 15 tablas que vamos a replicar, digamos, ¿no?

**Agustin Garcia**: Hm.

**Christian Schiavo**: Por la lógica que tienen esas tablas, como para que después nosotros teníamos un proyecto antes de hablar de todo esto, ¿no? Pero sí que eran una conjunción de esas tablas como para que explique un overall de la compañía, decir,

**Agustin Garcia**: Claro.

**Christian Schiavo**: estos son costos de fabricación, estas son tus este tus ventas, esto es cómo vos trabajas la gente, cómo está tu headccount, cómo está tus costos, eh cuánto se te encareció, digamos, los costos de materiales. un overall,

**Agustin Garcia**: Los principales scorcar y tableros de la compañía.

**Christian Schiavo**: eso logística, todo eso. Claro.

**Pablo Barbarelli**: Sal.

**Christian Schiavo**: Y lo íbamos a agrupar en en un room que decíamos, nuestra idea es que el director y y toda la gente que lo rodea pueda ver el todo y discutir, sí, con una pericida X eh todos los números. Bueno, digo, me lle me voy a esto y digo, bueno, macanudo, tengo que llevar toda esa información a otro lugar, ¿no? Y ese otro lugar no me no recuerdo si era una WS, era porque ahí tengo un tema de realocación de datos como otro gasto. Además, estoy pensando en todas las partidas, ¿no?

**Agustin Garcia**: Sí.

**Christian Schiavo**: Una partida es realocar una cantidad de gigas en otro en otro lugar que me dirán ustedes dónde dónde va.

**Agustin Garcia**: Sí.

**Christian Schiavo**: que yo también estaba re y él y Pablo también orientados a que tenemos que hacer un nuevo entre comillas warehus, pero que no es con la con la lógica de dataho que ya tenemos que la tenemos muy bien armada porque esa es la fuente de la verdad de la compañía, ¿no?

**Agustin Garcia**: Sí.

**Christian Schiavo**: y tiene datos de afuera, tiene tiene lógica de negocio muy entrincada que si me voy a SAP no la encuentro porque tiene, o sea, le hacen la cuarta derivada acá para, imagínate que quisimos poner contenedores estándar de SAP que traen working capital y obviamente no no aplicaban porque era distinta la definición de la compañía. Entonces digo, ¿qué qué dónde va el costo ese, no? ¿Y dónde va a estar los datos alojados? Esa es la primer pregunta. Lo segundo es la seguridad la voy a tener por Teram y cómo va a ser la seguridad de ese warehouse también, porque claro, nadie va a ir a preguntarle al warehouse, pero el warehouse va a tener que tener alguna estructura de seguridad.

**Agustin Garcia**: Mhm.

**Christian Schiavo**: Eh, y bueno, y después, bueno, obviamente vienen los costos de Tera y todo, pero vamos a la parte de esta la otra ya me quedó clara que como es el pago de tokens, que esa es una de las una de las digamos

**Agustin Garcia**: Perfecto. Después con respecto a la seguridad, nosotros trabajamos hoy en nuestra versión software service trabaja sobre una nube de AWS. Digamos,

**Christian Schiavo**: Ajá.

**Agustin Garcia**: nosotros tenemos una certificación SOC 2 de seguridad,

**Christian Schiavo**: Sí.

**Agustin Garcia**: tenemos auditoría todos los años, dos veces por año, digamos que en ese sentido, digamos, no no no tenemos capacidad de acceder a los datos, digamos, hay toda una serie de normas que se cumplen,

**Christian Schiavo**: Eso.

**Agustin Garcia**: eh, y digamos que hasta ahí es nuestro esquema de seguridad. Inclusive si si necesitan una charla más profunda con nuestro incor seguridad también es una posibilidad. Nosotros tenemos dos flavor del producto, que uno es el software a service, que es el que vimos hoy,

**Christian Schiavo**: Sí.

**Agustin Garcia**: y después una réplica que es instalable en sus en su

**Christian Schiavo**: Aha.

**Agustin Garcia**: estructura, ¿sí?

**Christian Schiavo**: Sí, sí, sí, sí.

**Agustin Garcia**: Que básicamente permite es que usar de fuente su propio datalake, ¿no?

**Christian Schiavo**: Ah.

**Agustin Garcia**: Entonces ahora esa es la otra opción e que básicamente eso se implementa. Esto nosotros lo tenemos. ¿Por qué? Porque tenemos clientes de ciertas industrias particulares que la sensibilidad de los

**Pablo Barbarelli**: Sí, Bos

**Agustin Garcia**: datos y el compliance es más difícil, más engorroso la parte burocrática y administrativa de sacar los datos afuera de que implantar un producto adentro,

**Christian Schiavo**: Eh, sí, sí,

**Agustin Garcia**: ¿se entienden? Entonces eso también es una opción.

**Christian Schiavo**: sí.

**Agustin Garcia**: Inclusive ahí digamos que si bien hoy los costos de de storage no es algo digamos preocupante en todo esto, nada, digamos que inclusive los modelos, obviamente que el software servi tiene un tr un límite de de storage por y procesamiento por una cuestión básica que bueno puede venir un cliente y nos puede destrozar y nosotros no lo controlamos.

**Christian Schiavo**: O

**Agustin Garcia**: Eso el sistema tiene ciertos límites, pero digo, e en el generalmente el el sistema de licenciamiento es por tipo usuario, usuario viewer, usuario member. Eh,

**Christian Schiavo**: A

**Agustin Garcia**: digamos que es hoy en día, digamos eh los dos principales restricciones que tienen ambos modelos, ¿no? Entonces, si vos lo querés implantar local, no hay ningún problema. La diferencia es, ¿cuál? que el modelo de licen. potenciamiento. Si vos lo querés implantar local en tu infraestructura, yo te yo te hago una propuesta comercial por un periodo de tiempo y vos me lo prepagás porque, digamos, yo cuando te doy el producto te lo instalo con una llave que esa llave tiene está va a estar disponible por el periodo de tiempo definido, ¿se entiende?

**Christian Schiavo**: Sí,

**Agustin Garcia**: En el otro,

**Christian Schiavo**: sí.

**Agustin Garcia**: en el otro es un software a service de base mensual que bueno que si vos el día mañana decís,"Che, sabes que esto no me funcionó, bueno, entrad, eliminar mi dato, pum, bajar todo, chao, listo y se acabó." ¿Entendés?

**Christian Schiavo**: Ahí está bien.

**Agustin Garcia**: Un poco los dos modelos que que tienen

**Christian Schiavo**: Okay. Y el gasto el gasto de de almacenamiento lo lo pago,

**Pablo Barbarelli**: dentro del SAS.

**Christian Schiavo**: sea además de el SAS.

**Pablo Barbarelli**: dentro del SARS, ¿no?

**Agustin Garcia**: en el SAS. está incluido en el precio que yo te paso, que vas a tener ciertos límites,

**Christian Schiavo**: Ah.

**Agustin Garcia**: digamos, si vos me decí,"Che, mira, aquí una propuesta por el SAS y una Yo la propuesta del SAS incluye, yo te detallo todo lo los límites que de procesamiento de storage, el otro y en el otro eh básicamente va por usuario, por tipo por usuario y tipo usuario, porque básicamente el storage lo pones vos,

**Christian Schiavo**: B

**Agustin Garcia**: el procesamiento lo pones vos, ese tipo de cosas. Eh, es así. El servicio también incluye un un unas secciones de onboarding para que el equipo customer sucessome.

**Agustin Garcia**: Armar, a estructurar, digamos, también a agarrarle bien la mano a la a la herramienta. Y obviamente que también después una vez de la de terminado el onboarding, tienen acceso al equipo de customer sucess que los ayuda con lo que necesiten, dudas, preguntas. También lo que hacemos cada x cantidad de tiempo es hacer alguna sesión para ver si hay algo que se pueda optimizar en términos de cómo estructuraron la data y eso porque digamos si bien una de las ventajas competitivas

**Christian Schiavo**: Claro,

**Agustin Garcia**: que tiene Teramot es la eficiencia en la conexión con el MCP, está preparado para ser eficiente y no matarte a tokens, si los datos eh no están bien estructurados puede ser una una un punto de fricción.

**Christian Schiavo**: obvio.

**Agustin Garcia**: Entonces ese tipo de cosas se revisan un poco con el equipo como para que ustedes nada puedan sacarle el mayor jugo y exactamente

**Christian Schiavo**: Sí, sí. Optimizar el MCP es clave. Bien.

**Pablo Barbarelli**: Bueno, digo yo para no robar más tiempo del que tenían agendado por si tienen otras temas.

**Christian Schiavo**: He.

**Pablo Barbarelli**: Eh, Aus ahí creo que la próxima es poder contar con una una orden magnitud, una propuesta. Yo me gustaría entender las dos, tanto SAS como si fuese instalar nuestra infraestructura, teniendo en cuenta ambos perfiles, tanto members como viewers.

**Agustin Garcia**: Dale.

**Pablo Barbarelli**: Eh, no sé si tiene un un a partir de un mínimo de cantidad de usuarios para

**Agustin Garcia**: Mira,

**Pablo Barbarelli**: dimensionar.

**Agustin Garcia**: si querés lo que podemos hacer es yo decidme vos con qué mínimo podrían arrancar y yo te arme una propuesta con eso la charlamos. M. Y después la idea es que a medida que van creciendo y quieren ir escalando,

**Christian Schiavo**: Eso.

**Agustin Garcia**: se pueden ir sumando paquetes, eso no hay problema. Díganme ustedes qué idea tienen de cono arrancar.

**Pablo Barbarelli**: No, bueno, a ver, digo, de mínima, digo, me gustaría arrancar de muy mínima, pero para tener una idea, tipo cinco y cinco cinco usuarios viver, cinco y cinco cinco members, pero digo,

**Agustin Garcia**: Mhm.

**Pablo Barbarelli**: eh, y después no sé si paquetes de a C, de A 10, como para también una idea. cómo seguir el crecimiento en caso de que crecer o si es que si ese mínimo es viable, ¿no? Digo, para pensando nuevamente apuntando al board y a primeros a los primeros power user que ya tenemos, ¿no?

**Agustin Garcia**: Perfecto.

**Pablo Barbarelli**: Eh,

**Christian Schiavo**: Ahí un challenge a eso, Pablo,

**Agustin Garcia**: He.

**Christian Schiavo**: es hay una instancia anterior posible que sea algo más pequeño, inclusive algo muy pequeño que es para el área de Haití y nosotros ponemos dos tablas, tres tablas, jugamos un poco con esas tres tablas, jugamos un mes, dos meses, pagamos los dos meses, armamos todo y nos sacamos todas las dudas.

**Christian Schiavo**: digo, para estar totalmente seguro de que eh esta es la solución y después podemos ir con algo robusto y decir, miren, la la o sea, esto es lo que hicimos con estos dos, tres licencias, etcétera. Y lo después este sií, claro. Después bueno.

**Agustin Garcia**: Yo ahí, chicos, lo que les sugiero es les pueden arrancar con un plan starter en el software service, que son eh $400 por mes. hagan todas las pruebas que tienen, se sacan todas las dudas, los laburan con con el equipo de customer y una y cuando estén convencidos

**Christian Schiavo**: Claro.

**Agustin Garcia**: vemos el plan de digamos ahora cuál es el único tema que lo que tenemos que ver es que si vos después querés pasar a la versión que se implanta en tu infraestructura,

**Christian Schiavo**: Sí,

**Agustin Garcia**: ahí tendría que ver con el equipo técnico si es algo que se puede llegar a migrar.

**Christian Schiavo**: sí.

**Agustin Garcia**: lo veo como más costoso la migración, pero bueno, por lo menos es un escenario en el

**Pablo Barbarelli**: Lo tenemos en cuenta, lo tenemos en cuenta como para ver internamente. A mí el SAS es el que mejor me me gusta, pero también tengo que terminarlo de de ver internamente,

**Christian Schiavo**: Yes.

**Pablo Barbarelli**: incluso para no sumar temas a nuestro equipo de infra que siempre está con un millón de cosas.

**Pablo Barbarelli**: Y ese ese starters, ¿qué qué cantidad de usuarios tiene?

**Agustin Garcia**: definición viene con cinco usuarios eh member y con cinco usuarios los viewer, eh, y aparte si necesitan más porque digamos después el próximo plan se va a 2000 y ya después pack para el Enterprise que tiene que ver ya con la otra versión, pero digo, si necesitan un paquete de usuarios adicional o algo, lo podemos arreglar. Lo importante es que lo prueben y vean hasta acá en general lo que nos pasa es que lo prueban y me dicen,"Che,

**Christian Schiavo**: y Yeah.

**Agustin Garcia**: sale con usuario,

**Pablo Barbarelli**: es exponencial.

**Agustin Garcia**: vamos de aparte porque si te paso la propuesta sin usuario, vamos andando generando ven.

**Pablo Barbarelli**: Es que es exponencial. Sí, sí, sí. Cuando ves eso, todo lo que vimos hoy eh se parece

**Agustin Garcia**: Claro, cuando ven el valor que le pueden sacar, la eficiencia que pueden ganar, ¿entendés? Es como bastante deal breaker. Así que nada, si quieren yo el lunes, hoy o no sé si llego ahí hora,

**Pablo Barbarelli**: Tranqu, tranqu. Somos ansiosos,

**Agustin Garcia**: pero dale,

**Pablo Barbarelli**: pero podemos esperar el lunes. Es

**Agustin Garcia**: me avisan, lo charlamos y si quieren lo activamos la misma semana que viene y y arrancan a probar.

**Christian Schiavo**: Sí, sí.

**Agustin Garcia**: Lo que estaría bueno ahí o lo que hay que pensar ahí es bueno ya establecer las conexiones con la base de datos, que ahí tal vez lo que más puedes llevar es que el área de ustedes, porque si no queré llevar todo, ¿entendés? A lo mejor que genere algunas vistas o algo que se haga con la info que ustedes ya tienen y ya con eso configuramos la ingesta,

**Pablo Barbarelli**: Ok.

**Agustin Garcia**: la recurrencia y ya ustedes pueden empezar a a trabajar solos.

**Christian Schiavo**: Sí, sí, sí. Y por ahí inclusive, viste, podemos ir con estos Excels que yo te armé y metemos Excel porque el el click es,"Che, mira el valor que tiene esto." Esa es la esa es la eso es mostrar y después decir nosotros,"Che, esto va bien, escala." Y sí, porque si lo conect porque el tema de la conexión es un trámite, digamos,

**Agustin Garcia**: Total,

**Christian Schiavo**: o sea,

**Agustin Garcia**: total.

**Christian Schiavo**: y dejar el delta también es otro trámite, digo, no pasa por ahí. Eh, el tema es que le vamos a hablar con los mismos datos nosotros también. Yo las tablas las estoy armando para allá. ¿Qué qué significa armarlas para allá? que el MCP cuando vaya a buscar un cliente ID, va a estar cliente ID en todos lados deyado.

**Agustin Garcia**: Claro.

**Christian Schiavo**: Entonces, de esa manera, esas 15 tablas que yo te nombraba van a empezar a tener sentido, digamos, de de consumo. Eh,

**Pablo Barbarelli**: E no y después otro porque me queda la duda para el problema futuro, ¿no? Cuando esto, como decís vos, empieza a escalar y demás, más allá de los usuarios, desde la de la capacidad que tiene el starter, es decir, memoria, no sé, digo, espacio de memoria, procesamiento y demás, eh del starter saltamos el Enterprise que pasa de de 4000 a 2000 a, perdón, de 400 a 2000, es así más o menos la escala por lo que dijiste.

**Agustin Garcia**: Sí, sí, podemos llegar si hace falta armar un plano intermedio. Con algunos clientes lo hemos hecho, armábamos un plan intermedio como para si el salto no es aparte tal vez vos capaz que de cinco, después pasas a a a a 10, ¿entendés? Eso no hay problema, lo vemos. Lo importante, digo

**Pablo Barbarelli**: Pero se puede se puede podemos ir gestionando nosotros desde la plataforma eh el entendimiento de che, nosotros tenemos, como decía tenemos estos 15 modelos de datos que son el core de la organización y con esto va a hacemos el 95% de las cosas que necesitamos y al cargarlo sabemos exactamente el espacio que estamos teniendo y si estamos al al 95 de de la capacidad o al 50 y estamos tranquilos como para hacer todo un análisis completo de viste,

**Pablo Barbarelli**: de no solo de ahora que atiende y demás, sino proyectarlo en el tiempo que claro que aunque sea hasta final del año

**Christian Schiavo**: poquito. H

**Pablo Barbarelli**: estamos ya estamos por empezar a hablar del presupuesto 2027, ya hasta final del año que viene Esto puede correr sin problema, ¿no?

**Agustin Garcia**: Sí,

**Pablo Barbarelli**: Va por ahí.

**Agustin Garcia**: sí, eso. Preocupate. Lo que te mueve la aguja es la cantidad de usuarios, que aparte te va a mover la aguja por Teramot y también por la cantidad de licencias que necesites, que yo en general, me imagino que como te decía Gabi, con un plan pro normal de $20 vas a estar bien. Ahora, si después tenés alguno que venga y diga,"Che, macho, a cada rato me está pidiendo que espere." Bueno, ahí tendrás que sacar uno de 100 tal vez, pero en general no pasa poco, ¿eh?

**Christian Schiavo**: M.

**Agustin Garcia**: Y nada, y pero con eso quédate tranquilo que que nada, que lo importante es que ustedes lo puedan probar, le vean el valor y en función de eso ahí después vemos porque seguramente van a

**Christian Schiavo**: Sí.

**Agustin Garcia**: necesitar después saltar algo más. Y bueno, y si querés en algún momento me vas a decir,"Che, mira, bueno, necesito presupuestar para el año que viene." Yo puedo llegar a tener, no sé, 50 usuarios eh member y 150 viewers. ¿Listo? Y ahí eh te paso una propuesta, lo ves, lo acomodamos y y vemos ahí. Obviamente que después puede ser un plan escalonado, eso es algo que que lo podemos charlar sin problema.

**Pablo Barbarelli**: Bien. Bueno,

**Agustin Garcia**: Sí.

**Christian Schiavo**: Super.

**Pablo Barbarelli**: nada más.

**Gabriel Puertas**: Chicos,

**Agustin Garcia**: Bueno,

**Gabriel Puertas**: disculpen que yo apagué la cámara,

**Agustin Garcia**: muchachos.

**Gabriel Puertas**: pero estoy yendo a buscar mi hijo, pero escucho todo.

**Pablo Barbarelli**: Perfecto.

**Gabriel Puertas**: a disposición de algo.

**Pablo Barbarelli**: Ahora hacemos lo mismo nosotros acáamos. Vamos a buscar los hijos al colegio los viernes.

**Christian Schiavo**: Sí, sí,

**Pablo Barbarelli**: Es el es el día.

**Christian Schiavo**: es el día.

**Agustin Garcia**: Bueno, muchachos,

**Pablo Barbarelli**: Bueno,

**Christian Schiavo**: Muy amable, eh,

**Agustin Garcia**: propuesta cualquier cos vamos hablando Dale,

**Pablo Barbarelli**: dale porfa.

**Christian Schiavo**: super bien. Gracias. Eh, buen fin de semana.

**Agustin Garcia**: chao.

**Christian Schiavo**: Saludos.
