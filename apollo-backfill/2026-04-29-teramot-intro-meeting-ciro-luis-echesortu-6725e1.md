# Teramot Intro Meeting (Ciro Luis Echesortu)

**Fecha:** 2026-04-29T14:46:01.310+00:00  
**Duración:** ~43 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Ciro Luis Echesortu <luis.echesortu@ceibosgroup.com>  
**Externos:** luis.echesortu@ceibosgroup.com  
**Apollo ID:** 69f223c2ae4fc000196725e1

---

**Lucio Rojas**: Buenas noches. Hola Lucio. ¿Todo bien? Te pido disculpas, estoy tratando de que me tome la cámara. Dale, no me apuro. Segundo que voy a probar haciendo un cambio. Bien, No tuve éxito.

**Ciro Luis Echesortu**: Ahí vi la cámara. Un segundo. Vi tu cámara por un segundo la vi. Igual que. ¿Cuál es el problema, la cámara o el audio?

**Lucio Rojas**: Ahí estamos. Ahí estamos. Bien, perfecto. Disculpa, teniendo este problema que mil veces toma, a veces no toma la cámara. Bueno, ahora sí. ¿Cómo estás? ¿Todo bien?

**Ciro Luis Echesortu**: Todo bien. Perdón, se te corta mucho, pero entiendo que estás preguntando. Si, Ciro, Luis, cualquiera de los dos.

**Lucio Rojas**: No tengo preferencia.

**Ciro Luis Echesortu**: Se te corta mucho la conexión.

**Lucio Rojas**: Ahí estamos. Ahora sí. Ahora sí. ¿Me escuchas bien? No surfeamos por todos los problemas de conectividad posibles en cinco minutos, pero ya la pasamos. Estábamos esperando también a Juan, no sé si lo conoces personalmente o si solamente reunión, pero está en una reunión que tragando. Así que por lo pronto arrancamos con. Si querés, para entrar un poco en tema, yo no tengo todo el contexto. ¿Querés contarme cómo llegaste a Telamot? ¿Si conoces a Juan?

**Ciro Luis Echesortu**: No, una persona que trabaja con nosotros conoce a Bruno y me dijo hace unos meses, en diciembre, me dijo, me contó sobre Theramot, estábamos pensando armar un data Lake y me comentó un poco lo que ofrecían. Lo vi en ese momento por encima Y bueno, en el transcurso estuvimos avanzando con algunos otros proveedores y quería entender mejor cómo era la oferta de Theramot como tal y en dónde se diferenciaba para entender cómo se relacionaba con lo que necesitábamos.

**Lucio Rojas**: Bien. Entonces entiendo que un poco para sacar provecho de los minutos que tenemos te puede servir ver alguna demo, recorrer la herramienta, entender cómo funciona y hacer algunas preguntas.

**Ciro Luis Echesortu**: Sí. Entender cómo se integraría a distintas fuentes de datos, qué tipo de conocimiento necesito tener para interactuar con ella, con la herramienta y si hay capas de modelado de la información, temas de ETL y demás, cómo se gestiona eso y sobre qué nube está, cómo lo integro con. Otras fuentes o mismo LLMs que interactúan con. Con nuestros datos. También

**Lucio Rojas**: hacemos un recorrido, si te parece, sobre la herramienta y generalmente se cubren esas preguntas. Andá haciéndolas puntualmente así. Lo primero, esto es la web de Telamont. Está sobre unas fuentes de datos de prueba que simulan ser datos de una farmacia y lo que tenemos es una herramienta que automatiza todo el proceso de construcción de ETL. Se conecta a más de una fuente de datos a partir de conectores que desarrollamos. Tenemos las grandes fuentes de bases de datos como SQL Server, BigQuery, MySQL. Nos conectamos a algunos sistemas como ASAP. Tenemos ASAP desarrollados, asaforce es lo que nos hemos encontrado con los clientes. Si se requiere un conector por fuera de alguno de estos servicios, se puede desarrollar. Vamos desarrollando un poco a demanda. Y en caso de tener los datos en alguna nube privada, se puede hacer algún túnel con el equipo Infraestructura.

**Ciro Luis Echesortu**: ¿OK, pero en este sentido, la nube la tengo que traer yo, la tengo que contratar yo primero, separado e integrarla acá?

**Lucio Rojas**: No. ¿En dónde tenés los datos vos hoy

**Ciro Luis Echesortu**: entre Azure y Snowflake?

**Lucio Rojas**: Bien, creo que nos podríamos conectar directamente a donde están tus datos en Azure, Snowflake, y nosotros hacemos una copia de esos datos en la nube de AWS. La infraestructura está inmersa dentro del servicio. Ahora vamos a ver cómo se desarrolla TTL. Pero vos no tendrías, si querés, no tendrías que tocar nada de infer. Dejo un espacio en el sitio, ¿Se puede hacer algo?

**Ciro Luis Echesortu**: Apago la cámara un segundo que me muevo.

**Lucio Rojas**: Entonces aprovecho para avanzar un poco cuál es el proceso. Una vez que vos conectas las fuentes de datos, se corre una primer llamada o grupos de agentes que se encargan de la normalización y estandarización de esas fuentes de datos que se cargaron. Estandarización de columnas, de fechas, de nombres, detección de outliers, eliminación de duplicados, etcétera. Y ahí se genera dentro de nuestra arquitectura, lo que decimos que es el paso de una capa bronce, que es los datos como vienen de origen del sistema de clientes, a una capa silver, que lo que hace es tener esos mismos datos ya estandarizados, curados, sanitizados. Y se crea una capa semántica que te deja una suerte de mapeo de cuál es la fuente que vos conectaste. Entonces nosotros conectamos 5 o 6 fuentes y después cada una de esas tablas y columnas dentro de esa fuente se genera una descripción y la gente de Fixer, que nosotros le decimos, hace un mapeo general de qué es lo que tenés conectado y ya listo para pasar un agente moderado.

**Ciro Luis Echesortu**: Y en este caso, ¿Este es propietario de ustedes o están usando algún ETL, no sé, un servicio microservicio de AWS que limpia Nosotros usamos DBT por ejemplo, por encima de Snowflake para esto, pero esto es propio suyo nativo?

**Lucio Rojas**: Nosotros lo que hicimos es construir la tecnología que hace el pipeline completo, desde conectar los datos hasta desployar la tabla en latina de AWS. Y son dos agentes que interactúan y agentes que orquestan cada uno de los que tienen función particular que están dentro de nuestra solución como SaaS está patentada en Estados Unidos con tecnología, no estamos usando algún servicio de terceros en esta parte. ¿Acá un poco lo interesante y también

**Ciro Luis Echesortu**: te quería preguntar qué tipo de clientes es como que usa esto o está pensada la solución para qué tipo de clientes? Más que nada, bueno, anticipándome ya el tema costos o qué tipo de servicio tengo que montar encima de esto, si es un ingeniero de datos que que lo mantenga, qué complejidad y bueno, cuánto puedo cambiarlo en sentido que cómo me compite contra mi proveedor de Data Lake que me ayudó a armar el repositorio en Snowflake o en Azure.

**Lucio Rojas**: No creo que nuestro valor principal esté en lo que es el Data Lake que queda deployado en AWS en sí o en cómo nosotros alojamos información, sino la facilidad que te damos a vos para crear nuevas etapas de modelado, ampliar nuevas tablas. Gol en general ese análisis, que es la parte que todavía no vimos de la herramienta, pero después todo lo que es infraestructura está provisto como como SaaS o IaaS, si querés, vos te conectas, no necesitas nadie técnico de soporte de tu lado. Y con la licencia, la gratis, la starter son $50 o la professional son $200, ya incluye todo el mantenimiento de infraestructura, no necesitas ningún recurso adicional que lo gestione. Yendo un poco más a lo que es lo que nosotros entendemos que genera valor, es la parte del modelado de nuevas tablas. No sé si me contaste bien qué es lo que hacen dentro de tu empresa.

**Ciro Luis Echesortu**: Somos una compañía de producción agrícola, que además tenemos una empresa de originación de granos, o sea de servicios a productores. Y procesamos alimentos de forma primaria, o sea en seco, para generar harinas o texturados y demás. Y algunos hacemos empaquetados en origen para retailers y eso en distintos países. Somos si querés un grupo de muchas pymes que cada una tenía su isla de datos o su no isla de datos, y estamos integrando todas a un ERP, si querés, único modelo único y después por encima de eso, aplicaciones de operación, porque hay una aplicación distinta de producción agrícola, a la de originación, a la de procesamiento industrial. Entonces cada una de esas aplicaciones generan un dato distinto o un set de datos distintos que interactúa con el ERP. Y eso nos da, para darte una idea, no sé, cuánto estoy cosechando por hectárea, contra cuánto estoy comprando de grano, a qué precio, contra cuánto estoy vendiendo por kilo la bolsa porotos, por ejemplo. Entonces todos esos son datos distintos en compañías distintas, pero con un stack, si querés, comparable. Y quiero que todo eso vaya a un repositorio donde pueda generar distintos reportes o habilitar ese repositorio curado con cierta limpieza, para que cualquiera de la organización, sea administrativo del negocio, pueda consultarlo y hacer un tablero o o responder preguntas.

**Lucio Rojas**: Perfecto. Bueno, veo que ifit es un poco lo que propone la herramienta. Es decir, tenés múltiples fuentes de datos que vienen sistemas de distintas empresas desconectadas entre sí, están en entornos distintos, los conectas a Telamot, a partir del conector a esa base de datos, se genera la suerte de warehouse, donde los mismos modelos ya entienden cómo relacionar esas tablas. Entonces no tenés que trabajarlo vos, que es un poco la parte más tediosa. Y después se habilita esta parte de reporting ad hoc, Después vemos el tema de cómo segmentar la información y demás, que se puede hacer. Pero por ejemplo, este usuario del negocio que vos describís, que quiere saber algo sobre los datos, seríamos nosotros en esta demo, donde yo le pregunto desde Cloud a Telegram, que se conecte y me diga qué tablas tengo para hacer análisis. ¿Por qué nosotros nos conectamos a Cloud? Porque entendemos que la mejor interfaz o la mejor forma de trabajar con tablas, que vos no tenés mucho conocimiento de cuáles son, es a partir de una LL. Puede ser cualquiera, puede ser cloud, puede ser ChatGPT. Nosotros entendemos que está funcionando mejor.

**Ciro Luis Echesortu**: Esto te reemplaza el SQL Query, porque ahí te ayuda a interactuar con una interfaz de chat en vez de un query SQL. Y básicamente estarías pagando la licencia, implementación, licencia theramot, más la licencia de Cloud. En este caso, si quisieras hacerlo por fuera, lo haces separado.

**Lucio Rojas**: Si El costo son dos, la licencia de Telamo de 0.50 o 200, depende del uso que después corresponda. Y la de 20 dólares de cloud para tener los tokens cincuenta, cien.

**Ciro Luis Echesortu**: ¿Cómo es el tema de pricing?

**Lucio Rojas**: Si querés, no sé cómo estás vos de tiempo, si tenés que ir, pero si no, después recorremos el pricing desde página.

**Ciro Luis Echesortu**: Tengo hasta la una, no sé dónde estás. ¿Dónde?

**Lucio Rojas**: En Rosario.

**Ciro Luis Echesortu**: Hasta la una de Rosario.

**Lucio Rojas**: Entonces si querés después hacemos. Nos detenemos.

**Ciro Luis Echesortu**: ¿Cómo se compara Theramot con Hex? ¿Es parecido?

**Lucio Rojas**: ¿Conoces Gex? No conozco Gex. ¿Qué hace? Me describir un poco.

**Ciro Luis Echesortu**: Es parecido, es un Analytics Platform. Como así medio self service, por lo menos por lo que lo vi. Te lo dejo ahí en el chat para que lo veas. Estuve viéndolo también. A mí lo que. La razón por la cual arranqué trabajando con un Data Modeler en Snowflake es porque sabía. Sabía muy bien la base de datos que estaba manejando o el proveedor, entonces podía integrarse rápido y no tenía que tener alguien interno para lidiar con cómo conectarse con el data Warehouse, nuestro ERP. Pero estoy analizando próximos pasos, cómo evoluciona eso, y bueno, cómo evolucionan también los servicios encima de eso.

**Lucio Rojas**: Porque

**Ciro Luis Echesortu**: cada fuente de datos tiene su complejidad. Algunos tienen APIs, otros no tienen nada, y algunos tienen datos más sucios que otros. Entonces tengo que ver cómo los vinculo entre. ¿Tengo algún dato de lote o de siembra en un lado que es distinto al del otro? Y esa parte me hace entender cómo es fácil, es gestionar Enter a Mod. En comparación,

**Lucio Rojas**: ¿Cuántas fuentes de datos estás manejando hoy medianamente?

**Ciro Luis Echesortu**: Mirá, en esta demo que arrancamos, integramos tres una aplicación productiva vía API, un SharePoint con muchos Excel y. Y el ERP. Pero en total tenemos muchas más,

**Lucio Rojas**: no

**Ciro Luis Echesortu**: sé, más de 20. Si querés, para resumir cómo está, si querés te muestro la arquitectura, pero ahí está la complejidad de cómo haces el mantenimiento y cómo montas un servicio que se sienta cómodo sobre la herramienta,

**Lucio Rojas**: Qué

**Ciro Luis Echesortu**: conocimiento tiene que tener, si es SQL, si es otro, y sobre Amazon o sobre alguna nube en particular.

**Lucio Rojas**: ¿Vos lo que estás pensando es en contratar a alguien para que?

**Ciro Luis Echesortu**: Si tenemos a alguien, yo necesito a alguien que le dé el servicio al negocio, que no es técnico, que tampoco se va a meter, no sabe interactuar con datos, o no tiene tiempo para interactuar y poder modelar los datos o dejarlos listos para que los consuma alguien del negocio y darle esa guía. Entonces la pregunta ¿Eso lo ofrece Theramot como servicio o no? Te deja la licencia y vos manejate

**Lucio Rojas**: con

**Ciro Luis Echesortu**: alguien que sepa SQL o alguien que sepa esto, esto y lo otro.

**Lucio Rojas**: Acá lo que nosotros hacemos como Telamot es, hacemos una herramienta, la herramienta se va a conectar a múltiples fuentes de datos. Una vez que esté la conexión, ya si se quiere canalizada, se va a actualizar todos los días por default a las 9 de la mañana. Si ya está el puente hecho, no necesitas ningún soporte. Una vez tengas las múltiples tablas dentro de Telamon, las puedes trabajar desde cloud, como estoy viendo mostrando un ejemplo acá. Decirle bueno, quiero analizar las ventas, ¿Qué tipo de tablas tengo que cruzar dentro de mi warehouse para hacer un análisis de venta? Y me dice, bueno, en base a lo que vos tenés, tendrías que armar una tabla gold que cruce las tablas dim products, dim products, categories y subcategories, que son las dimensiones y la manufactura en determinados campos o columnas de esas tablas para poder realizar ventas. Además incluía algunas métricas como la suma de unidades vendidas, la suma de montos netos totales, ya entienden qué es lo que tienen tus tablas, porque genera una capa semántica y te permite a vos hacer nuevas tablas que quedan desarrolladas con infraestructura en producción. Entonces. Vos necesitarías soporte para crear esta nueva estructura de datos. ¿Si alguien que se siente usar la herramienta? Esta persona no tiene que ser necesariamente técnica, o sea, vos no tenés que salir a contratar un data engineering, administrar las tablas dentro de Telegram, o tengo que crear nuevas tablas o gestionar los permisos. Ha funcionado bien con analistas funcionales, ha funcionado mejor con usuarios técnicos, entiendo un poco más lo que están trabajando por detrás, ha funcionado con usuarios de negocio. Acá para que veas un ejemplo, en esta tabla estábamos buscando crear un modelo para hacer un análisis predictivo. Entonces dijo, bueno, en base a las tablas que tengo, una nueva tabla que soporte un análisis descriptivo, tendría que incluir el product ID, el product name y el branch de identificador. Incluir las unidades vendidas, te hace todo el requerimiento funcional de qué es lo que tiene que hacer la nueva tabla. Clarísima el requerimiento, que esto lo levanta Cloud de la interacción con el usuario. Y estos requerimientos después Teramot los convierte en query SQL. Esta query SQL, Teramot a su vez que hace una query ultra compleja, la convierte en una tabla en producción, ya queda el armado y todos los días a las 9 de la mañana cuando se actualice fuentes de datos de entrada, se va a actualizar el ETL final. Esto va a quedar atina de AWS y puede ser en el tenant de ustedes como cliente que propone su propio tenant o en el tenant nuestro de Telan, donde un poco ahí las ventajas y las desventajas es que si tenan, tienen más privacidad los datos que hay a su lado, pero pagan el costo del almacenamiento y si queda de nuestro lado, bueno, están de nuestro lado los datos, pero todo el almacenamiento y storage y procesamiento dentro de la licencia es un poco la diferencia. OK. Nosotros nos enfocamos mucho en intentar hacer una herramienta que entendemos que es barata, no son costos de implementación, vamos a generar un proyecto, sino que es un tier de licencia flat, donde si generas hasta 2 ETL Doublas Gold es gratis hasta la quinta estás dentro de un plan starter de 50 dólares hasta los 20 ETLs en un plan professional y una vez que escalas de ese volumen en un plan enterprise donde te sentás con el equipo comercial y bueno, si sos un buen cliente para nosotros, entendemos que es un volumen de uso interesante de herramientas. ¿Se ve algún tipo de descuento o de paquete a medida en base al consumo?

**Ciro Luis Echesortu**: ¿Y ese costo por mes tiene alguna limitante de usuarios o es solamente por el uso, por el consumo?

**Lucio Rojas**: Las limitantes son las que están acá, son la cantidad de tablas gold y storage, son las dos.

**Ciro Luis Echesortu**: Está bueno, yo creo que es como te da ese self service. Yo creo que todavía tenemos que armar nuestro equipo de analytics como para estar listos, decir bueno, alguien que se adueñe y dice bueno, lo puedo usar, tengo tiempo para usarlo. Medio que arrancamos con un servicio gestionado porque no teníamos ese equipo interno y el conocimiento nos iba a tomar más tiempo de llegar a un resultado. Pero es posible que a la larga nos miremos, aunque estamos con un costo bastante eficiente por el momento vamos a ver si se nos dispara o no, depende la dependencia que tengamos con este proveedor de mantenimiento, tiempo, etcétera. A ver, mostrame los conectores un segundo. Yo te quería preguntar, caso de uso con farmacias y el mundo de salud, ¿Qué otros clientes han visto esto? Si se han integrado con algún ERP ahí de Argentina, nosotros usamos uno que que tiene algunas dificultades porque también es una pyme. Tal cual. Y a veces hay que gestionar un poco lo que integra. Pero quería entender más bien en dónde se están enfocando a nivel evolución del producto y demás y qué flexibilidad nos genera si eventualmente queremos desviarlo, como decís, el tenant propio, hacer otras cosas, integraciones hacia dónde ven el producto y qué clientes son los que lo guían en ese sentido.

**Lucio Rojas**: Bien, nosotros clientes como BD o Más Enterprise, hemos trabajado con Coca Cola, con Johnson Johnson, que son de retail, hemos trabajado con lo que es más si quiere seguros o cobertura, como la segunda, una empresa más de producción, con la Virginia también acá de Rosario, una de las más importantes, con bancos también, con bancos de Buenos Aires, Molbin que también es ingreso nuestro, salía mucho lo que es la industria, no estamos apalancados sobre la industria, sino que vamos a un problema más horizontal que vertical. El uso de los datos, la construcción de los warehouse, eso lo vemos en todas las industrias y lo que hacemos o apuntamos como producto es una herramienta que se conecte la mayor cantidad de input de data posible y que le dé autonomía al usuario en generar su propio TL, consumir información sin depender de un equipo de datos. Entonces un poco en contra de la hipótesis que vos me planteás de tenemos que desarrollar un equipo de datos para hacer esto, nuestra idea con Theramot creamos

**Ciro Luis Echesortu**: Telamotis, no es un equipo de datos, sino como decís, es un funcional o alguien que lo maneje. Pero como hoy tenemos la persona que que hace visitas a campo, necesita el reporte, no tiene tiempo para ni aprender a usar la herramienta. Entonces es como decir bueno, puede aprender a hacer un SQL con Power BI, pero la configuración, entender quién la hace.

**Lucio Rojas**: Eso es lo que Si, a vos lo que te tira un poco del hilo por sí o sí el negocio es una persona que tiene que ir a una visita, un campo, a un cliente y tiene que decir bueno, cuánto vendió, ¿Cuándo le vendí, ¿Cuándo produce, cuánto siembra? No sé cuáles son las preguntas y necesita tener esa información en vivo de su base de datos real. Desde Telamo te conectarte a Clot y preguntarle eso y te va a responder sin tener jamás el reporte. Lo que vos vas a necesitar es un equipo interno que antes ya dejé tiempo configurado para que respondas a preguntas puntualmente, agarrar la fuente de datos, crear una tabla gold que se llame en este caso comercial Juan, el que va a visitar el campo.

**Ciro Luis Echesortu**: Tabla gold es el nivel de limpieza,

**Lucio Rojas**: Cuando vos conectas la base de datos sucia y queda limpia a partir del proceso automático de Telamot. Y tabla gold es juntar varias silver, hacer los joins o hacer la transformación SQL para que quede un reporte listo para consumir por el usuario de negocio. Entonces vos desde Telemo llegarías a este reporte que está listo para consumir por el usuario de negocio. Y desde cloud ese usuario en sí le puede preguntar, bueno, fíjate en theramo, se lo pedí por ejemplo, acá dice, fíjate en esta tabla que yo tengo clara en theramo y queda un dashboard de qué es lo que hay en los datos. Acá tranquilamente le puedo preguntar, decime cuál es el cliente que más vende, o este cliente, cuántos datos tengo, este cliente y una query. Esa tabla gold que vos ya armaste le responde como un chat biorrata en tiempo real. Entonces por eso decía que es como que tiene una complejidad que resuelve varias cosas en la solución. Resuelve la conexión a múltiple fuente de datos, la limpieza de nuevas tablas, que serían dejar la tabla lista para que la consuma el usuario de negocio, y también te da una solución en la mano que es muy sencilla, que es preguntarle a un cosas de tus datos, para decirlo bien incluso.

**Ciro Luis Echesortu**: OK, me queda claro, está bueno. ¿Si yo tuviese que hacer una migración de un lugar al otro, en eso, ustedes ofrecen algún servicio? Lo tendría que gestionar yo, ya tengo todos los modelados de un lado.

**Lucio Rojas**: Bien, tenemos un equipo de conexiones e infraestructura que entiende bien dónde tenemos alojados los datos, qué tabla querés migrar y las copias enteramente. Lo que sí es, vos el otro servicio lo tenés que mantener, solaparlo, ahí sí creamos el conector, es una copia, así que no copiar todo para hacer una prueba controlada, se puede empezar con algunas tablas y ahí probar cómo sería en Telamo, crear nuevas tablas de eso que conectaste y consumirlo desde el cloud, o sea consumirlo. A mí me pasa que yo me armo reportes para mi SEO acá internamente, que quiere saber cómo están los usuarios. Me conecté la base de datos de nosotros los usuarios a un dashboard de Telamo, le armé su tabla y le dije mira en este proyecto de clock desde el celular preguntar bueno cómo me crecieron la cantidad de usuarios inscriptos en el último dos días, últimos tres días y él ya tiene satisfecha su demanda de información y de medio yo tuve que orquestar la herramienta. Va a necesitar esas dos cosas, alguien que se ciega con la herramienta, la orqueste, genere las tablas, separe los usuarios según el acceso a la información que pueden tener en pareja. Bueno esta persona puede preguntar solo esta tabla, hay una suerte de arte ahí, pero la licencia siempre la misma. ¿OK,

**Ciro Luis Echesortu**: bueno

**Lucio Rojas**: acá nosotros lo que solemos ofrecer y las demos por ahí son complejas de explicar, es una solución compuesta, por suerte te veo técnico, así que

**Ciro Luis Echesortu**: espero nos haya técnico no? Pero bueno, voy aprendiendo cada vez más.

**Lucio Rojas**: ¿Lo que solemos ofrecer es decir bueno quieren probar la herramienta de forma gratuita, es lo que nosotros alentamos para que vean cómo funciona con datos de ustedes

**Ciro Luis Echesortu**: ahí si tuviese que hostear una una máquina virtual por procesar algunos datos también le ofrecen eso, un virtual machine?

**Lucio Rojas**: No, no ofrecemos eso. Dentro de lo que sí puedes hacer es preparar las tablas para después correr algún modelo. Hemos hecho tablas para hacer modelos predictivos y lo corremos localmente a la computadora y con su atina atina se puede conectar a ese tipo de.

**Ciro Luis Echesortu**: Pero ahí tengo que contratar a Tina separado, lo puede contratar Téramot por mí porque está en el tenant En ese

**Lucio Rojas**: sentido cómo es Tina es el servicio que pone las tablas, todo lo que vos creaste, las tablas son tuyas, la información es tuya. Si vos decís quiero agarrar la Gol que crees para hacer un modelo predictivo que tienen que correr en una marina mía, una laptop, decís bueno dame las keys y te conectas a Tina para entrenar ese modelo. ¿Se entiende? ¿Es como quedan donde viven los datos? Los datos son tuyos, si vos me los pedís, nosotros hacemos la conexión a Tina y los podés trabajar. Y si está más fácil porque bueno ya vos mismo administras las credenciales y demás, bueno también tiene la complejidad que tenés que saber hacerlo y no sé si es algo tan sencillo.

**Ciro Luis Echesortu**: Sí tenemos, justo entró al equipo alguien de de datos que está ayudando con eso y lo tenía en su propio equipo, estamos mudándolo o Azure o a Snowflake ahora y bueno quería entender qué flexibilidad había para ese tipo de cosas.

**Lucio Rojas**: OK, bueno, bueno, espero que haya quedado claro. Si quieren probarlo, nosotros atentamos. ¿Puede ser algún conector, algún SharePoint como decís vos con Excel, eso ya lo ha hecho o para hacerlo más dinámico todavía con algunos sbs?

**Ciro Luis Echesortu**: No, bueno, es que lo sé, Excel, CSV, están todos ahí en el SharePoint, pero para mí, déjame que tenemos que evolucionar un poco el servicio, aterrizar el servicio que tenemos ahora en Snowflake, proyectar los costos y entender si una vez ya modelado la información y ya estabilizado nos da para migrarlo porque es más económico y flexible el self service entero, eso más o menos estaríamos.

**Lucio Rojas**: ¿Y qué dificultades están encontrando ahora en lo que estás armando? Entiendo que si ves otras soluciones por ahí es por.

**Ciro Luis Echesortu**: No, la dificultad está principalmente en la limpieza del dato y el vínculo, el solapamiento del mismo dato con distintas características en una fuente y en la otra, o sea es más que nada un tema más de proceso, más que de proceso y limpieza, modelamiento. Entonces estamos más en 1. ¿Ya que estamos viendo el mismo dato en dos lugares distintos, cuál es el dato real? Y cómo cuando lo consultas le das al usuario alguna certeza, por ejemplo, dónde estamos sembrando, cuánto llovió, cuánto estamos cosechando. Tenemos esos datos repartidos en las tres bases de datos que te compartí, que estamos como en el submódulo y ahora estamos definiendo dónde tiene sentido y en qué formato hacerlo bien para que ahora lo puedo consumir a los tres, pueden interactuar bien en un informe. Tiene que ver más con el proceso y funcionamiento de las herramientas disponibilizadas más que otra cosa y hay algunos gaps en eso, porque tal vez hay usuarios que lo quieren mandan por WhatsApp o no usan la herramienta, entonces cómo empujar

**Lucio Rojas**: eso, o sea, es más problema de herramientas no tanto, sino de datos y.

**Ciro Luis Echesortu**: Anteriormente no teníamos un servicio de tecnología, entonces el proveedor respondía directamente al usuario y el usuario se frustraba porque el proveedor no le daba la solución que él quería, quiero este dato, quiero esta forma de subirlo, entonces generó desconfianza el sistema y todo revirtió. Si querés al Excel o a distintas tablas de reportes, puedo integrar ambos, el Excel y los sistemas y puedo darle una confianza al usuario si querés. No tiene excusa de subir la información, cualquier informe ahora sin esa excusa, entonces es en dónde tiene sentido que suba la información si la sigo subiendo en WhatsApp y a qué sistema nutre, si esa a una tabla en Excel o una tabla en la aplicación o lo que fuera. Y eso nos empieza a cuestionar cuáles son los sistemas que sí tiene sentido mantener, cuáles son los que tiene sentido reemplazar o consolidar. Entonces estamos medio en eso.

**Lucio Rojas**: Bueno, entiendo que lo tienen que analizar un poco internamente. Si querés llevarte algo desde tenemos, vas a poder conectar varias fuentes de datos y la herramienta sola hace la limpieza y entender cómo se relacionan esas tablas entre sí. ¿Que es lo que nosotros ofrecemos como valor? El modelado de todas tablas y la consulta desde algún L son derivados del valor de TER principal. Está en eso. Sí, sí, sí.

**Ciro Luis Echesortu**: Bueno, Lucio, yo te comento, entiendo el valor, te mantengo al tanto si resurge, si una vez estabilizado vale la pena hacer algún tipo de migración de algo. Todos los servicios que venimos consumiendo y hablamos,

**Lucio Rojas**: me mantengo agendado para hablar en el futuro y ver qué tal fue con esa. Dale, dale, Bueno, gracias. Dale, un gusto. Adiós.
