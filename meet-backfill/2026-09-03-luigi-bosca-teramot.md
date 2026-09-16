# Luigi Bosca <> Teramot

**Fecha:** 2026-09-03T15:00  
**Duracion:** ~103 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** dfritzler@luigibosca.com, efranco@luigibosca.com, fmartinez@luigibosca.com, mbacher@luigibosca.com, Gabriel Puertas, Agustin Garcia  
**Externos:** dfritzler@luigibosca.com, efranco@luigibosca.com, fmartinez@luigibosca.com, mbacher@luigibosca.com  
**Archivo origen:** Luigi Bosca _ Teramot - 2026-09-03 15_00 GMT-03_00/Luigi Bosca _ Teramot_ 2026_09_03 15_00 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Evaluación de Teramot para consolidar datos corporativos y generar reportes mediante inteligencia artificial.Demostración de TeramotProcesamiento de consultas financieras con Claude demostró la integración de Teramot con modelos de lenguaje para generar reportes.Seguridad y costosDiscusión sobre la protección de datos, control de accesos por usuario y optimización de los costos asociados al consumo de tokens.Propuesta pilotoPropuesta de ejecutar un proyecto piloto de 2 meses para demostrar eficiencia antes de una implementación generalizada.

### Decisiones

Requiere más debate
Desarrollo de un modelo de costos intermedio Se acordó revisar y armar en conjunto con Agustín un esquema de costo mensual intermedio adaptado a la escala de usuarios de Luigi Bosca.
Acordada
Estructuración de permisos y roles de usuarios Se acordó definir tres modelos de usuario diferenciados para la plataforma, segmentando la creación, la consulta mediante tokens y el consumo exclusivo de tableros según el rol.

### Próximos pasos

[Damian Fritzler LB] Enviar archivos: Enviar el archivo Excel con la información de configuración y los prompts correspondientes por correo electrónico a Gabriel.
[Gabriel Puertas] Procesar datos: Integrar la nueva información recibida en la plataforma Teramod y procesar los reportes ajustándolos a las configuraciones proporcionadas.
[Gabriel Puertas] Analizar costos: Realizar un análisis de consumo de tokens y costos asociados utilizando la API de la plataforma para verificar el impacto presupuestario del flujo de trabajo.
[Gabriel Puertas] Comparar costos: Realizar una prueba con la API de Sonet 5 para calcular y contrastar los costos con los resultados actuales.
[Damian Fritzler LB] Revisar usuarios: Analizar la lista de usuarios para definir los niveles de acceso y consulta necesarios en la plataforma.
[Gabriel Puertas] Actualizar datos: Procesar el archivo Excel mañana para preparar la demostración junto a Eli.
[Damian Fritzler LB] Agendar reunión: Coordinar un espacio para la próxima semana con Eli y el equipo de Teramot para revisar la seguridad y estructuración del tablero.
[Agustin Garcia, Gabriel Puertas] Diseñar licenciamiento: Desarrollar un esquema de costos a medida que se ajuste a las necesidades específicas de la empresa.
[Gabriel Puertas, Damian Fritzler LB] Estructurar usuarios: Estructurar los roles y permisos de los usuarios para la plataforma. Esto permitirá definir qué usuarios tienen acceso a cargar archivos con consumo de tokens y qué funcionalidades específicas tendrán disponibles.
[Damian Fritzler LB] Definir modelos: Desarrollar una propuesta de estructura para los modelos de Inteligencia Artificial que incluya la orquestación, el uso con tokens y el uso exclusivo de paneles de control. El objetivo es comparar los tres modelos definidos para seleccionar el más eficiente en costos.
[Damian Fritzler LB] Evaluar costos: Evaluar un modelo de costo mensual intermedio para la implementación de los servicios. Esta gestión se realizará en conjunto con el equipo de infraestructura o adquisiciones para optimizar el presupuesto.

### Detalles

Presentación de participantes y objetivo de la prueba: Damian Fritzler LB presenta a Mati, Fabi y Eli al inicio de la reunión. El propósito de la sesión es realizar pruebas utilizando un reporte complejo de días de pago pendientes que Eli procesa habitualmente descargando información del sistema contra tableros de Excel, evaluando si la plataforma Teramot puede replicar o mejorar dichos resultados (00:06:48).
Estado de actualización de las bases de datos: Gabriel Puertas y Damian Fritzler LB discuten sobre la fecha de los datos disponibles, señalando que la base se cargó el 1 de septiembre pero no se había actualizado automáticamente, acordando trabajar inicialmente con la vista actualizada hasta junio (00:07:55).
Introducción a la plataforma Teramot: Agustin Garcia explica que Teramot es una herramienta diseñada para consolidar información de diversos sistemas empresariales (incluyendo un sistema de planificación de recursos empresariales o ERP de nicho) en un único depósito de datos. El sistema permite limpiar, gestionar y preparar la información para su posterior explotación mediante inteligencia artificial (00:09:13).
Conectividad con modelos de lenguaje y generación de reportes: Agustin Garcia detalla que la plataforma utiliza un protocolo de contexto de modelos o MCP para conectarse con modelos de lenguaje grande en el mercado como ChatGPT, Claude, Gemini y Copilot, además de incluir un agente interno que facilita la conversación con los datos, la automatización de análisis y la generación de reportes de inteligencia de negocios (00:10:25).
Carga de fuentes de datos y estructuración: Gabriel Puertas describe el proceso de carga de dos fuentes de datos (una con 16 tablas y otra con 5 vistas para Tableau) procedentes de sistemas como Aon, Vtex, Salesforce y Nitre (00:13:19). Explica que el proceso agéntico realiza una sanitización de datos (normalización de formatos y manejo de valores nulos) y genera metadatos automáticos para cada tabla y columna (00:14:29).
Procesamiento de consultas financieras con Claude: Gabriel Puertas demuestra en vivo cómo se conecta Teramot con Claude mediante el protocolo MCP para resolver un caso práctico planteado por Eli, consistente en obtener un cuadro con saldos de proveedores de cierre mensual, compras del calendario y días de pago pendientes agrupados por categoría de gasto (00:17:17) (00:21:14).
Almacenamiento de conocimiento y reglas de negocio: Gabriel Puertas explica que las particularidades descubiertas durante el procesamiento de los datos, como reglas contables específicas de rubros, quedan almacenadas en un campo de conocimiento colaborativo dentro de Teramot, auditándose y enriqueciéndose con el uso de le participantes (00:24:39).
Resultados de la tabla generada y análisis del costo de uva: Gabriel Puertas revisa los resultados obtenidos por Claude, señalando ajustes en saldos de proveedores, movimientos de cuentas de resultados al cierre de junio, cálculo de días de pago pendientes y la capitalización de la compra de uva en inventario (00:26:00). Se observa que categorías como publicidad presentan entre 190 y 215 días de pago pendientes frente a los 70 y 115 días del resto (00:29:10).
Creación de procesos de extracción, transformación y carga (ETL) y tableros: Gabriel Puertas explica que una vez validada la tabla resultante mediante lenguaje natural, Teramot genera un proceso de extracción, transformación y carga automatizado para futuras actualizaciones diarias sin intervención de agentes, permitiendo además publicar tableros interactivos actualizados en tiempo real (00:30:27).
Resumen de la propuesta de valor de Teramot: Damian Fritzler LB resume que el valor esencial de Teramot radica en unificar información dispersa en múltiples sistemas de la compañía y centralizarla para interactuar con agentes de inteligencia artificial en la creación de tableros y reportes (00:33:53).
Cambio en la dinámica de trabajo y generación de planes de acción: Gabriel Puertas argumenta que el verdadero valor de la herramienta trasciende la creación rápida de tableros en una o dos horas, transformando la forma de trabajar al permitir que modelos como Claude generen perspectivas comerciales, planes de acción, automatizaciones, modelos predictivos y reportes gerenciales para directorios (00:35:38).
Seguridad y confidencialidad de la información: Gabriel Puertas y Damian Fritzler LB abordan la protección de datos, aclarando que Teramot puede instalarse en la infraestructura interna de Luigi Bosca o utilizarse mediante un protocolo donde los modelos de lenguaje externo solo visualizan la estructura de tablas, vistas previas y datos agregados, respaldados por certificaciones de seguridad SOC y acuerdos de confidencialidad empresariales (00:39:39).
Modelos de consumo de tokens y costos asociados: Agustin Garcia y Gabriel Puertas explican las opciones de consumo de tokens, indicando que las versiones de escritorio de los proveedores ofrecen planes estándar accesibles (como planes de 20 dólares y de 100 dólares para usuarios intensivos) con costos subsidiados en comparación con las interfaces de programación de aplicaciones o API (00:45:05).
Comparativa entre consumo por aplicación y por interfaz de programación: Gabriel Puertas detalla las diferencias entre utilizar cuentas estandarizadas con planes fijos de consumo masivo frente a llamadas directas mediante llaves de interfaz de programación vinculadas a servidores de proveedores como Anthropic, señalando que ambas opciones permiten controlar presupuestos y límites por hora, semana y mes (00:50:25).
Acompañamiento de éxito del cliente y adopción de la herramienta: Gabriel Puertas y Agustin Garcia señalan que Teramot incluye un servicio de acompañamiento a través del equipo de éxito del cliente diseñado para transferir conocimientos, ayudar a superar la curva de aprendizaje inicial y resolver casos de uso específicos como la configuración de sistemas de alerta inteligente (00:57:33).
Control de accesos y permisos por usuario: Damian Fritzler LB consulta sobre la restricción de información para que no todes les usuaries tengan acceso a todos los datos, a lo cual Agustin Garcia responde que la plataforma cuenta con un esquema de espacios de trabajo y proyectos gestionados con el equipo de éxito del cliente, asegurando que cada persona visualice únicamente los tableros y datos permitidos según sus permisos (01:00:29).
Gestión de roles y permisos en Teramod: Gabriel Puertas detalla las funciones del superusuario (*owner*) y los niveles de edición, vista y eliminación de información dentro de Teramod para Luigi Bosca. Se explica que es posible configurar proyectos y tablas personalizadas para restringir datos sensibles, como excluir los sueldos de directivos para el personal de recursos humanos, contemplando a futuro restricciones a nivel de conector de base de datos (01:01:38). Damian Fritzler LB solicita agendar una revisión detallada de la estructuración de seguridad y los archivos de Excel asociados (01:04:11).
Actualización diaria de datos y licenciamiento intermedio: Gabriel Puertas informa que la plataforma se ha configurado para actualizar la base de datos automáticamente todos los días a las 5 de la mañana. Por su parte, Damian Fritzler LB consulta sobre la existencia de un modelo de licenciamiento intermedio, indicando que las opciones de 1,000 y 400 dólares no se ajustan a los requerimientos de Luigi Bosca (01:05:39). Gabriel Puertas confirma que la mayoría de las organizaciones operan bajo un esquema intermedio (01:06:47).
Estructura de usuarios y consumo de tokens: Damian Fritzler LB plantea la preocupación de incurrir en altos costos al licenciar a todo el personal en la nube, proponiendo que solo un grupo reducido de creadores (incluyendo a Eli, Mati y cuatro o cinco usuarios clave) cuenten con licencias completas (01:07:34) (01:09:46). Gabriel Puertas aclara que los usuarios con acceso exclusivo de lectura a los tableros publicados no consumen tokens, a diferencia de quienes interactúan mediante agentes conversacionales (01:11:11). Damian Fritzler LB compara estos costos con las opciones integradas en herramientas como Tableau y Slack (01:13:46) (01:16:06).
Restricciones de permisos y modelos de inteligencia artificial: Damian Fritzler LB propone establecer limitaciones según el rol de cada participante, restringiendo la facultad de adjuntar archivos externos para prevenir un consumo innecesario de tokens en consultas exploratorias (01:19:58). Gabriel Puertas expone la disponibilidad de diversos modelos de inteligencia artificial, tales como alternativas de Cloud, OpenAI y proveedores chinos (01:21:03). Damian Fritzler LB desecha el uso de modelos de origen chino, norcoreano y ruso debido a políticas de seguridad de la información, inclinándose por estándares corporativos o por el despliegue de infraestructura propia en Azure con modelos optimizados para planificación (01:22:09).
Propuesta de proyecto piloto y retorno de inversión: Gabriel Puertas sugiere ejecutar un proyecto piloto limitado a dos meses con tres o cuatro integrantes clave de Luigi Bosca para demostrar la eficiencia y medir el retorno de inversión antes de una implementación generalizada (01:25:56). Damian Fritzler LB se compromete a revisar el volumen actual de usuarios de consulta y a evaluar junto con Agustin Garcia un modelo de costos intermedio (01:28:15). Gabriel Puertas advierte sobre la necesidad de supervisar el uso de los chats con datos externos para evitar un impacto presupuestario imprevisto (01:29:39).
Casos de uso operativo y comercial mediante WhatsApp: Gabriel Puertas comparte un caso de éxito implementado en otra compañía llamado "el minuto de oro", el cual emplea tablas optimizadas en Teramod conectadas a WhatsApp para dotar a los equipos comerciales de información relevante sobre los clientes antes de cada visita sin un consumo elevado de tokens (01:32:15). Damian Fritzler LB expone un desarrollo similar en curso en Luigi Bosca enfocado en operaciones y ventas, orientado a integrar datos de Salesforce y actividades comerciales a través de interacciones automatizadas por WhatsApp (01:34:33).
Integración técnica y próximos pasos: Gabriel Puertas explica el procedimiento técnico para conectar SAP, Salesforce y Teramod mediante claves de API, la herramienta N8N y protocolos de contexto de modelo para automatizar flujos de trabajo y reposición de stock (01:37:22). Damian Fritzler LB señala que Luigi Bosca centraliza la gobernanza y los datos de clientes directamente en Salesforce (01:39:46). Finalmente, Damian Fritzler LB acuerda coordinar con Agustin Garcia y Gabriel Puertas la definición de los perfiles de usuario y la estructura de costos para la semana siguiente (01:40:54).

---

## Transcripcion

**Agustin Garcia**: Buenas, buenas.

**Gabriel Puertas**: Seonar la campana, la campana virtual.

**Agustin Garcia**: No, aparte también iba dispuesto a negociar, pero no hizo falta.

**Gabriel Puertas**: Bien. Uy, boludo, desde que volví de no sé que cuando volví de Brasil hay alguien más volví con las alergias

**Agustin Garcia**: Ah, sí.

**Gabriel Puertas**: full. Estoyando,

**Agustin Garcia**: Empieza

**Gabriel Puertas**: hermano. Te decía, boludo, que volví y no sé, viste que capaz que te desacostumbraba, pero Rosario empieza una época de eso, de eso, ¿cómo que le llaman?

**Agustin Garcia**: la

**Gabriel Puertas**: Eh, sí, pero hay un árbol de m***** que ¿Cómo es?

**Agustin Garcia**: El el el plátano,

**Gabriel Puertas**: Los plátanos. el plátano.

**Agustin Garcia**: el plátano. Eh, olvidate,

**Gabriel Puertas**: Me mata,

**Agustin Garcia**: a mí había una época que me a mí me mata, eh, a mí me mata, pero bueno, todavía acá no sé, no llegó,

**Gabriel Puertas**: boludo.

**Agustin Garcia**: parece. Vamos a ver.

**Gabriel Puertas**: A ver qué hacen estos chicos. Y esto con estos chicos era hacer demos. Yo medio que estoy como para ver qué onda con los nuevos

**Agustin Garcia**: van a querer querer explotar las nuevas tablas,

**Gabriel Puertas**: tablas.

**Agustin Garcia**: seguramente traigan un tablero, eh, y bueno, vienen con gente de administración y finanzas que que seguramente sepan del tema. E así que bueno, vamos a ver qué necesitan y a ver cómo cómo los podemos acompañar. Espera

**Gabriel Puertas**: Sí, pera. con estos chicos de esto que me acaba de pasar. ¿Qué onda? Nos tenemos que juntar, conectarle la tabla.

**Agustin Garcia**: que te tengo la transcripción. Uh.

**La sesión comenzó después de 00**: 02:57

**Damian Fritzler LB**: Ahí estamos.

**Gabriel Puertas**: Estamos bien,

**Damian Fritzler LB**: No se escucha bien,

**Gabriel Puertas**: todo bien. ¿Cómo están?

**Agustin Garcia**: Sí.

**Damian Fritzler LB**: eh. por acá la TV. Ahí vamos. Bueno, ahí te está sumando, Fabi. En un minutito va saliendo una reunión. Les presento a Mati ya lo conocían, ¿verdad?

**Agustin Garcia**: A Mati lo conocíamos. Hola, Mati.

**Damian Fritzler LB**: Las primeras reuniones. ¿Cómo están? Bueno, y Ali creo que no. No me conocen. Hola, ¿qué tal? Eh,

**Gabriel Puertas**: Todo

**Agustin Garcia**: Un gusto.

**Damian Fritzler LB**: tienen el definitivamente el gusto va a ser de ustedes, ¿no? Bueno, bien. Una vez que me tiraste,

**Agustin Garcia**: No.

**Damian Fritzler LB**: obvio, una vez me tocaba. Eh, Eli es jefa de de control de gestión.

**Gabriel Puertas**: Bien.

**Damian Fritzler LB**: Sí, soy del equipo de estrategia. Eh, con lo cual ella tiene mucho conocimiento. Los números de la empresa los tiene bien fresquitos en la cabeza, nos va a estar ayudando hoy junto con Fabi,

**Gabriel Puertas**: Bueno,

**Damian Fritzler LB**: con Mati hacer algunas pruebas. La idea, ¿cuál es? Con él estuvimos laborando un poquito. Le dije,"Pasarle un reporte que te complejice el cierre, te moleste, qué datos tengas que usar que estén dentro de la plataforma y no." Y la idea era un poquito, bueno, desafiar e lo que hoy ella hace un poquito bajando información del sistema, contra los tableros y demás en una en un Excel que ella también tiene ciertas configuraciones. Bueno, tirarse la ter y si llegamos algo parecido a lo que ella espera. Lo que hicimos también es, bueno, adelantemos, ¿no?

**Damian Fritzler LB**: Y hagamos un breve prom de lo que le pediríamos en base a al reporte a nivel estructural y y conceptual de los datos.

**Agustin Garcia**: Perfecto.

**Gabriel Puertas**: Buenas,

**Damian Fritzler LB**: Hola,

**Agustin Garcia**: Hola, ¿qué tal?

**Damian Fritzler LB**: perdóname,

**Agustin Garcia**: No hay problema.

**Damian Fritzler LB**: con lo cual también tiene los números muy claros del día. E le estaba contando la idea es hacer algunas pruebas con con los chicos con él estuvimos trabajando en un reporte que a ella le complexab el cierro algún reporte medio complejo. La idea es hacer una prueba hoy. Tenemos los datos hasta junio eh la vista está actualizada, no sé si está en actualizada. Está.

**Gabriel Puertas**: Ah, nosotros yo ahí hay un comentario, eh, nosotros lo cargamos el primero de septiembre,

**Damian Fritzler LB**: Okay.

**Gabriel Puertas**: pero no pusimos actualizar porque nada, no nos sentimos, o sea, como eso le pega una vez por día a la base, queríamos tener el okay de ustedes, con lo cual eso está actualizado el primero de septiembre en la última. Yeah. que nos pasaron lo tro un poquito más atrás,

**Damian Fritzler LB**: Lo podemos hacer Julio último.

**Gabriel Puertas**: pero

**Damian Fritzler LB**: Sí, si quieren uno más atrás también. Bueno, hagamos una cosa, Agustín Gabriel, si quieren más para él y para Fabi hacer un breve resumen de conceptualmenteamos.

**Gabriel Puertas**: vamos,

**Damian Fritzler LB**: están al tanto. Les comenté lo que es la herramienta, pero eh si tienen alguna duda estaría bueno que que

**Gabriel Puertas**: dale. Buenísimo. Yo le les voy a compartir pantalla, ¿no? para hacerle una presentación, sino para Sí,

**Agustin Garcia**: que le le hago una introducción breve para les cuento un poco la

**Gabriel Puertas**: de una de una de una de una

**Agustin Garcia**: herramienta, ¿no? O sea, la herramienta básicamente es una herramienta que permite consolidar la información,

**Gabriel Puertas**: Vale.

**Agustin Garcia**: generar un datalake, eh ingestando datos de los distintos sistemas que ustedes puedan tener. Ya venimos hablando con con Dami, con Mati, que sabemos que tienen un IRP particular, muy de nicho, que tienen ciertos sistemas, digamos, en paralelo que con distintas funciones. Teramot lo que permite es ingestar la información de esos distintos sistemas en un solo lugar con el fin de poder explotar la información en conjunto sacando insights eh digamos más valiosos que si tenés la información por separado. también, obviamente que permite la gestión, la limpieza. Hay un montón de cuestiones sobre los datos para digamos que esa información esté correcta al momento de explotarla, pero digamos que ese es el paso cero para después poder eh digamos hacer una gestión y explotación con inteligencia artificial.

**Damian Fritzler LB**: Oh.

**Agustin Garcia**: La plataforma permite por medio de un conector NCP conectarse a digamos eh los distintos

**Gabriel Puertas**: Ok.

**Agustin Garcia**: LLM hoy en día en el mercado como Chachi PT, Cloud, Gemini y Copilot. Eh, y también, obviamente, tiene un agente interno que permite ciertas funcionalidades y conversar con sus datos. Y adicional a esto, el sistema lo que permite también es por el por medio del uso de inteligencia artificial realizar análisis, eh explotación de información, generación de reportes que tal vez hoy en día puedan ser eh de carácter manual en digamos de forma un poco más automatizada, logrando eficiencia y productividad. y también la generación de reportes de B, que eh hoy en día es un trabajo bastante manual,

**Damian Fritzler LB**: Ok.

**Agustin Garcia**: que hay que preparar los datos y también después preparar los tableros. Esto hoy se puede hacer, digamos, por medio de algunos prompts y la publicación inclusive también para que eh una definida cantidad de usuarios según los permisos que se definan puedan tener acceso a ver esos tableros que después se van actualizando a medida que que la información va actualizándose, ¿no? Eso como para que tengan una idea así general de de de la plataforma.

**Damian Fritzler LB**: Okay. Mario está con Mario. Sí. Em, no sé si tengo eh lo que arré con Eli, es el reporte de DPO, eh, Tengo el Excel que ella suele usar para para la información que ella suele sacar del sistema.

**Damian Fritzler LB**: Tengo el tablero también, ¿cuál es? Podemos arrancar por ahí a ver qué es lo que saca y de última, no sé si querés último podemos ir desafiándolo con algún dato o o algún reporte más complejo de vos. quizás necesit más podemos arrancar con eso. Sí, creo que tal vez estaría bueno y no sé si está en la en la base de info que les compartimos a ellos, pero para entender un poco, si querés, tomando datos de distintos sistemas nuestros, cómo unificas en un único reporte al final del día, digamos, la es el valor que te da la herramienta, digamos, ¿no? donde bueno, consolidarse el único reporte eh información que vienen de que nosotros tenemos disaminados en distintos sistemas de no solamente en sino en el resto lo que habla con se habla con Ávaron, pero no sé por eso no sé la verdad que no conozco la base de qué nivel de información tienen ellos

**Gabriel Puertas**: Pero le le ya vamos aí. Yo le yo mientras ustedes le cuentan que van van a saber explicar mejor, yo le voy mostrando la

**Damian Fritzler LB**: ese tablero, o sea, tiene toda la información,

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: la misma información que tiene tabló la tiene. Okay. Si vos le pasaste esos Ex. No, no,

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: no tengo el la idea era cargar el Excel y ver cómo lo procesa en el momento para ver cómo procesa la información que no conoce. E tenemos información de Aon hoy. Si querés pongo después sumar información de Vtex, de Cellforce, de Nitre, no hay problema con eso. Okay. Em, ¿a quién le paso el correíto con la info?

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: Ahí está explicado brevemente el

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: prompt y el Excel que usa Eli. Estaría bueno que nada quizás cargarlo. Leemos justo a ver qué les parece. Te lo

**Gabriel Puertas**: mandalo a a Gabriel @teram que estoy yo estoy proyectando. Yo ahora lo busco y mientras tanto le cuento a Fabi muy muy muy

**Damian Fritzler LB**: mando.

**Gabriel Puertas**: rápidamente qué pasó hasta acá. Básicamente nosotros esto termod posiblemente sea la última vez que lo lo veas, pero digo para mostrarte es cargamos dos fuentes de datos. Una es una base de datos que tiene 16 tablas y la otra que aparentemente son tablas o vistas para tabló son cinco tablas. ¿Qué pasó acá cuando yo cargué todo eso?

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: Vos andas mandándomelo que hasta que llegue el correo yo ya después sigo y engancho desde ahí. Eh, ¿qué pasó acá? Nosotros cuando inestamos esa información, eh cuando nos hacemos desinformación,

**Damian Fritzler LB**: Ok.

**Gabriel Puertas**: hay un proceso agéntico que básicamente lo que hace es un proceso que es muy necesario en ingeniería de datos, que es sanitización de la información. O sea, cualquiera que entienda eso, esto es simplemente normalizar formato cuanto de fecha, bueno, todo tipo de cosas, trabajar con nulos, cosas que se hacen, pero lo que es más importante es generar metadata de de esas tablas. Acá yo me puse en una tabla que se llama code y fíjate que el modelo dice cada row representa, no sé si ven, yo voy a aumentar un poco, each row represent of goods, ces forne products detailing sale performance associated every time. Esto esto es un proceso que interpretó que era esa información. Eh, digamos, ninguno de nosotros escribió nada acá. el proceso que yo te decía en el cual sanitizo esa información. Eh, nada, nosotros esto es más técnico, pero lo exponemos acá. O sea, eso es super importante. ¿Por qué? Porque lo que hicieron los agentes, como esto va a ser datos que que en definitiva son fuente de verdad y tenemos que confiar.

**Gabriel Puertas**: El proceso de transformación de esa información está explícito acá con el código que que realmente se ejecuta, ¿no? Acá, por ejemplo, importa saber, pero acá básicamente lo que está haciendo en una columna es sacando eh tipos de datos que que en realidad no representan un dato, sino que son un campo vacío. Eh, nada. Y acá esto esta esto a mí en particular me gusta mucho. ¿Por qué? Porque hace hace mucho al al producto, digamos. detecta es cada columna y qué representa. Eso fue bueno, eso pasa con todas las tablas y todas las columnas de toda la información que nos pasaron. Una vez que esto está conectado, quiere decir que si nosotros venimos y definimos cada cuánto actualizamos, esto es un proceso que va a correr todos los días, se va a traer la información nueva y va a quedar funcionando. Ahora, ¿qué hago yo con esto? La idea de Teramot es que Teramot sea una herramienta para que le dé acceso a los modelos de inteligencia artificial para explotar esta información. Eso lo hacemos, o sea, nosotros si bien no vendemos inteligencia artificial, sino que nosotros, yo por ejemplo uso mucho Cloud, yo tengo esta es mi cuenta en particular y lo que se hace con eso, con este proveedor es conectarlo a Teramod a Cloud.

**Gabriel Puertas**: Esto no es compartirle información a Teram, sino a través de un protocolo que que se usa, se llama MCP, no importa. Es como es un protocolo con el cual yo le permito a Cloud utilizar Teramod sin hacerse de la información, pero entender qué información tiene y entender lo que lo que yo necesito. Yo lo que lo que vamos a hacer acá en vivo es, esperen que yo esto acá no lo veo. Ah, me debería ir a mi mail. Esperen, perdón, Gmail. y buscar el correo. Yo lo que voy a hacer es básicamente darle lo que ustedes me pasaron. Esto. Voy a hacer prontos. A ver si se lo puedo pasar así hasta

**Damian Fritzler LB**: Lo de abajo no, Gabi, es simplemente referencial a la nuestra.

**Gabriel Puertas**: acá.

**Damian Fritzler LB**: E si el PR, ¿qué es lo que me gustó de esto? que el PR lo hizo directamente y le dije explicaron tus palabras como si vos lo tendrías que pedir para

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: entender un poco la interacción que va a tener un usuario que no sea

**Gabriel Puertas**: Bueno, dale.

**Damian Fritzler LB**: tecnológico y

**Gabriel Puertas**: Yo le voy a poner, yo lo voy a rotear a esto.

**Damian Fritzler LB**: tiene

**Gabriel Puertas**: Voy a decir eh vamos a conectarnos con digamos con el

**Damian Fritzler LB**: un exunto Todo bien.

**Gabriel Puertas**: sí con el workspace de Luigi. Él va a buscar de nuevo. Estamos conectados con con Teramod. Yo básicamente hice una conexión. Eso nada, se hace se hace en 2 minutos, se autentifica, o sea, esto no es que lo va a poder usar cualquiera, sino que se autentifica con el usuario de Teramot, o sea, solamente yo lo puedo ver. De hecho, si a ustedes no los cargo, no lo podrían hacer. Acá encontró el proyecto que es data warehouse y le y le voy a decir, eh, perdón, Dami, el Excel que vos me pasaste es para revisión. Se lo puedo pasar a a Cloud o no? Porque tengo miedo que tenga alguno datos porque digo acá ya no pasa nada.

**Damian Fritzler LB**: No, no, no. No, enteramos gustaría

**Gabriel Puertas**: A CL no vamos para vamos hacer una cosa.

**Damian Fritzler LB**: igual.

**Gabriel Puertas**: Yo a Cloud lo que le voy a decir es le voy a pasar esto.

**Damian Fritzler LB**: Exacto.

**Gabriel Puertas**: Este de acá decir, bueno, mira, estoy en esto para que me haya quedado

**Damian Fritzler LB**: ¿Vas

**Gabriel Puertas**: bien. Voy a pasar un problema que me dieron para resolver con los datos disponibles.

**Damian Fritzler LB**: a necesitar del Excel para resolverlo,

**Gabriel Puertas**: Eh, dame un segundo. Vamos a ver qué me dice. Lo que voy a hacer es bajarme el Excel. Este lo debería ver porque algo que no hablamos de la de la demo es que yo le quiero ver al Excel a ver si lo puedo cargar a Cis, ¿no? Porque esto va a demorar un rato. Son todas las tablas así,

**Damian Fritzler LB**: Sí, puede

**Gabriel Puertas**: ¿no? Esta esta tiene tablas agregadas. Esta no la puedo mandar yo.

**Damian Fritzler LB**: tener

**Gabriel Puertas**: La la fuente de datos que puedo cargar en Teramod eh son de este tipo, o sea, tipo como si fuese una base de datos, digamos.

**Damian Fritzler LB**: columnar.

**Gabriel Puertas**: estas agregadas,

**Damian Fritzler LB**: M.

**Gabriel Puertas**: digamos, esto tiene campos agregado o calculado, qué sé yo. O sea, nosotros enteramos cargamos fuentes de información. Lo que deberíamos hacer con esta es seleccionar dejarnos solamente las que son fuente

**Damian Fritzler LB**: Okay.

**Gabriel Puertas**: de información y que que deben ser estas

**Damian Fritzler LB**: No, lo que vas a son las de

**Gabriel Puertas**: y cargar,

**Damian Fritzler LB**: configuración.

**Gabriel Puertas**: pero bueno. Y cargar solamente esas porque si no lo que voy a intentar es cargar todo esto. Pero vamos a ver qué nos está diciendo Cloud. Está buenísimo. Dale, vamos. Primero miro que hay disponible del lado del proveedor y compras. Si no lo puede hacer, yo esperaría que me diga,"Che, me va a faltar algunos datos y me va a proponer algo particular para hacer." Y digamos acá lo que está haciendo, yo les muestro eh este protocolo MCP, básicamente lo que es un set de herramientas que Teramo le ofrece a Cloud para que para que use Teram, por ejemplo, explorar las tablas, hacer previews que son eh mirar las primeras 100 filas y cosas por el estilo. y él lo que está haciendo es buscando eh analizando toda la información que nosotros ya le dimos disponible para intentar resolver lo que lo que lo que le pedimos, que en particular yo no lo leí. Necesito quedarme en un cuadro con filas y columnas donde las filas son saldo de proveedores de cierre de cada mes, compras del mel calendario y DPO, saldo sobre compras propomedio del último 12 meses por 30 agrupado en categoría por tipo de gasto, sugerencia costo uva vino.

**Gabriel Puertas**: Bueno, ahí lo que está haciendo Cloud es nada, ya recib el prom estoy intentando resolver lo que aparezca. en los datos que que nosotros ya le habíamos ya le habíamos dado.

**Damian Fritzler LB**: Voy a preparar

**Gabriel Puertas**: cada uno de est de estas llamadas, eso es algo que a mí me gusta, fíjense que que tiene una frase balance versus monly in the accounts, lo que él está buscando y haciendo queries muy específica en cada una de las fuentes de datos que nosotros le dimos intentando entender cómo va esa información. Eh, fíjense que acá hay algunos resultados. producto en elaboración, producto curso, vino, que no, qué sé yo. ¿Dejaron de ver o Ah,

**Damian Fritzler LB**: Estamos viendo.

**Gabriel Puertas**: perdón,

**Damian Fritzler LB**: Perfecto.

**Gabriel Puertas**: perdón, perdón que me molesta este cartel se acá está definiendo, no sé por qué Clud alguna veces me cambia de idioma, pero digo, definiendo la mejor manera de asignar cada rubro contable y ahí les cuento un poquito más cómo funciona eh perod. Una vez que nosotros vinculamos todos los datos que funcionan, probablemente en esta primer corrida eh lleguemos a un a un punto bastante cercano, pero quizá haya particularidad de las bases de datos que no están no son explícitas o al menos el modelo no lo encuentran.

**Gabriel Puertas**: Supongamos que el que lo está usando es el y dice,"No, fíjate que no sé, el rubro aceituna a granel nosotros la vemos de tal o cual forma. se lo explica. Nosotros tenemos, digamos, ese tipo de conocimiento se se guarda en la herramienta. Vengo acá, lo vuelvo a Teram. Nosotros tenemos acá un campo que se llama knowledge. Acá ya incluso ya tenemos algo cargado, pero digo, acá se van cargando todo el conocimiento que que fue detectando el modelo respecto a las bases de datos, cómo están. Entonces, por ejemplo, el ejemplo que yo le daba, el ruro, aceituna, granel, se verifica así, no sé, la nota de crédito se cargan de esta forma, de aquella, qué sé yo, eso acá queda queda almacenado. Entonces, y esto es colaborativo, o sea, si Damián lo utiliza y él lo utiliza, este conocimiento lo comparten y se enriquece, digamos, con algunos usuarios tienen habilitado modificar este conocimiento y ese conocimiento es auditable, es no menor, porque eso, digamos, nos pasa que mucha gente encuentra valor en esto porque esto es esto es información muy útil para para explotar la información propia de Luigi Bosca y además hace que la herramienta mejore en en la medida que se usa y la gente contribuye a este conocimiento.

**Gabriel Puertas**: Eh, acá esto, Dami, es todo lo que nosotros habíamos encontrado de las iteraciones que que vimos con vos. Si si aparecen nueva nuevas cosas, se van a ir cargando. Eh, vamos a ver cómo viene esto. El David una compra de UA como crédito de la cuenta clave. No sé qué estar haciendo. Fíjense acá, descifrando la relación entre débitos, crédito y movimiento neto, redefiniendo las compras de UA como crédito de la cuenta clave. No sé, veremos cómo sale el que está haciendo Es está armando ya una tabla de solución. Nolis. Acá cargó algunos Nolis. Vamos a mir un poco la tabla de cuentas. Es un balance de cuentas de suma y saldo. Me lo sacó, ¿eh?

**Damian Fritzler LB**: Ahí te

**Gabriel Puertas**: Saldo de proveer. ¿Cómo se resolvió cada fila? Saldo de saldo final de las cuentas por pagar las provenciones comerciales. Invertido del signo excluí capex, anticipo del cliente y provisión en intereses financieros y gastos extraordinarios. No son no son deuda comercial operativa. Asumo que esto está bien, ¿no? Al menos a mí me hace sentido.

**Gabriel Puertas**: Compra del movimiento de las cuentas de resultado.

**Damian Fritzler LB**: con

**Gabriel Puertas**: Ojo con esto. Es el hallazgo importante. El ejercicio cierra en junio y ahí saldo final del resultado vuelve a cero. Si alguien arma esto con saldo en vez de movimiento, junio lo explota. Vamos bien ahí. DPO, saldo sobre promedio de compra de 12 meses por 30. Las cinco categorías salen del propio mapeo de vida que ya tienen cargado en el plan de cuentas vida, así que están en su idioma. Cox y producción de costos. Un supuesto que conviene plantear con ello. El mayor de proveedores está abierto por moneda y mercado, no por tipo de gasto. La única cuenta con tipo de gasto identificable es la 214 14, recepción de uva de tercero a liquidad. Va directo.

**Damian Fritzler LB**: Esa es la configuración que esa es parte de las

**Gabriel Puertas**: ¿Cómo?

**Damian Fritzler LB**: configuraciones que te falta, que las tengo en el Excel.

**Gabriel Puertas**: Ahí va, ahí va. Eh, bueno, el resto del pool lo pratic según la participación de cada categoría en las compras de los últimos meses. Es el criterio estándar, pero es un supuesto. Si ellos tienen el subsidiario de proveedores con clasificación de gasto, se reemplaza y queda exacto.

**Gabriel Puertas**: O sea, el uso un toma un criterio de prorrateo, ¿no? El número que les va a llamar la atención, publicidad entre 190 y 215 días de DPO contra 70 115 del resto. las provisiones de marketing y trading que se devengan mucho antes de liquidarse. También ajusté y vino. La compra de UA se capitaliza en inventario y no pasa por resultado, así que la tomé de los créditos. Con eso da 85 días coherente. Si lo tomaba de las cuentas de producción daba 1800 días, que es un artefacto. Acá lo que está haciendo con esto, nosotros volvemos a Teram, perdón, me pasé. Si yo vuelvo a Teramot, lo que está haciendo es una Bueno, ya la hizo. En realidad esta es la nueva, creo que es esta o esta de PO. Esta esta es la nueva tabla que armó en función de lo que nosotros le pedimos.

**Damian Fritzler LB**: No,

**Gabriel Puertas**: Eh, saldo de proveedores al cierre, compra del MIDI DPO por categoría de gasto mensual y último 24 meses. Acá, bueno, esto es como se ve la tabla en particular y acá es como una especie de de memoria de todo lo que hizo, ¿no?

**Gabriel Puertas**: Esto queda almacenado acá. Yo ahora lo que le voy a decir es a CL la tabla ya terminó. Veamos cómo quedó. Y parece unos resultados. Zoomiando. Acá si abrimos lo que está haciendo es explorando la tabla que acabamos de armar. O sea,

**Damian Fritzler LB**: No

**Gabriel Puertas**: para Fabi, nosotros teníamos fuente de información cruda,

**Damian Fritzler LB**: sé.

**Gabriel Puertas**: en realidad no es tan cruda porque viene del tabló que nos compartieron los chicos, o al menos lo mejor que pudimos. Analizó toda esa información, encontró todos esos detalles que que que acabamos de leer y armó una nueva tabla intentando atender al prom que le había pedido Eli. ¿Cuál es la particularidad de esa nueva tabla? Supongamos que Eli trabaja con esto y ter una dos veces hasta que llega al resultado final. Fíjate que es absolutamente el lenguaje natural. Una vez que eso queda, lo que nosotros armamos fue un ETL. O sea, yo todos los días voy a ir a buscar la información cruda, se va a ejecutar el código que nosotros armamos para generar esa nueva tabla y eso ahí ya no participan agentes. Una vez que yo ya armé eso, ese dato siempre es el mismo, ¿no es cierto?

**Gabriel Puertas**: que alguien decida, no sé, hacer una modificación o lo que sea. Eh, ahora una vez que él analice y vea, nosotros hagamos de cuenta que nosotros somos él y estamos iterando esto, una vez que llegamos a lo que querramos, nosotros además le podemos pedir, bueno, sobre esto armame un dashboard que sea así, así o asá. lo va a armar y lo publica enteramente y a partir de ahí ya lo miramos al dashboard todos los días actualizándose. Es un poco si querés la dinámica cuando queremos llegar al dash no podemos ver que se pueden hacer otras cosas, pero bueno, ahora lo dejamos está haciendo, ¿qué está haciendo ahora Cloud? está analizando si lo que construimos atiende a lo que necesitábamos y yo además le pedí alguno algunos resultados,

**Damian Fritzler LB**: Ok.

**Gabriel Puertas**: entonces estaba haciendo algunas inspecciones para darnos algunos insights. Se ve que me va. dar gráfico. Bueno, quedó lista. DPO de categoría por gastos, costo UA logística. No sé esos picos. Eh, les voy a aumentar un poco. No sé que les queda más cómodo. Si ustedes lo van leyendo, yo se lo bajo.

**Damian Fritzler LB**: A ver si voy a bajar un poquito más.

**Gabriel Puertas**: Vamos.

**Damian Fritzler LB**: Gracias por

**Gabriel Puertas**: Ay, no entendí esto. Tiene bendimia. salta de Ah, claro.

**Damian Fritzler LB**: la Claro.

**Gabriel Puertas**: Este es el periodo en que se perdón,

**Damian Fritzler LB**: estacionar la uva y y te juega ahí con el sombra de

**Gabriel Puertas**: para mí esto, para mí esto es muy nuevo,

**Damian Fritzler LB**: UA.

**Gabriel Puertas**: no es muy nuevo, pero sentido.

**Damian Fritzler LB**: Está muy bien porque tiene esa estacionalidad, o sea, es muy caracterí industria. Eso.

**Gabriel Puertas**: Una decisión de la fila de costos toma el COX nivel 51, el gasto de producción del nivel 52, insumo de etiquetado se debita y se asigna producción en curso dentro del mismo mes. Así que el movimiento neto es cero y no aparece.

**Damian Fritzler LB**: Una consulta de lo que vimos hasta simplificar de alguna manera.

**Gabriel Puertas**: Dale.

**Damian Fritzler LB**: y te lo te lo te lo pongo en mis palabras, digamos, no no soy técnico, pero digamos en definitiva, la lo que nos ofrece Teramot es la es la posibilidad de unificar en Teramot información que está contenida o alojada en distintos sistemas en la compañía y después desde ahí con toda esa información este si querés ahí centralizada en Teramod interactúa con agentes para bueno, para para armar la los dashboards o los o los reportes eh de información que nutriste con distintas fuentes en distintos sistema dentro de la compañía.

**Damian Fritzler LB**: tuviera que simplificarlo esencialmente es eso.

**Gabriel Puertas**: Sí, o sea, eso eso sí lo que podés hacer,

**Damian Fritzler LB**: No.

**Gabriel Puertas**: pero yo creo que el el valor más grande, o sea, yo ahora sí a él le digo, bueno, okay, okay, armemos un dash Oh. ener va a ir hasta ahí, pero para mí el valor, o sea, ¿qué es lo que pienso yo obviamente como como founder, no estoy convencido de esta idea? Es que lo que planteo es una forma nueva de trabajar. ¿Por qué? Porque nosotros hasta aquí nada, en estos minutos, no sé, llevamos 30 minutos de reunión, eh, armamos un dashboard con esto que pedían. Supongamos que le faltan datos, le quedan algunas iteraciones, pero bueno, nada, me comí una hora armando un das todo bien. ¿Cuál es la ventaja real de esto? Es que si vos tenés conectados los datos en Teramot, los tenés eh ya con la metadata, se puede saber, los entiende cómo utilizar. A partir de ahí tenés una inteligencia como como cloud, chaco, lo que sea que te ayuda. En ese sentido, una vez que yo armé el dashbor, yo puedo empezar a pedirle insight o planes de acción o cosas por el estilo.

**Gabriel Puertas**: Y si nosotros tomamos esa gimnasia, vas a ver que son muy atinados. de la misma forma que entendió todo eso. Hay muchos niveles de qué se puede hacer con eso, digamos, a partir de ahí más técnico, yo puedo empezar a hacer automatizaciones, puedo intentar hacer un modelo predictivo que me anticipe alguna cosa, pero incluso nosotros tenemos clientes que que hacen planes de venta o de negocio, que hacen ciertos análisis que que tienen que ver con flujo de caja, con mejores clientes, con lifetime value, con lo que sea. O sea, lo que nosotros ofrecemos es la posibilidad de incluir una inteligencia como la de como como la de estos agentes que conocen de prácticamente todo, eh utilizando datos reales de la empresa y pudiendo generar valor por ahí. Entonces, a mí lo que me pasa es nosotros vamos a llegar muy rápido a hacer un dash pero nada, como lo vemos acá, eso es algo que me ocupó una o dos horas, o sea, el verdadero valor a lo que viene después, ¿no? Es que yo tengo el dasho, eh, ¿por qué no puedo utilizarlo a cloud para definir cuáles son mis próximos planes de acción? ¿Cuál es mi mi planificación o algo? digo, dicho así, para mí lo que hay que hacer es probarlo en ese sentido, porque lo que sigue, creo yo, que es lo que realmente te da un valor de lo que nosotros estamos viendo con los clientes que lo usan, digamos, que que lo generan en ese sentido.

**Gabriel Puertas**: Nada,

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: tenemos CFO que que lo que hicieron es, no sé, cargan el el último reporte para el directorio basado en lo que hicieron, se lo dan a Claud y le dicen,"Che, bueno, armemos el próximo y tengamos", le arma todo el reportes, lo discuten y termina funcionando y eso es son dinámicas que toman una o

**Damian Fritzler LB**: No.

**Gabriel Puertas**: horas. Eh, yo creo que yo estoy convencido de que este tipo de herramienta plantea un cambio en la forma de trabajar. O sea, cuando uno se acostumbra a hacer esto, la velocidad, digamos, yo resuelvo muy rápido todo lo que es reporting, eh debería debería, digamos la dinámica de la empresa debería responder con los datos mucho más rápido y creo yo, tomar mejores decisiones porque en cierta forma están apalancadas por estos modelos.

**Damian Fritzler LB**: Los clientes que tenés, ¿cómo cómo protegen si querés la la confidencialidad de la información que que le mandan a la gente? Una vez lo abriste con la gente,

**Gabriel Puertas**: Mira,

**Damian Fritzler LB**: ¿hasta dónde lo puedes

**Gabriel Puertas**: ahí va lo que nosotros hacemos,

**Damian Fritzler LB**: controlar?

**Gabriel Puertas**: o sea, nuestra herramienta no requiere que Cloud se conecte a las bases de datos de Luigi Bosca.

**Gabriel Puertas**: Ese es básicamente no el secreto de Teramot, sino cómo se hace eso. Lo que hace Teramot es eh nosotros tenemos varias varios tipos de soluciones, pero creo que lo que veníamos hablando con Damián tiene más que ver con nosotros eventualmente podemos instalar a Teramot en la infraestructura de Luigi Bosca y que y que de esa forma Teramot corra en la infra de ustedes. Y cuando nosotros lo utilizamos de esta forma con cloud, lo único que le permite ver eh digamos Teramot a cloud es la estructura de las tablas, algunos preview y la metadata. O sea, le dice vos en la columna code tenés los datos, los gastos y todo ese tipo de cosas y obviamente acá vamos a ver los datos agregados. O sea, yo acá lo que hice fue contarle, no sé, lo primero que vieron en lo primero que vieron en agosto o este tipo de información agregada, eso sí se comparte con los agentes. todo lo que es la privacidad de la información, nosotros certificamos normas SOCs porque tenemos algunos clientes afuera que la requieren. Eh, y eso nada, tenemos todas las auditorías de seguridad y toda esa información. Lo importante acá es cómo interactúan los agentes con eso. Los agentes no tienen la capacidad de de que nosotros le pasemos toda la información y puedan puedan generar estos estos reportes.

**Gabriel Puertas**: Hay una cuestión técnica y hay una cuestión de privacidad. Entonces, por eso ahí justamente por eso es interesante el Teramot en ese sentido, ¿no? Acá lo que me hizo fue un un dashboard. Yo eventual creo que me

**Damian Fritzler LB**: No te seguí del todo, Dios.

**Gabriel Puertas**: está

**Damian Fritzler LB**: entiendo que obviamente si quieres me das eh Teramot tiene, a ver, para ponerlo simple está blindado el punto de vista de la seguridad de la información, ¿no?

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: Y eso ahí es la instancia entre el cliente y Teramot y después tenés la otra instancia que es entre Teramot y la

**Gabriel Puertas**: el

**Damian Fritzler LB**: gente.

**Gabriel Puertas**: sí.

**Damian Fritzler LB**: digo, tabla ahí con la gente, digo, siguiendo este ejemplo, toda la información que vos le pasaste recién para que arme el el este reporte días de pago por categoría, eso si querés salió de Teramot y digamos Yeah. esa información que está compartida con la gente

**Gabriel Puertas**: esa información está compartida,

**Damian Fritzler LB**: ya.

**Gabriel Puertas**: digamos, esa información cae en el acuerdo de confidencialidad con Cloud, eh, digamos que es información agregada, digamos, es como decir de esto, saldo de proveedores. En julio 2026 fue 11,289.

**Gabriel Puertas**: Esa información, digamos, entra dentro del compromiso de confidencialidad que que tendrían eventualmente con Cloud. Hay otra forma de utilizarlo que ya es más adentro, que es que vos digas, bueno, yo tengo un acuerdo particular con algún proveedor de modelo de inteligencia artificial, sea cual sea, y nosotros utilizamos esos tokens dentro de la herramienta de Teramot y ahí quedaría mucho más restringido. O sea, lo que yo te estoy mostrando acá tiene que ver con usaram con un con con con Cloud, que es un proveedor. Nada, nosotros tenemos un acuerdo eh tipo company, que es, digamos, distinta escala, pero el mismo acuerdo que no se puede llegar a tener Mercadoolbre eh con el con los compromisos confidencial, confidencialidad y y yo que sé que tengan firmado. La otra es que tengan un acuerdo o incluso hosteen un propio modelo adentro y utilizamos ese modelo para para generar todas estas soluciones. Ahí ya depende la capacidad de los modelos y todo ese tipo de cosas, pero bueno, nada, es una opción. Ahí Hugo quiere decir algo.

**Agustin Garcia**: No, iba a decir que bueno que como decías vos aplica digamos el el acuerdo de confidencialidad que haya con el LLM,

**Gabriel Puertas**: No.

**Agustin Garcia**: ¿no? Que en general todos eh se explícitamente informan que no entrenan sus modelos con la información que se gestiona.

**Agustin Garcia**: Ahora, digamos, este es el caso de Antropic porque estamos usando cloud. Si ustedes quisieran usar otro, digamos, ahí se valida cuál es el que se usa en cada caso, ¿no? Y lo que decía Gabriel básicamente es que también se puede usar un un Llía MCP, que sea vía la gente que nosotros tenemos y por detrás se podría conectar, digamos, el que ustedes quisieran utilizar si hubiese algún tipo de restricción por tema legal, No.

**Gabriel Puertas**: Y acá, bueno, nada,

**Damian Fritzler LB**: Okay,

**Gabriel Puertas**: acá publicamos el el dashboard y este dashboard queda

**Damian Fritzler LB**: Gabriel Agustín,

**Gabriel Puertas**: queda

**Damian Fritzler LB**: ¿no? Eh, ¿tiene alguna métrica del uso de de tokens a nivel dinero de algún

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: cliente parecido a Luigi Bosca para entender un poquito el consumo?

**Agustin Garcia**: Mira,

**Gabriel Puertas**: mira,

**Agustin Garcia**: yo métrica,

**Gabriel Puertas**: ahí

**Agustin Garcia**: no sé, Gabi,

**Gabriel Puertas**: está.

**Agustin Garcia**: vos después complemente. métrica métrica no tenemos la la situación es la siguiente, digamos, eh por así decirlo, digamos los LLM, más allá de los acuerdos enterprise que hayan, ¿sí? M. En general, cuando el consumo no es grande, digamos que tu paquete de usuarios no es, digamos, que no no te obligue a ir al enterprise, usas la versión desktop.

**Agustin Garcia**: La versión desktop tiene el consumo de token, por así decirlo, subsidiado. ¿Qué te quiero decir con esto? Que el consumo es más barato que si vas por una piquit. Sí. Entonces, ¿por qué te digo esto? Porque la realidad es que nosotros tenemos clientes que lo usan fuertemente en este escenario y no tenemos tampoco, digamos, e reclamo de que el consumo es excesivo. ¿Sí? ¿Por qué? Porque en general vos en los esquemas tradicionales o el básico, vos tenés planes y el plan es de $20 por se o en cloud el siguiente es de $100, ¿no? Entonces para un usuario eh regular hoy en día con el plan de $ la verdad que alcanza y a vos te da previsibilidad. Y lo que estamos viendo también en los clientes es que dentro de los usuarios seguramente que hay algún heavy user que le dé, digamos, bastante más fuerte que el resto y que tal vez en esos casos se aplica un plan de $100. Pero bueno, también, ¿por qué se da esto? Porque también digamos que es un poco la ventaja que tiene Teram, ¿no? O sea, está pensado y está diseñado para ser eficiente en término de la comunicación que hay con el Ll.

**Agustin Garcia**: Entonces, si vos lo comparás contra un conector de, como por ejemplo el de Sup Base, el de Sup Base, eh,

**Damian Fritzler LB**: Dos.

**Agustin Garcia**: te deja te limpia los tokens rápidamente porque el conector no es tan eficiente, ¿no? Entonces esa es un poco la ventaja también, pero hoy nosotros los clientes que tenemos que no son enterprise, digamos, que no tienen planes Enterprise, en general, eh los usuarios comunes usan planes de 20 y algún heavy user plan de $100.

**Damian Fritzler LB**: Para entenderte bien, yo quiero usar el el agente que ofrecen ustedes derecho a la plataforma.

**Agustin Garcia**: Sí.

**Damian Fritzler LB**: Debo licenciarlo para que toda la empresa tenga acceso a los datos.

**Agustin Garcia**: Mira, eh nosotros la gente que tenemos hoy embebido es un LLM, digamos que tiene bastante capacidad y permite hacer bastantes cosas, pero no puedes hacer un análisis como el que acabamos de hacer. Sí, está pensado para que sea eh digamos un chat with your data, ¿sí? para que puedas hacer alguna gestión de datos sobre las tablas existentes, algún merge, alguna limpieza depuración, algún digamos algo más relacionado a gestión de datos, digamos. Pero es hoy como lo tenemos nosotros empaquetado.

**Gabriel Puertas**: F.

**Agustin Garcia**: Si vos me decís, mira, la verdad que nosotros por algún motivo no queremos ir por el modelo del cual vamos a conectar por el MCP, no hay ningún problema.

**Agustin Garcia**: Podemos ir o poner el modelo que ustedes quieran. Suponete que vos tenés una negociación particular con chatt. Nosotros podríamos conectarlo directamente atrás para que quede como el motor detrás de de la gente. ente conversacional. Sí. Y la negociación puede ser tuya. Básicamente lo que vas a ver es que, digamos, eh lo que podemos identificar es la cantidad de golpes que le da eh un usuario, porque nosotros también por la certificación de seguridad que tenemos no llegamos a a poder ver qué hace cada usuario, ¿se entiende? Pero sí, tal vez podamos ver el el volumen de consumo. Ahí corregime, Gabi, si si estoy diciendo

**Gabriel Puertas**: No, no es tal cual. Yo lo que le iba a decir a Dami es yo si querés puedo armar un, o sea, decir digamos con con la pisky nuestra, ¿no? Es decir, intentamos hacer este mismo caminito, ahí en la API Key ya entra, bueno, qué modelo y y el proveedor, ¿no? Porque tienen distintos costos, pero digo, agarrar un un modelo y decir, bueno, hice todo este camino y ver cuánto costó. Es importante ahí lo que dice Agustín, digamos, hoy el mercado de de los grandes proveedores del LM tienen como dos niveles de servicio o dos formas de consumirlo.

**Gabriel Puertas**: Una es con con las aplicaciones y otra es vía API, o sea, yo llamo al servidor y resuelvo el el consumo, o sea, la intención o todo el mundo dice que la intención con con la con la aplicación, como yo les mostré, es masificar, es mostrar lo que se puede hacer con estos modelos. Entonces, el costo es muy acotado, incluso creo yo que es el momento en en el cual hay que empezar a usar, porque eso es lo que nos tiene que generar el criterio de cómo y cuándo utilizarlo, ¿no? El el servicio que es tipo API Key es a a igualdad de modelo es mucho más caro. Eso te va a llamar la atención, digamos. ¿Qué es lo que creo yo? Nosotros hoy nos juntamos con con gente de Mercado Pago y lo que lo que ellos dicen, o sea, el criterio que tienen ellos como compañía es decir,"Bueno, yo voy a tener un acuerdo con todo mi uso, pero nada, están super convencidos que la gente tiene que utilizar eh estos modelos y lo que tienen son acuerdos de se obviamente un poco más bajo a la escala de ello, ¿no? Pero digo, ¿cuál es la ventaja de eso? que esos seats vos ya los controlas de antemano porque loss tienen límites por hora, por semana y por mes.

**Gabriel Puertas**: Y vos sabés que cada persona consume lo que vos definiste que consuma, sean $ en 100 o si vos a algún usuario le permitís que exceda, se lo das. Y hoy esa es la forma eh más económica. Dicho eso, Dami, te repito, yo nos podemos poner de acuerdo que sí. Nada, probemos esto con la API de Sonet 5 y yo digamos hago todo este camino que hicimos, intento llegar a los mismos resultados y te digo,"Mira, esto hubiese costado tanto. M.

**Damian Fritzler LB**: M.

**Gabriel Puertas**: Eh, eso puede

**Damian Fritzler LB**: atrás porque tengo formación financiera,

**Gabriel Puertas**: ser.

**Damian Fritzler LB**: no técnica, digamos, no tecnológica, pero digo para no te seguir del todo con la segunda alternativa, una me queda claro que es usar la aplicación que sería digamos ponte,

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: la otra cuál sería no tener la aplicación y que en definitiva el agente conviva directamente con todos los

**Gabriel Puertas**: la otra.

**Damian Fritzler LB**: sistemas donde tengo que son repositorio de datos que necesito para para armar reportes.

**Gabriel Puertas**: Claro. La otra, la otra sería de esta forma. Eh, vos podés utilizar un modelo de esto eh haciendo llamadas tuyas directamente al servidor de de en este caso eh Antropic, que es el que provee los modelos de de cloud como el que yo utilicé acá.

**Gabriel Puertas**: Eso, ¿qué quiere decir? Yo le mando cada una de las interacciones con con una API Key. Esa API Key es como una es como una llave, de hecho es que que me permite que identifica quién es el usuario y impacta el consumo de los tokens, ¿no? Es básicamente la misma interacción que tuvimos ahora, solo que vos la hacés desde tu entorno privado. Yo te lo podría poner acá, perdón, yo lo podría poner acá. Yo tengo acá un agente. Yo configuro la AP key de ustedes y ustedes lo usan acá. Dicen,"Hola, estoy es lo mismo. Todo lo que nosotros estábamos hablando acá. Solo que los consumos de esto los pagan con su servicio que tenían contratado con con COS." ¿Cuál es la diferencia? Realmente no hay mucha diferencia a nivel tecnológico ni nada por el estilo, solo que los precios que imponen esos proveedores a los dos tipos de consumo están son diferentes. ¿Qué pasa? Ni este ni el consumo de API es tan caro, ni el consumo de vía la aplicación es tan barato. Solo que hoy como están intentando masificar el consumo de de las de los modelos, eh se ofrece de esa forma. Es como que este subvenciona un poco el de los el de el B2C, digamos, porque el el que yo te mostraba es B2C.

**Gabriel Puertas**: Me bajo la aplicación, paso la tarjeta $ y tengo fijo un uso y eso me permite a mí elegir el modelo. Si yo elijo modelo más caro, me gasto mi cuota más rápido y si no, no. El otro es directamente yo llamo y cada vez que llamo me cuenta y voy acumulando el gasto. No sé si fui claro. Es es son como dos formas de consumir lo mismo, digamos. Básicamente el Pero también lo podemos hacer.

**Damian Fritzler LB**: Okay.

**Gabriel Puertas**: Nosotros tenemos empresas que no sé es muy vario pinto. Entonces nuestra nuestra estrategia es poder absorber todos. O sea, yo creo que hoy por hoy todas las empresas tienen que tener un criterio de cómo van a cómo van a consumir inteligencia artificial, cómo cómo van a decidir utilizar esos tokens. está la privacidad, que obviamente es muy importante. Y después los costos. Tenemos empresas que incluso pagan AWS, por ejemplo, te permite eh hostear tus propios modelos. O sea, vos alquilás ese servicio de procesamiento y decís,"Bueno, yo voy a tener acá corriendo un modelo tal que ese es tuyo, ya no es de Antropic, pero vos pagas el servicio de costearlo y nosotros le pegamos a ese modelo y lo consumimos. Otras personas, como dice Agus, tienen otr otras empresas tienen acuerdos con con Openea y con Gemin y con el que sea, dicen,"Bueno, mira, yo ya tengo este acuerdo con este proveedor porque tengo la suit de Google, porque tengo no sé qué.

**Gabriel Puertas**: Eh, yo quiero que utilicemos estos modelos." Bueno, listo, nosotros te conectamos con esos modelos y vos utilizas esos tokens para hacer lo que hicimos ahora. O hay hay empresas que no son de base tecnológica que están entrando en esto y dicen,"Bueno, ¿cómo es la mejor forma para empezar?" Yo creo que la mejor forma para empresar es definir las personas que lo usan, darle tener un una cuenta company en uno de estos proveedores. Hoy por hoy el que mejor funciona es Cloud, pero eso es eso es muy cambiante en el tiempo. Eh, tener una cuenta de esa con x persona, uno acota el gasto y y lo consumen ahí y y van entendiendo cuál es el valor que aporta de ese lugar, ¿no? Y ahí uno, a mí lo que me parece que tiene mucho sentido es que vos acotás el gasto, o sea, sabes que no le estás dando un cheque en blanco por el uso de de los tokens, ¿no? Y y nada, ahí yo, o sea, esta cuenta, lo que nosotros hicimos está, bueno, acá no lo veo, pero digo, esta es una cuenta, sí, esta es la cuenta de Teramot, que el S mío son 5 y yo raramente llego a superar el límite mensual, alguna vez el límite diario,

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: sí, pero nada, tengo que esperar unas horas y lo puedo volver a usar,

**Damian Fritzler LB**: Okay.

**Gabriel Puertas**: digamos.

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: Pero pero bueno,

**Damian Fritzler LB**: Ok.

**Gabriel Puertas**: nada, si esa ese tipo de cuenta, yo creo que digamos por por el tema seguridad es nada. A mí me parece que los términos y condiciones respecto a las cuando uno utiliza eh los LLM de esa forma, Antropic, todo eso, tienen contrato de confidencialidad que son muy fuertes respecto a que no utilizan esa información para entrenar sus propios modelos. Yo tiendo a pensar que eso es cierto porque porque si no se quedan sin negocio. O sea, si de repente la gente que usa que que confía en esa información resulta que lo usan para otra cosa, es como pierden el negocio. Pero bueno, nada. La verdad es que cuando uno contrata esos servicios, eh, está está, digamos, está protegido por ese contrato de confidencialidad,

**Damian Fritzler LB**: Está claro. Okay.

**Gabriel Puertas**: No.

**Damian Fritzler LB**: ¿Quieres hacer alguna pregunta al modelo de cara algún dato específico de julio muy puntual? No, no, no digamos si querés encia no no me interesa tanto, ¿viste? ir al detalle de la consistencia de de los datos y demás, sino entender un poquito más globalmente el modelo y el beneficio que tiene la la herramienta.

**Damian Fritzler LB**: Tal cual. Pensá que esto nosotros lo vimos la base cruda, pero vimos con la cabeza. No hubo nadie que interprete el modelo de información así como la base de datos de árbol que usa Mati, que lo mismo con el Excel y demás. Está la compción fiscal en Tendela. relación y ese es un poco el valorable resolver y después te generes ahí. Pero

**Gabriel Puertas**: el y ahí hay nosotros eh tenemos como una especie de cle nosotros sabemos que nuestro producto es muy nuevo, o sea, como que nosotros estamos muy early, ¿no? Entonces nosotros tenemos como una especie de clínica de acompañamiento en este sentido, porque pues nos interesa eso, digamos, que que uno entienda el valor. Con esto uno puede decir, bueno, yo puedo configurar un sistema de alerta que que nada que mire stock y y alerte a ciertas personas, pero con inteligencia, o sea, no simplemente un umbral y disparo, sino que cuando pasa esto, esto, esto, esto, eh digo, bueno, tengo que mandar este correo explicando la situación y haciéndolo o incluso ciertas transacciones o cosas por el estilo y nada, tienen Lo que a nosotros más nos funciona en esas clínicas es fomentar el uso de esta herramienta haciendo estrategias comerciales o financieras, no sé.

**Agustin Garcia**: Claro, ahí un poco digamos que el producto también va acompañado del servicio de parte del equipo de Customer Success,

**Gabriel Puertas**: Eh

**Agustin Garcia**: que básicamente lo que hace es ayudarlos a ustedes a ganar adopción y para que eso ocurra básicamente ustedes tienen que poder empezar a atacar casos de uso puntuales y resolverlos. Entonces, ¿qué te quiero decir con esto? Digamos, el servicio no tiene el objetivo de generar una permanencia, al contrario, tiene el objetivo de poder transferir el conocimiento, ayudarlos con cada una de las situaciones que tengan que enfrentar para que, digamos, rápidamente ustedes puedan empezar a ganar eficiencia y productividad aplicando la tecnología que que les ofrecemos, ¿entiendes? Ahora, como decía eh Gabriel, sabemos que es nuevo, sabemos que a priori es difícil tal vez eh eh bien, vos ves que pasan las líneas, Pero no no no queda muy claro. Entonces, cuando te acompañe alguien del equipo, digamos, eh nada, es mucho más fácil eh implementar, hacer un dashboard, validar los datos, saber de dónde viene la info, toda la información, todo lo que usa queda eh trackada eh en logs, entonces digamos que es fácil la trazabilidad eh como para poder validar. Entonces, pero bueno, para eso también está el servicio que que acompaña el producto de acompañamiento,

**Damian Fritzler LB**: Austín Gabriel, tengo Una duda que no sé si la habíamos visto antes,

**Gabriel Puertas**: Dale.

**Agustin Garcia**: ¿no?

**Damian Fritzler LB**: nosotros tenemos información,

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: obviamente toda la base de datos, pero no queremos que todos los usuarios vean toda la información. Entonces, ¿dónde seteo acá a nivel columna?

**Gabriel Puertas**: a ver,

**Agustin Garcia**: Lo te lo contesto rápido.

**Gabriel Puertas**: vamos.

**Agustin Garcia**: Nosotros tenemos un esquema de Word Spex y Proyecto que está pensado para eso mismo y

**Damian Fritzler LB**: Eh

**Agustin Garcia**: obviamente que al momento de iniciar empezar a trabajar con nosotros, este equipo de customer sucessa con ustedes para empezar a diagramar cómo va a ser, digamos, esa estrategia para, digamos, plantear los esquemas que corresponden y después vos poder ir moviendo la información en función de eh las necesidades. Obviamente que no toda la empresa tiene que ver toda la información y por eso está pensado ese esquema, ¿no? Entonces, cuando vos vas a mirar ciertos dashboard, van a vas a ver solo los dashboard que vos tengas acceso. Cuando vas a conversar con tus datos, vas a conversar solo con los datos que vos podés acceder, no con todo. ¿Se entiende? Entonces

**Damian Fritzler LB**: Lo que quiero entender es quién tiene la capacidad de agregar información al modelo. No sé si es por roles,

**Gabriel Puertas**: Est muy bien.

**Agustin Garcia**: hay

**Gabriel Puertas**: Claro. Alelo. Fíjate,

**Agustin Garcia**: roll.

**Damian Fritzler LB**: eh.

**Gabriel Puertas**: yo acá en este estoy yo como owner. El owner es como el superusuario, ese el owner puede hacer prácticamente todo, incluso el que tiene la potestad de borrar. O sea, yo puedo borrar el Wordface y eso hace que desaparezca toda la información de de Luigi Bosca de que está almacenada enamor eso es hasta normativo. El owner, además, bueno, este no porque está en el free, pero digo, yo puedo agregar, vamos ver acá, yo puedo agregar distintos roles que eso, digamos, son roles que te permiten niveles de edición, niveles de de vista y todo más. Entonces, supongamos que vos se lo das,

**Damian Fritzler LB**: Gracias,

**Gabriel Puertas**: vamos, un caso concreto. Supongamos que, uy, perdón, me fui de dónde estoy acá.

**Agustin Garcia**: Chicos, perdón,

**Gabriel Puertas**: Supongamos que vos se lo das.

**Agustin Garcia**: porque tengo otra reunión,

**Gabriel Puertas**: Dale, dale, dale.

**Agustin Garcia**: pero después Gracias,

**Gabriel Puertas**: Yo me aco con eso.

**Agustin Garcia**: disculpen. No.

**Gabriel Puertas**: Dale, Agus.

**Damian Fritzler LB**: Adiós.

**Gabriel Puertas**: Eh, suponte que armamos el caso de vos sos owner de todo el Wordpace y armamos el caso de, no sé, recurso humano.

**Gabriel Puertas**: un tema sensible, agarrar recursos humanos, vincular los datos y decís,"Bueno, yo creo este caso y pero a Me interesa que la persona de recursos humano que va a usar

**Damian Fritzler LB**: Oh. Yeah.

**Gabriel Puertas**: esto eh vea todos los suelos que soo, pero de los directivos no, por decirte, no sé, una cosa así. Vos podés crear un proyecto donde eliminás esas filas directamente y esa eso es una tabla nueva. Entonces ahí vas y generas otro proyecto que se le le das como fuente de información a ese proyecto la

**Damian Fritzler LB**: Filas.

**Gabriel Puertas**: tabla que vos habías configurado. Es decir, yo armé un proyecto donde eliminé las personas que no quiero que aparezcan. genero otro proyecto para la persona de recursos humanos. Le digo,"Mira, esta es tu fuente de información. Acá aparecen están todos los sueldos de la compañía. Vos sos recursos recursos humanos, eso lo podés ver, pero no están filtrados los la los registros que vos no querés." O sea, todo esto apela a que hay una persona con el suficiente ownership para para decir quién puede ver y qué cosa, ¿no? O sea, porque obviamente el modelo en sí no lo no lo tiene, pero eso está hecho. Y después, digamos, eh a futuro la idea es eh configurar eso a nivel conector, o sea, que vos puedas decir esta tabla, la persona, esto es más técnico, ¿no?

**Gabriel Puertas**: digo, la persona que vincula una base de datos eventualmente va a poder decidir qué columnas si entran a Teramot y hasta qué filas pueden o no entrar a Teramot. Obviamente que es una conexión mucho más eh técnica, pero eventualmente lo podes hacer. Si eso pasa directamente esa información que vos eliminaste eh no entra no entra no entra como como transferencia de información incluso dentro de la versión que que se depla en la infra de ustedes, ¿no?

**Damian Fritzler LB**: Okay, después si lo vamos más en detalle algo.

**Gabriel Puertas**: Claro, esto tiene el Ay,

**Damian Fritzler LB**: Yo parte tengo que No,

**Gabriel Puertas**: perdón,

**Damian Fritzler LB**: no. Sí,

**Gabriel Puertas**: no te iba a decir que tiene el mismo el mismo criterio de la industria.

**Damian Fritzler LB**: Gabi,

**Gabriel Puertas**: O sea, si vos mirá Ghub tiene una lógica muy parecida a eso, digamos, los roles de usuario y permiso de edición y tipo de cosas.

**Damian Fritzler LB**: después nos juntamos si te hago algunas preguntas que cómo poder intentaricarlo.

**Gabriel Puertas**: Sí, de una,

**Damian Fritzler LB**: No quiero ahora indagar en

**Gabriel Puertas**: Dami, y si querés pasame. Yo yo puedo intentar interpretar ese Excel y subírtelo como como estaba yo ahora.

**Damian Fritzler LB**: estos

**Gabriel Puertas**: Ah, espera, vamos a hacer eso porque esto esto estaría bueno que que lo empiece a utilizar alguien de ustedes, ¿eh?

**Damian Fritzler LB**: lo que podemos hacer es me gustaría sumarla y quiz la semana que

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: ¿Cuándo? de vacaciones que me gustaría que participe, que tiene los datos bien frescos. Yeah. y que sí ahí siga haciendo un doble sobre el dato e y quizás agendar para la

**Gabriel Puertas**: Dale.

**Damian Fritzler LB**: semana que viene y y vemos lo de la seguridad y la estructuración del tablero, ¿te

**Gabriel Puertas**: Sí, dale de una. Mira,

**Damian Fritzler LB**: parece?

**Gabriel Puertas**: yo acabo de configurar para que esto se actualice todos los días a las 5 de la mañana. O sea, yo a las 5 de la mañana voy ahí a mirar la base de datos de ustedes, me voy a traer la actualización, eh, te subo te subo el Excel y nada, si hoy no tienen una licencia de cloud o algo así para para usar, nada, hacemos reuniones con Eli y lo hacemos juntos.

**Damian Fritzler LB**: Okay,

**Gabriel Puertas**: pasa nada.

**Damian Fritzler LB**: perfecto, David. Eh, después la última para revisar con con Agustín. Ahí vi los modelos de licenciamientos. ¿Hay algún intermedio en lo que podamos pasar de uno?

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: Gracias.

**Gabriel Puertas**: perdón, a mí a mí a mí me suelen retar cuando hablo de estas cosas,

**Damian Fritzler LB**: Gracias

**Gabriel Puertas**: pero te diría que no hay nadie que esté utilizando estrictamente el tiro. Están todos en

**Damian Fritzler LB**: porque a ver qué pasa.

**Gabriel Puertas**: intermedio.

**Damian Fritzler LB**: No voy a necesitar algo tan fuerte como el modelo de los 000 ni tampoco me necesito el de 400.

**Gabriel Puertas**: Sí, sí, sí.

**Damian Fritzler LB**: ¿Crees que se puede hacer intermedio para llegar ahí?

**Gabriel Puertas**: Sí, sí, sin duda, sin duda. Hablas con él. Pero eso es lo que te digo, Dami. No hay nadie que esté estrictamente en uno o en otro. Están todos en el en el medio, digamos.

**Damian Fritzler LB**: Impecable.

**Gabriel Puertas**: No le digas que te dije

**Damian Fritzler LB**: No, no, no. Obvio.

**Gabriel Puertas**: esto.

**Damian Fritzler LB**: Gabi, hagamos esto. Yo te mando ahora hablo con Eli y vemos de agendar un espacio chiquito la semana que viene.

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: ¿Te

**Gabriel Puertas**: sí, que eh sí que me escriba directo si está ella sola y se perdió,

**Damian Fritzler LB**: parece?

**Gabriel Puertas**: lo quiere ver. Ya mañana lo vamos a tener actualizado, eh, yo subo el Excel y lo vemos junto con ella. A mí me interesa porque ella va a ser la usuaria que ya que lo va a

**Damian Fritzler LB**: A mí lo que me interesa que ella tome el tiempo de lo mismo que hoy le lleva a hacerlo,

**Gabriel Puertas**: entender.

**Damian Fritzler LB**: dos tr horas. A ver cuánto le lleva

**Gabriel Puertas**: Ah, sí, sí, sí.

**Damian Fritzler LB**: hacerlo.

**Gabriel Puertas**: Incluso la clave, perdón Dami que te estoy robando el tiempo, la clave es le va a tomar menos tiempo, pero ya va a quedar hecho. O sea, esto se le va a actualizar todos los

**Damian Fritzler LB**: Sí. Totalmente, totalmente.

**Gabriel Puertas**: días.

**Damian Fritzler LB**: A ver, e yo quiero mostrar acá un poquito eso lo que a ver, voy con lo que te decía antes, eh, tenemos que tenemos que ver que vamos a hacer también con con lo de la gente. Por eso lo que te preguntaba antes de un modelo interno y se lo preguntaba Agustín, sin la necesidad de tener que licenciárselo a cada usuario. pensar que hoy la reportería de nuestros sistemas es tan mala que sí o sí necesito eh la licencia de de tablo, pero no sé si quiero licenciar a todo el mundo con inteligencia artificial.

**Damian Fritzler LB**: Me ese es el

**Gabriel Puertas**: No, no, mira,

**Damian Fritzler LB**: tema.

**Gabriel Puertas**: con esto, o sea, vos tenés distintos tipos de usuario. ¿Qué va? Porque por ahí se mezcla un poco. Eh, vos consumís tokens con Teramot. solamente el que construye soluciones, no el que consume.

**Damian Fritzler LB**: No, ya lo sé, pero necesito igual Tak. de cloud para consultar los datos o

**Gabriel Puertas**: Eh, claro. Ve ahí va lo que lo que decía.

**Damian Fritzler LB**: no.

**Gabriel Puertas**: Nosotros podemos porque el tema es así. Acá acá fíjate, la gente de Teramo tiene Cloud Sonet 5. Para mí es un modelo es un modelo muy bueno que hace que te dure bastante la licencia.

**Damian Fritzler LB**: Sí.

**Gabriel Puertas**: No es el mejor que tiene Clover hoy por hoy. Y voy a hacer más concreto porque me pongo a hablar de esto y se me va. Vos podés hacer que este tipo de agente sirva para a ver, pero vamos a hacer una nueva conversación que vos le digas, no sé, cómo viene, cómo vienen las ventas en el último mes. No sé, una cosa así. Yo acá no estoy armando una tabla, no estoy armando un dashboard.

**Gabriel Puertas**: Estoy consultando sobre tablas que ya están hechas nada más. Eso técnicamente consume menos y un uso eh bastante más acotado. Porque, ¿qué pasa? Es raro que la gente esté todo el tiempo preguntando. Mi opinión personal es que el chat eso es lo que Agustín le llama el chat within your data, esto de decir, decime cómo viene la venta, fíjate como coso, eso consume poco y creo yo que tiene bastante poco valor. Es lo que es lo que están ofreciendo todas las herramientas tipo Power BI, te ponen un chat al lado que conversan. Eso no suma mucho. El que realmente suma es el que el que vos utilizás para para construir esas tabla. Que vos digas,"Che, necesito necesito que revises todo."

**Damian Fritzler LB**: Pero por eso vos pon que esos que construyen los uso con con cloud y lo pongo a Mat y lo pongo a él y lo pongo a cuatro o cinco usuarios claves para crear la información que el resto de la compañía compía

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: va a consumir cómo y desde la consuma el resto de la compañía desde acá,

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: desde este agente de Teram, sin necesitar licenciamiento del

**Gabriel Puertas**: claro,

**Damian Fritzler LB**: cloud.

**Gabriel Puertas**: en este lo que podemos hacer es eso, digamos, el resto de la compañía vosotros lo que tenemos puesto acá es que vos tengas publicado estos estos dashboard.

**Gabriel Puertas**: Ahí reemplazaste tabló porque para supongamos que este es el dashw que a ustedes les gustó,

**Damian Fritzler LB**: Claro,

**Gabriel Puertas**: ¿no?

**Damian Fritzler LB**: pon que eso.

**Gabriel Puertas**: Eh, no va a ser, pero esto ya está. Voy a agarrar los tienen publicados e acá y nada, si ustedes cargan los usuarios read only, esa persona lo único que hace es puede entrar todos los días. Este este dashboard está se actualiza, entra y mira, lo consume, qué sé yo, lo mismo que te habló, solo que eso esos usuarios no cuestan lo mismo que los otros.

**Damian Fritzler LB**: Sí.

**Gabriel Puertas**: Esos usuarios no consumen token, es lo único que hacen, entran todos los días, incluso podés refrescar, qué s yo, y y te fijas.

**Damian Fritzler LB**: Ok.

**Gabriel Puertas**: Esto replicamos exactamente lo que ustedes tienen en tabló y ahí ya lo tiene todo el mundo. Después hay otro usuario que vos decís,"Che, yo tengo consumidores de dashward que muchas veces responden preguntas sobre esos dash o arman reporte, qué sé yo." A eso le podemos dar acceso a este chat. Ese obviamente esos tokens se consumen, pero ahí hacen un acuerdo de límite, qué s no sé a este chat que lo que hace es, perdón, chatear con con esos das lec che, bueno, fíjate el dashor tal, decme cómo viene, ayudame así un mail para la dirección que le reporte y qué s yo.

**Gabriel Puertas**: Ese ese es el usuario

**Damian Fritzler LB**: y Gabi.

**Gabriel Puertas**: chat.

**Damian Fritzler LB**: Perfecto. Ahora, en este agente le puedo sumar, por ejemplo, un archivo que yo tengo de una consultora que me mandó sin necesidad, porque yo lo único necesito es que me lo me lo analice para este momento, sin necesidad de pasar por cloud.

**Gabriel Puertas**: Sí, sí, sí se puede hacer. Ahora nosotros lo tenemos como imagen o qué sé yo, pero sí sí se debería poder hacer

**Damian Fritzler LB**: Yo lo que tengo que llegar y hablando acá con Fabi es que el costo a mí de implementar Teram sea mejor del costo que yo hoy tengo con Tablo, fuera de todo el valor agregado que me da, porque quiero ir al modelo de Teram. Sí.

**Gabriel Puertas**: Está

**Damian Fritzler LB**: Ahora, la pregunta que me haces es, ¿por qué voy a Teramont y no voy a otro lado? ¿Porque no lo desarrollo inhouse? Porque bueno,

**Gabriel Puertas**: No.

**Damian Fritzler LB**: entonces por qué obviamente tiene un montón de respuestas teóricas y lógicas de ya está estructurado, hay un equipo atrás, el acompañamiento, el desarrollo, el prove error y demás, pero yendo al valor en el tiempo, porque quiero que sea un proyecto en el cual me quedé enterado, no lo usé únicamente para la adopción de la gente y después me muis lo que digo

**Gabriel Puertas**: Sií, si, sin duda. Pero espera, hoy o yo estoy hace mucho que no me yo ya saqué la licencia del tabló. Eh, hoy hoy vos no tenés la posibilidad de vincular tabló con, por ejemplo, el informe que te tiró la consultora y analizarlo. Ahí va.

**Damian Fritzler LB**: No,

**Gabriel Puertas**: Eh, y ese y ese tipo de análisis, ¿vo esperar que sea un usuario tipo que que consumiría este chat?

**Damian Fritzler LB**: claro.

**Gabriel Puertas**: ¿Está bien?

**Damian Fritzler LB**: Yo lo que no quiero es tener que poner licenciamiento de cloud a cada uno de los usuarios.

**Gabriel Puertas**: Y

**Damian Fritzler LB**: Ahí es donde se me va el número a la m*****. O estoy pagando ya de cloud más de lo que pago por por

**Gabriel Puertas**: claro, lo que pasa, bueno,

**Damian Fritzler LB**: tablo.

**Gabriel Puertas**: lo que pasa que esos usuarios que van a hacer ese análisis consumen tokens,

**Damian Fritzler LB**: Está bien,

**Gabriel Puertas**: esos tokens

**Damian Fritzler LB**: pero no pasa nada. Pero los token es termina siendo, como decís vos, es ocasional, no van a estar todo el tiempo cruzando información, pero sí lo que yo quiero es que poner este este

**Gabriel Puertas**: H

**Damian Fritzler LB**: usuario, no sé, a esto que que pusiste acá es Okay.

**Damian Fritzler LB**: cómo debiese impagar impactar mis días de pagos si incremento la producción en un 20% en mis exportaciones. No sé. Entonces,

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: esos escenarios sí me gustaría que los puedan resolver desde acá.

**Gabriel Puertas**: sí. Ahí yo tengo duda,

**Damian Fritzler LB**: seis

**Gabriel Puertas**: es cuánto, cuánto costaría ese tipo de análisis utilizando estos estos modelos, porque digamos vos implícitamente estás asumiendo que eso porque nosotros en este caso lo único

**Damian Fritzler LB**: congradísimo,

**Gabriel Puertas**: que estamos haciendo es ser broker de tokens, o sea, nosotros, o sea, no lo pagas vos, yo te lo paso, digamos, no es lo mismo.

**Damian Fritzler LB**: No,

**Gabriel Puertas**: Poniéndome en tu lugar, necesitamos analizar eso, digamos. ¿Cuánto consume en costo ese ese

**Damian Fritzler LB**: por eso, por eso, por eso yo te preguntaba si tenés el costo promedio más o menos de una empresa parecida a Luigi

**Gabriel Puertas**: modelo?

**Damian Fritzler LB**: 2 150 usuarios, 100 usuarios. poner 100 usuarios del tabló que hagan uso de información donde

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: tengas equipos estratégicos, comerciales, de planificación, que ellos van a usar más quizás tokens que un usuario de gestión o de administración.

**Gabriel Puertas**: Claro.

**Damian Fritzler LB**: Entonces, eh con lo de los dashw, listo, ya estoy al mismo nivel, pero ahí lo que me pasa es que tabló lo están incluyendo en Slack y Slack me da servicios de ll distintas empresas inituando una única licencia. A m que me dicen comprar SL y ya viene con tabló y las Llm SL es lo que es

**Gabriel Puertas**: Es la mensajería.

**Damian Fritzler LB**: Teams para Microsoft.

**Gabriel Puertas**: No, no, nosotros usamos Slack, pero te digo, no, no, pero no vas a poder hacer eso, análisis,

**Damian Fritzler LB**: No voy a hacer estos análisis.

**Gabriel Puertas**: eh.

**Damian Fritzler LB**: Yo estoy de acuerdo, no voy a hacer esto análisis, pero no así directamente, depende del modelo. Hay modelos de Slack que usa, hay Slack que tienen modelos de Cloud y de Chat GPT que no te lo van a hacer a este nivel, pero que me incluyen todo el licenciamiento. Entonces, lo que digo es, ¿cómo debo estructurar la licencia de mis usuarios para optimizar el uso de los tokens y no tener que pagar licenciamiento para cada uno de ellos?

**Gabriel Puertas**: Pero sí,

**Damian Fritzler LB**: Lo que digo porque lo que usa únicamente como hub de

**Gabriel Puertas**: sí, sí.

**Damian Fritzler LB**: datos me seguís

**Gabriel Puertas**: No, no, no. Sí, tal cual, tal cual, tal cual.

**Gabriel Puertas**: Te entiendo. Yo lo que pasa ahí es claro digamos termina siendo una cuestión comercial, pero digo, nosotros usamos Slack obviamente y y tenemos la opción de conectar vincular cloud y volver preguntar a Cloud, qué sé yo. Eh, el tema de eso es que digamos como si consumen tokens, yo no me acuerdo bien cómo es la licencia. Yo sé que los chicos hasta le piden que le haga y cosas por el estilo. Coso,

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: pero no tiene mucha más utilidad de eso que en en Slat. Lo que lo que me genera alguna duda es que tan intensivo en uso es porque a mí qué me pasa, yo sé que si lo muestro a Eli, le va a decir,"Listo, ya está, esto me entendió." O sea, correte vos, salteño, y dejame a mí con clock que yo me entiendo bien. No necesito ninguna clínica ni nada. El tema de eso es esos usuarios en toda la compañía que le están pegando directamente va a ser un consumo muy alto y este consumo, o sea, acá en la página es vía API Key, que es el token caro que yo te decía. Entonces, una pregunta válida es, si vos ya aceptas tus empleados en Luis y Bosca, ¿van a consumir eh el LM?

**Gabriel Puertas**: que es es una inversión en definitiva, es decir, en cuánto tiempo yo llego al a lo que me cuesta la licencia.

**Damian Fritzler LB**: Está clarísimo y necesito un escenario intermedio que va a terminar pasando.

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: terminar pasando, porque a menos que a menos que cada uno de los de los

**Gabriel Puertas**: espérate.

**Damian Fritzler LB**: aplicativos termina haciendo un acuerdo con estas compañías, la vas a terminar nucleando al revés del LLM de las aplicaciones al LM y no el LM en las aplicaciones. Entonces, vas a tener un único Hub que va a ser el LM que hayas elegido.

**Gabriel Puertas**: Clud.

**Damian Fritzler LB**: Exacto. y vas a trans desde

**Gabriel Puertas**: Es esa es nuestra visión, digamos.

**Damian Fritzler LB**: cl es que a eso yo creo que va a

**Gabriel Puertas**: Por eso tenemos hecho el el producto de esa forma,

**Damian Fritzler LB**: terminar pasando,

**Gabriel Puertas**: digamos.

**Damian Fritzler LB**: todo va a terminar siendo conversacional, no vas a necesitar un IRP, lo único que te van a dar son estructuras y reglas de negocio que con que validar. Para eso van a terminar haciendo los sistemas.

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: Ahora es lo que yo imagino, eh, no puedo ir de nada todo porque hay un tema de adopción, de confianza y de capacidad por sobre todo.

**Damian Fritzler LB**: Entonces, yo necesito a usuarios como Eli que si puedan interactuar con Cloud, pero que seas usuarios como algún administrador que únicamente usen esta herramienta,

**Gabriel Puertas**: Claro.

**Damian Fritzler LB**: pero que si les mandaron un reporte de CRD Saraza de Arca, lo pueda cruzar el flaco de impuestos, pero es muy específico.

**Gabriel Puertas**: Está

**Damian Fritzler LB**: Entonces,

**Gabriel Puertas**: bien.

**Damian Fritzler LB**: si yo puedo yo y acá no sé si puedo también restringir el uso de los tokens o no o ser únicamente conversaciones,

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: digo,"Che, Damián, vos vas a poder usar eh esta plataforma, pero no vas a poder adjuntar ningún dato de afuera. Eli lo va a poder hacer, Mati va a usarlo para gestionar los dashboard. Entonces, ahí voy estructurando quizás y limitando el uso según el rol. ¿Para qué? para que no le empiecen a mandar a ver qué pasa así, a ver qué pasa así, que no va a ningún lado. el A ver qué pasa. Así todavía no quiero llegar hasta ahí. ¿Me seguís?

**Gabriel Puertas**: Sí, sí, sí, sin duda. Sí, sí. Bueno, hagamos.

**Damian Fritzler LB**: Eh,

**Gabriel Puertas**: Yo eso que te dije lo puedo hacer esto de decir, bueno, nosotros acá ya hicimos todo una dinámica desde que empezamos, que le hicimos hola Cloud hasta que nos entregó el dashboard. Yo puedo simular eso con con un ap decirte,

**Damian Fritzler LB**: obvio.

**Gabriel Puertas**: "Che, mira, Dami, toda esta dinámica hubiese costado tan y y eso no da una

**Damian Fritzler LB**: Eso,

**Gabriel Puertas**: idea." Otra pregunta.

**Damian Fritzler LB**: tal cual. Y para y lo último. Sí, disculpa. y después quizás generar estos tres, cuatro usuarios, cómo podría interactuar y no el que genera el tablero, el que lo consume, el que lo consume y lo crea desde cloud y el que lo usa solamente de acá. ¿Me seguís?

**Gabriel Puertas**: Sí, sí, sí, sí,

**Damian Fritzler LB**: como para entender capacidades de uno y otro y cómo me responde.

**Gabriel Puertas**: sí. Bien, no, eso, eso, eso está claro. ¿Qué otra pregunta que digamos a ver cómo tema modelo?

**Damian Fritzler LB**: Dígamo.

**Gabriel Puertas**: Hoy tenemos Cloud y Open. A, es como en este lado del mundo son los únicos,

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: pero hay un universo más grande de modelo, incluso hay modelo chino.

**Gabriel Puertas**: Vos ves algún problema en ver en abrir el abanico y decir,"Mira, este modelo cuesta tanto, tanto, tanto, tanto." Nosotros lo probamos a todos, ¿eh?

**Damian Fritzler LB**: A mí lo que me pasa es que hoy no negocio la el resguardo de la información y a qué voy a un modelo chino le confío poco,

**Gabriel Puertas**: No, eso está claro.

**Damian Fritzler LB**: a un norcoreano menos, ruso que casi nada. Entonces, al americano tampoco le confío, pero no más confiable dentro de todo ponerle

**Gabriel Puertas**: Claro,

**Damian Fritzler LB**: no puedo

**Gabriel Puertas**: pero al menos eso dicen que cumplen con la ley. No, no, pero o sea, están los chinos, los chinos vuelan. los modelos chinos, el Kimi, Kimica K3. De hecho, el problema con los modelos chinos que tampoco es que tienen tanto, o sea, tienen weightlist para porque son muy baratos y están a nivel de los buenos de este lado. Eh, pero por ejemplo, hace poco nos juntamos gente de la AWS. As. Bedrock, que es lo que yo le intenté explicar a a Fabián. Berrock es vos como que contratas infraestructura para que corra tu modelo ahí y es tu Sony o lo que sea ahí es tuyo y eso es

**Damian Fritzler LB**: Só

**Gabriel Puertas**: como lejos lo más seguro porque vos sabes que ese modelo tuyo no lo usa nadie que va eso no tiene su costo que yo se puede implementar eso también pero además ellos por ejemplo tienen un modelo propio. Nosotros no sabemos muy bien cómo funciona, pero están desesperado por vender tokens, ¿entendés?

**Damian Fritzler LB**: está.

**Gabriel Puertas**: Entonces nada, es como eventualmente se puede pensar en en unir puntas y decir,

**Damian Fritzler LB**: Mira,

**Gabriel Puertas**: "Bueno, che, usen este,

**Damian Fritzler LB**: mira,

**Gabriel Puertas**: eh,

**Damian Fritzler LB**: nosotros tenemos un modelo montado en una infraestructura nuestra.

**Gabriel Puertas**: Yeah.

**Damian Fritzler LB**: Ah. en la nube en Asul con un modelo de charitina, ¿no? Eh, donde lo que hacemos es hacer toda la simulación de abastecimiento y planificación de insumos eh y logístico.

**Gabriel Puertas**: Bien, yo no me acuerdo el nano.

**Damian Fritzler LB**: Es usamos nano porque para lo que necesitamos es muy flat, se basa en únicamente en información histórica y nada más. La idea ahora es empezar a desafiarlos con información de afuera,

**Gabriel Puertas**: Bueno,

**Damian Fritzler LB**: pero qué voy con esto posibilidad también de montarlo en un infraestructura

**Gabriel Puertas**: pero

**Damian Fritzler LB**: propia y generar un agente propio, pero que esté nada toquenizado,

**Gabriel Puertas**: obvio,

**Damian Fritzler LB**: pero voy a lo mismo. C'est

**Gabriel Puertas**: este se puede poner, ese se puede poner acá si ustedes, si encontramos un modelo que atiende a las personas que

**Damian Fritzler LB**: el

**Gabriel Puertas**: chatean y que nada, vos sabés que en algún momento si el prom es medio malo y el modelo no es tan potente, capaz que le responde alguna cosa, pero si puedo un universo de gente que a mí no me preocupa tanto, ese modelo se los conectamos acá y y usan, o sea, ustedes van a pagar el hosteo de ese modelo.

**Damian Fritzler LB**: Totalmente, Gabi. Y y a lo que voy es e a ver, yo quiero empezar primero por un por un por un modelo donde donde me repague. Hoy vos bien sabés, el costo de las empresas no pueden seguir aumentando, tienen que entrar en decreción.

**Gabriel Puertas**: Sí, ni hablando.

**Damian Fritzler LB**: Entonces, yo tengo que mostrar no solo una eficiencia, sino un un decreción en en el gasto. Eh, mismo también porque hoy es difícil medirlo, entonces de repente me voy a encontrar con que o no lo puedo usar o pagé una fortuna y ninguna de las dos son varias porque no poder usarlo me sale caro.

**Gabriel Puertas**: Claro,

**Damian Fritzler LB**: Entonces, nada, ahí es donde digo,"Che, bueno, mi empresa

**Gabriel Puertas**: lo que lo que pasa para mí, una cosa que yo haría Ya estamos estamos adelantando, ¿no? Pero digo yo o lo veo que tiene mucho sentido con con coso. Nosotros eh estamos con una empresa grande que es de consumo masivo de producto alimenticio. Me retan, si te digo quién es. Eh, me retan, me retan mucho a mí el eh, pero bueno, en fin, a lo que voy a es lo que ellos hicieron fue un caminito muy parecido a todas las preguntas que que surgen, que es decir, bueno, hagamos una cosa, eh, ponerte mod en un esquema que a vos te hagas te haga sentido ahora acotado, en el cual tres o cuatro usuarios, porque para mí el el valor, el principal valor, es decir, yo ya sé que nosotros podemos hacer los dashboard como como tabl y lo podés apagar, pero eso no es terita, o sea, vos podes hacer mucho más que eso. Y para mí eso es lo primero que ten que probar en el sentido de decir, bueno,

**Damian Fritzler LB**: Yeah.

**Gabriel Puertas**: podríamos Así una poca acortada de dos meses en el cual conectamos la fuente de datos que ustedes necesiten, acompañamos la gente que ustedes necesiten y validan eso. Dicen check, check, check.

**Gabriel Puertas**: Bueno, esto esto a mí me sirve. Yo puedo eso, sería como agarrar tres, cuatro personas las que ustedes decidan y como darle superpoderes. Decir, bueno, ahora Fabián sabe que si él pide el flujo de caja el viernes a las 5 de la tarde, 5:20 lo tienen que tener, lo tienen que tener reporte como lo necesita y no sé con estrategia o lo que sea. Ahí va a depender cómo lo usan, ¿eh? Y eso durante un mes decir,"Che, bueno, la verdad esto cambia tanto como como dicen ellos, ¿sí? No, a nosotros nos sirve, no nos sirve porque qué sé yo. Bueno, una vez que tengamos eso medido, el siguiente paso es ver cómo lo extendemos, porque capaz que ahora estamos discutiendo para todos los empleados y cosas así, ¿no? Eh, no sé si te parece hacemos algo que tenga sentido. Esa esa po nosotros por ahí la cobramos, pero no deberías es como que no nos tenemos que poner de acuerdo para toda la vida y avanzamos y probamos eso, digamos.

**Damian Fritzler LB**: Sí. A ver, e yo lo que voy a hacer es una revisión de de mis usuarios. Yo en tablot tengo muchos usuarios de consulta y que van a seguir siendo de consulta.

**Gabriel Puertas**: Ahí

**Damian Fritzler LB**: Se dice. Entonces, sencillamente lo lo puedo compartir.

**Gabriel Puertas**: va.

**Damian Fritzler LB**: Eh, lo que quiero entender después con Agustín es, che, el usuario que únicamente va a consultar tableros, ¿qué costo tiene?

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: seguir,

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: eh, y a partir de ahí poder entender, bueno, qué tan escalable es mañana entran dos personas nuevas en qué coto tiene el recursos humanos también me va a levantar el decir,"Che, ¿cuánto vale un la posición a nivel eh sistemas?" No lo sé. Eh, hagamos esto si te parece. Yo me voy a llevar para revisar los usuarios. Vos más o menos ya sabes cuál es mi mi escenario acá dentro.

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: Lo que necesito que me ayuden es armar un modelo a medida para mí. La verdad que yo hoy lo que me pasa es que no encuentro un modelo de los que ustedes

**Gabriel Puertas**: Listo.

**Damian Fritzler LB**: ofrecen donde calce derecho para Luigi Bosca. O estoy muy pasado o me quedo corto y no necesito que todos hagan todo.

**Gabriel Puertas**: Claro, el a mí de todo lo que vos me contaste, el que me preocupa es el usuario que chatea, pero además pero que chatea con un nivel de inteligencia un poco mayor porque ese puede gasear intensivo y consumir más.

**Gabriel Puertas**: el que el el que genera ese no me preocupa. Creo que vuelve a entender, ese flaco tiene que tener mucha capacidad, tiene que, qué sé yo, para mí eso le ten que dar cloud.

**Damian Fritzler LB**: Sí, total.

**Gabriel Puertas**: es el es irónicamente es el usuario más barato en respecto a Teramod.

**Damian Fritzler LB**: Sí, sí, sí.

**Gabriel Puertas**: mod y creo que yo globalmente también porque te va a dar, no, eso no sé, depende cuánto uses, pero ese es el el si quieres el más flat porque ese ese no te no te consume

**Damian Fritzler LB**: Eh,

**Gabriel Puertas**: tokens. En definitiva, eso es lo que pasa. Esto es una usina de consumir tokens. El el el usuario que chatea creo que tiene, yo lo he visto porque nuestra primera nosotros estamos hace tres años con esto y nuestras primeras versiones tenían que ver un poco con este chat with your data. Lo que nosotros veíamos y aparte por eso también pivoteamos fuerte es que empieza como un chiche que está buenísimo y después baja porque vos nada, yo le puedo preguntar las ventas, pero también la puedo ver en el dashor.

**Damian Fritzler LB**: Totalmente,

**Gabriel Puertas**: ¿Entendés? Entonces ese se cae un poco.

**Damian Fritzler LB**: totalmente.

**Gabriel Puertas**: Me preocupa el del medio.

**Gabriel Puertas**: Vos decí,"Che, recibí el dashboard, se lo cargo a esto, que s

**Damian Fritzler LB**: Pero sabes lo que pasa, David, no. De esos hay pocos.

**Gabriel Puertas**: sí.

**Damian Fritzler LB**: De esos hay poco y suelen ser informes de consultoras que nos suelen pasar y que hoy por hoy el tiempo que le llega a procesarlo a nivel costo de tiempo es mucho más alto que los tes que puede llegar a consumir. Entonces ahí es donde digo,"Bueno, listo,

**Gabriel Puertas**: Claro.

**Damian Fritzler LB**: estoy okay.Ok." Pero lo que no quiero es que todo el mundo pueda cargar archivos con uso de de tokens, porque ahí sí va a empezar ese chiche de jugar y a ver qué pasa donde no genere ningún valor agregado.

**Gabriel Puertas**: Tal.

**Damian Fritzler LB**: Yo quiero dárselo a el tipo de planificación comercial.

**Gabriel Puertas**: Claro, el tipo que lo que estaría bueno, estoy pensando de del lado de ustedes es tener un esquema en el que el usuario adicional decirma valor porque digamos entendemos decir, bueno, yo solar el de planificación comercial, pero mostrame que que con esto está eficientizando algo.

**Damian Fritzler LB**: Es que, a ver, la idea nuestra también es a nosotros tenemos algunos proyectos inteligencia artificial donde lo estamos usando como modelo para entender qué costos beneficios nos está tomando y son desarrollos muy muy puntuales a nivel interacción con WhatsApp, con los comerciales, eficiencia concional y demás.

**Damian Fritzler LB**: Eh, todo va a medir un poco y va a poner en blanco solo, en negro el retorno de la inteligencia artificial. Lo que no puedo hacer es que me pase como algunas empresas que de repente me encuentren con que consumí todo el presupuesto en 3 meses.

**Gabriel Puertas**: No, no, no, no, no. Eso, eso no se puede porque para mí eso le pasó mucho a la que a la que desarrollaban.

**Damian Fritzler LB**: ¿Entend?

**Gabriel Puertas**: Pero escúchame, hay un proyecto en esta que no puedo decir que está buenísimo. Me si te acuerdas con esto que dijiste de WhatsApp los comerciales que se llamaba el minuto de oro y me encantó. O sea, nosotros lo hicimos. ¿Qué fue? Es como a los comerciales le hicimos una tabla Gold, como la tabla que acabamos de hacer, que tiene por cliente toda la información relevante que define la área comercial. Entonces, ¿qué le pasa a esto? Que me imagino que no sé cómo venden ustedes, pero esto estos tipos venden mucho por distribuidor, entonces iban a visitar gente. Entonces, ¿qué pasaba? Los comerciales decían,"Nosotros tenemos dashboard y todo eso para que el el punta de lanza, comercial, punta de lanza eh tenga información para ir a visitar un cliente." Pero eso tipo no lo ven nunca porque vienen el auto,

**Gabriel Puertas**: qué s. Entonces armaron algo que que vivió en WhatsApp que que se llamaba Minutor, ¿cómo funcionaba? Eh, va Gabriel Puerta a visitar a Damián y 5 minutos antes le manda un WhatsApp y le dice,"Che, estoy yendo a ver a Damián Fitler." Ahí va. Buenísimo. Entonces, lo que hacía era hacer una query a la tabla que vos habías armado en Teram. De hecho, lo tienen usando y ya tiene predefinida eh la info que se tiene que traer de ese cliente que va a ver y le dice,"Che, fíjate que hace tanto que no te compra esto, fíjate que te debe tanto, fíjate que te Entonces el tipo nada, está llegando en el auto, por eso se llama minuto de oro. Es ese minuto que le da la info exacta que necesita para ir a ver ese tipo, ¿entendés? Y ese volaba porque pensarlo como como infraestructura. Ventamos lo único que hacés es armar la tabla gold que se tiene que mantener todos los días actualizada y tiene que tener esa información. No lo piense como de sistema como vos decís,"Bueno, lo hago una sola vez y listo." No, porque los comerciales a cada rato le están agregando, sacando información, qué són.

**Gabriel Puertas**: Entonces, enteramos eso se usa porque en un momento vos necesitas ponerle la deuda, después sacarle la deuda, ponerle tal cosa, qué sé yo, y esa tabla dinámica. Y después lo único que hacé es un modelo que que la coerea. Además, eventualmente le pegas con una API a la a la tabla gol y organizar el mensaje. Lo único que te tiene que llegar el mensaje es exactamente quién es el cliente, nada más para hacer bien la query. Después la cuer está armada siempre y ese vuela porque porque vos le estás dando información eh superalineada al tipo que va a ver el cliente y esa información la maneja la gente comercial, ¿entendés? Porque ellos hasta definen el el texto de la respuesta, ¿me entendés? Ese ese volaba en en Goos y está

**Damian Fritzler LB**: Eh,

**Gabriel Puertas**: buenísimo porque eso eso no consume

**Damian Fritzler LB**: nosotros estamos nosotros estamos armando algo parecido, pero de operación.

**Gabriel Puertas**: tokens.

**Damian Fritzler LB**: Eh, hoy perdemos mucho tiempo y muchas oportunidades y esto lo que termina haciendo es generar una una interacción a través de WhatsApp con nuestros sistemas para operarlos, eh crear pedidos, cargar pedidos, consultarlos,

**Gabriel Puertas**: M.

**Damian Fritzler LB**: eh acciones y que sea de verdad M. no reactivo, sino eh sino proactivo.

**Damian Fritzler LB**: Che, está cerca de fulanito que tiene esta situación, vas a verlo. Entonces nada, estamos viéndolo.

**Gabriel Puertas**: Pero ustedes tienen insight de los clientes tipo que se va acabando y bueno

**Damian Fritzler LB**: Nosotros tenemos self y lo y lo que hacemos ahí es cargamos todas las tareas que hace el comercial dentro de Self.

**Gabriel Puertas**: Y tienen tipo de alertas de este no, este

**Damian Fritzler LB**: Y lo que queremos hacer es que con información de transacción,

**Gabriel Puertas**: sí.

**Damian Fritzler LB**: las oportunidades de los de los clientes, las las actividades de cada uno de los comerciales, entender quién le mandaste dos mail y lo fuiste a visitar una vez, no te volvió a comprar, pero es una zona donde hay un producto que está funcionando muy bien, que nunca le vendiste, anda a visitarlo porque está cerca y ofrecer este nuevo producto y mostrar toda esta información. Yo creo que el modelo va en en compartir información y ser más un consultor comercial con el cliente que es solamente un vendedor. Entonces,

**Gabriel Puertas**: Claro,

**Damian Fritzler LB**: brindar información que le ayude al al cliente a a

**Gabriel Puertas**: Pero

**Damian Fritzler LB**: potenciar sus ventas. Si mi cliente vende más, yo vendo más.

**Gabriel Puertas**: hagamos eso. Dame si vos podés conectar enter y SAP y lo que haga falta.

**Gabriel Puertas**: Ya, yo no te mostré. Vamos est acá. Espérame un segundito. Ah, no, pues estoy ahora está bien. Mira, vos con esto, ¿qué es lo que cómo se lo implementamos nosotros a esta gente? Es tal cual. Eh, conectaron SAP y Save Force. Vos acá lo que podés hacer es crear una key en N8N.

**Damian Fritzler LB**: Ah.

**Gabriel Puertas**: ¿Conocéis N8N?

**Damian Fritzler LB**: Sí, de hecho el parte del proyecto de de WhatsApp lo

**Gabriel Puertas**: Bien. Buenísimo. Bueno, NHN tiene dos ventajas para mí.

**Damian Fritzler LB**: hacemos.

**Gabriel Puertas**: Yo creo que le está cayendo porque la gente no lo entiende, pero nada. Vos podés configurar N8N con un Jason. Eso quiere decir que si es con un Jason te lo hace cloud, ¿entendés? como bueno y el MCP que nosotros tenemos es básicamente un conjunto de Apples, ¿no? O sea,

**Damian Fritzler LB**: Mhm.

**Gabriel Puertas**: que vos le podés conectar a N8N el MCP, que Cloud haga el el Jason y acá lo que haces es generar una una piquí y vos lo cargas en NHN y ahí te armas todo ese flujo.

**Gabriel Puertas**: ¿Qué quiere decir con esto? Vos agarraste con Teram y te armaste tu gol que vinculaba Saleford con con Goso, armaste toda esa vista junto con Claud, ¿no? Y le explicaste todo este problema que que vos decís que tienes. o decir,"Bueno, yo necesito que nada, haya un mail que le mande del comercial cuando oh resulta que tal cliente hizo tal cosa, tal cosa que s yo todo lo que ustedes hicieron ellos pueden ser una o varias golds que después las tenés vinculadas con NHN y después configura en N ese flujo, va, mira, extrae información y dispara los mails. Eso lo tenemos hecho por una farmacia que digamos lo que hace es reponer stocks. Mapea los stocks de las distintas sucursales y dice,

**Damian Fritzler LB**: Sí.

**Gabriel Puertas**: bueno, lo agrupa por proveedor y dice, bueno, la sucursal tanto, el proveedor tanto, le tenés que pedir esto, esto, esto, esto y esto, el otro, este, esto y esto, es el mismo flujo. O sea, ¿cuál es el me imagino cuál es el problema que pueden llegar a tener ustedes para implementar eso? Es el laburo de ingeniería de datos en el que te extraés las cosas de de Sale Force, de SAP. vincul que tenga el coso, qué sé

**Damian Fritzler LB**: Por eso, por eso nosotros tuvimos la suerte de que no implementamos hace mucho y cuando implementamos lo que desagregamos es la

**Gabriel Puertas**: yo.

**Damian Fritzler LB**: gobernanza de los datos. Leos acá en aplicativo la gobernanza. Yo el cliente y todo lo que conlleva información del cliente lo tengo en CF. No necesito balon el IRP para nada. Datos de factura en el CRM, nota de crédito en el CRM,

**Gabriel Puertas**: Hm.

**Damian Fritzler LB**: TR en el CRM, descuentos en el CRM, oportunidades en el CRM, lista de precio en el CRM. Entonces hoy el comercial lo tiene todo CRM. Yo lo que hago es con WhatsApp y N8N conectar ese el flujo que yo hago conversacional. con con WhatsApp, traducirlo después en un en un flujo para nada

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: impactarlo después en self si es transaccional o si es consultivo al

**Gabriel Puertas**: Pero ese ese al revés y este debería ser así.

**Damian Fritzler LB**: revés.

**Gabriel Puertas**: Está bien. Claro. Bueno, si tienen todas N8N y va, pero un poco esa es la dinámica, ¿entendés? O sea, yo obviamente no le contesto esto a Fabián porque lo que iba a salir con los pelos todas esas cosas, pero te ha pensado para que hagas esos flujos.

**Gabriel Puertas**: O sea, vos de repente decir,

**Damian Fritzler LB**: No.

**Gabriel Puertas**: "Tengo tal quilombo, vos sabes que lo tenés en los datos, podés automatizar." Este, nada, de la misma forma podés hacer un modelo predictivo. ¿Por qué? Porque igualas a las gol que armaste le podés pegar programáticamente. Entonces, si abrimos cloud y le decimos,"Che, necesito un modelo de predicción de venta, qué sé yo, él mismo va a armar todos los todos los dataset normalizados para correr un LGB, c***** sea que él sabe qué hacer. te va a dar el código y vos lo vinculás con esta API Key para que todos los días corra y te te genere las cosas. O sea, un poco la idea es esa, digamos, nosotros por qué por qué tenemos publicados los dashw. Los dashwam son es código HTML que hizo un modelo y nosotros lo hosteamos, o sea, no tiene ningún secreto. Lo que nosotros sabemos que el el valor viene en en lo que sigue, ¿me explico?

**Damian Fritzler LB**: Sí, sí, sí.

**Gabriel Puertas**: en es en esa potencialidad y el y el problema que tienen los modelos es que

**Damian Fritzler LB**: Bueno,

**Gabriel Puertas**: no no le pegan a las bases de datos, no interpretan la base de datos. Entonces, la idea nuestra es quedarnos ahí en ese en ese coso. Teó un montón de tiempo, igual estuvo buenísima la

**Damian Fritzler LB**: Em, hagamos esto, Gabi,

**Gabriel Puertas**: charla.

**Damian Fritzler LB**: si queres como para la semana que viene. Veamos esto de los usuarios, cómo lo podemos estructurar. A ver si ya podemos darle un poquito más de contexto a al modelo que quizás necesitaríamos nosotros. Yo me me llevo en la cabeza y tengo tres modelos,

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: uno con con un ll la orquestación, poner o la creación de los modelos, uno que lo consulte usando tokens y otro únicamente el uso de los das. ¿Le parece?

**Gabriel Puertas**: Está igual.

**Damian Fritzler LB**: A vamos a armar.

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: Sí.

**Gabriel Puertas**: está igual.

**Damian Fritzler LB**: Y ahí con Aus armar quizás algo o pasárselo a ver que podemos armar en algún modelo de de costo mensual más intermedio entre las

**Gabriel Puertas**: Sí, sí, sí.

**Damian Fritzler LB**: dos.

**Gabriel Puertas**: Ahí, ahí vemos. Dale, dale, Dami,

**Damian Fritzler LB**: Gracias.

**Gabriel Puertas**: estamos hablando.

**Damian Fritzler LB**: Ahora

**Gabriel Puertas**: Abrazo. Chao.
