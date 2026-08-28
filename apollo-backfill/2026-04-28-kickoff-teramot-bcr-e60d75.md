# Kickoff Teramot - BCR

**Fecha:** 2026-04-28T14:59:08.217+00:00  
**Duración:** ~47 min  
**Participantes:** Schmidt, Nicole <nschmidt@bcr.com.ar>, Tomas Teramot <>, Lucio Rojas <lucio@teramot.com>, read.ai meeting notes <>, Romano Bazán, Ayelen <>, Juan - Teramot <>, Frezzini, Diego <dfrezzini@bcr.com.ar>  
**Externos:** nschmidt@bcr.com.ar, dfrezzini@bcr.com.ar  
**Apollo ID:** 69f0d671776c83001de60d75

---

**Schmidt, Nicole**: Buenas.

**Lucio Rojas**: No sé si decir buenos días, buenas tardes. Lo pensé tres, cuatro segundos.

**Schmidt, Nicole**: Para mí son buenas tardes porque vivo en España, Entonces son las 5 de la tarde acá.

**Lucio Rojas**: Mira.

**Romano Bazán, Ayelen**: Musculosa.

**Schmidt, Nicole**: Claro. Tengo un par de grados en Barcelona.

**Lucio Rojas**: Barcelona. ¿Y que haces? Hace mucho yo. ¿Trabajas acá y después te fuiste o te contrataron desde allá?

**Schmidt, Nicole**: No, ya trabajaba en Bolsa antes de irme y lo mantuve increíblemente. Nunca en mi cabeza fue como. Pero me quedo en Bolsa. Pero me vino bien y también está bueno. Tengo la mañana libre, así que a horario de allá. Y bueno, raro, pero está bueno.

**Lucio Rojas**: No sé si esperamos a alguien más de su lado.

**Romano Bazán, Ayelen**: No, si quieren empezamos ahí. Yo le escribo igual por las dudas.

**Lucio Rojas**: Nosotros estamos también acá. ¿Que lo esperamos o no? A Juan, que también ha estado en otras reuniones, pero estaba con un delay, tenía otras reuniones presenciales y me dijo que arranquemos y. Y después su map. Bueno, entonces si quieren arrancamos. La idea de la reunión era hacer un kick off de la herramienta, empezar a saber cuáles son las pautas de trabajo, cuáles van a ser los casos de uso que vamos a tratar. También un poco conocernos entre nosotros. Entiendo que vamos a estar teniendo algunas reuniones consecutivas. Me interesaría entender bien qué perfiles tienen, si son BI Analyst, si son más de negocio, eso tenerlo claro también para trabajar. Así que les escucho un poco qué idea tenían y en base a eso vamos. Vamos trabajando

**Romano Bazán, Ayelen**: bien. Bueno, ahí si quieren empiezo un poco. Nosotras trabajamos en el área de BI y de datos dentro de la Bolsa de Comercio. Generalmente, bueno, nosotros usamos diferentes herramientas como SSIS, tenemos reportes en Power BI, y lo que tenemos también son cuos en Análisis Services. Y actualmente los usuarios consumen esa información a través de Excel, conectándose a esos cubos de Análisis Services. La idea un poco de ahora de la prueba de concepto, es utilizar la información de solicitudes, que es información del laboratorio, que es un área puntual dentro de la Bolsa. Y la idea es reemplazar a lo que ahora ellos están consumiendo a través de ese cubo, que ellos lo que hacen es a través de tablas dinámicas, consumen la información y van modificando las consultas. Es información que se actualiza diariamente la noche anterior. Y ahora lo que nos está pasando es que reprocesar ese cubo y demás tarda muchísimas horas y muchas veces nos trae inconvenientes de errores, problemas y demás. Entonces lo ideal sería hacer el reemplazo de ese cubo utilizando theramon y que ellos desde ahí directamente puedan consumir esa información. Y también lo que nos fue pasando es que los usuarios van pidiendo también solicitudes de algunos reportes o algunos requerimientos que ahora los estamos anotando. Y bueno, todos estos requerimientos que tienen que ver con esta parte de solicitudes, o sea con el mismo origen de datos. La idea es probar theramont para ver qué potencial tiene, si esos casos los podríamos usar, podríamos aplicarlos acá en esta herramienta o no. Y ver después también cómo sería la dinámica con el usuario. Actualmente ellos suben un ticket con un requerimiento, nosotros hacemos todo el desarrollo y se lo damos. Pero bueno, ahora es entender un poco qué tanto podría ser el usuario, hasta dónde haríamos nosotros y si ellos después van a tener la posibilidad de cambiar esos reportes. Es un poco eso la prueba que queremos hacer.

**Lucio Rojas**: Bueno, por ese lado se entiende, lo veo viable, tenemos construye este tipo de soluciones, vamos a tener que trabajar un poco entre ustedes y nosotros probablemente si ustedes tienen un set de información importante, generar algunas tablas Shago para que estos usuarios finales consuman desde ahí y puedan hacer su propia nueva instancia de análisis. Hay una pregunta que no hay que dejarla pasar, es importante, es ¿Qué expertise tienen estos usuarios? ¿Qué nivel de uso le pueden dar? ¿Se puede pedir algo un poco más complejo técnicamente algo muy sencillo, cuántos son? Como es por ese lado la situación.

**Romano Bazán, Ayelen**: Si, usuarios que usan el cubo son más de 20, por eso la idea no es darle directamente la herramienta a ellos, sino era estar nosotros como intermediarios de generar esos requerimientos y después otorgarle la información a ellos o ver cómo lo hacíamos para no darle a los 20 usuarios el acceso libre. Ellos hoy tienen acceso libre a estos cubos y les tuvimos que dar varias capacitaciones porque lo que pasaba es que generaban tablas dinámicas y traían capaz toda la información de toda la historia o generaban malas consultas y demás y terminaban rompiendo el cubo. Entonces sí, en ese nivel los usuarios hay de todo, pero la mayoría no son muy expertos, no sé, en consultas de SQL y demás, no lo harían. Por eso siempre estamos nosotros como intermediando, como intermediando digamos, entre lo que ellos piden y lo que se puede hacer y cómo hacerlo. No sé si ahí respondí tu pregunta o había algo más.

**Lucio Rojas**: Sí, sí, sí. Quería entender si íbamos a estar trabajando con ustedes como usuario intermediario. Voy a dejarles como ambiente de testing, que ellos entren y se generen sus propios reportes. Lo que solemos proponer es que si hay dos, tres usuarios que ustedes lo ven, que pueden adoptar la herramienta, que pueden ya tener un poco más de un uso controlado, probarlo con ellos está bueno, porque la ventaja que da la herramienta es que no se necesita conocimiento técnico para hacer consultas. Se puede hacer consultas de nuevas tablas a partir de interacción con clock, puntualmente como inteligencia artificial, y te genera texture, te genera, crea la tabla, la de apoyo en producción, y después se puede consumir de vuelta desde el cloud. Entonces un usuario que se maneje lo puede hacer. Y lo ideal, siempre que alguien de sistemas esté orquestando un poco toda la solución, porque si no se vuelve un caos.

**Schmidt, Nicole**: Ahí un poco para sumar, lo ideal sería que sí, que le demos acceso, me parece, a dos usuarios que son como nuestros Pro owner dentro de esta área gigante del laboratorio. Más que nada porque por ahí ellos están en contacto con las consultas que suelen hacer los usuarios. Entonces estaría piola que si se puede meter a esas dos personas nada más, porque nosotras podemos intentar, pero no conocemos tanto qué necesitan. Ahora es como que tienen libertad absoluta de arrastrar campos dentro de una tabla dinámica y hacer lo que ellos quieren. Entonces, nada, como para ver si se puede sacar todo de la misma forma y cómo funciona. Ellos dos sirve. De hecho, a veces nos falla el proceso y ellos sacan las consultas, ellos saben hacer, conocen SQL, o sea, como que son usuarios que manejan, digamos, la información. Ahí solamente es cuando se testee, pero nosotras podemos también hacerlo. No sé cómo la ven.

**Lucio Rojas**: Bien, sí, yo lo sumaría. Si quemamos por ese camino. Lo primero ya para empezar a organizarnos en pasos es conectar la información. Hay información, no los datos. Para eso Tommy es nuestro. Yo lo tengo a la derecha.

**Schmidt, Nicole**: No, yo lo tengo.

**Lucio Rojas**: ¿Quien va a estar con las conexiones? Así, Una vez logrado eso, definamos todo y marcamos una próxima reunión para trabajar directamente sobre la herramienta. Así que Tommy, haga sus preguntas, dale.

**Tomas Teramot**: Bueno, principalmente ustedes usan como herramienta cubo, si no escuché mal. ¿Cómo llenan de datos a Cubo se les suelen cargar CSV, Excel?

**Romano Bazán, Ayelen**: No, ahí nosotros tenemos un Data Warehouse creado en SQL Server y nosotros lo que pensábamos conectar a theramont serían las tablas, que ahí sería una tabla FAQ de solicitudes y las distintas dimensiones.

**Tomas Teramot**: Bien, así vamos más por el lado del SQL. Nosotros en theramont obviamente soportamos todo tipo de conectores, sean CSV, bases de datos. Para hacer las conexiones de base de datos nosotros solicitamos un par de campos que ustedes nos tendrían que pasar. Calculo que iría más por la parte técnica de implementación de su parte. Si quieren, no sé si se los muestro ahora, sino vía mail, para ya dejar pactado qué datos necesitamos de ustedes y qué datos le vamos a pasar nosotros para hacer la conexión, porque obviamente imagino que las bases de datos son privadas.

**Schmidt, Nicole**: Sí, ahí habían tenido una reunión para armarlo del túnel y todo eso.

**Romano Bazán, Ayelen**: Sí, que ahí estuvimos con Aníbal, creo que Lucio estaba y Juan, no sé si te acordás que habíamos hecho una reunión para ver la parte técnica, lo que habían hablado desde nuestro lado, desde la seguridad de bolsa era generar un túnel que ellos ya lo han hecho para otro. Para otro proyecto que tuvimos. Así que la idea era conectarnos por ahí a nuestro ambiente, ahora sería de staging, o sea de desarrollo, pero a través de ese túnel. ¿Ahí habría que ver ahí, bueno, si querés mandarnos por correo, bien, que necesitas? Involucramos a Aníbal que él es del área de seguridad, digamos, que va a estar haciendo la configuración y demás.

**Tomas Teramot**: Bien, buenísimo. Después, bueno, consultas por fuera. Ustedes los datos manejan primary keys, imagino a un dato de tipo off date, por ejemplo, ¿Entra alguna tabla?

**Schmidt, Nicole**: Sí, sí, o sea, bueno, armado un modelo estrella, digamos con la. No sé si conocen nuevos modelos relacionales. Modelo estrella y bueno, y tiene. ¿Preguntaste por datos tipo columna de update, cuando se incrementó la tabla o se cambió la tabla?

**Tomas Teramot**: Estamos trabajando con un nuevo modelo de incremental, así que calculo para tener los datos lo más rápido posible vendría bastante bien.

**Schmidt, Nicole**: Sí, bueno, ahí no sé cómo se comporta. Ay, cuando corre el carga completa ese update de tablas como que siempre va a estar al último mes capaz

**Romano Bazán, Ayelen**: tenemos como un proceso diario que hace la carga y después lo que dice Niki es una carga completa que los una vez por mes se hace un borrado y se vuelve a cargar todo. Entonces ahí lo que tendríamos que ver esas fechas de update. Si, siempre va a poner la última fecha de la carga completa, que sería como a principio de mes.

**Schmidt, Nicole**: Claro, tenemos que chequear cómo se actualizan esos datos, digamos, diariamente. Sí va a aparecer el día anterior, se ejecuta una sola vez y sería como que se actualizó la tabla a la noche del día anterior o a la madrugada de ese día sería. Pero después una vez al mes tenemos que ver cómo se actualiza esa fecha, como que se actualizan todos los datos. Va a quedar, no sé, el 2 de mayo, por ejemplo, ahora corre los sábado, va a quedar todo el historial de datos con 2-5. Capaz hay que ver, ¿No? Capaz con todas las tablas, tendríamos que ver con la de solicitudes.

**Tomas Teramot**: Bien, sí, ahí calculo. Para esos casos es conveniente un full load en vez de ir haciendo las cargas incrementales. Bien, de mi parte no tengo más dudas. No sé, Lucio, si hayan charlado alguno más.

**Lucio Rojas**: Bueno, principalmente hasta no tener cargadas las tablas no podemos hacer nada de implementación. Lógico. Así que avanzaríamos por ese lado. Tommy, subí una cadena de mail ahora y en copia a todos. Y también quién era de su parte, la persona que tenía que estar en copia, Aníbal.

**Romano Bazán, Ayelen**: No sé si ustedes lo tienen igual, pero si no nosotros lo agregamos, envíenlo y se lo reenvíe.

**Lucio Rojas**: Bien. Bueno, y una vez definido eso, tendremos que marcar otra, siempre la de kick off es muy cortita, para ponernos de acuerdo en cómo cargar los datos. Y después ya sí, la idea nuestra como Tenamot, es acompañarlos a ustedes en la implementación de la solución, no resolverlo por ustedes. Por la cuestión de que nosotros damos una herramienta que una vez se conecta el MCP a Claude o con un usuario, tengo el otro lado, es mucho mejor que ustedes manejen directamente los datos y tipo de soluciones que quieren generar. Así que quería por ese lado marcar una próxima reunión para mostrarle bien la herramienta, ver cómo funciona, que ustedes puedan hacer las preguntas que se vayan encontrando, y después hacer unos seguimientos una vez por semana, para en caso de saber cómo viene, nosotros le damos soporte Classy, todos los días en tiempo real, nos escriben, me escriben a mí, me escriben a Juan, y vemos si hay alguna falla, algún tipo de error. Eso tratamos de solucionarlo en el momento. A veces hay error con alguna columna que se carga los tipos de errores clásicos, alguna tabla se desactualiza y demás. Y bueno, por ustedes como usuarios no pueden hacer nada y nos tienen que escribir a nosotros para dar el soporte ahí.

**Schmidt, Nicole**: Nosotros de nuestro lado es 100 web, no tenemos que instalar absolutamente nada, nuestra compu ni nada, es acceder a una página, ¿No? Guiarnos ahí y usarlo desde ahí, ¿No?

**Lucio Rojas**: Sí, tenemos una web app donde manejan más que nada lo que es la conexión de las fuentes y la creación de nuevas tablas. Y también nos conectamos por MCP a Cloud. No sé si ustedes tienen. De chat GPT, pero pregunta acá a ustedes desde Bolsa, ¿Tiene alguna restricción con modelos de inteligencia artificial y privacidad de los datos por ese lado?

**Schmidt, Nicole**: Eso no lo hablaron, yo no estuve justo esta ocasión en la reunión con Aníbal, Dani, no hablaron nada ahí no

**Romano Bazán, Ayelen**: hablamos de conectarnos directo a al modelo. Si hablamos de esto, de generar el túnel para pasar la información, pero no de conectarnos directamente a Cloud o ChatGPT.

**Lucio Rojas**: Si quieren les comparto para revisar un poco eso y vemos por qué hay alternativas. Bien, esto es una base de prueba que usamos para mostrar herramientas y mostrar la demo. Lo primero que van a hacer es conectar la fuente de datos solamente cuando generen el túnel, van a ver acá las fuentes, y adentro las distintas tablas de cada una de las fuentes. Se pueden, por ejemplo, esta es una fuente con varias tablas, tiene dimensiones, acá hay una fact, parecido a lo que ustedes plantearon, y se puede ver en esta segunda pestaña o layer, las distintas tablas Gold que se van creando. Si uno quiere crear una tabla Gold nueva, lo puede hacer directamente desde MCP interactuando con CLOT, que es hoy por hoy lo que nosotros entendemos que funciona mejor. Para crear nuevas tablas. Se genera directamente un token de conexión, y desde el propio Cloud, en un conector custom que creamos como theramo, se conecta el token y desde ahí se gestionan las tablas y se crean nuevos

**Romano Bazán, Ayelen**: reportes ahí consulta, o sea, sí o Sí para usar Theramon tenemos que tener usuarios o en Cloud o en ChatGPT. ¿No nos podemos usar directamente usuarios de pago, No?

**Lucio Rojas**: ¿Sí o sí? No, Por eso quería proyectarlo. Quiero mostrarles esto, que nosotros entendemos que es la mejor forma y alentamos a usarlo. Y en caso de no tener un usuario de Cloud o de chatgpt, se gestiona directamente desde la web, no es restrictivo, voy mostrando las dos formas en paralelo, si entendemos las diferencias, Acá lo que hacemos es por MCP gestionamos la herramienta y te lista cuáles son las distintas tablas que tenés, cómo se relacionan, cuando uno pide un nuevo análisis, clop, les va a preguntar a ustedes qué tipo de análisis quieren generar, cuál es el objetivo, le sugiere distintos tipos de de relaciones o vinculaciones para una nueva tabla y las ejecuta creando el SQL en Telamot y deployando esa tabla que después se puede volver a consumir desde Cloud o desde alguna otra aplicación de BI como Power BI por ejemplo. Entonces yo le pedí que me liste las tablas, me va diciendo bueno tenía una tabla de fax, tenés tablas de fax, que tenés una Go Silver con tantas columnas, la tabla significa tanto, podés pedirle que explique la tabla y cada una de las columnas, esto para hacer un poco más de diagnóstico de que tenemos conectado y se puede pedir que te sugiera alguna nueva tabla, algún tipo de análisis, por ejemplo si quiero analizar ventas históricas, Acá si vayan haciéndome preguntas, vamos respondiendo en un momento, pero entiendo que cuando se conecten herramientas, ya sean ustedes quienes tengan que generar los reportes, por ahí se amegan un poco más.

**Schmidt, Nicole**: Esto sería la forma sí o sí, teniendo licencia y cloud digamos y la otra forma cuál sería, o sea si no, igual estamos viendo de tener la licencia, pero no sé ahí como venimos, pero para poder empezar a ver lo otro sino

**Lucio Rojas**: bueno, termino en un minuto de explicar esto, te sugiere cuál es la nueva tabla, cuáles son los cruces, te dice qué tipo de preguntas puedes responder y bueno acá la experiencia es mucho más amigable tanto para usuarios técnicos como para técnicos, porque se puede burlar, pedir sugerencias y demás. Una segunda opción, este es un caso de uso que les creé, donde ya tienen los usuarios vinculados, caso publicitario, por si quieren lo vemos en una segunda opción se pueden generar nuevas tablas directamente desde Telamo de dos formas, una es con un agente de inteligencia artificial que también responde, por ejemplo. Este es un agente interno que tiene desarrollado Dynamo, usando las APIs, de ahí todas, no sé si es un modelo de OpenAI o de plot, no estamos cor.

**Tomas Teramot**: OpenAI, cómo estamos trabajando con OpenAI,

**Lucio Rojas**: este es un agente que también uno puede interactuar con el agente decirle, bueno, ¿Qué tablas tengo, ¿Qué tipo de reportes puedo crear para analizar ventas? Y te sugiere tres tipos de análisis. Se pueden hacer preguntas mucho más exploratorias, se pueden relaciones y demás. Yo quiero hacerlo un poco sencillo para no detenernos mucho ahora. Por ejemplo, si yo le pido este reporte, Directamente crea la o hace el SQL, vincula las tablas y ya deploya STL que se mantiene actualizando. Esta es una de las formas de crear un nuevo reporte. No sé si esta les parece más viable o si lo haría más por Cloud.

**Schmidt, Nicole**: Ahí nosotros tendríamos que analizar el uso de Cloud, digamos, porque hay un límite con el tema este de los créditos de Cloud y todo eso. Tendríamos que ver cuál sería el consumo. ¿Ustedes tienen un consumo promedio? ¿Saben algo de eso? Porque, bueno, ahí tendríamos que ver el tema de licenciamiento para esta herramienta.

**Lucio Rojas**: Bien, la pregunta puntual es si te deja sin tokens rápido o no usar. Después hay que revisar este. No, generalmente no tiene un consumo desmedido de tokens. Lo uso casi todos los días a Téramo desde Cloud y no me deja sin tokens directamente. Después le pregunto a los chicos de EI cómo son los consumos, pero es un consumo normal.

**Schmidt, Nicole**: OK.

**Romano Bazán, Ayelen**: Sí, porque ahí también hay que ver esto que hablamos antes. Si agregamos a los usuarios del laboratorio y demás, ellos tampoco entiendo que tienen cuenta.

**Schmidt, Nicole**: Claro.

**Romano Bazán, Ayelen**: Así que ahí, bueno, habría que revisarlo o ver si podemos usarlo así de esta manera directamente.

**Schmidt, Nicole**: Igual acá podríamos usar un mismo token de Cloud. Por más de que nosotros tengamos una sola licencia, podemos conectarnos con el mismo token. Ponele, AYA y yo podemos usar el mismo.

**Lucio Rojas**: El mismo token de Cloud.

**Schmidt, Nicole**: Ahí como la misma licencia de Cloud, si nos podemos compartirla y conectarnos con theramon con la misma licencia.

**Lucio Rojas**: Creo que se tienen que conectar cada una de sus cuentas personales. Ahí un poco la solución que creo que estás planteando es compartir una cuenta personal, siendo que se pueden las dos al mismo tiempo. No estoy tan seguro de que sea lo ideal por el consumo de créditos.

**Schmidt, Nicole**: Claro. Lo vamos a llenar más rápido. Más rápido. Sí, sí, sí. ¿Se entiende? Sí. Bueno, nada, eso nos queda como de definir y analizar para ver. Entiendo que es mejor conectarlo desde el cloud.

**Lucio Rojas**: Sí. Una tercera forma, que es como lo hacíamos antes, el que se cree todo el protocolo MCP, es agregando una nueva tabla. Agregando una nueva tabla Gold, desde Tablas lista todas las tablas silver que ustedes tienen conectadas de su warehouse staging. Te hace una descripción de cada una de las tablas, te muestra cuál es cada una de las columnas que tienes vinculada a cada tabla, y vos seleccionás con las que querés trabajar en este nuevo reporte. Una vez las seleccionás, haces una descripción de cada uno de los requerimientos funcionales que tiene que tener una nueva tabla. Por ejemplo, unir determinada tabla con otra determinada tabla a partir de tal campo. Después calcular por año y por mes y por producto, la categoría y la subcategoría. Calcular unidades vendidas como la suma de las cantidades. Todas estas descripciones en realidad no las escribimos nosotros, sino que la escribió Claude adentro de theramov, a partir de interactuar con esta interfaz. Por eso se recomienda que es mucho más intuitivo hacerlo desde acá. Y uno a partir de decirle, quiere una tabla que analice las ventas históricas, te haga toda esta descripción de requerimientos funcionales y después te genere la poli SQL, A tener que uno sentarse a pensar cada uno de los requerimientos que le da para que después te haga una conversión SQL. Asimismo, las instrucciones que le puedes dar también pueden ser más genéricos. Yo creo que le hace alguna

**Schmidt, Nicole**: todo esto que te apareció acá fue porque lo conectaste con Cloud, digamos.

**Romano Bazán, Ayelen**: Tenemos que mostrar y escribir cada paso, o sea, calcular unidades.

**Lucio Rojas**: Si, esa es la diferencia. Aunque la descripción, los requerimientos, también puede ser mucho más genérico. Acá lo hizo muy detallado porque Claude es muy bueno haciendo esto y por eso lo usamos con MCP. Pero si no puedes decirle, bueno, necesito un reporte que me analice ventas históricas, o que me analice ventas por tal categoría en tal sucursal. Estoy yendo siempre a un caso de retail, su caso de uso será distinto, pero la gente de modelado también va a generar una QL en base a cómo entiende que se relacionan las tablas. Pero bueno, la otra forma honestamente es mejor. Así que podemos ser, si se puede llegar a hacer desde Cloud, mejor. Y bueno, si no, nosotros le vamos a dar soporte para que igual sea una buena experiencia, No va a haber problema por ese lado.

**Romano Bazán, Ayelen**: Y hay una consulta, perdón, con respecto a las cuentas de Teramond que vos dijiste, bueno, nos vamos a loggear y demás, ¿Esas cuentas cuántas serían? Son individuales no las podemos compartir. Sí. ¿Cómo funciona eso?

**Lucio Rojas**: Este es su caso de uso. No sé si apunta alguien más, escucha una voz. Este es un caso de uso donde aresha ustedes dos y

**Schmidt, Nicole**: ah, sí, me llevo un email a mí, no sabía si que tenía.

**Lucio Rojas**: Se tienen que seguir el email, seguir los pasos y una vez hagan el túnel, acá van a aparecer sus fuentes de datos. La verdad que en esta prueba de concepto nosotros queremos alentar a que lo usen y que la experiencia sea satisfactoria y que no tengan límites. Así que pueden conectar la cantidad de cuentas que pueden conectar, la cantidad de cuentas que quieran. Lo que sí se puede hacer es, por ejemplo, si ustedes a nivel sistemas quieren tener más como una etapa de administración y generar maestros y no exponerle todos los datos a todos los usuarios, se pueden crear distintas instancias de use case, donde la fuente de un próximo use case. Sea una tabla que ustedes hayan creado anteriormente. Se entiende esa abstracción como haciendo distintos ambientes para cada uno de los usuarios que ustedes les dan la prueba. Por ejemplo, si con él dan estas dos personas que trabajen no con toda la información, sino con algunas tablas que nosotros ya les dejamos para que prueben,

**Romano Bazán, Ayelen**: Ahí limitaríamos los datos. Pero en cuanto a funcionalidades, todos los usuarios tienen las mismas.

**Lucio Rojas**: Sí, por ese lado, sí.

**Romano Bazán, Ayelen**: ¿Hay alguna manera de solimitarlo o no?

**Lucio Rojas**: Sí, lo que se puede hacer es, si alguien quiere consultar la información, se le puede dar solamente ese acceso a través de un chat donde le puede hacer preguntas y es una suerte de chat eso lo que ofrecemos. Y si no, la forma que estamos usando ahora es también consumirlo desde cloud, donde con el MCP y con una conexión a diversas tablas, se le puede pedir a Teheramot que te genere reportes, que te genere dashboards, que te genere informes y demás. Mi recomendación por un lado, es que estoy compartiendo infinito hoy en día, un poco la mejor experiencia, la mejor práctica para usar Telamo pasa por comentar honestamente. Así que por dos circunstancias. La primera que es el modelado de tablas, que mucho más ameno que en RCP, y el consumo sobre todo, porque si hoy en día uno quiere consumir las tablas que generó solamente desde telabox, sin conectar algún LL, se puede hacer a través de un chat interno que nosotros proporcionamos, donde puedes hacer preguntas a los datos y haz una query a las tablas y te devuelve la información que le pedís, o conectándolos a herramientas de BI. Y entiendo que eso, no se, sale un poco de lo que ustedes ya tienen, entonces quizás agrega menos valor. Y por el contrario, conectarlo a Cloud te abre un universo de posibilidades bastante más amplios, lo que es consumo, puedes pedirle que te genere dashboards en el momento, que te genere informes, hacer análisis exploratorio con la data y demás, que bueno, cambia mucho la experiencia. Así que no sé cómo lo ven ustedes, si creen que se puede gestionar.

**Juan - Teramot**: Hola, Sí, acá estoy, hace un rato lo escuchando. Hola, Hola, Disculpen, me sumé más tarde, salí recién de otra reunión ahí. Aye Niki, la idea, lo más poderoso es esto último que mencionaba Lucio, tener el acceso mediante un LLM ya con Cloud. Todo lo otro se puede, requiere otros tiempos, requiere otro camino, requiere otra pericia, pero desde Cloud es todo muchísimo más simple, mucho más detallado, es más fácil hacer traveshooting, cuando hay alguna duda, se le pregunta al LLM, explícame lo que hiciste, contame en detalle, describime la fórmula. Y la experiencia para el usuario cambia radicalmente, hasta pensándolo en el usuario final de la reportería del laboratorio, que ese era uno de sus miedos, que por ahí cuando lo tenían conectado el cubo con Excel, le pedían un dato y le traía todo el histórico, porque no había restricción de fechas o era implementado de otra manera. Bueno, ahora ese usuario todas esas cosas las puede usar prompteando, necesito los informes de soja tal calidad de tal campaña, tal campaña. Bueno, es un prompt y se lo trae. Entonces los acompañamos en cualquier implementación. Pero lo que radicalmente define y cambia la experiencia es a través de un LLM de preferencia. Claud, ya escuchaba que estaban bien con el tema de las licencias. La última vez que me junté, Diego me dijo, estaban hablando de eso, estaban viendo cómo implementarlo dentro de toda la organización. Pero realmente hoy sería muy importante si ustedes pueden contar con una, si la comparten con Ayelén y Niki, es tener un usuario y contraseña, que lo sepan las dos, un correo genérico y listo. ¿Como poder hacerlo? Pueden, se desconecta una, se conecta a la otra, pero definitivamente es la experiencia más rica de UCI.

**Schmidt, Nicole**: OK, lo vamos a pedir, No depende de nosotras. A mí me encantaría.

**Romano Bazán, Ayelen**: Alguien tiene que pagar.

**Schmidt, Nicole**: Claro,

**Juan - Teramot**: sí, A ver, es un gasto de caja chica, son 30 pesos por mes, pasa como Pinocho por detector de metales, no se entera nada.

**Romano Bazán, Ayelen**: Sí, ahí lo que más nos preocupa es eso, el consumo y después con las restricciones que tenga la cuenta, cuánto se van incrementando esos costos. Eso es más que nada entender eso.

**Juan - Teramot**: Restricciones de la cuenta por el lado de Claude.

**Romano Bazán, Ayelen**: Claro, la cuenta de Cloud, de lo que vayas reprocesando y cuánto lo usen, cuánto el tema de los token y demás, cuánto se vayan gastando, cuánto necesitemos, cuánto.

**Schmidt, Nicole**: En bolsa tenemos mucha burocracia para pedir algo, tenemos que levantar, no es fácil. Sí, sí, entonces tenemos que ir con todo, como ya tener en claro cuánto,

**Juan - Teramot**: a lo mejor es más fácil y pedí la de 100 de una y se olvidan cualquier potencial. Bueno, hay una salida a cenar de equipo, la justifican. Pero te digo, con usuarios intensivos, recién esto fue ayer, ayer a la tarde me dijo un usuario intensivo que lo está estrangulando a Cloud, me dijo hoy fue la primera vez que me salió, se le había agotado el límite de procesamiento de una herramienta, pues también, no quiere decir que no lo pueda seguir usando, pero por ahí una herramienta de todas las que usa Cloud no se puede seguir usando y tenía que esperar dos horas para que se le libere el uso, pero venía acumulando uso intensivo con una base de datos que están manejando catorce, quince GB, la data que ustedes nos comparten creo que era menos, y bueno, y también va a depender el uso. Y hay algo que esto también lo sabe antropic, lo sabe OpenAI y están laburando en todo esto, algoritmos, bueno, Tommy por ahí tiene más precisión de vocabulario, tipo de compresión, para que sea más óptimo el uso de esos toques y realmente rinde porque les pega a ellos también, o sea, por 20 dólares hacen un gasto infernal y no les cierra el negocio. Entonces es una tecnología que también está evolucionando, o sea, esto es hoy, probablemente en un mes, dos meses, sea otra la realidad del consumo de los LLM, o sea, no se lo planteen como una restricción de uso futura. Hoy, hoy existe, sí, pero probablemente en un par de veces no esté más. Dale Lucio, me muteo porque aburrido en el auto.

**Lucio Rojas**: Hay algunas, dos, tres cosas que las funcionalidades que nosotros ofrecemos desde Teleamot, son exactamente las mismas. Una vez que Telamot va a tener más o menos acceso por trabajar con Cloud, la experiencia va a cambiar por los tokens. No va a pasar una licencia de 200, se vuelve de 20, se vuelve una de 200. Porque nosotros trabajamos con metadata, o sea, le estamos dando un archivo de texto plano en realidad a Cloud y unas herramientas. Entonces no es que está trabajando una base de datos, es un poco el diferencial. También queda Theramo, que si uno tiene que cargarle CCB, le cargas un CC infernal, te quedas sin toque en la primera cuelli que se corre. Entonces es un poco la solución que nosotros encontramos y en lo que se basa el poder de la herramienta. Y después, para todo lo que es buenas prácticas de utilización de tokens, nos volvimos un poco expertos. Decir bueno, arranca un chat de vuelta todos los días, no uses mucha memoria, no repreguntes, no le digas, retomá la última conversación, porque te lee la conversación entre ella te queda sin token a la segunda pregunta. Esas cosas también podemos ir dando una mano en caso de que avancemos por ese lado. Y después lo que sí podemos alentar es que se puede probar, confirme, se puede probar sin tener la licencia. Si ustedes entran a Cloud, o sea sin una cuenta, no pagan nada y se conectan a Terramotor NCP, pueden hacer algunas preguntas. Lo que sí es que te limita, ahí sí a dos o tres preguntas después te dice hasta llegamos. Pero bueno, al fin y al cabo una licencia de 20. 20 dólares, una llama, pero también sigue consciente de lo que está. Si se llegue por ese camino, que nos sobrarían los tokens después de revender. Creo que si llegamos a poder incurrir en ese ese pedido, va a ser un game changer. Así que bueno, no sé, para que esté claro de nuestro lado que el servicio va a ser el mismo que nosotros ofrezcamos, la experiencia va a cambiar, pero en los dos casos la vamos a acompañar hasta que entendamos que llegamos a algo exitoso. Así que bueno, creo que, no sé si ustedes tienen preguntas puntuales, algo de herramientas, algo de conseguimos, ¿No?

**Schmidt, Nicole**: El próximo paso sería entonces armar una reunión más con Aníbal para ver la conexión y ya ahí empezaríamos, bueno, después definiríamos también una reunión de seguimiento semanal digamos.

**Lucio Rojas**: Sí, hagamos los celulares quieren todos los martes a esta hora, nosotros podemos, fijamos si quieren hacer las primeras de una hora, después cuando ya entremos en otra dinámica de 30 minutos como para seguimiento, también eso está incluido y lo vamos manejando. Bueno, ahí entonces para las conexiones dejamos a la gente de sistemas, no sé si ustedes se auto perciben como sistemas o no.

**Romano Bazán, Ayelen**: No, pará, somos el sistema, estudiamos esto,

**Lucio Rojas**: ayer estábamos haciendo la conexión con otra empresa y le digo, bueno, lo sumo al sistema, al mail y mandó un mail, pero creo que yo tardé 10 minutos en leer el mail. Y entre eso se conectaron a la base de datos, no necesitaban reunión, Lo sumamos a los chicos, a las cadenas para que. Y si hace falta ponemos una reunión para charlar y una vez con los datos conectados, no hace falta hablar sobre el aire, sino que nos ponemos a trabajar en eso.

**Schmidt, Nicole**: Genial, buenísimo.

**Lucio Rojas**: Bueno, perfecto. Entonces seguimos así. Por lo pronto nos vemos el martes que viene, si les parece.

**Juan - Teramot**: Con Aníbal, ¿Cómo hacemos? ¿Lo conectan a Tommy directamente, los ponen en contacto o el martes que viene?

**Lucio Rojas**: No, no, trabajamos entre semana

**Juan - Teramot**: y ahí

**Romano Bazán, Ayelen**: van a mandar un mail con lo que necesitamos y ahí lo copiamos, Aníbal, para que lo empiecen a ver.

**Juan - Teramot**: Ah, listo, Dale, dale, dale. Sí, si, hagamos así, puede ser. Esa es la. La principal traba, la principal restricción.

**Lucio Rojas**: Si llegamos al map que viene con todo conectado, sería éxito rotundo. Y bueno, si no, hacemos una reunión para ver cómo está eso.

**Schmidt, Nicole**: Bueno, y nosotros hacemos la tarea de buscar alguna licencia de cloud, robar algo, vamos llorar.

**Juan - Teramot**: Por ahí Diego tiene ganas.

**Schmidt, Nicole**: Sí, sí, sí, sí. Diego ya sabemos que nos dice que sí, o sea, nosotros mandamos un email, manda el aprobado, pero bueno, tenemos que hablar.

**Juan - Teramot**: El primer equipo en usar IA de verdad, en la BCR. Eso de verdad

**Schmidt, Nicole**: estaría bueno.

**Juan - Teramot**: Obvio, es. Ya está, ya estoy viendo el cartel. Vamos, vamos, equipo.

**Lucio Rojas**: Y si, no, yo arranqué al revés, cuando tenía tantas ganas de usarlo, me lo pagué yo y después lo fui a reclamar, hice la inversa, así que me lo dieron porque si no me iba a quedar. Después lo presten la bolsa, tampoco me afectará la economía. Bueno, nos vemos. Perfecto.
