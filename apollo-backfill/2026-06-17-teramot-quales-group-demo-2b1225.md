# Teramot- Quales Group. Demo

**Fecha:** 2026-06-17T17:46:43.273+00:00  
**Duración:** ~47 min  
**Participantes:** Agustin Gaig <agaig@qualesgroup.com>, Facundo Belgrano <fbelgrano@qualesgroup.com>, Lucio Rojas <lucio@teramot.com>  
**Externos:** agaig@qualesgroup.com, fbelgrano@qualesgroup.com  
**Apollo ID:** 6a32e8a0ac313a000c2b1225

---

**Lucio Rojas**: No sé si les molesta que lleve la reunión, me queda en caso de levantar algún feedback. La fuente se puede seleccionar las tablas que uno quiere disponibilizarle la herramienta cuando la conecta, por ejemplo si no hubiésemos querido ver x tabla no se selecciona y se publica en esa tabla. Se pueden setear actualizaciones incrementales si la base de datos está preparada para no traerse las novedades, acá no deben estar preparadas para no traerse las novedades todos los días, sino traer el delta de novedades en una base de datos con histórico.

**Agustin Gaig**: En realidad en estas tablas sí hay campos de fecha que podrían usarse como delta, digamos para decir que estos son

**Facundo Belgrano**: nuevos,

**Lucio Rojas**: nosotros pedimos una fecha y un id único, poder también manejar los cambios hacia atrás, pero bueno ahí es cuestión de ver bien la base y setear que necesitamos nosotros. Bueno, una vez ahí se puede editar la conexión, además ya la dejó el equipo preparada. Una vez conectada la fuente se puede setear la actualización desde el tercer label a la derecha a la izquierda, en el panel de la izquierda para que se actualice cuando ustedes le da sentido, puede ser diario, por hora, semanal, depende del intervalo y demás. Bueno eso un poco el seteo de la configuración, ahí lo único que varía es que por ejemplo si hacemos una actualización por hora en vez de diaria aumenta el volumen de procesamiento que es una de las variables del pricing de la herramienta, no es lo mismo moverlos a dos una vez al día que 24. ¿Qué pasa una vez que conectamos la fuente de datos? Si queremos conectar más tenemos la opción arriba a la derecha donde vas a ver los distintos conectores que tenemos en seleccionar tipo de fuente en el desplegable de río siempre vamos sumando más, los objetivos de estos spring son sumar muchos conectores, así que van a ir viendo a medida que vayamos creciendo en ese sentido hasta ahora buscamos trabajar con los motores o los motores de datos que albergan la mayor cantidad de de soluciones posibles. Si querés cargar un s, los datos

**Agustin Gaig**: de s tienen que estar estructurados siempre ser CSV o pueden ser de otro

**Lucio Rojas**: tipo, hacer CSV, excel, parquet y JSON.

**Agustin Gaig**: ¿Y es una conexión por archivo por lo que veo acá o es en realidad una el bucket y te levanta

**Facundo Belgrano**: todo lo que tenés?

**Lucio Rojas**: No es al bucket, el bucket te da una UI y vos podés levantarlo. Si los datos están on premise, se hace un túnel VPN. Si necesitan un conector que no está dentro de los que nosotros ya exhibimos, se puede charlar y generalmente no suele tener costo. Bueno, dicho todo esto, un poco más el espacio, me queda un poquito de espacio publicitario. Después podemos ponernos a trabajar con los datos. En un segundo label van a ver lo que es el estudio de datos en el panel de la izquierda, que lo que hace es mostrarte las tablas que vos cargaste. La mayoría de las tablas van a estar sujetas a modificaciones automáticas que nosotros generamos para poder estandarizar y normalizar esa información que se ve en el segundo switcher de detalles de creación. Ahí va a tener SQL generado. Si se expande, vas a poder ver las transformaciones que hacemos para esas tablas, para hacer distintos joins. Y además cuando hacemos la transformación, levantamos todos los archivos de metadata para darle el contexto al MCB de cómo trabajan estas tablas.

**Agustin Gaig**: Pero acá en realidad la conexión en sí, este es un espejo. Bueno, acá no se cambió. From Silver. Entiendo que esto ya es una copia que los lleva un Silver. Ustedes, digamos, con esta estructura y adentro, en realidad lo que hizo fue Castó algunos, Castó algunos campos a lo que interpretó que iban a ser.

**Lucio Rojas**: Exacto. Nosotros guardamos lo que ustedes nos comparten en bronce, eso no lo disponibilizamos en Silver, ya empezamos a trabajarlo y hacernos un poco el owner de esas tablas. Así que ahora lo que ustedes, el objetivo por ahí de la herramienta es consumirla desde un modelo de inteligencia artificial. La idea es conectar el MCP. Para eso está la opción de conexión, ahí arriba a la derecha o abajo a la izquierda, que lo que hace es darte un URL y un client ID. Si ustedes usan Cloud, lo podemos configurar ahora. Ahí en personalizar, Elige conectores, no sé por qué Claude lo es contando. Ahí se puede generar un nuevo conector personalizado con más. Y te pide el nombre que le pones vos,

**Agustin Gaig**: La URL tengo que ser.

**Lucio Rojas**: Y el client id. Ahí van a ver todas las tools. Si querés, donde dice requiere aprobación, se puede permitir siempre para que no te moleste tanto. Esas son todas las tools que nosotros le disponibilizamos a nuestro MCP para trabajar sobre la herramienta. Ustedes van a ir viendo que a medida que necesiten va llamado distintas tools, quizás la que más vean es la de Query data para traerse alguna información o crear alguna tabla gold a partir de create gold table, pero bueno, perdí un poco el ownership de qué tool tenemos porque van sacando todos los días, pero siempre se le puede preguntar al mismo club. Que dulce. Ahora, desde un nuevo, esto es como cualquier MCP, se le pide que se conecte a Telamot y que para empezar nos liste los workspaces que tenemos. Ahora te va a hacer autentificarte. Ahí me estoy dando cuenta que Clot se dio por defecto un opus 4.8

**Agustin Gaig**: alto, sí no porque lo tenía Wenger laburando con eso.

**Facundo Belgrano**: En realidad

**Lucio Rojas**: esto es un no out contra la herramienta. Y ahora si vas sobre el de cuál es, te podés pedir que te liste las tablas que tiene y que te haga una descripción conceptual de qué significa cada una para ver cómo generó la metadata y después ya puedes empezar a pedirle que te sugiera análisis. Sí, te va a explicar que tiene cada tabla, va a ser un list de las tablas, va a ver la metadata y te va a explicar qué tiene. Está un poco raro, ya le permitimos hacer todo y después te pide permiso de vuelta. Acá lo interesante por ahí es, no sé si ustedes quieren hacer algo puntual con el caso de uso, si no, lo que está bueno es pedirle al mismo club te sugiera distintos análisis.

**Agustin Gaig**: Con esa acá yo vengo conversando y sabe qué es esto, digamos, Son 20 entidades lógicas con esta tabla física

**Facundo Belgrano**: acá

**Agustin Gaig**: nos estaremos capaz que lo tendría que aprobar Facu. Cuestión de que.

**Lucio Rojas**: Ahí si querés preguntarle ahora qué tipo de análisis puedo hacer, Sugerime tres análisis de alto valor de negocio para hacer con esto. Te va a sugerir las tablas gold cuando nos devuelva. Acá lo que hace Claude es usar toda su capacidad sobre tus datos y te da sugerir análisis, uno elige el que quiere realizar y ya te genera la tabla para ese análisis y después lo ejecutas con el mismo cloud. Esa tabla se mantiene actualizándose, ya es un ETL clásico.

**Agustin Gaig**: OK, si querés arranco por el 1 para mejor relación esfuerzo impacto. Te hago una primera preview de las tablas de ventas para confirmar cómo vienen los descuentos y los flags, o sea, definitivamente tenés que conocer del modelo o de qué te está trayendo ahí, porque

**Lucio Rojas**: te está queriendo corroborar, podés decirle que infiera todo.

**Agustin Gaig**: Infierito, no me preguntes nada. Listo. Vamos así con gana, con algo rápido.

**Lucio Rojas**: Sí, sí.

**Facundo Belgrano**: OK.

**Lucio Rojas**: Ahí quizás les lleve más tiempo. No voy a hablar por Cloudbo, siempre me sorprende. Vamos a dejarlo.

**Agustin Gaig**: No, igual con opus 4 y 8 en alto razonamiento tarda un toque, se me sume la vida, pero no importa,

**Lucio Rojas**: Ahí puede ir viendo lo que está haciendo, puedes ir viendo qué Tools llama, cómo razona. Generalmente Opus 4.8 tiene esto de razonar, otros modelos no lo hacen tanto.

**Agustin Gaig**: Siempre creo que la primera vez que lo debe usar lo debe volver a pedir, porque

**Lucio Rojas**: claro, para validarlo. Sí yo tengo sospecha también. Acá siempre puedes ver cómo razona, ver qué hace, qué query está haciendo, es todo transparente. ¿Ahora va lo que hace un poco Claude, qué función cumple? Es interpretar la intención de negocio. Acá podría dialogar 20 minutos para confirmar el scout de lo que se quiere hacer o hacer algo mucho más inferido como en este caso, y inyectar en Theramot una descripción con requerimientos funcionales de qué tiene que tener esa nueva tabla que el usuario de negocio pide. Después Telamo toma esa descripción que hace CL y con sus agentes de modeling o de creación de teles, genera la query, genera el update de nuestra infraestructura y se mantiene actualizando esos ETN en

**Agustin Gaig**: qué los desarrolla Lucio, o sea abajo. Porque usa AWS esto que están hechos en Lambda, ¿Qué es abajo? ¿Qué tecnología?

**Lucio Rojas**: Bien, no tengo un detalle bien técnico para responderte. Lo que sé es que se van a un bucket s y se levantan en la tina. Sé que usamos Lambda también porque se menciona mucho por ahí para explicarte bien el proceso estaría bueno que esté la infraestructura. Entiendo que ustedes usan AWS también, ¿No?

**Agustin Gaig**: Sí, sí, usamos. Para un montón de cosas usamos AWS. Por eso. Está creando la tabla Go.

**Lucio Rojas**: Ahí puedes ver la solicitud para entender que tenés que tocar el de solicitud. Ahí te va a decir, Ahí está explicándole a Theramot un poco qué es lo que tiene que hacer. Le diste las tablas donde tiene que buscarlo y ya dispató la construcción. Eso. Ahora desde Theramot se puede ver cómo se está creando la gold y suele tardar dos o tres minutos en crearse.

**Agustin Gaig**: Facturación, descarté y zona corruptos en la tabla, cuando quiera decir, fíjate cómo va y desde el lado de Teramot, me decías que acá podemos ver bien,

**Lucio Rojas**: no muestra en estudio de datos, Ahí va a mostrar, te hace una descripción de la tabla, y una vez se genere vas a poder ver la tabla. Te va a dar la posibilidad de hacer cuellos.

**Agustin Gaig**: ¿Construyó una única tabla gold basado en 20 en función de un requerimiento de negocio? No necesariamente, lo que hizo fue modelarlo. Todas las tablas silver que necesita, más todas las tablas gold que necesita para tener un modelo dimensional después a consumir. Por cada requisito te va creando distintas tablas gold.

**Lucio Rojas**: Bien, ahí es donde si ustedes en detalles de creación podés ver bien como la creo. Ahí tenés el linaje y las tablas que usó en origen está la descripción que hizo Claude, que era lo que se necesitaba, y tenés el SQL generado por Teramot. Acá yo lo que describís vos lo entiendo cómo. A ver, confirmame si lo interpreto bien. Vos me estás haciendo una pregunta y me estás creando una tabla para responderme esa pregunta. Me parece que eso es un poco eficiente en términos de nuevas tablas generadas en mi warehouse.

**Agustin Gaig**: Y a lo que doy es si por cada pregunta de negocio me va a crear una gold. Pero capaz que es el modelo, no lo sé, desconozco, digamos.

**Lucio Rojas**: Por eso estaba confirmando un poco lo que me nosotros creemos que esta herramienta tiene que tener dos usuarios, si querés, con perfiles distintos. Uno que sea el que lo administra SAPU, te voy a poner como ejemplo, no conozco bien tu rol dentro de cuáles, pero sería el que tiene acceso a la silver, entiende medianamente qué es lo que le va a preguntar el negocio, y le genera las tablas Gold con el 80 de la información que necesita consultar para que cada pregunta de negocio no genere una gold, sino que consuma de las que ya existen. Y después está el usuario que consume, por ahí tiene muy poco entendimiento de qué es lo que hay en la herramienta, de que es una silver, que es una gold y demás, y nada más quiere hacer preguntas. La idea es que a ese usuario no se le genere una tabla gold por cada una de las preguntas que hace. Y eso incluso se puede administrar desde los roles. Por ejemplo, si vos hacés una pregunta ahora, decís que te arme o un dashboard, o que te arme un análisis de lo que tiene la tabla,

**Facundo Belgrano**: o

**Lucio Rojas**: haces inteligencia comercial sobre esa tabla,

**Agustin Gaig**: En

**Facundo Belgrano**: vez de preguntarle en esa tabla golpe, hacele una pregunta relacionada con una frase de negocio, porque ahí nosotros estamos analizando ahí no sé, fíjate en la descripción. No, no, fíjate si no en el pedido que nos recomendó algo Claudio nos recomendó algo, le dijimos hacelo. Bueno, ¿Qué era lo que nos recomendó? Veamos eso y pidámoselo con un término de negocio como si lo está pidiendo un usuario.

**Lucio Rojas**: Me encanta Facu, es un poco lo que.

**Agustin Gaig**: Entonces respóndeme, le copio tal cual, dale.

**Lucio Rojas**: Ahí lo que nosotros solemos hacer es acompañar el uso de este tipo de usuarios con una skill o con un pron system que mejore o refine esa parte de decir me está haciendo una pregunta de negocio esta persona. Yo lo primero que voy a hacer es entender qué quiere con dos o tres preguntas de validación muy sencillas y después fijarme bien si ya tengo una tabla gold para responder eso. Volvé para atrás y decirle que no prepararlo. No hizo la confirmación todavía. No, fíjate que la tabla ya está, Pero ahí el ejemplo te va a servir para sacar un poco la duda que tenías. Borro lo que te contestó, te había dicho, la tabla se está construyendo. Voy a fijarme sobre los datos silver y voy a hacer una query directamente a la silver para responder eso. Eso es un poco lo que queremos evitar con la tabla Gol,

**Agustin Gaig**: que la facturación total. Fíjate que recién profundizó en los datos, se dio cuenta que había algún tema en realidad a nivel. No sé cómo infirió la nota de crédito igualmente, porque un código de nota de crédito no sé cómo lo habrá hecho, no vamos a ver el código ahora. Pero.

**Facundo Belgrano**: Básicamente le hicimos la pregunta y volvió a construir la tabla.

**Lucio Rojas**: No, no, no está consultando sobre la

**Agustin Gaig**: tabla, en realidad.

**Lucio Rojas**: Estaba confirmando un valor raro que vio. Está como autocorrigiendo

**Facundo Belgrano**: que en realidad lo

**Agustin Gaig**: está haciendo Claudí, no sé si Theramod Claudí o qué. Quién lo está terminando de masticar al tema. No sé hasta dónde llega. No sé hasta dónde llega en realidad Theramot como producto y dónde en realidad es Claude usando SMCP para razonar y sacar conclusiones.

**Lucio Rojas**: Perfecto. Como producto llega si querés solamente al lado de Telamo, recibir instrucciones y generar ETLs, disponibilizar esa tabla a partir de Tools. Después Claude lo que hace es inyecta esas instrucciones para generar la gold a partir de lo que interpreta el negocio y después usar las tools que apuntan a todas las tablas que tiene disponible para responder preguntas. Y ahí lo que hace es ir a una Gold, ir a una Silver, dependiendo la pregunta. Nosotros por eso creamos prompts para que vaya si es un usuario de negocio a las Gol que ya tiene disponibles o creamos proyectos solamente con las gols para que consulte ahí y va generando respuestas a las tablas que. No creo. No, no, no. Está debagueando la tabla porque veo algo raro. Claude pensando.

**Agustin Gaig**: Sí, sí, sí. Por eso acá ya está al lado de Claude que está yendo a buscar info, Razona, vuelve.

**Lucio Rojas**: Sí, está resonando porque un rato raro que no le gusta.

**Agustin Gaig**: Bueno, claro, lo que pasa que acá se dio cuenta que tiene que ir a OTR,

**Lucio Rojas**: Había que ver bien qué hizo con la. Estaba haciendo verificaciones. Esto nosotros éramos la posibilidad de que consulte a las Silver, que consulte a las Bronce para hacer verificaciones de bagging o demás por parte el usuario. Pero acá ya un poco clot, viendo algo raro y viendo por qué pasó.

**Agustin Gaig**: Notas de crédito, datos sólidos de fondo, sobre vista, ruidoso, inflado por fija, un precio de vista corrupto, tomarlo como techo, venta.

**Lucio Rojas**: Bien, entonces ahí te está diciendo que hay un problema de datos en importe. A mí me interesaría mucho ahora entender ese importe NC, si tiene un importe, un outlier o un importe raro que viene desde su base de datos que nos pasaron a nosotros desde la Bronce o fue algo que se convirtió en el medio con los datos, ¿Entendés?

**Agustin Gaig**: Sí, en realidad no, estaba mirando un poquito acá y demás.

**Lucio Rojas**: Perdón, me decías sí que. Los problemas de calidad de datos ustedes ya los tienen.

**Agustin Gaig**: Sí, hay problemas calidad de datos sobre la tabla, ¿No? Sí, sí, sí. Lo que pasa que el modelo es complejo, no necesariamente las notas de crédito sean mayores, la factura está mal, está mal, pero no tan mal, digamos. Pero bueno, tenemos que poner a analizar todo el negocio. A lo que voy es en gran medida a ver como para la idea, nosotros tenemos una capa raw con eso en realidad Teramot se conectó, armó una Silver a través de preguntas de negocio en Claudi lo que hizo fue definir qué tablas Gol necesita y a través del MCP las crea y luego en realidad como cada una de estas tablas Gol tiene metadata, por lo que veo acá, y tiene descripciones, tiene linaje, tiene acá toda una descripción. Esta es una metadata de la tabla. Con esto luego lo que puede hacer Claudí u otro Gemini o demás que estaban en la web, es conectarse a este modelo vial, comenzar este modelo y empezar a responder preguntas de negocio. Ese sería el punto 2. Lo que queda delegado a Teramot es en realidad el APR continuo de la actualización del esquema Silver. Bien, porque el primer esquema que hay es un silver. No, o sea, el primero que se genera es un silver.

**Lucio Rojas**: En realidad el primero que se genera es un bronce que nosotros demostramos. El primero que se debe un silver para el usuario.

**Agustin Gaig**: El silver este se corre cada n cantidad de minutos, cada n cantidad de tiempo, con un cron y esta tabla go, cada cuánto corren al mismo cron que este, terminan la Silver y se corren.

**Lucio Rojas**: Sí se actualiza sobre la Silver. OK.

**Agustin Gaig**: Bien, en el caso de que esto esté mal, el usuario viene y lo edita acá y le va cambiando la metadata de este modelo. Bien,

**Lucio Rojas**: Y también lo puede hacer desde Club. Club puede editar la tabla que creó en caso de que la metadata de la silver. Acá estabas viendo ese origen que vos ves ahí, no sé si lo desplegás ahí. Quiero confirmar que se llegó bien a la conclusión. Este lo creó Claude. OK. Y también sirve como metadata. Es como doble. Tiene doble función si querés verlo así. Lo que hizo Claude es entender preguntas de negocio, generar este origen y después nosotros levantamos esto para hacer el texture y lo levantamos infraestructura y queda la otra. Las tablas Silver, todas las transformaciones que tiene, que yo vi algunas tablas que tienen transformaciones bastante grandes, tendremos que buscarlo. Y la metadata que se genera desde Theramot sobre esa silver, por ahora es un poco caja cerrada. Theramot va levantar la Silver, entenderlas y generar transformaciones un poco de como entiende que esa data tiene que estar normalizada, está en Roma, poder abrir un poco más a que el usuario todo lo

**Agustin Gaig**: que Silver quiso acá en realidad si nosotros le queremos decir, che, no, mira, no castees como int al id propietario sapo, que es un número, que en realidad está bien que es un número, pero en realidad no es algo que deberíamos sumar, ni restar, ni nada. Esto lo tenemos que pedir porque no lo puede editar el usuario.

**Lucio Rojas**: Bien, hoy en día no, y está en roadmap para dentro de. Justo lo venimos tratando de que se pueda editar por el usuario, Bien, y

**Agustin Gaig**: ver tabla Gol. En realidad acá podría yo arrastrar tabla Gol, darle un metadatado, Bien, distrucciones, puede

**Lucio Rojas**: hacerlo manual eso un poco lo que hace Claud y lo que me decías vos hoy es de que por cada interacción que tengo con un usuario, más una Gol. No necesariamente, Si vos ya administraste un poco la herramienta y creaste como unos maestros y le das a los usuarios finales de negocio un acceso read only, lo único que pueden hacer son preguntas y análisis de negocios sobre esas tablas que vos les diste creadas como Gold, que es un poco para mí una evolución de BI de Business Intelligence. Te doy tablas y preguntales y a ese usuario le da la posibilidad de crear Gol si la tiene alguien que administre la herramienta.

**Agustin Gaig**: Te hago una pregunta y esto es la única forma después de consumir esta capa Gold, o sea, ¿Cuáles son las distintas posibilidades de consumo de esta capa Gold? ¿La podría consumir desde un Dasher en Power BI? ¿La podría Consumir desde un Dashboard en React que tiene una conexión a Teramot y expone la info? ¿Cuáles son las fórmulas? Porque hasta acá, bueno, listo, con Claudi por MCP lo puede ir a consultar y sacar conclusiones. ¿Pero si es un modelo Gol, contra qué lo puedo consumir?

**Lucio Rojas**: Ahí tenés un data igles a la izquierda, en el cuarto, creo que es el quinto nivel.

**Agustin Gaig**: Quinto salida de datos.

**Lucio Rojas**: Ahí lo que puedes hacer es generarte salida de datos para las tablas que vos elijas y te da los

**Facundo Belgrano**: las

**Lucio Rojas**: distintas variables para configurar conexiones a otras herramientas como puede ser Power BI.

**Agustin Gaig**: Lo que podría hacer es cargando tablas de AWS, o sea creo un usuario,

**Lucio Rojas**: si querés probar, proba alguna tabla y fíjate los datos que te da.

**Agustin Gaig**: Para que acá fuga, Vamos acá. Bien, Dar acceso a tablas. OK, y con este usuario para acceso a tablas, revocar tabla, revocar BD, eliminar usuario, opciones de autenticación. ¿Me debería poder conectar con estos datos de AWS?

**Lucio Rojas**: Sí, te puedes conectar a la tabla desde distintos servicios. Pone Power BI, te pide esta opción, autentificación para conectarte a la tabla Power BI. Después se actualiza. A medida que se actualiza toda tu Silver. En realidad también lo puedes consumir desde Cloud Code para armar algo en React y publicarlo, yo lo he hecho también te podemos dar acceso a la tabla Gold para correrle un modelo de Machine Learning. Ahí un poco nuestro valor es armarte la tabla y exponértela para que vos la consumas como te parezca. Lo que está más facilitado es la herramienta, es consumirla desde Cloud y armarte dashboards y demás. Ahora desde Cowork, los dashboards tienen la posibilidad de actualizarse a medida que vos lo vas reflejando, porque tiene una función que llama el MCP, te arma HTML y te lo actualiza.

**Agustin Gaig**: Perdón, para que estoy dando con la

**Lucio Rojas**: instrucción mientras como Desde Cloud Cowork ahora está la posibilidad de crearte los dashboards y con HTML y se actualizan a medida que vos los vas refrescando y en un proyecto de Enterprise los compartís para que lo vea toda la organización. Eso para mí es un poco la muerte de Power en un punto. Puedes crearle Artifac y compartirlo. No sé si ustedes tienen cuenta empresarial.

**Agustin Gaig**: Sí, sí tenemos.

**Lucio Rojas**: Ahí lo compartís, te creas un Dash con esa Gol, se actualiza a medida que vos lo refrescás y lo compartís con tu equipo que apunta a esa tabla Gold. Esa es una función nueva de Cloud, la estamos explorando esta semana. Y si no, si vos elegís que se deploye todo en tu tenant, ya te queda la tabla guardada en tus servicios de AWS. Depende de nosotros para consumirla,

**Facundo Belgrano**: ¿No?

**Agustin Gaig**: Me fui moviendo y me parece que. Facu no.

**Facundo Belgrano**: ¿Y ahí cuáles serían los costos, digamos, de tener diferentes tipos de servicios? Porque por lo que vi ahí, cada licencia tiene una capacidad de procesamiento, una cantidad de memoria y un espacio disponible en el TENAM de AWS. Si yo lo implemento en mi AWS, ¿Qué licenciamiento tendría que pagar?

**Lucio Rojas**: Bien, ahí si querés Agus entramo,

**Agustin Gaig**: Estaban precios.

**Lucio Rojas**: OK, bien. Ahí lo que nosotros vendemos un tire que fluye todo el tenant, como decir Facu, si es de su lado, las variables de almacenamiento y procesamiento no contarían para. Sería en función a usuarios y a tablas Gold, que es un poco el valor que queda dentro de nuestra herramienta. ¿Pero qué costo tendría, no? Y se mantiene el mismo tiro.

**Agustin Gaig**: Sigue siendo 399 dólares por mes, pero posteado en realidad dentro del tenant del cliente, vamos a poner, si yo voy por esta, no cuenta ni esto ni esto. Los 20 dólares. La limitación de 20 usuarios. Está y la de 5. 20 golpes. La de 5 usuarios se mantiene a 400 %.

**Lucio Rojas**: Claro. Y igualmente es una buena pregunta. El equipo comercial después lo voy a repreguntar. Yo estoy más del lado de implementación, pero me parece, entiendo tu consulta. Decir, bueno, es un precio distinto. Si está todo nuestro Tenon. Eso lo voy a consultar.

**Facundo Belgrano**: Claro, porque yo por otro lado tengo el costo del procesamiento. Claro.

**Agustin Gaig**: Sí, a ver, en realidad algo que tal vez creo que está muy bien gobernado, o sea que los que solamente pueden crear tablas deberían ser determinados tablas Gold, determinados usuarios, tiene que estar bien gobernado para aplicarlo en la lógica de creación de tablas Gold y no que por cada, como te decía, por cada pregunta de negocio te termine armando una tabla, porque Si no estas 20 no te alcanzan para nada.

**Lucio Rojas**: 100%.

**Agustin Gaig**: Por otro lado, pensándolo un poco en sí dependes en gran medida de que Claude razone y proponga las tablas Gold, en realidad, o sea, eso no lo tiene. A lo que voy es, Theramo en realidad lo que te provee es toda la infraestructura para crear para que después no estoy tirando abajo.

**Lucio Rojas**: Dejo eso Lucio, pero lo que te

**Agustin Gaig**: están dando infraestructura, pero en sí la capa de inteligencia, ¿Te estás apoyando en cloud o en el que sea? Bueno, en cloud, porque estás usando MCP en cloud para en realidad que resuelve y defina qué tablas se necesitan y todo lo demás.

**Lucio Rojas**: Nosotros igual un poco también propiciamos eso desde nuestro pitch, permitirte a vos trabajar con tus tablas desde Cloud. Igualmente también está la posibilidad de hacerlo sin clot y uno poner las instrucciones

**Agustin Gaig**: de acá a acá, ir creando. Lobo en gran medida lo que tiene que es como que no aceleraría, digamos, la parte.

**Lucio Rojas**: Y bueno, después lo otro que también tiene el valor es eso de generarte los dashboard, el análisis, los gráficos para los usuarios de negocio dentro de una empresa consultando una tabla desde Cloud. Eso para los usuarios finales que están acostumbrados en el mejor de los casos, a mirar un Power BI en las empresas que hemos llegado, quizás yo empresa una tarea totalmente distinta. Es un valor puntual. Es un valor claro. Es decir, bueno, ahora puedo hacer ayuda, trabajar con blog sobre los datos que antes miraban en Power BI.

**Facundo Belgrano**: OK,

**Agustin Gaig**: bien, Facu.

**Facundo Belgrano**: No, ninguna pregunta más. Creo que está bastante claro cómo funciona y dónde está el potencial de esto.

**Agustin Gaig**: Sí, sí, te simplifica tener toda una infraestructura montada para mantener esto. Sí, gran tema. Creo que está en la construcción de

**Lucio Rojas**: las tablas ahí dentro de si volvés un label para atrás a los proyectos dentro de Téram, Si vas a los tres puntitos del proyecto, podés administrar los roles de los miembros. Por esto que vos decías, por ejemplo, el solo lectura no puede crear tablas Gol, solamente las puede construir, consumir. El miembro puede crear tablas Gol, pero no puede hacer data. El administrador puede hacer data y crear Gol si el propietario te prende y te apague la luz si quiere las diferencias. Ahí lo explica mejor, espero que diga lo que acabo de decir.

**Agustin Gaig**: No, no, sí, sí, porque lo más

**Lucio Rojas**: temprano ahí es como se administra la herramienta. ¿Sí nosotros entendemos el uso, que nos pasó? Exactamente lo que vos decís, le dimos esto a un CEO, empezó a hacer preguntas de negocio, llegó a las tablas, a las 20 tablas gold al quinto día porque estaba recobrado preguntando, ahora tengo que pasarme de T, cuando se pone a ver, está haciendo la tabla gold para consultar la misma información filtrada por dos variables distintas. Y vos ahí con un poco de ojo que decís, no, quedate la tabla Gold sin filtros y consumirla y hacer el filtro con el consumo. Pero bueno, ahí vos necesitas un usuario administrador que pueda tomar el ownership de qué tablas hay, por lo menos acomodarlo, armar los maestros y después rentar el consumo libre. La hipótesis es esto de darle usuarios. Yo soy un usuario no técnico, no tengo un background de ingeniería ni de datos ni demás, y me sirve mucho para quedarme en mis tablas. Yo uso esto internamente para ver métricas de uso de usuarios, registros directamente contra base a todo el sistema y a mí me resulta el valor clarísimo, porque bueno, esto no lo hubiese podido hacer sin la herramienta y quizás un usuario del sistema te dice, bueno, ahora puedo George achicar un poco el backlog con esto que me permite otra velocidad o me permite delegárselo a alguien que no sea tan técnico o que el equipo de negocio se arme su propio equipo de BI o de Business Intelligence. Así que bueno, eso un poco la herramienta, no sé qué les pareció, si les gustó, si no, si quieren probarlo,

**Agustin Gaig**: sí en realidad quiere darle una vuelta a rosca, ver un poquito mensualidad,

**Lucio Rojas**: a

**Agustin Gaig**: ver internamente no sé, pero sí cómo la podríamos posicionar también cómo aceleraría nuestro proceso de desarrollo. Ese es el gran punto. Entiendo lo que hace En realidad lo que voy es, voy a sonar arrogante con esto, pero si en realidad lo que le dejo a Claude es lo conecto contra WS, le digo che, vos acá tenés estos servicios, podés construir lo que quieras, armame, en realidad

**Lucio Rojas**: vamos a

**Agustin Gaig**: poner que definimos que vamos por Lambda, armame este, armame el otro, en gran medida, no digo que lo haga, ni lo haga bien, ni vamos a tardar un momento en hacerlo, lejos de eso. OK, ahí está el diferencial de que ustedes ya lo hicieron, digamos. Podrías lograr el mismo efecto 100%.

**Lucio Rojas**: Mira esto, de acuerdo, yo lo tengo vaciado, hay empresas que me dicen mi warehouse está perfecto, yo necesito que me hagan metadata ni nada, yo me hago un MCP y uso para crearme nuevas tablas y estoy contento con eso. Válido. No le pasa a todas las empresas, la mayoría de las empresas es el contrario, es decir, no sé ni por dónde arrancar, ni tengo equipo de datos, entonces quizás está en un corner side un poco ya más, muy profesionalizado de todo lo que es un equipo de datos, pero proveer esto por ahí, equipos de datos de consultoría de datos, usar esto para proveer servicios, para agilizar la velocidad de entrega de delivery, hay tipo de empresas que necesitan eso, o nosotros también dejamos que los lleven como marca blanca al cliente y que cobren sobre implementación para armar el warehouse de una empresa, no nos molesta tampoco. Y después lo otro que decías es si se puede hacer la licencia nuestra gratis o vale 400 dólares. Hay que poner un poco en la balanza el costo del desarrollo contra no estamos charlando igualmente.

**Agustin Gaig**: Bueno, mira, ahí lo que estaba haciendo es ver en realidad, y fíjate que este modelo que en realidad no termina, o sea, este modelo que todo esto que subimos justo termino de darle la vuelta a rosca, pensá que ese modelo que responde está bien, son ocho dominios de información, venta, despacho, son distintas cuestiones, actividades del cerem y demás, son 8 dominios de información, tenés 23 tablas en un modelo gold para poder después, no con el enfoque que acabamos de ver de responder una pregunta de negocio, sino un enfoque, una capa gold sobre la cual después monto preguntas de negocio, ya habiendo depurado todo, ya te consumiste los 400 dólares mensual de mínima, porque ya tenés 24 tablas, salvo que no vayas por ese enfoque y vayas por un enfoque como el que vimos recién de tablas Gol que responden a preguntas propias de negocio. Hay que ver qué enfoque querés hacer ahí.

**Lucio Rojas**: No te seguí muy bien esto que

**Agustin Gaig**: vimos recién ahí, esas tablas que tenemos, yo subí hoy más temprano tablas transaccionales y tablas de maestros, donde las tablas transaccionales en gran medida repiten un montón de información de los maestros porque no están depuradas. Es como decir una empresa que no tiene un warehouse y tu maestro ya

**Lucio Rojas**: son como tus gols.

**Agustin Gaig**: No, ni tampoco de todo eso se deberían construir, como decimos, los golds y las tablas transaccionales para después poder consumir. Eso implica más o menos, por lo que le pregunté a Claudio, usando toda la magia, lo que acabamos de ver, que Tiene que construir 24 tablas para armar un modelo wall dimensional bien depurado, con reglas bien armadas, no me repitas el nombre del cliente acá y allá,

**Lucio Rojas**: para liberar eso al usuario que consuma libremente. Entendí, o sea, vos me dijiste más

**Agustin Gaig**: o menos con estos datos bien armadas,

**Facundo Belgrano**: es un modelo con metodología Kimball que separa dimensiones de hechos y te arma un único modelo para responder todas las consultas que el usuario hace sobre ese entorno o ese alcance que es definido para estas tablas. Entonces ahí ya te consumís la licencia mínima, digamos que 20 gol son 24 en este caso, porque el dominio es grande, incluso podría ser AP, podría ser mucho más grande, agregándole pequeños cambios como categoría y subcategoría de producto, y eso ya te multiplica o dimensiones de tiempo que te permitan hacer, no sé, distintos cruces de la información, por ejemplo el acumulado anual y el interanual acumulado en los últimos seis meses, mes contra mes, year to day, entre años agregás por lo menos dos tablas más de tiempo que te van cambiando la cantidad de dimensiones. Nada medio técnico esto, pero nosotros lo vamos pensando, porque si nosotros lo queremos implementar, ya sea para nosotros o para alguien más, tenemos que pensar en estas entre comillas, limitaciones que tienen cada uno de los licenciamientos.

**Lucio Rojas**: Ahí nosotros, paréntesis, no sé cuánto es el contexto que tiene. De Telamot si hablaste una vez con. Pero somos una startup, tenemos un año de ya tener este producto bien definido, estamos yendo al mercado y no siempre nos encontramos con usuarios con su nivel de tecnicidad y de conocimiento. Ya se dieron cuenta en una reunión de una hora, bien cómo funciona la herramienta y empezaron a hacer hipótesis sobre los planes. A nosotros nos sirve un montón eso y que nos diga mira el valor yo lo veo re claro y el precio me está haciendo una traba cómo está la licencia de herramienta o que usted haga un balance, decir bueno a mí me conviene pagar 400 dólares a tener que hacer todo este trabajo yo. Si usted en un momento tienen algo con respecto a eso, el pricing, decir bueno tenemos esta idea, nosotros súper abiertos a escucharlo y elevarlo a algún nivel más el level para que lo puedan plantear y ver si algún acuerdo comercial no hay problema.

**Facundo Belgrano**: Sí, sí, súper. ¿Trabajan con alguna empresa, tiene algún partner digamos, o sea alguien que los haya contratado a usted para a través de ustedes vender el servicio de modelado?

**Lucio Rojas**: Bien, todavía no tenemos ninguno realmente productivo. Sí, hemos tenido varias charlas y como te digo estamos empezando y están un poco encaminándose hacia eso y ahora tenemos un kick off dentro un poco con alguna empresa que quiere hacer algo así, pero no son muchos los casos y es un poco lo que nosotros creemos que que estaría bueno. Así que nos gustaría tener más casos de eso.

**Agustin Gaig**: Sí trabajamos Bruno en su momento de esto, che bueno, lo que necesitamos hoy, gente que tal vez nos acerque el cliente final. Claro, bueno, ustedes tienen los clientes final bueno que nos acercan a nosotros con marca blanca, con lo que sea, como chapate más temprano y empezamos a crecer sería un poco el punto.

**Lucio Rojas**: Sí, 100%. Nosotros tenemos muchos clientes finales, nos llegan muchos clientes finales, sobre todo por el branding, por lo que es la IA y demás, quieren que la implementación sea medio ad hoc y nosotros como ustedes se dan cuenta muy bien, metemos una herramienta, un SAS, entonces ahí esa sinergia está buena y nosotros súper abierto y esperándolo un poco, bueno

**Agustin Gaig**: nos lo quedamos para mirar, lo miramos un poco, lo charlamos internamente y vemos qué podemos acoplar de todo esto.

**Lucio Rojas**: Buenísimo. Sí yo dejo a disposición mi mail, cualquier otra consulta, si quieren probarlo y

**Agustin Gaig**: demás, para qué hora voy a desactivar el Chrome porque si no te va a quedar corriendo el pedo que lo teníamos por ahí. Eliminar programación.

**Lucio Rojas**: Bueno, espero que se haya entendido un poco todo, si tienen más dudas me pueden escribir. Perfecto, súper claro.

**Facundo Belgrano**: Muchas Gracias.

**Lucio Rojas**: You.
