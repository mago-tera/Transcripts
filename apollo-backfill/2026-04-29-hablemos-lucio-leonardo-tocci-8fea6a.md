# Hablemos !  Lucio  (Leonardo Tocci)

**Fecha:** 2026-04-29T12:00:42.403+00:00  
**Duración:** ~73 min  
**Participantes:** Sabrina Colazzo <>, Leonardo Tocci <letocci@baufest.com>, luis alberto galeazzi <galeazzila@gmail.com>, Veronica Sznek <>, Luciana L <>, Lucio Rojas <lucio@teramot.com>, Gabriel Puertas <gabriel@teramot.com>  
**Externos:** letocci@baufest.com, galeazzila@gmail.com  
**Apollo ID:** 69f2041cb68b9a000d8fea6a

---

**Gabriel Puertas**: Buenas.

**Sabrina Colazzo**: Hola, ¿Qué tal?

**Gabriel Puertas**: ¿Todo bien?

**Gabriel Puertas**: ¿Cómo va?

**Sabrina Colazzo**: ¿Todo bien, ¿Todo tranquilo?

**Gabriel Puertas**: Bueno, me alegro.

**Gabriel Puertas**: Qué sé lucio. Pensé que no me habían abandonado.

**Lucio Rojas**: Buen Día, ¿Cómo andás?

**Gabriel Puertas**: ¿Todo bien? Hola fan, ¿Cómo estás?

**Sabrina Colazzo**: ¿Qué tal? ¿Todo bien, vos?

**Lucio Rojas**: ¿Todo bien? Cero paciencia. Un minuto.

**Gabriel Puertas**: Hola, buen día.

**Sabrina Colazzo**: ¿Qué tal?

**Gabriel Puertas**: ¿Lucio? Por nuestro lado, Juan dijo que empecemos, así que no sé si esperamos a alguien más.

**Gabriel Puertas**: Ahí ya les escribí a las personas que faltan, así que si me dan dos minutos o uno, a ver qué me dicen.

**luis alberto galeazzi**: Buen día.

**Leonardo Tocci**: Hola, buen día. ¿Cómo están? Disculpen, pero no me levantó la cámara, no sé.

**Lucio Rojas**: Cómo va a llenarlo.

**Gabriel Puertas**: ¿Todo bien?

**Leonardo Tocci**: Bien, todo bien.

**luis alberto galeazzi**: Bueno, ¿Cómo vamos a organizar la presentación?

**Gabriel Puertas**: ¿Leonardo?

**luis alberto galeazzi**: ¿Cómo lo tiene pensado?

**Leonardo Tocci**: A ver, particularmente lo que habíamos acordado luego de la charla anterior era buscar un espacio, nos pudiesen mostrar un poco la plataforma. Los chicos me habían pedido algún archivo interno, pero la verdad que hasta este punto todavía no tengo ningún dataset propio que les pudiera compartir. Obviamente no les puedo pasar de cliente, así que. Sí, pero los chicos me habían mencionado que tenían datasets como para mostrarnos funcionalidad de la plataforma. Así que la idea es como que puedan hacer un barrido por ahí, idealmente. Por eso también traje parte de mi equipo técnico para que eventualmente, ante la curiosidad, le hagan muchas preguntas.

**luis alberto galeazzi**: Estamos con los que saben, entonces.

**Leonardo Tocci**: Claro, sí, sí, sí. Yo estoy solamente para atraer a la gente.

**Gabriel Puertas**: Y consulta yo porque no recuerdo. Estamos teniendo muchas reuniones últimamente, no recuerdo haberme juntado alguna vez. ¿Pero ustedes son o trabajan como tipo consultoría?

**Leonardo Tocci**: Nosotros somos una empresa que presta servicios de tecnología en diferentes ámbitos. Data es una de las verticales técnicas que tenemos a la interna de Office. Somos una empresa de desarrollo Con más de 30 años de experiencia, basados en Argentina, pero con operación en en toda Latinoamérica, Estados Unidos y España.

**Gabriel Puertas**: Buenísimo. ¿Y qué tipo de clientes tienen? A ver si elijo en realidad les pregunto, pero ¿Tienen por ejemplo clientes retail?

**Leonardo Tocci**: Tenemos clientes de retail, tenemos clientes de bancas, seguros, tenemos clientes de múltiples industrias Target, El Capuna, por ejemplo. El cliente nuestro es Danone, es Encosud, es Banco Galicia, como en esa liga. Sobre todo en Latinoamérica. En Estados Unidos los clientes son en términos de tamaño, renombre, si querés algo más chicos, pero para lo que es mercado latinoamericano son enormes.

**Gabriel Puertas**: No, no, sin duda son grandes.

**Gabriel Puertas**: Y en términos de la vertical de datos del servicio que ustedes le dan, ¿Qué tipo de servicio le dan?

**Leonardo Tocci**: Nosotros damos desde estrategia, gobierno, plataforma de datos, ingeniería, reportería, analítica, analítica avanzada, IA, cubrimos punto a punto.

**Gabriel Puertas**: Yo pregunto, bueno, obviamente no está bien, pero digo, además como para orientar un poquito la demo, nosotros tenemos clientes que están en esas verticales tipo retail, supermercado y ese tipo de cosas, pero yo no tengo datos anonimizados o sintéticos como para poder mostrarles lo más parecido. Es un caso de uso de una cadena de farmacias que a los fines prácticos termina siendo como un retail sin parcial, unas particularidades de los productos que venden, pero bueno, nada, y ahí yo quería orientar, o sea, yo les pregunté si hacían retail cruzando los dedos, porque en realidad el único set de datos que tengo. Está muy bien, entonces, pero bueno, al menos esa parte estamos bien. Entonces, la idea, yo les cuento muy rápido que Estéramo, qué hace así orientamos la demo. Teramot a los fines prácticos es simplemente una herramienta que les permite, a través de un proveedor de inteligencia artificial que puede ser chatgpt, Cloud, nosotros ahora estamos usando Cloud porque nos parece que es el que mejor funciona, ustedes conectan, o sea, le permiten a Cloud que opere sobre la infraestructura de datos de eventual cliente a través de la plataforma de Theramot, puesto así es como si fuese un conector, pero es mucho más que un conector, porque además permite que esa interacción de datos sea segura y además lo que está haciendo es generando infraestructura de esa solución que ustedes van creando. Entonces, muy rápido, ¿Qué hace Tenamo? Theramo básicamente toma los datos que ustedes ingestan, supongamos que estamos en esta farmacia, que por la duda cuando haga la demo le va a hacer referencia a Medmar, pero digo, es un nombre genérico, toma los datos, pero toma los datos de la base de datos transaccional, o sea, nosotros no necesitamos que haya un warehouse, que haya ninguna capa semántica ni nada por el estilo, o sea, yo le pego, en este caso están en una Postgres, que es la que soporta las transacciones de la cadena de farmacia, o sea, de la cadena de farmacia que tiene varias sucursales y congrega toda esa información, pero nada, es una Postgres, tiene un diseño estrella, tiene dos tablas de hecho y varias dimensiones y nada más. Nosotros levantamos esa base de datos, la levantamos porque hacemos como una copia nuestra infraestructura, para no pegarle directamente a la base de datos, nos parece más seguro. Y además es un servicio de lectura. Y lo que va a pasar a partir de eso es que nosotros armamos como una especie de warehouse, o sea, levantamos los datos en una capa bronce, que son exactamente los mismos datos del transaccional de esta farmacia. Hay un proceso de sanitización de esa base de datos, por sanitización me refiero a normalización de ciertos formatos que haga falta, normalización de columnas categóricas, ese tipo de cosas, que se hace automáticamente. Es como el proceso cuando ustedes reciben una nueva base de datos y empiezan con ese proceso de EDA que seguramente hacen para entender de qué va cada una de las dimensiones, si sirve, si no sirve, cómo está, cómo se interrelacionan, y ese tipo de cosas, valores nulos y todo eso ocurre automáticamente. Y ese proceso de ingeniería de datos, nosotros más o menos lo tenemos medido en la medida que van apareciendo distintos clientes y se cumple en un 80-90% ese pareto, digamos, de cosas que descubro. Eso se hace a través de distintos agentes. Hay agentes que hacen distintas funciones, como, no sé, un detector de nulo, un parseador de fecha, cosas por el estilo. Y eso queda en una capa silver. Ya estoy hablando en nuestra infraestructura, le menciono esto porque en la demo van a aparecer esos términos, cuántas silver tengo y todo eso. Y lo que sigue es pedirle a este LLM que genere cosas, es decir, no sé, quiero hacer un dashboard que monitoree las ventas. Bueno, eso va a terminar siendo una tabla gold que toma información de distinta silver, haciendo joins, haciendo transformaciones, no sé qué. Y esa nueva tabla gold que la generó un LLM que vive en Theramo, se va a actualizar todos los días, le va a quedar hecho como LTL. Entonces nosotros lo vemos esto como una forma de hacer un delivery mucho más rápido, en el caso de ustedes que hacen este tipo de servicio. Así que yo sin más, vamos a ir a la herramienta. Yo lo que les voy a mostrar, voy a actualizar por la duda,

**Leonardo Tocci**: lo

**Gabriel Puertas**: que les voy a mostrar es básicamente nuestra página, que ahí lo único que se hace es la ingesta de datos. Es decir, acá se entra la primera vez, se conectan todas las fuentes de datos. Esto lo estamos cambiando, pero bueno, a los fines prácticos es la misma practicidad. Acá lo que les muestro rápido es acá yo en este ejemplo tengo varias bases de datos, porque eso es algo que yo no les dije, no es

**Gabriel Puertas**: que digamos, si yo quiero, vamos a

**Gabriel Puertas**: agregar una, yo esto lo voy a sacar, ustedes me avisan si alguien me quiere decir algo, porque ese cartel me resulta súper molesto. Yo ahí lo que hago es agregar una fuente de datos. Entonces yo para agregar tengo todos estos sabores, o sea, puedo agregar mysql, Postgres, Oracle, bigquery, Salesforce, lo que haga falta. Y la idea nuestra es ir agregando conectores en la medida que vayan apareciendo casos reales. Si ustedes tienen un cliente que me dice, no sé, estoy conectado ahora, no se me ocurre un ejemplo, pero digo, no sé, Databricks, tengo un cliente que está en data breaks, bueno, nosotros vamos a hacer el conector porque ya nos queda productivizado, se lo pueden agregar. ¿Cuál es la ventaja de esto? Que ustedes, no sé, por ejemplo, si tienen un cliente que tiene el ERP en Postgres, pero el CRM lo tiene en Salesforce, ustedes con Theramo pueden juntar esas dos fuentes de información y después la ven y la pueden vincular y usarla juntas, digamos. Bueno, yo acá esto tengo varias fuentes de datos, no nos vamos a parar mucho en esto, yo lo único que les quiero mostrar es, ustedes retengan algunos nombres, fíjense, tiene DIN branch, que son las sucursales, cuestiones, condiciones comerciales, los clientes, los nombres de las drogas, no sé, por acá van a estar los médicos y todo eso. Acá cuando ustedes conectan esta información, lo que nosotros levantamos inicialmente el esquema de las bases de datos, y acá uno puede decir, no sé, por che, no me parece compartir los nombres de los clientes acá, justo acá no están, pero bueno, supongamos que acá aparece, no sé, el nombre y el DNI de un cliente, uno puede deseleccionarlo y eso no participa en el análisis ni se ingesta por téramo. Acá hay una capa de selección donde uno puede decidir qué información agregar. Una vez que esto corre, que yo les comentaba, yo conecté esto, se copia en una capa bronce y ocurre proceso automático que lo lleva a una silver. Yo lo voy a mostrar muy rápido,

**Lucio Rojas**: Gabo, si querés te piso con un e case, porque se actualizaron todas las tablas.

**Gabriel Puertas**: No, no importa que vos funcione igual, porque, o sea, no va a estar actualizado ayer, no pasa nada creo, siempre hay un demonio en las demos, pero no pasa nada. Yo acá lo que les quería mostrar, recuerden esas tablas que yo tenía antes, que levanté, acá va a empezar a aparecer algo que es súper importante, que se empieza a mostrar lo útil de la herramienta, cada una de estas tablas me empieza a aparecer una capa semántica que me está explicando de qué va la información esa, o sea, acá ustedes me tienen que creer, por eso esto es más importante si conseguíamos un dataset de ustedes, pero nosotros entendemos que eso es difícil por cuestiones de privacidad, pero digo, esto se ingesta y acá ya empiezan a aparecer descripciones que son muy relevantes respecto a lo que los modelos descubrieron que contiene esa información. Esto nos sirve a nosotros porque entendemos de qué va, pero lo más útil es que le va a servir al modelo de inteligencia artificial que finalmente va a consumir esto, que ahora vamos a esa parte. Pero yo básicamente lo que les quiero mostrar es que ahora cada una de las tablas tiene una capa semántica que nada, tiene algunas palabras que yo creo clave, como por ejemplo si se fijan acá dice each row representa unique, drugs, name, record, qué sé yo, este unique es muy importante porque eso es producto de un agente específico que se dedica a verificar si la dimensión tiene un solo valor para cada ID, eso puede ser medio obvio, pero cualquiera que trabajó con datos en una dimensión que eso no pasa cuando yo hago un join, explota todo, entonces yo eso ya lo peiné, ya lo analicé, y si yo al modelo le digo que acá hay una única droga para cada ID, él sabe que puede vincular eso sin que tenga problemas de cardinalidad, ¿No? Y acá me quedo esto como acá yo lo que hice fue theramo levantó los datos, ingestó la información, sanitizó si hubo necesidad, si ustedes ven acá hay por ejemplo esta, lo único que hace esta query es la que va de la capa bronce a la capa silver, lo único que hizo fue traerse los valores distintos, no hay, no hay mucha, no sé si navegamos por acá, quizá encontremos alguna que tenga alguna fecha, no sé si habrá por ejemplo, ejemplo esta, nada que haya hecho algún parseo particular de algún formato o algo por el estilo. Una vez que yo estoy acá, y acá ahora viene lo divertido, por si estaba un poco aburrido. Básicamente lo que yo tengo es solo

**Leonardo Tocci**: una consulta, ¿Esa inferencia de la metadata va a nivel de tabla o llega también hasta nivel de columnas?

**Gabriel Puertas**: A nivel de columna hace sampleo de datos,

**Leonardo Tocci**: es lo que me habías contado la otra vez, por eso, pero como vi la metadata a nivel de tabla

**Gabriel Puertas**: no soy, lo que pasa que, a ver, está buena la pregunta, vamos a tratar de encontrar una si es que hay. A ver, no, perdón, esta no, en algunos casos agrega descripción a las columnas, solo que lo que pasa que como esta tabla es muy sintética, está bien hecha, en el caso no aparecen, pero acá vemos, acá lo que hizo, fíjate, insurance plans, acá lo que vio es que la descripción suele estar dividida en dos partes, la descripción del plan, de seguro esto lo hizo automáticamente, levantó la tabla de planes y se dio cuenta que la descripción, después podemos ver qué datos tenía la descripción, pero no importa, estaba dividida en dos partes, entonces dijo, che acá es importante a la descripción dividirla en dos, entonces me quedo con la primer parte del guión y la segunda parte del guión. Como eso lo hizo él solo, o sea estas dos columnas no están en los datos originales, nada lo aclara y dice che mira esta columna tiene esto y la otra, esta otra cosa, acá lo hizo, y más si me vengo, fíjate que acá la query ya es diferente, acá tiene un split que tiene con el guión, yo que sé. Esto es importante porque nosotros, y creo que para ustedes un valor, nosotros queremos dar plena transparencia de lo que está pasando con los datos. Eventualmente estas queries se pueden editar, o sea si vos decís, che no, mirá no me gusta esto de que me haya separado la columna, lo sacas, o vos decís, mira acá te comiste una sanitización que era, no sé, pasar esto entero, bueno, editá la query y listo, te queda. La idea nuestra es darle a ustedes dos dominio de cómo va ese flujo de datos. Entonces vamos de vuelta, esto ya lo tengo y lo tengo listo para empezar a consumir.

**Leonardo Tocci**: Solo una más de rompepiés nomás. Hay una mezcla entre español e inglés en las descripciones. ¿Eso es porque hereda de cosas o por los tipos?

**Gabriel Puertas**: En realidad eso es más un error mío de configuración, vos cuando lo pones acá decidís un idioma, este idioma te suele venir por defecto con la configuración que tenés del explorador, pero yo hice algunas configuraciones en inglés y otras en español. Simplemente para la persona que lo usa es digamos, todo eso. Para el modelo de lenguaje lo mismo. Pero por cierto, cuestión de. No me quedó prolijo, digamos.

**Leonardo Tocci**: No, no hay problema, no queremos,

**Sabrina Colazzo**: pero por más que esté seteada en inglés, interpreta también en español, es multiplicar

**Gabriel Puertas**: en portugués, lo que sea, porque son modelos de lenguaje, no es magia nuestra. Entonces, el siguiente paso es acá, es conectar a Theramo, a un proveedor de ustedes que ustedes utilicen vía un servidor de MCP para que ese modelo de lenguaje use y opere Teramot. Básicamente yo acá, esto es de una demo de ayer, bueno de un webinar que estoy preparando yo si me vengo acá, espero que esto siga conectado, yo tengo un conector aquí, si me vengo y lo reviso a este conector, básicamente lo que es un conector de MCP, no sé si conocen, yo creo que va a ser el futuro de cómo se van a empezar a mostrar las aplicaciones. Es básicamente, es como si fuese una API, no es muy diferente que una API, pero una API pensada para que lo usen modelo de lenguaje. Es decir, yo le doy un set de tools o herramientas para que el modelo de lenguaje que ustedes usen, yo ahora le estoy proyectando Cloud, tenga capacidad de hacer cosas en Theramo. ¿Qué son esas cosas? Nada. Puede a una tabla Gold que ya está hecha, buscarle entender cuál es la query de SQL, hacer una especie de query para entender qué datos tiene, o hacer un preview, crear nuevas tablas, o incluso borrar nuevas tablas y todo más. Todo esto, nada es. Es estándar, es un servicio que se configura, nosotros vamos agregando nueva funcionalidad en la medida que vemos que hacen falta. ¿Y cómo se usa esto? Yo ya este lo tengo conectado, si me vengo acá, perdón que acá me van a empezar a aparecer cosas. Esto pasa a ser demasiado íntimo mostrar el modelo de lenguaje que uno usa, porque va a aparecer cuando le pregunto qué hago, cuando me dijo tiene fiebre, pero. Y lo que voy a hacer acá es decirle, no sé, por ejemplo, verificá,

**Gabriel Puertas**: verificá si la tool de Theramo está conectada.

**Gabriel Puertas**: Lo que va a hacer está cargando esas tools, se está fijando qué tareas. Funcionando correctamente. Esto es lo que encontré. Conexión activa, era el use case este de Pharmacy que yo les estaba mostrando, y me está diciendo, tengo dos tablas Gol creadas. Yo le voy a decir algo para

**Gabriel Puertas**: que ustedes entiendan, me gustaría que generes un diagrama, las tablas disponibles.

**Gabriel Puertas**: Acá lo que va a hacer, esto lo hago porque ustedes entienden, para que vean que el modelo tiene conciencia de cómo se relacionan las tablas que yo le estoy dando, ofreciendo como disponible. Fíjense, acá lo que tiene es una tool que se llama Gettable Relationship. Si ustedes cliquean, yo digo, tráete de este caso de uso de cada una de las DIM que yo le había mostrado cómo se relacionan. Se trae eso, o sea, este es un servidor que le pega Theramo en ese caso de uso que ustedes tienen configurado y me muestra cómo está relacionada la cosa. No se ve nada, pero perdonen, lo está mostrando pero nada, es, no tiene mucho sentido entrar en detalle alguna de estas. Dos de estas grandes son las tablas de hecho que registras todas las transacciones, el resto son todas dimensiones, fíjense que algunas tienen uno o dos niveles superiores y bueno, nada, tiene identificado cuáles son las keys, cómo se consumen, y estas

**Leonardo Tocci**: las creó automáticamente Gabriel. Estas tablas las crea Teramot en base al análisis que hizo de esa primera barriga cuando vos le pegaste a los orígenes.

**Gabriel Puertas**: Esto es ni más ni menos un reflejo de la base de datos que vos le conectaste y este relacionamiento lo detectó y lo curó el proceso de EDA que vos hiciste. Vos pensá, técnicamente nunca trabajé en una consultora, pero sí trabajé con datos, digo, a mí me cae una nueva base de datos, me aparece, no sé, iba a decir Jumbo, pero ese es en Kosut, no sé, Carrefour, te aparece Carrefour, te dan su base de datos que tiene sus transaccionales, donde están registrados, todo lo que van vendiendo en cada una de las sucursales, una mega Postgres gigante. Bueno, yo me imagino que lo que ustedes hacen es empezar a navegar y entender que es cada una de las tablas que tiene, cómo se relacionan. Acá la idea es, lo conectas a Theramo, eso va a ocurrir automáticamente, se va a levantar una capa semántica, puede ser que en algún momento haya que ajustar algo, no digo que no, pero pasa. ¿En muy pocos casos usted tiene visibilidad de lo que interpretó y lo que hizo y ahora ya tienen esto, entonces ustedes ya es como que caminaron ese proceso de EDA inicial que te toma ingestar y qué sé yo, después cómo usan eso? No sé, vos lo podés presupuestar y ganástelo, porque yo entiendo de hablar con consultora es que cuando vos presupuestás datos es muy difícil entender cuántas horas le va a dedicar, porque vos no sabes que te va a tocar, eso sí lo sufrimos, hemos tenido clientes que tienen un quilombo en su base de datos, que son capas sobre capa de distintos sistemas, que quizá no es tan lindo como esto, pero bueno, nada, esto lo que te hace ayudarte a caminar mucho esa parte, fíjate, tiene 25 tablas, ya la organicé y acá es donde uno le empieza a pedir perdón Gabriel que

**Sabrina Colazzo**: te interrumpa el diálogo y no me quedó Claro, o sea ese der lo hace a partir de las tablas que están en silver, que viene de Theramo,

**Gabriel Puertas**: digamos, Sí está conectado, vamos a decir una cosa,

**Leonardo Tocci**: solo la ingesta inicial los deja en bronce, o sea ese primer, cuando vos conectaste tablas, ahí es donde

**Gabriel Puertas**: vos le compartiste los datos, Le compartiste

**Leonardo Tocci**: los datos, eso es lo que hace, como nos mostraste los SQL, tomo y tiro, tiro en un lugar que en definitiva es esa capa bronce, más allá del análisis de metadata y demás, lo que hiciste fue, tenías 20 tablas de origen, esas 20 tablas de origen las pasas así como están a bronce. Después hay un proceso adicional que haga Theramo que te deje ya definida esta capa silver a la que le estás pegando para preguntar esto, Creo que esa era la pieza que nos faltaba.

**Gabriel Puertas**: Hay un proceso automático que lleva cada una de las tablas analizando tabla, tabla, columna, columna tipo dato que tiene y te la deja en silver, vamos a decir curada, curada en el sentido normalizada y ya sanitizada, hay procesos de detección, de outlier, todo ese tipo de cosas, pero bueno, no importa, eso es cuestión de probarlo. Y además sobre esa capa silver yo levanté una capa semántica, se armó automáticamente, que es súper importante porque vamos a suponer qué tipo, no sé si les puedo preguntar esto, de última inventenme o mientras me o díganme que no me lo pueden contestar, pero ¿Qué tipo de análisis de reportería le hicieron a Sencosud o Prá? Vamos a cambiar la pregunta, ¿Qué tipo de análisis de reportería le harían a un cliente nuevo, que sea una cadena de farmacia? Yo para escribirle acá que lo haga. ¿No hace falta, no sé, un monitor de venta, una cosa por el estilo?

**Leonardo Tocci**: Sí, monitor de ventas puede ser, puede ser algún forecast. Va a depender de la necesidad del cliente. En realidad. Nosotros en general actuamos en base a una necesidad de negocio específica. Hayamos hecho últimamente hay alguno en el que hicimos Customer Lifestyle Value, que no

**Gabriel Puertas**: sé si este tiene poca. Tiene un registro, digamos, tiene poco como

**Leonardo Tocci**: venta de poco tiempo, pero o sea

**Gabriel Puertas**: que un Lifetime Value posiblemente no funcione.

**Gabriel Puertas**: Preguntarte, ¿Alisa la posibilidad de generar? ¿Lifetime Value basado en los clientes? Tengo duda. Registros de clientes tiene. Hace un análisis de eso y luego vemos cómo seguimos.

**Gabriel Puertas**: Ustedes piensen esto, no sé si ustedes utilizan alguna herramienta tipo Cursor o VS Code, viste esto que el famoso bycodeo, la idea de Téramo es que les permita bycodear, pero con los datos. Es un poco la idea. Acá fíjense lo que yo le pregunté, lo hice muy genérico, tomando el ejemplo que vos me pediste. A mí me gusta mostrar, sobre todo a la gente técnica, lo que está haciendo acá. Lo que está haciendo. Yo le tiré che, mirá, fíjate si podemos calcular un Lifetime Value. Tengo duda de que también están los clientes para eso. Acá está haciendo unas queries exploratorias. Tienen que ver con entender realmente qué perforación de clientes tengo en las ventas. Yo le pregunté así porque ya sé que eso pasa. Y estas son las. Fíjate que está haciendo. Le tiró uno, acomodó un poco la primera, le tiró un error, la segunda también. Vamos la tercera. Tac. Esta me está mostrando. Voy directo con eso. Fíjate que le tiró un error. Porque esto tiene que ver con lo que dijo Lucio al principio. Es posible que se esté actualizando algunos nombres, pero digo, lo bueno de esto es que nosotros, la herramienta le permite iterar y autocorregirse, o sea, básicamente lo que está haciendo acá es ver qué role tira y acomodo todo.

**Leonardo Tocci**: ¿Te fue a buscar la otra tabla?

**Gabriel Puertas**: Claro, Ahí está.

**Gabriel Puertas**: Bueno, en fin.

**Gabriel Puertas**: Lo que está haciendo es a ver qué dice. Ahora voy con el análisis completo,

**Lucio Rojas**: Vamos

**Gabriel Puertas**: a inspeccionar un poquito qué está haciendo. Acá consigo resultados. Estas son todas query exploratorias que está haciendo el propio Cloud. Esta query corre en la infraestructura de theramot, le ofrece los resultados. Acá deberíamos ver algún tipo de resultado. La forma en que está, Le va a decir que no tiene acceso con los clientes. Yo recordaba que había un problema en esta base de datos con los clientes. Pero fíjense como él acá la idea, independientemente del resultado, es, fíjense la capacidad que tiene para ir haciendo estas query exploratorias y traerte un resultado que tenga sentido. Muy revelador el tribunal. Ahora voy a medir la cobertura y la riqueza histórica del cliente identificado.

**Gabriel Puertas**: Y ahí sigue.

**Gabriel Puertas**: Acá lo que está haciendo es pueriar sobre, debe ser sobre la tabla de clientes. Select líneas

**Gabriel Puertas**: response,

**Gabriel Puertas**: acá le dice líneas sin cliente, casi todas líneas con cliente, muy poquita. Total de línea, tanto porcentaje con cliente, 4.5 %. Esto no hace falta que lo lean de acá, yo les estoy mostrando porque usted es mostrarle lo que está haciendo Claude con los datos. ¿Pero cuando? Y además, para que esperar esto no sea tan aburrido. Pero. Pero nada, es simplemente después cuando termine de hacer toda esa query, va a orquestar todo en una respuesta más probable. Me va a decir, Mirá, hay solamente un 5% de los registros que tienen

**Leonardo Tocci**: identificado, no alcanza para hacer un análisis significativo o ninguna cosa por el estilo.

**Gabriel Puertas**: Claro, es como decir, el programa del Oyalty de la farmacia es bajo, no sé, una cosa por el estilo, no sé nada. Podemos hacer otro tipo de análisis o lo que sea.

**Sabrina Colazzo**: La volumetría, perdón, ¿Incide dentro de la latencia, digamos, o es simplemente un análisis de estructura esto que está haciendo?

**Gabriel Puertas**: A ver, no entendí. Incide dentro de la latencia, Claro.

**Leonardo Tocci**: De la espera de tiempo de respuesta de la herramienta.

**Gabriel Puertas**: No, el tiempo de respuesta, este tiempo que tomó depende mucho del nivel de profundidad que tenga Claude para analizar los datos. Por ejemplo, si yo le hubiese preguntado, no sé, decime cuántas ventas, suponte que lo uso como consultor, o sea, como para consumir datos, le digo, decime cuántas ventas hice en el último mes. Eso va a ser una query muy sencilla, va a ir, la va a hacer y va a venir. Yo mi pregunta fue bastante profunda, porque le digo, che, tenemos que hacer un lifetime value, pero no estoy tan seguro que tengamos muchos clientes. ¿Como pase eso? Entonces, construir esa respuesta, dado que estos modelos son muy potentes, es como que el tipo decidió hacer muchas query para validar bien lo que está haciendo. El tiempo de respuesta va a depender de eso. Fíjate que la complejidad del prompt.

**Gabriel Puertas**: Dos, tres, cuatro cinco seis siete ocho

**Gabriel Puertas**: nueve diez once doce, trece queries para armar todo esto. Me dice, tengo suficiente información para hacer un análisis sólido, Voy a presentarlo. Línea de venta totales son 76 millones sin clientes, son lo que habíamos visto el 95.5.

**Leonardo Tocci**: Qué suele pasar como en esto, salvo que tengan un programa de fidelización muy, muy piola. Además no tenés traqueo de venta contra cliente.

**Gabriel Puertas**: Claro. Entonces vos decís, bueno, vamos a tener por otro lado. Pero eso es lo que a mí me gusta de esta herramienta. Bueno, acá podemos leer todo, pero no tienen asociado. Algunos clientes tienen revenue negativo, probablemente son operadores o cuenta interna. Mira, un detalle, yo no lo sabía, capaz que deberíamos dejar, pero digo, se da cuenta que hay algunos clientes que en realidad deben ser transacciones de conciliación o cosas por el estilo, que tienen como resultado negativo. Muestra el historial de dos años entre 2024 y 2026, frecuencia del top 40, cliente concentra 300 mil líneas. Bueno, y acá me ofrece hacer distintos análisis, ver distribución de revenue, investigar el revenue negativo, explorar retención. Bueno, esperá, vamos a hacer una cosa. Porque acá lo útil de todo esto es utilizar el criterio que tiene Claude para mejorar esto.

**Gabriel Puertas**: Decir, bueno, bueno, pero si mi programa de fidelización no es muy bueno, ¿Qué otra alternativa puedo ofrecer para hacer algo del estilo?

**Lucio Rojas**: Hola, buen día a todos. Juan, yo me sumé unos minutos después para volver a la pregunta de Sabrina por la latencia. Me imagino que ahí es por, a lo mejor estás pensando como la visualización final, el tiempo que tarda en escribir un reporte, en mostrar los datos, por ahí si hay consultas o cosas por el estilo. Acá lo que nosotros estamos viendo es el proceso de construcción de todo el pipeline de trabajo. Entonces acá Claude y por consecuencia tardan un poco más. ¿Pero por qué? Porque está escribiendo las queries que te generan todo el set de datos para que vos después lo puedas mostrar en un reporte. Entonces acá sí es un poco lento, entre comillas, porque lo que hizo como trago Gabo 15 queries en 4 minutos con un análisis complejo de un lifetime value. Yo vengo del mundo de datos, hacía migraciones de datos. Trabajé mucho tiempo con base de datos. A mí me decís, generame un análisis así ahora, la verdad que no sé ni por dónde empezar. Entonces, todo ese tiempo de tener el conocimiento de generar las queries y de armar la infraestructura, el pipeline de transformación para tener el set de datos que quedó representado en esa forma de reporte o de graficación que nos mostró Glo, pero tranquilamente podríamos tenerlo en una tabla final, o sea, todos esos datos sin quedar renderizados de esa forma para que vos después lo consumas en un reporte tradicional colgado en un sitio de reportería tradicional. Ahí la única latencia, cuando eso está productivo que tenés es pegarle la consulta a AWS, que es donde está hosteada la solución. Esto es lo único Sabrina, que igualmente si esto viene de un sistema On Prem, hace toda la transformación, es muy simple tomar ese resultado y volver a copiarlo al On Prem y ahí lo tenés en toda tu infraestructura con la latencia mínima. De paso, como no laburamos directamente sobre los transaccionales, no tenés problema de bloqueo, no tenés que andar pensando en cómo escribo la query, para que tengo que ir a leer en vivo transaccional, no, bloquear una escritura, una cosa, nada, esto va a cobrar copias que tiene obviamente su demora de refresco, no es tiempo real, pero esos problemas no los tenés, hay alguna cuestión del trabajo que te lo saca de la cabeza. Y luego está todo construido, o sea, si vos decís, che, esto que me acaba de escribir lo quiero productivizar, la tabla que contiene todos esos datos, que plot escribió, ya está generada, es nomás pasar a reportería y dar el reporte.

**Sabrina Colazzo**: Claro, sí, sí, o sea, principalmente mi pregunta se basaba en cuánto incide la volumetría de cada tabla a las que pega cada query, porque si una tabla tiene 100 millones de registros, no es lo mismo que corra una tabla con mil. Entonces no sé si es un factor, digamos, ponderante dentro de la latencia o no.

**Gabriel Puertas**: No, de la latencia no tanto, porque como te decía Juan, como eso está replicado en nuestra infraestructura que es AWS, nosotros el gestor de base de datos es Atina, un gestor que es serverless, o sea trabaja con archivos, entonces lo hace mucho más rápido, pero nada, no es transaccional, es lo que vos perdés, digamos. La idea, como te decía Juan, la idea nuestra es ofrecerte todo esto desacoplado de los servidores transaccionales con lo que te dijo, perdón, y a nivel costo,

**Gabriel Puertas**: los token tienen actividad caché.

**Gabriel Puertas**: Yo igual me quedé un poco con lo que me dijo, porque le dije, esto es lo que yo te decía utilizar esto cuando vas a consultoría. Yo creo que es súper útil, porque si viene esta farmacia y te dice, che, yo quiero un Lifetime value, vos te metes en los datos y te das cuenta que tiene 40 clientes que no va a hacer nada, yo no sé nada de marketing de esto, estos términos son medio nuevos para mí. Le digo, bueno, pero si mi programa de fidelización no es muy bueno, ¿Qué otra alternativa tengo? Se puso a analizar y me tira tres que a mí me resultaron súper copadas. Una, dejá de pensar en el cliente, pensá en la obra social y analizarlo por ese lado. Y esta para la gente de datos me pareció súper interesante. Que es lo que dice básicamente, che, vos vendés productos que son de consumo crónico, entonces por qué no empezaba a ver cómo compran eso y que otra compra te arrastra que. Claro, bueno, a mí me dio que me la voló. Entonces dice Lifetime value por obra social y plan, y acá te dice, bueno, este es el que mejor puede andar porque ya analicé los datos que importan y tengo suficiente datos y le pongo acá y ahí va a ser lo que dice Juan. Yo estoy esperando que me haga una tabla Cloud, porque hasta ahora una tabla Gol, ahí está, Ahora les explico qué está haciendo, pero digo, ah, está bien,

**Leonardo Tocci**: valía que no sea un análisis que ya tenés como muy parecido previo.

**Gabriel Puertas**: Claro, porque si ya tenés una tabla Gold hecha que hizo otro que se sirve de esos datos, él la usa, si no, lo más probable que ahora genere otra. Y esa tabla Gold que ustedes hicieron, que es súper importante, eso queda armado como un ETL, o sea, yo generé esta tabla Gold que me armaba el Lifetime value de estos clientes, buenísimo, mañana ya no la tengo que generar de vuelta, o sea, va a haber un Chrome que levanta datos, vuelve a levantar datos crudo, pasa por la capa bronce, por la capa silver y me actualiza la Go. Esa Gol ustedes la pueden usar para conectarlo a un Power BI, A mí me gusta pedirle los dashboards directamente a Cloud porque lo hace más lindo y es más rápido, pero bueno, nada, lo pueden usar con Power BI, pueden servir una aplicación, es decir, esos datos residen en este servicio que yo le decía, Tina, esos datos son de ustedes, o sea, ustedes tendrían un usuario, contraseña y todos los perfiles para hacerse de esos datos, lo pueden bajar. Ustedes podrían, así como yo le estoy pidiendo el Lifetime Value, es preparar un set de datos para correr un modelo de Machine Learning. Eso Cloud lo va a hacer, va a curar, lo va a normalizar, va a hacer todo lo que haga falta y lo va a correr, ustedes lo utilizan, corren su modelo, vuelve lo que haga falta, o sea, lo que les ofrece Téramo es la posibilidad de armar una infraestructura de datos de cada uno de sus clientes, que eso funcione como un ETL, se actualice y después utilicen los datos y la posibilidad de generar esas tablas. Gol va a ir codeando en cierta forma ahí lo que está haciendo es, vamos a ver lo que hizo, esto es lo que habíamos visto, se fijó qué tabla disponible tenía, le dice no tengo ninguna que me sirve acá no sé por qué salió a hacer algunas queries, no sé, habrá sido para armar algo, no lo sé, habría que verlo en detalle, más queries, la lógica funciona, tengo lo suficiente para validar, ahí está

**Leonardo Tocci**: armando la tabla de Gol, me imagino

**Gabriel Puertas**: acá validó que esto funciona y yo les quiero mostrar acá. No sé qué hizo, acá tenemos tool, acá análisis de valor por plan de seguro y obra social, cada fila representa question y estas son las instrucciones. Acá ya terminó y se le acaba de pedir a Tenam, si yo vengo y actualizo acá, acá a mí me debería aparecer esta valor por obra social.

**Gabriel Puertas**: Vamos a verificar que no estoy mintiendo.

**Gabriel Puertas**: Fíjense, la que le pidió crear es valor por obra social, tiene una descripción que se llama análisis valor por plan seguro obra social. Cada fila representa, y ahora les explico bien qué son estas questions o algo por el estilo, si yo me vuelvo a Theramo, ustedes la van a ver, acá tiene la descripción, ahora les explico bien para qué es esto está corriendo en progreso y Claude lo que le pidió a Theramo es que arme esa tabla basada en instrucciones. ¿Por qué esto es importante? Porque la idea es que como las queries corren en la infraestructura de Teramot, lo que hace Cloud es darle instrucciones a theramot de cómo armar esa tabla go, que son estas, yo esta tabla con esta otra hace estos filtros, qué sé yo, a nosotros esto nos resulta. Es súper importante que se persista, ¿Para qué? Para que estas tablas, que pueden ser distintas personas las que la van armando o distintos modelos de inteligencia artificial la que van consumiendo, sean reutilizables de alguna forma, o sea que vos tenga una descripción de para qué es, cómo le hiciste. Y acá cuando termine de correr y le dé un resultado que no dé error, va a tener la query de SQL que se generó y va a poder hacer un preview de los datos. Pero digo, y esta es la tabla que después se va a ir actualizando. Entonces, nada, si nosotros recapitulamos, nos cayó un cliente nuevo que no conocíamos los datos, que sabíamos que quería hacer una especie de lifetime value. Nosotros ingestamos esos datos, ese proceso ustedes no lo vieron, pero ponele esta tabla, si yo la ingesto nuevo, ponele que demora una hora en generarse todas esas capas silver con su capa semántica. Una vez que la tenemos listo, digamos, pasó esa hora, empezamos a utilizar con Cloud decirle, che, esto me están pidiendo un lifetime value. Bueno, nos pusimos a analizar, nos dimos cuenta que los clientes no se podía. Siguiente paso, recomendación, che, hacelo por obra social. La primer prueba fue esta tabla Gol, que ahora ya quedó conectada. Esta es la query de SQL que hizo usted. Quizás sean mejores que yo, sabiendo qué tan compleja es. Yo creo que la complejidad depende mucho de la cantidad de joins y casteos que hizo y cuestiones lógicas que son los que uno tiene que pensar. Y acá tiene el preview. Esta es la tabla final que quedó. Esta es la que todos los días cuando se actualicen los datos de entrada, esto va a volver a correr y se va a actualizar. Si yo me vengo acá, este me debería decir, ya la generé, la tabla quedó construida y los datos son muy ricos. Voy a visualizar lo más importante. Y este ahora ya lo que está haciendo es, como él la hizo a la tabla Gol, empezar a extraer valor de esa tabla. Lo más probable que arme algo parecido como un dashboard o algo por el estilo. Entonces fíjense que ahí ustedes ya tienen un. Un primer entregable para ese cliente, quizá haciéndolo en un proceso que siendo muy generoso, le toma un día hacer una primera iteración. Es un poco la idea de Theramo. Todo eso para que sea posible, obviamente se utilizó mucho a Cloud, pero para que Cloud pueda hacer todo esto necesita un acceso seguro y confiable y que le permite hacer todas estas cosas, que es lo que básicamente ofrece nuestro producto. Nada, no sé qué es todo esto que está haciendo, después me lo explicará.

**Sabrina Colazzo**: Gabriel, Perdón, ¿Cómo maneja Teramot el tema de gobernanza? O seguridad, por ejemplo, no sé, para que un cliente, digamos, solo vea lo suyo y no lo que no tiene que ver, por ejemplo, qué sé yo,

**Gabriel Puertas**: lo que nosotros, o sea, nosotros, nuestra infraestructura, o sea, nosotros del minuto cero entendimos que esto es un producto para empresa y que nosotros teníamos que certificar. Nosotros certificamos SOC y estamos certificando ISO 27001, que es como un paso

**Lucio Rojas**: que

**Gabriel Puertas**: tiene que ver con, digamos, lo que te certifica eso es la forma en que vos manejas los datos un poco más. El capó lo que hace es, cuando vos generas un caso de uso, dentro de poco se me empeza a llamar Workspace. Suponte que Baufest abre, vos lo que deberías hacer, creo yo, es un workspace por cliente. Ese workspace es un tenant individual de AWS. Esto quiere decir, todo el pipeline de datos es como aislado por Workspace. En términos de infraestructura, quiere decir que no hay conexión física entre, no sé, nosotros trabajamos con Coca Cola, nunca Claude te va a decir a la farmacia, che, mira, vi en Coca Cola que pasa así eso porque está armado de esa forma. Después, la otra parte que es importante es que vos dijiste que es gobernanza. A través de nuestra página vos tenés dominio de por dónde están pasando los datos, qué se está haciendo, podés controlar qué usuarios acceden a este MCP. Eso yo lo pasé medio rápido, pero vos acá generas una API key, le pongo Baufest y la genero. Esta es una key que es con la que vos te conectas a cloud. Y esta key le indica a cloud que solamente tiene acceso a este caso de uso. Y nada, vos por workpate podés generar la que vos quieras, incluso gestionarla, generarla, revocarla y todo lo que sea. Y lo que vas a poder hacer en esta versión no tiene es la posibilidad de segmentar. Pensalo como la farmacia, porque quizá para un consultor tiene más sentido acceder a toda la información. Pero suponte que vos laburás en una farmacia y vos decís, bueno, pero yo quizá no quiero mostrar los financials o los datos de todas las sucursales a todo el mundo. Entonces yo voy a hacer una segmentación de esa información. Es decir, me voy a quedar con una vista que tenga una sola sucursal y solamente lo registro de esa sucursal y le voy a conectar eso a la gente de esta sucursal, como para que vos tengas gobernanza de qué segmento ves y quién lo ve. No sé si me explico, pero un poco esa es la idea. Eso nosotros lo pensamos para empresas grandes que no sé conectan todos sus datos y vos tenés los datos financieros, los datos productivos y él no, yo al financiero le voy a dar estos datos, a la gente que está en fábrica no le quiero dar mis datos financieros.

**Gabriel Puertas**: Pero eso se maneja desde la herramienta de ellos, no desde acá.

**Gabriel Puertas**: No, no, vos lo que podrías hacer es tener un owner de ese workspace, suponte que sos vos, decir bueno, yo veo todo y yo decido después quién ve que, en este caso yo soy de la sucursal 1. Bueno, Gabriel solamente va a ver, vos le armas una segmentación que lo armás con los modelos y decís bueno a Gabriel le voy a conectar solamente los registros de hechos que tienen que ver con la SU, no muestro más nada.

**Gabriel Puertas**: Eso sí te entendí, pero desde la herramienta, o sea técnicamente cómo llegamos a decir, o sea, entiendo que segmentamos la información y después como digo, Gabriel solo puede ver esto, ¿Cómo le hago?

**Gabriel Puertas**: Le armas un proyecto a Gabriel y le creas la API key, o sea la armada del proyecto tiene todas esas segmentaciones lógica que son lógica de negocio, y le compartí a Gabriel esa API key que le permite ver solo ese proyecto.

**Gabriel Puertas**: Una consulta, perdón. ¿Como en una primera instancia se conecta a los distintos sur, hay sur que ya tienen los permisos gestionados o los tenés ya administrados dentro de las bases, heredan esos permisos y ofrece segmentación a partir de esos permisos, no?

**Gabriel Puertas**: ¿Si vos levantas una base de datos, o sea después Teramot es como que después tenés que segmentar los permisos después de la ingesta de la nueva,

**Leonardo Tocci**: o sea, a ver, a nivel Lake House, que como que lo terminan desplegando, no tenés, tienen definido una herramienta de gobierno de datos, esto lo levantan en Atenas, ustedes hay una herramienta de gobierno que usen?

**Gabriel Puertas**: Lo que te digo es, o sea, se utiliza desde la página y vos armas distintos proyectos y segmentas el acceso en función de esos proyectos, pero es

**Leonardo Tocci**: por proyecto, no tenés como manera de definir, pensándolo a futuro, vos dejas definido los pipelines de trabajo, es como que hiciste el laburo que hacemos nosotros como data engineer en general, que es, entendí los orígenes, diseñé una plataforma donde vos puedas dejar tus datos, te armo los procesos para traerte esos datos y te dejo al menos a alto nivel los permisos que esa plataforma requiere, después vos vas a seguir viviendo y operando. ¿Esto tiene que por un lado actualizar, que eso no sé dónde cae, de

**Gabriel Puertas**: qué manera te que este tiene, o sea vos actualizadas acá, vos definís acá la frecuencia con la que actualizada y el horario, fíjense que estaba a las 9, por eso Lucio casi le dio

**Leonardo Tocci**: un algo porque justo le estaba actualizando

**Gabriel Puertas**: cuando estaba 9 de la mañana y

**Lucio Rojas**: querés comparte un segundo cómo es la segmentación de USE?

**Sabrina Colazzo**: Perdón, tengo una última pregunta antes de que pasemos. ¿Hay algún tipo de estrategia de masking o enmascarado de columnas o simplemente si es data sensible la sacas a la columna y deja de ser parte de la tabla?

**Gabriel Puertas**: Mirá, es buenísima tu pregunta porque justo estamos discutiendo eso. Nosotros estábamos pensando en agregar una capa de anonimización, nosotros la pensábamos más te digo la verdad, como para que a vos te dé confianza de subir una base de datos como prueba, me interesaría mucho entender si a ustedes eso les serviría, porque acá un poco la discusión es, una persona como ustedes que sube una base de datos para probar, tiene mucho para perder, poco para ganar eventualmente si hace algo que no, entonces en definitiva todo se dirime en confío o no confío en la anonimización que hizo. Obviamente nosotros estábamos pensando hoy hacer una capa de anonimización con un modelo de inteligencia artificial, incluso el modelo puede detectar qué datos son sensibles y hacer un masking como vos decías, es decir, vos hacés una prueba y te va a decir el cliente XJW es el que más vende y vos sabés que ahí hay un nombre detrás, no sabés quién es, pero está. ¿Mi pregunta quizá es si ustedes confiarían en esa capa, o sea si vos conectarías, porque nosotros tenemos un tier que es free, entonces vos analista decís che que bueno que está esto Theramot y tiene para probar gratis, La pregunta es, si tuviese esa capa de anonimización, conectarías tu base de datos?

**Sabrina Colazzo**: ¿No, claro, si es un tier free no, porque rompe con los patrones quizás de la data sensible, pero nada, o sea como mi pregunta iba más para el lado de si era escalable para,

**Gabriel Puertas**: no sé, para y cómo lo usaría ese masking, porque vos decís, yo conecto Teramot con una capa de anonimización y en dónde desanonimizas para consumir, no?

**Sabrina Colazzo**: Bueno, ahí es donde viene quizás el tema de la gobernanza y seguridad por usuario, donde un usuario puede tener permisos para ver esa data desenmascarada y otro usuario puede no, digamos, por ejemplo una data de recursos humanos, no se me ocurre. Sí, o bancaria o bancaria, totalmente.

**Gabriel Puertas**: Está bueno, o sea, sí, para nosotros, o sea, para nosotros hacer herramientas tiene mucho que ver con lo que nos traiciona como producto, con lo que encuentres

**Leonardo Tocci**: que te pide la gente.

**Gabriel Puertas**: Interesante. Vos lo que decías, bueno, yo ingesto y hago todos los análisis con una capa de anonimización y después las desanonimizaciones la hago por perfil. Entonces tales personas pueden ver el dato real o no, pero cualquiera puede generar valor con los datos.

**Leonardo Tocci**: Claro, en realidad, si vos lo que vas a hacer es un análisis clusterizado de esa información, no te importa que sea ese cliente en particular, si vos lo que vas a hacer es como definir bloques y ver cuál es el bloque que más vende. Ahora, si vos por lo que sea, como decías alguien, no, que yo soy de recursos humanos y tengo que poder entrar y saber exactamente cuál es el vendedor que tuvo más venta el año pasado.

**Gabriel Puertas**: Está bueno, interesante. ¿Y ustedes hacen algo de eso? Ustedes laburan así como.

**Leonardo Tocci**: Sí, sí, sí. Dependiendo del cliente y las particularidades de ese cliente y lo que haya que hacer. Sí, de hecho la pregunta seguro de Sabri está driveada por un.

**Gabriel Puertas**: ¿Le estoy sacando datos a ustedes, pero digo, y el masking que ustedes hacen? ¿Ustedes vienen y dicen, no, bueno, estos datos son sensibles, los nombres de las personas, los clientes, el saldo, si un banco, una cosa así, o hay una lógica por atrás general de enmascarado? Explicó, Nosotros lo pensábamos como decir, yo pongo un agente que analice los datos de las columnas y diga, con un promoteo inteligente que diga, che, esto es sensible, lo voy a anonimizar. Si ustedes preferirían tener injerencia en esa anonimización.

**Leonardo Tocci**: En general va a depender como, corríjanme chicos, más claro, pero generalmente va a depender de ese cliente, quién sea el dueño de esos datos, para qué se vayan a usar esos datos y cuál sea la decisión a nivel organización de qué tipo de acceso van a tener, independientemente de cómo técnicamente después resolvamos el enmascarado o no.

**Gabriel Puertas**: Es que después aparte depende, hay datos que pueden ser intuitivamente sensibles y datos que necesitan de alguien que defina si ese dato es sensible en algún momento

**Lucio Rojas**: está bien, y otro está

**Leonardo Tocci**: por leyes así como más amplios. HYPA, GDPR, o sea que te dice explícitamente, por ejemplo, si trabajaste en España no podés entender el trazado entre número de seguridad social y persona, porque ahí

**Gabriel Puertas**: eso es lo más fácil, porque es un modelo, lo hace y lo hace bien. Es más probable que nosotros nos equivoquemos interpretando GDPR que por eso lo que nosotros pensamos cuando esto se pone en serio, una base de datos de un banco quizá tiene 1500 tablas, tiene columnas, Entonces digo, pensar en anonimizar de memoria o seleccionando, ¿No?

**Leonardo Tocci**: Como que el racional detrás de esa anonimización siempre es mandato de cliente o mandato regulatorio que te implique que vos tengas que trabajar en esa anonimización.

**Gabriel Puertas**: Claro, lo que estoy pensando yo, que debería correr un agente sobre la base de datos y levantar un criterio de anonimización.

**Leonardo Tocci**: Si vos sos experto de gobierno de datos, necesito que analices esta, esta y esta tabla.

**Gabriel Puertas**: ¿Y que me querés que haga esto

**Gabriel Puertas**: o haga otra cosa más? Pero bueno, en definitiva yo algo que no les mostré. Ah, te conectaste vos, Lucio. Sí, porque iba a compartir por tiempo, Lucio, que le mostré lo del pricing, que me parece súper.

**Leonardo Tocci**: Rápido.

**Lucio Rojas**: Primero lo que preguntaban de cómo segmentar a distintos niveles usuarios y qué data pueden ver puede hacer a partir de consumir tablas de un use case madre, si se quiere a use case más pequeños. Tomemos este como use case base, que es lo mismo que mostró Gabriel con todas las tablas de múltiples fuentes que se actualizan todos los días a las 9 de la mañana. Y nosotros a partir de MCP creamos una tabla que es la de valor por hora social. Hagamos el ejercicio que dijimos. Bueno, yo necesito darle tablas a Gabriel para que él tenga su propio warehouse. Gabriel es de operaciones y creé una bol para que él pueda trabajar solamente con eso y no con toda mi base de datos. Entonces tomo el ID de esta bol que creé y en un nuevo caso de uso, donde solo le di acceso a Gabriel, creo una fuente de datos que. Que tome como input esa propia tabla. Eso está contemplado dentro de la herramienta, se copia el ID de su tabla que creaste, la busca, la encuentra, y se puede hasta incluso seleccionar qué columnas de esa tabla puede ver Gabriel. Seleccionamos todas. Y mientras carga la fuente de datos, que es lo que va a poder ver Gabriel, que es su entorno de prueba, su entorno seguro, les muestro el pricing. Nosotros trabajamos con Tigers Flat, es bastante transparente, depende directamente de los cuellos de botella, que son las cantidades de tablas Gold o ETL que vos generaste. Es un modelo freemium, donde ustedes pueden probar hasta dos tablas Boy de forma gratuita, y luego va escalando en proporción a la cantidad. 5 tablas vol es un pack de 50. 20 tablas vol es un pack professional. Y después si ustedes, porque tienen más de un cliente, están escalando en volumen y no me hace sentido escalar proporcionalmente, pueden hacer un plan enterprise donde hablan con el tipo comercial y se ajusta un poco el consumo, la cantidad de clientes se pone entendiendo que son buen cliente, que sea algún tipo de descuento. También sobre ese tema, algo que quería agregar también, que no sé si lo dijimos, es que cuando hablamos de segmentación de información a nivel infraestructura, mencionamos los tenants de AW, que son los espacios que tiene cada uno de almacenamiento. Y ese tema puede ser nuestro, estar en nuestra infraestructura, o puede ser directamente de ustedes, donde ustedes nos dicen, quiero que esté adentro de mi propia cuenta W. Así manejo yo un poco lo que es esa privacidad de los datos. Así que eso también se puede ofrecer y no tiene costo adicional. Es más para nosotros, incluso mejor, porque no nos haría un cargo del storage

**Gabriel Puertas**: de esa, para el caso de ustedes, sería en un cliente de ustedes. No sé si Bauf tiene reductorenado.

**Leonardo Tocci**: No, nuestra infraestructura está levantada en Azure, pero igual trabajamos con todas las nubes también. De nuevo, va a depender como del cliente al que lleguemos.

**Gabriel Puertas**: Pero bueno, la idea nuestra es, para mí la charla estuvo buenísima, la idea nuestra es que se animen a probar y usar el Tile Free para hacer todo lo que yo hice, es simplemente consumirlo vía cloud y bueno, y usar datos que tengan sentido de consumir. Después lo que a mí me parece súper útil también es si ustedes tienen algún cliente, un cliente nuevo o algo por el estilo, que ustedes perciban que se puede. Que se puede probar rápido, como decir, che, bueno, si es tan rápido, mira, me apareció este cliente que me estaba costando meterlo por la cantidad de fuerza que tenemos, lo hacemos y nosotros con Lucio para ayudarlo en todo el camino de ingesta de datos, conexión, uso, para que nada, lleguen rápido a poder usar la herramienta.

**Leonardo Tocci**: Buenísimo, buenísimo. Sí la idea de nuestro lado era probar cuando con esas ideas seguro y sobre todo por el equipo que tenés del otro lado de acá, van a querer probar, así que seguramente los estemos molestando.

**Gabriel Puertas**: Dale, de una ahí. Nada, se pueden hacer usuario, cada uno te hacen un usuario y cada uno tiene el free, digamos, esto no es por Baufest sino por persona, por mail y nada, se puede probar y lo que haga falta nosotros a disposición para ese camino.

**Leonardo Tocci**: Buenísimo.

**luis alberto galeazzi**: Yo quería preguntar un poquito la estructura de servicios, porque Baufex tiene un cliente y ustedes son un Teramot, es un servicio a través de Baufes a ese cliente, digámoslo así, especie de triángulo, y el servicio de Teramot, un servicio permanente, repetitivo, en función de la cantidad de usos que tiene en el mes o no sé en qué periodo. ¿Comercialmente esto cómo sería que Teramot le factura directamente al cliente final?

**Gabriel Puertas**: Está buena la pregunta. Lo que yo les conté a los chicos de Bauf, si ellos de repente usan Cloud para agilizar su servicio, cloud code o lo que sea, ellos se lo pagan y nada, prestan un servicio mucho más rápido, así le hablé a Baufest, o sea, para ellos ellos pagarían el. Suponte que me voy a poner creativo, suponte que con esto pueden, no sé, atender 10 veces más clientes y eso le implica, no sé, ellos pagan el tier de

**Gabriel Puertas**: como usuarios y nosotros no

**Gabriel Puertas**: sabemos cómo ganan de eso. Ahora vos decís, no sé, Senkosud, le mostraron a Senkosud le gustó y Senkuzud dice che, yo quiero esto porque quiero usar Cloud para consumir mis datos. Yo, nosotros tenemos un plan como de referido que vos decís, bueno, ahí Bauf es un partner y nada, se nos está acabando el tiempo, pero digo, tenemos un esquema de referido que también puede funcionar, o sea decir si ellos nos traen la cuenta esa, como el esquema de partner que tiene de esta herramienta es como un implementador de Theramore, también lo tenemos, incluso tenemos si lo quieren vender, digamos, decir che mira tateramo, che yo te lo vendí. Bueno, entonces normalmente el primer mes de la facturación se la queda el vendedor y ese tipo de esquemas está, eso

**Lucio Rojas**: después lo podemos aclarar, pero en términos de negocio son dos opciones claras, una es usarlo vos como ventaja competitiva para tener más clientes, y la otra es llevarlo hasta hay decisión de negocio de Baufor. Yo tenerlo como ventaja para tener más clientes y no llevar cliente final. Pero eso depende de la. Pero lo podemos también conversar en una.

**Gabriel Puertas**: Les repito que lo que mostramos y vimos, los pricing y todo eso, está pensado como una herramienta para Baufes, después que si el cliente de Baufes no

**Leonardo Tocci**: se entera que usaba Téramo, Sí así nos lo habían mencionado la primera charla,

**Gabriel Puertas**: también es una herramienta y los tires están hechos para eso, para que ustedes lo usen y nada, y sale de esa forma.

**Leonardo Tocci**: Sí, lo único hay como que diferente a lo que en general nosotros prestamos como servicios, que quede atado como

**Lucio Rojas**: la

**Leonardo Tocci**: vida del producto, el producto, la plataforma de datos a Theramot, porque sigue corriendo como bajo esquema de ustedes.

**Gabriel Puertas**: Sí, ahí puede ser, o sea, si vos querés armar el ETL, eso es cierto, pero si vos te fijás, nosotros damos plena visibilidad de todo lo que se creó, o sea.

**Leonardo Tocci**: Sí, sí, y lo habíamos charlado con Bruno, es que es como lo único que diferente conceptualmente en como en general nosotros planteamos estos servicios, que es entramos, hacemos el mismo laburo que hace la herramienta, pero lo que dejamos lo dejamos disponibilizado en plataforma de cliente y eso sigue viviendo independientemente de intervención nuestra.

**Gabriel Puertas**: No, no, pero te quiero decir Leo, fíjate que todas las queries que van de la bronce a la silver, de la silver a una gole, están explícitas,

**Leonardo Tocci**: las podríamos agarrar, copiar y desplegar y

**Gabriel Puertas**: usar el mismo tile para otro cliente. A nosotros no nos cambia nada, o sea, nuestro negocio no es quedarnos conectado en eso. Menos para las consultoras, porque vos entendés que eso te genera un gasto recurrente que no entra dentro de un esquema de la consultora. Lo que nosotros sabemos que una empresa que implementa esto va a decir, che, me es más fácil seguir pagándole $50 o $200 a Téramo, que armá yo toda la infraestructura que después la voy a tener que mantener. La idea nuestra de mostrar toda esa square y todo lo que se fue haciendo es justamente eso, que eventualmente te lo llevar.

**Gabriel Puertas**: Pero bueno, sí, no, está perfecto.

**Leonardo Tocci**: Sí, sí, sí, creo que había sido también parte de esa primera charla que habíamos tenido también con Bruno.

**Gabriel Puertas**: Yo creo que el gran valor para para un cliente como ustedes es que los acelere. La idea es que, viste que ahora nuestros dev, por ejemplo, los obligamos a que utilicen modelo, la idea es que entreguen 10, 15, 20 veces más rápido, digamos, vaya mucho más rápido. Yo creo que esa es una gran ventaja en una consultora y me parece que eso va a marcar una diferencia en la que lo adopten o no. No digo por Téramo en particular, pero digo que entiendan la nueva velocidad. Buenísimo.

**luis alberto galeazzi**: Yo no sé si hay un próximo paso definido o no sé, ustedes se quedan pensando Leo, cómo hacer, cómo sería lo que sigue.

**Leonardo Tocci**: Ahí nosotros si querés Luis, lo que vamos a hacer a la interna es pensar alguna situación, alguno de los clientes que estemos trabajando, ideas que tengamos en existente para ver si podemos probar y verlo primera persona, porque está buenísimo que nos muestren, pero viste que en general estas cosas se entienden cuando lo elabora uno en vivo.

**Lucio Rojas**: Bueno, seguir ese proceso con los próximos pasos, explicarles qué formato de archivo tienen que ser, si quieren cargar, un placer, si quieren contar soporte,

**Leonardo Tocci**: por lo menos

**Lucio Rojas**: por lo pronto,

**luis alberto galeazzi**: Bueno, creo que cumplida la reunión, ¿No es cierto?

**Gabriel Puertas**: Verlo haciéndose una cuenta.

**Leonardo Tocci**: Bueno, dale. Muchísimas gracias.
