# Andromeda x Teramot

**Fecha:** 2026-08-18T18:00:52.964+00:00  
**Duración:** ~55 min  
**Participantes:** Sebastián Marcello <smarcello@fydsistemas.com.ar>, Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, FyD Sistemas <>  
**Externos:** smarcello@fydsistemas.com.ar  
**Apollo ID:** 6a84aac2b47ab2001c0efefa

---

**Lucio Rojas**: Buenas, ¿Cómo va?

**Sebastián Marcello**: Hola, ¿Qué tal? Buen día.

**Lucio Rojas**: ¿Te estoy escuchando? No sé si estoy escuchando. ¿Vos me escuchás? Sí, perfecto. Ah, yo te escucho también. Buenísimo. Perfecto, perfecto. ¿Cómo están? ¿Todo bien?

**Sebastián Marcello**: ¿Bien, todo tranquilo? Todo bien. ¿Pudiste arreglar con Juan?

**Lucio Rojas**: Juan no podía sumarse, así que me sumo yo y les cuento, pero adelante. Fue suma. Bien, nos acompaña ya más.

**Sebastián Marcello**: Perdón, Nahuel está ahí, lo habilita. Ahí está.

**Lucio Rojas**: ¿Qué haces, Nahuel? ¿Todo bien? ¿La cámara, cómo va? ¿Todo bien'? Todo tranquilo. Nahuel de sistemas, imagino.

**Sebastián Marcello**: Claro, los dos, bueno, los dos somos de FID, de Andrómeda, ¿No? De Aurora.

**Lucio Rojas**: Sí. Yo no sé por qué, perdón, se me.

**Sebastián Marcello**: No hay problema. A ver, nosotros lo que hacemos son. Bueno, tenemos un producto principal que es el sistema de gestión administrativa Andrómeda, y ese lo tienen todos nuestros clientes. Hacemos también, hacemos tableros por nuestra cuenta, pero nos dedicamos, nos piden más, Así que bueno, puede llegar, ¿No?

**Lucio Rojas**: El sistema, perdón, que te está yendo, ¿Está orientado a alguna industria en particular, alguna vertical o un sistema de gestión más?

**Sebastián Marcello**: No, no, es un ERP que puede ir para cualquier actividad. Tenemos muchos que tienen toda la parte de producción, tenemos muy desarrollada la parte de producción, así que bueno, abarca toda la gestión administrativa.

**Lucio Rojas**: Buenísimo. Ahí se sumó Franco, nuestro equipo también de TEA Moto, ¿Cómo te va?

**Sebastián Marcello**: Buen día.

**Lucio Rojas**: Buenas, ¿Cómo va? Bueno, si quieren doy un poco de contexto de nuestro lado, explico el porqué de haberles pedido la reunión y qué me gustaría mostrar. Nosotros en Ceramo somos una startup, una startup, ahora estamos situados en Rosario, tenemos orígenes en Estados Unidos, y lo que hacemos un poco es vincular lo que son los sistemas, los ERP, los sistemas que usan distintas empresas con inteligencia artificial para facilitar lo que es la explotación de datos. Trabajamos agnósticamente al sistema, nos conectamos a SAP, a sistemas más parecidos a Andrómeda, que son ya locales, o a cualquier motor de base de datos, y creamos un contexto y una metadata que les ponemos a distintos modelos para poder explotar esa información. Funcionamos como una suerte de warehouse, armamos un warehouse, también proveemos infraestructura y lo que buscamos hacer es democratizar un poco el acceso a la información directamente contra las tablas de un usuario de negocio, o sea, un usuario tiene un request nuevo de información y se genera sus propias vistas, sus propias tablas y si quiere también sus propios dashboards. Todo desde un chat conversacional. La idea es mostrárselo, no quedarnos sobre lo conceptual. Pero yo te escribí, Seba, porque me parece que esto es algo que puede llegar a potenciar lo que son distintos, la llegada de distintos clientes, sobre todo conectado a lo que es, o vinculado a lo que es aplicaciones de inteligencia artificial. Y nosotros buscamos activamente poder trabajar con empresas que ya tienen sistema y ya tengan clientes para ofrecerlo. Como una posibilidad extra, quiero ir sobre

**Sebastián Marcello**: con los sistemas para acceder a las bases de datos que le dan permiso para acceder a vistas, cómo hacen habitualmente.

**Lucio Rojas**: Sí, un usuario de Vistas a la base de datos

**Sebastián Marcello**: para vista. Eso, como hicimos ahí en Química Moro.

**Lucio Rojas**: Exactamente, sí. Nosotros nos encontramos con un poco de todo, con algunas empresas que ya son dueñas de sus propias bases de datos y lo tienen on premise, y tenemos que hacer. Hay un túnel VPN o alguna conexión, o si no, en algunos casos como el suyo, que ustedes tienen un sistema, las bases de datos son ustedes y tienen los datos de ellos, ¿Hay que conectarse contra el sistema, o tenemos casos de clientes que usan sistemas ya más internacionalizados, como si fuese un SAP, que no podés hablar con SAP, sino que tienes que pegarle una API, conectarte por los protocolos, la documentación, que te da más complicado?

**Sebastián Marcello**: Perfecto.

**Lucio Rojas**: Casi siempre lo resolvemos, pero cuando uno encuentra un sistema que tiene nombre, tiene apellido, que tiene cara, que tiene una base de datos, es mucho más fácil coordinar esa conexión, y por eso está bueno buscarlo, replicar. Así que voy a ir sobre una demo, la idea es que me maten a preguntas, que no sea como un monólogo, así que no tengan ningún problema. Venir frenándome. Perfecto. ¿Están viendo la pantalla? Sí, perfecto. Acá estamos viendo directamente Telamot, que es nuestra plataforma, y estamos viendo el conector que tenemos establecido Andrómeda sobre el cliente Clínica Molón. Yo lo que hice fue pedirle permiso a Juan, quien era que tenía los datos del cliente, para que me deja hacer la demo sobre estos datos. Y en Terabot, cada uno de los clientes que nosotros tenemos, se crea un espacio de trabajo distinto, espacio de trabajo en un workspace, ahora vamos particularmente a la técnica Molón, y dentro del espacio de trabajos se conectan diversas fuentes. Nosotros acá vinculamos más de un sistema, mismo tiempo, y ofrecemos las posibilidades de conectores. Tenemos los conectores a las bases de datos más tradicionales, las POGRE, MySQL, SQL Server, Azure. Nos podemos conectar directamente a un bucket AWS en la nube, a BigQuery, que es la nube de Google, o también estamos desarrollando conectores ya a sistemas en particular como Salesforce, Monday, Airtable, SAP HANA. La idea es que las empresas.

**Sebastián Marcello**: Monday. ¿Pero que sacas de Monday?

**Lucio Rojas**: Toma la tabla de. Yo no estoy en la cuenta en particular, un cliente de hecho. Pero toman la tabla. Supongo que de las transacciones, lo que está registrando ahora no te sirvió.

**Sebastián Marcello**: Es un administrador de proyectos.

**Lucio Rojas**: Sí, sí, sí. Debe traer los proyectos, los clientes que vos descargas, no sé qué guardan las tablas.

**Franco Ferrero**: No, yo creo toda información que tenga de algún proyecto que lo pueda llevar una tabla.

**Lucio Rojas**: En su caso ustedes tenían las tablas sobre SQL Server. Entonces creamos el usuario, las conexiones. Acá hay un equipo de infraestructura, yo estoy más en la parte de cuentas y de negocio, pero coordinó con su equipo de infraestructura y lograron la conexión. Ustedes nos dieron una vista que tenía tres tablas, que eran una tabla de estadísticas, una de resumen contable, estadísticas de

**Sebastián Marcello**: compra, estadísticas de venta y resumen contable.

**Lucio Rojas**: Esto nosotros lo cargamos, lo guardamos en AWS, en un tenant para el cliente en específico. Y esta información se va actualizando a la medida que se actualiza su sistema. Todos los días, no sé si está configurado acá. Sí, todos los días tiene un Chrome que va actualizando las novedades. ¿Nosotros qué hacemos con esto? Creamos un conector a Cloud para poder empezar a trabajar los datos directamente desde un modelo qué hicimos antes. Generamos a nivel columna una descripción de qué significa cada una de las columnas y de qué tipo de datos tiene, para darle esta metadata a Cloud para que pueda trabajar como asesor de datos para el usuario final en sí sobre las tablas reales. Entonces acá nosotros para conectarnos a Cloud lo que hacemos es configurar una URL y un token. No sé si han conectado un MCP alguna vez a lo que es un modelo.

**Sebastián Marcello**: No, nosotros no. Sin saber la parte técnica, nosotros también somos más de el contacto con el cliente negocio.

**Lucio Rojas**: Bien, entonces hago lo acá de cero, es ultra mega sencillo. No sé qué ustedes están usando ahora, alguna.

**Sebastián Marcello**: Esto, Cloud.

**Lucio Rojas**: Les muestro esto que son dos patadas, literalmente borrando que ya tenía para hacerlo de vuelta. Yo vengo acá a personalizar a conectores, genero un conector personalizado nombre Theramot, le pongo la URL que nosotros provisionamos

**Sebastián Marcello**: y

**Lucio Rojas**: le pongo el client. Esto vincula directamente las tablas del sistema con cloud. ¿Qué podemos hacer a partir de vincular las tablas de sistemas con Cloud? Preguntarle abiertamente sobre las tablas que vaya a buscar, un registro, una fila, una columna que haga análisis, que haga tableros, o podemos pedirle que nos genere nuevas vistas. Nuevas vistas que nosotros llamamos tabla go, para poder analizar distinta información del sistema. Así que vamos a empezar a rutearlo y ver cómo funciona, que esta es la parte un poco jugosa de la demo. Hasta acá trate de ir rápido para no embarrarnos, es decir, a Cloud conect, al workspace de UM, acá estoy rooteando, lo estoy diciendo dónde ir dentro de Theramot, que es el workspace de Clínica Mouton, al proyecto. Control gestión y decime qué información puedo extraer. Tablas. Ahora me va a empezar a sugerir distintos tipos de análisis que yo puedo hacer a partir de las tablas que tengo disponible en mi sistema con mis datos. En algunos casos puntuales de otras industrias, hemos hecho mucho lo que es análisis de venta, proyecciones de venta, control de stock, automatizaciones para reabastecimiento de stock en base a una predicción de ventas contra stock actual. Otros equipos la han usado para hacer toda la parte de control y gestión, de analizar las cuentas por cobrar que tienen abiertas, analizar comportamientos de pago de cientos clientes, hacer una proyección de cuántas cuentas por cobrar tengo. Cualquier tipo de análisis que vos hagas partiendo de tu base.

**Sebastián Marcello**: Cuatro tablas y hay tres tablas.

**Lucio Rojas**: Teóricamente tengo una vista creada. Esta es la vista que creó Juan para lo que está haciendo él con Química Molón, que está analizando un caso de uso. Ahora vamos a ver de qué es esa tabla. Entonces estamos viendo acá qué entiende Claude directamente de la tabla que le cargamos en la parte estadística de compras, que dice, Bueno, tengo el detalle de comprobantes de compras, puede sacar información sobre artículos comprados, cantidades y precios, proveedores, línea de marca de producto, depósito, más tengo un resumen contable, que es el libro contable resumido, tenés cuentas contables, códigos y demás, tenés estadísticas de venta, Dice que la tabla más rica es como la FAC, que incluye artículos vendidos, clientes, vendedores, cobradores, condiciones de venta, lista de precio y demás. Y tengo una tabla de resultados que bueno, es la tabla ya construida, la nueva vista que replica la estructura de compras. Y no me dice muy bien que está haciendo Juan acá, pero se lo podríamos preguntar. Esto es la base. Entonces uno de acá le dice, bueno, en base a las tablas que tenés. Qué cruces, Nosotros tablas bot, le decimos a las vistas nuevas que creamos, puedes crear para realizar. Ahora me va a sugerir nuevas vistas que el usuario de negocio las pide directamente así o también acá estamos yendo como un camino mucho más explorativo, vos podés ir a lo puntual, yo quiero ver esto, quiero analizar una métrica en particular de mi negocio, en base a las tablas que tengo, ¿Cómo lo puedo hacer? ¿Acá me va a preguntar, en base a las tablas que tengo, qué puedo hacer? Entonces me dice, bueno, acá podés sacar rentabilidad por artículo, performance de vendedores, análisis de clientes, compras por proveedor, resultado contable mensual, margen por zona geográfica, evolución de precios y de compra contra la venta. ¿Y acá si quieren díganme cuál elegir y hacemos el reporte en vivo y también generamos el

**Sebastián Marcello**: análisis del cliente, decirle bueno? ¿Ya está listo, de qué periodo?

**Lucio Rojas**: Y acá creo que lo va a hacer en base a la información histórica. Nosotros podríamos pedirlo la segmentación, ahí debemos

**Sebastián Marcello**: tener desde el año, no sé, 2015

**Lucio Rojas**: supongo que si estamos pegando a la tabla es la historia que tengan para atrás.

**Sebastián Marcello**: Ah no, no, nos pidieron limitar las fechas me parece.

**Lucio Rojas**: Ah, OK. Acá nosotros vemos dos valores adentro de la herramienta. La primer parte es un poco más esta técnica que te da mucho más velocidad en la creación de tablas y de dashboard si querés. Pero acá es donde ve el valor el usuario final.

**Sebastián Marcello**: Esto no lo pueden hacer los usuarios, quien sea un usuario más avanzado.

**Lucio Rojas**: Claro, hay dos tipos. Nosotros eso lo tenemos mapeado herramienta, tenemos accesos. El usuario final lo único que hace es ver la vista que vos ya creaste y consultar esa tabla, o sea, hacerle preguntas, preguntarle por clientes, preguntarle por algún input más de negocio.

**Sebastián Marcello**: Desde la herramienta.

**Lucio Rojas**: No es la licencia, es lo mismo que hacerle una pregunta a tu cloud.

**Sebastián Marcello**: Ah, es igual.

**Lucio Rojas**: No es que consume, no consume toda esa parte. Entonces vamos a ver lo que hizo acá el conector nuestro fue a Theramo, miró las tablas que tenía, tomó el contexto de metadata que nosotros le pasamos, y ya vio las tablas que tenía, vio qué significaba esas tablas. El modelo entiende cómo se joinean las distintas tablas, entiende los códigos primarios, las claves foreign, todo lo que necesitas para hacerlo join. Y el SQL entiende también el contexto del negocio y en base a eso hace una indicación para crear la vista nueva. Esto es lo que Claude, en base a todo lo que ve, todo lo que le damos, le pasa a Telmo. Telm recibe ese input. Lo vamos a ver por acá. Vamos a verlo en la tabla anterior, que acá Juan lo que hizo. Está bien, acá Juan lo que hizo fue directamente copiar la misma tabla, pero que tiene que ver con. Con desconocimiento de cómo usar herramientas. Vamos a ver acá. ¿Acá qué hicimos? Acá Claude le dijo a Theramo, todo lo que el usuario necesita para la vista nueva que se quiere crear son toda la descripción de requerimientos funcionales, que Cloud lo puede hacer porque tiene todo el contexto y porque está hablando con vos para identificar qué querés. Le da eso a Theramo, lo lee, crea todo el SQL y deja la tabla nueva deployada en nuestra infraestructura. Y esto se actualiza. A medida que se actualiza la fuente, que sería la información del sistema, cabe el linaje. Lo que hizo fue agarrar una de las tablas y le puso un montón de reglas lógicas en sí. Entonces ahora nosotros lo que podemos hacer es consumir esta información desde acá y podemos empezar a preguntar sobre el análisis de cliente instala. ¿Que hicimos para entrencar justo dada la que hicimos? ¿Qué preguntas? ¿Negocio queríamos responder? Yo la verdad no tengo ni idea de los datos ni de qué va el caso de uso, así que le voy a preguntar a Claude a ver qué preguntas podemos hacer y le hacemos alguna para que ustedes vean cómo responden. ¿Cuántos clientes concentran el 80% de la facturación? ¿Qué pasa si perdemos al cliente top 1 o top 3? ¿Cuántos clientes categoría C tenemos? ¿Cuánto facturan en conjunto? ¿Vale la pena mantenerlos? ¿Cuáles son los clientes con mayor margen bruto en pesos? ¿Hay clientes con margen negativo? ¿Qué clientes reciben los mayores descuentos promedio? Hay varias preguntas de negocio, si quieren elegimos una y la hacemos. Justamente

**Sebastián Marcello**: pregúntale eso que está arriba. Si, dependemos, tenemos dependencia. Pocos clientes.

**Lucio Rojas**: Ahí. Sebastián, una pregunta. Vos sos el CEO, ¿Cuál es tu hace? ¿Venís de la parte más de negocio contable, algo así?

**Sebastián Marcello**: A ver. Yo me encargo más de la parte vínculo con la empresa. Soy licenciado en sistemas, pero especializado en la parte contable. Y ayudamos a las empresas junto con Nahuo a mejorar todo el tema de procesos, a darle información a los clientes y a que usen principalmente bien el sistema. Porque muchas veces tiene un millón de de table, pero usan mal el sistema y lo que te muestra el tablero es cualquier cosa

**Lucio Rojas**: más. Toda la parte de data entry decís vos de cara a la información.

**Sebastián Marcello**: No, la parte de data entry, pero por ejemplo ahí en Química Morón del estudio contable, las chicas del estudio contable, por ejemplo, nos explican a nosotros qué es lo que necesitan y nosotros se lo traducimos de alguna manera a los chicos de Kimegamoro, qué es lo que tienen que hacer, cómo usarlo en el sistema. Tratamos de aprovechar lo más posible el sistema dentro de los procesos de las empresas. Usamos Power BI, mostrar estas cosas.

**Lucio Rojas**: Bueno, vamos a ver qué armamos.

**Sebastián Marcello**: A ver qué te contesto.

**Lucio Rojas**: Yo no lo conozco mucho los datos así no hay mucho. Total de clientes 1186.

**Sebastián Marcello**: Hablamos de un periodo acá. Acá no te está diciendo de cuándo ni nada. No,

**Lucio Rojas**: Todo esto se le puede. Acá esto es literalmente clot sobre los datos. Nosotros decimos que la idea es que todas las preguntas, todas las dudas, directamente al LLM y que te respondan base a los datos. Muchas veces sirve para incluso autodevaguearse. La primera pregunta no estaba muy bien. Tiene una tabla sin muchas especificaciones. Puedes ir preguntando hasta que vaya construyendo lo que vos querés.

**Sebastián Marcello**: ¿Puedes subir un cachito que quiero ver lo que te contestó? Te contestó que sí, que tenemos el 79,9%. Porque detecta al consumidor final como un cliente.

**Lucio Rojas**: Claro, eso hay que. Si es una regla de negocio, hay que explicárselo y lo va refinando. Los datos de venta cubren ocho meses de 2026, desde el 2 de enero hasta el.

**Sebastián Marcello**: Lo limitamos para que no sea mucha información, me parece. Creo que nos pidieron eso de Química Morón.

**Lucio Rojas**: Bien. No sé si podemos ir con otra pregunta.

**Sebastián Marcello**: No, no, está bien. A ver. Esto es claumo, lo podemos aprovechar. ¿Cuál es el beneficio que tiene Teramo? Tenemos que salir a venderle esto a los clientes, ¿Que le tenemos que decir? ¿Qué ventaja tienen?

**Lucio Rojas**: ¿Nosotros donde encontramos el valor? ¿No sé, ustedes hoy cómo están permitiendo que el usuario consuma la información del sistema? Si es a partir de tableros de Power BI, a partir de. Por ejemplo, si ellos necesitan información que no está en un tablero y tienen que crearse uno nuevo, ¿Cómo sería el

**Sebastián Marcello**: work que vos decide mucho de la empresa? Hay empresas, te diría la mayoría, que no tienen alguien idóneo como para hacer eso. Entonces nos piden a nosotros constantemente que le hagamos informes, que puede ser Power BI, tablas dinámicas, lo que pueda recibir mejor el usuario. Y eso lo hacemos. Hay un par de chicos en la oficina que se encargan de hacer eso.

**Lucio Rojas**: Bueno, nosotros como te. Nuestra tesis principal para construir herramientas fue esa. Por ahí el usuario de negocio, el usuario final, dependía de un equipo de sistemas para poder generarse su nueva información. Y que muchas veces ese equipo de sistemas siempre lo que es universo pyme hablando, no lo tiene. Entonces tiene que tratar con su externa, tiene que generarse esa información. Y la idea era que con el sistema conectado se lo pueda hacer de modo self service. Después de ir con esa teoría del mercado, nos dimos cuenta que TheRamond no era suficiente por el usuario de negocio, por más que tenga una herramienta que se automatice, tampoco se iba a hacer todos los tableros él solo. Así que entendimos que Teramot puede mucho a ese intermedio, al equipo de sistema que está generando tableros. Entonces poder crearse las vistas con esta practicidad era mucho más fácil. Entonces eso de la parte de creación de nuevos reportes, después de la parte de consumo de información, una vez que vos le dejas las tablas bien armadas, como el modelo de tablas que tiene listo los informes, o la consulta a esas tablas se la puede hacer el usuario final directamente desde Cloud. Hoy en día tenemos varios gerentes de empresas locales de Rosario, conectados a las tablas que el hermoso equipo de sistemas, y preguntando libremente, lo cual es un complemento a ver un dashboard, porque no se reemplazan las cosas. Vos el dashboard que te muestra todos los BIND, lo tenés que ver siempre igual. Poder preguntar información, preguntarle sobre estrategias, preguntarle sobre, bueno, ¿Cómo puedo crecer mis ventas? Puedo empezar a decir, y yo iría por estos clientes, podría ofrecerle el producto B al cliente que te compra solamente producto A, y muy buen comprador de producto a empezar a hablar de los sellings, hacer todo el análisis de costos de la parte control y gestión sirve mucho también. Hemos tenido buenos casos de éxito en equipos de cuentas por cobrar, equipos de finanzas. Entonces el consumo final sin duda un valor agregado, porque es la empresa preguntando directamente con sus datos contra Cloud. Y después que también te agiliza esa parte del BI. Por ejemplo, nosotros acá, yo le pedí directamente un tablero de evolución de ventas mes a mes y me lo armó en menos de un minuto. Supongo que debe estar bastante bien. Pero esto tiene un problema, que es que la información que vos te generas a partir de Cloud no es un snapshot. Va, mide la información, la ventaja del

**Sebastián Marcello**: tablero en ese caso.

**Lucio Rojas**: Entonces si yo ahora le puedo decir, puedes crear. ¿Qué hicimos? Para eso tenemos la funcionalidad de dashboards dentro del propio Theramot. Acá no hay ninguno creado, pero ahora lo vamos a crear. Entonces este tablero que es un snapshot desde Cloud, nosotros le pasamos a Theramot el HTML y lo dejamos ya como tablero y se actualiza mirando las tablas que vos tenés creadas. Entonces acá también ya iríamos más para un lado. Lo que es parecido a Power BI, sigue siendo el usuario no tan de negocio el que se lo hace, pero te creas tu propio tablero. Para eso tenés que armarte la vista. Primero me armar la vista, después me va a hacer el tablero sobre la vista y me lo va a dejar ya creado entera. No te lo puedo mostrar porque tengo que esperar que lo cree. Pero después te da un link.

**Sebastián Marcello**: Perfecto.

**Lucio Rojas**: Que vos ese link te lo llevas al cual, o sea, entras por Google, que es una vista distinta a esta vista administrador, que solamente te muestra el tablero como si fuese Google, una vista de Power BI. Y te da el tablero y te da un agente para preguntar sobre información del tablero.

**Sebastián Marcello**: ¿Ahí cómo es el tema de seguridad? ¿Como seguridad? ¿Seguridad me refiero a ese link le llega a cualquiera y puede entrar?

**Lucio Rojas**: No, no, no. Te respeta el usuario que vos tenés en Teramop creado. Vos tenés que tener, ponele como estamos acá, dentro de un proyecto. Este es el workspace. El Workspace es como cada una de las empresas que tenemos nosotros tiene un workspace. Dentro del workspace tenés distintos proyectos que podés verlo como si fuesen áreas de la empresa. Acá podemos hablar de la parte de ventas, comercial.

**Sebastián Marcello**: Siempre dentro de Química Morón, ¿Verdad?

**Lucio Rojas**: Sí, sí, sí. Esto ya queda. Es siempre a nivel el workspace, a nivel empresa. Después te subdividís por proyectos y entre workspace no se pueden ver si son de usuarios distintos, o sea, son dos universos totalmente distintos. Entonces yo acá a control y gestión le puedo dar acceso a los usuarios de control y gestión. Ponele que vos Eva, sos de control y gestión y te pongo sebastiánicamorón. Com y te adquiero como administrador, como miembro, como usuario de solo lectura. Si vos sos usuario de solo lectura, no te puedes crear distintas tablas o nuevas tablas, solamente puedes consultar las que hay. Si sos miembro puedes crear nuevas tablas, si sos administrador puedes crear y compartir nuevas tablas. Ahora vemos qué significa compartir. Entonces ahora por ejemplo, si yo me creé esta tabla, justo me hizo rápido, que solamente ve cosas de ventas, yo se la comparto al equipo comercial,

**Sebastián Marcello**: Y

**Lucio Rojas**: el equipo comercial solamente va a tener acceso a esa tabla con un usuario de solamente vista. Entonces acá vos tenés un usuario que solamente puede consumir información, todo esto de lo conceptual. Después cuando vos lo llevas a cloud y vinculas el cloud con el téram de ese usuario, solamente va a poder ver esto, no va a poder ver todas las otras tablas que existen dentro del proyecto. Así es como trabajamos la gobernanza. Entonces después si vos estás agregado a un proyecto que tiene creado un dashboard que se crea a nivel proyecto, ya está hecho, Perdón, yo le voy a pedir que me cree el dashboard y me lo va a quedar dentro de este proyecto acá, donde en un ratito ya vamos a ver. Este proyecto solamente va a tener acceso a las personas que yo se las di, con el rol que yo le di. Entonces después se va a crear un link que vos para verlo tenés que loguearte, porque es un link de Teleamot, es como si fuese Teleamot en otra pestaña. Entonces vos cuando te logueas te va a copiar los roles y los permisos que tenías dentro de Telemot, y solamente te va a mostrar los dashboards que vos podés ver por cómo está configurada la. Entonces tus dos preguntas tenemos todo lo que es gestión de usuarios, roles, accesos. Después para ver un link y un dashboard de la empresa, tenés que loggearte. Y después más a términos de seguridad de qué hacemos con los datos y cómo te aseguramos a vos que no van a estarlos actuando vuelda board por Internet, que no nos fácil y demás. Yéndonos a palabras poco técnicas, certificamos SOC, que es lo que es norma de ciberseguridad como estándar a nivel global, y cada seis meses nos sometemos a auditoría para volver a certificar ese estándar. Esto es lo que nos han pedido empresas internacionales para poder trabajar con ellos. Y bueno, eso nos dio un poco.

**Sebastián Marcello**: Antes decías que trabajan en Estados Unidos ¿También tienen clientes o la empresa está allá?

**Lucio Rojas**: Las dos. Tenemos una ETL s y tenemos clientes allá. Ahora estamos trabajando con algunos clientes de afuera. Ahora uno de los clientes que tenemos a nivel internacional, trabajamos con Coca, con Coca Cola, con Johnson Johnson, que es de la parte farmacéutica. Trabajamos con industrias de retail, con Ave Mauri, que es británica, no es estadounidense, pero es una cadena de comidas. Llevado a lo que es retail, más lo que nosotros conocemos, son los que hacen los cubitos de levadura de calza. Esa empresa es Calza, que es de Ave Mauri, no la conocía. Vamos a ver qué está haciendo con el dashboard. Está pidiendo permiso para crear el dashboard. Bueno, y ahora me crea el Azure y me lo deja ya guardado dentro de T. Principal. ¿Le gusta cómo quedó? Esta feature de dashboards es nueva, la sacamos hace poco porque me hicieron muchas veces la pregunta de bueno, ¿Cómo hago para consumir todo esto? Antes teníamos otra respuesta que sigue estando, que es nos conectamos a Power BI nosotros a partir de un export por ODBC, te copia todas las tablas que vos tenés, todos los reportes nuevos que armaste en Power BI, y desde ahí te puedes construir tu dashboard o le puedes pegar a las tablas por API también. Tenemos la API acá creada, tenemos la documentación ahí lo puedes usar para crearte vos alguna página web o algo.

**Sebastián Marcello**: Yo uso mucho los resultados.

**Lucio Rojas**: Esto está bien resultado, a ver si me crea, Pero bueno, después está.

**Sebastián Marcello**: Vos estás en la parte comercial, ¿Verdad?

**Lucio Rojas**: No, no, yo lo que hago es ir a las empresas más hacer customer success. Por ahí me encargo también un poco de lo que decías vos. Use la herramienta de ver qué automatización le podemos hacer. Juego mucho con n automatizaciones de workflow, de MA, partiendo de los datos. Esto después uso mucho lo de.

**Sebastián Marcello**: Tenemos a Nahuel que es especialista en n.

**Lucio Rojas**: Ahí Nahuel lo que podés hacer es por API, le pegas a las tablas estas y mira todos los días las tablas y te creas el workflow sobre la consulta a la Go se conecta directamente a theramot, entonces si n lo conectas a Telamot y te ve las tablas que vos creaste. A ver si me dice que está listo el dashboard, vamos a ver si me está mintiendo a ver qué hizo. Segundo, voy abriendo acá el link para que lo vean. Te voy a abrir una pestaña incógnita, Te va a pedir iniciar sesión como recién voy a continuar con Google, esto es lo que vos me decías, Ir de vuelta. ¿Hola, si están viendo una incógnita, entro en su sesión, como inicié? ¿Como inicio cuando entro a Theamo? Voy a mi cuenta. No más. El org puede ser más incógnito. Esto lo hace una sola vez y después ya te muestra el dashboard directamente. Y acá vos ya entras directamente a la vista de dashboards. Tendría que cargar o está actualmente acot. Acá no anduvo cómo parece que no

**Franco Ferrero**: se creó bien la Go, porque a veces pasa eso,

**Lucio Rojas**: estamos entre sistemas.

**Sebastián Marcello**: Relájate, relájate porque estás. No te preocupes.

**Lucio Rojas**: ¿Bueno, pero es un poco el concepto, no? Estas cosas a veces fallan como.

**Sebastián Marcello**: A ver, no entiendo cómo es la relación de Juan, el estudio contable con Química Morón, por ejemplo, y ustedes, porque creo que sería así similar la relación nuestra. Juan lleva a sus clientes a ustedes, ¿Es así?

**Lucio Rojas**: No, no, no, Juan es independiente, es consultor, nosotros no tenemos ninguna vinculación con Juan, eligió usar Telamo para poder darle un servicio a su cliente.

**Sebastián Marcello**: Me refiero a Juan lleva a sus clientes a ustedes, o sea, ¿Cómo llegó química morón a ustedes?

**Lucio Rojas**: Sí, por Juan

**Sebastián Marcello**: es como tendríamos que llegar nosotros. ¿Cuál es la parte comercial? ¿Cómo sería la forma comercial?

**Lucio Rojas**: Perfecto, nosotros somos una herramienta eso para arrancar, no prestamos servicios, no prestamos servicios de consultoría, Esto es un SaaS aparte que hago yo de Castlebox Access, porque nosotros tenemos algunas cuentas que me interesa expandir, nada más. Te amo. Está publicado, tiene su pricing, su pricing corresponde al uso, a la cantidad de usuarios, cantidad de tablas o vistas nuevas que generas, cantidad de GB de almacenamiento, procesamiento y quien contrate theamot para nosotros es un poco indiferente. Si a nosotros nos contrata Química Molón y Química Molón quiere conectar sus datos y sus datos están en Andrómeda y tiene todos los permisos quiere conectar eso para explotarlo desde la Un caso válido. Otro caso puede ser que Andrómeda traiga a sus clientes y lo conecta a Theramo, pague la licencia y después lo cobre como si querés como módulo nuevo, como módulo de AI, y nos paga 400 nosotros y le cobra 800 al cliente también nos da igual, nosotros somos una plataforma que tiene un plugin, es un poco las reglas del juego. Y después hay distintos casos de uso. También hay consultoría, muchos que son consultores de datos, que usan TeamOT para dar su servicio de consultoría de datos y también consiguen conectarse a las tablas de los sistemas de las empresas y les hacen informe, les hacen análisis y demás usando cloud las tablas. Son combinaciones, un poco de todo. Nosotros como herramienta hoy en día estamos pensando en usuarios que son de control y gestión, que trabajan sobre SAP, en empresas más enterprise, y estamos haciendo todo el marketing, todos los esfuerzos para allá. Lo que no quita que la herramienta sirva para muchos otros casos, que son los que por ahí estamos charlando acá. Yo que había visto que te escribí,

**Sebastián Marcello**: en realidad Franco quiere hablar, termina de

**Franco Ferrero**: terminar y después aclaro algo

**Lucio Rojas**: Franco. Sí, está en la parte comercial. Yo había visto que nada, que el caso de Juan me pareció bueno, vi que ustedes tenían un sistema y que seguramente tenían clientes y que por ahí les les podría llegar a interesar usar Theramo para ofrecer un servicio nuevo a sus clientes. Ese servicio puede ser usen Tegamot, o puede ser que damos acceso a Cloud conectado a Andrómeda. Si Theramot está en el medio y ellos no se enteran tampoco. En el caso era más como decir, bueno, Poli está bueno, Poli le sirve, Poli no sirve. Y podemos charlar

**Franco Ferrero**: también un poco lo que decían de cómo sería capaz el esquema también nosotros contamos con la posibilidad de que ustedes lo usen como marca blanca, digamos que no tenga que ser Theramo, sino que ustedes se lo ofrezcan a sus clientes como parte del servicio suyo, y después nosotros entre ustedes y nosotros armamos el esquema del pricing. Pero se puede trabajar con marca blanca y que ustedes digan, che, esta parte de nuestro servicio, sin incluir nuestro nombre, digamos, nuestra marca.

**Sebastián Marcello**: Está clarísimo, está bien. Por eso eso es lo que quería entender, a ver si yo tenía que adquirir Theramo y vendérselo a mis clientes como un producto nuestro, o si yo los vinculaba con nuestros clientes.

**Franco Ferrero**: A ver, tenemos las dos posibilidades. Capaz hay veces que capaz hay clientes que prefieren usarlo con marca blanca, con decir, che, esto es parte de lo que yo te ofrezco a vos como cliente. Y no tener que decirle, bueno, si

**Sebastián Marcello**: querés puedes usar tela, moté. En el caso de Química Morón, ni saben que ustedes existen, yo creo. No, no creo que ni saben quiénes son. El servicio se lo debe estar dando Juan para ellos. OK. Bueno. El pelo. ¿Dónde tengo información como para compartir al resto de los chicos de mi oficina? ¿Usted me puede mandar algo como para mostrarles, para que vean de qué se

**Lucio Rojas**: trata, un poco mostrar una demo, un poco más técnico?

**Sebastián Marcello**: No sé si una demo, quién sabe, puedo sacar, no sé, la página que tiene, las cosas que pueda hacer. Esto, lo que vimos recién,

**Lucio Rojas**: ahí preparamos. Si quería un poco de información, Seba, para.

**Sebastián Marcello**: Sí, somos varios y quisiera compartirlo a ver con cada área, a ver cómo nos pueden ayudar.

**Lucio Rojas**: Bien. Otra cosa que está a disposición es que nosotros tenemos un plan free donde pueden probar y sin ningún problema, sin ningún límite, si quieren compartirnos algunas tablas, algunos CSV, algo que quieran analizar, se puede hacer. Y hasta incluso podrían conectar algún módulo, así como hicieron con Química Molón, también cabe dentro del plan free. Creo que incluso Juan es con un plan free. Así que eso también está ahí a disposición. Pero todo lo que sea información y

**Sebastián Marcello**: demás, dentro de la misma cuenta que yo les contrate a ustedes, ahí tendría todos mis clientes.

**Lucio Rojas**: ¿Serían todos proyectos distintos, todos Workspace distintos? Si. Vos estás entrando como Andromeda. Sí.

**Sebastián Marcello**: OK, bien, perfecto.

**Lucio Rojas**: Eso nosotros lo tenemos separado a nivel infraestructura y demás. Pero bueno, una pregunta más de mi lado. ¿Cómo lo ven? ¿Creen que les puede ser útil? ¿Qué feedback tienen? ¿Puede ser que no también nosotros nos sienta más Charlotte?

**Sebastián Marcello**: No, no, a ver, para mí es súper interesante. Para mí es súper interesante esto. No tengo claro cómo lo implementaría. Siempre todos nuestros desarrollos son nuestros. En realidad nunca contratamos así herramientas de terceros que estamos abiertos a hacerlo por los cambios que hay. Es imposible correr siempre atrás de todos los cambios. Pero a ver, puede funcionar. No tengo ni idea. El tema costos, ni idea. Y vi tres numeritos, pero yo creo que ninguno de los números. Eso sería como para nosotros sería dependiendo la cantidad de clientes que integre por los usuarios. Vi que las variables, esto es por

**Lucio Rojas**: cliente, si querés multiplicarlo cómo. Cómo es por cliente. Si querés multiplicarlo a nivel. Claro, por ejemplo, yo te explico si querés, cómo yo lo había mapeado en mi cabeza, no sé, ustedes tienen, pongo el caso Clínica Morón, que yo imaginé como puede decir Clínica Morón. Buenos días. Desde ahora tenemos la posibilidad de lo que es información, poder explotarlo desde Andrómeda a partir de un modelo como si fuese Clock, puede hacerle preguntas a tus datos, podemos hacer reporte y demás. Eso es un módulo nuevo que sale 500 dólares más por mes, tiramos 400 y o las 500 del cliente y le das Telamo si querés disfrazado a través de una UI tuya que lo vinculas para eso es un ejemplo. Otro ejemplo es decirle bueno, a partir de ahora ofrecemos servicios. De información, reportería, creación de tableros y demás y lo usas como herramienta interna para ir un poco más rápido y vos te pagas una licencia y después no se lo traslada directo al cliente como un afiche nuevo. Eso era un poco las dos.

**Sebastián Marcello**: Como el servicio de cloud ya tenemos que tener, o Teramot usa el suyo.

**Lucio Rojas**: No, no se conecta a un cloud

**Sebastián Marcello**: del cliente, hay que vincularlo bien. Que tenés chat GPT también tiene que ser cloud. Puede ser cualquier IA, cualquiera menos Gemini,

**Lucio Rojas**: porque Gemini no acepta MCP.

**Sebastián Marcello**: OK,

**Lucio Rojas**: si querés tenerlo en mente, para mí es como una plataforma en estos casos es la forma que vos tenés de decirle a tus clientes che, ahora puedes explotar todo con IA

**Franco Ferrero**: igual Sebastián, también un poco a ver, el tema del pricing, yo creo que también es algo que al ser algo más a medida lo podemos ir charlando y hacer algo como que nos sirva a los dos eso. Después si seguimos avanzando se puede coordinar una reunión con el otro, con mi jefe que es el jefe del área comercial y se puede armar algún tipo de arreglo como para que nos sirva a los dos.

**Sebastián Marcello**: ¿Su cartera de cliente, más o menos qué cantidades tiene idea?

**Lucio Rojas**: Sí, ahora estamos en lo que es cuentas BB, lo que es cantidad de usuarios en el orden de 300. Llegamos con el producto hace poco, somos hace un año no menos, desde marzo que está, digamos así como lo viste vos.

**Sebastián Marcello**: Cuenta es Química Morón, es una cuenta, ahí.

**Lucio Rojas**: Tiene tres usuarios.

**Sebastián Marcello**: Sí, sí, seguro. Está bien. Nahue, ¿Alguna pregunta tenés para hacerle a los chicos que tienen ellos? No, la tranquilidad que tienen, ellos viven en Rosario, nada que ver con nosotros. Nosotros somos unos alterados.

**Franco Ferrero**: Franco es de Yo soy Buenos Aires.

**Sebastián Marcello**: Ah, vos estás acá, yo estoy acá. Descartado, Lucio. ¿Viste que tranquilidad?

**Franco Ferrero**: Yo también lo noto.

**Lucio Rojas**: Honestamente, hoy estoy. No sé qué me pasa, estoy como con dos cambios abajo, no sé por qué. Estoy un poquito pausado.

**Sebastián Marcello**: Si me escucharon muy lento, mantenelo, eso va bien.

**Lucio Rojas**: OK.

**Sebastián Marcello**: Trabajamos con una empresa, Nahuel, los de SIG son de Rosario también, son repachorras, re tranquilos. Es bárbaro

**Lucio Rojas**: para hablar. Tengo una pausita más, pero bueno, después también me muevo rápido en lo que multitasking, eso sí lo llevo. Bueno chicos,

**Sebastián Marcello**: compartirme lo que tengas sin hacer mucho esfuerzo, lo que tengas, compartirme, así yo puedo mostrar un poco de qué se trata y en todo caso los vuelvo a hinchar y vemos de nuevo.

**Lucio Rojas**: Buenísimo.

**Sebastián Marcello**: Bueno, hay que digerirlo esto. Esto no es de un día para otro, lo tenemos que digerir.

**Lucio Rojas**: Piénsalo, piensa si les gusta, si no, como lo quieren. Y a nosotros nos interesa que salga, la verdad. Y si no sale, también nos interesa saber por qué, ¿No? Porque nos sirve mucho para el producto. Así que bueno chicos, muchas gracias por el tiempo.

**Sebastián Marcello**: No, gracias Franco.

**Franco Ferrero**: Abrazo.
