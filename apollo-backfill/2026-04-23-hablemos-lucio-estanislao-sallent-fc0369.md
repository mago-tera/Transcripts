# Hablemos !  Lucio  (Estanislao Sallent)

**Fecha:** 2026-04-23T19:26:16.632+00:00  
**Duración:** ~47 min  
**Participantes:** Dana Perelmuter <dana.perelmuter@inspectia.ai>, Estanislao Sallent <estanislao@inspectia.ai>, Lucio Rojas <lucio@teramot.com>  
**Externos:** dana.perelmuter@inspectia.ai, estanislao@inspectia.ai  
**Apollo ID:** 69ea7d80a2a5690019fc0369

---

**Lucio Rojas**: Bueno, ¿Cómo andan? ¿Todo bien?

**Estanislao Sallent**: Muy bien. ¿Vosotros? Me siento a Dana, desarrolladora del equipo.

**Lucio Rojas**: Dana, desarrolladora. ¿Que datos por dónde viene?

**Dana Perelmuter**: Un poco de todo en realidad, pero soy más del lado IA que otra cosa.

**Lucio Rojas**: Perfecto. Sentido. Bueno, un poco. Un gusto, Dana. Un poco la idea, Stanislabo, si no me confundo, es volver a mostrarle la herramienta a Dana para que ella.

**Estanislao Sallent**: Yo no traje ahora para esta reunión, pero tengo un cliente que creo que está. Está para hacer la prueba, con lo cual después te aviso y activamos la prueba y después. Pero antes quería ver el tema comercial que habíamos visto de che, bueno, ¿Cómo sería el esquema? Nosotros usarlo como parte del desarrollo que yo le voy a dar a clientes. Entonces, entre técnico de cómo se implementaría esa parte, hasta comercial, ¿Cómo sería? Si con más de una licencia, una licencia, costo por uso, bueno, nada, etcétera. ¿Cómo funcionaría eso?

**Lucio Rojas**: Bueno, perfecto. ¿Por dónde te parece que arranquemos?

**Estanislao Sallent**: ¿Por lo comercial o por lo técnico primero para verlo?

**Lucio Rojas**: Dale. Bien. ¿Querés que trabajemos sobre el caso de uso de este cliente? Que pensemos cómo. Como. ¿Querés ver una demo para Dana? Todavía no, una demo para Dana.

**Estanislao Sallent**: Yo ahora no tengo las bases por eso, porque todavía no terminé de confirmar que el cliente esté para hacer la prueba.

**Lucio Rojas**: Bien, perfecto.

**Estanislao Sallent**: Así que yo haría una demo normal.

**Lucio Rojas**: Bien, bien.

**Estanislao Sallent**: Cuando me confirme, nada, te aviso. Por ahí me pasas credenciales y entramos.

**Lucio Rojas**: Sí, disculpa, no había terminado de entender eso, pero ya me quedó. Me quedó claro. Bueno, estoy acá refrescando todo porque recién salgo de una demo. Quiero ponerlo en cero para poder mostrarles. Bien. Y arrancamos ya. Dana, ¿Te pudieron contar algo de casetéramos? Perfecto. Mejor.

**Dana Perelmuter**: Estoy acá medio perdida, pero bueno, mejor,

**Lucio Rojas**: así puedo explicar de cero todo. Bueno, vamos a hacer. Aparte tenemos un punto de vista nuevo, no está sesgada por la última reunión. Bueno, arranco. Explicar un poco la herramienta. Ante todo, bienvenida a las preguntas. Si quieren frenarme si no se entendió algo. ¿Quieren que pensemos cómo aplicarlo en un caso de uso más de ustedes también? Arrancando. Nosotros como theramo, somos una startup de Rosario. Y lo que hicimos es desarrollar una herramienta que se encarga de automatizar el proceso de ingeniería de datos. Lo que hace, en una oración simple, es hacer el ETL de punta a punta. Se conecta una fuente de datos, hace el proceso de limpieza estandarización, normalización y modelado de la data a partir de interactuar con una inteligencia artificial en particular, que ES Cloud, o ChatGPT también si se quiere. Y esa tabla que se genera para el análisis de datos se deploya en un servicio Cloud que es AWS, se alojan los datos en atina de AWS y se deja la infraestructura en producción de las tablas para hacer el análisis. Lo que nosotros desarrollamos es un ecosistema de agentes que tiene más de 50 agentes de inteligencia artificial que se encargan de resolver partes distintas del problema. Como por ejemplo, hay una gente que entiende las bases de datos, las tablas, las relaciones, otro agente que hace limpieza de datos, otro que hace detección de outliers, otro que interactúa con CLOT para poder entender qué es lo que está pidiendo el cliente, otro que modela las nuevas tablas, otros que se encargan de la parte de infraestructura y entre otros que orquestan la solución. Y entre todos esos agentes funciona Teleamot. Así que vamos a recorrer un poco el camino de lo que es un caso de uso en Teleamot, cómo sirve para hacer análisis de datos y bueno, los invito a que también sugieran cómo esto puede llegar a acelerar un proceso, un proyecto de desarrollo. Lo primero que se hace es conectar una base de datos, una fuente de datos. Nos conectamos al 80% de las bases de datos más conocidas, eso incluye BigQuery, SQL Server, MySQL, también nos conectamos a algunos sistemas como Salesforce y SAP. Si hay un conector que no está incluido dentro de estos, se puede evaluar el desarrollarlo. Si no, se pueden cargar los datos como archivos CSV o parquets. Para conectarse una base de datos se piden algunos campos que son el host, el esquema, el usuario, la contraseña, el nombre de la base de datos y así uno empieza a conectar a t múltiples fuentes de datos, generando lo que es una suerte de data lake. Podemos usar una base de datos de un sistema, enriquecerlo con los Excel y a partir de ahí empezar a trabajar con todas esas tablas.

**Estanislao Sallent**: Tengo dos dudas yo. La primera, si yo subo archivos,

**Lucio Rojas**: suponete

**Estanislao Sallent**: archivos de un sistema de gestión, en vez de conectarme a la base de datos, hago una bajada y la subo el mes pasado, cerrado, termino el mes, vuelvo a subir, ya reconoce y actualiza y lo incorpora al Data Warehouse virtual o hay que hacer de vuelta un procesamiento.

**Lucio Rojas**: Bien, ahí primero depende de tu intención. Siempre y cuando tu intención sea actualizarlo, se pisan esos archivos. Si mantiene el mismo formato, la fuente de tablas y de columnas, se hace una actualización directa y se pisa el archivo. Si vos querés mantener el histórico de meses, se va cargando como una nueva fuente. Es una nueva fuente, depende. Si vos querés actualizarlo, no se actualiza.

**Estanislao Sallent**: Lo que quiero es ir acumulando y teniendo todos los meses. Cuando termina febrero, quiero subirlo y que se acomode abajo y seguir consultando la información consolidada de todo ese periodo.

**Lucio Rojas**: Claro, ahí sí generas una fuente compuesta con varios apps.

**Estanislao Sallent**: Y tengo que ir después a Claudia y decirle, acabo de subir este archivo, por favor incorporalo abajo. Agregalo.

**Lucio Rojas**: Sí, si vas. Ah, si no lo puedes concatenar. Si querés hacer un consolidado, entiendo que también se puede concatenar la información y ya se suma directamente dentro del ETL al mes anterior. Entiende.

**Dana Perelmuter**: ¿Esto se consume directamente desde Cloud?

**Lucio Rojas**: Sí, es la opción principal.

**Estanislao Sallent**: Tengo otra consulta. Yo tengo un esquema de salida, yo tengo una aplicación y yo tengo un esquema de tablas, digamos, de valores que tengo que respetar para poder alimentar esa aplicación. Se lo puedo dar y transformarme en esto en particular y le voy sumando cosas y siempre va transformando en eso.

**Lucio Rojas**: ¿El esquema cómo sería? Sería una tabla con determinados campos, varias tablas. Varias tablas con determinados campos. Y acá lo que funciona es el ETL. Vos una fuente o varias fuentes de input, generas transformaciones para un output. Ese output se puede generar el que vos querés, que si es el que me entiende mi sistema, que después lo tiene que recibir. Si vos después agregas más información, las fuentes que ya definiste, te lo va a tomar como dentro de ese mismo ETL y seguir el camino. Si agregas una fuente nueva, no tenés que empezar el proceso de vuelta.

**Estanislao Sallent**: La pregunta de fondo es si se puede generar funciones, ¿Entendés? Donde yo le doy indicaciones, pero que sea siempre igual. Yo voy a subir todos los meses la actualización del archivo, agárralo, procesalo y pégalo abajo de la tabla que ya veniste haciendo, o todas las actualizaciones siempre las tenés que transformar en esta salida, hacer un pipeline, no sé cómo decirlo. ¿Cuál sería el equivalente?

**Lucio Rojas**: Es que un poco lo que hacemos, el pipeline de datos ese, a medida que se va haciendo el upload de datos o la actualización de la información. Te devuelve el.

**Estanislao Sallent**: Claro, pero cada vez que yo suba un archivo, ¿Tengo que darle indicaciones o subo?

**Lucio Rojas**: No, no, se mantiene. Ya se mantiene.

**Estanislao Sallent**: El túnel ya está hecho y siempre sale, ¿Entendés? Siempre sale por el mismo lugar. Y si yo tomo esto en un servicio, siempre me va a actualizar, no sé, el Data Studio de donde lo estoy tomando para verlo. Siempre se me va a actualizar a la última información subida.

**Lucio Rojas**: Exacto. Sí, funciona así. Funciona estilo pipeline. Cuando vos actualizas la fuente, se actualiza el output y actualiza también el Data Studio. Lo que sí, no tenemos versionados. Eso para aclarar. Por ejemplo, si vos actualizaste un mes y querés hacer un versionado del mes anterior, eso ya está, se convierte al mes nuevo. Bien, Dana, te veo tomando nota. Me gusta. Espera que voy a hacer un cambio de pantalla si quiero ver distinto dentro de mi computadora. Un segundo. Si no los veo así en loop, No me gusta. ¿Hasta acá ¿Te surgió alguna duda? Vos anda. ¿Alguna pregunta que quieras hacer?

**Estanislao Sallent**: ¿No?

**Lucio Rojas**: No. Bueno, entonces si querés vemos un poco lo que es la integración con Cloud. ¿Has trabajado con Cloud? ¿Has conectado?

**Dana Perelmuter**: Ya había hecho un MCP de datos para Cloud.

**Lucio Rojas**: Buenísimo, entonces vamos mucho más rápido. Lo que nosotros hacemos acá es conectarnos a Cloud por MCP. Para conectarnos hacemos un, valga la redundancia, un conector personalizado donde le damos la URL y el token que genera ya la misma web. Se usa esta URL y como token se genera uno nuevo cada vez que querés actualizar la conexión. Este tiene muchísimo porque es justo el caso de uso de demo. Generamos el nuevo token, Tiene hasta 10 token activos en paralelo, así que si cumpliste los días, hay que borrar alguno para actualizarlo. Se copia la URL, el token que genera lazo de uso y se conecta Teramot a Cloud. Una vez conectado, lo que hacemos es gestionar estas tablas, explorar las que ya tenemos y crear nuevas. Además puedes crear dashboards o interacciones desde Cloud con tus datos. Una de las primeras preguntas que solemos hacer es, Y para saber qué tablas tiene, digo. Así que vamos a pedir un diagrama anti relación para que nos muestre que ya entendió toda la metadata de las tablas, que hizo toda la limpieza, estandarización y sanitización y las tiene disponible como para que nosotros la podamos trabajar y empezar hacer casos de uso. Una vez nos responda con las tablas que ya tiene, si se quiere su conocimiento, se puede empezar a hacer dos tipos de preguntas, depende mucho para lo que ustedes quieran usar. ¿Téramot se puede ir por un camino que es más explorativo, con preguntas como bueno, qué patrones puedo identificar en mis datos? ¿Cómo puedo mejorar cientos insights de negocio? ¿Cómo puedo generar más ventas? ¿Cómo puedo reducir costos? Eso más explorativo y si se quiere más cuando uno sabe muy bien el rumbo que quiere seguir con los datos. Y si no, se puede hacer algo mucho más puntual, como por ejemplo me quiero generar una tabla que haga conciliaciones de ventas con productos, o sea con el stock en tal punto de venta. Entonces va a empezar a tomar las tablas de ventas, la tabla de stock, la tabla de producto, va a hacer las transformaciones necesarias y uno puede hacer la conciliación. Entonces se puede ir algo más general o algo más puntual, depende lo que necesitemos. ¿Yo ahora voy por algo más general, porque me parece un poco más divertido hacer la exploración de los datos en la demo voy a decir en base a los datos que tenés, cómo puedo mejorar métricas de procesos? Vamos a ver qué distintos tipos de análisis nos sugiere en base a los datos nuestros que ya tiene. Ahora está generando una query sobre la data, para investigar un poco más sobre la pregunta que yo le hago conectándose BMCP y vamos a esperar a ver qué nos responde. ¿Quien usa el espacio publicitario puede hacer alguna pregunta, alguna acotación? Podemos ir respondiendo.

**Dana Perelmuter**: Podés. ¿Te muestra cuando expandís las consultas? ¿Te puedes expandir para las consultas? No, no. Ah sí,

**Lucio Rojas**: Haciendo como una exploración de toda la base de datos para entender qué responderme, porque fui con una pregunta súper amplia y tiene que hacerse un paneo general de la base de datos. La próxima vez le pregunta algo más, no tan genérico.

**Estanislao Sallent**: Volví, perdón.

**Lucio Rojas**: Perfecto, estamos haciendo el recorrido, Estamos esperando que nos devuelva. ¿Qué tipo de análisis podemos hacer para mejorar métricas de procesos en el negocio? Creo que fuimos algo más explorativo. También podemos ser más puntual en base a las tablas que tenemos, decir bueno, quiero generar una tabla que me sirva para analizar X situación o quiero llegar a tal tabla. En puntual, como lo harías

**Estanislao Sallent**: en el volumen de datos a procesar.

**Lucio Rojas**: No, hasta ahora no hemos encontrado un tope. Supongo que la escalabilidad del producto quizás funcione mejor con cantidades de datos controladas, pero un cliente nos cargó una base de datos de dos teras y anduvo.

**Estanislao Sallent**: Yo tengo un caso concreto que es un sistema que tiene sus tablas, que serían de dimensiones, digamos, con información estática, y los registros que se van generando son más o menos 450 mil por

**Lucio Rojas**: mes y se van acumulando de registros. No suele tener tanto problema con los registros porque toma mucho más trabajo para el sistema entender varias tablas o varias columnas. La cantidad de filas no es tanto.

**Dana Perelmuter**: Y te hago una consulta. En la página hablan de lo que sería Golden tables. Creo que sí. Gold tables. ¿Qué sería?

**Lucio Rojas**: Nosotros lo que hacemos es trabajar con las tablas bajo una arquitectura que se llama Medallion. Lo que hace la arquitectura Medallion es separar las tablas en tres instancias. La primera instancia es la bronce, como si fuesen medallas de una competición de carrera. La de bronce, la de plata y la de oro. La medalla de bronce lo que hace es copiar los datos tal cual te los da el cliente. Nosotros trabajamos siempre con copias que se almacenan en Latina, en AWS. La capa silver es los datos del cliente sanitizados y estandarizados, además de detección de outliers y eliminación de duplicados. Y las capas gold es lo que estamos llevando a hacer ahora a la gente, que es entender todo mi modelo de datos y generar tablas listas para el análisis. Cada una de las tablas gold serían los pipelines, que hoy estábamos hablando, por ejemplo con Stanislaw, que es un resultado puntual, que yo necesito generar una tabla con ciertas columnas, ciertos cálculos, ciertas combinaciones, que se actualice siempre con una fuente de datos que yo voy refrescando todos los meses. Eso sería una tabla gota, sería un ETL, un pack.

**Dana Perelmuter**: ¿Podría ser considerado una vista?

**Lucio Rojas**: Sí, puede ser considerado una vista. Es mucho más fácil si te hubiese respondido eso que toda. Acá nos sugirió Theramot distintas oportunidades de mejoras por área. Nos dice que lo más urgente es solucionar problemas de stock dentro de la empresa en base a los datos que investigó al activar el reabastecimiento automático de los sistemas de ellos. Otro es más relacionado con los canales de venta. Otro proceso que nos sugirió mejorar es todo lo que es el delivery, que tiene bajo uso, pero son las ventas de mayor ticket. Otro aspecto mejorar son los descuentos operadores. Vamos a ir sobre algo puntual que siempre está bueno trabajar que son las ventas y decir tomemos acá, vamos a decirle esto, que me sugiera una tabla gold así nos lleva una vista nueva que sirva para analista posibilidades, mejora las ventas. Esto lo que hace es no solamente entender lo que quiere el usuario y sistema, sino ya crear esta nueva vista, esta nueva tabla. En realidad el sistema se ven como tablas distintas, una vista, una tabla, Muchas tablas, esto me pasa, puede ser muchas veces la misma demo, Así que lo que va a hacer es entender un poco cuál es el request, crear la lista de requerimientos funcionales que necesita esa nueva tabla, volver a interpretar eso y generar toda la query SQL necesaria para llegar a esa tabla, correrla y desarrollarla como infraestructura en producción. Una vez que tenga esa esa call creada lo que se puede hacer es consumirla desde el mismo plot, pedirle que haga un dashboard, un sistema de alertas, algún HTML con datos o correr algún proceso de machine learning para hacer predicciones, eso lo hemos usado bastante. ¿Está bueno armar algún agente o se puede ir más a lo clásico y desconectarlo a una herramienta de visualización como tabló por Uy, un poco como hacen los canales de cocina para no esperar a que se genere la Gol? Te voy a mostrar una gol ya creada, como te dice cómo hacer la torta, sale con la torta de ella. Vamos a hacer algo de eso sí vamos más rápido. Por ejemplo esta gol que creo es una gold de ventas históricas por producto y por segmento de cliente, pequeña descripción, como es bastante descriptivo el título no da mucha información, pero hay veces que esto se vuelve más complejo, te da una idea de la tabla que te sirve para crear un nuevo use case, o sea de esta tabla gol. Después vos podés crear una fuente de datos para volver a someterlo a capas de análisis, se puede incluir esta tabla gold con otra fuente de datos que vos ya tengas del cliente. Se selecciona por default todas las fuentes de datos que son necesarias para crear esa tabla, se genera lo que decía la lista de requerimientos funcionales, como por ejemplo acá bien puntual, unir la tabla X con la otra tabla a partir del product ID, o sea arranca todo con un join y después lo va enriqueciendo. Después hace descripciones para hacer cálculos derivados de distintos campos, aplica filtros como filtros solo de ventas.

**Dana Perelmuter**: Un segundo, ya vengo.

**Lucio Rojas**: Es el famoso tocadón timbre,

**Estanislao Sallent**: llegó Mercado

**Lucio Rojas**: Libre, Llegó Mercado Libre o cuando tenés a tu hermana o que te están tocando la puerta. Nos pasa a todos. ¿No, no, pero nosotros estamos suponiendo cuáles eran los múltiples escenarios, no?

**Dana Perelmuter**: Yo y papá,

**Lucio Rojas**: algo se iba a hacer. Bien, terminando un poco con toda la demostración, después de hacer la descripción de todos los requerimientos funcionales, te crea la query SQL, La query donde contempla todas las necesidades que tiene que tener esta nueva tabla, nueva vista, y te da el preview que está un preview nada más para ver un poco cómo quedó la tabla y queda alojada en la tina, desde donde vos después te podés conectar, como te digo, con Cloud de vuelta o con cualquier otra herramienta de visualización. Después de Cloud podemos, podemos hacer algo que todos ya sabemos que puede hacer Cloud. No me voy a detener mucho porque entiendo que ya son usuarios, pero ponelo, Se puede pedir dashboards que los hace en cuestión de dos a cinco minutos. Nunca he querido poner tiempo porque siento me sorprende. Tarda dos minutos, tarda cinco, tarda dos,

**Estanislao Sallent**: pero depende la hora del día.

**Lucio Rojas**: Sí no me caso con Nike no le creo nada. Pero bueno, se puede habilitar toda la potencia que tiene Claude con las tablas que vos ya creaste. Así que bueno, este un poco el recorrido por la herramienta. Haciendo un poco de benchmark, dedujimos que llegara a ser un proceso de tele completo, como los que han hecho clientes. Esto parece simple porque estamos yendo sobre algo muy genérico, no es un dolor de nadie, no estamos resolviendo puntual, pero cuando realmente hay un dolor del otro lado y se quiere atacar una solución puntual, tuvimos resultados mucho más rápidos. Redujeron trabajos de dos o tres meses a dos o tres días, gracias a la automatización de todo este proceso de entender mucha fuente de datos, entender muchas tablas, entender cómo se relacionan, cómo son las keys, cómo se hace un join entre varias tablas, las transformaciones, automáticamente una conversación. Así que bueno, no sé si tienen alguna pregunta.

**Estanislao Sallent**: ¿Yo tengo una que es si en el armado del Data Warehouse toda la parte del ETL tiene algún tipo de alucinación, algún riesgo de que interprete mal algo si les pasa, cómo resuelven ese tema?

**Lucio Rojas**: Bien, en qué ¿Tenés alguna parte específica de todo el armado del tele que te preocupe más o una pregunta más general?

**Estanislao Sallent**: No, en la transformación, en los outliers, hay interpretación de negocio ahí adentro y puede generar una interpretación no correcta, no porque se equivoque demasiado, sino porque no interpreta. ¿Como con el criterio que tiene el negocio, puede modificar algo? ¿Se puede reemplazar, se puede editar?

**Lucio Rojas**: Eso es una pregunta que obviamente la primera vez que surgió fue internamente, hace varios meses. Tiene todo el sentido del mundo. Capaz que yo en mi base de datos tengo cargado cierto producto, que es muy parecido en SKU al resto de los productos, pero este tiene sentido que valga 30 en vez de valer 3. Elimina el sistema y me está armando un bárbaro poder eliminarmelo. Y antes no te preguntaba. Nosotros ya teníamos una versión paralela a esta web. Esta web que ven ahora, no le queda mucho más tiempo, en una cuestión de un mes ya vamos a estar migrados a una nueva UI, donde esto se controla con un agente que te pregunta a vos por las modificaciones que hace. Entonces te dice, yo estoy viendo esta transformación de este producto, ¿Hace sentido hacerlo o no? Y la mayoría de las respuestas son automáticas. Y si no, uno puede modificar. Si algo en esa parte de la creación de Bronce, Silver, que entiendo vos donde me preguntas, eso va a estar disponible para ustedes. Ya está la versión en productivo, nada más. Hay que probarlo un poco antes de llevarse a los posibles clientes.

**Estanislao Sallent**: La otra es. Un plan. Debo tener una API, Cada cliente tiene que tener Cloud para poder conectarse. Yo puedo hacer, puedo hacer, uso un front que le doy a mi cliente, y atrás uso la API de Cloud.

**Lucio Rojas**: ¿Cómo pensás vos el uso de tu cliente, de Theramot?

**Estanislao Sallent**: Mi cliente no ve Theramot.

**Lucio Rojas**: Bien, vos querés, si querés pensarlo así, sumarle, o sea, te gustaría sumarle una capa de más de. De interacción, un front con una API de Antropic y que esa API sea la que ejecute sobre Teyamot y responda.

**Estanislao Sallent**: Claro, yo lo que quiero por un

**Lucio Rojas**: lado es

**Estanislao Sallent**: generar dashboards en una aplicación que tomen información, conectados a las tablas Gold sería, y muestre un dashboard. Eso por un lado. Sobre ese dashboard yo le pongo un cuadrito de texto, y pueden hacer preguntas, y hace consultas a la base de datos, tanto la Gold como la Silver, y responde sobre esa información. Y atrás eso me da una réplica, yo la cargo en mi servidor, lo conecto a Theramo, estas son las tablas, genera la Silver y genera las Go y disponibilizame toda la. Una API, no sé que trabaja con Cloud, pero no tengan que entrar a Cloud Com, sino que entren a mi aplicación y mi aplicación consume Cloud para consultar la téramo.

**Lucio Rojas**: ¿Esto funcionaría así? Entiendo tu pregunta. Primero despejemos unas dudas. Las tablas God las creas vos, no las creas el cliente. Después tu aplicación, entiendo que lo que va a tener que llevar adentro es un modelo propio de inteligencia artificial, que lo compras vos, lo pones dentro de tu UI.

**Estanislao Sallent**: Si uso la API de Cloud,

**Lucio Rojas**: a esa API de Cloud le poderoso, le puedes generar el conector Atina directamente. Entonces va a poder ver las tablas Gold y va a poder generar los dashboards y las preguntas a las tablas Gold de Telamo. Siendo un modelo de Cloud. Está buena esa idea. Entiendo, entiendo. Directamente con nosotros lo que hacemos ahora es, tenemos dos tipos de conexiones. Tenemos el conector de Cloud a theramo y los agentes que generan la Go, que se llama autotl para nosotros. Tenemos el conector Atina, que es lo que después vos ves que genera todas las respuestas, los dashboards y eso. Vos con ese conector Atina, que nosotros supongo que te pasaremos las direcciones de la tabla para que le pegues por MCP con tu modelo de la consola Tropic, tendrías que andar.

**Estanislao Sallent**: Yo con eso no necesito que cada cliente saque una cuenta de Cloud ya solo con la mía.

**Lucio Rojas**: Si vos nada más te pagas tus token y supongo que después trasladarás el costo del cliente. Pero sí se puede. Está muy.

**Estanislao Sallent**: ¿Cómo escuchaste todo eso que acabo de decir?

**Dana Perelmuter**: Que vos pagues la cuenta de todos y que después les mandes un invoice. No,

**Estanislao Sallent**: no, no. Yo cobro, yo pago mi cuenta y después a ellos les cobro un servicio por el. Por precio, por el servicio que le doy.

**Dana Perelmuter**: El tema es que a menos que vos armes una estructura de pago por mes, como en este caso tiene Teramont, vos no podés mandarles un invoice sin mucha especificación, porque puede generar problemas a futuro.

**Estanislao Sallent**: No importa la parte comercial, eso. Yo le voy a poner un fee.

**Lucio Rojas**: Importa eso.

**Estanislao Sallent**: No importa esa parte de negociación. Yo lo que estoy diciendo es, si técnicamente está bien lo que acabamos de plantear entre Lucio y yo, digamos, pego, consumo, tengo una API.

**Dana Perelmuter**: Si tienen una API que se puede acceder, no debería haber problema.

**Estanislao Sallent**: Que no tienen una API ellos. La conexión de Atina a la que vos le podés pegar a las tablas para consumir los datos. Y habría que tener un cloud conectado a Theramo que haga de nexo entre la consulta del usuario. En el front cloud consulta Teramot y Teramot devuelve

**Lucio Rojas**: ahí en la última aplicación que decís vos no tenés que meterte a Teramot, van a quedar las tablas Gol, ya van a quedar en Latina. Vos lo que tenés que conectar es tu cuenta de cloud Atina, o sea, mi botina. No importa mi bot, vos sos un botina. Es más, hasta incluso lo que podemos ofrecerte nosotros es un esquema de multitenancy donde toda la orquestación de la infraestructura en AWS no se hace en nuestra cuenta, sino que se hacen para ustedes. Entonces ahí tenés mucha más flexibilidad para manejar el conector Atina sin tener que hablar con nosotros.

**Estanislao Sallent**: Pero sí o sí en Atina no puedo hacerlo de GCP.

**Lucio Rojas**: No, en Atina nuestra infraestructura se levanta en AWS. Pero bueno, eso tiene beneficios y costos. Tu beneficio si usas tu tenant en AWS para deployar las tablas de Tenamotex, es tu Tena, tiene más privacidad, ya sabemos de tener tus propios datos del host propiamente. Lo malo es que tenés que pagar vos todo el invoice de AWS. En este caso nosotros somos los que absorbemos y damos una. Se volvería al revés el ejemplo que vos diste con tus clientes. Pero yo lo veo bien lo que vos decís me parece interesante. Agarras Téramo, te resolvés el problema de las tablas, generas una UI, le pones unos. Unos tokens, unos créditos de Antropic, y le das al cliente un sistema de dashboards a demanda y consultas. Y después le cobra un fee por eso. Te fijas que la diferencia te queda a favor. Está bueno, me gusta. Bueno, ¿Querés que repasemos los costos de Telamota?

**Estanislao Sallent**: Sí, vamos. Una consulta mientras va buscando eso. La diferencia entre la prueba esta de dos meses y el plan free, ¿Cuál es? Tengo más tablas, pero si quiero hacer una prueba con un cliente para. ¿Solamente para probar, puedo agarrar esa de la capa gratis? Lo pruebo, lo muestro. Si le gusta

**Lucio Rojas**: esto así. En Dream tiene cuatro tier. El primer tier es el modelo freemium, como siempre el free tier, pero te deja a vos hacer hasta dos. Hasta dos gold o dos ETLs. 15 GB storage, 150 GB de procesamiento mensual, y después a medida que va subiendo de Tigger, van subiendo los mismos parámetros. Siempre que más miramos son las tablas Gold, que es el cuello de botella. En el pack starter sale 50 dólares por mes y puede generar hasta 5 tablas go professional, hasta 20 y así va escalando por proyecto. Siempre esto es por proyecto dentro de Teleamot. Cada proyecto dentro de Teleamot tiene su checkout. Si vos tenés dos clientes esto se duplicaría. Y acá la diferencia que vos me decís de la prueba de dos meses, es que la prueba de dos meses es con un checkout donde vos podés pasarte de los planes, pasarte las tabletar

**Estanislao Sallent**: el plan profesional con dos meses gratis, el mes 3 me empieza a ganar 200 dólares, pero desde el mes 1 tengo 20 tablas gold.

**Lucio Rojas**: Exacto. Estamos en realidad una ventaja de dos meses para usarlo. Y bueno, después pasa a la parte pago.

**Estanislao Sallent**: OK. Y la parte de precio mayorista, el custom pricing, revendedor, etcétera, que habíamos hablado última vez.

**Lucio Rojas**: Eso es en caso de que el volumen de goals, de storage, de procesamiento que vos estés trabajando exceda el plan professional. Nosotros revisamos un poco el consumo del cliente y tenemos un cálculo en base a cada una de las variables, cuánto cuesta y se genera un ticket final mensual. Después se va actualizando a medida que crece el volumen mensualmente. Sobre ese ticket mensual, en caso de ser un cliente con volumen que es alto, que nosotros entendemos que nos está llevando a nuevos clientes, que además una buena relación de reuniones de soporte, también podemos ofrecer un descuento, por ejemplo 15% de descuento sobre el plan. Eso es ya una vez excedido los límites del plan profesional, o si vos me decís, yo estoy sumando clientes, cada vez que sumo cliente tengo que sumar un ticket profesional de 200, me está escalando linealmente, al quinto cliente tengo que pagar mil dólares, al décimo cliente tengo que paga dos mil dólares. Me gustaría poder absorberlo distinto. Y bueno, ahí podemos pensar un checkout por cuenta y que también sentido, pero yo creo que son conversiones. Una vez que se genera más volumen de usuario y podamos ver el caso en particular. OK,

**Estanislao Sallent**: Tengo tres clientes que podría, que podría ya meter acá, más una aplicación propia, Me gustaría entender cómo encararlos y lo encaro, como los hago entrar y poner su tarjeta de crédito y qué sé yo, y desarrollan su propia infraestructura, si hago esto, descentralizarlo en la mía, yo les doy el servicio, Tengo que ir ya, tengo que hablar comercialmente con ellos para.

**Lucio Rojas**: ¿Y ahí creo que es definir un poco tu modelo de negocio, si lo haces más como consultor de implementación, como por ejemplo a mí alguien me dice, bueno vos tenés, sos paladín, yo te voy a implementar SAP y yo soy X consultora, te voy a cobrar un millón de dólares por hacer toda la implementación, parametrización y todo es, pero después la cuenta de SAP la pagas vos modelo y la otra es vos ofrecerte como quien está proveyendo el sistema y usar como marca blanca Theramo,

**Estanislao Sallent**: ustedes no tienen un programa de revendedores, por ejemplo, de partners?

**Lucio Rojas**: Creo que activamente no dejamos más que se lleve la negocio y lo que sí hemos visto es algunos esquemas de eso, déjame consultarlo bien con quién, con mi superior que me dice si, sí, activo, lo hemos hecho pero no sé Si se activó. ¿Cómo lo preferirías hacer? ¿Preferís hacerlo más marcado y ango o hacer lo de partners?

**Estanislao Sallent**: A ver, por simplicidad a mí me conviene tener un mismo contrato y formato, donde yo ya, nada, yo ya sé que entra por ahí, yo me manejo de esa manera y qué sé yo, nada, entiendo que ustedes tienen que también nosotros tenemos estos esquemas, adaptate, y yo si tengo un cliente que no entra por esta forma, nada, lo meto por otra, ahí yo me arreglo con cada uno, pero quiero entender si está este modelo donde yo pongo mi infra para las tablas de cliente, Entrego el front, digamos, ya directamente hecho, Bueno nada, si querés averiguame nada más esa parte de partner, digamos y de cómo sería de última tener un mismo, o sea, porque yo también tendría que tener como multitenant, digamos interno, porque tengo que separar también las tablas de los clientes, etcétera, entonces nada, tengo que entender cómo hacer eso.

**Lucio Rojas**: Perfecto. ¿Para dejarlo bien claro, yo después te averiguo, podemos ver dos esquemas donde yo los veo a ustedes como clientes y ustedes tienen su multitena y me pagan a mí un invoice, o podemos ir sobre un esquema de partners donde cada uno de sus clientes se hace una cuenta multitenant adentro de Telamot y ustedes ahí que quisieran a cambio? Solamente llevar la implementación adelante, comisión sobre la suscripción del cliente, me imagino un

**Estanislao Sallent**: típico esquema de department no sé, 15% del primer año del cliente, el estándar, digamos, en SaaS.

**Lucio Rojas**: Bueno, averiguo eso, estaba, tengo que saber si sigue estando y te lo mando por mail.

**Estanislao Sallent**: Dale, si vos me confirmás eso, yo ya activo con estos dos clientes para los dos primeros. Después el otro es un poquito más largo porque es una empresa que se toma sus tiempos. Y después tengo una aplicación propia que también me gustaría implementarlo para sumarlo esto, el chat dentro de la aplicación para contestar sobre.

**Lucio Rojas**: Perfecto, buenísimo. ¿Ustedes dónde están? Acá en Rosario me dijiste.

**Estanislao Sallent**: No, no, en Buenos Aires.

**Lucio Rojas**: Buenos Aires. Dana, ¿Vos que estudiaste?

**Dana Perelmuter**: Estoy estudiando ingeniería en sistemas

**Lucio Rojas**: en el palo técnico. Yo soy más del lado de negocios, negocios digitales. Bueno, creo que súper clara la reunión de mi lado. Trato de responderlo rápido, hablo con Bruno y vuelvo. Seguimos hablando. Buenísimo, muchísimas gracias, Lucio. A ustedes.
