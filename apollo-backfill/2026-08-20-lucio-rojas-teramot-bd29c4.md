# Lucio Rojas - Teramot

**Fecha:** 2026-08-20T13:15:50.816+00:00  
**Duración:** ~67 min  
**Participantes:** Gabriel Puertas <gabriel@teramot.com>, Ignacio Chiera <ignacio@jupidigital.com>, Lucio Rojas <lucio@teramot.com>  
**Externos:** ignacio@jupidigital.com  
**Apollo ID:** 6a870dab11f8580010bd29c4

---

**Lucio Rojas**: Buen Lucio, ¿Cómo andás? ¿Todo bien? Estás muteado.

**Ignacio Chiera**: ¿Qué tal? Buen día. Lucio, Gabriel, ¿Cómo están?

**Gabriel Puertas**: ¿Cómo andan? ¿Todo bien, todo bien? Vos sabés que me acabo de quedar sin Internet, Entré con el celu. Denme un segundo.

**Lucio Rojas**: Mientras Nacho estuve haciendo la intro. Nosotros somos de Telamot, somos una empresa, una startup que tenemos una plataforma para conectar bases de datos con AI, es BB y buscamos automatizar todo el proceso de ingeniería de datos y de creación de datos de Azure, de reportería, de consulta de información. Estuvimos hablando hace un tiempo con Cristian, que entiendo que es el CEO de PUPI o algo así, y nos ofreció dar un webinar para explicar cómo Teramot puede automatizar o resolver con AI los procesos que antes ingeniero de datos y equipos de vida tenían que hacer acá. Para eso un poco la idea era partir de la misma base que ustedes usaron las clases, que entiendo que es la base de Contoso de Microsoft, y poder escuchar de vos qué les enseñaron cuáles fueron los pasos y les hacían primero sanexar la base, armar un TL, después armar los dashboards y demás. Como para nosotros mañana en el webinar poder hacer algo parecido y que el contraste sea claro entre lo que decían ustedes y lo que nosotros hacemos con la herramienta. Así que Gabo es el que va a dar el webinar, nuestro COO brillante y flamante.

**Gabriel Puertas**: Vamos a la UIFE que tenemos poco tiempo. Vos no conocés la herramienta, No,

**Ignacio Chiera**: Un vídeo que habían hecho, no me acuerdo quién lo había realizado ustedes. No la he usado, pero vi una presentación de ustedes.

**Gabriel Puertas**: Bueno, esperá, porque ayer yo hice unas pruebas ayer que. Porque digamos, yo le decía a Lucio en el webinar, a mí me parece que escopado mostrar la herramienta para hacer el paso a paso que ustedes hacen cuando enseñan cómo hacer un proceso de esto de analítica, digamos. La prueba que hicimos ayer fue diferente, nosotros conectamos la base de datos, agarramos los WhatsApp que nos mandaron de lo que querían llegar, se los tiramos a Cloud e hizo todo. Yo no quiero mostrarlo así porque pierde a la gente, ¿Entendés? Es como, esperá, te voy a compartir pantalla así vos me entendés. No, esperá, pantalla, pantalla. ¿Cuál es la pantalla que pierda la gente?

**Ignacio Chiera**: Te refería a que le cuestan.

**Gabriel Puertas**: Es como raro, digamos, y me da la impresión que no es la idea. Yo acá lo que hice fue. Esperá, vamos a hacerlo más prolijo. A ver, te voy a poner esta. Seguir viendo esto, me vengo a. Acá Contoso. ¿Por qué se llama Contoso? ¿Lucio? ¿Qué es Contoso?

**Lucio Rojas**: No quería preguntarle a Minecraft, usa el

**Gabriel Puertas**: nombre así, es una base de datos genérica. Ese dato se llama contoso, boludo, no entendía, no entendía. Bueno, acá Lucio la subió. Si vos te metes en esta base de datos, tiene todas estas tablas. Lucio la subió como un CSV, pero la podemos subir. Si estuviese puesta te podés conectar, qué sé yo. Un poco acá la idea que conecta la fuente de datos. ¿Qué pasa? Una vez que vos te conectás la fuente de datos, yo voy un poco rápido por el tema del tiempo, lo que hace Teramot es ingerir cada una de esas tablas que están acá y lo que te va a armar es un lake house, que es básicamente yo tomo una fuente de datos en datos crudos, internamente entra en una capa bronce, exactamente la forma en que te los compartieron, y después pasan a una capa silver donde hay un proceso de sanitización. Ese proceso de sanitización lo hacen alguna gente, no siempre se hace, o sea, por ejemplo es muy probable que esta tabla esté bastante bien y no haya hecho mucho. Fíjate que esta sería la query que te lleva de bronce a silver y se trajo toda la tabla, básicamente. No hay mucho cambio, no estoy viendo ninguna que tenga adaptaciones, pero bueno, si tuviese que hacer, los haría. Cuando yo ingestó los datos, o sea, yo cargué datos automáticamente después de un tiempo, depende de la cantidad de tablas, cantidad de columnas, puede ser media hora, 20 minutos, que se yo, no sé, a mí me quedan todas las tablas en la capa silver. Lo que hace la gente es, digamos, lo que. Lo que sigue es generar las capas González, que son ya como respuestas de negocio. Cada una de estas capa gold apunta a un cierto warehouse. Entonces yo mañana empiezo el webinar este explicando justamente eso, presentando la herramienta, diciendo qué pasa acá. Yo hago, conecto la base de datos está con toso, hay un proceso de ingesta de información. En esa ingesta de información yo no solamente sanitizo, sino que entiendo de qué va la información, es como que armo metadata, entiendo los datos. Pensalo esto como si las personas, cuando vos le enseñás a las personas qué le decís Bueno, acá tiene una base de datos, no sé. Ahí te pregunto. Lo primero que hacen es un análisis exploratorio, me imagino.

**Ignacio Chiera**: Exacto, lo que vos me comentaste está bien. Haces una conexión para traer una base de datos, lo almacenas como capa bronce crudos y a partir de ahí empezás a hacer transformaciones. Eso se va a la silver. Lo que sí, por ejemplo, nosotros no hacemos en la capa Gol, hacemos como la que dejamos las tablas ya definidas y las vamos ya listas con alguna otra cosita que falte. Por ejemplo los. Ahí me parece que donde descoordinamos ayer Lucio, a tus consultas. Nosotros lo que es el análisis no lo hacemos desde las tablas, hacemos después.

**Gabriel Puertas**: No, no, pero me parece que estamos hablando. Es más o menos lo mismo para

**Ignacio Chiera**: comentarte y a ver después también lo que ustedes quieran hacer está buenísimo.

**Gabriel Puertas**: Es una cuestión de término y está muy bien. Es como para nosotros, lo que para ustedes son tablas Gol, para nosotros son silver. Entonces vos lo que me decías es, bueno, nada, si yo quiero, una vez que ya saniticé todo eso, me quedo en una Gol y yo quiero armar una siguiente tabla, que son joins de distintas tablas, algunos filtros, algunas cuentas. ¿A esas tablas cómo le llaman?

**Ignacio Chiera**: Eso es lo de Silver Vista. Yo eso lo llamo transformación.

**Gabriel Puertas**: Ahí va, una transformación. Perfecto.

**Ignacio Chiera**: ¿Que es lo de silver? Cómo sigo parado en silver.

**Gabriel Puertas**: No, pero esperá, mira, yo acá hice una cuenta, mira esta tabla. Yo acá hice una cuenta de. De RFM, Esto ya es una query y empiezo a calcular el valor de f, de R, de m, qué sé. Yo en particular elegí una que utiliza una única tabla, pero esta query le apunta, hace un cálculo, digamos, es. ¿A ustedes le siguen diciendo silver?

**Ignacio Chiera**: No, está bien, por eso te digo, eso por ahí uno lo hace, pero justamente lo hacemos de la herramienta visualización.

**Gabriel Puertas**: Ahí va bien, lo hacemos de la

**Ignacio Chiera**: parte visualización en la plataforma de Fabric, en Power BI.

**Gabriel Puertas**: Bien, perfecto, perfecto. ¿Y en qué codean? Ahí por ejemplo, por las vistas que nosotros nos pasamos eran de clic. ¿En qué codean? En SQL también.

**Ignacio Chiera**: Y el lenguaje, si no me equivoco, no es explícitamente SQL, creo que es como un lenguaje de clic, pero obviamente tiene todo el formato de SQL, tiene los select, los from, los war, pero tiene algunas funciones estándar que me parece que las tiene, clic.

**Gabriel Puertas**: Bueno, ¿Cómo funciona Theramont? Ahora que nos pusimos de acuerdo con la terminología, yo conecto los datos, ahí pasan dos cosas, yo ingestó la información, la traigo a la nube de Theramot, la subís ahí y la segunda parte es, hago una suerte de sanitización si hace falta, o sea, si detecto que hay formato de fecha, lo paso a formato de fecha, ese tipo de cosas,

**Ignacio Chiera**: una mayúscula en un campo, pero lo

**Gabriel Puertas**: más importante es que yo en esa ingesta genero metadata, o sea entiendo de qué va la información, es como que te hace una especie de análisis exploratorio, dice ah mira, estas son venta, esta es la tabla de lo que sea. Una vez que yo tengo eso, es como que vos te paraste ya conectado a la herramienta de visualización, o sea vos ya tenés todo puesto en esa herramienta de visualización y como que tenés que empezar a crear esas vistas, esos procesos. La idea cómo es mostrarlo mañana nosotros tenemos la posibilidad de conectar Teramot a un LLM a tu cuenta de chatgpt, en este caso vamos a Cloud con un protocolo que se llama MCP, MCP no sé si lo conoces, es básicamente un protocolo que le permite al LLM utilizar una herramienta, en este caso es Theramot, pero vos te lo podés conectar a Gmail, al Calendar, a Slack, no sé, ahora están apareciendo muchas tools que implementan el, perdón, MCP, eso es básicamente para que un agente use esa herramienta. Nosotros ya lo tenemos conectado, entonces fíjate, yo acá le digo, esto ya es cloud, ya estoy en cloud, acá le digo listame los workpace, yo porque tengo varios, me aparece Contoso, le digo che vamos a usar Contoso, veamos que tiene, y me dice mirá Word tiene un proyecto, tiene 24 tablas, hay 18 dimensiones, Dim Customer Store, producto, Product Category, toda esa historia y seis de hechos, es un modelo estrella completo de retail, venta, de inventario, cupo. Fíjate que es como que ya tiene conciencia de que tiene esa toda información que le pasó TR ahí ya la

**Ignacio Chiera**: ingresó a la capa bronce o solamente

**Gabriel Puertas**: la ley ahí yo antes había conectado enteramo todos los datos, esto que te. Esto que mostrarlo, Sí, obvio, surgir de

**Lucio Rojas**: un,

**Gabriel Puertas**: o sea ahora lo voy a limpiar todo, voy a borrar todo, no se, lo hago en vivo, porque, porque el proceso este de ingesta por ahí no, no sé, en esta tabla se debe haber tomado su media hora, ¿Entendés? Claro, no tiene sentido estar haciendo como el webinar, un poco la idea es ya llevarlo hecho. Pero bueno, es explicar muy bien esta parte, digamos, decir bueno, la herramienta termina siendo lo mismo. Yo además lo que le pedí es que esto me imaginé un poco, yo necesitaba entender un poco más, le dije a Claude, le digo, che, hagamos un EDA de las tablas general, y recién ahí vemos qué pasa. Un EDA es un poco más profundo, ¿Entendés? Como decirte, fíjate que cuando le digo eso a Claude, Claude empieza a utilizar esa herramienta y nada, toda esa lectura que hace las tablas, ahí va exploratoria, se fijó, fíjate todas las query que hizo esto sí lo vamos en vivo, vamos en vivo y ahí me sale con un bien, el esquema clásico, me dice, mira, la tabla de ventas tiene 34 millones, va del 2007 a 2009, las métricas clave son en dólares, todo esto, B, qué sé yo, las unidades, qué sé yo. Y acá me gusta algo, fíjate, me dice, ojo, las ventas, sales, amount menos total coinciden, te da 43%, que es como una especie de margen, pero contra unit coast, o sea el costo unitario de los productos, el margen es 57%. Hay dos definiciones de costo conviviendo. Algo a resolver, si armamos una gol de rentabilidad acá, yo voy a tener que aclarar muy bien a lo que nosotros le llamamos gold, son como las vistas que vos armas en tu herramienta,

**Ignacio Chiera**: Eso es muy distinto, o sea, eso es lo más distinto a lo que hicimos Jupi. Así que sí, eso acrárenlo, explíquenlo. Y ahí te digo, nosotros eso lo trabajamos, esto de la rentabilidad, justamente, claramente uno es el margen neto y el otro margen bruto. Bueno, bien, no sé si hay mucho por aclarar ahí más que eso.

**Gabriel Puertas**: Si le decís eso, el flaco lo

**Ignacio Chiera**: entiende y queda, porque nosotros esas métricas la hicimos, hicimos unos KPI sobre eso, margen neto y margen bruto.

**Gabriel Puertas**: Bueno, dale. Entonces, hallazgo de negocio, encontró todo esto y bueno, y acá es donde ya empezamos a diverger. Lucio tenía como 8 millones de WhatsApp y vistas y yo agarré y le dije, che mirá, fíjate, el tema es así, fíjate lo visceral que es cuando vos hablas, sí, todo lenguaje natural, claro, vamos a hacer un webinar con estos datos, va a ir gente que utiliza esta base de datos para aprender a hacer Business Intelligence, utilizando esta base de datos para armar tablero y eso, sobre lo que tienen que hacer. Tengo una serie de mensajes de WhatsApp sobre los dashboards que llegan. Te voy pasando, le pasé una banda, o sea, pues yo posta esto no lo leí.

**Ignacio Chiera**: Sí, sí, te entiendo, es lo que te pasé yo, Lucio.

**Gabriel Puertas**: Claro. Y están todas las imágenes.

**Ignacio Chiera**: Entendí que le iba a servir justamente a la IA para hacerlo, por eso es que te pasé eso. Pensé que era lo que iban a necesitar.

**Gabriel Puertas**: Claro. Entonces se pone a pensar, me dice, mira, tengo los dash, son las 5 hojas, tengo hoja de producto, hoja de cliente, me dice matriz RFM, pero me dice, ojo porque el RFM no está como una dimensión del cliente, eso recuerdo que en un momento me lo dijo. Entonces me dice, con qué datos vamos a trabajar en el webinar 2007 a 2009, lo que ya está cargado en Teramot. ¿Después, cuál es el foco principal del webinar? Yo le dije acá replicar el dashboard visualmente lo más fiel posible. Y le dije, arrancá a hacer las las tablas Gol y ahí, disculpame ahí

**Ignacio Chiera**: si querés, recordá que las Gold tables son las vistas de ustedes. Sí, sí, porque el ambiente va a ser jupi y para mí va a ser lo que menos van a cachar los chicos, los alumnos.

**Gabriel Puertas**: Ahí va, dale, dale. Igual vos va a estar en el webinar.

**Ignacio Chiera**: Sí, sí, yo voy a estar mañana.

**Gabriel Puertas**: Equivocado ahí aclarando, digamos. Bueno, me armó todas estas vistas, tuki, tuki, tuki. En la tercera me dice cliente RFM, me dice, ojo que esto no está, le dije bueno, calcula el RFM, calculalo. Le digo, al RFM hay que calcularlo, qué sé yo. Bueno, empezó Frequency, aparentemente como no tiene indexada la venta al cliente, o al menos este no lo detectó, como no tiene cómo calcular una frecuencia.

**Ignacio Chiera**: Claro.

**Gabriel Puertas**: Entender, no sé que vos tenías en los dashboards, quizás otro set de datos.

**Ignacio Chiera**: Sí, quiero ver donde lo usé yo el RFM, no sé si lo usamos

**Gabriel Puertas**: las vistas, por ahí este lo detectó en algún lugar, en un trimap, pero nada, no pasa nada porque no es ni idea, Entendés, o sea, fíjate, lo que me parece es mostrar cómo va

**Ignacio Chiera**: el palo la ya y hacer con un par de mensajes.

**Gabriel Puertas**: Claro. ¿Entendés? Es un poco esa la idea. Y a mí lo que me interesa transmitir es que como, fíjate, acá terminó armando. ¿Dónde está el artefacto? ¿Acá? Acá Claude terminó armando las vistas y esos son los mensajes que hicimos. Posiblemente los datos no coincidan exactamente con los tuyos, pero nada, fíjate que a

**Lucio Rojas**: los

**Ignacio Chiera**: curiosidad te hace cambio de moneda,

**Gabriel Puertas**: por ejemplo, mira acá está Tuki,

**Ignacio Chiera**: ese botón está bueno tenerlo algo como para

**Gabriel Puertas**: mostrar está bueno, y yo en un momento, no sé, el mapa, mandale el mapa, qué sé yo y todas esas cosas. Yo creo que el mensaje para mañana, esto es opinión nuestra, las herramientas de visualización ya están todas muertas, no tiene ningún sentido que sigan porque vos tenés todo modelo que te hacen las visualizaciones al toque, pero mucho más profundo que la visualización, esto es lo lindo digamos. Pero si vos te fijas, cada una de estas tablas o vistas como le dicen ustedes, para nosotros son gold estas, si yo me vengo a la herramienta, me generó las query de SQL, fíjate que esta le mete a cuatro tablas, este te muestra el Lineage y estas son las queries, tipo me generó todo. Lo que termina haciendo Theramot es como orquestando esa información, o sea vos tenés armado un ETL, si vos conectaste tu base de datos, esto lo haces y te queda ya listo. Ahora vos me decís, che, pero bueno a mí me gusta compartir los datos con Power BI, no pasa nada, nosotros tenemos la posibilidad de conectar, bueno, con todos estos datos, o sea los datos que vos generas, estas vistas Gol. Claro, las tablas gol para nosotros quedan almacenadas en un servicio de AWS que es del dueño del Workspace, en este caso tuyo ponele que se llama TINA, que tiene conector con Power BI, o sea, si vos te llevas todas estas credenciales y habilita un conector en Power BI, metele a credenciales y vas a ver esas tablas que generaste y te querés hacer los gráficos ahí hacételo porque ya lo tenés como fuente de datos, ¿Entendés? No tenés que seguir haciendo transformaciones en la herramienta, un poco la idea, pero para mí el mensaje es ir un poco más allá, porque tipo la visualización es como que OK, yo te hago el dashboard, está todo muy bien, pero puedes hacer automatizaciones, puedes conectarlo a otros servicios que generen alerta, que manden correo, que sea. Me gustaría terminar por ahí. Yo la idea del webinar es hacer el paso a paso con

**Ignacio Chiera**: Claudia, con

**Gabriel Puertas**: los chicos, con Claude. ¿Ahora te pregunto, los chicos, Claude, no sé, yo le digo chicos, pero quiénes son?

**Ignacio Chiera**: Somos una variedad de personas. Bien, Hay pibes de 19 años, serán los menos, y hay gente de 55.60 años, hay abogados, hay gente técnica como yo, hay médicos. Tener un rubro para donde vos quieras ir. ¿Todo en el mismo idioma, si son hispanohablantes, no?

**Lucio Rojas**: El mismo idioma de datos y eso. Podemos ir a lo técnico.

**Ignacio Chiera**: Sí, sí todos hicieron el curso. Sí, sí. A ver, hay gente que lo va a tener más visto, menos visto, o sea, eso ya no va por ustedes. Aparte también la idea de webinar es que queda grabado.

**Gabriel Puertas**: Bien, buenísimo.

**Ignacio Chiera**: Repasar entonces también, si uno se tiene que bandear un poquito lo que uno quiere mostrar en eso que queda grabado, no hay problema. Después si alguien lo tiene que repasar y detenerse e ir informándose, brillante.

**Gabriel Puertas**: Escuchá, y la idea es que nosotros le podríamos, o sea, le podríamos dejar un workpace a las personas que quieran probar, pero nada, tienen que tener, o sea, se tienen que loguear en Teramot. Nosotros le podemos hacer esta u otra fuente de datos que ellos quieran. Obviamente esas cuentas free tienen algunas limitantes de usuario y cosas así, pero nada, lo pueden usar, lo pueden probar y ayudarlos un poco. Ahí te hago una pregunta, ¿Tenés sensibilidad? Si ellos son personas que están acostumbrados a utilizar cloud o chatgpt o cosas por el estilo.

**Ignacio Chiera**: Y hasta ahí, primero, certeza no tengo. Está bien también, pero yo creo que, a ver, para mí el uso de la IA la usan. Creo que tu pregunta va que no sé si el caso, no sé qué tanto lo tendrá. La versión paga. ¿Vos necesitas tener la versión paga para conectar esto, para usar esto?

**Gabriel Puertas**: El MCP me parece que sí ilusionó.

**Lucio Rojas**: No, no, hasta un MCP te deja.

**Ignacio Chiera**: Y el tema de los.

**Lucio Rojas**: Vas a probar algunos, Yo he tenido alguno que probó bastante. No consume distinto a lo que es hablarle normal.

**Ignacio Chiera**: ¿A qué le llamas vos que hizo bastantes distintos proyectos o distintas consultas sobre el mismo? ¿Lo han probado?

**Lucio Rojas**: ¿Vos me estás preguntando sobre? ¿Sobre Cloud o sobre Telamo? ¿La versión free de qué?

**Ignacio Chiera**: La versión free de la IA que ellos conectan.

**Lucio Rojas**: Cloud. No, no va a llegar a ser. Todo esto se va a cortar antes.

**Gabriel Puertas**: Sí, sí, claro. Porque claro, yo lo tengo con el de 20 dólares. El de 20 dólares seguro, porque eso vos es como que te comes cuota, o sea, si empezás termina y no sé, se te habilita, mañana le volvé a meter y qué sé yo. El de 20 dólares seguro que lo terminan. Seguro que lo terminan Fíjate que el de 20 dólares lo que tiene es cuotas diarias, semanales y mensuales, entendés, o sea. Pero lo que pasa con esto es que vos por ejemplo le empezás a meter a Cloud, ponele.

**Ignacio Chiera**: Sí, también depende cuántas visualizaciones, cuántas vistas quiera hacer pero lo que pasa que

**Gabriel Puertas**: digamos, es muy poco lo que consume, poco en el sentido de que como tiene mucha herramienta y el laburo pesado pasa en Theramo si querés, o sea, lo único que hace Claude llama a la herramienta y genera un poco de código y después todo lo que te enseña y yo mañana. Claro, nosotros vamos a empezar a laburar con un agente que va a estar en. En theramo que lo tenemos un poco en desarrollo, tiene modelos un poco menos potentes pero más baratos, pero nada de ahí lo van a poder usar también pero yo invitaría a todo el mundo a que se meta o que nos escriba a mí y a Lucio, el que va a laburar va a ser Lucio y le genera como los workpace y cosas para que prueben. Yo preferiría que no metan los datos de Contoso porque como para jugar, sino que algo que a ellos les sirva, pero bueno, que metan lo que quieran

**Ignacio Chiera**: contarlo porque les va a interesar. Hay un poco, no sé con quién hablaba Cristian esto de si puede armar un QR o algo y no sé, díganle si el que se conecta al QR le hacemos workpay nosotros como ofrecerle algo para que les meta curiosidad y se metan ellos. Para mí la gente se va a meter porque hoy la IA es pan caliente en ventas, digamos, a la gente le llama la atención lo que es IA, la gente quiere aprender IA, Bueno,

**Gabriel Puertas**: bueno, hacemos así entonces. Yo voy a seguir un poco más de espacio de lo que te mostré a vos, es decir, la parte en donde terminamos jugando en theramot, en la página de theramo es simplemente mostrar que conecte los datos, resto de las cosas ya es con Claudia.

**Ignacio Chiera**: Perfecto, Yo lo que tengo para mencionarte ya te lo dije yo te lo vuelvo a decir, la diferencia de lo que es una tabla gold para ustedes, porque no es que algo nuevo, sino que lo tienen como otra cosa. Entonces eso va a haber que aclararlo. Y después me surge a mí la duda, yo por ahí soy medio por ahí más técnico en esto del análisis de datos. ¿Qué certeza tenés vos de lo que es esa? ¿Esa limpieza de datos? Por si vos quieres mostrar algo mañana. Perdón, Eso, y por ahí mostrar qué tabla se conectó con cuál a la hora de transformar.

**Gabriel Puertas**: Ahí va, mira, estoy tratando de buscar alguna que haya hecho alguna transformación. Fíjate, certeza no tenés nunca, digamos, certeza con los impuestos y la muerte. Pero digo, lo que nosotros exponemos de lo que hizo la gente son dos cosas que para mí es como te permiten tener certeza eventualmente o que lo necesites corregir. Una es la query que te que pasó de bronce a silver. Fíjate que acá yo hice una transformación de fecha, por lo que veo, hice que haga una T y además pasé a fecha y después casteé como fecha otra columna que se llama date key, no sé, esa fue la transformación. Si vos te venís acá, yo además te muestro la tabla y vos acá podrías correr una query, por ejemplo esta daykey, y ver si realmente la formatea bien. Todo eso se permite. ¿Y además, espera, agarremos esta tabla, esta cómo se llama? Conduce Demo fact. Eso no debería. Fac Strategy Plan. Yo acá le voy a decir, mira, tengo. Tengo dudas de cómo pasé de bronce. Bronce,

**Ignacio Chiera**: Por ejemplo acá, esto para mí esto, mostralo, hacer un ejemplo sobre esto y le podés decir, no sé qué te va a contestar, pero pedirle que te diga qué cambios hizo.

**Gabriel Puertas**: Ah, sí lo va a hacer.

**Ignacio Chiera**: Capaz que ya te lo contesta con

**Gabriel Puertas**: ese prompt, pero que no me diga que tenemos. ¿Cómo es esto? Avísale a Agu que estoy en una llamada. Lucio, me llamó Agus y le corté. ¿Cómo es esto? Lo que yo creo es que digamos, fíjate, tengo la bronce, perfecto, ya tengo el panorama. Hice unos timestamp, se pasó a string, se descartó hora que era constante y se mantuvieron. Ahí está, mira los cambios fue en data key, hice que haga el 0,0000 que era todo igual en la. Se pareció a string, a timestamp real. Esto, Dayatina Montatina es algo nuestro, o sea, está mal que se lo explique, pero otra cosa, después te explico, pero no importa, y el resto se mantuvo igual. Y bueno, y así, digamos, nada de esto tener certeza, la lógica nuestra de Theramo es que vos tengas gobierno, sobre todo entender estas dudas que vos tenés, ¿Habrá hecho bien las cosas? Bueno, puedes verlo, puedes cambiarlo, interferir, y nosotros como que mostramos todo el proceso y todos los códigos, o sea, si eventualmente vos decís, bueno, voy a hacer una cosa, sabes que a mí me gusta seguir laburando con Power BI y estas vistas que yo me hago, me gustó cómo le hizo theramon, pero no la quiero dejar en theramo, me llevo la query, acá tengo una query, me llevo esta query y la hago en Power BI, listo, llévatela y hacela.

**Ignacio Chiera**: Y eso por ejemplo te lleva mucho tiempo hacerlo mañana en el webinar pasar uno a Power BI, yo no tengo

**Gabriel Puertas**: porque uso Mac, pero bueno, ya no sería viable, mirá, vamos a hacer una prueba, eso no lo debería fomentar mucho, pero bueno, quiero que agarres una que hicimos y tomes el SQL y lo pases al lenguaje de Power BI, así, Porque cuando vos tenés uno de estos modelos, ya es como que pasa a ser, estoy tratando de ubicarme.

**Lucio Rojas**: Intermediario.

**Gabriel Puertas**: Claro, ahí puede hacer lo que sea, este te hace lo que sea, fíjate, usa DAX, va a agarrar una no sé cuál venta mensual, ahí dijo, y ahí te lo está haciendo, entonces le ponemos la query y está, yo, mi opinión es que va a terminar gastando más guita. Ah, y perito, mostrarte algo más, Ahí me está generando un documento con las medidas de DAX y las notas de traducción, te lo llevaste. Lo que también podés hacer, o sea,

**Ignacio Chiera**: vos en Power BI tenés que tener cargada las tablas y le pone este

**Gabriel Puertas**: DAX y ahí funciona y debería funcionar y se tienen que llamar iguales y toda esa historia. Acá estamos haciendo un chino, lo que te quiero mostrar es cómo tenés dominio de todo eso. Otra cosa que vos podés hacer es pedirle a Cloud que te genere un dashboard, pero ya no que te lo muestre en Cloud, sino que te lo muestre en theramo, que lo almacene en theramo. La ventaja de eso, o sea, se va a ver parecido, va a ser, ahora lo hacemos. Me arrepentí de haber hecho esto porque está demorando mucho.

**Ignacio Chiera**: Paralo si querés, si querés.

**Gabriel Puertas**: Bueno, ahí está comprá listo.

**Ignacio Chiera**: ¿Cloud vos le llama al HTML que hizo el dashboard en Cloud?

**Gabriel Puertas**: El dashboard, claro, en realidad técnicamente este de acá es un artefacto, el que yo te mostré hace un rato, el problema de esto es que más difícil mantenerlo actualizado, con este anda bien, porque una base que es estática, pero si vos tuviese una base que se actualiza todos los días, es un poco más hincha bola desde Cloud mantenerlo actualizado. Ahora hagamos un dashboard con ventas mensuales y publicarlo entero. Está mirando que tiene esa vista y nada, cuando lo haga me va a decir ya está listo, me va a pedir permiso. La idea es esa digamos. Y este dashboard que vive en Téramot, cuando se actualiza el pipeline, porque lo que nosotros te armamos en definitiva es un host conectado con un ETL, entendés, o sea esta base son archivo, pero vos lo podrías conectar a una base de datos posta, mysql, pogre, no sé, lo que sea, y definir que yo voy, levanto los datos todos los días o con la frecuencia que vos quieras, eso va a hacer que me está preguntando permitir, siempre me está preguntando si lo puede publicar, eso va, eso lo que arma es un ETL, o sea todos los días va a ir, va a extraer las actualizaciones y va a publicar. Si vos tenés un dashboard, ese dashboard se va a actualizar todos los días y lo ves acá. ¿Vamos a verlo

**Ignacio Chiera**: si querés te menciono que esa pregunta que te hace también está buena de si lo publica, no

**Gabriel Puertas**: lo publica, por qué no pidió conectar este muñeco? Así está buena, pero vamos a ver por qué me pidió. Puede ser porque yo le meto, no aquí, bueno, esto lo tenemos, Ahí está diseñador azul está preguntando. Claro, lo que quiso hacer es verlo, guárdalo, Esto me pasa a mí solamente, no le pasaría a la gente. Lo que pasa, yo tengo varios conectores de MCP, tengo los que nosotros usamos de desarrollo y todos le pegan a Theramo, entonces por ahí Cloud se me confunde entre cuál usar, pero sufrimos nosotros.

**Lucio Rojas**: Los dejo que me tengo que ir a.

**Gabriel Puertas**: Yo termino, le quiero mostrar esto, si

**Ignacio Chiera**: necesitan conectarse más tarde me avisan con tiempo, no hay problema.

**Gabriel Puertas**: Lo que voy a hacer mañana es. Esperá que esto ya me quedó la sangre, pero digo buen día. Yo lo que voy a hacer mañana es simplemente esto, lo borro todo o sea voy a borrar todas estas goals, acá debería haber un coso que es

**Ignacio Chiera**: ventas mensuales, ahí te lo hizo este

**Gabriel Puertas**: que hizo recién y ahí me hizo un dashboard, si vos le pedís este, no se, le quedó menos lindo porque no lo vio, digo yo agarro y lo itero, le digo no, no me gusta esa tabla. Y lo que tiene interesante esto es que se actualiza, entonces vos es como usas Teramot y ya no necesita Power BI, no necesita pagar Tabló, necesita pagar nada, y las iteraciones, las, o sea, fíjate que esto lo hace cualquiera, digamos, técnicamente ni siquiera tiene que tener muchas skills de datos para que, a mí me parece que son súper importantes las skill de datos para tener sensibilidad, esto de decir bueno, che, hagamos unos crosscheck, veamos si esta rentabilidad es la otra y qué sé yo,

**Ignacio Chiera**: que los datos sean coherentes.

**Gabriel Puertas**: Claro. Y eso es básicamente lo que mostraríamos mañana, lo copado sería que la gente lo use y pruebe y bueno después si ustedes lo quieren usar como parte de herramientas también

**Ignacio Chiera**: y después me comentaste que iba a ser alguna automatización, algo por el estilo, yo la verdad que eso no conozco, pero bueno, si la

**Gabriel Puertas**: llegaría tanto yo lo comentaría, o sea vos lo que podés hacer, viste que

**Ignacio Chiera**: yo no te quiero quitar tiempo por las dudas Gabriel.

**Gabriel Puertas**: No, no, te cuento, vos, básicamente es así, el MCP, vos un poco más técnico, yo te lo puedo explicar más fácil, pero el MCP es como un conjunto de APIs que le da Theramo al LLM y le enseña cómo usarlas, básicamente es un, un MCP, un conector MCP. Entonces por ejemplo, hay una API que es Query Data, entonces esa Query data, el LLM sabe qué tipo de queries tiene que cargar en esa API y sabe qué le va a devolver la API. El tipo carga una query y la respuesta termina siendo un JSON con los resultados de la query o un mensaje de error, entonces el tipo itera, qué sé yo, básicamente Theramot está expuesto con APIs, básicamente el MTV. Ahora bien, esas APIs están autentificadas por la persona que lo está usando, son seguras, solamente la puede usar el dueño del workplace y toda esa historia. Entonces hay algunos servicios que vos podés automatizar flujos utilizando eso, el más conocido se llama NN, ahí va. ¿Y por qué es muy útil eso? Porque vos a n le das acceso a ese mcp, después vemos cómo, pero le tenés que dar unos tokens, y lo bueno es que n se configura por archivo, digamos, se configura uniendo flechita y todo eso es como flujo de trabajo. Bueno, pero lo mejor que tiene en n, mi criterio, es que además te permite configurarlo vía archivo, vía un JSON que vos escribís, por qué eso, o sea, si fuésemos mero humano, es lo más hinchahuevo del mundo, prefiero unir flechitas. Pero qué pasa si yo vengo a cloud y le digo, che, vamos a configurar un flujo basado en cloud que está conectado a entera, ya sabe cómo son los datos qué hacen, qué sé yo, le digo, vamos a armar un flujo, no sé, en el que yo tengo una línea que es el stock de los productos, entonces yo cuando tengo cierta alerta de que voy a romper, mando un correo, ¿Entendés? El que me escribe ese JSON es cloud.

**Ignacio Chiera**: Sí, sí, es mucho más configurable, obviamente hacerlo a mano sería una locura, pero al tener la oportunidad de hacerlo con un archivo, o sea le asignás la tarea que vos quieras, según el alerta que salga, según la métrica que esté midiendo, Me imagino que ahí también le meté la automatización en ese JSON.

**Gabriel Puertas**: Tal cual, entonces vos ahí empezás, le pedís a Claude que empiece a hacer esos flujos y en nn te queda armado que vos, no sé, una vez al día vas, miras esa tabla que vos habías creado, se filtra y se queda con lo que están por quebrar stock, entonces no se lo separa y además te arma un correo que vos le configuras a quien se lo manda y ya le avisa que hay algo que se está rompiendo, cosas así, y no sé, ahí ya depende de cómo lo quiere usar la gente. El mensaje va mucho más allá de la visualización. ¿Visualicé, entiendo el problema, los dashboards son súper importantes para controlar, pero qué hago después de que yo vi algo y tomo acción? ¿Normalmente que se hace con un dashboard? Esa toma de acción, Incluso además se puede automatizar, eso es súper.

**Ignacio Chiera**: Sí, sí, sí, los avisos y bueno, como Si, la acción en sí, automatizarlo es,

**Gabriel Puertas**: tenemos cliente que le mandan correo de pedido, o sea tipo filtran por proveedor los productos, o sea ya es una gold que no está pensada para

**Ignacio Chiera**: un dashboard, Sí, sí, está hecho para.

**Gabriel Puertas**: Me armo una vista que tiene los productos que se están por quedar sin stock, ordenado por proveedor. Entonces en n se agrupan por proveedor y arman un correo que dice che para mañana mándame esto, esto, esto, porque estoy por romper stock. Y eso funciona todos los días, a lo sumo te ponen copia a vos del correo y vos decís uy, sí o no, podés hacer un flujo de autorización, como decirte, te avisa a vos que che, voy a mandar todos estos correos, revisa, OK, OK, OK, OK, no, este no, agregale tal cosa, podés hacer esto, es súper importante, no sé si la gente lo conocerá. ¿Vos hiciste algún tema de machine learning, entrenarte modelo? Bueno, entrenar no, pero no es entrenar un modelo, porque ahora ya medio que hasta se bicodea cuando vos hace un flujo, pone que creas un modelo de predicción de demanda, lo podríamos, hasta podríamos hacer la prueba con estos datos. Lo más hincha huevo es la parte de proceso de datos, por qué vos los tenés que limpiar. Hay ciertos procesos, ciertos modelos que requieren que los datos estén parametrizados de una forma particular, normalmente entre 0 y 1 cada una de las variables y qué sé yo, no sé, no importa. Todo eso Cloud lo puede hacer. Todo eso cloud lo sabe, o sea, si yo en eso que te mostré le digo che mirá, vamos a agarrar los clientes y vamos a correr un proceso de k means que se llama, que lo que hace es elige variables para agruparlos en cluster de gente, entonces después te dice, estos son los que más gastan, estos son los que. Parecido al RFM, pero un poquito más pro si querés. Entonces Claude como sabe hacer eso y conoce tus datos, se puede armar sus propias tablas, donde ya sanitizó todos esos datos, hizo lo que tenía que hacer y además te escribe el correo para correr ese modelo. Vos estás bicodeando en cierta forma un machine learning y eso es una locura, porque vos no necesitas saber ser experto en eso, simplemente conoce un poco del negocio y saber que eso existe. Obvio, digamos.

**Ignacio Chiera**: Pero digo, realmente está muy bueno, muy bueno.

**Gabriel Puertas**: Pero bueno, yo mañana, excepto que alguien surja con una duda, no voy a llegar. Un poco es ir al foco del dashboard, por ahí comentar que se pueden hacer otras automatizaciones, pero que lo entiendan y que sepan que nada, si usan estos modelos pueden usar, me preguntan a mí. Yo creo que hoy cualquier persona debería tener una suscripción a uno de los LLM, al menos la de 20 dólares.

**Ignacio Chiera**: Yo lo tomo así es como es

**Gabriel Puertas**: más barato que Netflix y 10 mil pesos.

**Ignacio Chiera**: La comparación es esa. Es como el Internet, si querés, casi y así. Hay momentos donde es crucial esto ya

**Gabriel Puertas**: es un mensaje más personal lo que tiene, que está muy subvencionado ese precio.

**Ignacio Chiera**: En algún momento se va a disparar.

**Gabriel Puertas**: Claro.

**Ignacio Chiera**: Pero está muy para que lo use todo el mundo con ese precio.

**Gabriel Puertas**: Pero en esta época es donde yo creo que la gente tiene que aprender a usarlo, porque cuando el precio aumente, uno va a tener que ser eficiente utilizándolo. Decir a ver, esperá, no necesito yo nada en cloud. Tengo puesto creo que opus 4.8, opus 4.8, pero no quiero poner un modelo más alto, lo tuve porque no lo necesito y se me acaba la cuota más rápido. No tiene sentido. La gente va a empezar a pensar en esas cosas y para aprender eso se tiene que subir ahora que está barato y entender qué son las cosas, como a vos todo esto te ayuda

**Ignacio Chiera**: y usarlo como todo, puede aprender más o menos, pero usando lo aprender. Gabriel, te quiero preguntar una última cosa de mañana me mostran de nuevo las tablas.

**Gabriel Puertas**: Yo la veo.

**Ignacio Chiera**: Sí, pero a ver, voy a dejar

**Gabriel Puertas**: solamente la silver, voy a dejar esta.

**Ignacio Chiera**: Entonces vos va a aparecer con las tablas ya cargadas en la silver, y en esa silver está, y dónde tiene los datos crudos sin transformar los datos

**Gabriel Puertas**: crudos nosotros en la web no te los mostramos, es como que están acá igual. Estas silver son exactamente igual a los datos crudos, excepto las transformaciones que hicimos, pero no vinculó tabla con tabla, o sea uno a uno son todas las tablas que tenemos. Si querés vamos acá. Claro, estas son todas las tablas que conectamos.

**Ignacio Chiera**: Entiendo. Yo te diría, si vos te lo querés anotar, marcaría. Porque a ver, eso como decir que son sólo transformaciones pero no están conectadas justamente, ya son transformaciones, entonces nos irán los datos crudos. Yo marcaría la cancha de sentido de dónde están los datos crudos y esos sirver ya no son crudos. Si, está bien, porque en un proceso de tele eso es re importante, o sea, es la clave del DTL en realidad, que vos en algún lado tenga almacenado los datos crudos y de ahí desde los datos crudos ya en tu plataforma, ahí empieza a transformar. Yo te entendí que lo hace así, pero se puede visualizar en algún lado, sino por lo menos aclararlo que están en tal lado como crudos.

**Gabriel Puertas**: Está bien. Dale, dale, dale. Igual eso ¿Por qué? Porque ellos acostumbran a ver los datos crudos.

**Ignacio Chiera**: Si nosotros tenemos toda una capa de extracción que están los datos crudos y después hacemos todo de nuevo, nosotros guardamos en QBD, que es clic, guardamos toda una capa de las tablas con los datos como vienen y después por ejemplo vos me hablaste Lake House, eso en el Lake House y después hago un flujo de trabajo que paso de que tomo los datos ya no de la base de datos sino localmente, pero agarro los crudos y ahí los paso a un data warehouse con los datos silver ya transformados.

**Gabriel Puertas**: Ahí va. Es más o menos lo mismo, solo que nosotros no le damos. Cuando vos conectaste esta, todos estos datos crudos ya quedaron localmente en theramo almacenados crudos.

**Ignacio Chiera**: Eso yo te lo entendí, pero yo digo para mostrar a los que hicieron el bootcamp, que es como lo hacemos nosotros, eso lo podés mostrar dónde quedan o sería eso, lo que sea que vos puedas mostrar, sino mencionarlo sería.

**Gabriel Puertas**: No, y es mencionarlo de última ahí es muy importante que vos haga los. Llevarlos a que ellos entiendan en el lenguaje de ustedes, como decirte, o sea la única diferencia que vos no los ves a los datos crudos, nuestro front,

**Ignacio Chiera**: la lógica también va, porque vos cuando nos mostra las tablas, justamente ya está en una tabla silver, entonces la lógica va de que no está usando los crudos. Ahí eso va bien, digamos, no es que vos lo mostrás en bronce y ya están transformados, vos lo estás mostrando en silver. Entonces eso acompaña la lógica que uno ya tiene.

**Gabriel Puertas**: Y el paso de bronce a silver, nosotros digamos, no lo hace inicialmente el usuario, se lo hacen los modelos, miran y hacen y entienden y hacen y normalmente son muy buenos. Es como que ese paso de bronce a silver que es de sanitización, lo hace un agente. ¿Cómo ves eso? Eso sí es importante ver. ¿Qué carajo hizo? Perdón, esto lo tengo que borrar, toda la mierda lo voy a borrar. ¿Qué carajo hizo con eso? Nosotros exponemos, acá no hizo nada, acá hizo un select de toda la tabla y desde.

**Ignacio Chiera**: Sí, capaz que no trajo todos los campos, por ejemplo, porque no tiene el asterisco, que capaz que no trajo todos los campos.

**Gabriel Puertas**: No, no trae todo, no sé por

**Ignacio Chiera**: qué los menciona uno por uno.

**Gabriel Puertas**: OK, claro, claro, son todos los. Acá en el asterisco, esta no es la query que crea, pero acá están nombrados todos los campos. Ah, los nombro uno por uno, entendés, o sea no tenés que eliminar ninguno. Digamos, la query que vimos anterior es como si fuese un select asterisco y listo, ¿No?

**Ignacio Chiera**: Perfecto, como no estaba el asterisco pensé que mencionó algunos. Igual te entendí Gabriel, y esto está bueno, o sea está buenísimo. Simplemente

**Gabriel Puertas**: digamos acá si vos escribís una query y pones run query, es como un lugar donde exploras datos, esto para consultar no transforma. A mí me resulta súper hincha huevo porque ya no me acuerdo cómo escribí las query, o sea yo prefiero preguntar

**Ignacio Chiera**: al no hacerlas también, no, no podés saberlos todos los campos. Perfecto, muy bueno Gabriel, yo no te

**Gabriel Puertas**: quiero quitar más tiempo, si vos te querés hacer una cuenta y usarlo con otras bases, que se yo, metele, te ayudamos yo o Lucio, Pero algo que te quiero mostrar, el billing este, tenés el free, tiene un límite de storage, esto tiene que ver con la cantidad de tablas gol, acordate de lo que yo hablo, cantidad de tablas gol, La cantidad de vistas. De vistas, y esta es la cantidad de gigas que podés subir. Y esto es si vos programas un refresh, o sea si vos realmente haces un ETL y vos querés que vaya y mire, eso es cuánto flujo de datos te podés traer y nada, te da el conector.

**Ignacio Chiera**: Perfecto. ¿Ese medio user qué significa?

**Gabriel Puertas**: ¿Cómo?

**Ignacio Chiera**: ¿Ese medio user qué significa? Es como un tipo de cliente free,

**Gabriel Puertas**: no es un error como está escrito es entre 1 y 2. Ah, OK, es buenísimo que lo haya leído como medio users, pero son hasta 2 users

**Ignacio Chiera**: haya conectar con cloud, con

**Gabriel Puertas**: el MCQ y eso es gratarola, esto es súper potente y nosotros estamos por dejar de controlar esto, vos puedas hacer las que quieras, va a haber un límite ahí, pero no sé, serán 300, un límite absurdo, o sea, lo que te va a controlar los gigas que tenés almacenado.

**Ignacio Chiera**: Perfecto. Me surgió otra pregunta ahora, ¿Es una gold table, es el dashboard entero o es una visualización?

**Gabriel Puertas**: Es una de estas. De estas, claro.

**Ignacio Chiera**: ¿Pero esa gold table es la hoja del dashboard o es una visualización?

**Gabriel Puertas**: Vos podrías hacer 500 de estos dashboard, cada dashboard le pega una gol, cada dashboard gira de una gol y pronto va a mirar de una o más, o sea vos podrías hacer un dashboard que consuma más de una Gold. Los dashboard no los estamos limitando, posiblemente en algún momento aparezca un límite, pero podría ser 2000. Lo que sí te limita ahora es la cantidad de. Fíjate que tampoco estamos limitando porque tengo 6 y yo estoy en el free

**Ignacio Chiera**: hasta como aviso, no está restringido

**Lucio Rojas**: y

**Gabriel Puertas**: nada, vos le metés, o sea, esto como herramienta es súper potente. Nosotros acá tenemos un agente que bueno acá me aparecen conversaciones anteriores y qué sé yo, pero. Y este agente tiene un modelo

**Lucio Rojas**: que

**Gabriel Puertas**: para mí anda bastante bien, pero no necesita usar Cloud, vos con este te arma la Gold, te arma los dashboard, te arma qué sé yo. Claro, este posiblemente si vos le pedís los DAX de Power BI, Pero hay que probarlo, qué sé yo, no sé, vos que tenés Cloud, lo tenés que conectar a tu MCP, usarlo, la verdad

**Ignacio Chiera**: está buenísimo, está buenísimo, yo creo que los chicos, los alumnos se van a reenganchar y cada uno tendrá su curiosidad y después también está re bueno el producto para usarlo por ejemplo como un módulo, nosotros que hacemos learning parece que está bueno como para usarlo como herramienta, usamos Click, Power BI, Snowflake y por ahí jugar un poco con eso y capaz que se puede meter Téramo, sobre

**Gabriel Puertas**: todo porque es gratis, sí no, bueno, claro, sí le apuntamos a la empresa no es gratis porque somos buenos, porque nosotros entendemos que hay gente que tiene que entender de qué se trata, es súper importante nosotros que haya gente que tenemos un acuerdo con cómo es Data Q Data, cómo Data

**Ignacio Chiera**: Data, son un montón de empresas, conozco datiq que es

**Gabriel Puertas**: de clic, una que es muy grande que hace capacitaciones es DataQ casi seguro que también da algunos webinars, pero ustedes también lo pueden hacer y usarlo como una herramienta más, digamos. Bueno, les muestro cómo funciona esto. Nosotros es 100% agéntica, 100% toda la creación de todo y si vos querés

**Ignacio Chiera**: podés meter mano en esa creación o transformación.

**Gabriel Puertas**: Sí, sí, o sea, meter mano a este nivel sería meter mano en la creación de las tablas Silver, en cómo vos las transformas.

**Ignacio Chiera**: OK. No me gusta que quede con esa mayúscula le cambio la query.

**Gabriel Puertas**: Claro, claro. Son tuyas digamos, directamente. Ahí no te hacemos nada. Vos le pedí algo al modelo, el modelo te traduce eso en una Go,

**Ignacio Chiera**: pero vos podés hacer esa gol tabla a mano, por ejemplo.

**Gabriel Puertas**: Sí, mira, no lo preguntan mucho pero sería como old school. Vamos a ver esta del producto, rentabilidad. No, no, fíjate, bots acá lo que nosotros tenemos, yo no te lo mostré, pero bueno, esta tabla tiene como una serie de descripciones.

**Ignacio Chiera**: Como un proyecto.

**Gabriel Puertas**: Claro, una descripción y fíjate que acá tiene instrucciones, un registro por producto, product query, fíjate que ahí yo le estoy dando el grano de la tabla, incluí product name, estas instrucciones las escribió Claud según tu prompt. Según mi prompt, interpretó mi prompt y agarró y escribió estas instrucciones. ¿Qué podría hacer acá? Decir incluir product name, no sé, yo me meto acá y le borro product name, digo no, incluye el product name, guardas esto tiki y lo corres y el modelo de Theramo va a interpretar esa instrucción y va a ajustar la query para lo que sea. Eventualmente si vos querés le podés escribir una query y decir ejecuta esta query y te la va a hacer. Entendés, o sea, lo que hace Cloud no es escribir la query directamente, sino que le da instrucciones al modelo de Theramot y Theramo que tiene conciencia de cómo está guardada en su infraestructura los datos, adapta esa query para que funcione un poco la idea.

**Ignacio Chiera**: Y en eso también que por ejemplo no se usarían tanto los tokens de Cloud, por ejemplo, pero lo que vos usas de Cloud son esas instrucciones.

**Gabriel Puertas**: No, usa la generación de la tabla a mano. Tabla, le pongo un nombre, acá tengo que seleccionar qué tablas silver yo voy a utilizar. Yo como soy medio vago le voy a mandar todo la descripción, esto es opcional, así que no lo voy a poner, le voy a decir, no sé, quiero una tabla cuyo grano sean las rentas y acá le agrego algo más y quiero, quiero que, no sé, calcules el margen bruto basado en, qué sé yo, el precio, precio por unidad. Ahí yo estoy escribiendo las instrucciones y

**Ignacio Chiera**: ahí nunca, no gastaste nada de cloud,

**Gabriel Puertas**: porque básicamente lo que hace Cloud es interpretar lo que vos querés y escribir bien esas instrucciones. ¿Qué nos pasaba a nosotros? Nuestro producto inicial era así o sea, nosotros le decíamos ponele las instrucciones y él te hace, pero que la gente no sabe dar instrucciones y el que sabía usa bien era Bo, pero que básicamente tus instrucciones terminaban siendo query de SQL. Filtra tal cosa, seleccioná tal cosa. Como escribí la query cuando lo pudimos conectar con MCP, ahí explotó, porque los agentes del LM son muy buenos haciendo justamente eso. Es decir, yo lo entiendo a Ignacio que lo que quiero, conozco muy bien los datos, uno eso, dos mundos con instrucciones que son. Que están muy bien.

**Ignacio Chiera**: Claro, si, la traducción del lenguaje natural,

**Gabriel Puertas**: como tipo la forma de codear, pero si vos te querés armar las tablas de esa forma, nada, te las arma. Esto cuando termine va a generar una, va a generar una query de SQL que después le podés seguir agregando instrucciones para ir editándola y haciéndola lo que vos necesitas.

**Ignacio Chiera**: ¿Y no entendí la parte, o sea, si el dashboard puede agarrar una sola query, cómo hace todos los gráficos?

**Gabriel Puertas**: No es que hace una sola query, básicamente el dashboard es código HTML, cada uno de estos valores es una query, está en el código HTML, lo que yo te decía, que le pega una sola tabla, ¿Entendés? Que se yo, estas ventas totales, no sé suma el total de ventas y lo muestra acá, ¿Entendés? Esto es una query en sí, el gráfico de una query en sí, pero usa como fuente de información una sola Gol.

**Lucio Rojas**: OK,

**Gabriel Puertas**: en esa golpe gana esa Gol.

**Ignacio Chiera**: Claro, o sea, en esa Gol tendría que estar la hoja del dashboard entera, entonces, por ejemplo, en términos de query. Claro, tendría que estar solicitado todo el Dashboard.

**Gabriel Puertas**: Técnicamente sería así, en la Gol deberían estar todos los datos que vos querés que se vean en el Dashboard.

**Ignacio Chiera**: Perfecto.

**Gabriel Puertas**: ¿Después cómo te armo el Dashboard? Eso se va a encargar Cloud, el prompt, lo que vos quieras, ¿Entendés? Lo que nosotros ahora es, y lo vamos a tener dentro de poco es interactividad, o sea que vos le puedas poner filtrito, que le pueda poner no sé qué miedo, todo eso como te lo hace Cloud, Pero es básicamente lo mismo, o sea, fíjate que quiero ver si por acá está, en algún lugar está el código, el HTML que hizo tiene que ser uno de estos. Run SQL query. Bueno, relevant chart No, te quería mostrar cómo es el código HTML de eso,

**Ignacio Chiera**: con el F no te lo llega a mostrar.

**Gabriel Puertas**: No, no, no, en el F no, no, HTML que lo levantamos en la página y ese HTML te lo hizo Cloud. Perfecto, la verdad está muy bueno el Artifact, si vos lo abrís, fíjate, este es el código HTML del Artifact y por acá tiene las query hechas, digamos, lo que pasa, lo que tienen los Artifact es que ya le mete los visual clean sheets, en algún lugar debe tener los valores, acá también data, ahí se trajo en el propio código, se trajo todos los datos y entonces así lo muestra la clave. Por qué digo yo que Power BI, todas esas cosas ya está muerta, en algún momento se van a adaptar, algo parecido a esto, que se están adaptando, están usando gentes. ¿Sí, pero enganchado en que vos armes el grafiquito, elige el tipo de gráfico, es una mierda, o sea te lo tiene que hacer un agente, entendés, que vos le digas, yo no sé, yo acá le mandé las mismas imágenes que armaste vos, pero le digo sabes qué no me gustan estos gráficos, quiero que no sé sea rojo y negro porque soy hincha de Newell y bueno y ahí terá y él te hace rofi negro entendés, o cosas así, o quiero un gráfico que sea de torta, quiero un gráfico que sea así, asá, esto no se entiende, no que vos te tengas que meter a hacerle las cosas dónde están hoy las herramientas en el chat con los datos, que vos le digas cuánto fueron las ventas, el margen bruto de no sé cuánto fue tanto, entonces en eso, pero esta interacción, o sea vos usa esto, te acostumbramos a usar esto, que te haga él los dashboard cuando va a usar Power BI de vuelta, te querés matar?

**Ignacio Chiera**: ¿La verdad que está muy bueno Gabriel y bueno, gracias también por la charla,

**Gabriel Puertas**: la explicación, dale tranca y después nada, nos quedamos en contacto para eso, digamos, que la gente lo use y que se haga cuenta y nada, después en próxima, después si tenemos que hacer otro webinar con gente que esté aprendiendo, lo

**Ignacio Chiera**: hacemos, no hay problema, todo eso ya lo manejan, viste, con Cristian, con los chicos de Jupi, pero por ahí mañana entonces por lo que vos me dijiste, algún meto algún bocadito como para llevarlo, hacer la comparación con lo que hicimos Jupi, parece bien?

**Gabriel Puertas**: Sí, sí,

**Ignacio Chiera**: muchas gracias. Buen día, que estés bien.

**Gabriel Puertas**: Igualmente.
