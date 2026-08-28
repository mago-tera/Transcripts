# Teramot Intro Meeting (Diego Gismondi)

**Fecha:** 2026-05-21T17:01:38.001+00:00  
**Duración:** ~49 min  
**Participantes:** Juan Peralta <juan@teramot.com>, Diego Gismondi <diegogismondi@gmail.com>, sandra boidi <>, Lucio Rojas <lucio@teramot.com>  
**Externos:** diegogismondi@gmail.com  
**Apollo ID:** 6a0f46006f9c010010e57937

---

**Diego Gismondi**: La idea era, les contamos un poquito, nosotros somos una empresa acá local, básicamente nos dedicamos a consultoría tecnológica en general, y tenemos varios clientes, pero puntualmente uno ahora, donde hemos encontrado las cosas bastante desordenadas y están haciendo todo un camino bastante sinuoso por tener una especie de. De dashboard, no te digan, tiempo real, porque todo lo que hacen es casi autopsia de datos que ya están quemados de hace varios años, desde hace varias semanas. Entonces, particularmente es una constructora que tiene un ERP clásico, digamos, con base de datos. SQL Server. ¿Era la base, Sandra? Ya ni recuerdo. ¿Recordás un SQL Server? Y después tiene un abuso, te diría, de Excel, que me imagino que no es nada nuevo para ustedes. Un abuso de Excel de todo tipo, porque te imaginarás que una constructora con 400 obreros tiene en cada obra mucha informalidad, trabajo manual. Hay mucho de eso que nosotros queremos automatizar e informatizar y digitalizar. Pero eso va a llevar un tiempo más, porque ahí no hay higa que te salve, digamos, porque hay alguien que tiene que hacer laburo y gente que viene con un martillo en la mano, con lo cual necesitas resolver otras cosas primero, digamos. Pero hay algo que más o menos ordena todo y es una especie de certificado, o sea, ellos trabajan mucho con obra pública, entonces en las licitaciones vos tenés que hacer un certificado para entregar a la provincia. Claro, cada vez que hay que entregar ese certificado, alguien tiene que ponerse a juntar todos los datos que están en todos los lugares que te dije, desde la base de datos hasta los Excel. Entonces ellos lo que quisieran resolver, y nos lo tiraron a nosotros como un desafío, es tener una especie de visualización, un BI, lo que sea, digamos, para poder ver eso un poco más en tiempo real y no tener que esperar a esa certificación para hacerse de todos los datos tan artesanalmente como lo hacen. Entonces cuando ellos plantearon hacer el clásico camino con una empresa de las que construyen BI, que puede ser Qlik Sense o Power BI, que lo están usando mucho, yo le dije a uno de los directores ahí, digo, esperá un poco porque ahora hay otras herramientas y otras cosas que podemos explorar y por ahí hacer esto con una curva mucho más corta y no tampoco romper la cabeza en meter esto en Power BI tomando datos de un Excel que después probablemente nos quede rápidamente obsoleto, digamos. Bueno, nada, ustedes los había conocido por un evento que estuvo en el Polo, creo que había hablado con Bruno en su momento, que fue él el que charló, dio una charla ahí en el Polo, algo muy breve, pero bueno, nada, me acordaba que estaban con este tema y entonces era contarles un poco este caso para ver qué se les ocurre a ustedes.

**Juan Peralta**: Genial, bueno, bueno, interesante, nos presentamos. Bueno, vos Sandra, no sé si querés sumar algo.

**sandra boidi**: No, no, estamos trabajando junto con Diego, intentando en estos clientes poder modernizarlos un poco y también facilitarles lo que vienen requiriendo desde hace años. Les faltan procesos, les falta tecnología y les falta disponibilidad de la información casi online te diría, o ahí media inmediata. Ese es un poco el dolor. Y lo que ellos tienen son procesos antiguos, muy fragmentados también entre áreas. Y bueno, nada, el desafío es poder ver, les podemos dar y que les dure un poquito, unos años más.

**Juan Peralta**: Bueno, bueno Lucio, ¿Vos quién sos?

**Lucio Rojas**: Una buena pregunta. No todo el tiempo. Bueno, yo trabajo junto con Juan en Theramot, un poco en la parte comercial, un poco en la parte de acompañamiento, en la implementación de soluciones a clientes, a partners en este caso, así que si avanzamos vamos a estar muy en contacto, me gustó mucho la idea. Nosotros tenemos, después vamos a contar mejor, pero a veces puede servir y un poco alzar toda esta reportería, así que buenísimo el caso, lo que me cuentan.

**Diego Gismondi**: Ya que dijiste eso, te agrego una cosa más, Juan y Lucio, o sea, en este caso lo estamos haciendo contra un RP que es Calypso, que es uno de los tantos RP que están dando vuelta por el mundo, por lo menos en esta región. Eso no quita que en otros clientes tengamos otras situaciones muy parecidas. Por eso nos gustaba escuchar qué es lo que ustedes pueden ofrecer, porque además somos partner de Odoo, y si bien no es nuestro core, digamos, tenemos implementaciones de Odoo con productos propios nuestros que podrían ser muy positivas a la hora de ofrecerle al cliente un ecosistema de herramientas, además de la consultoría. Te ofrezco esto otro, digamos, porque hoy pasa mucho esto, las herramientas existen, los datos están todos dispersos y no hay nada que junte todo eso y hacer la curva larga de contratar, traer un desarrollador, un senior que arme un BI. Lo más costoso de eso no es el senior, lo más costoso de eso es que ese senior probablemente no entienda nada del negocio, no sepa, le tiene que explicar que es un plan de cuenta, le tiene que explicar qué es lo que una gestión contable, que es un cash flow, que es un aging de deuda, o sea, y no podés estar explicándole eso a un desarrollador. Entonces eso es lo más costoso y a nosotros eso se nos repite n veces en todos nuestros clientes. Acá yo te planteé un caso con este cliente que es muy grande y demanda mucho, pero tranquilamente lo podríamos aplicar a todos nuestros clientes. Digo esto por lo que decía Juan, de cuando él hablaba de partners. Si nosotros podemos lograr trabajar con ustedes, podríamos ir a más de un cliente. Eso quería decir.

**sandra boidi**: Sí, laboratorios, Diego. Laboratorios, exacto.

**Diego Gismondi**: Tenemos muchos laboratorios bioquímicos en el ámbito de la salud, tenemos varios clientes, digamos.

**Juan Peralta**: Bueno. Sí, sí, sí, sí. Bueno, viene bien toda la introducción. Bueno, yo estoy con Lucio, estamos en el área comercial e igual que Lucio, haciendo un poco de preventa, venta demo, apoyo a clientes en las primeras interacciones. Así que tenemos varios sombreros que usamos constantemente, como suele ser en empresas como Theramot, que estamos en pleno crecimiento y en pleno movimiento. El planteo que nos hacen de datos fragmentados, múltiples orígenes de datos y necesidad de información, es donde, digamos, por lo que nace, una de las cuestiones por las que nace TENAM, porque muchos de los problemas de las organizaciones, y sobre todo al querer aplicar algo, alguna herramienta de inteligencia artificial, es que no tienen los datos en el orden o en la forma ideal para que un agente o una solución los pueda utilizar y ser productiva. Dentro de nuestra postura, por lo que es útil nuestra herramienta, vemos que la parte de organización de la información es la que lleva más tiempo, que es lo que vos me decís, los Excel, el ERP, juntar los distintos orígenes. Entonces ahí nosotros, los agentes que componen la solución, muy efectivamente se ponen a trabajar y esta primera parte de ese proceso de trabajo, que constituye casi el 80 por ciento, que es entender los datos, entender el diagrama de ERP, las planillas, todo lo hacen agentes. Y en vez de tener un 20% para hacer análisis y hacer el cash flow, ya directamente, el trabajo más duro y que es el menos importante para el negocio, pero que se transforma en el más importante por la cantidad de tiempo que lleva, se hace muy rápido y queda todo el resto del tiempo para hacer el análisis, que es lo que realmente agrega valor. Así que esta ecuación de 80-20 se invierte y queda 20-80. Hay una cuestión acá de modelo de lenguaje, que es donde nosotros nos apoyamos para trabajar, donde está armada nuestra solución. Es que los modelos de lenguaje son buenos, pero con datos, con texto, con imágenes, etc. Pero no, por ejemplo, para trabajar con una base de datos, lisa y llanamente, la ventana de contexto no soporta el tamaño de una base de datos. No fueron entrenados con base de datos, porque las bases en su gran mayoría son privadas y no estuvieron disponibles como estuvo todo este material al cual se pudo acceder para entrenar a los modelos. Entonces, en theramo lo que nosotros hicimos acá, como bien dice el slide, no se diseñó para esto, pero theramon sí, es poder conectarnos al origen de datos, ya sea una planilla de Excel, ya sea una base de datos MySQL, SQL, Aurora, Dynamo, si están en AWS, SAP, Oracle, Salesforce, bigquery, tenemos muchos conectores desarrollados, sobre todo a las bases, a lo que es mainstream, o sea, las más importantes. Y nosotros entendemos el modelo de datos, los agentes entienden el esquema, entienden la relación entre las tablas, se hacen como una foto de lo que representa esa base de datos y ya infieren a través de esa metadata lo que significa ese negocio. Entonces, cuando llega el momento de contextualizar una pregunta, no hay una alucinación, porque ya se entiende sobre qué se trata. Entonces, si viene una pregunta o una consulta para armar un modelo de datos que pueda responder un requerimiento de ventas, bueno, ya está construida esa metadata para entender lo que significa ventas dentro de esa base de datos. Y no es solamente un agente haciéndole una consulta al catálogo de la base de datos buscando, no sé, SELECT FROM DATABASE where catalog, entre porcentajes ventas, o sea, tratando de buscar algo que referencia ventas, sino que hay ahí hay un entendimiento y en base a eso se construye nuestra solución. Bueno, hay agentes que trabajan en dos etapas. Una, ordenamiento y limpieza de los datos, que a veces es necesario, otras veces no es necesario. Si la base de datos está ordenada, no hay cuestiones de ANSI o de caracteres que estén mal persistidos, no pasa nada acá, o sea, no hay agentes que arreglen formato de fecha si están bien ordenados. Pero si tenés un archivo que te lo mandaron de Estados Unidos con mes día, y tu base de datos está en español con día mes, bueno, hay una gente que se da cuenta y unifica esos formatos de fechas para que tengan sentido, porque para una lista de datos es una tareita que lleva un poco de tiempo. Y después, bueno, los agentes que pueden trabajar en el modelado de datos, permita ser nuestra solución. Ese modelado de datos, con respecto a lo que ustedes nos planteaban, era empezar a construir los sets de datos que van a responder a esa necesidad de un tablero, a los dashboard, a los KPI's, al reporte que le tienen que mandar a la provincia, porque seguramente tiene una estructura, tiene que hacer totales, agrupar, categorizar, separar, etc. Entonces todo ese modelado se encarga de ser un agente donde uno en lenguaje natural le explica tengo que hacer, o si querés le puede hasta poner la foto y decir, mirá, con la data de Tenet vamos a empezar a armar un reporte que sea como este, y va a armar el modelo de datos que va a responder a ese requerimiento. ¿Hasta acá vamos bien? Sí, sí, la solución está montada sobre AWS, trabajamos con bases de datos, podemos trabajar con varias bases de datos al mismo tiempo, distintos orígenes, puede ser en MySQL y en SQL Server y una planilla de Excel, los tres orígenes de datos en una misma instancia. Se genera un data lake con toda esa información y a partir de ese data lake se empiezan a construir los casos de uso para responder a las diferentes necesidades que ustedes tengan que atender, tengan que responder. Nosotros inicialmente, inicialmente, por defecto, la solución está planteada para que todo ese trabajo se haga en nuestro tenant, en nuestro AWS, en nuestro espacio de Cloud AWS. Pero si ustedes tienen su tenant de AWS y dicen, no, mira, yo tengo información acá que la cargo, o el cliente con el cual ustedes trabajan ya tiene algo en AWS, tranquilamente nos podemos conectar ahí y hacer todo el camino por el tenant del cliente. Cuestiones de privacidad, estamos certificados en Softdog, estamos trabajando, que es el estándar más alto de privacidad, información, y estamos trabajando en la certificación de la ISO 27001. Brevemente, ese es el pantallazo técnico y descriptivo, después yo les puedo pasar esta presentación para que la tengan de referencia con respecto a lo que es Telama. Ahora voy a dejar de compartir, así los vuelvo a ver y ahora sí charlamos un poquito de este caso. Conectarnos a la base de datos de ese ERP, o sea, no representa un problema, es cuestión de accesos, usuarios, etcétera. Luego el tema de los excels, eso sí tiene una particularidad, porque los excels nosotros los trabajamos a medida que se van cargando, entonces ustedes teóricamente los van actualizando diariamente, van generando registros de esta empresa y llega un punto donde tiene el Excel completo y en base a esa información y la que tienen las bases de datos, le tiene que generar el reporte a la provincia, quedémonos con ese caso. Llegado esa instancia se hace el outload del Excel y se empieza a iterar a través de nuestro MCB para generar el modelo de datos que responda a lo que ustedes tienen que generar, o sea, tipo decir, no sé, en el Excel a lo mejor decir cualquier cosa, tienen los materiales que se consumen en una obra y en la base de datos tienen como parte del ERP, no sé, cuestiones de personal, horarios, no sé, y hacen ese cruce, bueno, con el modelado nuestro van a poder construir ese dataset que va a responder a esa ganancia. Yo necesito saber de los empleados que intervinieron en la obra, código 24, todos los días que asistieron, ayúdame a calcular, tráeme el sueldo, el jornal que le corresponde, si estuvieron ausentes, si se lesionaron, que entró en la RT, y tráeme toda la cuestión de materiales que sean asociados a esta obra. Y se empieza a iterar y se empieza a construir ese modelo de datos para hacer en este caso, la presentación que tienen o la analítica necesaria para entender mejor la obra. La obra estaba planificada en 20 días, tardó 40, ayúdame a entender qué pasó, no sé, a lo mejor en esa analítica te aparece que durante cuatro días se quedaron sin cemento, bueno, hubo cuatro días delay porque el camión, las bolsas o el camión con el cemento no llevó tiempo, etc. Y ahí vas viendo.

**Diego Gismondi**: Ahora sí, sí, no, perdón que te interrumpa, yo una de las preguntas que tenía es ese scrapping de información, digamos, cómo es, o sea, la plataforma, lo haces una vez y es el típico como si lo harías con un cubo que preparas de Qlik Sense o de Power BI que vos tenés que armar, más allá que obviamente nada es mágico, le tiro 20 excel en un repositorio y que me los explore solo. No estoy hablando de eso. Podría hacerse, digamos, pero digo, no estoy hablando de eso, lo que digo es hay que sentarse a explicarle qué es cada campo, cómo funciona esa parte que es la más laboriosa y la que entiendo yo que en la curva de hacer un BI es la que más tiempo lleva.

**Juan Peralta**: Ese entendimiento lo hacen los agentes. Ahí está el poder de no. Entonces ahí hacen la foto de toda la información que está entonces con lo que está en el Excel y contra lo que está en la base de datos. Y como decías lo de Qlik Sense, esta idea de cubo es el data lake, se va generando autónomamente con toda la información que se le comparte y después bueno, a través de Cloud o ChatGPT con nuestro MCP empieza a interactuar con todos esos datos y empezás a generar, pero con lenguaje natural, no tenés que aprender a programar en Clicksense, acá no programas, acá pronteás,

**Diego Gismondi**: querés ver un estado de resultados, podés prontearlo así a ese nivel.

**Juan Peralta**: Bueno, si vos le decís che, hacemos un estado de resultado en base a la resolución técnica 48-37 del Colegio de Profesionales de Ciencia Económica de la provincia de Santa Fe y todo, algo va a ser. ¿Pero por qué? Porque nosotros podemos acceder a la información que vos tenés. Si en SRP está la información contable, toda la información que necesita y el modelo de lenguaje con lo que nosotros trabajamos en este caso ChatGPT o Cloud, tiene contexto de qué significa un estado de resultado de la ley tanto.

**Diego Gismondi**: Pero lo tenés que definir vos como empresa qué consideras costo indirecto directo.

**Juan Peralta**: Sí, eso sí, hay cosas que sí, a ver, te va a proponer, te va a ayudar y te va a acelerar de una forma que vos va a decir che, esto funciona rápido, se va a dar cuenta de cosas y tiene inferencia y tiene contexto. Pero lo bueno de todo esto es que más allá de que el punto por ahí no es generar un estado de resultado, pero no hay alucinación porque va a buscar sobre tus datos. Entonces ahí directamente nuestro guardi, nuestra contención es que tus datos, tu base, tu sexo da diez. Da diez. ¿La otra parte decirle, hemos tenido cosas mágicas, decirle che, por ejemplo con un ejemplo de un comercio, un retail,

**sandra boidi**: un

**Juan Peralta**: comercio minorista que vende ropa, o sea con una base de datos de ejemplo, dijimos che, me armás dos reportes, uno de cesta de compras, o sea una canasta de compra donde si normalmente los clientes compran A, cuál es la tendencia a comprar B? Y que hagan toda esa relación. Y el prompt fue haceme un market basket análisis, pero se puede decir en español, en el idioma, como quiera, el modelo de lenguaje te lo entiende. Y después la otra puede hacer y hacemos un análisis de RFM, que es un análisis de cantidad de compras en un periodo de tiempo, frecuencia, cada cuánto compra y del monto que se gasta en esa compra, Recency frequency y money análisis. Y por ese Trump quiero un análisis RFM y quiero un análisis de compra en base a mis datos de mi retail y en un minuto y medio estaba. Y por detrás nosotros te mostramos la query, nosotros mostramos el código SQL que se hace. Eso es totalmente transparente. Totalmente transparente, totalmente auditable y te muestra un choclo de una query de 200,

**Diego Gismondi**: 300 líneas ahí respecto a eso tengo un par de preguntas, Juan. ¿La primera es más allá, después vamos a la parte final digamos de tema de cómo lo venden ustedes y demás, pero digo, cuál es el equipo que necesitas de contraparte y cuál es el equipo que tenés que poner vos para hacer esto, o es simplemente les pasamos los repos, digamos, conectas contra los repos de la compañía y ya está, digamos, o requiere de que exista un analista que primero indague todas las cosas con la empresa, vea procesos, etcétera? Cómo es un poco esa parte, digamos. Esa era una pregunta. ¿Y la segunda? Y la segunda tiene que ver, ya me lo olvidé la segunda, pero con algo que dijiste recién respecto al SQL, si ustedes hacen esto, ya me acordé, estaba hablando despacio para que venga mi memoria, digamos, si ustedes hacen esto directamente sobre productivo o están acostumbrados a. ¿No sé si che, separo esto, viste que en el típico BI lo que hace es, se corre fuera de horario, una extracción de datos, lo dejas en una base espejo y después el BI consume de ahí, digamos, la pregunta es cómo lo hace Theramo en tiempo real o realmente usas un espejo?

**Juan Peralta**: Bien, voy a trabajar adelante así me acuerdo la primera, me olvidé, hacemos una copia y son dos detalles, nosotros no hacemos tiempo real, no hacemos streaming, porque una vez que capturamos el dato, pasa en esa suerte de ETL, de pipeline, de transformación, no está, más que nada el impacto mayor es de la lógica de negocio para che, con todos estos datos que me dieron sueltos de la tabla de venta, la tabla de costo, de medio de pago, así tengo que armar este dataset de salida. Eso se hace una sola vez. Después una vez que el dato queda determinístico, no interviene más ningún agente. Una vez que hay refresco de datos correctamente y tener los resultados expuestos del otro lado y ese refresco, nosotros tenemos un scheduler, decimos che, una vez al Día a las 3 de la mañana, andá y tomá las novedades de lo que vos me digas. Una copia espejo. Si vos decís, che, yo quiero estar ultra tranquilo, no quiero que le pegue al transaccional nunca, listo, vamos ahí. Y si es el transaccional lo hacemos, pero en un momento donde no haya actividad. Y la recurrencia de ese proceso se da en base a la necesidad del negocio. Siempre hay un delay porque no es tiempo real. Hay un proceso, hay bases que son chicas, todo depende de los tamaños, pero ponele cosas promedio, base de datos de 10, 15, 15 megas, que vos decís, che, pero bueno, en base de datos es una cantidad de datos interesante. El proceso se hace en tres minutos.

**sandra boidi**: Claro, sí, sí.

**Juan Peralta**: Entonces es muy. No te digo para poner un refresh cada diez, pero una hora me animo.

**Diego Gismondi**: Tampoco lo necesita esta industria.

**Juan Peralta**: El negocio es bastante estático. ¿Te acordás la primera, Lucio?

**Lucio Rojas**: Hacemos equipo. Esto como la conferencia de defensa de los jugadores. Hacen dos, tres preguntas y no se acuerdan la primera sobre los equipos, cómo armar los equipos. Entiendo. ¿La pregunta que va dirigida hacia cómo trabajaríamos entre Tegamot y ustedes como partner?

**sandra boidi**: Con el cliente Y con el cliente.

**Diego Gismondi**: Con el cliente final, digamos. Porque acá habría tres partes. Nosotros en realidad con este cliente lo que estamos haciendo, acabamos de terminar una consultoría de diagnóstico y ahora nos vamos a quedar como. Si todo sale bien, nos vamos a quedar con una especie de liderazgo del sector de IT de la empresa, donde podamos nosotros decirle, bueno, mirá, esta parte la vamos a resolver con Téramot, esta otra parte la vamos a resolver con este otro proveedor. Ese va a ser nuestro rol, digamos, orquestar un poco los proyectos.

**Lucio Rojas**: Nosotros en ese sentido lo que ofrecemos es un SaaS. No ofrecemos un servicio, la herramienta con licenciamiento flat, depende del consumo, depende de la cantidad de tablas que uno vaya generando y cómo lo escale, pero puede ir en orden de plan gratuito de 50 o de 200 dólares, algún plan más custom. No ofrecemos el servicio de implementación. Lo que sí ofrecemos es el acompañamiento y soporte sobre la herramienta, pero tampoco es estrictamente necesario cuando usas la herramienta, porque se vuelve mucho más sencillo a partir de un LLM como Cloud, poder hacer un diagnóstico de información, entender las tablas y pasa más un plano de la intención, decir bueno, necesito construir este dashboard, qué tablas me armonía propio Theramot con Cloth, generas Gold y después se consume. El consumo puede ser desde un Power Beat, a partir de una conexión desde el Warhouse de Teramot, o lo que a nosotros nos encanta es hacerlo directamente desde el Cloud y ya también ahorrarnos la curva de ese Power. No sé si ahí te respondí.

**Diego Gismondi**: Ustedes no pondrían una lista de negocios, digamos, para. Para ningún caso. Eso lo haríamos nosotros directamente con la gente del negocio básicamente.

**Juan Peralta**: Claro, exacto, exacto Diego, para complementarlo, esa es la persona ideal porque va a entender del negocio, o sea, sabe lo que quiere lograr, tiene idea de qué datos son, a lo mejor tiene el número como para hacer validaciones rápidas y tiene un perfil técnico que de nuevo no necesita programar, es cuestión de tener la cabeza para poder promptear y que todos los agentes, toda la maquinaria que hay detrás esté laburando para el público. Como le decimos a Chat CPT, contestame este mail, enter, copio y pego y sale el mail. Es lo mismo.

**sandra boidi**: Creo que lo que más nos. Perdón, creo que los que más nos tenemos que adaptar somos nosotros Diego.

**Juan Peralta**: Sandra, una vez que vos lo ves, o sea el modelo de lenguaje, ya sea bueno por defecto, nosotros trabajamos con Claude porque la verdad los resultados son muy buenos, muy potente el modelo, la propositividad que tiene, te va llevando cuando vos estás con la hoja en blanco, pero si sabes que tenés que lograr un reporte donde se muestre total de horas consumidas, cantidad de personal asignado, no sé, costo de tal cosa, de tal otra, y tener los datos sueltos, los agentes nuestro van, lo buscan, unen y le tiran encapsuladito este paquetito y le dicen a Cloud, che, most datos y Cloud lo escribe. Entonces ah mira qué genial, me armás un PDF con esto que se lo paso al dueño, al CEO de la empresa que tiene directorio, en 10 minutos arma el PDF y se lo manda por correo.

**Diego Gismondi**: ¿Ahí va otra pregunta que emergió de todo lo que iban diciendo, porque hasta donde entiendo la respuesta es casi pantalla negra con texto, columnas, con valores, digamos, en el caso de algunas visualizaciones de estas, requiere de un look and feel específico, digamos, porque vos decís, che, quiero que, no sé, olvídate del certificado para emitir a la provincia, porque eso lo tenés que hacer en el formato del pliego y todo lo demás, pero puede que vos tengas que hacer justamente lo que acabas de decir vos, Juan, una presentación, un directorio, y quieras decir, che, bueno, tengo que armar tres slide y que cada una de ellas tenga ahí como una estética particular, algunos gráficos y esos, o sea, Téramo te da las posibilidades, o sea, lo que arroja, le arroja texto en pantalla, o podés directamente lograr visualizaciones, como por ejemplo un gráfico de los de Power BI o los de Crix?

**Juan Peralta**: Sí, sí, podés lograr ese nivel de visualización, a lo mejor, porque, a ver, porque la visualización la termina construyendo Cloud, o sea, el que hace el gráfico de barra, la torta y todo eso, vos le decís, che, que se parezca a Power BI y te lo va a hacer igual a Power BI. Y si decís, che, en los márgenes o en el pie, poneme la foto del logo de la empresa, de última es un prom más, agregándole, cargándole la imagen, eso ya escapa de lo que nosotros hacemos, pero es la palanca con la cual nosotros trabajamos. Por eso a mí me gustó cuando dijiste, somos una consultora de tecnología, porque en requerimientos por ahí tan específicos como estos, vos, nosotros podemos hacer la parte central del proceso y vos a lo mejor te podés encargar de la inicial, que es la ingesta de los datos. Cuando vos me decías, che, el Excel bueno, y todas las semanas o por obra generan un Excel bueno, a lo mejor es un Excel grande que va creciendo, pero si tenés algo que es más dinámico, bueno, por ahí le podés hacer un mini gestor, un mini formulario que cargue datos en una base de

**Diego Gismondi**: datos, en eso estamos. Bueno, no, no, no, está claro que

**Juan Peralta**: hay todo un ecosistema y pluma y consumimos toda. Y sabes qué yo estoy medio jugado con el tiempo.

**Diego Gismondi**: No, no, estamos

**Juan Peralta**: por ahí para mostrarte algo como para que vos veas la interacción y lo que logra Claude, está como para levantar algo.

**Lucio Rojas**: Lucio 5 Sí, no tengo problema,

**Diego Gismondi**: creo

**Juan Peralta**: que estamos hasta las menos cuarto.

**Lucio Rojas**: Puedo, te ofrezco, si querés, podemos hacerlo genérico, pero te ofrezco que si vos tenés algún set de datos en CSV para probar y querés hacer un usuario, cargarlo y lo vemos en vivo mañana o el lunes o el martes, para mí sería lo mejor

**Juan Peralta**: eso, imagina para que tenga contexto de lo que vos estás necesitando.

**Diego Gismondi**: Antes de eso también estaría. Bueno chicos, así rápido, muy sintéticamente, cómo nosotros podemos, no sé si existe el caso de que seamos partner directamente o nos conviene directamente que el cliente hable con ustedes. La verdad que si me preguntás a mí, depende cómo sea el modelo de negocio de ustedes, o sea, obviamente que prefiero estar en el medio, pero si ustedes dicen no, mira esto va contra cliente final, no hay ningún problema, nosotros acercamos las partes y decimos che bueno mira contratar a los chicos directo y

**Juan Peralta**: ya digamos tenemos un esquema de partners y para nosotros el cliente final va igualmente hacer el caso de uso, va a tener que pagar el fee de la suscripción mensual, etcétera y ahí es donde entras vos y bueno es este cliente, es otro, es otro, es otro, es otro y vamos armando.

**Diego Gismondi**: Por eso la monetización del partner es a través de las suscripciones que hagan los clientes finales, básicamente

**Lucio Rojas**: después vos.

**Juan Peralta**: Claro, y si después vos decís, che pero yo a esta solución como le armé el formulario de carga y le hice el sistema y vos tenés un fi.

**Diego Gismondi**: Que mucho eso, aparte.

**Juan Peralta**: Nosotros somos una herramienta básicamente, entonces por eso esta parte, pero nos damos cuenta de decir, che alguien como vos tiene una consultora, a nosotros nos sirve, bueno, gestionar esto, lo puedo resolver con tela, no sé, conciliaciones bancarias, cadenas, por ejemplo con una cadena de comer, una empresa que tiene varios comercios, hacer la conciliación bancaria de mercado pago, Payway, Getnet, Visa Master, contrapunto de venta y contra liquidación bancaria. Se volvían locos, ¿Por qué? Por una pyme. Y lo hacían a mano, la contadora estaba con los pelos así cada fin de mes dedicándole tres días a ver planillas y bueno, empezaron a cargar los archivos, hicieron el modelito de datos que simplificadamente cruzá A con B, con C, con D, con F y fíjate qué falta. Bueno, cargan los datos y en un rato tienen un listadito, dice che esto está, esto está bien, acá hay un centavo de diferencia, bueno no le voy a ir a reclamar visa un centavo, pero bueno está bueno saber que te deben un centavo todo suma,

**Diego Gismondi**: las conciliaciones son todo un mundo y la cantidad de horas que insumen las empresas en hacer eso es tremendo.

**Juan Peralta**: Facturas de servicios, qué sé yo, hay un montón de cosas que vos podés hacer cargándome el dato, o sea, si vos me tirás el PDF, no hacemos nada, si vos mandás la factura de la F, le tirá el PDF, che, té la moto a ver qué pasa, cero. Ahora, si vos de alguna manera capturás los WO consumidos, la tarifa final, el mes que pagás, etcétera, y sobre eso creas analíticas, si te cobraron dos veces, cómo viene el consumo, el OCR lo

**sandra boidi**: hago previo, lo cr lobo previo y vos tomás el dato. ¿Diego, yo a mí no me queda claro, o sea, Lucio mencionó el tema de SAS y las licencias, pero vos te queda claro los costos?

**Diego Gismondi**: Porque no lo vimos, si quieren contarnos eso, después vemos el caso práctico, no hay problema por verlo en marcha, confiamos en ustedes. Creo que de hecho Bruno había mostrado algo ese día que yo estuve en el foro, así que algo de eso tenía visto, no recuerdo tanto ahora, pero nada, cuéntenos un poquito cómo sería ese modelo para ya directamente poder. Porque nosotros estamos armando justamente un plan de inversión para el cliente final,

**Juan Peralta**: te

**Diego Gismondi**: va a doler tanto, digamos,

**Juan Peralta**: Es lo que está en la página.

**Lucio Rojas**: Eso es un poco lo que lo que comenté rápidamente. La desventaja que tiene el pricing es que tenés que entender la herramienta para entender, así que explico un poco la herramienta, el bloqueante en todas las etapas principalmente, salvo que carguen una cantidad voluminosa de datos, son las gold tables. Las gold tables lo que van a hacer son no RTL que ustedes armen a partir de las tablas que tenga el sistema Negra tiene X tablas y ustedes quieren hacer una nueva vista que les sirva para armar BI Dashboard. Ese nuevo TL es una tabla gold que se va a crear. La infraestructura de Telamont se va a tener que actualizar dentro de los días.

**Diego Gismondi**: Acá data source es eso, ¿No?

**Lucio Rojas**: Esto es las tablas nuevas que vos crees a partir del data source. El data source se mide por storage.

**sandra boidi**: Claro, por los giga que tenés, ¿No es cierto?

**Juan Peralta**: Exactamente, exactamente, claro.

**Lucio Rojas**: Esto es lo que vos construís en sí conectás tres data source, un sistema, unos Excel y un sistema interno, con esos tres data source generas una nueva tabla, un etel nuevo Gold desde donde vos vas a consumir, que lo generaste a partir del analista de negocio, que se hizo una tabla donde usaba información de compras con clientes, con sucursales y con frecuencia, para hacer una tabla de análisis de ventas. Esa es una tabla Go. ¿En un plan Starter podés tener hasta 5, se cobra mensualmente?

**Diego Gismondi**: ¿Ese valor ya tiene incluido el uso de la API, de los créditos de consumo de token de Cloud, que es lo que ustedes usan, o eso aparte lo tiene que contratar el cliente final?

**Lucio Rojas**: Nosotros respondemos acá por Telamo, nosotros exponemos todo en MCP y el usuario trae su propio modelo.

**Diego Gismondi**: ¿Cómo ecualizas del crédito, o sea, básicamente si te consumiste todos los tokens de tu cuenta de chat GPT o la de Cloud Teramot, no podría funcionar? ¿Sería así?

**Lucio Rojas**: No necesariamente, ahí lo que se reduce es la exploración y creación de nuevas tablas, pero lo que vos ya tenés creado y lo tenés consumiendo se mantiene. Igualmente Telmo sirve mucho para optimizar la consulta de la base de datos, a partir de una buena gestión de la herramienta, donde vos creas Go y para tomar información, no tiene que hacer una query Cloud, sino que va a buscarlo bien a donde lo dejaste vos preparado.

**Diego Gismondi**: ¿Y la escala de esto, Lucio, cómo es? ¿Suponete, yo arranco con la de 50 y me doy cuenta que rápidamente se agota ese excedente, automáticamente dispara algo que me dice, che, tenés que pasar la de 200 o cómo funciona eso?

**Lucio Rojas**: Tenés algo intermedio, no te va a dejar crear más tablas hasta 5, crear la sexta, tenés que ir al plan

**Diego Gismondi**: Professional, pero no hay ninguna otra limitación, o sea, la limitación más grosera es esa, digamos, las Gold.

**Juan Peralta**: Y si llegaste al límite de las Gold, pero terminas haciendo algo consultivo, consultás, consultá y consultá, o sea, ahí no hay problema.

**sandra boidi**: Y si tengo más storage, ¿Qué pasa? ¿Me van bien Storage?

**Lucio Rojas**: Son límites, límites individuales.

**Diego Gismondi**: Che, este plan tiene que hacer un upgrade, ya.

**Lucio Rojas**: Muy pocas veces nos pasó que el límite llegue por Storage antes que por Go.

**Diego Gismondi**: Eso está claro, porque aparte están íntimamente relacionadas, digamos. Es probable que con 5 gold table no alcances ese storage nunca.

**Juan Peralta**: Y lo Sandra, lo que quería decir, si la relación esa que vos decías, che, yo necesito crear dos tablas más, por dos tablas no sé que, no voy a usar las 20, me voy a quedar en 7, bueno, podemos hacer algo manual e ir a una situación intermedia.

**sandra boidi**: Claro, porque digo, de 50 a 200

**Juan Peralta**: es mucho, no es ninguna restricción.

**sandra boidi**: Ocho tablas que no podés laburarlo y no va a pagar 200 por eso.

**Lucio Rojas**: Te hablaba de algo intermedio.

**Juan Peralta**: Claro, sí, sí, lo podemos hacer. Es administrativamente manejable. Después si tenemos un millón de usuarios, se va a complicar. Ojalá que llegue.

**sandra boidi**: Van a tener que agregar.

**Diego Gismondi**: Además ese valor es único, no es por usuario. Son 50 dólares por mes.

**Lucio Rojas**: Exacto, sí, sí.

**Diego Gismondi**: Bueno, está clarísimo. No sé cómo es el esquema de partners que tienen, pero entiendo que debe ser una licencia sobre esos 50, digamos. Una comisión, perdón, sobre los 50 una licencia.

**Juan Peralta**: Sí, sí, sí, es eso. A ver, vos por tu cuenta vas trayendo clientes, bueno, y va acumulando en lo que va ganando. Sobre eso después te paso un documento para que lo tengas presente. Digo, porque la idea para nosotros lo mejor es que vos tengas clientes que los puedas subir a la herramienta y de última para vos te queda el asesoramiento en cómo generar el modelo de datos. Esa suerte de data warehouse optimizado, lo vas construyendo en tiempo real prácticamente de una manera muy simple. Conteando la Go sería el set de datos al cual vos le vas a pegar la consulta. Algo que decías, si vos venís y el cliente decís, che, mi cliente sí o sí, la reportería la hacen Power BI porque ya tiene todo el portal y usan la app en el celu y Power BI por todos lados, pagan la licencia, no van a cambiar, no quieren hacer otra cosa. Bueno, de tu lado vos le podés desarrollar el tablero ya con nosotros haces toda la lógica, te generas la Gol que contenga todos los datos que va a necesitar ese tablero y a esa Gol le conectas el Power BI del cliente. Eso se hace con un ODBC, un conector ODBC.

**Diego Gismondi**: Está bien. El Data source de Power BI sería Teramot.

**Juan Peralta**: Exactamente. Pero ¿Qué es la ventaja? Vos le decía Claude, Claude, una vez que llegaste a lo que todo el año necesito, ahora dame el paso a paso para hacerlo en Power BI. Y Claud te va a poner 1. Abrir Power BI 2. Crear proyecto 3. ¿Lo ven? Y bueno, la reportería es algo interesante y te podés encontrar con cualquier negocio. ¿Que vemos nosotros? Soluciones de reporting o de Business Intelligence, son de nicho, son para esta industria, son para el software, para constructoras. Listo, genial. ¿Existe? Sí, obvio que existe. Tiene reportería, tiene reportería, ocho reportes y para de contar. Ahora esto queré cruzar el software de la constructora con los costos de los empleados que están en otro lado

**Diego Gismondi**: y

**Juan Peralta**: no, no se puede. Listo,

**Diego Gismondi**: está clarísimo, es bien simple el modelo y

**Juan Peralta**: hasta de usarlo cuando vamos a la demo, eso, subite un Excel con datos, algo.

**Lucio Rojas**: Eso, bueno, ahí va a ir por ahí si ya nos. Yo también me corro un poco el tiempo, no quiero cerrar los prodijos.

**Diego Gismondi**: No, no, ya estamos chicos, para la

**sandra boidi**: semana próxima si les parece.

**Diego Gismondi**: Esto era exploración y además nosotros tenemos que concretar con el cliente, avanzar con otras cosas y ni bien lo tengamos, la idea era ya tener enchufado esto

**Juan Peralta**: de alguna forma, digo, esto es marginal en temas de costo, o sea no te va a mover la aguja, así vos le digas, toma, te regalo la licencia de cloud, o sea así te va a encargo de eso con 150 dólares, en el peor de los casos le da una licencia de cloud de 100 y el téramo de 50 y el te va a amar.

**sandra boidi**: Otra cosa, les pregunto, todo lo que es privacidad, data protection, todo eso, ¿Ustedes cómo firman acuerdos? Ahí firman.

**Juan Peralta**: Tenemos un NDA nuestro, si vos tenés uno tuyo, no manda, o sea vos revisarías el nuestro, nosotros revisamos el tuyo y asimismo cuando entras a Theramot y generas el usuario como para tenerlo para que se hagan una prueba, ahí te aparecen los términos y condiciones y está cómo tratamos los datos, la privacidad y va todo. Si creo un diagrama arquitectura yo te lo podemos compartir. ¿Una vez que firmamos un NDA, le pasamos cómo trabajamos con eso? ¿Repito, certificado, ENSOC y la solución está montada en AWS, toda la información queda en buckets? Sí, está todo cifrado, en reposo, en tránsito, en producción, o sea, Nada, no sé. ¿El JP Morgan está en AWS?

**Diego Gismondi**: Sí, nosotros también trabajamos con AWS, tenemos un producto específico para salud y tenemos todo ahí con alta disponibilidad, digamos, pero obviamente es como confiar en Google con tu cuenta de correo, es lo mismo a esta altura.

**Juan Peralta**: Entiendo. Pero bueno, está

**Diego Gismondi**: bueno chicos, vamos a estar en contacto.

**Lucio Rojas**: Me interesa mucho si puedo hacer un usuario y sumarlos para que prueben. No sé si ya tiene acceso a esa mysql, si quieren hacer un dump de algunas tablas y cargarlo en la herramienta.

**Diego Gismondi**: Vamos a preparar una para la semana que viene y después

**Lucio Rojas**: unos SV y yo mientras tanto le creo los usuarios y entran y van probando un poco cómo es.

**sandra boidi**: ¿Te hago una última pregunta Lucio, cuántos tenés?

**Juan Peralta**: ¿Es el que mejor usa la herramienta?

**sandra boidi**: Increíble, increíble, felicitaciones.

**Diego Gismondi**: Nosotros a los 22 estábamos tratando de ver qué pasaba con la universidad, recién

**Juan Peralta**: en la jornada yo me delato en

**sandra boidi**: la edad,

**Juan Peralta**: imaginate, había docentes que nos hablaban de tarjetas perforadas.

**sandra boidi**: Imagínate mi primer trabajo, Municipalidad de Rosario,

**Juan Peralta**: tarjeta perforada de la portería, equipos,

**sandra boidi**: un BRX tremendo.

**Diego Gismondi**: ¿Lucio está mirando como diciendo que son tarjetas perforadas?

**sandra boidi**: ¿La historia la viste? La historia de la computación la habrás leído alguna vez.

**Juan Peralta**: Le hablo de un disquete y me dice ah, vi una foto, el seminario

**Diego Gismondi**: lo hice con disquet.

**Lucio Rojas**: Cuando me preguntan, yo no soy de sistemas negocios, justo entramos acá a todo lo que es una empresa tecnológica y ahí mamé. Por eso decimos no hace falta hacer de datos para usar estas herramientas.

**sandra boidi**: No, tal cual, tal cual, Es la mejor, la mejor, el mejor ejemplo. Está muy bien lo que nos contaste.

**Diego Gismondi**: Bueno chicos, estamos en contacto.

**Juan Peralta**: Yes.
