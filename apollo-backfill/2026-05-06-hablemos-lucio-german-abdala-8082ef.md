# Hablemos !  Lucio  (German Abdala)

**Fecha:** 2026-05-06T12:00:39.737+00:00  
**Duración:** ~37 min  
**Participantes:** German Abdala <gabdala@daseragro.com.ar>, Lucio Rojas <lucio@teramot.com>  
**Externos:** gabdala@daseragro.com.ar  
**Apollo ID:** 69fb3628067fdd00218082ef

---

**German Abdala**: Hola, ¿Qué tal?

**Lucio Rojas**: Hola Germán, ¿Cómo estás? ¿Todo bien?

**German Abdala**: Bien.

**Lucio Rojas**: ¿Me escuchas bien? ¿Me ves bien? ¿Todo

**German Abdala**: bien, Lucio? Sí, pero bien, cómo un poco apurado de tiempo, pero quería dedicarle unos minutos para comprender un poco la solución.

**Lucio Rojas**: Perfecto, bueno, entonces si querés vamos de lleno, así no llevamos mucho tiempo. ¿Querés tomarte un minuto para contarme cómo conociste de nosotros, qué tipo de clientes pensás que pueden ya usar la herramienta? Uno o dos minutos y después ya vamos a una demo del producto.

**German Abdala**: Bien, mirá, yo como que estoy acá en Victoria, Entre Ríos, frente Rosario. Tengo una consultora que atiendo algunos clientes, Mi cliente principal es Dáser Agro, que por la que te escribí, digamos, ahí en Dasser tenemos instalado Finnegan, que entiendo que es una. ¿Ustedes son partner, alguna cuestión así leen la página? Tengo otros clientes, Acopio también, un par de empresas de Acopio, Estudios Contables, tengo otros clientes con otras plataformas, tengo un equipo de. Somos tres en total en la consultora que le damos así soporte, integración y demás. Un par más de personas que laburan con nosotros en lo que es tableros, un poco inteligencia artificial, o sea como que se especializan más en esa cuestión. Y llegué a ustedes, vi a un conocido, me dijo che, viste Teramot, qué sé yo, o sea, esto acá. Entré a la página, vi un poco lo que tenían y demás. Y bueno, la otra, hace 15 días hice una presentación ahí en dsser de lo que es la inteligencia artificial. Y lo que le digo es un poco como que se está constantemente recalculando, en un mes cambió ya el panorama, o sea, te cambian herramientas, usar. Y bueno, nosotros ahí, es la empresa más grande, tiene siete sucursales, el área nuestra de Tyson, más allá de lo mío, ahí como que estoy yo medio como líder, gerente, tengo dos personas a cargo, estamos viendo sumar una tercera, estamos tratando de ver automatizaciones, tenemos automatizaciones en Power Automate, tenemos algunos bots que leen APIs de un lugar y las graban en otro, digamos, hemos hecho un recorrido en esto de lo que es la IA y la automatización incipiente todavía, si querés en Finigan tenemos el bote compra, estamos conectando Braulio para lectura de comprobante, que yo. Estamos ahí con un montón de cosas.

**Lucio Rojas**: Bueno, gracias por el panorama bastante completo. Entiendo que tu perfil es un poco más técnico o de grado. Así que voy a tratar de tomar un lenguaje un poco específico para la demo. Como me mencionaste. Y antes del agro voy a tratar de mostrar unas tablas del agro que tenemos de prueba para empezar a entender la herramienta. Bueno, Telamot lo que hace es un producto, una herramienta que automatiza el pipeline de ingeniería de datos a partir de interacción con un humano y agentes de inteligencia artificial. Nosotros tenemos dos grupos agénticos, uno que se encarga de la limpieza, la estandarización y la normalización de los datos. Se pueden conectar múltiples fuentes de datos a Theramo, por ejemplo podemos elegir una Postgre, una MySQL, una SQL Server, un s de Amazon. Con BigQuery se proporcionan los distintos campos que requiere el conector para generar la fuente de datos. También se pueden cargar distintos archivos, por ejemplo en este caso de uso tengo cargados distintos archivos de Excel. Formato de la demo es un supuesto cliente que tiene archivos de Excel cargado y tiene guardada su información en todo lo que es hojas de cálculo y demás. Pero también se puede vincular esto con una base de datos. Nosotros lo que hacemos en un primer momento es crear una suerte de warehouse o de lighthouse con estos datos sanitizados en lo que decimos capa silver. Tomamos los datos crudos, entendemos la relación entre estos datos, lo dejamos en la capa silver y permitimos al usuario modelar nuevas tablas o realizar nuevos análisis con sus datos a partir de una interacción con LLMs. Nosotros el que estamos usando hoy en día es Cloud, Estamos usando Cloud adentro de alguna de las empresas, entendemos que es de los LLMs el que mejor está funcionando para todo lo que es análisis de datos. Se crea una conexión de los datos que uno carga en Theramo a Cloud vía MCP, donde nosotros le disponemos al usuario desde la web las URLs y los ID necesarios para generar la conexión. Y uno directamente desde Cloud puede empezar a interactuar con sus datos y modelar nuevas tablas que después quedan deployadas en la nube como infraestructura. Una primera pregunta es decirle buenas. Análisis con ellos. Entonces ahora lo que hace el es llamar a la tool de Theramot, tomar las tablas que vos descargaste, que puede ser directamente tu base de datos. Entonces vos le podes estar preguntando vivo tu base de datos o creando análisis con tus datos en vivo. Y lo que se puede hacer después es generar también reportes o distintos dashboards con Cloud en base a alguno está analizando, Elegir con qué datos tengo cargados. Hasta acá se va entendiendo medianamente toda la.

**German Abdala**: Sí, sí, hasta acá no lo veo tan distinto a que yo conecte cloud con mi dataset de Finnegan, digamos.

**Lucio Rojas**: ¿Bien, y ese dataset qué características tiene?

**German Abdala**: Un data warehouse que tengo armado, digamos, con todas las tablas que quiero publicar, digamos. No digo que esté mal, digo que un poco me parece. No, no, entiendo, entiendo, le sumo más cuestiones, digamos.

**Lucio Rojas**: Entiendo la cuestión que si vos tenés un data warehouse que ya está ordenado y entendés bien la estructura de las tablas y la relación, le conectás un MCP y haces preguntas. Lo que no entiendo si ese MCP también puede modelar nuevas tablas a partir de.

**German Abdala**: No tendrías que hacerlo en Cloud, digamos, o sea, tendrías como que darle alguna capacidad cloud para que te lo vea, digamos.

**Lucio Rojas**: Eso es una diferencia

**German Abdala**: y quizá entiendo que ustedes por ahí tienen capaz mejor resuelto todo lo que es la integración con otras fuentes, digamos, como una ventaja. ¿Ahí,

**Lucio Rojas**: ahí, mira, le hice una pregunta simple, digo que gol? Nosotros gol le decimos a las nuevas vistas puedo crear para generar un nuevo análisis en el caso de que esto lo agarre un usuario de negocio y necesite analizar sus datos. Entonces podemos elegir una, por ejemplo, esta segmentación de productores por comportamiento, que nos va a clasificar productores en segmentos altos, medios y bajos volumen, según sus ventas históricas y origen de compra. Yo le pido que cree esta bol y automáticamente lo que va a hacer Claude es entender mi pedido y generar una solicitud de creación de tabla Gold en Theramo que dice, bueno, segmentar productores en alto, medio y bajo volumen de ventas, Usar estas dos tablas de orígenes. Y yo in a partir de determinado campo, después hace una serie de descripciones de qué es lo que tiene que tener la tabla, y el agente de modelado de Téramo toma ese input de clock y genera la tabla y la deploya en infraestructura, puntualmente en Atina de AWS, y esa tabla queda en producción. Cada vez que vos actualizas tu fuente de datos, se actualiza la tabla. Entonces eso quizás una diferencia creo yo, de las principales, que también no solamente haces flujos de vuelta le digo yo que vamos a hacerle preguntas a las

**German Abdala**: tablas, puedes modelar, generas nuevas tablas y nuevos vínculos.

**Lucio Rojas**: Sí generas el Pylori y Clock ya entiende toda tu estructura, porque nosotros lo que hicimos fue pasarle archivos de metadata, y también entiende cómo está vinculada la tabla y se pueden conectar varias fuentes al mismo tiempo. Vos si tenés una base de datos de un sistema a otra de otro sistema, y tenés un excel colgado en la nube, bueno, podés armarte un Warhol. Es un bola. Es una de las preguntas que más nos costó responder al principio, porque cuando salió MCP no la esperábamos tanto. Bueno, hay gente que ya está conectando MCP a su warehouse, ¿Cómo nos diferenciamos? Y bueno, entendimos un poco el valor que estaba por acá. Vamos a esperar que la cree. Te muestro el resultado de la query SQL y no sé qué tan apremiado de tiempo estás, si no después podemos hacer alguna otra pregunta.

**German Abdala**: ¿Cómo son los proyectos ustedes? ¿Cómo son los Proyectos que desarrollan? Como decís, che, yo hago esto, tenés tres meses de implementación, tenemos parte, esto te lo doy y lo usás.

**Lucio Rojas**: ¿Los costos?

**German Abdala**: Los costos de la IA, digamos, ¿Cómo lo manejas?

**Lucio Rojas**: Nosotros no hacemos implementación, nada más damos una herramienta que la quiere usar y por tiers tenemos un tier que es gratis, puede entrar y probar después de esta reunión hasta dos tablas gold. Después si vos querés crear cinco tablas gold y dejarlas dos ya, ya son un tier de 50 dólares. Un profesional de 20 tablas sale 200 y después se entra en un modelo de enterprise. Nosotros elegimos un poco la filosofía de exponemos nuestra licencia y que la tome el que quiere para montar su negocio. Si vos querés ofrecerle servicios BI a otra empresa con inteligencia artificial, bueno, paga una licencia, nosotros y después generas tu negocio. Por otro lado, o por otra parte, si quieres acercarnos hacia una empresa, tenemos un programa de referidos, donde las primeras dos licencias las facturamos a quien nos refiere.

**German Abdala**: OK, Bien. Y entonces nosotros le pagaríamos a Theramo según la cantidad de Gold que usamos, Gol le llamas, como estas tablas nuevas que vamos generando, digamos,

**Lucio Rojas**: Estas serían las Silver que son las que vos conectaste, y las Gold, por ejemplo este caso de uso que tiene tres, ya no entra en un plan gratis, sino que va en starter de 50 datos.

**German Abdala**: OK. Y las goles estas es como para tratar de entender. Yo tengo el Data Warehouse en Finnegan, y es nuestra principal fuente de datos. Por decirte, en Dasser puntualmente, Las Gol serían como tablas adicionales que yo quiero generar para tener ya algo resuelto, algo para visualizar, digamos. Sería un poco esa la idea, Lucio.

**Lucio Rojas**: Claro, exactamente. Vos conectas el warehouse, eso nosotros los tomamos como input, sería en tabla Silver, y cada vez que usted genera un nuevo análisis para resolver algo, sería una tabla Go.

**German Abdala**: OK. Cada análisis se plasma en una tabla, digamos. Sería.

**Lucio Rojas**: Sí, cada objeto de análisis. Si querés después uno puede consultar esa tabla n veces.

**German Abdala**: Bien. ¿Y Uds? ¿Con eso se hacen cargo de la licencia de Cloud, o eso es nuestra, o como lo gestionan, digamos?

**Lucio Rojas**: Ahí tenés dos alternativas. Una es usar Cloud, como mostré recién, que eso es mi cuenta, si se quiere particular, donde ustedes conectan MCP y la cuenta de Cloud queda de su lado. Y la otra es usar este agent, está al costado, no lo mostraré en el momento, pero es en realidad una API, una API key de Antropic, donde podés hacer preguntas también, decirle bueno, quiero crear una nueva BO, Este también va a crearla igual que como si estuviésemos trabajando con CL, y esto sí queda de nuestro lado. Lo único que diferencia es que este tipo de agente no funcionaría. Para lo que esto, aparte de generar análisis con Cloud, nosotros lo vemos bien, que bastante útil. El usuario final decir, bueno, con la información que tenemos acá, hagamos un informe de gestión, lo pone todo dentro de un PDF con análisis de los datos, lo tiene para mandar. Pero bueno, tu valor está en construir RTL, con esto alcanza.

**German Abdala**: OK. Esto ustedes lo tienen como una opción, pero bueno, sugieren Cloud por la versatilidad, por toda la potencia que tiene, digamos, de alguna manera. Bueno, ¿Tienen conexiones con Finnegan? ¿Tienen, digo, tienen clientes que ya están operando? ¿Conectan? ¿Cómo conectan? ¿Conectan al Data Warehouse? ¿Conectan al ADB? ¿Cómo lo hacen?

**Lucio Rojas**: Honestamente no tenemos, o yo no tengo una relación clara de clientes. ¿Confían que hemos trabajado conjunto? ¿Quizás es algún partner nuevo, cuando vos lo mencionaste? Si, tenemos clientes históricos, ya Tenemos más de 30 clientes. Trabajamos con Coca Cola, con Johnson Johnson, con empresas acá de Rosario y con la Bolsa de Comercio, con Los Aires, con el Banco Industrial, y siempre nos conectamos a su DB. Generamos la conexión a partir de los conectores que tenemos en la herramienta y se va actualizando. Todos los días a las 8 de la mañana

**German Abdala**: se entiende cliente de algoritmo de algoritmo, una herramienta, trabaja con Oracle,

**Lucio Rojas**: la base de datos no lo conozco.

**German Abdala**: ¿Y cómo es el sistema de referidos, Lucio? Para saber,

**Lucio Rojas**: por ejemplo, si vos llevas la licencia hasta un cliente, nosotros vendemos por tiers mensuales, los dos primeros tiers te damos la opción de que vos no los captures a nosotros referente, y después. Bueno, si querés esperamos hasta que termine de crear la bol, si no, ya entendiste un poco el concepto. Este está terminando de construirse, te puedo mostrar anterior, un poco el viejo programa de cocina que la torta cocía. Por ejemplo acá muestra que toma cuatro tablas de entrada, deja una tabla final, un ETL de venta de soja por producto, hace una descripción del origen, necesita una fila post quit del productor con nombre productor, venta de sojas por año, estados de licencia, genera una serie de instrucciones que tiene que tener tabla. Todo esto nace de la conversación que uno tiene con cloud, donde inserta los inputs a theramo y Teramot, toma este input para generar el código SQL, la query SQL, acá está la query nueva que da origen a la tabla, Los joins y demás. No soy ultra, tengo SQL, no te voy a mentir, hoy en día no sé si tiene tanta implicancia, hace toda la query y después en el editor de SQL también puedes hacer consultas a esa nueva tabla que gener. Pero bueno, medianamente se puede ver la tabla como queda generada. Y esto lo podés consumir desde el mismo cloud, o nosotros damos la posibilidad de harte esta tabla o conectarla a alguna salida de datos, por ejemplo lo que es Power BI, Look Studio, Tabló y demás, generar la conexión, se le da acceso a la nueva tabla, Genera acceso y le da las opciones de autenticación para conectarlo a alguna herramienta de BI.

**German Abdala**: Sí Lucio, claro. Y si no podés usar las opciones de visualización de cloud, podés pedirle que te haga un tablero, algo que te lo Programe Cloud directamente 100%.

**Lucio Rojas**: Eso es lo que a mí más me gusta hacer, si se quiere, estoy esperando que termine la GOL para poder mostrarte. Casi siempre lo que más sorprende es, bueno, vos un usuario de negocio, y te creas tableros a demanda, y los tableros que te hace clot son una bomba buenísima. Le podés pedir informes directamente, generar un análisis de la situación en base a los datos, ponerlo en un informe PDF y llevarlo a algún gerente, tenerlo como recurso. Otra cosa que ha funcionado muy bien es entrenar algunos modelitos de Machine Learning o algunos modelos predictivos a partir de la tabla que vos le planteas a Claude tu problema en base a estos datos, ¿Necesitarías esta tabla para entrenar tu modelo? Bueno, tenemos la tabla, una vez que tenemos la tabla, elegimos el modelo, lo generamos todo con Cloud Code y ese modelo después lo entrenamos en alguna virtual machine, en una EC AWS y queda corriendo y ya tenés todo lo que es la parte predictiva funcionando. Acá la estrella sería un poco plot, pero bueno, esperamos que nos permite a nosotros trabajar con los datos, crear las tablas, empezar a darle más herramientas.

**German Abdala**: Claro, es como que Teramot va al medio, digamos, o sea como que de una manera como que te permite homogeneizar toda tu data, digamos, para que esté disponible para Cloud. Sería un poco el punto, digamos.

**Lucio Rojas**: Eso fue exactamente lo que pensamos cuando empezamos a ver los conectores MCP y el producto que teníamos que armaba TL, dijimos nosotros tenemos que dejarle al usuario usar sus datos de cloud. Certificamos SOC, estamos a un 90% de auditoría ISO 27001. Tenemos algunas cuestiones que nos posicionan en ese lugar, de decir, bueno, no hay una competencia que esté haciendo como producto. Si puede haber alguna empresa que esté desarrollado internamente, un buen Data Warehouse, conecta por MCP, hace consultas, quizás le da SMCP tools para generar nuevas tablas, Bueno, tiene algo similar, pero nada, acá lo tenés por 50 dólares. Se sabe menos que contratar a alguien que empiece a pensar cómo ser eso. Claro.

**German Abdala**: Lucio, ¿Y la licencia de Cloud? ¿No te quedás corto o qué tipo de licencia sugieren o demás para usarla, digamos?

**Lucio Rojas**: Mira, no es un gran consumo de tokens, porque nosotros manejamos la información por metadata y les pone la las tools. Entonces el consumo de token tratamos de eficientizarlo con un pack directamente starter de 20 dólares. Funciona. Pasa mucho que el usuario se copa cuando empieza voy a hacer así, voy a ir directamente sobre. Herramientas para seguir creando la Gol, yo la voy a matar porque quiero hacer una consulta. Finalmente consultar tus tablas, entender el problema y generar una nueva tabla. No es un un consumo muy alto de tokens. Lo que sí es que cuando agarra el usuario y le dice bien este que muestra el total de venta de sojas agrupado por estado, licencia. Yo voy a decir de esta tabla. Interactivo para presentar la reunión, credencial, encima se ceban y ponen opus 4 y 7, la que va mejor. Ahí sí está empezando a consumir varios tokens por lo que vos empezás a querer hacer con tus datos. Pero.

**German Abdala**: Por eso pensaba un poco en el uso, digo, que tienen ustedes cliente Lucio, como capaz que no el que quiere los datos, porque capaz que se te entretiene con esto y gasta, digamos, meten a alguien un poco más un rol un poco técnico, un poco que conozca los datos para eficientizar un poco la búsqueda, para pensar cómo armarlo. ¿Quiénes son los clientes?

**Lucio Rojas**: Tenemos si querés dos tipos de clientes, quizás tres. Uno muy claro es el analista de datos, la persona que trabaja con datos dentro de la empresa. Ayer estábamos acompañando puntualmente en una reunión alguien de la bolsa en el Rosario, y necesitaban cruzar dos tablas con información de distintos sistemas y un ID que no estaba creado y se tenía que inducir en base a una tercera tabla y algunas reglas lógicas. Y las chicas decían bueno, hicimos lo mismo, se POC para ver si lo podemos resolver. Resolvimos lo mismo que no habíamos resuelto en dos meses, en una reunión, una hora. No porque nosotros unos genios, sino porque Cloud funciona muy bien para esto, con tercer gráfico. Después hay otro tipo de usuarios que son los implementadores. Nosotros trabajamos con empresas que llevan estos tableros finales, estos análisis finales a un cliente al final de la cadena. Y bueno, eso también tiene una suerte de rasgos técnicos, sería más parecido a tu caso, Entiendo. Y en un tercer lugar, tenemos mucho SEO de empresa usando esto, o nivel alto de pyme, alguien que quiere consultar la información rápido, decime esto y te lo respondo. Y como el jefe de la empresa no le importa para nada cuánto toque está gastando ese. Así que bueno, ahí tenés esos tres tipos de usuarios. Alguien muy técnico para resolver su problema de datos, el medio para resolverle el problema a otra persona, y alguien que sigue, alguien que charla, alguien que quiere hablar, no importa, consume.

**German Abdala**: Lo veo, o sea ¿Que nos pasó en Finnegan? Finnegan lanzó una herramienta de IA integrada, integrada digamos, y como que puede ver lo que vos tenés en el data warehouse, y vos sabes que lo lanzó hace, ponele, capaz ocho meses, por ejemplo, por decir. Entonces vos generar un reporte nuevo, un tablero te costaba 15 dólares por decirte, o 30 dependiendo cuántas veces interactuaba, ellos fueron puliendo y hoy capaz que armas un reporte con tres dólares, digamos. Perdón, y desarrollamos bastante con otro chico que labura como bastante fino esto que vos decís técnico, como que le dice los campos, le dice che tomame esto de tal tabla, de tal dataset, digamos, y como que te arma un gráfico con todo eso y sale de una, nada que ver con esto, es mucho más básico, o sea, mucho más, o sea, estamos apuntando a un reporte o un tablero simple, digamos, pero entiendo que está piola estos tres perfiles que decís con el pricing, digamos. Entonces para entender estás Gol, porque yo digo, veo, veo, ahí estaba mirando, ponele las 20 tablas son 200 dólares, las 20 gold, el día de mañana yo genero algo nuevo. Estoy pensando en cómo evolucionaría esto digamos, no decir che, cada reporte nuevo de alguna manera es una tabla para Bouna Gol o no, digamos.

**Lucio Rojas**: Claro, cada vez que vos generas un Intel si querés y dejas una Gold creada, estás generando una de las variables de consumo de pricing, pero hicimos optimizar la herramienta para si hay un usuario del otro lado haciéndole una pregunta que puede resolverse con alguna gold que ya está creada o con las silver que ya están creadas, no te hace crear la Gold porque sí se la crea cuando realmente es necesario.

**German Abdala**: Claro, eso pensaba Lucio, porque digo, por ejemplo pienso en las ventas, o sea algo puntual che, ventas, venta, que yo siempre, seguramente por ahí agregan algo nuevo, che, ahora queremos ver que eso es una Gol nueva o es la modificación de la que está, digamos, se puede

**Lucio Rojas**: modificar la que está, No son inalterables, lo único que por ahora no se pueden modificar vía MCP, sino que desde la herramienta de Telamot se tienen que agregar instrucciones, pero sí, históricamente se puede modificar eso y si no se puede eliminar y crear una nueva, no son estáticas.

**German Abdala**: Ahora podrías decir che esta no me sirve más, tengo la viste, nosotros por ahí vamos versionando como diciendo che versión 2, versión 3, che deja la última versión y te consume la última, digamos, diste de baja esa digamos y la

**Lucio Rojas**: agarrás y la eliminas, o sea lo que nosotros apostamos es tener cinco tablas que le están generando valor al usuario y que no se las quiera, que

**German Abdala**: las tenga ahí, que tenga 20 que no usa y 5.

**Lucio Rojas**: La verdad que serio, tramposo el pricing. Nosotros al contrario, buscamos alentar al uso. Somos una startup y va modificando mucho todo lo que es, como vemos el pricing, como vamos. Hace unos meses atrás era por consumo, elegimos que era mucho más fácil explicarlo desde Tiers, tenemos un plan enterprise, o si alguien crece mucho en consumo, se sienta a hablar con el equipo comercial y dice Bueno, yo tengo 5 clientes, estoy escalando proporcionalmente mis clientes, se me está volviendo un costo irremontable, bueno, no pasa nada, frenamos hasta acá, hacemos un descuento, vamos por este lado. Me interesa más la parte de poder yo el producto al mercado y la monetización es un derivado.

**German Abdala**: Una pregunta más, no, Marisa, ¿Cuántas personas son y cuánto hace que están laburando en esto?

**Lucio Rojas**: Digámonos enteramente, Hoy en día La startup tiene 23 personas, donde 5 somos de equipo comercial, de negocio, business development, el resto son ingenieros y científicos de datos. Todos trabajan en el producto. Empezamos hace dos años y medio, los founders Bruno y Lucas estaban hace mucho en lo que es inteligencia artificial, y si se quiere, se hizo un corte hace un año y algo atrás con la inversión, una ronda de 2 millones de dólares y el producto lo pudimos definir y enfocarnos a esto. Estamos buscando expandirnos y mejorar todo esto que llevamos hasta el momento. Yo estoy hace un año y algo.

**German Abdala**: Qué bueno che. Qué bueno. Bueno Lucio, déjame analizarlo un poco y bueno, me interesa para mis clientes, voy a ver de canalizarlo y me parece genial la idea y que tengan muchas suerte, loco. Me parece una muy buena opción, digamos.

**Lucio Rojas**: Buenísimo. Yo por mi lado invitarte a probar si querés un plan gratuito o te extendemos alguna prueba por algunos meses, cargar unas tablas, cargar alguna base de datos, algunas tablas del warehouse. Yo voy a mandar un mail siguiendo un poco el caso y si te llegas a hacer un usuario, nosotros y probarlo y ver si te sirve.

**German Abdala**: Bárbaro, bárbaro, bárbaro. Muchas gracias Lucio.

**Lucio Rojas**: No, por favor.

**German Abdala**: Suerte loco.

**Lucio Rojas**: Chau, chau.
