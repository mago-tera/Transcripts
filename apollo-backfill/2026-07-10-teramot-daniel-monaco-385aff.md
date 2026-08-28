# Teramot (Daniel Mónaco)

**Fecha:** 2026-07-10T18:02:16.981+00:00  
**Duración:** ~63 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Daniel Mónaco <daniel.monaco@abmaurila.com>  
**Externos:** daniel.monaco@abmaurila.com  
**Apollo ID:** 6a51429c80f1e5000c385aff

---

**Lucio Rojas**: Hola Daniel, ¿Cómo estás?

**Daniel Mónaco**: Buenas Lucio, un gusto.

**Lucio Rojas**: Todo bien, todo bien, un gusto igualmente. Confirmame si me escuchas bien ahí.

**Daniel Mónaco**: Te escucho bien, buenísimo.

**Lucio Rojas**: Bueno, no sé si estamos en feriado o no termino de entender.

**Daniel Mónaco**: Hoy es raro, es un viernes con aire de lunes, porque venimos de un

**Lucio Rojas**: feriado y termina la semana física día RA, pero bueno. Bueno Daniel, un poco de contexto de la reunión. A mí me pidió Gabriel Puertas, que mi jefe que lo reemplaza en la reunión, porque él no pudo llegar por un tema de logística interna, y me dijo que vos estás empezando a trabajar en Calza y que tenía que ayudarte a introducirte un poco en todo lo que era el tema de Thermo. Así que entiendo que un poco esa es la macro. ¿Si querés contarme un poco de vos, hace cuánto arrancaste, sabes, de Telamot? Me sirve mucho.

**Daniel Mónaco**: Mirá, estuve ahora, estuve chusmeando un poco el sitio, viendo algunos vídeos en YouTube. Estaba justo viendo uno de Gabriel que dice cómo armar un reporte de ventas con Cloud más Teramot. Estaba viendo ese. Bueno, te comento quién soy yo. Arranqué justo, tengo una semana ahí en AVE Mauri, en Calza, estoy como ahí como Data Manager, como líder BI, y entonces bueno, voy a estar haciéndome cargo de toda la parte de la capa de datos, de explotación de datos de la empresa, más que nada en lo que es liderar, gestionar las herramientas y bueno, estar ahí atento a lo que necesitan los usuarios.

**Lucio Rojas**: Buenísimo.

**Daniel Mónaco**: Bueno, estuve chusmeando Teramot, sí, estuve ya sacando algunos apuntes de cómo trabaja y bueno, ahí ya. Y lo que no sé que no vi todavía son las POC o qué empezaron a hacer acá con Calza, eso no lo vi.

**Lucio Rojas**: Bueno, yo de mi lado estoy en la parte más de Customer Success y un poco de análisis de producto en Tetamo. Mi background no es súper técnico, yo soy más de. Estudié negocios digitales, obviamente dentro de lo que es el producto me puedo meter en tecnicismos, así que no soy el Account Manager particularmente de Calza, es más Gabrielli, pero ahora estoy cubriéndolo y la idea es poder hacer un repaso con vos en vivo de la herramienta. El caso uso lo podemos repasar juntos, porque preguntándole a Claude nos va a dar un montón de insights, ver qué se hizo y sobre todo ver qué se puede hacer. Me interesa que lo directamente ya desde, si podes vos desde tu máquina, no sé si tenés una cuenta de Cloud, presentes la pantalla y yo te voy guiando y ya dejar todo configurado como para que vos puedas meter.

**Daniel Mónaco**: No, cuenta de Cloud, no tengo.

**Lucio Rojas**: Cloud sí. ¿Qué otra

**Daniel Mónaco**: yo venía usando? Bueno, pero una cuenta personal de la empresa anterior, Copilot más que nada, pero bueno, no trabajé con Gemini y con Copilot, son las dos que más que nada uso.

**Lucio Rojas**: OK. ¿Y dentro de Mauri que usan?

**Daniel Mónaco**: ¿Una propia? Tiene una que es propia, no sé si es de OpenAI, me parece que es de Open, que está basado con chat CBT, todavía no entré, pero hay una propia de la empresa, no sé después si tiene un vínculo ahí, tiene ya una licencia propia o capaz con alguna de las conocidas y paga el servicio, o es una que levantaron un servidor acá de la compañía, no lo sé.

**Lucio Rojas**: Ahí no sé cómo lo están usando internamente dentro de ustedes y quien está probando la herramienta lo está haciendo con alguna cuenta de plot que que tomó.

**Daniel Mónaco**: Pero si vos, bueno, ustedes ya estuvieron ya con algún usuario clave haciendo pruebas, bueno ya seguramente y con Cloud debe tener esa persona ya una cuenta de cloud que habrá sacado seguramente.

**Lucio Rojas**: Es independiente a la demo. Yo para empezar entonces lo hacemos desde mi compu y te voy haciendo un repaso y después nos conectamos al modelo que querías ver también para qué sirve y qué capacidades tiene. Y somos un poco agnósticos modelo, nosotros exponemos un MCP y se puede distintos LLMs, Cloud, chat, CPT, un interno, no hay problema, pero solemos usar Cloud porque nos gusta la platform que tiene.

**Daniel Mónaco**: Y hay una pregunta, entró en detalle de cómo brindarían el servicio acá en Calza, Si es como llave en mano. Si es directamente ustedes se hacen cargo de todo lo que es la orquestación, la parte de, no sé, el data lake house, Si también el entorno, hay para todo lo que se genere en la capa de la arquitectura. ¿Medallion va a estar a cargo acá de la empresa o ustedes van a brindar todo este servicio donde estar guardando ya el modelo dimensional

**Lucio Rojas**: ahí Teramot como default funciona como SaaS, donde nosotros a cambio de una licencia nos hacemos un poco cargo de todo, tanto desde el alojamiento de los datos en árbol BBS, puede ser nuestro tenant que ya ofrecemos dentro de la licencia, o que ustedes configuren su tenant propio adentro de AW? Si nosotros hacemos cargo de la orquestación, pero en un principio, como está la herramienta, todo termina viviendo alojado por nosotros. Ustedes nada más hacen cargo de la licencia y bueno, en caso de que eso termine, se borra toda la información. ¿Y? ¿Todavía no lo hablaron Eso, eso honestamente, quizás Juan y Gabriel lo hablaron? Yo sé que tuvieron muchas charlas técnicas con el equipo de Mauri, pero yo no tengo el detalle.

**Daniel Mónaco**: Si ya lo hablaron como lo quiero hacer, después averiguo. Perfecto.

**Lucio Rojas**: Si no, después lo averiguamos. Pues justo están, no sé por qué se fueron todos de vacaciones esta semana, estamos con el nido vacío.

**Daniel Mónaco**: Justo vacaciones de invierno de los chicos.

**Lucio Rojas**: Vacaciones de invierno. Claro. Yo todavía no soy padre, así que creo, así que me o no lo sabes Claro, o no lo sé. Así que me escapa ese tema. Bueno, voy a hacer un repaso por la herramienta. Daniel anda haciéndome preguntas, te parezca y querías ver un poco las funcionalidades. En un principio, nosotros lo que hacemos desde theramop es, si se quiere automatizar el proceso de generación de reportes a partir de modelos de inteligencia artificial y brindamos una fuente de conector seguro entre la base de datos y los LL, lo que hacemos en el proceso es tomar las fuentes de datos, múltiples fuentes, pueden venir de SAP, pueden venir archivos de Excel, pueden venir de algún ERP distinto de organización, hacernos de toda esa información en nuestro tener AWS y hacer un descubrimiento del esquema. Entonces nosotros le proveemos a los modelos nuestros del elementos, esquemas de las tablas, las columnas, corremos un proceso de sanitización y estandarización de esos datos, outliers, modelado, problemas de fechas en distintos sistemas, para ya tener toda la información lista para cruzarlo. Y a partir de descubrir la intención de negocio con el usuario final, con un DLM de por medio, poder identificar cuál es el reporte nuevo que se necesita. La herramienta con todos los datos ya mapeados, estandarizados, puede inferir cuáles son los los joins, las relaciones entre las tablas y genera la capa gold para consumir esa información. Todo eso desde cloud. Entonces, no solamente te automatiza la estandarización, la limpieza de los datos, la creación del nuevo ETL, sino que también ayuda mucho con el consumo. Y ahí creo que es donde está encontrando valor. Calza en hacer preguntas como por ejemplo, estuve viendo, están evaluando cuál es la relación entre lo que le van aumentando los proveedores y la inflación, para saber si hay aumentos que están por encima de la inflación, para entender cómo los proveedores están aumentando, están viendo cuáles son los centros y costos más altos que tienen toda la

**Daniel Mónaco**: ese punto de la inflación. Suponete que no tenés información del IPC, por ejemplo. Ahí se configura el tema de además lo que tenés en el Lake House, quiero buscar información externa. Eso que se configura, ir a buscar información de Internet para recopilar datos o tiene que estar ya, voy a hablar de inflación, tengo que tener ya una tabla interna con datos de la inflación.

**Lucio Rojas**: Ahí cargas la tabla, ellos lo que hicieron que descargar la tabla. ¿Telamot funciona como warehouse, carga una tabla

**Daniel Mónaco**: de Excel, información externa, no te da la posibilidad en algún momento buscar información?

**Lucio Rojas**: Sí, podés buscar la información. Esto separa Cloud de Telamo. Cuando vos estás consultando tablas desde Cloud, podés comparar esa información con un IPC que lo busque Cloud en Internet, pero no tenés la información como tabla para generar un análisis, hacer un shun, comparas

**Daniel Mónaco**: con justo quiero ver con el índice IPC del mes pasado y no tenés el dato de IPC. Entonces tenés que cruzar tus datos contra ese indicador.

**Lucio Rojas**: Sí se puede cruzar contra lo que está en Internet, pero desde Clock, no a nivel tabla, no puedes crear una

**Daniel Mónaco**: tabla nueva que use y eso vos lo controlas, puede decir no, no quiero que vaya a buscar nada, no darle la posibilidad de usuario que vaya a buscar algo externo, que toda la información la saque solamente de la capa Gol que tenés que no vas a buscar externamente. Se puede configurar eso.

**Lucio Rojas**: Hay que separar dos cuestiones, que es el uso de Téramo con el consumo de Téramo desde Cloud, lo que es el uso de Tlamo. Vos siempre vas a trabajar con la información que tengas dentro de tu warehouse que armaste en Telamot, donde vos podés conectarte a tus tablas de SAP, conectarte a algún warehouse que ya tengas armado y cargar nuevas tablas, como por ejemplo el IPC del último mes, para vincularlas entre todos. Eso es lo que termina siendo remoto. Después cuando vos lo estás consumiendo desde Cloud, lo que podés hacer es consumir esa información que te da Teramot, que cargaste en Teramot, las tablas Gold que generaste. Pero a su vez Clot por ser Cloud o cualquier EDM CPT por ejemplo, puede consultar información externa, porque ahí ya estamos hablando de lo que es el consumo de la herramienta con un LL. Entonces eso nosotros no podemos por ejemplo decir usa contra Internet, tenés que ahí más hablar de lo que es el uso del EDM, o cambiar el modelo o usar un modelo propio que está pronteado con las instrucciones que vos querés. Eso son dos cuestiones.

**Daniel Mónaco**: Y pregunta y todo el consumo, suponete que todo lo que gastes de consulta, el usuario empieza a hacer muchas consultas, todo lo que es consumo de tokens, ¿Eso cómo lo administras? Una cuota de, no sé, tokens, Bueno, acá al sale doy, no sé, por decir, algún millón de tokens por mes. ¿Eso como lo administras hoy? Y de repente un día, mira, excedió, excedió la cantidad, y ahí el usuario no puede preguntar más porque se quedó sin token justo el modelo que estás usando.

**Lucio Rojas**: Bien, ahí también es separar un poco la. En un momento hasta casi que parecimos broker de un LLM, porque nosotros estamos llegando al consumo a Cloud HTTP. Tenemos una herramienta interna nuestra acá dentro de Telamot, Que es el agente donde vos podés consultar información con un modelo interno, pero está en una versión bastante beta, Yo lo tengo desde mi cuenta y puedo consultar todos los workspace que tengo abierto, pero es un elemento interno donde nosotros creamos la API de consumo de información y ahí puedes consultar casi que libremente. Este modelo lo que tiene que es un modelo bastante liviano, es un haiku de cloud y no tiene mucha capacidad para preguntar. Pero bueno, acá los tokens están a cargo nuestro y están dentro de la licencia. Es un punto a favor de luz. Después si vos lo consumís de Cloud, nosotros trabajamos mucho para que el MCP, las tools que le damos al MCP para consumirlos en EDM, optimicen los tokens, traten de hacer la consulta la más eficiente posible, pero ya depende de la cuenta que vos estés comprando de flota a nivel enterprise, donde por ejemplo, le das licencia a tus empleados, tus consumidores, tu suyo final, y se quedan sin los tokens de la sesión y tienen que esperar hasta que se renueve esa opción para volver a consultarlo. Eso ya funciona como cualquier modelo. Y si no, nosotros podemos exponer las capas gold que creamos para que vos las consumas desde un modelo que corras en tus servidores propios. Entonces ahí el consumo de tokens ya queda a tu Ethereum a tu disposición. Volviendo un poco a la herramienta, un repaso general y rápido que hago. Vos podés conectar distintas fuentes, puedes conectar una Postgre, una mysql, SQL Server, puedes cargar archivos directamente un s, que entiendo que es lo que están haciendo ahora, están bajando los archivos de SAP y están cargando un s para poder consumirlos de Teramot, o se puede habilitar el conector directamente a SAP HANA. Esto también es un proceso bastante más manual, no es tan estandarizable, porque siempre depende de cómo es la relación entre SAP y nuestro cliente, y nosotros somos tres partes, pero se puede crear este conector a SAP y ya hacer un refresh directamente de los datos desde ahí. Después vos podés ver todas las tablas que cargaste en distintas capas. La capa silver son esas mismas tablas que vienen de tu sistema, con un proceso de personalización y normalización, que lo podés ver desde tallas de creación, las transformaciones que hacen, por ejemplo, hace solamente un tricast para una columna de la tabla, hay tablas donde hace más, tablas donde hace menos. Por ahora esto es un poco caja negra, que nuestros agentes autónomos eligen dónde hacer esas transformaciones y dónde no, para un roadmap. Dentro de muy poco vos vas a poder tener un human in the loop que decida también junto con nuestros agentes, qué transformaciones hacer y cuáles no. Toda esta información de las distintas tablas que se generan, Telamo convierte a Metadata y los expone en MCP. Acá en este MCP vos podés conectar distintos modelos, chatgpt, Cloud Code, Cloud Desktop PC también nos jugamos con el Clopilot a Gemini todavía no, porque Gemini es bastante restrictivo con las conexiones MCP, pero casi siempre sigue, hay algún conector que no está acá, podemos encontrar la vuelta en el equipo de desarrollo siempre que es a pedido del cliente.

**Daniel Mónaco**: ¿Entonces hay la posibilidad de los conectores de IA se la dan acá al cliente o ustedes dicen, bueno, no vemos que mejor usen ustedes Cloud, por decir algo?

**Lucio Rojas**: No, nosotros dejamos a libre dirección. Yo la estoy basándome sobre Cloud porque es un poco lo que entendemos que performa mejor para las demos, un poco más sorprendente el nivel de análisis que tiene. Y Claude, el padre de MCP, facilita mucho las conexiones. ChatGPT también lo hace bastante bien, lo que es la creación de mcps. Después ya más en Copilot, es un poco más complicado pero también se puede conectar Gemini con Google están atrasados en el tema MCP, hicieron la plataforma aparte que se llama Antigravity para poder conectar mcps a Gemini. Puede que sea como un bypass y si no, exponemos todas las tablas a modo de endpoint para que un modelo ustedes propio les pueda pegar y consultarlo. Eso lo hemos hecho con otros clientes también a modo custom. Pero la idea es, trae tu propio y lo conectas a Teja y. Y nosotros, si ya no está dentro de lo que tenemos como producto, lo llevamos a una conversación con el equipo técnico y se configura el problema. Eso.

**Daniel Mónaco**: ¿Se habló algo de usar el propio modelo de lenguaje?

**Lucio Rojas**: Sí, creo que sí. Creo que la idea iría con ustedes, pero creo no te. Sobre todo por el consumo de tokens, porque creo que el uso que le querían dar era mejor tener un Volta. Entonces uno conecta al MCP como conector, te aparece Teramot, tenés que vincular la URL y el client ID que exponemos nosotros. Y ya desde tomarlo, cualquier consulta, decirle. Y haceme una descripción lenguaje natural. De cada una de las fuentes vinculadas.

**Daniel Mónaco**: ¿Te quedó mal? ¿Fuentes, cómo te querés decir? Te quedó mal.

**Lucio Rojas**: Gracias.

**Daniel Mónaco**: Capaz que te lo toma igual, interpreta que está bien, que se le pone.

**Lucio Rojas**: Sí, sí, entiende perfecto. Por eso yo por eso, Desde que mis capacidades bajaron 100%, porque es como que me entiende tanto que.

**Daniel Mónaco**: Sí, sí, sí. Yo muchas veces escribo rápido, le escribí mal y no lo interpretó bien.

**Lucio Rojas**: Sí, sí, generadas. Y para. Dejarlo que tenga un rato acá va a llamar el conector, capaz que nos pida autentificarnos, capaz que no. Nosotros le ponemos varias tools que vas a ver que la va llamando en momentos.

**Daniel Mónaco**: Lucio consulta todo este proyecto de calza, se puede ver ahí ya tienen como disponible o compartido el código, los scriptsql que va generando para la extracción, para la transformación de los datos.

**Lucio Rojas**: Sí, eso se puede ver. Siempre es todo audible. Por ejemplo acá he creado una Gol de evolución de 24. 26 creo que son los años por proveedor. Acá te muestra la tabla que creamos. Esta es una tabla gold y puedes ver los detalles de creación.

**Daniel Mónaco**: Para poder ver el proyecto.

**Lucio Rojas**: Sí, sí, ya te agrego.

**Daniel Mónaco**: Si no averiguá y después me das. Me agregas. Primero averiguás y me agregas.

**Lucio Rojas**: No, no, yo te agrego yo puedo agregar. Acá te dice qué tablas toma como input. La tabla de resultados explica el origen, que es la descripción o el requerimiento funcional que levanta el LLM de interacción con el usuario. Después esto lo inyecta de nuevo dentro de la plataforma y nuestros modelos internos de Teramot entienden este origen y hacen la query SQL. Y esto lo deja deployado en AWS y se actualiza siempre a medida que se actualizan las fuentes información. Después se puede volver a consumir desde acá. Ya queda hecho. Esto es un ETL cada vez que te usas la fuente actual. Y ya que te digo, Hola, decime tu usuario

**Daniel Mónaco**: que te doy el mail. Sí, Daniel Mónaco. Mauri la

**Lucio Rojas**: mauri ilea

**Daniel Mónaco**: así, sí, así.

**Lucio Rojas**: Yo acá tengo el problema de que con mi cuenta de Teramot me criaron el conector a los tres ambientes. Acá tengo staging MCP y se me pierde el MCP. Fíjate que arrancó yendo a dev, me parece. Acá vio el proyecto y va a listar. Vio el workspace, perdón, y va a listar los proyectos dentro del workspace. Ustedes tienen varios proyectos. Yo no entendí muy bien, investigué, pero en el contexto de alguien humano que me diga por qué no lo entendí. Pero pusieron los datos de compras en un proyecto, los datos de gastos en otro, los datos de ventas en otro, que en calza unificaron todo. No sé por qué.

**Daniel Mónaco**: Ahí no te preocupes que yo no vi nada, así que no sé la estrategia que estuvieron haciendo, más que nada conocer un poquito la herramienta, cómo trabaja. No te preocupes.

**Lucio Rojas**: Perfecto.

**Daniel Mónaco**: Ahí me llevó el mail, Pero no

**Lucio Rojas**: me he quedado sin token. Se diciendo

**Daniel Mónaco**: sí, que estaba probando ahora primero el logueo. Acá tengo que. Iniciar sesión por primera vez,

**Lucio Rojas**: usar la opción de usar un out.

**Daniel Mónaco**: Me da una opción de Google, pero bueno, el tema que la cuenta esta es corporativa a la que te pasé.

**Lucio Rojas**: Sí, y no quería usar eso.

**Daniel Mónaco**: No, no, por eso, por usar la cuenta corporativa, o sea, ¿Dónde genero la

**Lucio Rojas**: contraseña que compartí mi pantalla? Un segundo.

**Daniel Mónaco**: Ahí estás viendo. No tengo cuenta.

**Lucio Rojas**: ¿Vos sabes tu usuario y contraseña de la B, Mauri? Porque ahí podés arquear la otra cuenta

**Daniel Mónaco**: la tengo directamente con la red interna, no tengo la contraseña.

**Lucio Rojas**: Bueno, volvemos para atrás y. Usa que te hay una cuenta abajo. No tiene una cuenta todavía.

**Daniel Mónaco**: ¿La corporativa?

**Lucio Rojas**: ¿Es de Outlook?

**Daniel Mónaco**: Sí, sí, es de Outlook. Entiendo que sí, de Microsoft. Bueno, acá genera la contraseña. Entonces.

**Lucio Rojas**: Ahí me confirmaron que están usando CLOT, que se están generando unos SITs. No te deja. Entiende que es fácil, pero no te dice que no es fácil. Para

**Daniel Mónaco**: OK,

**Lucio Rojas**: estoy poniendo algunas mayúsculas o algunas.

**Daniel Mónaco**: You.

**Lucio Rojas**: Also point.

**Daniel Mónaco**: Bueno, ahí está, ahí estoy logueado. OK, ya tengo los cuatro proyectos. Bueno, después entonces empiezo a chusmear esto, a ver si querés ahí continuar.

**Lucio Rojas**: Perfecto, ahí dale, te comparto de vuelta la pantalla. Bueno, acá volviendo un poco la herramienta, le habíamos hecho una pregunta que era que me diste qué fuentes teníamos conectadas. Lenguaje natural para no complicar. Me dice, bueno, el proyecto Calza, del workspace calza, tiene 77 tablas organizadas en tres capas, 11 en silver y algunas otras. Dice las fuentes de datos vinculadas, las agrupó por fuente y después mostró las tablas. Hay una fuente principal que es Calza, con los datos call y ventas de maestros. Dice que probablemente ya está bajando desde SAP y me va diciendo cada una de las tablas que un calendario maestro y un calendario de fecha de la pacta. Es una descripción de la tabla de clientes. Siempre fue describiendo las 77 tablas. Si querés leer un poquito cómo describir cada una, pero no leerlas todas,

**Daniel Mónaco**: está ahí. Claro, seguramente. Buena. Ya te dividió antes la. De hecho con las dimensiones

**Lucio Rojas**: puedes pedirle cosas ultra interesantes. Yo le pido muchas veces que me haga un un der de cómo se vinculan todas las fuentes, que les cargué cuáles son las relaciones entre las distintas tablas del warehouse, todo eso lo hace porque tiene muy bien el contexto de cada tabla y cómo se vinculan.

**Daniel Mónaco**: Sí, sí, ya le pones ahí el código nombre de la transacción de SAP y ya te dice lo que tiene

**Lucio Rojas**: esa tabla y también te dice cómo se pueden relacionar entre ellas. Y después nosotros armamos, no sé quién, supongo que fue alguien armó tablas de resultado, que son estas Gol que vos le pedís a Claude que haga con la herramienta, y te va haciendo análisis. Tenemos una tabla de evolución de 2024 a 2026 por proveedor, que es la tabla analítica más compleja del proyecto. Compara para los 30 proveedores de gastos fijos más relevantes, el peso unitario y el importe pagado en un mes base, el primer mes que es marzo 2024 contra mayo de 2026. El análisis normaliza los conceptos facturados de cada proveedor. Por ejemplo, agrupa todo lo del almacenamiento, MP, in out, picking, vigilancia, limpieza, etcétera. Y calcula,

**Daniel Mónaco**: le diga, para que no quede estático, créame, siempre en Gol después cuando corre todos los procesos del año actual y mirando también desde dos años hacia atrás. Entonces, para no atar que sea 2024-2026, el proceso sabe siempre de forma dinámica que me va a cargar los datos de los últimos dos años más el actual.

**Lucio Rojas**: ¿Claro, sí eso se estandariza dentro del código SQL, va a decir y en staging para que?

**Daniel Mónaco**: Después en Go siempre va a tener no codificado el año, sino que vas a ver que siempre el año actual donde está parado y buscar hacia atrás.

**Lucio Rojas**: Un ejemplo claro es, nosotros hacemos mucho para algunos clientes lo que es reposición de stock. Y reposición de stock comparamos las las ventas en los últimos 60 días para predecir un poco las ventas en los próximos 30 días, o comparando los mismos 15 días del año anterior. Eso se define parado de hoy para atrás, y va actualizando a medida que pasen los días.

**Daniel Mónaco**: Tocaste un lindo punto. Suponte que le quiero sumar modelos predictivos o modelos de segmentación. Así de analítica hace predicción de ventas. Tengo que sumar un modelo ahí analítico, machine learning, data mining, lo que sea, pero un modelo ahí de predicción de, no sé, reducción lineal, lo que sea. Pero bueno, yo es un modelo predictivo ahí ¿Cómo sería?

**Lucio Rojas**: Yo he hecho algunos casos más jugando para un cliente real. Sé que hay clientes que lo han hecho, pero no lo llevé yo. Pero bueno, la teoría te dice que vos para tener un buen modelo de machine Learning, primero tenés que tener una tabla, una fuente de datos sobre la que pueda correr. Eso un poco lo difícil de lograr. Después el modelo es un script de Python. Entonces vos lo que haces es describir la cloud que querés hacer, por ejemplo un modelo de predicción de ventas, y en base a las tablas de tu fuente, te va a generar la tabla Gold para entrenar ese modelo. Esa tabla a vos te la va a poner por API y la podés consumir corriendo el modelo. El modelo te arma el mismo Cloud, si usas Cloud Code, te arma el propio modelo y lo podés correr, por ejemplo, en una virtual machine de AWS, corres el modelo ahí y consume la tabla. Pero eso es un caso ultra interesante para hacer. Nosotros estamos empezando ahora a jugar un poco con los clientes en ir automatizaciones también hemos hecho flujos de n, donde consulta todos los días a una tabla y automatiza toda la cadena de reposición de stock en base a lógicas de negocio y ya te manda los mails de reposición. Se puede hacer un montón de automatizaciones basadas en datos. Nosotros lo que hacemos es dejamos la tabla lista y después te las ponemos para que vos la puedas consumir. Volviendo acá, entiendo que son dos tablas de análisis puro que hicimos en Gold. Una fue esta devolución de proveedores y otra fue una de top de proveedores, que es un ranking de 75 proveedores de ustedes con mayor gasto acumulado entre febrero y mayo. Y las otras tres tablas gol que tenés son categorías que usaron para armar los análisis entre todas las silver o la fuente. Generaron las dimensiones y después hicieron gol de gol, me parece. Esas tablas se pueden consumir. Tablas Gol para crear nuevas.

**Daniel Mónaco**: Trata.

**Lucio Rojas**: Así que ahora vamos a hacer un procesito medio rápido. Le dije, bueno, ¿Qué otros análisis podemos hacer con Teamot? No veo nada de ventas. Le dije, no vi que tenga análisis de ventas, sino el proveedor y tiene venta. Así que le dije, bueno, vamos a hacer algo con las ventas y dame tres ejemplos de qué podés hacer. Leámoslo y te dejo vos que elijas uno para crear y lo creamos ahora vivo. Tenemos una de cumplimiento de presupuesto por marca y familia de producto. Va a cruzar la tabla de hechos con las jerarquías de producto para armar una tabla que muestre mes a mes cuánto se vendió realmente contra lo que estaba presupuestando. El porcentaje de cumplimiento y el desvío absoluto se podría cortar por negocio, marca y familia para identificar rápidamente qué líneas de productos están por debajo del plan y cuáles los esperan. Es útil para la revisión mensual con equipo comercial. Te ofrece esta te ofrece un ranking performance de la fuerza de ventas. Vamos a combinar la tabla de hechos con estructura de ventas y clientes. Puedo generar un tablero por vendedor que muestre el valor facturado, el volumen en kilos, la cantidad de clientes atendidos, CCC. No sé qué será reportada.

**Daniel Mónaco**: Pusimos ahí la tercera 12, la de la evolución del 1000 de ventas por canal y segment.

**Lucio Rojas**: ¿Ya habías leído antes? Yo terminé.

**Daniel Mónaco**: Sí, te estaba leyendo y después seguí leyendo y sea bueno, hacemos esta bien. Una pregunta. Ponele que el usuario me defina, bueno, quiero esta métrica. Y después bueno, me queda grabada en gol, me queda ahí ese campo calculado en una tabla, una tabla de hechos, una FAC, me queda ese campo. ¿Si yo quiero ponerle como una descripción de lo que es esa métrica, me queda algún lado esa descripción? Como viste, como tener un glosario, diccionario de datos. Lo podría hacer de tener, bueno, a nivel usuario, bueno, estos son mis KPI, estas son mis métricas, y acá tengo el detalle funcional de qué significa cada métrica.

**Lucio Rojas**: Bien con eso, no lo que es dentro de la tabla, lo que es por fuera.

**Daniel Mónaco**: Lo quiero en algún lado para consultar. Entonces yo sé que esta tabla, quiero saber justo esta métrica qué significa, Quiero leer esa descripción. Ponele que lo coloque en un campo. Pasa que bueno, tendría que tener una tabla. Si lo hago a nivel tabla, me conviene tener una tabla aparte para no llenar ese texto por cada línea. Lo quiero catalogar en algún lado como metadata y descripción de la metadata para no ponerla en la tabla donde están los valores.

**Lucio Rojas**: Nosotros honestamente no tenemos ninguna feature que genere esta descripción de los APIs que vas armando. Sí le podés pedir a Cloud que te cree una tabla, sea como una linda y lo va a harcodear con el SQL, que le pida que lo genere en las instrucciones. Es decir, generame una tabla que cada fila tenga, no sé, una ID al KPI y me haga una descripción. Y si no podés, si querés que sea a nivel usuario, generarlo como un knowledge de cloud o alguna instrucción y se lo copias en el proyecto. Entonces la gente, el usuario va a tener muy claro lo que estás hablando. Pero creo que estábamos pensando en generar esto que nosotros le llamamos un agente de contexto de negocio, que en base a lo que va creando las gold, genere el contexto y lo guarde como metadata. Tu pedido está muy bueno y me lo voy a llevar.

**Daniel Mónaco**: Esa es la idea, más que nada para gobernar los datos, tener ese catálogo y esas descripciones a nivel negocio.

**Lucio Rojas**: Nos está haciendo unas preguntas antes de crear la tabla. Me dice, ¿Qué métrica de ventas querés ver en la evolución? Valor neto, peso neto.

**Daniel Mónaco**: ¿Pone valor neto?

**Lucio Rojas**: ¿A qué nivel?

**Daniel Mónaco**: Por canal, ponelo

**Lucio Rojas**: excluir notas de crédito, devoluciones o algún tipo de factura o

**Daniel Mónaco**: a todo, ponele todo incluido.

**Lucio Rojas**: Vamos a ver, Acá está razonando Claude en base a toda la metadata que tiene, lo que nosotros estamos pidiendo, me va a pedir el permiso a la tool de crear una tabla BO y ahora va a ser una inyección dentro de Theramo con Reworkspace, el proyecto, el nombre, la descripción de la tabla que queremos crear, las tablas fuente, los keys los describe y acá se da descripción funcional de qué tiene que tener esa tabla. Claude te dice bueno la tabla pasó correctamente

**Daniel Mónaco**: y una pregunta, una pregunta tonta, cuando Claude, vos le haces la pregunta, Claude nada más accede a la metadata,

**Lucio Rojas**: También tiene la posibilidad de hacer un query data, tiene una tool con query data,

**Daniel Mónaco**: Le estás compartiendo ahí entonces los registros, los valores, solamente calcula y envía el SQL,

**Lucio Rojas**: no tiene la posibilidad, tiene la tool habilitada, vos la podés restringir si querés desde el conector,

**Daniel Mónaco**: eso lo configuras en el MCP, no el tema

**Lucio Rojas**: que puede leer conectores, yo no lo puedo hacer porque así acá puedo ver si puedo agarrar la SQL. Estatus de la tabla, me dice cada una de las acciones que tiene y vos la permitís, le pedís permiso o lo que obviamente esto va a afectar un poco la performance del conector, nosotros casi siempre damos libertad, pero bueno eso también tiene que ver mucho con su política de privacidad. Acá es una descripción del origen y dice vamos a hacer una tabla que muestre una evolución mensual del mil de venta por generación de distribución, muestra el valor neto facturado por canal y mes junto con la participación porcentual de cada canal sobre el total mensual. Incluye todos los tipos de instrucciones, agrupar por año y mes extraído de fecha de factura y por canal, campo canal de la tabla, calza canal para cada combinación mes canal, calcular valor neto, zoom del valor neto de la FA y participación el porcentaje que representa el canal sobre el valor total neto del mismo mes. Usar window function zoom sobre mes, ordenar por fecha descendente y dentro de cada mes por valor neto total descendente, no excluir ningún tipo de factura ni documento Y acá generar el agente modding nuestro, genere SQL, acá dice cero columnas porque es una falla en la UI que tengo que arreglar, Me trajo resultados. Acá, no sé por qué la UI no me está trayendo los resultados de la tabla, quizás hay algún filtro que no excluyó todos los resultados posibles. ¿Lo que tiene Clot es que es buenísimo para debuggear, si vos tenés algún problema en la tabla que creaste o demás, lo haces revisar con las herramientas que tiene, empieza a ver la query, empieza a ver la tabla tenía datos, la tabla fuente, por qué no se creó? Y te da un

**Daniel Mónaco**: yo hago una consulta, uy sí, esto me sirve, esta tabla me sirve para persistirla, empecé a guardar, esta tabla Gol que me sirve, la voy a consultar todos los días.

**Lucio Rojas**: Claro, sí la tabla Gol tiene ese

**Daniel Mónaco**: concepto, está bien, pero yo con la consulta ya queda, le estoy diciendo directamente ya se genera la tabla golpe por una consulta puntual.

**Lucio Rojas**: Claro, vos le hace, ponele que partimos de la consulta, partís de preguntar algo, tiene dos formas de resolverlo, o hace una query directamente a la Silver, usa ahí el propio cloud tu capacidad a través de la tool de query data peque, soñar la Silver y responderte, o se crea una tabla Gol usando Telamo para hacer esa transformación y te deja la gol 80, vos podés elegir, por

**Daniel Mónaco**: lo que imagínate que te hace un montón de consultas y se te va a generar un montón de tablas Gol y te empieza a mantener esas tablas Gol y vos decís no, capaz consulta puntual del usuario, no quiero que me llenes de tablas Gol.

**Lucio Rojas**: Ya eso está buenísimo, habla de rápido que ente la herramienta tenemos esos problemas a veces con algunos clientes. ¿Qué pasa? El consumidor final quiere consultar información, nosotros un comercial, usted chupa un huevo si está filder una tabla 3. Entonces para eso empezamos a trabajar en la gobernanza, necesitamos usuarios administradores que sepan cuáles son el universo de preguntas posibles y creen tablas Gold que sean suerte de maestros donde se pueda querer y resolver un 80-90 de las consultas frecuentes. Cuando esas consultas no estén dentro de las Go, va a ir a consultarlo a la Silver y si la Silver no se lo responde va a tener que crear una Gold o es porque los datos no están en la Silver. Ahora dimos la posibilidad de que tenga errores los usuarios y hay usuarios que solamente pueden hacer queries, las Gol y las Silver, eso está pensado para el usuario final y ahí tenés que cruzar Telamot con un buen prompteo a Cloud para explicarle a Cloud y ponerlo al nivel del usuario final. Estás hablando con usuario final, no digas ni que es una Silver ni qué es una Gol. Funciona como un agente, como conversacional, te pregunta y le respondes con sus datos. Si esa pregunta no la puede responder, decide que contacte al administrador y vos con administrador te fijás porque no está respondiendo y a lo sumo le quería su table, se la compartí. Por ejemplo, mira acá. ¿Está bien?

**Daniel Mónaco**: Si. Vos podés entonces configurar y decirle bueno mira toda esta consulta que no pudiste resolver, dejalas o dispara un mail al administrador para que las vea.

**Lucio Rojas**: Sí, eso no lo podemos hacer por

**Daniel Mónaco**: Telabot, eso es propio finalmente por bueno, por ahí la gestión del modelo del lenguaje que usas. ¿Nosotros acá lo que dejamos, vos que pensás? Capaz a ver si me equivoco. Yo lo que estoy pensando es lo haces una POC o haces primero, bueno, necesito todo esto, este es el requerimiento, necesito todas estas tablas de SAP y necesito que me resuelva todas estas preguntas. Son preguntas clave del usuario, quiero que me conteste todas estas preguntas. Bueno, empezás a trabajar y bueno, creas, ahí se crea la arquitectura, todo para llegar a esas tablas finales y responder las consultas. De ahí decir bueno, OK, esta es mi orquestación, esta son mis capas, mis reglas, quiero ahora sacarle foto, que no se modifique. Entonces todos los días ya cargo esa estructura, cargo la estructura así como está, con todas esas tablas Gol que se generaron y proceso diario, que vaya haciendo los cálculos todos los días, que vaya incrementando la información, modificando, bueno, depende la situación, pero que no se modifique más, que sea, quiero controlar yo si voy a modificar o crearse algo diferente en staging, o sea en la capa Silver y en GO lo quiero administrar y no que se crea automáticamente.

**Lucio Rojas**: Claro.

**Daniel Mónaco**: ¿Cómo lo ves eso?

**Lucio Rojas**: Bien, vamos a ir el caso. Te cuento una analogía. Yo trabajé con un cliente que me dio acceso a sus sistemas y me dijo yo necesito un dashboard que me responda estas ocho preguntas y me dio 49 tablas. Yo fui a CRUD con ese pedido, yo necesito que me responda estas siete cosas para ver un dashboard que se utiliza todos los días. Puedes reemplazar dashboard por agente conversacional. Y Claude me hizo la estructura de turno, me armó el Medallion me generó las Go. Ese sistema estaba vivo, tenía actualización incremental todos los días, y me armó. Una vez que definí las Go, no se modifican, salvo que el administrador entre a tocarlas. Lo que puede hacer dentro de la herramienta es, suponiendo que este proyecto es el administrador, le comparto datos a otro proyecto. Suponiendo que este Compra Hispano es el consumidor, le comparto las tablas de resultado que creé. Por ejemplo esta. Le creo la compartición, se la mandamos a Compr, volvemos, vemos Compra Hispano. Acá Compra Hispano ya tenía otros datos, así que lo vamos a ver ya cargado. Pero también tiene la tabla Gol que yo le compartí en mi proyecto administrador. Y a Compras Hispano yo le puedo ingresar usuarios que no son los mismos que ven Calza, que es el madre. Acá yo creo un usuario nuevo, tiene bastantes bloqueo Lucio, Le doy un rol de solo lectura. Acá puedes ver que puede hacer cada rol. Y a partir de ahora Lucio solamente va a poder consultar las tablas Gol. El administrador le compartió para hacer preguntas. Esas mismas tablas pueden dar origen a un Dashboard. A nosotros el Dashboard nos encanta hacerlo desde Cloud. Ya casi que ni pasamos por Tableau ni por Power BI. La Cloud tiene la función de Live Artifact, donde te genera el HTML con el Dashboard, pero te deja abierto como variable la llamada de MCP.

**Daniel Mónaco**: Solventamos las preguntas del usuario, listo, hacemos toda la estructura, la arquitectura corre todos los días. Y recién cuando hay una consulta que no se puede contestar, bueno, ahí sí nosotros como administradores decimos, bueno, vamos a modificar acá entonces la capa Silver, la capa Gold, para que responde esa consulta. Entonces yo como administrador lo controlo y después hay una nueva versión de todo el ciclo. Y ya le digo al usuario, bueno, capaz al día siguiente lo tenés espérame que yo voy a actualizar todos los scripts, y listo, mañana lo vas a poder consultar, me imagino algo así 100%, sí.

**Lucio Rojas**: Es más, yo si fuese administrador le diría al usuario, pásame la pregunta que no puede contestar.

**Daniel Mónaco**: Y vos le pasas lo yo actualizo el modelo. Y digo, bueno, listo, ahora sí, probalo. Ponele que si esa demanda, bueno, corro de nuevo, se ejecuta de nuevo, listo. Fíjate ahora, preguntá de nuevo que ya te va a responder.

**Lucio Rojas**: La actualización del modelo es mandarla a Cloud, como viste recién el usuario me está diciendo que no puedo responder esta pregunta. Fíjate todas las silver que tenemos y las bot cómo están construidas y si tenés que modificar algo para que lo pueda responder.

**Daniel Mónaco**: ¿Ponele que después compara las versiones, la actual y la nueva, te dice mira se modifica esta vista, estás de acuerdo, o sea estás de acuerdo en cambiar esa vista? Y yo mirándola digo OK, sí, cámbiala vos como administrador, sí ponele, yo como administrador digo esta vista que está en Silver que alimenta tal tabla Gol me está pidiendo acá la herramienta que se tiene que modificar para responder la pregunta y OK, dale, dale, cambia la versión, cambiemos, actualicemos, hagamos ese alter view y

**Lucio Rojas**: cambiar, eso es como funciona la herramienta, Yo por ahí me pierdo con el alter view. Actualizar vista,

**Daniel Mónaco**: Esto voy a cambiar, sí, listo, hacelo.

**Lucio Rojas**: Sí, sí, te entiendo, perfecto, no lo vemos más como AlterView o Alter Vista. Yo directamente no entiendo, le pido clon, que me modifique la voz. ¿Ese es nuestro lenguaje, cambia y queremos

**Daniel Mónaco**: tener el control que saber tener los triples de capa, estos son los de extracción, estos los de transformación, y después eso de transformación cómo van llenando las tablas Gol, por qué cosa? Para nosotros tener el control, si queremos reproducir el día de mañana tenemos todo el código de cómo tenía cada capa.

**Lucio Rojas**: Eso es exactamente lo que está acá. Nosotros estamos en la Silver, vamos a datos, LATAM, gasto PX, es un excel caral. Vos ves acá el script de transformación lo tenés acá, puedes copiar la Q y todo, esta es la tabla ME y después te vas a la Gol, Vamos a agarrar esta Gol de evolución a 26 por proveedor y tenés las tablas que tienen el origen. Si yo ahora busco esta, puedo dar la transformación que la origina de once a Silver y tengo el SQL que me da origen a la vista de la GO. Este es el SQL que va a cambiar. Si querés que responda una consulta nueva, la tabla GOL, y si no responde porque no está dentro del universo de datos compartido, va a tener que agregar esa tabla o esa columna al warehouse de Telamot modificando la fuente. Y si no hacer la consulta, la herramienta directamente, la Silver también puede tratar de responderlo así. Es un recorrido un poco complicado. Acá en la tabla que creamos, Evolución mil venta, fíjate esta tabla acá vino vacía la que hicimos recién. Le pregunté a Claude por qué está vacía. Me dice está vacía porque la fuente que usaste, Calzafact. Calzafact tiene cero filas en Silver. Raro, ¿No? Entonces se fue a mirar la B, que es la que nos dieron ustedes a nosotros. La tabla que te dio Calzavo tiene 18 millones de filas. La que vos transformaste tiene cero filas. Fíjate que está rompiendo algo. Eso fuimos nosotros. Yo me voy a Calzafact acá adentro sé cuál será. Esta debería estar vacía. Está vacía evidentemente los detalles de creación, pero quizás la rompimos con este estilo. Yo ahora me tengo que llevar. Estas cosas son las que vos me tenés que avisar a mí como soporte. Che, Lucio, fíjate que la tabla que te cargué la HAC, vino vacía.

**Daniel Mónaco**: El día de mañana sacamos una foto de lo que queda bien consistente. Entonces que no se provoque cambio, que sea tipo lectura. Si no puede responder a consulta, listo, se deriva al administrador y entonces yo me aseguro de que va a funcionar y que por algo no queda roto ahí la capa Silver y no llena la capa Gol. Entonces yo lo controlo de esa forma.

**Lucio Rojas**: Claro, esa es la idea. Esa es la idea. Se llama Datashar esa función, donde vos. Lo conceptual es que vos tengas un proyecto de administración donde te querés maestro, donde querés tablas Gol. Y después le de comer a proyectos de consumo si querés, hasta incluso agrupados por unidad de negocio. Los comerciales le das sus tablas de comerciales. Yo te colgué las tablas acá. Ellos ni siquiera tienen que entrar a. Tienen que entrar al cloud y preguntar libremente. El día que ellos no puedan responder, te van a hablar a vos. Vos vas a ver porque no se va a responder. Opción A, no le di la voz que quería. Opción B, theramond no está funcionando porque está caída el MCP. Opción C, la tabla que yo le cargué a Bronce Telamon no tiene datos en Silver. Entonces vos vas ahí rápido, identificar el problema con Plot mucho más rápido. Porque ¿Cuál es el problema? Y si el problema es nuestro, vos me vas a llamar a mí y yo voy y lo soluciono un día. Ese es un poco el worship.

**Daniel Mónaco**: El usuario justo pregunta algo. ¿Che, mira esto que te pregunta? No hay información de si él te pregunta.

**Lucio Rojas**: Eso también puede pasar. Sí, muchas veces preguntan cosas que está fuera del Scope Lat. Y ahí también son varios momentos que puede fallar, está buenísimo. Para eso tenía un usuario administrador. La diferencia que tengo yo como como gasto los acces soporte cuando tengo alguien que entiende bien el producto y no hay solamente consumidores, es mucha diferencia.

**Daniel Mónaco**: Buenísimo Lucio, muchas gracias. Ahí ya contestaste varias consultas clave y bueno, ahora empezar a practicar y ver un poco las poc a ver qué se fueron pidiendo que yo no las conozco, así que me tengo que ir metiendo.

**Lucio Rojas**: Dale, ahí vamos hablando. Así que buenísimo conocerte. Vamos viendo a poco. Yo supongo que ahora que me metí en el caso no me van a dejar ir, así que está bueno. Y hoy vi tu LinkedIn, me gustó mucho la puntación que hiciste, cómo cambia el rol del programador. Tu LinkedIn era, Te investigué un poco y me gustó mucho la publicación.
