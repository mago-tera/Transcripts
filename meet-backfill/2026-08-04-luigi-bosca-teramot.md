# Luigi Bosca <> Teramot

**Fecha:** 2026-08-04T12:01  
**Duracion:** ~47 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** dfritzler@luigibosca.com, Gabriel Puertas, Agustin Garcia  
**Externos:** dfritzler@luigibosca.com  
**Archivo origen:** Luigi Bosca _ Teramot - 2026-08-04 12_01 GMT-03_00/Luigi Bosca _ Teramot_ 2026_08_04 12_01 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Se presentó la propuesta de valor y la demostración técnica junto con la estructura de implementación futura.Propuesta de valor estratégicoLa plataforma se posiciona como una alternativa eficiente frente a Tableau mediante la automatización de tableros. Se enfatizó la importancia de documentar hallazgos para gestionar particularidades de los datos.Funcionalidad técnica y seguridadLa demostración confirmó que la inteligencia artificial genera reportes editables manualmente en HTML y SQL. La arquitectura garantiza acceso de solo lectura para mayor seguridad.Estructura de implementación definidaSe decidió una estructura con 100 usuarios visualizadores y 10 administradores para optimizar costos de consumo. Se solicitó un modelo de estimación financiera basado en 80 tableros.

### Próximos pasos

[Agustin Garcia, Damian Fritzler LB] Firmar acuerdo confidencialidad: Formalizar el documento de confidencialidad para permitir la conexión a la base de datos de producción.
[Agustin Garcia] Compartir modelo reporte: Enviar el modelo de reporte inicial para facilitar el trabajo con la estructura de datos requerida.
[Damian Fritzler LB] Conectar base producción: Configurar el acceso a la base de datos de producción para realizar las pruebas técnicas necesarias.
[Agustin Garcia] Análisis de consumo: Calcular un benchmark de consumo de tokens por tablero para estimar costos futuros.
[Agustin Garcia] Presentar propuesta integral: Presentar una propuesta integral que incluya el cálculo estimado de costos operativos y el uso de agentes internos.
[Damian Fritzler LB] Preparar datos: Crear un conjunto de datos reducido para utilizar en la demostración con Eli.
[Damian Fritzler LB] Reunirse con Eli: Coordinar y realizar una reunión la próxima semana para revisar el progreso de la implementación.

### Detalles

Introducción y Contexto del Proyecto: Gabriel Puertas y Agustin Garcia conversaron sobre el progreso de un proyecto, mencionando un cambio de nombre de una funcionalidad a "Racon" por solicitud de una de las partes. También intercambiaron perspectivas sobre el mercado brasileño, destacando que en puestos de alto nivel existe una preferencia por el español frente al inglés, lo cual debe tenerse en cuenta para la interacción con clientes (00:00:26).
Propuesta de Valor y Reemplazo de Tableau: Agustin Garcia y Gabriel Puertas discutieron el posicionamiento de la plataforma como una alternativa a Tableau. El objetivo central es demostrar cómo la inteligencia artificial facilita la generación y publicación de tableros, permitiendo a los clientes sustituir sus actuales licencias y flujos de trabajo manuales por una solución más eficiente (00:04:49).
Metodología de Ingesta y Documentación de Datos: Gabriel Puertas detalló el proceso realizado con los datos de "Luigi Bosca", el cual incluyó la ingesta de 16 tablas. Se enfatizó la importancia de documentar los hallazgos en un archivo colaborativo para gestionar particularidades, como el manejo de diferentes divisas, asegurando que el conocimiento sea compartido para mejorar las iteraciones futuras (00:05:53).
Inicio de la Sesión con Damian Fritzler LB: Agustin Garcia y Gabriel Puertas dieron la bienvenida a Damian Fritzler LB para iniciar formalmente la demostración del nuevo módulo de reportes. Se estableció que el foco de la reunión sería mostrar la capacidad de la herramienta para generar reportes mediante inteligencia artificial y su facilidad para la distribución de los mismos entre múltiples usuarios (00:09:41).
Uso de Agentes de Inteligencia Artificial: Damian Fritzler LB consultó sobre la necesidad de contratar agentes externos en la nube para obtener información. Gabriel Puertas aclaró que la plataforma cuenta con un agente embebido, eliminando la necesidad obligatoria de adquirir licencias externas, aunque existe flexibilidad para alinear el motor de inteligencia artificial según el rendimiento y costo deseado (00:10:58).
Comparativa de Costos y Eficiencia frente a Tableau: Damian Fritzler LB expresó inquietudes sobre los costos de migración comparados con la licencia actual de Tableau, especialmente en relación con el consumo de "tokens" para la generación de reportes mediante inteligencia artificial. Agustin Garcia explicó que la plataforma ofrece ventajas de eficiencia al automatizar la creación de tableros, permitiendo que solo unos pocos usuarios administrativos requieran licencias completas, mientras que el resto puede operar como usuarios visualizadores ("viewers") (00:14:41).
Funcionalidad y Compartición de Tableros: Gabriel Puertas realizó una demostración sobre cómo un usuario creador puede utilizar un agente para construir un tablero basado en hallazgos específicos de los datos y luego compartirlo. Los usuarios visualizadores pueden acceder a estos reportes sin necesidad de tener capacidades de generación de inteligencia artificial, manteniendo el control sobre filtros y vistas (00:17:04).
Gestión de Conocimiento y Código: Gabriel Puertas destacó que la plataforma permite que los usuarios editores compartan el conocimiento sobre las particularidades de los datos, como criterios de comprobantes fiscales o manejo de monedas. Además, se subrayó que la plataforma genera código (como HTML y SQL) que permanece accesible y transparente para los usuarios (00:19:35).
Acceso y Gestión de Licencias: Damian Fritzler LB indagó sobre las implicaciones de compartir el acceso a un agente entre varios usuarios. Gabriel Puertas y Agustin Garcia clarificaron que, aunque es posible, compartir el acceso puede acelerar el consumo de "tokens", por lo que recomendaron una administración cuidadosa para gestionar estos costos de manera efectiva (00:22:00).
Preparación para la Prueba de Concepto: Damian Fritzler LB propuso realizar una reunión la semana siguiente con una integrante del área de "FPN" para testear la herramienta con datos complejos de la base de producción. Se acordó la firma de un acuerdo de confidencialidad (NDA) para permitir el acceso seguro a la base de datos necesaria para esta prueba (00:25:07).
Demostración de Velocidad en Creación de Tableros: Gabriel Puertas mostró la agilidad de la herramienta al generar un tablero de marketing en tiempo real. Esta demostración sirvió para ilustrar cómo el proceso de iteración y publicación es considerablemente más rápido en comparación con los métodos manuales tradicionales (00:28:31).
Capacidad de Edición Manual: Damian Fritzler LB consultó si era posible realizar modificaciones manuales en los tableros. Gabriel Puertas confirmó que, aunque la inteligencia artificial genera el código inicial (SQL y HTML), los usuarios capacitados tienen la posibilidad de editar estos componentes manualmente, lo cual evita el consumo innecesario de "tokens" adicionales (00:29:49).
Arquitectura de Datos y Seguridad: Gabriel Puertas explicó que la herramienta funciona como un almacén de datos ("warehouse") que lee de la base de datos de producción en intervalos definidos para actualizar las tablas utilizadas en los reportes, garantizando que el acceso sea siempre de solo lectura (00:32:47).
Estrategia de Implementación y Volumen de Usuarios: Agustin Garcia propuso una estructura para la implementación que contempla 100 usuarios visualizadores y entre 5 y 10 usuarios administradores para la gestión de tableros. Esta estrategia busca optimizar costos y facilitar una adopción gradual de la plataforma (00:33:46) (00:37:52).
Gestión de Costos y Tokens: Damian Fritzler LB y Agustin Garcia debatieron sobre cómo evitar sorpresas en la facturación debido al consumo de "tokens" durante la fase inicial. Concluyeron que, si bien la etapa de creación consume más recursos, las tareas de mantenimiento pueden realizarse mediante la edición manual de código, reduciendo la dependencia de la inteligencia artificial una vez que el tablero está establecido (00:35:23) (00:39:15).
Solicitud de Benchmarking de Costos: Damian Fritzler LB solicitó una estimación de costos basada en un volumen de 70 a 80 tableros para poder justificar el presupuesto internamente y evitar imprevistos financieros. Agustin Garcia se comprometió a elaborar una propuesta integral y un modelo de estimación para brindar claridad sobre el flujo de costos (00:40:26) (00:43:49).

---

## Transcripcion

**Gabriel Puertas**: querido.

**Agustin Garcia**: Todo Bien,

**Gabriel Puertas**: Todo bien con todo bien. ¿Qué onda? Que te pasé.

**Agustin Garcia**: todavía no lo pude ver porque estuve en reunión. No, no paré

**Gabriel Puertas**: No, tranca.

**Agustin Garcia**: de

**Gabriel Puertas**: Es lo lo de

**Agustin Garcia**: Perfecto. Ahora lo miro y cu te pregunto.

**Gabriel Puertas**: cambiaba el nombre a pedido tuyo. No sé si el nuevo nombre te gusta.

**Agustin Garcia**: Me gustó, me gustó, me gustó el bacon.

**Gabriel Puertas**: No es baikon. Racon porque tenía hambre

**Agustin Garcia**: Claro.

**Gabriel Puertas**: ahora.

**Agustin Garcia**: Vamos a ver si se suma este pibamos gas al tema. Bueno,

**Gabriel Puertas**: Se escucha música.

**Agustin Garcia**: No, nada se escucha. No se escucha nada. Pues termino acá tengo reunión con con Lucho. Hoy tenemos con hoy tenemos con Johnson

**Gabriel Puertas**: con Johnson. Sí, hay que ser portugués. Cuent. Ojo con el tema del inglés con los brazucas.

**Agustin Garcia**: eh

**Gabriel Puertas**: lo que le decía Bruno,

**Agustin Garcia**: Hor.

**Gabriel Puertas**: porque no es tan común que la gente hable inglés. en Brasil.

**Gabriel Puertas**: Y si vos tenés un gerente o alguien, alguno así que medio alto que no habla inglés y vuel empezar

**Agustin Garcia**: No, de hecho, de hecho, es más,

**Gabriel Puertas**: nada.

**Agustin Garcia**: yo mi experiencia es que hasta en muchos casos prefieren español que entiendan mejor que que inglés.

**Gabriel Puertas**: Sí, sí, sí, sí.

**Agustin Garcia**: Sí, sí, eso estamos alineados.

**Gabriel Puertas**: Brasil es como un mercado muy grande, entonces muchas veces a puestos altos llega gente que no está tan preparada como el equivalente en Argentina, que un mercado más chico, pero tiene más gente

**Agustin Garcia**: Claro,

**Gabriel Puertas**: preparada por

**Agustin Garcia**: sin hablar.

**Gabriel Puertas**: ahí. una Puedo inclusión venta. Acaba un poco la idea de decirle, yo hice dos, tres prom shot. Le dije, "Che, si quieres le puedo mostrar un poquito bien lo que hice, pero es como para perder el tiempo o no,

**Agustin Garcia**: No, aparte también,

**Gabriel Puertas**: no sé.

**Agustin Garcia**: ¿no? Sí,

**Gabriel Puertas**: Pero

**Agustin Garcia**: yo creo que estaría bueno nada que vea cómo se ve, dónde se ve, tal vez.

**Gabriel Puertas**: y contarle un poquito cuál va a ser la evolución de esto,

**Agustin Garcia**: Eh,

**Gabriel Puertas**: digamos, porque esto

**Agustin Garcia**: sí, perfecto.

**Agustin Garcia**: Vos pensass que también esto le puedes es una oportunidad para ellos también de no solo implementar el producto,

**Gabriel Puertas**: nosotrosarlo

**Agustin Garcia**: sino también de reemplazar la licencia que ellos quieran reemplazar de tabló y tal vez lo que estaría bueno,

**Gabriel Puertas**: a

**Agustin Garcia**: que no sé si puede ser en el alcance de esta reunión, vemos, pero nada, también que digamos estos dashboard se generan con inteligencia artificial, cómo se publican, digamos, cómo es el circuito, ¿entendés? que me parece que eso porque hoy

**Gabriel Puertas**: Es eso es lo que estamos refinando nosotros ahora porque lo que

**Agustin Garcia**: Claro,

**Gabriel Puertas**: estamos Ah,

**Agustin Garcia**: porque

**Gabriel Puertas**: bueno, no sé, lo deberíamos escuchar este muñeco, Pero dale, decime.

**Agustin Garcia**: no lo que te diría es nada,

**Gabriel Puertas**: Decime.

**Agustin Garcia**: vos yo lo que le dije que esto es una un feature que estamos que lanzamos al mercado, entonces digo, no quiero tampoco digamos que que que digamos vayamos a un esquema muy que estamos en en beta mode, ¿entendés? Entonces,

**Gabriel Puertas**: No, no,

**Agustin Garcia**: pero a mí me parece que lo interesante para él es ver cómo es el circuito en término

**Gabriel Puertas**: no.

**Agustin Garcia**: de, bueno, entro, hago, cómo creo un dashboard, cómo lo publico, ¿entendés?

**Gabriel Puertas**: venir

**Agustin Garcia**: y y cómo que eso es lo que creo yo que puede llegar a ser. Eh, s eh bueno para esos.

**Gabriel Puertas**: Mhm. la charla un poco es eso. Yo lo que, o sea, la dinámica de esto fue me conectaron los datos de Luigi Bosca. Okay, miremos que hay.

**Agustin Garcia**: Perfecto,

**Gabriel Puertas**: Entendemos menos son las tablas.

**Agustin Garcia**: ¿no? Pero para es un montón, digamos, ingestamos los datos, se interpretó el modelo de datos automáticamente, digamos, poder generar reportes por Me parece que es un es un valor importante esto.

**Gabriel Puertas**: A mí eh a mí me gustaría repasarle un poquito esto porque decirle yo de esta primer charla que tuve yo con los datos de eso, armo este documento que es compartido donde le donde está todos los hallazgos que yo encontré de los datos de ello. sé crítico e la columna Geno PR eh no sé qué tiene 100 tiene un montón de cosos 100% vacío. Eh, no sé, eh, todo este tipo de información que yo capturé de los datos de ello, me pasa a servir, por ejemplo, cómo tengo que manejar las monedas, cosas por el estilo. ya queda colaborativo para el resto de las personas que lo usen.

**Agustin Garcia**: Claro.

**Gabriel Puertas**: Esto debería hacerle sentido a él si conoce los datos. Y una vez que vos estás ahí, el siguiente paso es decirle, "Bueno, mira,

**Agustin Garcia**: No.

**Gabriel Puertas**: yo capaz que le dije un poquito, mira, vamos a hacer quiero quiero iterar unos documentos que quiero iterar una una pésima tele, le digo, eh, de vamos a hacer una especie de dashboard, se los iteré un poquito y nada. una herramienta, lo publica al o sea, vos tenés estos y estos eh rey los public y nada, los va iterando. Yo acá lo que puedo hacer es decir, a ver, Nada, en vivo con él le puedo pedir que cambie el idioma, cambores.

**Agustin Garcia**: Claro,

**Gabriel Puertas**: Lo que hice fue tipo

**Agustin Garcia**: ahí está, ahí está entrando. Ahí está entrando

**Gabriel Puertas**: un

**Agustin Garcia**: Damián. Hola, Damián, ¿cómo estás?

**Gabriel Puertas**: bueno.

**Damian Fritzler LB**: Buenas.

**Agustin Garcia**: ¿Todo bien?

**Gabriel Puertas**: Todo

**Agustin Garcia**: Perdón, no te escuchamos. ¿Cómo?

**Damian Fritzler LB**: Ah, denme un segundo.

**Agustin Garcia**: Sí,

**Damian Fritzler LB**: Ahí me escuchan.

**Agustin Garcia**: ahí te escuchamos. Perfecto,

**Damian Fritzler LB**: Un segundo cambio esto.

**Agustin Garcia**: perfecto, che.

**Damian Fritzler LB**: Buenísimo. Disculpen la demor se me pas estamos pasó la hora.

**Agustin Garcia**: No hay problema, no hay problema. Lo que sí que bueno, nada, si quieren arrancamos porque Gabo tiene un compromiso y tiene que estar yendo, tiene estar saliendo en 20 minutos.

**Damian Fritzler LB**: Vale.

**Agustin Garcia**: Así si quieren vamos a a ver un poco, les cuento, eh nos focalizamos un poco ahí en lo que me pediste Ami, que básicamente es ver cómo e digamos se nosotros tenemos este nuevo módulo de reportes, los reportes se pueden generar con la inteligencia artificial y básicamente están pensados para poder distribuir y compartir en un entorno con digamos otros usuarios, ¿no? Entonces ahí en función de la información que ya habíamos engestado en la vez anterior con la información del IRP, armamos algunos reportes como para mostrarles de ejemplo. Así que si les parece bien, vamos a ello.

**Damian Fritzler LB**: Sí,

**Gabriel Puertas**: Dale.

**Damian Fritzler LB**: dale.

**Gabriel Puertas**: Bueno, si va a decir algo.

**Damian Fritzler LB**: No, lo que quería entender es a ver si se entendió.

**Gabriel Puertas**: Dale.

**Agustin Garcia**: Buenísimo.

**Damian Fritzler LB**: Yo puedo no usar algún agente clouding lo que sea para obtener la información desde la plataforma directamente de Teram.

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: Okay,

**Gabriel Puertas**: ahora te muestro. Mira, vamos por parte. Yo acá lo que tengo cargado,

**Damian Fritzler LB**: perfecto.

**Gabriel Puertas**: este es el caso, el WordPace Luigi Bosca que me resulta supermolesto. Usted cualquiera, yo dejo de verlos, pero cosa me dicen. Yo acá tengo cargada la fuente de datos que que nos pasaron. Nada, eh, yo le puse nombre de W, pero tiene nada. Si me si me voy a fijar acá, ustedes nos compartieron 16 tablas que son estas, cada uno con su dato, el todo el tema. Nosotros eso lo ingestamos y bueno, en particular eh yo lo empecé a consumir con uno de estos modelos. Ahora, para poder consumirlo, nosotros tenemos acá un asistente que es, perdón, este que es el el que tenemos embebido en la página que te permite hacer todo lo que yo le voy a mostrar que hice con Cloud,

**Damian Fritzler LB**: Ah. Yeah.

**Gabriel Puertas**: No. Este agente como nosotros lo tenemos expuesto, la versión que está expuesta en la página es un agente barato, por así decirlo, pero nosotros nos podemos poner de acuerdo con ustedes y elegir el el mejor la agente que que más le convenga, digamos, ¿no?

**Gabriel Puertas**: En ese sentido puede ser cualquiera y se lo asignaríamos a ustedes en esto. Lo que yo puse acá, esta vista vendría a reemplazar todo lo que yo hice con cloud que no estaba mostrando.

**Agustin Garcia**: He.

**Gabriel Puertas**: ¿Dónde estás? Acá estás acá. Todo lo que yo hice con Cloud vía un conector MCP, eh, lo podés lo lo podés hacer con con este agente que nosotros tenemos embriido en la página. Así que si si vos me dejas, yo te sigo mostrando porque yo en particular lo hice simplemente con cloud, pero pero si si a la gente que tenemos en la página le ponés cloud, termina pasando más o menos lo mismo,

**Damian Fritzler LB**: Sí,

**Gabriel Puertas**: ¿eh?

**Damian Fritzler LB**: mi pregunta, mi pregunta es,

**Gabriel Puertas**: Dale.

**Damian Fritzler LB**: no quiero contratar ningún agente de inteligencia artificial.

**Gabriel Puertas**: No lo va a contratar a nosotros,

**Damian Fritzler LB**: Puedo claro,

**Gabriel Puertas**: digamos. Y con eso te

**Damian Fritzler LB**: yo lo contrato Teramot. Aparte necesito contratar algo más de la licencia que me pasó Agustín para hacer uso de la información y la

**Gabriel Puertas**: no

**Damian Fritzler LB**: estructura o los reportes.

**Gabriel Puertas**: digamos para para hacer uso de todo eso. Sí. No sé qué te pasó, Agustín de la parte comercial, pero digo nada.

**Gabriel Puertas**: El motor de inteligencia artificial que que usaría está embebido en la página. Esa es un poco la respuesta. Y no necesitas contratar cloud. Yo lo que te quiero decir es que este el agente que está detrás de esta página nos podemos poner de acuerdo cuál es en función de cuál performe, cuál no cueste tan caros los tokens y toda esa historia. Eh, no sé si quedó

**Damian Fritzler LB**: o usar el

**Agustin Garcia**: Ahí, ahí. Daniel, una pregunta.

**Damian Fritzler LB**: nativo,

**Agustin Garcia**: digo, la idea de no usar una inteligencia artificial es por alguna

**Gabriel Puertas**: claro.

**Damian Fritzler LB**: ¿no? A ver, ¿cuál es el tema?

**Agustin Garcia**: restricción.

**Damian Fritzler LB**: Yo estoy comparando esta solución con lo que hoy tengo licenciado de de tablón y te hablo calzón

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: quitado. Digo, yo hoy en tabl tengo tanto esto,

**Gabriel Puertas**: sí.

**Damian Fritzler LB**: Teram me es un poco más caro, pero me da una solución superadora a lo que yo quiero. Ahora no me alcanza con Teramot para llegar a el entregable que hoy me da Tablo, que es el reporte que cada usuario puede consumir.

**Gabriel Puertas**: Así.

**Damian Fritzler LB**: necesitaría alguna gente de inteligencia artificial para hacer estos reportes.

**Agustin Garcia**: Mhm.

**Damian Fritzler LB**: Entonces ahí tengo que abarle el gasto o el costo de la gente de inteligencia artificial para migrar. tabló a más algo para llegar al mismo resultado. Vale, todo consumido.

**Gabriel Puertas**: Bien, bieno para entender voy.

**Agustin Garcia**: No. Okay.

**Gabriel Puertas**: Oui.

**Agustin Garcia**: Pero para, pero, para. Hago la pregunta, ¿por qué? Porque digamos vos los repteres podés armar con una licencia de clud o de una inteligencia artificial, inclusive también nosotros tenemos la capacidad de embeb digamos cualquier tipo de motor de inteligencia artificial sobre la plataforma, digamos. Inclusive ya hay viene con una versión que no es tan potente, pero te permite hacer un montón de cosas y vos con eso podrías generar los reportes. Después, digamos, eh esto te va a permitir la eficiencia de generar reporte de forma muy rápida. Sí, porque vos hoy si no en tabló como en Power BI, digamos, tenés un laburo manual para el armado de del tablero. Sí, esa parte te la vas a ahorrar. Ahora, no hace falta que todos los usuarios tengan licencia. Con que uno tenga la licencia para poder armar el tablero, ya para vos es suficiente. Inclusive si no quisieras contratarlo, nosotros lo podemos embeber y reemplazar a la gente que viene por default en el producto con el motor que del L el que vos necesites.

**Agustin Garcia**: Ahora ahí con eso resolviste el tema del armado del dashboard, que también por otro lado no es solo el armado del dashboard porque también te sirve para el curado de los datos, la interpretación del modelo, que es lo que habíamos visto con la ingesta de la data del IRP, digamos, como que tenés un usuario que te permite gestión, por así decirlo, aparte de explotación y digamos esos dashboard que vos armes después pueden ser los dashboard que le compartas al resto de los usuarios que no necesariamente Obviamente tienen que tener, digamos, un conector de inteligencia artificial.

**Gabriel Puertas**: Espera,

**Agustin Garcia**: Esa solución a vos te

**Damian Fritzler LB**: A ver, quiero aprovechar el tiempo de Gabriel.

**Agustin Garcia**: cierra.

**Damian Fritzler LB**: Eh, perdona usted, porque, a ver, yo me paro, tengo 100 usuarios de tablo.

**Agustin Garcia**: C.

**Damian Fritzler LB**: ¿Cómo van a conir la información que hay a

**Gabriel Puertas**: espera, espera.

**Damian Fritzler LB**: todos?

**Gabriel Puertas**: Esos usuarios de tablo, ¿qué hacen? Consumen los datos.

**Damian Fritzler LB**: Consumen, son viws

**Gabriel Puertas**: viewers y yo no me acuerdo te habló porque yo tenía una licencia que era la

**Damian Fritzler LB**: no no quedan tableros, solo lo visualizan.

**Gabriel Puertas**: que Y eso vos le pagas el

**Damian Fritzler LB**: Solo ven info.

**Gabriel Puertas**: Sí. Ah, bueno,

**Damian Fritzler LB**: Sí.

**Gabriel Puertas**: el el digamos en ese sentido vos podrías definir este dasor lo hice yo, vi a un agente, le dije, "Analíame los datos de Luigi Bosca. Fíjate qué cosas, qué cosas tiene que son raras para mí. para usted, ¿no? Pero detectó cosas de cómo usa la cómo cambian de moneda, varias particularidades más y le dije, "Bueno, hac un tablero comercial y me armó esto." Nada, esto ustedes lo pueden iterar 1000 veces. Cambio de colores, cambio de filtro, cambio de cosas que una vez que ustedes lo tienen a este tablero que que le van a poder agregar filtros, vistas, lo que sea, ustedes habilitan usuarios que sean Yeah. Y esas personas consumen esos tableros, o sea, van a tener eh postulado, o sea, no tienen que entrar a esta vista porque est en la vista de del que está creando ese tablero. Eh, y va a tener, por ejemplo, yo tengo acá uno que es comercial, esto creo que era comercial en ahí está en pesos y este es comercial en dólares. Nada, es lo que se me ocurrió a mí en el momento que lo hice.

**Damian Fritzler LB**: Y aí a consumirlo.

**Gabriel Puertas**: Eh, nosotros tenemos una vista, lo que pasa que yo no la tengo por el por el por el perfil que tengo,

**Damian Fritzler LB**: Okay.

**Gabriel Puertas**: pero digo, es como si fuese una vista acá, pero te voy a mostrar un poco acá. Es como si yo acá tengo todos mis Wordface,

**Damian Fritzler LB**: Ah,

**Gabriel Puertas**: pero imagínate esto, pero vos tenés tus dashboard y te aparecen listados los dashboard que te compartieron, digamos.

**Damian Fritzler LB**: perfecto.

**Gabriel Puertas**: Solo eso.

**Damian Fritzler LB**: Misma heramienta, que la potestad de ver no degenerar.

**Gabriel Puertas**: Claro.

**Damian Fritzler LB**: Perfecto.

**Gabriel Puertas**: Vos ves consultas este dasor le pega a las tablas que vos creaste. Fíjate que vos me compartiste estas 16 tablas que tiene, bueno, cada uno su nombre y bueno, yo en mis interacciones con el modelo generé una tabla que era ventas en línea, que que es esta que consume de todas estas otras tablas. Eh, acá está el código SQL que generó, pasa nada, no importa. Acá está la memoria de cálculo, eh, digamos, cuáles son los filtros que usó y toda esa historia. Y esta tabla se actualiza todos los días en tanto y en cuanto se actualiza los datos fues, ¿no?

**Gabriel Puertas**: Algo que yo no sé si vos habías visto,

**Damian Fritzler LB**: M.

**Gabriel Puertas**: Damián, esto ya es una herramienta para los usuarios que arman estas vistas. Todo lo que yo fui descubriendo sobre la particularidad de su información, a ustedes le debería hacer mucho sentido.

**Damian Fritzler LB**: Mira

**Gabriel Puertas**: Eh, esto esto es conocimiento compartido entre todos los usuarios editores.

**Damian Fritzler LB**: traducción.

**Gabriel Puertas**: Entonces, nada, yo me di cuenta, vamos al último. Ya me di cuenta que para el manejo de la moneda yo utilizo no sé que ciertos criterios donde tengo varios tipo de documentos que pasan de un lado al otro e o o por ejemplo acá incluye vamos a ver una central

**Damian Fritzler LB**: Ay!

**Gabriel Puertas**: gran eh comprobaste fiscales de ventas qué sumna signo, montoneto, tanto tan esto es un MD, ustedes lo deben conocer esto es básicamente para que todos los agentes que aficen a las personas que crean estos tableros compartan el conocimiento de las particulares de los datos que tienen ustedes. Eh, nada, eso me parece super importante comentártelo porque en la medida que lo van curando este documento ya todos los agentes eh codean mejor y pueden verificar. Este dashword es básicamente el código HTML que generan los usuarios.

**Agustin Garcia**: M.

**Gabriel Puertas**: M. eh que tienen todas las vistas, que tiene toda la capacidad de lo que usted le puedan pedir.

**Gabriel Puertas**: No sé si si le quieren pedir otro tipo de gráfico, le lo quieren le quieren cambiar el idioma, otros colores.

**Damian Fritzler LB**: El refr se hace en cada cada momento que ingreso,

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: ¿no? No, con la actualización

**Gabriel Puertas**: este refresh, este refresh sí se va, o sea,

**Damian Fritzler LB**: del

**Gabriel Puertas**: vos vas cada uno de estos gráficos es una query a esta tabla gold que yo te mostré, a esta y cada vez que vos entras al dashboard, yo refresco los datos de esta tabla a Gold.

**Damian Fritzler LB**: si yo te doy datos frescos ahí,

**Gabriel Puertas**: Pero claro,

**Damian Fritzler LB**: actualiza. Perfecto.

**Gabriel Puertas**: pero esta tabla Gold se actualiza con la frecuencia que vos lo definas,

**Damian Fritzler LB**: Listo.

**Gabriel Puertas**: ¿entendés?

**Damian Fritzler LB**: A ver.

**Gabriel Puertas**: Yo me voy a buscarte tus datos fuente con la frecuencia que vos me digas. Puede ser una vez por día, una vez por hora, una vez por no sé.

**Damian Fritzler LB**: Okay,

**Gabriel Puertas**: Bueno, distinto.

**Damian Fritzler LB**: Gabi. Entonces,

**Gabriel Puertas**: Sí,

**Damian Fritzler LB**: el armado de los dashboard sí o sí lo tengo que hacer con un agente.

**Gabriel Puertas**: sí, pero eh no logro entender si eso te hace el ruido o no.

**Damian Fritzler LB**: Podemos

**Gabriel Puertas**: Es básicamente se lo se lo pedís.

**Damian Fritzler LB**: centralizarlo.

**Gabriel Puertas**: Para mí es mágico. Yo usé mucho tabló y todas esas cosas y bueno, nada,

**Damian Fritzler LB**: Yo estoy de acuerdo con vos.

**Gabriel Puertas**: quiero no volver a hacerlo nunca más en mi vida,

**Damian Fritzler LB**: No, no, Gabriel. Y esto recontra superador.

**Gabriel Puertas**: digamos.

**Damian Fritzler LB**: Lo que quiero entender es todo y yo en mi conocimiento digo, entro, quiero hacer un dashboard, necesito contratar alguna gente, uso de ustedes,

**Gabriel Puertas**: No,

**Damian Fritzler LB**: tiene un costo y eso y tiene un

**Gabriel Puertas**: usa el nuestro. Usa el nuestro.

**Agustin Garcia**: Igual

**Damian Fritzler LB**: costo pero los token no están dentro de

**Gabriel Puertas**: los token.

**Damian Fritzler LB**: los 000 que me pasó. ¿Cómo

**Gabriel Puertas**: Ah, perdón, Agustín, ahí contesta vos porque yo suelo embarrarme con estas cosas,

**Agustin Garcia**: para Dami igual SC ahí,

**Damian Fritzler LB**: se

**Agustin Garcia**: Dami tenemos que volver a charlar un poco cuál es el alcance, pero en la primera instancia era el tema de los datos,

**Gabriel Puertas**: Pero

**Agustin Garcia**: digamos, si lo vemos, o sea, y qué necesitas, o sea, digamos Podemos revisar el número.

**Agustin Garcia**: Digo, porque me parece que cambió el alcance de lo que habíamos visto.

**Damian Fritzler LB**: listo? Pero a ver, volvemos entonces. Vamos a la funcionalidad.

**Agustin Garcia**: Sí,

**Damian Fritzler LB**: Puedo un agente inteligencia artificial voy a tener que tener y voy a tener que contratar tokens.

**Agustin Garcia**: C.

**Damian Fritzler LB**: Ahora veré con ustedes qué licenciamiento me conviene más. Sí, lo uso a través de ustedes, uso a través de alguna inteligencia externa,

**Agustin Garcia**: Perfecto.

**Damian Fritzler LB**: consumimos con los token compro límita, veo. Lo puedo hacer siempre necesito un agente, por lo menos uno para generar los datos. Esa es la función, esa es la forma con la que se construyen los los esquemas de datos, ¿verdad?

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: Los reportes.

**Agustin Garcia**: Correcto,

**Damian Fritzler LB**: Bien. Okay, ahora puedo tener uno varios, cada uno puede hacer lo suyo,

**Agustin Garcia**: correcto.

**Damian Fritzler LB**: los puede compartir. Después gobierno con quién lo comparto, con quién no, pero tengo la potentad únicamente consumir.

**Gabriel Puertas**: Exactamente.

**Damian Fritzler LB**: Bien,

**Agustin Garcia**: Correcto.

**Damian Fritzler LB**: hasta ahí los entendí perfecto.

**Damian Fritzler LB**: el el uso.

**Agustin Garcia**: Perfecto.

**Damian Fritzler LB**: Si yo contrato solamente un agente para la creación,

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: ¿puedo darle acceso a más de un usuario a ese agente?

**Gabriel Puertas**: Sí, hay usuarios que no hacen eso.

**Damian Fritzler LB**: Porque va por token.

**Gabriel Puertas**: Eh,

**Damian Fritzler LB**: el

**Gabriel Puertas**: ponerle un cloud. Yo me contrato un cloud de ay,

**Damian Fritzler LB**: channel.

**Gabriel Puertas**: no sé por qué me hace esto y que no la puedo ver la página. Bueno, espérenme un segundito. Eh, yo me contrato un seat de cloud, este, que son, creo que está por decirle, y le doy contraseña a varias personas, también lo van a poder usar. O sea, nosotros es el el mismo cludel que está generando los dashboard. Lo que le va a pasar a ese sit eh sin token más rápido o ustedes tengan que pagar más token. Pero que no pasa nada. unat de un seat de cloud hoy cuesta y bueno, tiene todo lo que te permite hacer cloud y y vos lo conectas, tiramos y lo usas de ahí. Lo que nos está pasando muchas veces a nosotros que nada, darle seats a empleado en algunas empresas cuesta mucho más decir, "Bueno, arregla con Agustín, le doy a la gente a través de Teramot y lo usan por ahí.

**Damian Fritzler LB**: Okay,

**Gabriel Puertas**: Eso nosotros tenemos queir en la página.

**Damian Fritzler LB**: pero existe la opción, digamos, de hacer el se para que múltiples consulten.

**Gabriel Puertas**: No, eso es lo que te digo. O sea, si vos hacés un te contratas un sit de cloud, eh, y le pasas la contraseña a varias personas, son varias personas usando el mismo pegándole todo a Teramot, te vas a quedar sin token de cloud. Eso es lo que te digo.

**Damian Fritzler LB**: Está clarísimo,

**Gabriel Puertas**: No sé si fue

**Damian Fritzler LB**: ¿no? Está clarísimo, está clarísimo. A ver, estoy ahí terminando de ultimar detalles.

**Gabriel Puertas**: claro.

**Damian Fritzler LB**: junto la semana que viene con la chica de de FPN para para revisar unos datos que ella usa es bastante complejo,

**Agustin Garcia**: Bien.

**Damian Fritzler LB**: donde usa información externa. Eh,

**Gabriel Puertas**: Ahí va.

**Damian Fritzler LB**: me voy a juntar con ella porque a mí me gustaría desafiar junto con ella a ver si llegamos algo

**Gabriel Puertas**: ¿Y

**Damian Fritzler LB**: parecido a lo que ella suele hacer porque dice es bastante complejo, con lo cual me parece que está bueno para desarlo a ver cómo entiende los datos. e lo ven viable poder

**Gabriel Puertas**: qué datos vos disponés de los

**Damian Fritzler LB**: hacerlo.

**Gabriel Puertas**: datos?

**Damian Fritzler LB**: Son los datos de ella que te los van a beber ahí en el momento en un Excel más la información de de Advalor.

**Gabriel Puertas**: Bien.

**Damian Fritzler LB**: Ahí lo que me gustaría hacer, chicos, y ya entrando quizás un poco más en detalle para poder hacer un análisis de verdad, lo voy a tener conectado a base de datos de producción, con lo cual ahí me gustaría que firmemos algo y que ustedes se puedan conectar a la base de datos de producción. Me parece que va a ser lo mejor. Así veo el dato contra lo que ella sueleaburar que lo va a entender al toque todo enviable.

**Gabriel Puertas**: Dale.

**Agustin Garcia**: Okay,

**Gabriel Puertas**: Sí,

**Agustin Garcia**: nosotros estamos super acostumbrados.

**Gabriel Puertas**: obvio.

**Agustin Garcia**: Vamos a firmar en D y es parte del proceso porque los datos eh siempre son sensibles. Así que en ese sentido despreocupate. Si ya tenés un NDA que me quieras compartir, eh,

**Gabriel Puertas**: Ok.

**Agustin Garcia**: así avanzamos, dale para adelante y nada, y hacemos la ingesta y si vos tenés también algún modelo ya o algún reporte que puedas compartirnos como para que nosotros vayamos dándole forma también a a esa reportería de nuestro lado también como para ir ahorrando tiempo.

**Damian Fritzler LB**: Sí. A ver, lo que voy a querer ver es justamente la capacidad que tiene la herramienta de de

**Agustin Garcia**: Ok.

**Damian Fritzler LB**: hacer en vivo. Eh, entonces lo que sí les voy a pasar es quizar toda la conexión a la base de datos productiva nuestra. Si ya lo tienen eso sí hecho, me parece que está bueno pedo que lo hagamos. Igual la vez pasada fue nada, pero ahora va a ser toda la la la base y en el momento nada, ella la idea es que transaccionen ustedes pase cuál es el Excel e ella te diga, "Che, pedir esto, esto y esto, filtrarlo de esta manera me tiene que dar esta información, le va a hacer alguna pregunta a ver si llega algo parecido a lo que llegó el mes pasado."

**Gabriel Puertas**: Dale.

**Agustin Garcia**: Perfecto, perfecto,

**Damian Fritzler LB**: Sí.

**Agustin Garcia**: ningún problema. Es algo que solemos hacer, así que en ese sentido eh no no hay problema.

**Damian Fritzler LB**: Okay, me llevo eso. E no quiero sacarle mucho tiempo a Gab que me dijiste que se está yendo. Agustín, hagamos una cosa. me podrás pasar quizás eh o nos quedamos charlando un toque a ver cómo sería esta

**Agustin Garcia**: Dale,

**Damian Fritzler LB**: esta este modelo quizás con el que nosotros necesitaríamos transaccionar en un principio.

**Agustin Garcia**: vale.

**Gabriel Puertas**: ahí.

**Agustin Garcia**: Si querés lo liberamos a Gabi

**Gabriel Puertas**: No sé si Dale, dale. Yo le no llegamos, pero ahí yo básicamente lo que le pedí es hacerme un dashboard de marketing.

**Agustin Garcia**: youtuber

**Gabriel Puertas**: Eh, no sé. Eh,

**Damian Fritzler LB**: Aha.

**Gabriel Puertas**: yo debería poder a ver si me lo publicó y me debería venir el de marketing y me hizo el que no me falla. Ahí está.

**Damian Fritzler LB**: Mira más o la línea

**Gabriel Puertas**: el das market ese es el tiempo que demora, digamos, eso digamos y nada,

**Damian Fritzler LB**: Eh,

**Gabriel Puertas**: de ahí obviamente esta chica va a tener más sentido porque yo le pedí un un tablero de

**Damian Fritzler LB**: nada.

**Gabriel Puertas**: marketing, un prom bastante escueto, pero digo, ese es un poco la dinámica cuando vos llegas a a exactamente lo que querés y te gusta y incluso CL CL estos modelos son muy buenos proponiendo, eh, te gustó lo publicas y se le da acceso a las personas que que cree que lo vean. Esa esa es la dinámica, ese es el tiempo que te toma armar todo este das con estos modelos. Eso para mí es muy superador,

**Damian Fritzler LB**: No, no, no.

**Gabriel Puertas**: digamos.

**Damian Fritzler LB**: Estamos de acuerdo, Gabriel. Son dos cosas distintas. Si estás hablando de un Falcon un auto híbrido de hoy.

**Agustin Garcia**: Yeah.

**Damian Fritzler LB**: Lo que digo es em yo tengo usuarios también de marketing, pero eligen usar Gemini porque tienen banana, usen distintas herramientas, podrían convivir las dos tecnologías, ¿verdad? Los dos proveedores de Okay,

**Gabriel Puertas**: Sí, sí, sí, sin duda. O sea, lo que nosotros hacemos es la capa de datos,

**Damian Fritzler LB**: buenísimo.

**Gabriel Puertas**: digamos. Ellos posiblemente le pongan un poco más de de coso,

**Damian Fritzler LB**: Se puede editar manualmente también,

**Gabriel Puertas**: pero digo,

**Damian Fritzler LB**: ¿no? ¿Qué cosa? el dashboard,

**Gabriel Puertas**: va.

**Damian Fritzler LB**: porque el dashboard te genera el código que lo mostró una parte de la vista. Tengo una consulta, Gabrieto, porque tenemos también usuarios por ahí más capacitados que eh por ahí cuando llegan a un escenario donde ya está casi casi final, el último detalle fino lo pueden tocar por código o hacer alguna relación o sumarun. esa posibilidad también existe de seguirlo trabajando manualmente el

**Gabriel Puertas**: A vos te gustaría tener el código de este HTML.

**Damian Fritzler LB**: código, la relación

**Gabriel Puertas**: Ah, el que el que yo te mostré son estos. surge, digamos, ¿qué es lo que hace Teramot como fuerte? Porque los das son una capa de visualización. Es cuando yo te creo capas agrupados. Fíjate que yo no tengo ni la menor idea que tienen estos datos. La menor idea, ¿eh? Entonces, lo que te hace es armar estas estas tablas agrupadas con inteligencia de negocio, con todos los filtros que hacían falta. arma el ETL desde la base productiva. Nosotros, eh, fíjate que esta tabla de la que a la que yo le estoy leh,

**Damian Fritzler LB**: Claro.

**Gabriel Puertas**: perdón, esta no, esta a la que yo le estoy pegando la la general de ventas es una tabla

**Damian Fritzler LB**: Sí, era precisamente ahí.

**Gabriel Puertas**: que le pego a todas estas tablas.

**Damian Fritzler LB**: Generó todo ese código.

**Gabriel Puertas**: Ahí va. Y yo te pongo este código. Vos lo miraste el código,

**Damian Fritzler LB**: Claro.

**Gabriel Puertas**: ¿no te gustó? Acá tenés,

**Damian Fritzler LB**: Ahí va.

**Gabriel Puertas**: acá tenés como las instrucciones que yo le di para hacer ese código.

**Gabriel Puertas**: Entonces, vos, por ejemplo, vamos en detalle, eh, hacer el filtro, solo comprobantes fiscales de venta, incluir eh factura A, factura B,

**Damian Fritzler LB**: Bien,

**Gabriel Puertas**: factura C.

**Damian Fritzler LB**: por eso yo puedo editar ahí y excluir el que digo en lugar de pedirle la vengo acá, edito, saco este comprobante, listo.

**Gabriel Puertas**: Total,

**Damian Fritzler LB**: Bien,

**Gabriel Puertas**: total,

**Damian Fritzler LB**: esaulta.

**Gabriel Puertas**: eso lo hacé, va a correr y te genera el SQL nuevo.

**Damian Fritzler LB**: Buenísimo.

**Gabriel Puertas**: Te digo más, te lo querés llevar al SQL y plantarlo en el servidor y que esta tabla ya sea una fuente de entrada, también lo puede hacer.

**Damian Fritzler LB**: Y también y también puedo tocar la inscripción de ahí o tocar directamente el SQL y decir, "Che, borro esta consulta, edicto, quiero que esto sea así."

**Gabriel Puertas**: Claro, el SQL todavía nosotros no lo dejamos porque vía SQL vos podés hacer cosas medio raras, pero sí le podés pedir al modelo, cambiame esta parte del SQL, si es que vi acá, no sé,

**Damian Fritzler LB**: Pero para

**Gabriel Puertas**: si cambiame esta parte del SQL por otra y te lo va a hacer.

**Damian Fritzler LB**: bien.

**Gabriel Puertas**: Sí.

**Damian Fritzler LB**: Yo esto lo puedo hacer también por por base de datos, pero lo único que quiero que hagas es un select.

**Damian Fritzler LB**: Jamás te voy a pedir que actualices datos a través de esto. Eso lo

**Gabriel Puertas**: No, no,

**Damian Fritzler LB**: puedo

**Gabriel Puertas**: o sea, esto lo que funciona como warehous, son capas de consulta. M.

**Damian Fritzler LB**: sé yo.

**Agustin Garcia**: Yeah.

**Damian Fritzler LB**: ช. y mi base de datos,

**Gabriel Puertas**: No, pues yo a tu base de datos lo único que yo le hago en esta versión es una vez al día o con

**Damian Fritzler LB**: porque

**Gabriel Puertas**: la frecuencia que vos definas acá me traigo toda la fuente de datos que que vos me compartiste, que son estas 16 tablas. O sea, yo voy una vez al día y me copio toda esta estas tablas.

**Damian Fritzler LB**: y trae tu escribe, ¿cómo te conectaste?

**Gabriel Puertas**: Todo lo que hagas después lo hacés en la nube de Teramot.

**Damian Fritzler LB**: No,

**Gabriel Puertas**: Bueno,

**Damian Fritzler LB**: ya sé cómo te conectaste a la base de

**Gabriel Puertas**: le seguís pegando a tu servidor,

**Damian Fritzler LB**: datos.

**Gabriel Puertas**: eh, con el conector. Acá tenemos que yo lo voy a tener que dejar porque si no mi hijo me va a hacer un paro

**Damian Fritzler LB**: Yo lectura.

**Gabriel Puertas**: sindical, pero digo, nosotros tenemos todos estos tipos de conectores y estos conectores sonar, digamos.

**Damian Fritzler LB**: Listo. Yo lo filtro desde mio.

**Gabriel Puertas**: Bueno, chicos, yo los dejo.

**Damian Fritzler LB**: Perfecto.

**Gabriel Puertas**: Chao.

**Agustin Garcia**: Gracias, Sí,

**Damian Fritzler LB**: A ver cómo hacemos con esto se ocurre.

**Agustin Garcia**: mira, eh yo entiendo que el objetivo es reemplazar tabló. Sí, yo lo que creo es que esto lo pueden considerar como eh primero una herramienta en donde, por ejemplo, tal vez hay que considerar 100 usuarios viewer y cinco 10 usuarios con capacidad de administración. vos no querés, digamos, conectar eh cloud, podemos tener el agente embebido que probablemente para esas operaciones vaya a a ser suficiente. Y si querés que la gente de marketing tenga la capacidad de explotar los datos que serían como usuarios, digamos de gestión, o sea, no solo viewers, digamos, vamos considerar un paquete de 10 usuarios de gestión, 100 usuarios viewer para el tema de los reportes, eh, y nada,

**Damian Fritzler LB**: Vale.

**Agustin Garcia**: y con eso o inclusive también podemos pilotearlo en un formato más pequeño con algún área en específica que use tableros como para que ustedes también digamos se familiaricen con con la herramienta. Yo el único tema que tengo que cuando tenemos que hacer una prueba de concepto y el volumen de datos a ingestar es muy grande, empiezo a entrar en costos, ¿entendés?

**Agustin Garcia**: Porque digamos tenemos que mover toda una base,

**Damian Fritzler LB**: Ah,

**Agustin Garcia**: ¿entendés?

**Damian Fritzler LB**: no está

**Agustin Garcia**: Yo ya se entiende. Capaz que esto es con un, no sé, un set lo que venimos haciendo con muchas otras empresas, bueno, saquemos los últimos 3 cu meses de data, que la usamos para explotar y con eso ya podemos hacer reporte de similares reportes a los que

**Damian Fritzler LB**: No,

**Agustin Garcia**: están o

**Damian Fritzler LB**: voy a hacer otra cosa distinta.

**Agustin Garcia**: entendés.

**Damian Fritzler LB**: Yo voy a ver cuáles son las fuentes de datos que usa ella y voy a obtener la fuente de datos con el periodo que va analizar con la estructura. Eh, así. No, no te entrar en costos al pedo, que no vamos a consumir datos al pedo.

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: Hagamos eso. Eso por un lado, eso quédate tranquilo, yo lo resuelvo. Pero quiero entender, a ver, yo tengo las licencias y tengo también los tokenes.

**Agustin Garcia**: Sí, sí. Mira, eh yo te digo la verdad, o sea,

**Damian Fritzler LB**: Ok.

**Agustin Garcia**: eh y un poco viendo las implementaciones que tenemos en otros clientes, o sea, en una primera instancia, digamos que que el costo de la de la licencia nuestra no es algo tan significativo comparado con lo que te habló, estoy seguro que ahí vas a tener un ahorro importante.

**Agustin Garcia**: Después, una cosa que termina pasando, ¿cómo?

**Damian Fritzler LB**: Es que ahí ya voy perdiendo.

**Agustin Garcia**: ¿Cómo?

**Damian Fritzler LB**: Yo hoy de tabló pago ,000 al año y con los 2000 de ustedes ya entro para atrás. Pero el 9 también tiene un disclaimer, tiene un un beneficio. Ahora, si le sumo después inteligencia artificial, los tokens que no sé cuánto me voy a consumir y voy a tener una primera etapa donde los usuarios van a preguntar a manzara el costo de los se van a disparar. Es que para mí ahí por ahí lo que tenemos que tener es hacer los tokens con seguramente vamos a tener una carga de token alta para reproducir los mismos tablero que tenemos hoy y después disponibilizacer y disponibilizar eso. No vamos a tirar tablero al loco. No, yo estoy acuerdo. Va a ser un va a haber un pico de token y después no va a tener que usarse

**Agustin Garcia**: Pero la verdad también digamos que para la generación

**Damian Fritzler LB**: tokens.

**Agustin Garcia**: de los dashboard el consumo de tokens si los datos están bien estructurados no es algo que hasta acá hayamos tenido como tema, ¿entendés? Que de repente, ah, si no hubo que saltar de licencia porque no nos quedamos cortos.

**Damian Fritzler LB**: He.

**Agustin Garcia**: En ese sentido, ¿no? Inclusive lo que hacen algunos clientes es tienen un usuario o dos que son los que gestionan el datalake y que arman los dashboard y los reportes. Inclusive chat ya chat venimos con varios pilotos de este módulo de de porque básicamente vieron la facilidad para armar el dashboard, ¿no? Entonces armar el dashboard, lo publican y ya ahí ya no tenene más consumo de token. El consumo de token se dio en el armado del dashboard. Ahora, lo que termina pasando es que, por ejemplo, en en el área que controla la plataforma y todo, tienen uno o dos usuarios para la generación de dashboard, el manejo de los datos, qué s yo, y después son todos usuarios viewer y lo que sí están haciendo es les dan eh licencias eh para la conexión del MCP a a los directores o a las cabezas de equipo, ¿entendés? Que estos son los que pueden explotar. la información porque bueno, también tener la información disponible y poder conectarle ahí, ¿entendés? un módulo de inteligencia artificial para sacar provecho de la info.

**Damian Fritzler LB**: Sí.

**Agustin Garcia**: y es donde está hay una ventaja importante ahí. Entonces, pero bueno, digamos, nosotros podemos en conectar la inteligencia artificial que ustedes quieran, pudiendo controlar tema de token o licencia o también pueden usarlo la de ustedes, ¿entendés?

**Agustin Garcia**: Entonces, en ese sentido, si vos tenés a tus usuarios que, por ejemplo, líderes, eh, le das una licencia de $ de cloud o de 100, bueno, dependerá de de tu necesidad. Ahora, estás hablando de otra cosa, ¿no? Tabló eh quedó, digamos, el tema de tabló lo podemos resolver eh de una forma más sencilla, ¿sí? O sea, con un usuario crear los dashboard, eh, y después que sean todos viewer, ahí el problema, digamos, lo tengas

**Damian Fritzler LB**: Okay. Tengo una pregunta. Eh,

**Agustin Garcia**: resuelto.

**Damian Fritzler LB**: ¿tenés alguna implementación parecida ya el volumen estructura parecida a la de nosotros con 100 usuarios? viewer y que estén saliendo de un vi estructurado a

**Agustin Garcia**: Hoy no llegamos a 100 usuarios viewer,

**Damian Fritzler LB**: la

**Agustin Garcia**: pero tenemos clientes que están subiendo de a 15 usuarios por mes, por ejemplo, y de tendría que ver ahora en cuánto están los que ya vienen bastante avanzados,

**Damian Fritzler LB**: y

**Agustin Garcia**: pero pero aparte también, digamos, el tema es, perdón, eh el tema es nosotros no tenemos un problema de capacity técnico en ese sentido porque los reportes son HTML ya pregenerados. Entonces,

**Damian Fritzler LB**: no Está claro,

**Agustin Garcia**: digamos,

**Damian Fritzler LB**: está claro.

**Agustin Garcia**: no es que no es que un tema de de consumo de de fierro, o sea,

**Damian Fritzler LB**: Lo que necesito que me ayude es quizás con 50 tableros.

**Agustin Garcia**: porque

**Damian Fritzler LB**: ¿Cuánto cuánto levamos? 70 tableros. Sí, 70 y pico. 70 80 tableros a desarrollar. ¿Qué token consumiendo esas empresas hoy en Guita? ¿Se entiende?

**Agustin Garcia**: Eu

**Damian Fritzler LB**: Para yo entender, a ver, voy a tener un pico de los tres primeros meses de $500, después baja 200 y después estabilizado voy a consumir $. No lo sé, pero necesito entender un poquito ese flujo. A ver si vos me podés ayudar sin certero, sin darme nombre, nada, pero entender un poquito con esta cantidad de tableros de IRP, CRM y algún dato externo, algún dos trer para entender cuál va a ser mi mi flujo de caja para poder después justificar,

**Agustin Garcia**: Claro,

**Damian Fritzler LB**: salir

**Agustin Garcia**: vos vos lo que necesitás es estimar cuánto puede llegar a ser el costo de la implementación, por así decirlo, y después, obviamente, eh, del mantenimiento de la licencia mensual.

**Damian Fritzler LB**: Claro, implementación entre comillas porque a ver, yo te lo voy a tirar más más armadito y ahí voy a consumir mucho menos.

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: El tema va a estar cuando le dé a un usuario quizás la potestad de armar algún tablero y le diga, "Bueno, van a poner a jugar con la información que vos sostenés de un proveedor que pasa de estadística. Listo. Quiero darle esa potestad usuario porque hoy no lo tengo y es un beneficio que voy a poder darle con la herramienta.

**Agustin Garcia**: Claro,

**Damian Fritzler LB**: Eso está clarísimo,

**Agustin Garcia**: claro.

**Damian Fritzler LB**: pero lo que tengo que ver hoy y más que nada hoy en Argentina, en la industria vinícola, en ese contexto, ¿cuál va a ser mi flujo para salir de un licenciamiento de menos de $2,000 por m que hoy tengo en tablón a algo un poco más costoso pero que es superador? Bueno, listo. Pero en la incrementación, ¿cuál va a ser mi flujo?

**Agustin Garcia**: Claro,

**Damian Fritzler LB**: ¿Cuánto voy a tener que esforzarme para tener un mejor beneficio, se entiend?

**Agustin Garcia**: perfectamente.

**Damian Fritzler LB**: Nosotros aparte hoy tenemos un hoy tenemos un costo que no está medido, que es tenemos los dos usuarios que realizan, generan tableros, editan y modifican, que yo no sé hoy cuánto editan y cuánto modifican en el día a día, pero que cuando esté con el agente va a generar un consumo de token.

**Damian Fritzler LB**: Claro.

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: Indiferentemente hacer como dice AI la el show de la primer salida. Después en el día a día van tocando, pero como me decís vos, che, puedo tocar código, no me consume toque, no puede pedérselo por el agente. Entonces eso es como, che, hoy le puedo facilitar el laburo que consuma token y que lo pide o puedo seguir con la vieja escuela de che, el mantenimiento no me consuma token, hacerlo por código. Exacto.

**Agustin Garcia**: Claro, claro, claro. No, no, pero está clara la idea de, o sea, está clara la necesidad, digamos,

**Damian Fritzler LB**: Pero

**Agustin Garcia**: en ese sentido. Yo inclusive es más creo que como todo, ¿no? Bueno, la implementación, el armado de los dasur va a tener un consumo extraordinario que después va a desaparecer y va a ser algo ocasional, ¿no? Cuando tengas que armar un tablero nuevo o modificar algún tablero que, bueno, ya vieron, digamos, eh la rapidez de de cómo se se hace, ¿no? Ahora, inclusive te digo una cosa, si ustedes ya tienen los tableros armados, creo que hasta eso podría simplificar la implementación, porque hoy no es lo mismo vos pedirle todo el a decirle, "Che, arm un tablero igual a este con la fuente de datos que está acá,"Entés, o sea, como que inclusive hasta puede ser más rápido.

**Agustin Garcia**: Si quieres lo que podemos hacer y lo veo con los chicos y te cuento ahí, Dami nada, hasta podemos sacar un benchmark de qué consumió en el un tablero en particular como para que vos tengas una idea,

**Damian Fritzler LB**: Eso yo

**Agustin Garcia**: porque yo creo que el costo no es tan significativo, o sea,

**Damian Fritzler LB**: creo que tampoco,

**Agustin Garcia**: inclusive hasta acá

**Damian Fritzler LB**: pero lo que lo que no puedo es que me sorprenda la factura en la mano.

**Agustin Garcia**: sí lo que no querés es cuando termine el primer implementación y te llegue la factura. No, no, no querés sorpresas.

**Damian Fritzler LB**: Exacto.

**Agustin Garcia**: Me queda claro.

**Damian Fritzler LB**: Yo lo que quiero poner sobre la mesa es el modelo de verdad de lo que va a pasar.

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: Y yo sabiendo lo que va a pasar, nada, todos sabemos que es donde queremos ir,

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: que es una herramienta que sin lugar a duda es superadora, que para el momento donde estamos, yo estoy convencido que esto tenemos que ir. Eso aú quizás ya sabés, es fácil vender algo que está bueno,

**Agustin Garcia**: T.

**Damian Fritzler LB**: con lo cual no te estoy no te estoy regalando nada, pero a lo que voy es no me quiero sorprender con la otra contrapartida.

**Agustin Garcia**: Claro.

**Damian Fritzler LB**: Vos para poder vender tu producto necesitás de un tercero,

**Agustin Garcia**: No.

**Damian Fritzler LB**: de un predor tercero, que es el que me puede sorprender. No quiero que me sorprenda. Ayúdame a dimensionarlo con tu experiencia.

**Agustin Garcia**: Perfecto, perfecto. No, inclusive también digamos podemos hacerlo con los agentes internos que tenemos, o sea, eso de hecho es más eh eh lo veo como para charlarlo con los chicos y no te preocupes, yo te acerco una propuesta integral con esto, teniendo en cuenta esto y haciendo una estimación aproximada, porque inclusive si lo podemos hacer con el agente interno, te saca de del mapa el tema del potencial riesgo del costo adicional, ¿entendés?

**Damian Fritzler LB**: Đ

**Agustin Garcia**: ¿Entendés? Y ya con eso para vos puede ser una solución. Entonces, e nada, me quedó claro el tema. Yo lo veo con los chicos y y vuelvo a vos eh lo antes

**Damian Fritzler LB**: Vos tenés los select de cada tablero.

**Agustin Garcia**: posible.

**Damian Fritzler LB**: Sí. Eh, no, pero entrando tabl tienen que estar. Los puedo ver si ni sique. A ver, yo lo que estoy pensando, le puedo pasar la consulta. Exacto. Exacto. Ya habiendo analizado que trabaja con vistas. Si yo lo que quiero eliminar son las listas, pero podemos sacar los de las listas. Bueno, dale, hagamos esto. Ago, si te parece, ayúdame con esto. Yo me voy a a hacer este set de datos chiquitito, así no no te genera un gasto fuerte para para la demo que hagamos con con Eli, que es la chica de y y nos juntamos la semana que viene, ¿te parece? Te confirmo después de haber Te confirmo después de haberme juntado con ella.

**Agustin Garcia**: Me parece bárbaro.

**Damian Fritzler LB**: ¿Dónde estoy parado?

**Agustin Garcia**: Dale, dale,

**Damian Fritzler LB**: Sí.

**Agustin Garcia**: dale. Yo apenas tenga un feedback de esto, te cuento como para que vos también ya lo tengas en el radar.

**Damian Fritzler LB**: Gracias.

**Agustin Garcia**: Esto.

**Damian Fritzler LB**: Muchas gracias, Agustín.

**Agustin Garcia**: Gracias a ustedes, chicos. que estés bien. Chao.
