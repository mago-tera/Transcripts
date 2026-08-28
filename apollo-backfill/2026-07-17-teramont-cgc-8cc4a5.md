# Teramont/CGC

**Fecha:** 2026-07-17T13:01:16.639+00:00  
**Duración:** ~35 min  
**Participantes:** Arito, Joaquin <joaquin_arito@cgc.com.ar>, Garcia, Patricio <patricio_garcia@cgc.com.ar>, Aldabe, Sebastian Alberto [TEKNE] <>, Agustin Garcia <agustin.garcia@teramot.com>, Rodriguez, Magdalena <magdalena_rodriguez@cgc.com.ar>, Valentin Torassa Colombero <valentin@teramot.com>, Costas, Miguel <miguel_costas@cgc.com.ar>, Unknown_participant_1100 <>, Dominguez, Christian Julián <christian_dominguez@cgc.com.ar>, Facundo Vivas <facundo@teramot.com>  
**Externos:** joaquin_arito@cgc.com.ar, patricio_garcia@cgc.com.ar, magdalena_rodriguez@cgc.com.ar, miguel_costas@cgc.com.ar, christian_dominguez@cgc.com.ar  
**Apollo ID:** 6a5a3000ddf013000c8cc4a5

---

**Agustin Garcia**: Bien ustedes, Me alegro. Este viernes previo a una final,

**Valentin Torassa Colombero**: No

**Agustin Garcia**: sé si ustedes me pueden ver.

**Dominguez, Christian Julián**: Perfecto.

**Agustin Garcia**: No sé qué pasa,

**Rodriguez, Magdalena**: me trae muchos problemas.

**Agustin Garcia**: Salgo un minuto y vuelvo a entrar.

**Dominguez, Christian Julián**: De nuestro lado. Male, ya estamos completos, ya está Pato acá.

**Rodriguez, Magdalena**: Bueno, buen día. ¿Cómo andan?

**Valentin Torassa Colombero**: Bien, bien.

**Rodriguez, Magdalena**: Ahí vamos. Falta Agustín, me parece, ¿No? ¿Que dijo?

**Valentin Torassa Colombero**: Sí, sí, se está reiniciando la. Supongo que la conexión ahí cuando se sube. Le dejamos ahí que arranque.

**Agustin Garcia**: Ahora sí.

**Rodriguez, Magdalena**: Bueno, ¿Estamos todos? ¿Agus por nuestro lado?

**Agustin Garcia**: Sí, estamos todos. ¿Lucio está por ahí?

**Valentin Torassa Colombero**: Sí. ¿Estamos los chicos?

**Agustin Garcia**: Sí, estamos todos.

**Dominguez, Christian Julián**: Podemos empezar.

**Rodriguez, Magdalena**: Bueno, buenísimo. Bueno, ¿Cómo andan todos? Antes que nada, muchas gracias por tomarse un ratito para la reunión. Yo tengo Astimedia, Agus, tengo lamentablemente otro compromiso, pero bueno, estoy cuando estoy, después me bajo la idea un poco de. Bueno, gracias. La idea de la reunión es que estemos un poco todos para entender mejor el caso de USO. Fueron pensando con theramont, esto es una iniciativa de aislamiento que vino por el lado del negocio. Lo hablaron creo que Fede Salvia con Bruno. Y bueno, ahí después obviamente nos llegó este requerimiento a nosotros de Haití, como te decía, sin mucha definición de qué necesitan o qué les tenemos que disponer para apoyarlos. Entonces la idea era juntarnos y empezar a entender un poco más qué necesitan y ver las opciones factibles para poder realizar esto que planning está pidiendo. De nuestro lado estamos de data, somos yo y Seba por la parte de data de CGC, Después están Joaquín y Miguel por la parte de infraestructura. Y Cris y Pato son la parte de SAP. Así que bueno. Y lo último que digo, vieron que puse ahí en la descripción, Fede un poco dijo. Me dio una idea de qué es lo que necesitaba de esta POC, así tipo, te lo resumo así nomás. Era tener bien claro el cash flow a corto, necesitaba trabajar con esos datos. Así que como el punto principal de todo esto me parece que es como integrarnos con SAC. No sé si ustedes chicos, Miguel o Cris o Paco, tienen otra opinión.

**Agustin Garcia**: Buenísimo. No sé, hay chicos, Me parece que Joaquín quería decir algo, ¿No?

**Valentin Torassa Colombero**: El primer punto a discutir antes de avanzar con los otros temas es ver qué opciones hay para resolver y si se puede resolver el tema de tomar los datos de SAP. Si quieren veamos eso primero y después que es el principal tema a resolver.

**Agustin Garcia**: Buenísimo, Yo previo quisiera hacer una breve introducción para ver si estamos todos alineados con respecto a cómo funciona la solución. No sé si conocen cómo es el esquema técnico de nuestra solución. La puedo explicar en dos minutos.

**Rodriguez, Magdalena**: Dale, Contorno, estaría buenísimo.

**Agustin Garcia**: Buenísimo. Básicamente nosotros lo que hacemos, Theramot lo que arma es un Data Lake con un esquema Medallion, donde ingestamos la información de ustedes de los distintos sistemas y eso nos permite armar este Data Lake que luego es el que explotamos con inteligencia artificial. Entonces, para avanzar técnicamente, lo que tenemos que definir es esa integración entre los sistemas de ustedes con Theramo. La información de los sistemas ustedes, digamos, no se toca. ¿Cómo, cómo?

**Rodriguez, Magdalena**: No, no, sí, sí, tal cual, es lo que estábamos diciendo. Estamos en la misma página.

**Agustin Garcia**: Buenísimo. Más que nada como para que estemos todos, digo, sé porque a veces hay restricciones contractuales con respecto a pegarle a ciertas, digamos, entidades en SAT. Y esto es básicamente mover la información para poder explotarla ahí. Entonces, dicho esto, Sí, cómo no, ahí

**Valentin Torassa Colombero**: hay un tema importante que decías. Tenemos algunos sistemas.

**Dominguez, Christian Julián**: Se te escucha muy mal, Joaco, como si no tuvieras micrófono.

**Valentin Torassa Colombero**: Ahí. Me escucha

**Agustin Garcia**: mucho abajito.

**Facundo Vivas**: Es como si tuviesen unos auriculares conectados.

**Valentin Torassa Colombero**: No, Ahí sí, de lo que comentaba recién Agustín, hay algún sistema que tenemos que contactar. Pero después lo que yo te quería apuntar es, una vez que arman el Data Lake, ¿Cómo se conectan diferentes herramientas?

**Agustin Garcia**: Buena pregunta. Digamos, ahí el Data Lake que nosotros armamos, obviamente que tiene todo un esquema de usuarios, perfiles, cada uno de los usuarios también tiene una conexión MCP que permite la conexión al LLM que se utilice, que puede ser Cloud, ChatGPT. Entonces digamos que ahí tenés la conexión vía MCP. Sí, Pato.

**Garcia, Patricio**: Sí, Agustín. A ver, vos estás hablando de que extraes los datos y los pones un Data Lake, me parece perfecto. Y los explotás, que eso es lo correcto. A mí lo que me preocupa es cómo vos sacás los datos de SAP.

**Agustin Garcia**: Perfecto, digamos, ahí tenemos que establecer una conexión para poder hacer la ingesta. Y después esa ingesta se configura una recurrencia que básicamente lo que permite es ir actualizando los datos para tener, digamos, la data fresca también en el Data Lake de Theramot.

**Garcia, Patricio**: OK. Vos me decís que después obtenés un Delta, pero Y hay una carga inicial.

**Dominguez, Christian Julián**: Entendí muy ¿Se obtiene un delta o se hace un refresh de todo?

**Valentin Torassa Colombero**: Ahí depende, perdón, nos metemos. Depende de cómo esté configurada su base de datos y su base de datos soporte, incrementalidad. Nosotros tendemos a ir a hacer un Delta en vez de hacer un refresh completo. Se puede configurar eso.

**Aldabe, Sebastian Alberto [TEKNE]**: Yo tengo una consulta. Nosotros desde el lado del equipo de datos también tenemos un Lake House montado en Databricks con la misma arquitectura Medallion, que va desde Landing, Ronce, Silver y Gold. Y ahí nosotros sí tenemos 100% jurisdicción, tenemos gobernanza, tenemos todos los procesos, tenemos estándares tanto de calidad en las distintas capas. En vez de que ustedes le peguen directamente a SAP, porque nosotros ya estamos traqueando orígenes como SAP, como también otros. Si nosotros con databricks creamos una capa intermedia por medio del test y ustedes consumen esa data que aseguramos que tenga calidad y que sea igual que como saldría del origen, sería lo mismo. Un poco para resguardarnos nosotros y tener esa auditoría de qué sale, qué no. En vez de que vayan directamente al surs Igual.

**Rodriguez, Magdalena**: Perdón, perdón. Antes de que contesten. Gracias, Seba. Lo único que quiero aclarar que esto que dice Seba es tal cual así y tomamos la información de diferentes orígenes, pero con SAP no es tan así. Nosotros la verdad que no tenemos tantos datos de SAP, los consumimos vía CDs tampoco. Viste Cris que hemos charlado, las CDs muchas veces no reflejan la transacción, o sea, no es tan así. Así que ahí no la veo tan factible por el tema de los datos. Por eso creo que para mí lo que tenemos que charlar, ustedes dicen, bueno, lo que nosotros hacemos, te lo resumo así nomás, es armar un Data Lake y después consumen, se consume de ahí. Buenísimo. ¿Cómo van a armar ese Data Lake con los datos de SAP como origen? Parece que esa es la gran pregunta,

**Garcia, Patricio**: Male. Vuelvo a retomar el tema. Acá es fundamental cómo es que vamos a extraer los datos de SAP y qué es lo que vamos a llevar. Y después la recurrencia. Obviamente los datos no pueden ser explotados desde SAP, tienen que estar en un intermedio por cuestiones de performance, etc. Pero también adicionalmente de cómo sacar, no podemos usar CDs porque las CDs no están pensadas para eso, pero también yo no sé si le llegó a Agustín un documento de SAP acerca de las políticas, acerca de las restricciones que tenemos. Por eso ahí estoy apuntando ese lado, que me expliquen o que nos expliquen con más detalle cómo traen en forma masiva estos datos sin afectar los compromisos que tenemos nosotros con SAP y sin afectar nuestra performance. OK,

**Agustin Garcia**: perfecto, perfecto. Ahí Lucho, no sé si querés tomar la palabra

**Valentin Torassa Colombero**: ahí creo que tengo que pasarlo más para el lado de, supongo que de Facu, que está sistema de conexión con SAP y demás, cómo son los conectores o cómo lo pensamos hacer. Y si, vimos el documento, no lo dimos todavía tan al detalle, pero podemos dar nuestro estándar de SAP con tal como nosotros nos conectamos a SAR y después de última van diciendo qué restricciones tendríamos que tener en cuenta y lo vamos.

**Dominguez, Christian Julián**: Es importante aclarar que nosotros no lo tenemos SAP on premise, no es que nuestro SAP está on premise y que está en servidores nuestros y demás, sino que está en un modo RISE, donde SAP tiene responsabilidad por la disponibilidad de nuestros sistemas, con lo cual te aplican ciertas restricciones y demás para poder garantizar esa disponibilidad que tienen por contrato con nosotros. Entonces un poco el documento habla sobre las restricciones que hay para hacer extracciones masivas usando por ejemplo, o APIs públicas o APIs privadas y demás, y una serie de cuestiones con respecto a eso. Eso me parece es un punto, como dice Pato, a resolver y creo alguien decía si se puede configurar la base, cuando estábamos hablando si se extraía el Delta o todo cada vez. Si se puede configurar la base, las configuraciones de las bases y demás en nuestro entorno también las hace SAP. No es que nosotros entramos a la base de datos, cambiamos los parámetros y seguimos funcionando. Así que ese me parece un punto ahí para para revisar.

**Garcia, Patricio**: Adicionalmente Cris, la parte, la forma que SAP te sugiere cuando queremos hacer este tipo de exportación masiva es utilizar algo que nosotros no tenemos, que es la SLT, ese modelo SLDT, que es un componente que nos permite tomar los datos de SAP, hacer si hace falta alguna transformación en el medio y guardarlos en una base de datos HANA en un costado, para que después ustedes lo explican.

**Dominguez, Christian Julián**: OK, eso es como

**Garcia, Patricio**: Sí, sí, me estoy yendo para ese lado Cris,

**Valentin Torassa Colombero**: que

**Garcia, Patricio**: eso no lo tenemos licenciado, pero de nuevo, nosotros cualquier intención de extraer en forma masiva datos de CAP, va a saltar esto en RISE, en el monitoreo RISE y van a cortar esos accesos. ¿Está bien? Es decir, va a ser automático, va a ocurrir eso porque los tipos, como vos dijiste, nosotros, ellos tienen un SLA que tiene que cumplir, se va esto, vamos a afectar la performance y vamos a tener algún tipo de inconveniente. Por eso hay que ser muy cuidadoso Agustín con esto.

**Agustin Garcia**: Perfecto. Y digamos que ese módulo, perdóname, vos me dijiste que se llama SLT.

**Garcia, Patricio**: SLT System Lang Transformation. Es lo clásico que se tenía antes, que se usaba en el mundo de Business warehouse. Es decir, es un componente que vos lo pones y el tipo chupa datos de HANA a medida que se van actualizando los datos, le hace. Se hace falta alguna transformación, Vos te chupas determinadas tablas y te las tira en otra base de datos. Pero ojo, eso implica tener otra base de datos en otra punta, en la nube también hay que tener en cuenta toda esa arquitectura. No, Pero es lo que SAP te aconseja de cómo seguir, cuáles son los pasos, que eso I es BDC, que es lo que contaba Cris recién.

**Dominguez, Christian Julián**: Sí. Viste cómo es SAP, que por ahí agrupa varios productos bajo un mismo nombre, lo llama plataforma. Bueno, la plataforma ahora se llama BDC, que tiene varios componentes que vos podés habilitar para justamente compartir información en forma masiva fuera, fuera de SAP. Pero intentando de estudiemos esto, porque esto es crucial. ¿Pero digo, para poder avanzar, porque entiendo, Male, corregime que esto es una POC, por ahí primera instancia, por ahí no se necesita toda la información, o sí?

**Rodriguez, Magdalena**: No, lo que necesita Fede, lo que yo entendí es que los chicos puedan armar este data lake con los datos de cash flow a corto plazo que estén en SAP. Obviamente lo que no está registrado el sistema. No está registrado el sistema.

**Dominguez, Christian Julián**: Pero digo, por ahí con algún entorno. Estoy pensando fuera de la caja, Pato. Suponete que ellos nos dicen estas dos tres tablas que la podemos sacar de algún entorno cercano a producción, que tenemos alguno a una fecha X o de producción, vemos si ellos pueden identificar las dos tres tablas o algo así y con eso armar una poc y después vemos cómo resolvemos esto. Mientras tanto.

**Garcia, Patricio**: Lo tomo, Cris, lo tomo. Pero lo que sería el problema para evitar tranquilos, con SAP, lo que nos tenemos que asegurar es que esos servicios que van a consumir para la extracción sean los servicios que SAP tiene de tal cual dice la API Policy. Mientras sigamos lo que dice la Policy, no va a tener problema. Y lo que tienen que chequear nada más entrar en API Hub, etcétera, y ver si las APIs, tienen las APIs para lo que quieren extraer y ya estamos.

**Agustin Garcia**: Y en ese caso la extracción tendría que ser vía API, no va a

**Garcia, Patricio**: ser a través de servicios.

**Valentin Torassa Colombero**: Sí,

**Agustin Garcia**: también. Hacer una extracción de este tipo vía servicios es una operación pesada, me parece.

**Valentin Torassa Colombero**: Obviamente

**Dominguez, Christian Julián**: no puede quedar por ahí para una solución definitiva. De hecho, Pato, pero corregime porque ahí quizás estoy diciendo algo que no es correcto. Justamente una parte del documento habla de no usar por ahí las APIs para extracciones masivas. ¿Puede ser?

**Garcia, Patricio**: Te dice usar, usar públicas documentadas, que ellos son las que te van a dar soporte.

**Dominguez, Christian Julián**: Sí, pero habla me parece en algún lado de el uso masivo de eso. Como que lo detectan. Ahora lo reviso.

**Garcia, Patricio**: Sí, claro. Sí, sí, claro que lo detectan. Ahí quiere hablar, perdona,

**Agustin Garcia**: Hay un.

**Arito, Joaquin**: No, para hacer más. A ver ahí.

**Agustin Garcia**: Hola.

**Arito, Joaquin**: Hola. Ahí estoy. Creo, para ser un poco más concreto, digo, ¿Ustedes ya tienen resuelto o se han conectado en algún otro tenant o alguna otra plataforma con SAP? Porque creo que va a ser más fácil que nos digan ustedes cómo nos conectamos a SAP de tratar de estar buscándole la vuelta. No sé. Ahí Pato, creo que nombró cosas que todavía ni siquiera tenemos nosotros, ¿Viste? Entonces si no vamos a estar dando medio vueltas y no vamos a poder acelerarlo, ¿No?

**Agustin Garcia**: Sí, ahí chicos, si pueden complementar, yo creo que con. Escuchan, creo que es contra RICE, es la primera vez pública, pero ahí los chicos tienen más detalle.

**Facundo Vivas**: Sí, nosotros lo que tenemos actualmente es dos conectores de SAP. Uno es a través de SAP HANA y el otro es para SAP SC, una solución 1 poco anterior, creo que se considera un poco legacy, incluso estamos hablando tecnología del 2005-2006 por ahí, que bueno, obviamente tenía sentido para uno de nuestros clientes poder hacer la ingesta de datos de esta tecnología. Esos son los dos modelos que nosotros soportamos, que es concretamente hablando de la oferta de SAP. Luego, por supuesto, tenemos un montón de conectores de ingesta de bronce que están pensados, están construidos sobre una infraestructura común para leer datos desde APIs, generalmente APIs REST, por el estilo y automáticamente hacer la estación incremental, revisar todo el catálogo de información, hacer extracción paginada, respetar el throttling. Si el API del otro lado se empieza a quejar de que estamos pidiendo datos demasiado seguido, entonces relajarse un poco y espaciar los pedidos para mantenernos dentro de lo que estipula. Y quizás ese es un camino posible para la situación en la que se encuentren ustedes Ahora. Por supuesto, lo que nosotros tenemos que entender es qué volumen de datos estamos hablando, porque eso condiciona enormemente cuáles son las maneras de encarar esto factibles. Si estamos, si se quiere, volviendo locos buscando una solución extremadamente complicada por menos de un millón de rows, probablemente lo podamos resolucionar con el API sin mucho drama. Ahora, si estamos hablando de un volumen significativo de datos, tanto en ingesta inicial como en la incrementalidad diaria, ahí sí quizás tendríamos que ver opciones más sofisticadas donde seguramente tengamos que hacer desarrollo y un poco de investigación a nuestro lado.

**Dominguez, Christian Julián**: ¿Cómo era tu nombre? Perdóname, no te escuché. Federico. La verdad que no somos una empresa con gran volumen de transacciones por el tipo de industria que tenemos. No sé cuáles son los otros clientes que ustedes tienen, pero nosotros las facturas que hacemos por mes serán menos de 100, por decirte algo. Ahora, sí tenemos más factura en nuestros proveedores, te podría decir que tenemos algo así como 2900 facturas todos los meses y entre liquidaciones de pago y algunas notas de débito, crédito y demás, tendremos menos de mil. Por eso no somos, viste, un retail que por ahí tiene grandes volúmenes de información. Eso no quiere decir que SAP nos genere gran cantidad de registros, porque vos sabés que una transacción tiene un montón de. Sería interesante por ahí de estas conexiones que ustedes tienen con SAP HANA, porque el modelo de datos por ahí no cambió tanto antes de Hannah, y ahora ustedes ya tienen identificado cuál sería las dos, tres, cuatro, cinco tablas, no sé que tendrían que sacar, o las APIs, mejor dicho, como dice Pato, que tienen que usar para extraer esta información.

**Garcia, Patricio**: Creo que las tablas de su lado,

**Valentin Torassa Colombero**: por ejemplo, que módulo de SAPO depende del caso de uso y quizás tengan que pasar un poco más o no hay mantener esta mute.

**Rodriguez, Magdalena**: No chicos,

**Facundo Vivas**: Te perdimos de vuelta.

**Dominguez, Christian Julián**: Ahí está.

**Rodriguez, Magdalena**: No, decía que tengamos todos claro que el caso de uso que planteó Fede es que quiere tener mucho control sobre el cash flow a corto. Es como a corto plazo. Eso es como bastante sencillo y claro y lo planteó y por eso viste, lo puse también en la descripción de la mita, así vamos sobre algo concreto, después vemos de ampliar y todo, pero ya tenemos algo para agarrar.

**Valentin Torassa Colombero**: ¿Y las tablas de SAP que tienen esa información mapeadas o saben por ejemplo qué tablas pasarnos? Para nosotros puedes trabajar con SAP

**Dominguez, Christian Julián**: para todo lo que es cash flow. Hay dos reportes, digamos, que son las partidas de proveedores y las partidas de clientes. Son reportes estándar de SAP que te da hoy lo pendiente, lo que está hoy pendiente, pero son reportes. Los reportes en SAP no siempre se resuelven de una manera directa. ¿Qué quiere decir? Que muchas veces los reportes tienen código y embebido que no está en una vista de una tabla. Por eso a veces Male o al principio dice de la reunión decía a veces la CDS no trae el dato correcto. Eso es porque en verdad no es una CDS totalmente estándar. Si es una CDS totalmente estándar, te da lo que lo que te muestra la aplicación por pantalla.

**Arito, Joaquin**: Perdón, les quería hacer una consulta. Pues yo me había quedado con la que era lo que me parecía más interesante de lo que habíamos visto acá en las oficinas cuando vinieron de la solución, era que se pudiste que el modelo de SAP es un modelo que nadie conoce, que tiene tablas random con nombre X y demás. Y a mí lo que me había interesado, yo me quedé, era como que ustedes se conectaban a SAP y a través de los datos era como que entendían y podían armar de forma automática el modelo. Y con eso era interesante porque ahí ya dejábamos de pensar a ver qué tablas me tengo que traer o qué datos o qué lógica de negocio le tengo que poner para extraerme los datos. Eso era lo que a mí me había parecido súper interesante, porque digo, bueno, todo lo que quiere consultar la gente plan y no SAP y relacionarlo está resuelto. Pero entiendo que no podemos ir por ese camino.

**Agustin Garcia**: Lo que pasa que para eso tenemos que tener acceso a los datos para que el sistema lo pueda levantar e interpretar. Porque lo que vos decís es correcto, Etéramo tiene la capacidad de interpretar el modelo de datos de SAP para poder identificar cuáles son las entidades que tiene que utilizar para cada cosa. Pero para eso tenemos que poder acceder. Entonces en este escenario y pensando que estamos en el camino una prueba de concepto, que seguramente tengamos que resolver estas cuestiones técnicas de alguna manera. ¿Pero en términos de hacer una prueba de concepto, por ejemplo, existe la posibilidad de tener una descarga o un dump de algunas tablas? Yo no sé si esas tablas ya están en el data lake que ustedes tienen con databricks. Digo, como para buscar una solución intermedia para poder. Ahí me dice Magda que no. Perfecto. ¿Entonces digo, hay alguna posibilidad de, por ejemplo, no sé si ustedes tienen acceso a un backup o algo, como para poder acceder a un set de tablas y poder hacer la prueba concepto y en el medio ir dilucidando cómo resolvemos este tema técnico?

**Garcia, Patricio**: Ahí vamos de nuevo Agustín, De nuevo, yo entiendo que ustedes tienen experiencia en CC, etcétera. CC era on premise, era mucho más manejable, éramos dueños de los datos, hicimos lo que nosotros queríamos. Yo vengo con SAP trabajando hace mucho tiempo y en Sport HANA, la base de datos HANA, ni siquiera el modelo de datos es similar, en muchas cosas distinto. Y también como decía Cristian, en muchas tablas internas donde se procesan datos y después se termina sacando reportes. Acá antes de avanzar una poc, para mí deberíamos bajar la pelota. ¿Qué significa bajar la pelota? Básicamente no tiene sentido armar una poc si no puedo definir cómo voy a sacar los datos, porque la poc la puedo sacar perfecto, te puedo dar los datos a ustedes funka perfecto, pero después esto no puedo extrapolar. Entonces yo lo que diría estudiemos bien el tema RISE, cómo funciona RISE y en base a eso veamos cómo avanzamos. Cristo.

**Dominguez, Christian Julián**: No, no, para mí hay trabajo que tienen que hacer con respecto chicos de leer bien el documento de API Policy y ver cómo investigar, cómo trabajar con RISE. Ese es un punto a futuro. Si lo que se necesita es un BDC y demás y esto resuelve la cosa, bueno, habrá que ver costo, costo beneficio, cuánto sale tener un BDC y demás. Ahora, si ustedes nos dicen, no, mira, con estas dos, tres tablas CDS, les paso el código, es lo que sea que ustedes nos digan, si nosotros podemos evaluar si hay alguna manera de extraer esos datos puntuales para que ustedes intenten de armar esta POC. ¿Si está POC no funciona, por ahí no tiene sentido hacer un BDC e invertido, no? Si la POC funciona, quizás la empresa dice, OK, no sé si la mejor manera o la manera más segura es tener un BDC. Quizás estoy pensando en voz alta, Male, Joaco, epato. Digo por ahí usted con estas tres, cuatro tablas yo te voy a hacer la POC que pidió, que pidió el negocio. OK, la pague satisfactoria. Bueno, veamos qué hacer tenemos que hacer para que esto sea pueda escalar. Hay Malev, la veo también levantando el

**Agustin Garcia**: brazo a esto apuntaba un poco yo, Cris, con lo que preguntaba. ¿Estás en mute, male, Yo no te escucho?

**Aldabe, Sebastian Alberto [TEKNE]**: Sí, yo tampoco y creo que no está escuchando.

**Agustin Garcia**: No te escuchamos,

**Rodriguez, Magdalena**: Perdón. Creo que a lo que apuntaba Pato, que me parece que el punto es válido, que lo que de verdad apunte esta poca, es a poder extraer los datos de SAP y poder trabajar con los datos de SAP. Entonces es como si nosotros nos bypasseamos ese paso. No sé si la veo. Puede ser también, pero me parece raro porque en realidad lo que apuntaba Fede es a eso, a decir, quiero extraer los datos de SAP, ver cómo tengo esos datos en un Data Lake y bueno los interpreto y después sí extraigo

**Agustin Garcia**: valor de esos datos, ¿No está claro eso, Male? El tema es el siguiente.

**Rodriguez, Magdalena**: Sin resolver eso, no entiendo qué estamos probando. Entendésme, me pierdo en esa.

**Agustin Garcia**: Claro, pero pará, hay un tema que es no menor, digamos, nosotros tenemos que hacer una prueba de concepto funcional para mostrarle al negocio el valor que aplica la herramienta. Ahora en el medio sí hay que resolver estos temas técnicos, que es parte digamos, del desafío. Ahora, como decía también Cris, digo, tal vez hacemos todo el trabajo de la integración de datos y después la prueba concepto no avanza el trabajo es la integración de datos.

**Dominguez, Christian Julián**: Hasta donde está bien, pero hago una pregunta, digo, si esto se resuelve con BDC, listo, terminamos la reunión, me llevo yo el trabajo, compro BDC, ponemos no sé, 100, 200, palo verde, no sé, pongo BDS acá, ahora venimos, traemos los datos y no da el resultado, es malo. ¿Y qué decimos después? ¿Devuelvo BDC, me la quedo, la uso para otra cosa? Seguro que lo vamos a poder usar,

**Rodriguez, Magdalena**: pero no sé si esa es una opción, Cris. Bueno, puede ser, no, no sé, no

**Dominguez, Christian Julián**: sé, estoy pensando en voz alta, digo, el problema es RISE y cómo extraer los datos. Eso es un tema que se tiene que llevar para resolver y leer bien el documento y demás. Eso si ustedes no dicen, no, mira, esto necesitamos esta arquitectura y demás, bueno, evaluamos cuál será el costo. Eso para la solución definitiva escalable. No va a haber otra manera de hacerlo que no es a través de los métodos que te, que te establece SAP para hacerlo. Ahora, después está el modelo de Uds. Si puede resolver esa problemática, me parece que. Pero Uds. No tendrían que decir que sacar, cómo sacar, dame estas tres, cuatro cosas y yo con esto puedo armar una poco por ello no te doy lo que vos necesitas para armarla. Entiendo que un modelo ustedes aprende con todos los datos. No sé qué sucede cuando por ahí no tenés todos los datos.

**Agustin Garcia**: Perfecto, perfecto. Mira, yo lo que creo es que tenemos que explorar algunas opciones, por eso yo preguntaba si existe alguna forma de descargar la información como para poder avanzar con la prueba concepto y mientras ir pensando en la posible solución técnica. Bueno, si eso no es una opción, nosotros acercaremos, digamos, nuestra propuesta para poder avanzar con esto. Porque creo que ahí los caminos, no sé, por lo menos yo estoy alineado con vos, Cristian, digo, entiendo que hay un camino con una posible solución que seguramente va a tener un costo que para una prueba de concepto no sé si es una opción. Entonces, dicho eso, nosotros nos llevamos el tema para revisarlo internamente y les hacemos, digamos, ponemos sobre la mesa las distintas propuestas que vemos nosotros viables, o sea, como para que ustedes también después puedan decidir en términos de a ver qué camino nos conviene tomar. ¿Te parece bien?

**Dominguez, Christian Julián**: Por mi parte está perfecto.

**Agustin Garcia**: Buenísimo. Bueno, cualquier cosa, si surge alguna duda de nuestro lado, algún tema, seguramente que tal vez algún tema puntual, les escribimos

**Dominguez, Christian Julián**: como para te llevó el documento de las pólizas.

**Agustin Garcia**: Sí, sí, lo tenemos, lo vimos, pero bueno, también queríamos entender un poco cuáles son las posibilidades. Más allá de eso, ahora entendemos bien dónde está la limitación y por qué. Así que bueno, nada, lo vamos a revisar un poco a nuestro lado y les comentamos y vemos si hace falta hacer otra breve reunión, vemos de coordinar para los próximos días. ¿Les parece?

**Dominguez, Christian Julián**: Dale, dale. Lo que necesites de nuestra parte, avisanos.

**Agustin Garcia**: Buenísimo, buenísimo. Bueno, no sé chicos, si ustedes tienen alguna duda más allá en la oficina o Facu, Algún dato que necesitemos para poder darle una vuelta más nosotros a esto,

**Facundo Vivas**: yo creo que con lo que

**Dominguez, Christian Julián**: nos pasamos podemos arrancar a hacer algo de investigación.

**Agustin Garcia**: Dale, buenísimo.

**Garcia, Patricio**: Ahí Agustín, cualquier duda se contacta con nosotros. Si, no hay problema. Si querés ingeniar una reunión, nos chatean

**Agustin Garcia**: y hablamos, siempre hacemos así. Entonces, les agradecemos mucho el tiempo. Bueno, y buen fin. Ojalá que nos encontremos el domingo en el obelisco.

**Facundo Vivas**: Gracias.
