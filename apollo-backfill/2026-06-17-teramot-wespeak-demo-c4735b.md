# Teramot- Wespeak. Demo

**Fecha:** 2026-06-17T13:12:14.085+00:00  
**Duración:** ~37 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Agustin Albiero <agustin@wespeak.pro>, Rafael Villalba <rvillalba@tecnom.com.ar>  
**Externos:** agustin@wespeak.pro, rvillalba@tecnom.com.ar  
**Apollo ID:** 6a32a5eedf10210010c4735b

---

**Lucio Rojas**: Acaba de llegar, ¿Viste? Lo llamé. Sí. Creo que es porque creé la videollamada justo sobre el momento y tardó un rato en llegar. Bueno, voy a proyectar la pantalla y me interesa ir haciendo algunas preguntas también para guiar cómo podríamos ver esto materializado en alguna, ya sea la empresa de cualquiera de los dos, o en algún caso de uso. Voy a compartir esta ventana y voy a sacar de acá. Ahí se ve bien. Bueno, esto es la interfaz de Theramot, es nuestra una web app si se quiere. Tenemos desde un SaaS, uno paga una licencia y lo usa. No tiene una lógica de servicios, no tiene consultoría, es directamente un tire y nosotros disponibilizamos una herramienta y damos soporte. Lo que hay dentro de Time son distintos Workspaces. Cada Workspace yo entiendo que representa una organización. Uno puede tener Workspace para consumo privado, para consumo de una de las empresas a la que le presta servicios, si fuese en caso de servicios de consultoría, varias empresas. Puedes tener distintos Workspace dentro de tu organización, si querés, para separar los casos de uso. Y dentro de cada uno de los Workspace hay distintos proyectos. Los proyectos también sirven para subdividir un poco los casos de uso. Se puede compartir información y tablas entre los proyectos. Por ejemplo, podemos hacer un proyecto madre donde centralizamos todas las fuentes de datos que queremos conectar de alguna de las empresas. Y después esas fuentes de datos disponibilizarselas a distintos proyectos con accesos de distintos usuarios que requieren una segmentación. Yo acá usted había pedido algún dataset o alguna fuente de datos para probar en vivo con algunos algo que les interesa analizar. Entiendo que por ahí no lo podemos hacer para esta oportunidad, pero si querés después conectar alguna fuente de datos y hacer alguna prueba gratuita, la herramienta en el taller gratuito ofrece bastante flexibilidad, no hay problema. Y ahora lo que yo tengo cargado son distintos casos de uso con datos. Depende de la industria, es lo que un poco lo que vamos a ir viendo. Yo lo que voy a hacer es usar el SAP, porque es por un poco el más representativo de conectarse a un sistema de gestión de la empresa para poder analizar qué es lo que hay dentro de las tablas y tomar métricas. Lo primero que hacemos cuando nos conectamos a la herramienta es ingestar una fuente de datos. Acá tenemos varios conectores. Esto es importante. Nosotros tenemos un poco lo que nos fueron pidiendo. Hoy en día generar un nuevo conector no es un problema para nosotros, así que en caso de requerir alguien algún conector nuevo se evalúa y generalmente se hace. Pero para empezar tenemos los que son los más comunes, Postgres, MySQL, SQL Server, algún archivo Dc en Amazon que está almacenado, Google, BigQuery, algunos sistemas, podemos ver a Salesforce, HANA, Snowflake que ya está por salir en el próximo sprint te puedes conectar a una Google Sheets, una carpeta de Google y más. Cualquier fuente de base de datos con estructura tabular o archivos con estructura tabular. ¿No sé Agus, por Rafa, qué base de datos ustedes manejan? ¿En qué motores están? Para entender un poco eso también.

**Agustin Albiero**: En mi caso estamos generalmente MySQL, igual tenemos un click house también que le comentaba a los chicos que podría estar bueno conectar y otra fuente de datos como lo que habíamos hablado Post Hog, que no lo vi por ahí, pero

**Lucio Rojas**: nosotros creo que el post hoc nuestro lo llevamos hasta una bigquery y después los conectamos. Pudimos conectar directamente. Sí, pero quizás estaría interesante el conector. Bueno, voy a ir sobre el ejemplo de una myiswell me dijiste.

**Agustin Albiero**: Sí,

**Lucio Rojas**: acá básicamente lo que pide son las credenciales, el servidor, el puerto, el nombre de la base de datos, el esquema, usuario y contraseña. Y una vez que probamos esa conexión lo que hace es listarte las distintas tablas que vos tenés en la fuente con un descubrimiento del esquema y vos seleccionas cuáles querés conectar.

**Rafael Villalba**: ¿Perdón, consulta, a veces las bases las tenés abajo, un VPN, esto corre en la nube, o sea la VPN si tuvieras que hacer una conexión es configurable acá mismo? ¿Alguna cuestión de VPN o tenés que hacer alguna cosa más?

**Lucio Rojas**: Buenísimo Rafa. La mayoría en realidad de las empresas con las que nos terminamos conectando tiene algo bajo un IP o hay que hacer un túnel. Lo que hacemos es un túnel ipsec side to side y generalmente ahí ponemos en contacto nuestro equipo de infraestructura con algún equipo de tecnología de la empresa y cuando hacen la conexión VPN ya sí te conectas a este formulario.

**Rafael Villalba**: OK,

**Lucio Rojas**: Bueno, una vez que te conectas a la fuente de datos puedes configurar un cómo hacer el refresh de esos datos. Generalmente los estándares todos los días a las 7 de la mañana tengo una actualización lo voy a prender, no sé qué pasó ahí que no me mostró el historial, pero todos los días de las 7 de la mañana a las 8, lo que sea que seteamos, va a volver a levantar todas las novedades de la fuente de datos. Y ahí un poco lo que ocurre es que los agentes nuestros internos van a hacer un descubrimiento de lo que tienen todas estas tablas. Por ejemplo, en un caso de uso de SAP, uno ve las tablas de SAP y no infiere muy rápidamente qué es lo que tienen cada una de

**Rafael Villalba**: las tablas, o sea, esto hace discovery un poco por el esquema y otro poco por el contenido.

**Lucio Rojas**: Claro, no, más que nada por el esquema, hace una descripción de cada una de las tablas, que es cada una de las columnas, qué tipo de datos tiene, y todo eso lo guardan archivos de mercada y a veces, en algunos casos, acá la mayoría de las tablas ya venían bastante curadas de la fuente, pero lo que puedo hacer es alguna conversión para normalizar alguna fecha, alguna columna, hacer algo que los agentes nuestros internos consideran necesario para mejorar lo que es la sanitización y curar un poco más esa data.

**Agustin Albiero**: Pregunta rápida, Lucio. ¿Si yo al nombre de la columna le pongo cualquier cosa, no sé, algo que no es representativo del contenido que tiene ahí qué pasa? Ya que dijiste que en general no es por el dato, el descubrimiento o el análisis que hace esta inteligencia, sino que es más que nada bueno por el esquema.

**Lucio Rojas**: Es una combinación entre la tabla, por ejemplo, vamos a ver cuando le preguntemos a Claude qué tablas tiene, Set hace una combinación de la tabla, de qué tipo de datos guarda esa tabla, por ejemplo, si una tabla de producto ya se da un poco de contexto con eso, después con cada una de las columnas empieza a inferir qué es esta columna, qué tipo de datos tiene, y la verdad que si hay una columna que tiene un nombre muy poco representativo y con el tipo de datos y el contexto no lo puede inferir, lo que estamos haciendo ahora para el próximo sprint, o está ahí charlando en el roadmap, es poder editar lo que es ese campo para modificar un poco el contexto de la herramienta y poder guiar en esos casos donde quizás medio medio corner. Igualmente no nos hemos encontrado mucho con ese ejemplo, no termina de entender bien que es lo que lo que tiene la tabla. Bueno, acá lo que hacemos, el próximo paso, una vez que levantó toda la metadata, entendió que tiene cada una de las columnas, hizo una sanitización, hace una conexión por MCP al LLM que prefiere el usuario. Nosotros alentamos un poco por Claude, así que voy a mostrar la conexión a Cloud. Acá supongo que han conectado un MCP a. Así que cualquier cosa me dicen, pero generar un conector personalizado nuevo. En este caso traemos el Telamo, nos va a pedir la URL y el cliente ID, y directamente ya podemos consumir, administrar todo lo que es telamod desde Cloud. ¿Qué tablas tengo en el workspace? Y acá tengo que putearlo bien porque estoy desde una cuenta de soporte y todos los workspace. Y acá genera la conexión y me va a listar y hacer un descubrimiento del esquema para decirme qué tablas tengo y demás. Está llamando la herramienta a la tool de. Tenemos de listar las tablas que tiene disponibles. Si vemos el conector tiene varias tools disponibilizadas, entre estas están crear una nueva tabla Go, que sería un nuevo tele. También puede hacer queries a las tablas fuente, que es un poco lo que comentaron ustedes, que nosotros le llamamos Silver. Puede hacer varias, la mayoría de las. Vamos galeando casi todos los días, la mayoría ya se me escapan, pero representan un poco entre todos los distintos usos que vemos que dan los clientes.

**Agustin Albiero**: Acá para entender Lucio, si yo tengo 10 tablas en MySQL, voy a tener el equivalente en Theramod o este agente intermedio que se encarga de sanitizar los datos y ponerlos lindos. ¿Me puede llegar a sacar alguna tabla de configuración de usuario, que es obvio que no tiene información histórica relevante?

**Lucio Rojas**: No, no puede. La gente no te modifica ninguna de las tablas que vos modifica. A veces sí, porque hace alguna transformación en los tipos de DAT en algunos casos, pero no va a eliminar ni crear una tabla nueva en lo que es la source. Va a tener la misma cantidad de tablas que vos cargaste en el caso nosotros cargamos 70, en Silver tenemos 70. Lo que sí después puede hacer es crearte nuevas tablas gold, que es un poco lo que quiero que terminemos de cerremos la demo.

**Agustin Albiero**: Con mi ansiedad no me adelanto.

**Lucio Rojas**: Ahí si quieren ir haciéndome más preguntas y demás, por favor, no hay ningún problema.

**Rafael Villalba**: ¿Yo tengo una duda, vos esta cuestión que estás haciendo es el caso uso más clásico? Es uno de los casos de uso, digo, porque lo que había visto yo de Teramot hace un año más o menos, era más una herramienta de integración que de query quizás es, o por lo menos lo que había entendido. Capaz que no, quizás fueron mutando, pivoteando, capaz que tienen esa cuestión de integración. Te explico lo que había entendido, capaz

**Lucio Rojas**: nunca fuimos esto, ¿Qué es eso de integración?

**Rafael Villalba**: Tengo dos sistemas y tengo que mandarla todo, y los conectores son un dolor de huevo hacerlos, digamos. Y lo que había entendido que hacía theramot era conectarse a estas fuentes, hacer introspección, ver del otro lado que tengo que enviar y hacer el conector, hacer de conector entre sistemas, como una especie de, llámale zapier inteligente, digamos, medio con ad hoc, con sistemas, pero era lo que yo había entendido, capaz que nada que ver, capaz que nunca hicieron eso.

**Lucio Rojas**: Sí lo que vos entendiste es así, o sea, Teamot puede funcionar como una suerte de warehouse. Vos conectas más de una fuente de datos que tenés dentro de la empresa, más de un sistema. Justo este caso de uso, lo que hace es relegar una fuente de SAP para mostrar más que nada cómo. Cómo es el descubrimiento de las tablas y cómo traducís fuentes que no entendés muy bien a lo que es una lógica más de negocio, pero como está conectada esta fuente. Vos podés conectar n cantidad de fuentes que vengan de distintos sistemas y unificarlas todas desde la herramienta, y después puedes vincularlas, puedes relacionarlas, puedes crear nuevas tablas o nuevos ETLs con tablas de distintas fuentes al mismo tiempo, y ahí puedes vincular las fuentes. Y no hay problema en que lo haga, porque ya bueno, lo llevó todo en la misma infraestructura, tiene la metadata, sabe cómo relacionarlas y demás. Eso era un poco lo que vos habías entendido como para responder Bien, había

**Rafael Villalba**: entendido más como una herramienta transaccional de llevado de datos de un sistema al otro y no sólo de llevarlos a un esquema y después poder consultarlo.

**Lucio Rojas**: OK. No, creo que esa parte no, Lo que está haciendo es generando un. Esto no sé si lo pedí, podría tardar un rato en generarlo, va a ser un Discovery Table, va a ser un diagrama de R. Y la idea acá es un poco empezar a preguntarle, bueno, qué análisis puedo hacer yo con las tablas que tengo a disposición acá, como es un dataset de SAP para probar, me va a recomendar algunos cobros con clientes para analizar un poco más la información operativa. Pero bueno, si uno conecta datos de cómo funciona, esto exige el post hoc, la herramienta en sí puede sacar más analítica de cómo funcionan los sistemas.

**Agustin Albiero**: Se puede sumar como

**Lucio Rojas**: su tiempo acá,

**Agustin Albiero**: si se suma, se suma, y si no se suma, no pasa nada.

**Lucio Rojas**: Ahí no sé Abu, si vos tenés.

**Agustin Albiero**: Quiero entender, después que vi ahí, los chicos también me habían comentado de las tablas bronce, silver, gold, pero sé que va como a ir en una parte más avanzada de esta Meet, ¿No?

**Lucio Rojas**: Bien, sí, generalmente ahora cuando pasemos a crear una tabla gold, si querés explicamos bien cuáles son las distintas estancias y como nosotros explicando ahora, mientras vamos viendo que acá un poco lo que hizo un poco acá es agrupar, nos hizo un discovery de todas estas tablas. Uno ya sabe que la herramienta ya entiende qué tipo de tablas y qué significan todo lo que es el conector que hicimos del SAP, que uno ve, no sé muy bien qué es lo que tienen, las agrupó por categoría. Es decir, acá dentro de ocho tablas, yo hiciera doble clic, después me diría las tablas que responden a clientes de socios y negocios son estas, y estas tienen estas columnas y demás. Y ahora lo que uno puede hacer es crearse nuevas tablas gold a partir de esta tabla fuente y análisis que te sugiere Plot, a partir de la información que le hace acá hizo ya un resumen, dice las tablas de cliente y de negocio son, no voy a pronunciar el nombre de este, que son bastante bien de SAP, que son resúmenes de abreviaciones en alemán, así que no voy a poner a pronunciarlos, pero uno no conoce qué es lo que tiene el dataset. Acá le puedo decir, bueno, análisis interesantes,

**Agustin Albiero**: Como que medio me.

**Lucio Rojas**: Para ir puntualmente a lo que me preguntaste Agus, nosotros lo que hacemos es dividir dentro de nuestra arquitectura las tablas en tres estadios, si quieres decirlo así. Las tablas bronce para nosotros son tu fuente de datos, tal y cual vos no la disponibilizaste. Bueno, fuente de datos tiene 70 tablas. 70 tablas nuestras tablas bronce. Después las tablas silver son esas mismas 70 tablas que vos seleccionaste, pero sujetas a las transformaciones que vimos, que puede llegar a ser el agente de algún campo o alguna fecha puntual, algún castigo, y con toda la metadata relacionada a esas tablas ya creada. Y las tablas gold son, por ejemplo, la que vamos a generar ahora, que son los nuevos ETL que responden a una lógica del negocio, también quedan deployados en nuestra infraestructura de AWS, y se mantiene actualizándose a medida que se actualizan las fuentes Bronce, que actualizan la Siller y alcoholizan las esas Gol. A su vez también después se pueden consumir desde Cloud para hacer analytics.

**Agustin Albiero**: Bien, una cosa que me habían comentado los chicos es la limitante de Cloud, lo que tiene obviamente una ventana de contexto limitada, cada vez es más grande, pero para hacer análisis duro de datos no es tampoco la herramienta ideal. Y me habían dicho que hay como uno, no sé si un módulo, una funcionalidad o qué, pero para allá mandarle algún algoritmo, no sé, Random Forest, algo más como de Machine learning propiamente dicho. ¿Eso cómo sería o me cagaron a bolas?

**Lucio Rojas**: Ahí nosotros lo que hacemos es disponibilizarte la tabla Gold que quedó ya se quiere viviendo en Atina, que es el servicio AWS, donde nosotros lo deployamos, y vos después esa tabla Gold le podés correr algún agente de Machine Learning o lo que sea que vos quieras hacer para sugerirlo. Alguna analítica de datos más profunda en alguna Virtual Gen o en otro servicio de AWS. Claramente, sí, eso lo tenés que hacer vosotros. Disponibilizamos la tabla, o sea, vos llevas

**Rafael Villalba**: la fuente de datos a Atina y de ahí de Atina Qrea, conectas el MCP. Ese es más o menos el mecanismo,

**Lucio Rojas**: ¿No? En Atina viven las tablas Gold, que son las que creaste, los nuevos ETL que vos creaste a partir de las fuentes que cargaste.

**Rafael Villalba**: OK, pero lo que hace Tenamot es agarra las fuentes y los lleva, o sea hace esas transformaciones y lo estorea. Esto era en s digamos. Y lo quereas a través de Atina.

**Lucio Rojas**: Claro, si, Tina lo que hace es tomar esas fuentes, las lleva s, mientras tanto genera los archivos de metadata, los disponibiliza a Cloud vía MCP, y uno cuando quiere generar Mata o la Go devuelve. Ahora vamos a ver bien cómo es la descripción que se le hace a Theramot para que lo genere. Y los agentes de modeling de Teramot crean esa nueva tabla latina a partir de.

**Rafael Villalba**: OK, ¿Y como lo cobran esto? Vos dijiste que lo cobran por licencia y por volumen de datos que mueve. ¿Como es ese tema?

**Lucio Rojas**: En realidad hemos un poco ya testeado todos los caminos. Lo que hacemos ahora es directamente por licencia, por tires los Tires tienen como limitante principal la cantidad de tablas Gold que uno crea. Y por ejemplo, hasta la quinta tabla que se crea está dentro de un tier gratuito. También el volumen y el procesamiento son parámetros. Por ejemplo, el primer taller tiene hasta 37 creo, GB de almacenamiento. Vamos a revisarlo bien por las dudas.

**Rafael Villalba**: No, pero tentativo digo por qué lo estoy pensando un poco para mis clientes, para qué hay algunos que a veces necesitan. Ahí lo tenés. Está bien, Después lo voy a revisar.

**Lucio Rojas**: El Tire Free te va dando distintos parámetros. Dos usuarios, cinco tablas, como te decía, 37 GB de almacenamiento, como decía.

**Rafael Villalba**: Y ahí tenés, ahí tenés transferencia, 370 GB de procesamiento.

**Lucio Rojas**: Está bien, está bien. Y una medida que va ya requiriendo más de cada uno de estos parámetros, va saltando de taller,

**Rafael Villalba**: qué sé yo. La cantidad de usuarios, la verdad para estas cosas a veces son. Me voy al máximo de todo. Capaz tener dos usuarios, la transferencia mensual puede ser, puede ser la tabla o los tamaños. Puede ser.

**Lucio Rojas**: Nosotros lo que vemos que es más limitante es la cantidad de ETL que vos te generas, que es lo que por el primero termina marcando la variable del pricing.

**Rafael Villalba**: Y los ETL los hosteas vos.

**Lucio Rojas**: Sí, también lo podés costear vos en tu tenant de AWS, que la herramienta permite esa flexibilidad. Sí, en realidad una máxima preocupación por seguridad.

**Rafael Villalba**: Pero para, para, yo estoy analizando, por ahí vienen clientes con demandas de este estilo. Para mí, yo no quiero comprar el quilombo. Digo, che, mira, hay que ponerte en amor.

**Lucio Rojas**: Sí, ahí para la licencia y está todo incluido.

**Rafael Villalba**: OK, bueno, podría ser un caso de uso. A mí me puede llegar a interesar desde ese lado, capaz que vos no tenés ese problema.

**Agustin Albiero**: Sí, yo estoy pensando, a ver, tengo ganas de probarlo, obviamente, pero estoy pensando bien cuál podría ser mi caso de uso. Cuando nos juntamos con los chicos en Endeavor, empezamos a indagar a ver para qué me podría servir a mí, o bueno, a mis clientes también. Y una de las cosas que me decían es, bueno, podés llegar a predecir el churn que vas a tener en base justamente a los datos, esto de tus clientes, a ver de cuántas conversaciones tiene cada uno por día y algunos parámetros más. Y ahí, bueno, puedes predecir el churn y así con un montón de otras cosas. Entonces eso me parece que ponerme a indagar, a ver bien, quizás más algo como una introspección mía, qué cosas puedo generar yo con los datos que tengo ahí.

**Lucio Rojas**: Por eso había hecho un poco de hincapié en probar directamente con los datos o con datos, no para ahora, sino que vos lo pruebes. Porque qué va a pasar cuando vos le hagas después de cada. Todo lo que ya explicamos, entiende las datas, cuando le hagas esta pregunta, qué análisis puedo hacer con la data que te cargue, o voy a hacer una pregunta más puntual, Si quieres un análisis de churn, ¿Cómo lo harías? Te va a recomendar cuál es la tabla que vos necesitas para generar ese análisis. Nosotros no hacemos el análisis por vos, el churn, no corremos el modelo de Machine Learning para hacer el chan. Pero yo lo que he hecho en algunos casos míos es generarme la tabla, armarme el ETL y después correrle el modelo en alguna futura machine. Y eso está allana muchísimo el camino. Nosotros decimos que un 80% del tiempo de construir el modelo es ver en qué tabla están los datos, hacer el discovery, generar LTL, hacer la tabla para correr el modelo y después entrenarlo. Y los modelos son estándar también, son de análisis de chan. Entonces por ahí es donde a vos se te allana el camino con esta herramienta. Y así tenés infinitos casos de uso en base a tus datos y al análisis que vos veas que puedes ir haciendo. No sé si infinitos, pero varios.

**Agustin Albiero**: Sí le conecto al MCP y eso, le puedo empezar a preguntar y hasta que me cree nuevas tablas gold a partir de mi silver y eso.

**Lucio Rojas**: Claro, sí el MCP es exactamente lo que hace. Bueno, acá es un análisis directamente de el riesgo de fraude que tiene este dataset a partir de. Ah, el tema que ya tiene la tabla gold. Lo que pasó es que ya estaba la tabla gold generada, porque se ve que alguien en la demo le pidió este mismo análisis. Lo que hizo sirve igual para explicarles cómo se consume. Lo que hizo Thermo, cuando uno le pide riesgo de fraude, es a partir de tres tablas de entrada, que en este caso serían SAP, SC, no sé cuáles tablas serán de esta fuente, ahora la vamos a ver en la query, una descripción de qué es lo que necesita el usuario para poder generar un análisis de riesgo Entonces Claude lo que hace es interpretar la intención, traducir esa intención en los requerimientos un poco funcionales que tiene que tener la nueva tabla, generar instrucciones bien puntuales para que los agentes de modelado de Theramot generen esa nueva tabla, darle las tablas de origen. Y acá por ejemplo dice, bueno, accounts payable for risk analysis detect duplicate payments, same vendor, same account, same amount, close dates, y así genera varios requerimientos de lo que tiene que tener la tabla. Te da las tablas de origen, te dan la descripción, y lo que hace Telamo con esta descripción que generó Cloud a partir de la intención del usuario que trajo de la conversación, es generar una nueva tabla y esto ya desplazarlo en nuestra infraestructura en la tina y que se actualice a medida que se actualizan todas las silver.

**Agustin Albiero**: Claro, automáticamente.

**Lucio Rojas**: ¿En este caso, este análisis surgió del mismo flujo que hicimos nosotros de preguntarle qué análisis puedo hacer? Podés hacer un análisis de riesgo de fraude, donde cada fila va a traer motivo explícito de alerta, si es un pago duplicado, un fraccionamiento de facturas, una concentración de pagos en un proveedor con el monto del proveedor y el nivel de riesgo. Esto lo hizo el propio Plot a partir de todo el contexto de las tablas que le dio Theramop. Uno se lo pidió, hizo la descripción en Theramot, hizo la query, la tabla ya quedó en nuestra infraestructura actualizándose y ahora lo que puede hacer desde Cloud es consultarlo. Entonces puede hacer dashboards, puedes hacer un servidor data, o puede hacer un data egres de esta tabla, donde te damos todos los endpoints para consumirla y correr un modelo de machine learning, por ejemplo.

**Agustin Albiero**: Claro. De mi lado

**Lucio Rojas**: también damos la posibilidad de conectarlo, algunas herramientas de visualización como Power BI, Tableau, pero nosotros entendemos también un poco la capacidad gráfica y generación de dashboards de Cloud, y más que ahora que se pueden actualizar los HTML con alguna función que llamar MCP de vuelta, ese tipo de soluciones quedan un poco menos ágiles a lo que ofrece Cloud.

**Agustin Albiero**: Si vos decís que Cloud genera un HTML y que el HTML vos lo abrís, consulte a estos datos de forma automática para tenerlos frescos.

**Lucio Rojas**: Claro, sí lo que hace es ponerle, si yo le diría Claude, Dashboard que represente las alertas de fraude, me va a generar un HTML y yo la estoy desde Cloud web. Si yo estuviese desde Desktop. Puntualmente lo que hace es este HTML lo va a generar, pero le va incluir una función que esto es un feature bastante nuevo, que es de llamar al MCP cada vez que vos entras y lo actualizas. Entonces te actualiza el Azure automáticamente con los datos de nuestra bol. No lo investigue mucho porque salió esta semana, yo me quedo un poco como uff, es lo que necesitaba. Los de Cloud son un poco así, te lanzan features y ni te avisan, te vas a enterar cuando la necesites.

**Agustin Albiero**: Está buenísimo.

**Rafael Villalba**: Che muchachos, yo me tengo que bajar, me tengo que ir a Tramit. Gracias Lucio por la presentación, me parece muy interesante y veo un montón de posibles casos de usos, así que no, en lo inmediato no hoy a la tarde voy a necesitar algo, pero probablemente

**Lucio Rojas**: en algún momento vuelva o o los referencie, los veo muy activos,

**Rafael Villalba**: sé que pasaron por Adventure y algunos otros lados, Endeavor y demás, me parece es una herramienta que cubre un dolor interesante, así que buenísimo, creo que hay una oportunidad de que puedan hacer una linda startup.

**Lucio Rojas**: Buenísimo, Gracias Rafa.

**Rafael Villalba**: Ya nos cruzaremos en algún otro evento tipo Endeavor también.

**Lucio Rojas**: Dale, gracias.

**Rafael Villalba**: Abrazo.

**Lucio Rojas**: Abrazo, Chau, chau. Bueno, bueno Agus, yo ahí para ir más a que lo operativo, podemos seguir viendo los datos de la demo, cómo genera el dashboard. A mí por ahí me interesa más que si vos estás con ganas de probarlo, lo pruebes, me digas por ahí un poco eso, que yo no tenía bien tu background cuando estamos hablando por por mail, pero si quieres conectar directamente el post hoc o si querés algún MySQL o levantar alguna base de datos para esta prueba en particular, lo hacemos sin problema. Nosotros hacemos todo el soporte que haga falta para conectarlo, aunque no necesitarías mucho porque están los conectores a la web, nos conectamos de vuelta, vemos funciones, te guiamos ya más con tus datos.

**Agustin Albiero**: A mí me gusta mucho ponerme a usar las herramientas y probarlas como en modo auto discovery, me encanta. Entonces lo que podemos hacer si querés y como mencionaste que tienen un flip, me creo una cuenta, me pongo a probar, conecto mysql, algo básico como para empezar a preguntarle bueno a Cloud a ver qué datos puedo llegar a sacar, seguro me va a dar buenas ideas y a partir de eso voy viendo y si tengo alguna pregunta, obvio que te mando un mensajito y no hay ningún problema.

**Lucio Rojas**: Luci Dale. Bueno, perfecto. Entonces hacemos así. Si llegan a necesitar algo referido al soporte y demás, mandame. Ningún problema.

**Agustin Albiero**: ¿Estás más en el área de soporte, operaciones o ahora te veo comercial?

**Lucio Rojas**: No, yo estoy más en Customer Success y Acompañamiento Soport, ver cuál es el uso que dan los clientes y también llevar los productos. Pero pasé muchísimo por comercial, así que me quedo, me quedo ahí. Todavía estoy saliendo el cambio de chat.

**Agustin Albiero**: ¿Cuántos son en la empresa ahora?

**Lucio Rojas**: Y ahora estamos alrededor de veintilargos creo. No tengo el número exacto. 30. Equipo comercial tiene tres personas. En plataforma también somos tres o cuatro más. Pero con todo esto MCP y usar la herramienta más a partir de cloud, ¿No necesitas por ahí mucho de soporte o ayudarte un poco de trabajo más pensado para la escalabilidad?

**Agustin Albiero**: Cien por ciento. Y yo le veo, como decía Rafa, también mucho potencial. Eso me gustaría poner a probar lo seguro el fin de semana me ponga firme, que es cuando tengo tiempo, porque estoy de reunión en reunión, es como que me cuesta la semana, pero seguro el fin me ponga ahí a probar. Y cualquier duda eso, te mando mensajito Lucio y conectamos, charlamos.

**Lucio Rojas**: Buenísimo. Dale. Si querés un hack, en la página web hay un botón de WhatsApp que te lleva a mi WhatsApp. Si querés escribirme por WhatsApp directamente, mejor.

**Agustin Albiero**: Bueno Lucio, dale. Gracias. Gracias. Un gustazo haberte conocido. Muy buena onda. Y esto seguimos hablando.

**Lucio Rojas**: Gracias, vos también. Súper buena onda. Nos vemos.

**Agustin Albiero**: Abrazo.
