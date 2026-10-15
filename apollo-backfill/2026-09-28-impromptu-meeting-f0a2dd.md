# Impromptu meeting

**Fecha:** 2026-09-28T13:32:05.241+00:00  
**Duracion:** ~35 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Gabriel Puertas <gabriel@teramot.com>, Christian Schiavo <>, Pablo Barbarelli <>  
**Externos:** Christian Schiavo, Pablo Barbarelli  
**Apollo ID:** 6aba74934267090010f0a2dd

---

**Franco Ferrero**: Pablo, ¿Cómo estás?

**Pablo Barbarelli**: Buenas, buenas. ¿Cómo andan?

**Gabriel Puertas**: Pablo, ¿Cómo anda?

**Pablo Barbarelli**: ¿Se escucha bien ahí?

**Gabriel Puertas**: Sí, perfecto.

**Pablo Barbarelli**: Estoy siendo seculares y a veces en meet mete un poco de ruido el micrófono en la compu. Primero, mil disculpas, el juez nos agarró.

**Gabriel Puertas**: No Pablo, no te haga problema.

**Pablo Barbarelli**: Nuestro CEO que es nuestro principal usuario y pidió ver unas cosas y terminó siendo una hora y media de charla. Así que quise extender un poquito el inicio, pero disculpen que fue. Bueno, denme un segundo a ver si se suma Cristian.

**Franco Ferrero**: Dale.

**Pablo Barbarelli**: Que den un sueño de le man, dice Cristiana. Un segundito, a ver si puede ser. Ahí le mando la invitación.

**Franco Ferrero**: Hola Cristian, ¿Cómo estás?

**Christian Schiavo**: ¿Qué tal? Buen día. ¿Cómo andan? Disculpen la demora

**Pablo Barbarelli**: en la convocatoria. Bueno, ¿Todo bien?

**Christian Schiavo**: Sí, todo bien, todo bien.

**Pablo Barbarelli**: Bueno, ya me disculpé con los chicos porque el jueves estuvimos con Marcelo a las corridas. Tenemos media horita. El objetivo nosotros queremos un poco, ya lo fuimos adelantando por mail, vemos valor y queremos avanzar con una poc y poder transformarla. Somos los primeros interesados en que Grupo Ayudín la adopte. Y entonces transformar esa poc inicial en en un producto que realmente genere valor. Y hoy tenemos al directorio, principalmente el CEO y con eso decanta, ya lo hablábamos esto, pero decanta a los directores como principales provocadores de usar data. Y hoy lo que nos pasaba un poco lo que le contaba otra vez Agave y demás, era esto de muchas veces por más que hagamos, somos cuatro gatos locos y siempre llegamos tarde al delivery reporting. Entonces siempre lo hacemos perfecto, lo hacemos muy bien, somos los mejores. Pero reactivamente, esto de que queremos empezar a generar este caso de uso, primero nosotros con Gris y con Fe Director IT, para enseguida lograr empezar a hacer a los directores y al SEO chatear con nuestra información. Básicamente eso es un poco el driver de lo que queremos provocar. Y si eso va bien, decanta. Bueno Gaby, lo dijiste otra vez. El gran problema de esto es que enseguida van a necesitar o querer crecer en usuario. Después tenemos que ver cómo lo manejamos a nivel presupuesto. Pero otro buen problema que tenemos.

**Gabriel Puertas**: Está claro, está buenísimo. ¿Me encanta porque digamos, muchas veces nosotros es como que nos juntamos con el área de datos y se ve más, no sé si amenazada, pero como diciendo, pero no tiene sensación de que muchas veces no está llegando como piensan? Le damos todos los informes que quieren, Pero está buenísimo, me encanta. Nosotros estamos para meter una prueba esta poc. Nosotros, normalmente lo que a nosotros nos interesa mucho de la poc es que agregue valor, que tenga un tiempo como acotado, cosa de que nada, o ustedes nos dan feedback o avanzamos, pero nada, me interesa muchísimo hacerla y hacerla lo antes posible.

**Pablo Barbarelli**: Buenísimo, perfecto. Bueno, un poco las cosas que yo iba preguntando en el intercambio de correos es pensando en el horizonte, toda esta poc ya empezar a construirla sobre bases que podamos después activar X cantidad de. Empezando con un poco la dimensión que nos habían dado más o menos de empezar con cinco usuarios, Este tier de 400 dólares con 5 usuarios, viewer 5 usuarios para también conectar con cloud, sería como el primer paso, ni bien armemos esta poc, que nuestro objetivo y nuestra idea es, o compromiso, mejor dicho, es, le dedicamos las próximas dos semanas a esto como para darle forma, y ya después, si van dos, tres semanas, si vemos que esto funciona como estamos pensando y como fuimos, que vimos la otra vez y demás, con el archivo plano que le pasamos, activar este primer TIR de un tenant con cinco usuarios y después ver ya detalles más administrativos, comerciales, NDAs, etcétera, etcétera, etccétera. Dicho eso, ¿Cuál piensa entonces que debían ser las próximas acciones como para empezar a laburar?

**Gabriel Puertas**: Nada que hagamos, digamos. ¿Ustedes dónde tienen los datos?

**Pablo Barbarelli**: Hoy está en Data Fear, todo el mundo, Data Fear, que eso es. Ahí deberíamos ver cómo hacemos esa conexión. Datafear hoy SAP hosteado en AWS en San Pablo, en el detalle, ¿No?

**Gabriel Puertas**: Ahí va. Pero que lo tienen, o sea, es como una réplica de SAP. No conozco Data Fear, pero es un

**Pablo Barbarelli**: data warehouse que replicamos y vamos haciendo réplicas de información delta, no sólo de SAP, sino de un montón de otros orígenes, de datos de mercado, sistemas internos de producción, hay un montón de información. Claramente el core es app, pero bueno, hay un montón de.

**Gabriel Puertas**: ¿Hablando más de lo fierro, eso es en AWS que en donde? ¿En un s un archivo?

**Pablo Barbarelli**: No, no, es toda infraestructura SAP que está hosteada en AWS en San Pablo ahora, qué tiene por detrás, Entiendo yo. Corregime, Cris, vos sos el técnico acá, el que más conoce todo mundo HANA, SAP, tanto. Claro, toda la forma en que se almacena todo esto es memoria, Han.

**Gabriel Puertas**: Ah, buenísimo, porque nosotros tenemos hecho el conector de SANA, perdón de HANA, pero no lo, o sea, todavía no tuvimos nadie que lo probó, así que ideal. Pero nada, o sea, para nosotros los siguientes pasos es, yo no me acuerdo si nosotros no teníamos un NDA, nos suelen pedir eso, por eso lo menciono, pero una vez que tengamos eso, nos ponemos de acuerdo y nada, lo que vos habías visto esto te lo menciono, pero lo vamos a mantener. Nosotros cambiamos el pricing la semana pasada, pero con ustedes vamos a mantener lo que habíamos hablado. Sería eso simplemente, o sea, si ya tenemos el NDA y está todo bien, hacemos una reunión más técnica y nada, metemos el conector, digamos.

**Franco Ferrero**: Claro, a mí más que nada para ya conectar los datos, conectamos la fuente y una vez que ya podemos conectar la fuente, podemos hacer bien la poc y para que ustedes vean realmente el valor de la plataforma y a partir de ahí ya ustedes lo van a poder seguir usando.

**Gabriel Puertas**: Una vez que nosotros hagamos la conexión, tenemos que definir dos cosas, generamos el conector, ahí hay un proceso de ingesta de datos que lleva tiempo, depende el volumen de los datos, en realidad depende bastante de no tanto cuántos datos tiene, sino de cuántas columnas y todo eso, porque empiezan estos procesos que describen cada una de las cosas una sola vez. Y ahí después ya empezaría, ah, perdón, me falta preguntarle algo. ¿Y ustedes lo usarían con que? ¿Tienen cuentas de cloud o algo así?

**Pablo Barbarelli**: Sí, el caso sería con cuenta de cloud.

**Gabriel Puertas**: Nada, ahí nosotros es como en la POC del lado de customer success, ¿No? Nos conectamos junto con la gente que lo use, no sé si van a ser ustedes o alguna otra persona de COSO, tipo comercial o lo que sea, y nosotros los acompañamos enseñándole a usar, mostrándole la dinámica, cuando ellos crean algo en cloud, cómo se ve, qué sé yo, qué cosas pueden hacer y todo eso. No es que nosotros sabemos del negocio de ustedes ni nada, simplemente acompañarlo para que el flujo de la herramienta sea lo más natural posible. Lo que nos suele pasar es que una vez que la gente entiende, ya después empiezan a meter y nos toman como consulta, pero nada, vamos a estar disponible el tiempo que tome la poc.

**Pablo Barbarelli**: Entonces clarísimo, primero NDA, yo ya se los mando me parece que no se los había mandado todavía. Ya se los mando. Segundo, ahí más una reunión técnica gris con los chicos para empezar a hacer la conexión para que puedan ingestar hacia theramot la información que definamos y esto también nos va a permitir ir dimensionando. En esta poc había cantidad de tablas, gol tablas, bueno, ahí había toda una definición que teníamos que ir viendo. Claramente nosotros vamos a llevar la información al principio y después tenemos que ir viendo cómo va evolucionando esto. Pero lo más clave para poder responder las preguntas de negocio, que queremos o que pensamos que podemos querer, más allá que después podamos tener algunos descubrimientos. Y sobre esa, cuando está hecha esa conexión, el objetivo es empezar a interactuar con información y poder responder cosas que nosotros mismos podemos confirmar que están OK. Como mínimo primero, hoy tenemos un montón de reporte, un montón de cuestiones,

**Franco Ferrero**: es

**Pablo Barbarelli**: lo primero que vemos que si yo le pregunto lo que ya yo estoy calculando que me responda, OK, básicamente eso es un nivel de moores muy bajo, después vamos a empezar a exigirlo un poco más y después cuando exijamos entre nosotros, ahí sí sumaría alguien más del negocio para que, pensando bien a quién, para ver cómo lo podemos desafiar un poquito más y ahí ya con eso estamos OK. Después ya migramos al plan y a sumar a gente que empiece a laburar con información.

**Gabriel Puertas**: Buenísimo. Normalmente lo que termina pasando es cuando ustedes prueben, van a ver que yo creo que lo interesante que ustedes vean que como que no se las vuela en el sentido de decir bueno yo le pido que me haga un reporte, me va a generar las tablas, va a estar ahí el SQL, voy a poder ver que está bien hecho, que los números van bien, si le faltó algo se lo pide y me lo corrige, qué sé yo, o sea que ustedes tomen en eso, cuando vos pasás al área comercial, ahí el desafío no va tanto por ahí, sino que a mí me parece lo más copado es que darse cuenta como Claude entiende el área comercial y consigue resolver ese tipo de. No sé, ellos hacen un reporte de venta y se lo hace bien y hace delivery de lo que realmente esa persona estaba buscando, que quizá no es tan técnica, no sé si me explico la sutileza, digamos, como decir ustedes van a ver más la query, ellos van a ver más resultados. Y le hizo el dashboard con los botones, digo, de las empresas con las que fuimos caminando. Comentaba eso ahí. Después en la evolución, nosotros ahora en esta prueba podemos conectar todos los datos que ustedes necesiten. Nosotros ahí vamos a hacer un dump de la información, porque estamos en esta versión SaaS. Después, si deciden avanzar, es recordarle que como ustedes están en AWS y eso, incluso tenemos posibilidades de que los datos no salgan de su infraestructura. Si hacemos un deploy y quieren avanzar en ese sentido, está la posibilidad de que. De que en cierta forma Teramot corra con los recursos de su propio AWS. Eso es un detalle que me parece interesante para la evolución.

**Pablo Barbarelli**: Está clarísimo. Sí. Y después también en este proceso también esto de cómo vamos los Delta, una vez que empezamos a replicar información, cómo vamos replicando la información nueva, las novedades, todas esas cuestiones que son no menores, se supone que está resuelto claramente, pero

**Gabriel Puertas**: bueno, tenemos cuestiones que vos decís, las actualizaciones.

**Pablo Barbarelli**: Exacto, exacto.

**Gabriel Puertas**: Ahora lo que vamos a hacer, una vez que nosotros tengamos el conector, el paso siguiente es definir con qué frecuencia actualizamos los datos. Ahí hay dos caminos. Depende un poco si es posible configurar una actualización por novedades, por así decirlo. Es un camino. Si no, nada. Definimos un horario y se hace un DAM de toda la base con la frecuencia que definamos. Puede ser diaria, puede ser como usted diga. Esa es la forma que tenemos hoy en el SAP. Lo de la configuración por novedades. ¿Por ahí muchas veces depende de la base de datos, porque yo tengo que tener Mindsamp o algo que me diga, che, que cambió?

**Pablo Barbarelli**: A eso me refería.

**Gabriel Puertas**: Si eso lo tenemos, nada. Y eso es rapidísimo. Si no, lo otro. Normalmente las empresas que no tienen eso tienen actualizaciones diarias que ocurren en algún momento en la madrugada. Pero eso se configura ahí. Perfecto.

**Pablo Barbarelli**: Esas son las cosas que tenemos que ir pasando y aprendiendo y reviviendo. Cómo resolver. Aparte de NDA, Después cuando iniciemos, ¿Cómo es el modelo? ¿Hay algún contrato que debemos firmar? ¿Algún acuerdo? ¿Cómo es el allá del envíe que nosotros les compartamos? Donde obviamente estamos

**Gabriel Puertas**: en particular, como nosotros en el caso de ustedes no estamos haciendo ningún. Muchas empresas nos piden tipo, bueno, No, pero vengan ustedes y me hacen, no sé, por decirte, los 10 primeros dashboards me los haces vos o yo quiero que además vos le des capacitación a la gente o algún paso más. La prueba que estamos hablando con ustedes no es ni más ni menos que entrar a la página y armarse un workplace, o sea ustedes lo podrían hacer sin hablar con nosotros eventualmente, yo prefiero el camino en el que hablan, pero nada, si a vos te parece podemos hacer una especie de acuerdo por esta prueba, pero es basado en lo que nosotros tenemos expuesto, o sea hoy no cambia mucho, lo único que cambia es que cuando nosotros empezamos a hablar con ustedes esto costaba 400 dólares, nosotros ahora eso lo tenemos en mil y tenemos algunos cambios que eso, o sea los upgrade a 1000 si le aplicarían que tienen que ver, son 10 usuarios incluidos los límites, ponele, este tier tiene 150 gigas y 1.5 tera al mes de procesamiento, eso tiene que ver con las actualizaciones, lo que yo te comentaba, después los conectores al MCP y ese tipo de cosas. Lo que hicimos nosotros fue ajustar un poco el pricing dándole más cosas al tier de entrada y subiendo el precio. Pero nada, lo copado para la prueba es, o sea, yo no quiero que la prueba quede enganchada con temas comerciales, entonces si hablamos 400 lo dejamos 400 lo prueban ahí y nada, y eventualmente si requieren dos o tres cosas más o decir che mirá necesito meter tres usuarios más porque quiero que el director lo pruebe, también se puede hablar, no es que algo rígido. Si a ustedes les sirve por alguna cuestión de procurement que nosotros hagamos una especie de contrato o algo por el estilo, se lo mandamos.

**Christian Schiavo**: Por ahí lo que estoy pensando rápidamente es para Compras tener un presupuesto ya de lo que hablamos, o sea hacerlo formal y también ver el tema de los datos de alta de cliente, de proveedor, para también ir adelantando todo eso, que es una forma digamos de ir acá también Compras tiene todo un proceso de compra bastante particular, entonces bueno, nada, de esa manera, sin tener este acuerdo digamos de trabajo, sí el NDA empezar a recorrer ese camino formal por las

**Gabriel Puertas**: dudas usted tiene cómo fijarse si nosotros ya no tenemos alta de proveedor, a mí me parece, nosotros ya habíamos hablado hace como tipo año, año y medio.

**Pablo Barbarelli**: Yo no recuerdo que hayamos hecho el proceso de alta.

**Gabriel Puertas**: Yo hablé con. Ya no aplica. No, pero digo, estoy seguro que firmamos un NDA y todo, pero era más con un área comercial, no me acuerdo si hicimos alta de proveedor, tengo como ese recuerdo. Pero bueno, nada, última,

**Christian Schiavo**: pasame tu quit y lo busco rápidamente.

**Gabriel Puertas**: El quit de Teramo, No sé Franco, si vos lo tenés a mano, yo no me acuerdo.

**Christian Schiavo**: Sí, y lo busco por quit y vemos a ver si están dados de alta en la base de datos, si están ya como proveedores, listo.

**Pablo Barbarelli**: Sí, sí, si no, ya no hay problema, lo activamos y listo también.

**Gabriel Puertas**: De todas formas no quiero, por eso yo le decía, yo prefiero, a mí me interesa mucho tipo NDA, hacemos los conectores, después la parte comercial para pagar eso va, no frenemos, digamos, no pasa nada. Así que nada, si les parece vamos con eso. Pasanos Pablo tu versión, nosotros revisamos y firmo yo.

**Christian Schiavo**: Y acá dos cosas para adelantar, hay que probar dos conectores, o DBC o cómo se llama, o el de HANA que tenés así por lo dos. Yo a The Bieber me estoy conectando muy bien con Hannah, anda muy rápido y también me conecto con ODBC, con lo cual nada, habría que probar cualquiera

**Gabriel Puertas**: de los dos, pero no entendió. El de Hannah capaz que estoy preguntando una borrada, pero digo, son distintas fuentes de información.

**Christian Schiavo**: HANA No, no, la base HANA te permite entrar por ODBC.

**Gabriel Puertas**: Ahí va.

**Christian Schiavo**: Y te permite entrar.

**Gabriel Puertas**: ¿Usa PowerPoint?

**Christian Schiavo**: Claro, Excel, si, yo me conecto con

**Pablo Barbarelli**: Excel,

**Christian Schiavo**: pero la base. Pero eso lo probé con deviver, que es una herramienta de consulta y tiene, digamos, también obviamente el conector HANA, yo me conecté con ese y funcionó bárbaro. Así que nada, lo dejé siempre en HANA Y este también, si tenés las dos posibilidades. Nada, habría que ver cuál responde mejor, porque si tiene una mejor velocidad de transferencia.

**Pablo Barbarelli**: Yo creo que hoy ODBC nunca, siempre bien ponderado porque nos salvan un montón de cosas, Si hubiese algo más moderno, más seguro, más performante, genial.

**Gabriel Puertas**: Hoy lo usamos, es una opción, tenemos hecho, o sea, vos podés, toda la parte de seguridad está bien hecha en los conectores acá con Termo, después lo vamos a ver en detalle con. Con el ingeniero, pero nada, pueden configurar túneles, todo lo que haga falta, eso está hecho bien, digamos, nosotros certificamos SOC, o sea no debería tener ningún problema. Lo que le decía del conector es que nada, nosotros tenemos desarrollado muchos conectores que todavía no apareció un cliente que diga yo tengo los datos así de SAP tenemos lo mejor de SAP es que no sé cómo estará en HANA, pero bueno, nosotros usamos SC y nada, viste que las tablas y las columnas son crípticas, o sea, lo bueno de eso es que los modelos entienden el diseño de SAP, Entonces mi impresión es que en particular la gente que tiene la base de datos tipo SAP, que usa SAP con esto vuela porque los acelera un montón, o sea, si vos lo haces con gente, necesitas ciertas personas que entienden de SAP para resolver las cosas y cuando usás los modelos tipo cloud o algo por estilo, junto con el laburo que hace Teramot, vuela, los tipos piden casa y te lo acá

**Pablo Barbarelli**: el único asterisco Gaby, es que nosotros cuando tenemos a datafear, que datafirma la información o la conexión sería tipo HANA, en donde nosotros agarramos todas esas tablas de SAP o vistas, CDs vistas, son información que hoy SAP te devuelve para poder llevártelas a este Ataware House y de donde nosotros como que rearmamos todo el modelo, relacionamos datos maestros, relacionamos información tradicional incluso y que de la última que hablamos hace un año y medio hasta ahora lo que venimos laburando, donde armamos todas las capas de tablas FA y demás, para que tanto los modelos que consumimos de la herramienta de reporting del propio SAP o herramientas de reporting que el usuario final del negocio hace tipo self service como Power BI o como Excel mismo, puedan interpretarlas. Yo creo que esto va a ser que sea incluso, no sé si más simple, pero

**Gabriel Puertas**: si ustedes ya armaron un warehouse, eso anda bien, porque me imagino que el warehouse ya tiene tabla de hecho dimensiones, las columnas tienen sentido y toda esa cosa. Claro, ahí hay dos casos de uso, una es Teramo, te lo usa para, para, no sé, para el de comercial que va a consumir principalmente el warehouse y para ustedes, o sea, si le falta hacer cosas al warehouse, ustedes lo pueden usar tipo como para bycodear eso, decir che bueno mirá, necesito agregar esta dimensión, necesito agregarle estas cosas y nada, le genera los SQL, a mí me parece un montón

**Pablo Barbarelli**: eso fue la primera vez que cerramos, me mostraste eso que me pareció espectacular, estábamos recién en pañales nosotros.

**Gabriel Puertas**: ¿Ustedes habían cambiado, no? Era Clorox y cambió, me acuerdo eso.

**Pablo Barbarelli**: Sí, exacto. Lo que digo es, a lo mejor después podemos marcar Cris, una charlita también con ello, porque ahora con Cris, la última vez que charlamos vimos más la parte de esto de chatear contra información, pero seguramente este valor agregado de poder empezar a bycodear y armar a lo mejor que nos ayude a Theramot a construir nuestra base de datos, es un caso de uso que podemos a lo mejor acelerar mucho lo que venimos haciendo.

**Gabriel Puertas**: Claro, la única diferencia es conectar distintas fuentes de información. Incluso vos te podés armar en el mismo workpace de ayudante, arma dos proyectos, uno que sea el de data o IT, el que ustedes quieran, y el otro para los comerciales. Los comerciales utilizan el warehouse y decís, bueno, este es tu warehouse, si querés podés subir Excel, podés hacer lo que vos quieras, pedime cualquier cosa si necesitas algo, y al otro ustedes le conectan sus datos CRUD y lo usan para eso. Lo que a mí me parece súper útil, que nosotros lo venimos planteando con Theramot, es que todo lo que vos haces es transparente. ¿Qué va a pasar ahora? Nosotros vamos a levantar los datos y vamos a correr ciertas sanitizaciones. Sanitizaciones tienen que ver, no sé si usted tiene el warehouse, probablemente no haga nada, pero digo, imagínate otra base de datos que son varias fuentes. Claro, yo unifico formato de fecha, cosas así. Bueno, nada, hago eso. Todas esas transformaciones, código SQL que está todo expuesto, o sea, ustedes lo pueden, o sea, lo pueden ver, lo pueden auditar y además lo pueden cambiar, si se lo piden se lo cambia. Y después si ustedes arman eso, nosotros tenemos empresas que lo que hacen es decir, bueno, yo me conecto a los datos crudo, voy armando como mis tablas gold de ese proyecto son una especie de warehouse, que es como que las tablas gold van a ser las fuentes del otro proyecto, como que vos le armás el warehouse y después los otros proyectos te consumen de acá. Y ese tipo de laburo se hace después, como yo le digo, como está todo expuesto el código, vos decís, bueno, che, yo sé que esta era la tabla que tenía que hacer, pero no la quiero enterar, la voy a llevar a AWS. Te lo lleva y lo haces tener el código Ahí, o sea, va a tener que cambiar los nombres a las tablas, no sé, pero digo, el laburo hecho totalmente. Pero bueno, dale chicos, Pablo, yo me tengo que subir a otra call, pero

**Pablo Barbarelli**: estamos igual ahí yo ya compartí la NDA, avísennos cualquier cosa y avanzamos.

**Franco Ferrero**: Una vez que ya mandamos el NDA, mandamos los mails para coordinar otra reunión, así conectamos la foto.

**Pablo Barbarelli**: Dale, ahí, porfa, sumen a Cris siempre en copia, que él va a estar liderando todo esto.

**Gabriel Puertas**: Dale, buenísimo chicos, que tengan buena semana.
