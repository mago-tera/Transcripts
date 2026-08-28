# Weekly Teramot - BCR

**Fecha:** 2026-05-26T14:59:05.591+00:00  
**Duración:** ~45 min  
**Participantes:** read.ai meeting notes <>, Lucio Rojas <lucio@teramot.com>, Romano Bazán, Ayelen <>, Schmidt, Nicole <nschmidt@bcr.com.ar>  
**Externos:** nschmidt@bcr.com.ar  
**Apollo ID:** 6a15c08fda4ffe0014414e29

---

**Lucio Rojas**: Buenas, ¿Cómo están?

**Schmidt, Nicole**: Buenas.

**Romano Bazán, Ayelen**: Hola, ¿Cómo va?

**Lucio Rojas**: ¿Todo bien?

**Schmidt, Nicole**: Todo bien.

**Lucio Rojas**: Mi cámara está peleada de la vida.

**Romano Bazán, Ayelen**: Sí, no pasa nada con Teams ahora aprendemos.

**Lucio Rojas**: Muy martes.

**Romano Bazán, Ayelen**: Claro, fin de largo.

**Lucio Rojas**: Pero la mía

**Schmidt, Nicole**: todo bien, todo bien.

**Romano Bazán, Ayelen**: Bien, todo bien.

**Lucio Rojas**: Bueno, fin de. Nadie quería estar acá el martes, pero bueno, trabajando, digo. ¿Cómo le fue el otro día la presentación? ¿Pudiste hacerlo? Habíamos hablado.

**Romano Bazán, Ayelen**: Perdón, ¿De qué estamos hablando? ¿Lo de DJ o esto no lo hicimos? No sé a qué te referís con presentación. Lo que estuvimos haciendo prueba con los usuarios. Sí, ahí recién estábamos también con ellos, nos juntamos recién y tuvimos ya algunos problemitas, encontramos algunas pruebas o cosas que nos fueron dando errores. Lo primero que pasó es que nos faltaban cargar tablas, que yo y las estuve cargando algunas, lo que sí me tardó un montón de tiempo, como tres horas para cargar dos tablas, son como las más importantes, pero bueno, tardó un montón de tiempo.

**Lucio Rojas**: ¿Y cómo las cargaste?

**Romano Bazán, Ayelen**: Ahora les comparto. Esta era la que ya estaba creada, que habían creado ustedes, porque si yo entraba acá no me dejaba, o sea la conexión es la misma y quería cargar, crear tablas nuevas acá y no sabía cómo, entonces como que creé una conexión distinta a la misma base y acá seleccioné las tablas que quería.

**Lucio Rojas**: Sí, habría que editarla la conexión. Esto es, O sea, se puede seguramente crear la fuente de vuelta con todas las tablas seleccionadas, creo que es una obvia, no sé si se puede editar ahí. Acabo de preguntarle archivo de las conexiones, No, se tiene que crear de nuevo la source,

**Romano Bazán, Ayelen**: o sea, tengo que crear una nueva como esta que creé.

**Lucio Rojas**: Claro, seleccionar todo las tablas que querías.

**Romano Bazán, Ayelen**: ¿OK, Y el tema del tiempo de carga?

**Lucio Rojas**: El tiempo de carga, generalmente suelen tardar en hacer una conexión nueva en promedio ese tiempo, cuando es así, por VPN, alguna base de datos que analizar, es que mataron eso. Cuando llamas algo puntual, ponele alguna tabla que vos cargas por CSV o demás, tarda bastante menos, tarda algo de cuarenta, treinta minutos, pero el tiempo está un poco dentro de lo normal.

**Romano Bazán, Ayelen**: OK, porque ahora por ejemplo, ahora cargamos estas y ahora haciendo pruebas recién con los usuarios encontramos más tablas que faltarían cargar ahí, que tendríamos que hacer una conexión nueva y volver a cargar todo desde cero.

**Lucio Rojas**: Sí, Bueno, supongo yo que deberá hacerlo hasta que queden todas las tablas que necesita. Eso suele tardar un promedio de más de una hora, hoy tres como tardó, estamos medio OK.

**Romano Bazán, Ayelen**: Bueno, eso sería por un lado, o sea nos falta hacer la conexión esa con las tablas que faltan y después lo que vimos es que hay algunas tablas. Si, acá me deja ver la fac, No sé por qué acá no me deja como No, dentro de una de las fac había un campo que, o sea, si vos ves por ejemplo todas las tablas veíamos como el detalle de la query que hizo por detrás y todas eran como un select a la tabla directamente de los campos, pero encontramos una por ejemplo que hizo todo una lógica que aplicó toda una lógica que nosotros no se lo dijimos, que la hizo como por defecto y cambió un campo entero como a una fecha,

**Schmidt, Nicole**: pero

**Romano Bazán, Ayelen**: no sabemos por qué lo hizo

**Schmidt, Nicole**: este el campo que es aquí a una dimensión, la dimensión de solicitud info que está acá. Solicitud info Claro, en la misma pregunta que le estuvimos haciendo nos tiró che, no puedo relacionar estas dos, está raro el tipo de datos y. Y cuando nos dijo eso del tipo dato ahí nos dimos cuenta, de hecho nos dijo así literal. Dice el join sigue fallando por el tipo de dato raro en solicitud info key, voy a intentar con otro enfoque y termina haciendo cualquier cosa para poder relacionarla, le tira un gear al campo y devuelve valores que no van, pero es porque se hizo esto al momento de cargar esta tabla, o sea la fac de solicitud se hizo este esto que no sé por qué en la solicitud info que un int, o sea en la base de datos lo tenemos como un int y es una clave a la otra tabla.

**Lucio Rojas**: Eso ahí lo que hay son agentes, nosotros llamamos de primera categoría o primera capa que se ocupan de esa transformación de Veronce que como tienen hasta ahora ustedes a Silver como es el formato que pide la herramienta para empezar a trabajarlas, que hacen transformaciones y las hacen predeterminadas. Hay casos muy puntuales donde se equivocan como en este y nosotros tenemos que verlo por atrás. Te pido si querés que me pases la transformación, está la tabla y lo vemos nosotros.

**Schmidt, Nicole**: Pasó el código este

**Lucio Rojas**: debe faltar solicitud.

**Schmidt, Nicole**: Sí, Si, yo estuve chequeando y hay algunas que como que lo hace en algunos varios lugares digamos, como que cambia, bueno acá hace otro con el código postal de localidad pero no lo cambia tanto tipo, bueno le saca los ceros y tiene adelante y esas cosas me parece. Y no sé, era más que nada. Ahí sí hizo como medio cualquiera porque. Pero podríamos como primer caso acá también hace un array join, o sea no tengo ni idea, encima todo medio complejo, Como que nuestras tablas en sí no tendrían que tener medio como transformaciones. No sé si se puede poner algo como por defecto que no tenga.

**Lucio Rojas**: Bien, Tomo nota de esto y lo llevo a la parte de los chicos de producto y después respondo por mail. No puedo responderlo ahora. Te pido bien que me digas cuál es la tabla que tiene el campo de vuelta. Es. ¿Y era el aquí para hacer el join con qué otra tabla?

**Schmidt, Nicole**: Dim solicitud info. Quin bim solicitud info es la que está acá en Terapot.

**Lucio Rojas**: Si el debe lo pone adelante para. Porque es el nombre de la source. Tenemos ese tema y tenemos el tema de que para actualizar la tabla

**Schmidt, Nicole**: tienes

**Lucio Rojas**: que generar una fuente nueva. También es un tema eso. Nosotros ahí sabemos que sabemos que no está bien eso de tener que crear una source nueva para actualizarla, para cargarle dos o tres tablas extra. Entiendo que está en roadmap de cambiarlo por ahora hay que generar la source nueva e ir cargando las tablas. Eso tiene la complejidad de que si ustedes tenían golds creadas, o sea pone que tienen cargadas las 17 tablas que ya tenían hasta ahora y crearon tres gols y ahora necesitan cargar dos tablas más y para eso hacen una source nueva al mismo warehouse y cargan 19 y pisan las 17 que ya tenían y eliminan esas source, las 3 go que tenían creadas se van a romper porque estás eliminando la fuente. Una opción sería cargar nada más las dos tablas nuevas como hiciste hasta ahora y seguir usando la herramienta sin problemas porque puede hacer los joins y las relaciones entre las distintas fuentes indistintamente, no hace falta cargar todo de vuelta. Si ustedes quieren tenerlo más prolijo y tener una sola fuente y cargar las 19 tablas de vuelta, tienen que volver a crear las gol. ¿Entienden más o menos el punto de eso? Así que nosotros sabemos que no es lo mejor, estamos todavía para modificar. Después tenemos lo del modeling, lo del agente, este inversor de las tablas y lo de las fuentes. ¿Tiene algún otro inconveniente, alguna otra duda?

**Schmidt, Nicole**: No ahí igual con respecto a las fuentes o sea el cambio es que se llaman distintas, pero yo acá podría crear Gol con esta distinta fuente y no pasa nada, digamos.

**Lucio Rojas**: Sí,

**Schmidt, Nicole**: el tema, si yo ya creé una Go y no estaba esa fuente antes, ahí se complica también hacerla. No, o sea, como que no creamos ninguna todavía, Por eso estamos re perdida, o sea, capaz que todavía falta que creemos, ¿No?

**Lucio Rojas**: ¿Que hace la gol? La Gol toma, toma las tablas que vos tenés acá en toda esta columna silver y te crea una tabla nueva haciendo los joins entre las distintas tablas para que la información esté más accesible a la gente para consultarlo. ¿Entonces en vez de tener que hacer una que? 5 tablas distintas, hacer una query a una que lleven los datos consolidados y si querés hasta algunas columnas nuevas calculadas. Eso queda como ETL y ya se mantiene actualizándose. Si vos de las 17 tablas que tenías usaste 5 para crear una tabla gold y después cargas dos tablas más y creas otra tabla distinta usando las dos fuentes, no hay problema. Acá el problema es si vos cargas las 19 tablas de vuelta y borras la fuente anterior tomando de input, la tabla Gol desaparece.

**Schmidt, Nicole**: Está bien, está bien. Sí, sí, sí, está bien.

**Lucio Rojas**: No es retroactivo, pero si sumas más fuentes y combinas entre distintas fuentes, sin problema, está bien.

**Schmidt, Nicole**: Está bien. Joya.

**Lucio Rojas**: Está bien.

**Schmidt, Nicole**: OK, Sí, bueno, como que medio que estamos en cero. No sé si por ahí conviene dejarlo prolijito como una única fuente y ya así nos queda. Porque ya sabemos que todo lo del cubo de solicitudes va a ser como una fuente en específico. Después capaz que sí está bien separar en distintas fuentes, porque no sé si es a nivel permisos, que después nos va a ser más fácil mapear esas cosas, ponele, tipo si agregamos después a futuro otras tablas, lo que sea, sería identificable. Che, todo esto pertenece a Solicitudes, porque nuestros permisos dentro de bolsa van en base a esos cubos en sí y a esas cosas. Entonces capaz que diferenciar distintas fuentes ayuda a tener como esa separación de los permisos. Ni idea, estoy tirándolo como. No sé cómo lo vamos a manejar

**Lucio Rojas**: por ahí cuál es eso es más de ustedes. Cómo quieren tener las fuentes creadas, pueden, si tienen de vuelta el ejemplo, 17 tablas y 10 son de solicitudes y 7 son de otro concepto que tengan ustedes, lo pueden separar en dos fuentes, o si es todo solicitudes dejan las 17 fundas un solo nombre de fuente. Claro, depende la arquitectura que le quieran dar ustedes a las fuentes dentro de la solución.

**Schmidt, Nicole**: OK.

**Lucio Rojas**: La herramienta después ve que tiene disponible tablas silver, que serían estas que están todas listadas acá a la izquierda. Si vos sumas una tabla de un CSV, por ejemplo, la toma como una más, no distingue de qué fuente viene para trabajarla.

**Schmidt, Nicole**: Sí, sí, te entiendo. Sí, sí. Más que nada como para ver cómo nos organizamos en sí. Pero está bueno para tenerlo en cuenta.

**Lucio Rojas**: Hay preguntas después más de mi lado. Lo que hicieron con los usuarios fue darles el MCP que pregunten.

**Schmidt, Nicole**: En realidad estuvimos compartiendo pantalla y preguntando desde acá, porque la cuenta que ellos tienen de cloud es compartida entre todos los usuarios también dentro de su área. Entonces nos daba miedo de que después alguno vea algo ahí, empiece a preguntar. Y todavía como que lo estamos testeando. Aparte son datos de desarrollo que no son datos reales. De hecho nos reíamos de que si alguien lee las cosas que recién le preguntamos, como que no están del todo bien y se infartan porque no sé, les importa, no sé, saber esto de cuál es el máximo del mismo, el mínimo de un valor, porque ahí calibran los equipos. Si le está dando así, está recontra mal. Entonces imagínate que para ellos es algo regloso. Así que estuvimos con estos dos usuarios, viste que te contamos que son como más de sistema. Muchas veces los usuarios finales no saben armar las cosas en la tabla dinámica del cubo y los vuelven locos a ellos para que se las arme. Como que ni siquiera saben manejar de todo el Excel con la tabla dinámica que veíamos la otra vez. ¿Como que ellos tienen un historial de preguntas que les suelen hacer y que necesitan los usuarios, y que si esto lo resuelve bien, tapiola, viste? Así que bueno, estuvimos con ellos.

**Lucio Rojas**: Lo que le explicaría a esos usuarios es que para ellos hablar, armar las tablas dinámicas es muy similar a armar las tablas gold. Ahora son vistas consumo de información. Entonces cuando se armen las cinco tablas Gold que responden al 80% de las consultas, van a tener la vida bastante resuelta. Después van a tener preguntas que son por afuera de ese grupo, y tener dos opciones, solucionarla, que el mismo club te lo resuelve, o hace la cuella de la silver, que es lo que viene haciendo hasta ahora. ¿Tienen tablas volteadas? ¿Le están preguntando las tablas del warehouse o te sugiere crear alguna nueva Gol para eso?

**Schmidt, Nicole**: Sí, sí, re. No, de hecho bueno, como que le estamos tirando así como preguntas generales que ellos han usado y el mismo Claude nos va resolviendo ahí al toque digamos. Nos dimos cuenta que nos faltaban tablas en base a que nos dijo Claude y nos dimos cuenta que estaban esta mal en estas relaciones en base ahí, obvio que a futuro lo ideal sería que ya esté todo más o menos mapeado y que estén estas tablas gold, pero nos simplifica mucho más preguntarle directo y ver qué pasa, así que estamos por ese primer paso ahora después cuando empecemos ya a armar bien, pero bueno, nos dimos cuenta que nos faltaban un montón de cosas, así que cuando lo tengamos y obvio el próximo paso ya sería la semana que viene como tarea tener una tabla gol sí o sí.

**Lucio Rojas**: De nuestro lado o de mi lado lo llevo yo ser obsesión con eso de los tiempos, me dicen mira, esta semana no pudimos hacer nada, vamos a tener que estudiar un poquito más la prueba de concepto, no pasa nada, me interesa más saber hasta ahora cómo lo vieron o los usuarios, ustedes, el nivel de respuestas y si mejora lo que tenían, si no mejora por lo poquito que vieron o por ahí no pueden decir no, todavía la verdad no te

**Schmidt, Nicole**: podemos responder y como que está medio verde me parece porque como nos faltan todas esas cosas a mí posta me preocupa el tema de la carga esta que justo ayer te decía al principio, después cuando lo conectemos a producción, o sea, quiero esas cosas como que no sé bien a nivel tiempos, procesamiento, viste, como que por ahí son los miedos que tenemos de los traumas que ya sufrimos acá, que después tarda mucho y eso, pero sí, está piola, o sea, va más rápido que por ahí lo que teníamos antes en sí en resolución de cosas me parece, pero todavía no superó lo que teníamos porque faltan esas relaciones, faltan esas tablas, o sea, esa mi sensación, pero bueno, todavía no lo usamos tanto tampoco. Yo recién lo pude empezar a usar el jueves, después del jueves fue el viernes y hoy.

**Lucio Rojas**: Claro, sí, eso de Almel era muy gracioso, tenía un problema con las case, te normalizaba toda minúscula el compartir el mail y tenías la s con mayúscula en duelo. Después lo de producción, te tienen columnas para ser incremental, No me acuerdo si me habían dicho la actualización o habría que hacer.

**Schmidt, Nicole**: Sí, bueno, es la que tenemos que terminar de averiguar. Eso lo tenemos que sentar a pensarlo con AYE, porque tenemos eso, pero. Pero hay algunas cosas, como un proceso que se mensualmente que borra todo y vuelve a cargar todo de vuelta, que no sé cómo se comportaría ahí en

**Lucio Rojas**: ese caso lo haces una vez al mes y el resto del mes lo manejas con incremental para la carga no te lleve tanto tiempo.

**Schmidt, Nicole**: Estaría re piola que no repliquemos eso porque lo odio. Imagínate que nosotros con AYE una vez al mes tenemos miedo de dormir esa noche que se borra todo y se vuelve a cargar todo, porque ha pasado

**Romano Bazán, Ayelen**: que se borra todo y no vuelve a cargar, entonces es un problema. Y ahí si carga todo, tarda el mismo tiempo, o sea, es proporcional al tiempo que está cargando ahora la primera carga podría ser menos.

**Lucio Rojas**: No, es proporcional, o sea, no es que si dos tablas te cargan tres horas, 20 tablas te tardan 30.

**Romano Bazán, Ayelen**: Claro, no, eso, pero digo, por ejemplo, ahora yo cargué. Me tardó tres horas en cargar esas tablas, si yo no sé, mañana las actu. ¿Actualizo, me va a tardar tres horas de vuelta?

**Lucio Rojas**: No, creo que no. Eso también yo voy a preguntar, porque hasta ahora con los que hacemos incremental seguro que no, porque le cargamos nada más que las novedades y al actualizar las todas las tablas todos los días, no sé si te vuelve a interpretar todos los esquemas y demás o solamente vuelve a refrescar los datos. Eso tengo que preguntar. Si es la segunda opción, tarda menos, si tiene que volver a hacer el mismo proceso, va a tardar lo mismo. Ahora le pregunto al chico, porque ahí

**Romano Bazán, Ayelen**: si no nos daría el tiempo, o sea, el rango de tiempo para actualizarlo diariamente no nos daría.

**Lucio Rojas**: Y si lo podemos acordar ponerle a las 12 de la noche.

**Romano Bazán, Ayelen**: No, es que a las 12 de la noche empieza a correr nuestro proceso, que es el que actualiza las tablas. Está terminando 4 de la mañana, 4 y media.

**Lucio Rojas**: Sí, más o menos 4 y media. Y si ponemos este a las 5, terminaría en teoría a las 8. ¿Y a cuál arrancan a trabajar? ¿A las 8? A las 7.

**Schmidt, Nicole**: A las 7 arranca 7 o a

**Romano Bazán, Ayelen**: veces a las 6 si arranca el laboratorio antes. Pero igual estaríamos como muy jugados, porque el otro proceso también en algunos casos falla y nosotros tenemos que reprocesar. Entonces por eso es que también tenemos esos rangos de tiempo, por las dudas de que haya alguna falla a nuestro lado.

**Lucio Rojas**: Sí, pero esta tabla, la que ustedes ya tienen cargada, no la he visto que esté desactualizada por mucho tiempo o un proceso mucho tiempo. Bueno, voy a decir una cosa, no les quiero inventar la respuesta, se las paso ahora, lo llamo, cortamos con ustedes, lo llamo a la persona, al de OPS que está con todo esto y le pregunto y se los pongo en email.

**Romano Bazán, Ayelen**: Vale, perfecto. Y después la otra pregunta es, dentro de la conexión nosotros elegimos un determinado lista de tablas que se cargaron, pero hay más tablas. Ahora nosotros haciéndole preguntas, en un momento quería ir a buscar datos a tablas que nosotros no habíamos cargado, que fueron estas que ahora nos dimos cuenta que había que cargarlas, pero sólo el sistema, o sea desde cloud nos respondió como qué tablas deberíamos cargar. Nos dijo por ejemplo, ahí tienen datos, no sé, la de un ensayo que nosotros no la habíamos cargado. Ahí la consulta es el conector tiene acceso a otras tablas que nosotros no hayamos cargado.

**Lucio Rojas**: Eso como que sabe que de la existencia de las tablas que no están seleccionadas cuando vos conectaste la fuente, no las tiene, no tiene los datos, pero sabe la existencia porque les ha mapeado, no va a poder consultarla ni. Ni tomar esa información. Pero sabe la existencia, por eso te propone cargarlas.

**Romano Bazán, Ayelen**: Claro, pero cómo sabe, o sea, tiene como la estructura o tiene alguna de esa tabla.

**Lucio Rojas**: Debe tener la estructura o debe tener Cuando cargaste el esquema de base de datos debió haber tomado el nombre de la tabla y es una descripción. Pero buenísima tu pregunta,

**Romano Bazán, Ayelen**: porque nuestro problema es que después ahí nosotros tenemos otras tablas, por ejemplo ahora estamos con el laboratorio, pero hay tablas, no sé, de contratos o de otras áreas o de facturación que todas estas personas no deberían ver, entonces por seguridad también es bueno. ¿Hasta dónde llega el conector a ver tablas que nosotros no le cargamos bien los datos?

**Lucio Rojas**: Seguramente, seguro que no, no va a poder hacer, no a traer los filas ni poder consultarlas. Para mí sabe de la existencia nada más porque está dentro de la fuente.

**Schmidt, Nicole**: Sí, por ahí no sabíamos si tiene que ver algo de la estructura,

**Lucio Rojas**: la

**Schmidt, Nicole**: foránea o algo de eso. ¿Viste de la tabla que ya cargamos como para resolver sí digamos, llega a ver las tablas solamente porque sabe que existe una foránea a esa tabla dentro de la tabla que ya cargamos o puede ver todas las tablas libremente? Como que sería por ahí la pregunta,

**Lucio Rojas**: seguro que no saber todas las información y las filas, no sé si por la foraña o es porque cuando cargó el esquema de la fuente vio que había una tabla con ciertos campos, por ejemplo. Eso de vuelta se los voy a copiar en el mail porque lo sabe bien el chico que sabe cómo funciona el auto ETL, pero está bien la consulta, no sé qué decirle.

**Schmidt, Nicole**: Sí, tranca, tranca, parate. Y yo iba. Ah, también creo que llega a ver lo que yo estaba buscando era otra cosa que le preguntamos de cuándo había sido la última vez que se actualizó la información y como que llega a ver un poco más allá, como tipo el job que ejecutó las. ¿Estoy buscando la pregunta y que me respondió? ¿Porque no me acuerdo, pero como que me dijo que se había ejecutado el ETL en tal fecha, ponele, Sí? Y me puso acá, me puso, yo le puse ¿Sabes cuándo fue la última actualización de las tablas de la base de datos? Y me puso la fecha, me dice corresponde un proceso de tipo setup del ETL Y bueno dice última actualización, estado, no sé, o sea dice antes de esa hubo otra actualización exitosa, como que tiene esos datos. Ahora me gustaría preguntar qué consulta SQL ejecutó sobre eso, como para saber, a lo mejor con todas esas cosas le podemos tirar, che, ¿Qué consulta de SQL generaste para decirme esto? Para saber qué está mirando, digamos, no

**Lucio Rojas**: lo llevamos probable, todo se puede ver adentro de las solicitudes.

**Schmidt, Nicole**: Acá lo estoy abriendo. A ver si descomparon.

**Lucio Rojas**: Estoy viendo.

**Schmidt, Nicole**: Claro, porque ve todo esto que hizo está bueno para también nosotros empezar a preguntarle cómo se comportan los datos cuando se ejecutan los procesos. Esto de que elimina todo, O sea, esto es query, No me tira como la consulta SQL en sí me tiraba esto que no sé qué es. Data status access o es la ejecución dentro de Teramot, ahora que lo pienso, que será que cargamos los datos en Teramot o no sé, puede ser por

**Romano Bazán, Ayelen**: la fecha,

**Schmidt, Nicole**: bueno, tendríamos que terminar de ver, pero

**Romano Bazán, Ayelen**: por el 20 de mayo tiene sentido que sean. Tengo.

**Schmidt, Nicole**: Claro. Si, puede ser, no sé, Proceso de tipo setup, Sí, Que sea. Bueno, acá no fue como al SQL ahora que lo veo, o sea, como que está dentro de Terabot para mí Workpace Name es como esto. Me parece que lo mete, está ahí adentro.

**Lucio Rojas**: Ahí tiene la actualización. Se acabó de programar todos los días a las 7 de la mañana.

**Schmidt, Nicole**: Claro, acá se puede ver eso. Acá actualización, está

**Lucio Rojas**: eso ahí.

**Schmidt, Nicole**: Sí yo entro así, me aparece esto.

**Lucio Rojas**: UTC-3, es el de Argentina. Y ahora capaz lo puede poner un poco antes. A las 5. A las 6 si querés, porque entran a las 6. 5.

**Schmidt, Nicole**: Sí, a las 6 ponele. A ver qué onda. Igual esto como todavía de prueba no hay nadie acá, pero. OK. Y nosotros ahí, eso que vamos a hacer, o sea, acá va a aparecer cuando se sincronizó y no, la sincronización

**Lucio Rojas**: es cuando vuelve a tomar el esquema de las tablas y ve si hay alguna modificación con alguna columna. La actualización no te la muestra desde ahí.

**Schmidt, Nicole**: Ah, OK. ¿Y la puedo ver todos los días?

**Lucio Rojas**: En teoría. No, desde acá no se puede ver. En teoría está todos los días a las seis de la mañana.

**Schmidt, Nicole**: OK, pero sabemos cuánto, si ya corrió. Si, está bien. Eso no es como.

**Lucio Rojas**: Eso lo sabemos nosotros. Yo en particular.

**Schmidt, Nicole**: Sí. Claro. ¿Por qué?

**Lucio Rojas**: Creo que para directamente al de Box.

**Schmidt, Nicole**: OK. No, bueno, porque ahí también como estamos conectados a desarrollo, tampoco estamos cambiando la info siempre. Es solamente cuando ejecutamos el proceso DTL y volvemos a querer los datos, entonces no vamos a ver muchos cambios, a menos que programemos una actualización y tampoco va a haber, no sé ahora la actualización, que sería que vuelva a cargar todo porque no está hecho con nada incremental, sería.

**Lucio Rojas**: Bien, eso es lo que no sé responder. Si lo actualiza, si elimina la fuente y la vuelve a cargar, o si ya con el mismo esquema y ya con todo el proceso de descubrimiento de las tablas listo, que es lo que más suele tardar, hace un refresh de los datos, ¿Cuánto tarda eso? Si vuelve a tardar tres horas o si tarda menos. Esa respuesta se las mando.

**Schmidt, Nicole**: Bueno, bueno, en realidad si quieren ya sí.

**Lucio Rojas**: Yo acá tengo a mi amigo Recorder y ahora me llevo las preguntas bien que me hicieron y se las devuelvo listadas, así no queda nada. De última, si ven eso y todavía les quedó algo pendiente, me reescriben con eso. Ahora apenas termino, espero que me llegue el resumen y lo respondo.

**Romano Bazán, Ayelen**: Perfecto. Bueno, ahí luce. ¿Te hago otra consulta con respecto al otro tema al que estábamos viendo con DJ, al otro proyecto ahí que habíamos quedado una reunión para este jueves, puede ser?

**Lucio Rojas**: Sí, la tenemos que agendar.

**Romano Bazán, Ayelen**: Si, ahí no sé si vos la enviabas o en qué habían quedado.

**Lucio Rojas**: ¿Cuándo fue la reunión pasada? Fue el miércoles,

**Romano Bazán, Ayelen**: No, el jueves, había sido el jueves a las 9 y habíamos quedado de hacerla que quede fija, jueves 9 y media.

**Lucio Rojas**: ¿Qué área de anchos?

**Romano Bazán, Ayelen**: Área d, dirección de estudios económicos.

**Lucio Rojas**: ¿Sí, d? ¿Vos los seguís a ellos como un soporte de sistema?

**Romano Bazán, Ayelen**: Sí, en realidad me agregaron ahí más que nada como nosotros ya estuvimos trabajando y algunas cosas ya vimos para hacer un seguimiento.

**Lucio Rojas**: Caíste como te agrego las reuniones o.

**Romano Bazán, Ayelen**: Si, agrégame y.

**Lucio Rojas**: Nueve, diez y media,

**Romano Bazán, Ayelen**: Yo después tengo que agregar a otras. Otros chicos me pidieron que los agregue, pero bueno, ahora después les reenvío, sino la cita.

**Lucio Rojas**: Bueno, Habíamos quedado que yo. Iban a preparar los Excel para cargar. Sí, bueno, esa reunión va a ser media, vamos a ir con los Excel, ponerlo a cargar y esperar 40 minutos que carguen, no lo haría en vivo, si ya los tienen antes y vos querés ayudar a cargarlos, estaría buenísimo y si no nos conectamos sabiendo que es a eso, cargarlo de Excel y después nos volvemos a conectar la semana que viene o revisar lo que. Podemos revisar lo que hicieron, podemos estirarlo un poco, la herramienta va a tardar un tiempo en cargarse

**Romano Bazán, Ayelen**: y ahí lo que yo no sé ellos a dónde lo van a cargar, o sea van a tener otro proyecto,

**Lucio Rojas**: no sé cómo

**Romano Bazán, Ayelen**: lo están manejando, No sé la verdad. ¿Y que hicieron? Y después ellos ahí tienen la idea. Pero es más que nada por lo que también le dijo Bruno que en media hora iban a cargar todo, claramente va a ser imposible.

**Lucio Rojas**: ¿Que les dijo puntualmente?

**Romano Bazán, Ayelen**: ¿No, como que en las reuniones ellos, viste que dicen siempre el otro Gabriel creo que también le dijo el otro día como no, en media hora agarran todos los Excel, No va a pasar eso para mí van a empezar y van a tener errores y pruebas y van a ir, volver y así, obviamente

**Lucio Rojas**: Gabriel 1 te va a decir el ideal, después qué va a pasar? Va a quedar un Excel, el 50% de los Excel va a tener una columna, un acento y te van a romper ahí vamos a tener que ver por qué rompió, modificar eso, algunos van a tener un símbolo pesos, otros van a tener una fila arriba del encabezado. Te hace mal el trabajo que termino haciendo yo para ayudarlos a que carguen. Pero el tema que por ahí está malísimo que ellos me tengan que pasar a mí los Excel por mail para que yo lo modifique, volver a cargarlos por un tema de compartir datos confidenciales, por así decirlo. Entonces por ahí está más bueno que en una reunión me compartan pantalla y yo los instruyo un poco en cómo tienen que ser esos Excel Y eso ya los corrigen para la próxima.

**Romano Bazán, Ayelen**: Claro, sí, sí. Para mí la idea va a ser esa, van a ver y después ellos los modificarán. Y los datos que en teoría iban a cargar eran todos públicos. Ellos manejan mucha info pública.

**Lucio Rojas**: El caso uso yo creo que ya lo tienen creado. Bueno, si no les crea un caso, hacemos todavía en el momento. Hacemos así, aprovechamos esa reunión para crearle el caso de uso, mostrar la herramienta, ver los Excel para descargarlos y demás.

**Romano Bazán, Ayelen**: OK.

**Lucio Rojas**: Bueno, entonces esto yo como si fuese la reunión al parcial y siempre desapruebo con ustedes, me hacen preguntas, cosas muy puntual. Todas estas respuestas yo las tenía re claras para anterior, la que vimos antes, la nueva, no estoy tan seguro de cómo se comporta. Les podría mentir diciéndole que sí sé, pero después lo van a hacer distinto. Me mintió. Entonces prefiero decirle que no sé y de paso voy aprendiendo yo qué respuestas dar. Así que les respondo en un ratito.

**Schmidt, Nicole**: Bueno, no hay drama. No había drama.

**Lucio Rojas**: Buenísimo. Bueno, entonces dejamos acá y para la próxima tratamos de hacer una Old y ya entendamos un puntenazo.

**Romano Bazán, Ayelen**: Dale, muchas gracias. No entraron solicitudes.
