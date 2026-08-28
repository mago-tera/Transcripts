# Teramot <> BIND

**Fecha:** 2026-07-16T19:21:42.077+00:00  
**Duración:** ~30 min  
**Participantes:** Bruno Ruyu <bruno@teramot.com>, Facundo Ignacio Vivas <>, Micaela BACHER <mbacher@natan.vc>, Inti BENITES <ibenites@bind.com.ar>, Candelaria Villagra <cvillagra@bind.com.ar>, Franco Ferrero <franco.ferrero@teramot.com>  
**Externos:** mbacher@natan.vc, ibenites@bind.com.ar, cvillagra@bind.com.ar  
**Apollo ID:** 6a59364c96f27a0018dc8a1c

---

**Micaela BACHER**: Okay. No me leyó todavía, debe estar terminando la reunión.

**Bruno Ruyu**: Tranqui.

**Micaela BACHER**: I make both shame. Buenas, ¿Cómo va? Bien, ¿Vos?

**Inti BENITES**: Bien, bien. Acá con el vuelo sobrevendido, as usual.

**Micaela BACHER**: Olvídate. ¿Están todos igual?

**Inti BENITES**: ¿Solo conmigo la reunión o esperamos a alguien más?

**Micaela BACHER**: No, solo con vos, porque con todos los que estaban invitados entre la semana pasada y la anterior, medio que todos se fueron sumando a otras reuniones, así que esta era la reunión original, pero después nada, Cacho estaba con Cande y se sumó Bruno y así. Así que un poco el objetivo de ahora es hablar con vos. Nosotros igual hablamos el año pasado, me parece.

**Inti BENITES**: En concreto lo que me preguntó Hernán y creo que Jaime también en algún momento, que imagino que lo habrán hablado también con Jaime, era si se podían utilizar las capacidades de theramo para acelerar nuestro proceso de migración a Databricks desde DB Webcom. Sí, sí.

**Bruno Ruyu**: Hola Inti, ¿Cómo andás? Algo que en su momento lo charlamos, estuvimos en la reunión de Hernán y Jaime y fue una de las dos posibilidades donde vimos valor y que claramente entendemos que es algo que les puede agregar mucho por esto de la ventaja en tiempos. A ver cómo sería hoy Teramot hacia un Data Lakehouse. Su forma de proceder es esa, pero no implica que. Pero digamos, algo que tenemos siempre como lineamiento en Theramot es ser transparente en todo lo que hace Téramot, Así que todas las query de transformación, que básicamente es lo que conforman ser un Data Warehouse, un Data Lake House, quedan expuestas. Así que uno podría ir, plantear eso, plantear las transformaciones necesarias y después agarrar esas transformaciones y llevársela a Databricks y correrlas ahí para que ya queden en ese país. No es lo más cómodo. Obviamente uno preferiría no tener que hacerlo en dos lugares, llevárselo, pero hoy eso sería la forma de hacerlo ya mismo.

**Inti BENITES**: Dicho eso, tendría que mover a la infraestructura de téramod y ahí a la infraestructura de Databricks. No es que instalo algo on premise y del ETL paso por theramo y de ahí voy a Databricks.

**Bruno Ruyu**: Claro, hoy no, hoy es la única posibilidad.

**Inti BENITES**: Pero Bruno, ya se juntaron ustedes con Nico y con Nicanor. Con Nico y con Nicanor.

**Bruno Ruyu**: Con Nicoli y hablamos específicamente de esto también.

**Inti BENITES**: Ah, listo, Listo, listo.

**Bruno Ruyu**: Dicho eso, es entendible que tal vez digan la verdad que por tema de costo no tiene una gran implicancia, salvo que estemos hablando ya de muchísimos teras, con lo cual tampoco no es un problema. Pero digamos, es entendible. Si no es la opción más feliz para llevarse todo ahí. Estamos trabajando en una versión totalmente experimental por ahora. No quiero comprometernos a tener algo donde no es necesario hacer todo eso, sino que uno hace como una versión que de alguna forma se conecta y no necesita llevarse y duplicar todo ese wirefaust en otro lado. Pero estamos haciendo las primeras pruebas, está como a modo de experimentación. Con lo cual si fuese ese, dependiendo un poco cómo son las ventanas de tiempo y el interés, lo que se puede empezar ya es con la versión actual que es en AWS.

**Inti BENITES**: Tal vez Bruno, lo que. Yo creo que lo que va a determinar, independientemente de que los datos piquen en dos o tres infraestructuras, es cuánto a mi banco, eso me acelera y me deja ya automatizado. Pipeline de datos de mi información de un lado hacia mi Lake House y ya no sé qué. ¿Dejan la capa Silver lista ustedes?

**Bruno Ruyu**: ¿Cómo sería, digamos, ¿Se hace silver y gold?

**Inti BENITES**: Porque hoy lo que entiendo, no sé si lo hablaban esto con Nico, pero bueno, nosotros tenemos justamente el proceso de migración está haciendo que de los ETL se vuelvan a tener que reconstruir todo lo que son los scripts o los programas para llevarlos a la capa bronce y de ahí hacerlos a la capa silver. Entonces todo eso hoy es como que se agarra del DB Warehouse, se agarra el programa que está hecho, hay un conversor, me parece que tiene databricks que están usando, que eso acelera, pero aún así el roadmap es largo, es de larga duración para todas las cosas que hay que hacer. Entonces si hay alguna posibilidad de eso, acelerarlo y automatizarlo con Theramo probablemente habría que analizar ese aspecto.

**Bruno Ruyu**: Sí, ahí lo que estoy pensando y creo que sería una forma para ya dejarlo funcional sin tener que estar copiando, es si el objetivo es dejar directamente la capa silver, que Thermo construya eso y después se hace una conexión a databricks para que replique esas tablas. Eso para que quede el pipeline, Si no, como decía antes, agarrar las queries, o sea, hacerlo, llevarse las queries a datar y correrlo de vuelta ahí. Pero bueno, no sé, habría que entender volúmenes de datos para ver cuál de las dos sería más eficiente. La primera versión sería lo más. No sé, capaz la dos son igual.

**Inti BENITES**: Está bien acá, perdón, para. Para entender qué es lo que terminaron hablando con o en qué quedaron. Pero yo tenía la estructura de datos, y de hecho la estrategia de datos actual del banco es la que definimos en mi gestión el año pasado y está en ejecución. Pero todo lo que es el área de datos, inteligencia artificial, se lo asignaron a Jaime a partir de marzo de este año. Entonces es como que hoy yo, si bien doy algún servicio de infraestructura, por ahí sobre algunas cosas, casi que no tengo mucha injerencia, así que no tengo equipo, no tengo datos, no tengo el proyecto, no tengo herramientas, no tengo nada. Por eso me interesa saber cuánto de esto ya adelantaron y hasta qué profundidad llegaron con Jaime y con Nico. Igual después voy a hablar con ellos, pero para entender de parte de ustedes qué es lo que vieron.

**Bruno Ruyu**: Fue más una conversación sobre las posibilidades y quedó, si querés, el lado de ellos, pensar un poco en dónde les podía agregar eso. Foco.

**Inti BENITES**: Pero ellos ya conocen, porque conmigo habías hecho la demo, creo que no sé si había estado Nico en ese momento. Pero ellos ya conocen las capacidades.

**Bruno Ruyu**: Sí.

**Inti BENITES**: OK, está bien. Bueno, bueno, bueno. Me llevo yo entonces sincronizar con ellos dos juntos, separados. Pero más que nada yo, Mica, medio que la otra vez me contactaste vos para ver si manteníamos la reunión. Si no hubiera sido que Hernán Lede me pidió específicamente analicemos este punto. Por ahí te decía que no, porque yo ya no tengo mucho que ver, pero como Hernán me pidió puntualmente esto, me voy a juntar tanto con ellos, con Téramo, como con Jaime y con Nico para analizar esta posibilidad.

**Micaela BACHER**: Dale, dale, buenísimo. Y ahí yo puedo seguir en el medio, pueden hablar ustedes directamente como para ver.

**Inti BENITES**: Y ya que estoy, en qué andan. De la última vez que hablamos hace, no sé, un año más o menos fue. Puede ser poquito más.

**Bruno Ruyu**: Y sí, capaz que sí, porque por ahí cuando se hizo la evaluación

**Micaela BACHER**: y

**Bruno Ruyu**: no sé, un montón de cosas, pasaron un año y ya no sé en qué estábamos. Pero obviamente la plataforma fue cambiando, ganando en un montón de frentes. Y de hecho hicimos de esa época ahora, hicimos un refactor gigante en cómo funcionan muchas de las cosas.

**Inti BENITES**: Te perdí un segundo. La plataforma fue cambiando, me quedé ahí.

**Bruno Ruyu**: Sí, sí, emitimos bastantes refactors, un refactor muy grande en el backend. Diría que ahí cambió muchísimo cómo funciona todo por atrás. Seguimos con cambios también de funcionamiento de los pines, tecnología que vamos mejorando. Esto que te contaba para ir a un. Es como el primer paso, ir a una versión ya multicloud para que en escenarios como este no haya que tomar la decisión de che, replico todo o no, sino que lo puedas levantar en donde vos tenés la.

**Inti BENITES**: Ustedes están en AWS, ¿No?

**Bruno Ruyu**: Hoy estamos todos en AWS.

**Inti BENITES**: Y Bruno,

**Bruno Ruyu**: Lo más importante de todo para mí, que es lo que cambia el juego de febrero, es que al abrirse los conectores MCP Customs, la forma de uso de Theramot cambió, porque ahora el usuario Theramo es Cloud o chatgpt y todo el laburo humano que antes requería pensar las cosas que había que pedirle a Theramot, medio que ahora lo puedes plantear como objetivo para que Claude lo baje a tierra y le pida a Theramo, que Theramo construya todas esas transformaciones y se aumenta muchísimo la velocidad y la precisión y el funcionamiento, logro objetivos y eso es algo de este año.

**Inti BENITES**: Así que eso me resulta interesante.

**Bruno Ruyu**: ¿Y cómo?

**Inti BENITES**: ¿Y cómo sería la interacción con Cloud para indicarle, por ejemplo, que utilice o que trabaje con determinado repositorio de datos y genere, no sé, un data lake o lo que sea que genere?

**Bruno Ruyu**: Claro, el data lake nativamente lo va a hacer teram. ¿Cómo es el funcionamiento? Vos agarrás tus orígenes de información, donde tenés la información que querés de alguna forma meter en el data lake o para lo que vas a hacer un análisis o lo que vas a hacer una migración o lo que sea. Tramo de ingesta, corre los procesos de limpieza de datos, corre los procesos de generación de metadata y genera esa capa silver y después la conexión de MCP. Iteramo le expone un montón de tools a Cloud. Yo uso Cloud, digo el ejemplo. Cloud le expone un montón de tools, dentro de las cuales están analizar y ver qué información tiene la silver.

**Inti BENITES**: Sobre las API de los datos. Ya están enterados.

**Bruno Ruyu**: Claro. Y ahí tenés otras tools que es para crear tablas Go. Entonces vos le decís, quiero estar mirando de ahora que la SAP, por darte un ejemplo, decir che, necesito migrar todo esto a SAP, fíjate que hay en ORAC, fíjate que hay y empecemos a laburar. Y ahí empieza a decir, bueno, vos tenés que llevar a SAP, en SAP HANA necesitas un maestro materiales y empieza a decirle a Ter, o sea, con la inteligencia de Cloud, con todo el contexto de lo que generó Theramon y todo el acceso a los datos, la posibilidad de hacer queries sobre las tablas para ver un muestreo y demás, y toda esa metadata y el knowledge que va generando Claude, puede laburar bien y pedirle cosas para que le genere las tablas para levantar después en SAP como ejemplo, eso también para analítica o para. Para generar dashboards.

**Inti BENITES**: Y el proceso de desarrollo interno que tienen ustedes ¿Lo tienen a su vez agentizado? ¿Están siguiendo algún framework particular?

**Bruno Ruyu**: Mirá, sí, la verdad que nos pusimos muy serios con eso y de hecho desarrollamos un producto interno que nos parecía que había como un gap ahí. Creo que hay algunas herramientas buenas, a mí me gusta bastante Devin, pero decidimos construir uno nuestro.

**Inti BENITES**: ¿Cuál es el que te gusta, Bruno?

**Bruno Ruyu**: Devin.

**Inti BENITES**: Devin con B corta.

**Bruno Ruyu**: B corta, B corta. Ese está bueno. Bajaron bastante precio, era muy caro, pero la verdad que preferimos armar uno nuestro para tener total control. Y de hecho aprendimos varias cosas desarrollando este producto interno que tiene nombre Anchorage, que básicamente estamos tratando de llevar algunas ideas y conceptos de ahí a Theramo mismo, sobre todo por procesos de autohealing y de aprendizaje que nos salieron bien para este producto, para Anchorage, lo estamos tratando de conceptualizar y meterlos entero.

**Inti BENITES**: ¿Implementan SDD o alguna otra cosa?

**Bruno Ruyu**: ¿SD?

**Inti BENITES**: ¿Mataste Spec Driving Development? La verdad que no sé qué nosotros estamos haciendo. Te pregunto porque justo yo estoy haciendo pilotos de eso en BIM. Yo ahora el código mío lo genera ya Cloud, casi todos los programadores, todos tienen Cloud Code. Y estoy haciendo un piloto ahora con un framework que se llama Open Spec, que lo que hago, hago foco en la especificación y voy teniendo distintos tipos de Spec funcional, spec técnica, spec de librerías, lo que sea. Y ese es como va armando mi contexto de desarrollo. Entonces puedo usar Cloud Code o puedo usar cursor, puedo usar cualquiera, digamos, pero el valor, mi activo ya no está más en el código, mi copyright ya no está más en el código, el código pasó a ser como. Nada reciclable si querés, o sea, de un día para el otro puedo sacar otra versión de software totalmente distinta. Pero entonces hoy mi copyright está en los Spec, y sobre todo no en uno solo, sino en la estructura completa de spec y ese es el modelo al cual yo estoy queriendo llevar mi factory, por eso me intriga una empresa como la de ustedes que están en esta también, ¿Hacia dónde ven que están yendo el desarrollo está buenísimo, mirá, yo

**Bruno Ruyu**: ahí capaz que yo tengo una, no estoy tan metido en la nomenclatura y demás, pero básicamente lo que nosotros nos pusimos a hacer, que lo hizo un grupito de ninguno de los que está acá, así que capaz que la próxima o podemos hacer una reunión puntual con ellos para que te cuenten, estaría bueno creo? Pero básicamente donde encontramos, o sea, el procedimiento es, o sea, el objetivo era decir bueno, yo desde Slack tiro que hay un bug y se tiene que arreglar sol, ese es como el norte y lo mismo si queremos meter fichos nuevos, meter una nueva feature, no tiene que ser un proceso por el cual tengamos que hacer todo lo que hacíamos hasta ahora, fuimos con la misma idea, tiene que ser totalmente flexible frente al modelo y de hecho hoy lo están la mayoría de los chicos que lo está usando con Deepseak B, una cosa así, o sea súper barato para no tener que estar pagando Fable igual cuando podemos meterle Fable le metemos on premise, no usamos ¿Cómo se llama? Open Router. Open Router que también sale cinco dólares obviamente si le metes OPU, si le metes feo creo que va mejor, pero bueno, para lograr algunas cosas a mí

**Inti BENITES**: me piden barato y que no sea de China, o sea, bueno, listo,

**Micaela BACHER**: o

**Inti BENITES**: sea, porque viste, quiero que sea barato pero que no sea de chino, bueno

**Bruno Ruyu**: sí, pero Open Router es soc, o sea, eso lo chequeamos y qué sé yo, es un deep que está corriendo ahí en un servidor en Estados Unidos, pero bueno, entiendo igual hay alternativas, tenés un montón y básicamente lo que nosotros entendimos es que sobre todo para un repo enorme como el nuestro, el problema estaba en, o sea, lo que había que de alguna forma lograr era que no se gaste todos los tokens tendiendo el repo frente a cada nueva pregunta, porque por dos cosas, primero te gastas un montón de token y porque es también donde entra los problemas, que no tiene esa visión general. Entonces fue ahí donde hicimos el empuje y los chicos terminaron haciendo algunas cosas con grafos, con estos grafos los modelos entienden mejor y con menos dispersidad y memoria y tokens la estructura y después hacer que haya loops sobre eso, que en la medida que va recorriendo el repo vaya actualizando forma inteligente esos grafos, para que vaya aprendiendo cada vez más, digamos. Y después obviamente una estrategia de capas, donde está uno que planifica, uno que implementa, uno que revisa, uno que testea y demás, y todo que vuelva a retroalimentarse. Así que un poco por ahí va. Y bueno, como decía, estamos llevando algunos de esos conceptos a Theramo para que también tenga esa lógica de auto mejora, que hasta ahora no era tan directo eso cómo hacerlo en un generador de tablas. Pero mirá, nosotros, nuestra visión es que esta herramienta compartirla. Así que si en algún momento quieren hacer una prueba 100 para compartir, o de última contarle cómo le hicimos eso, no es el core de Teramond, así que no nos preocupemos.

**Inti BENITES**: Pero bueno, me interesa porque bueno, creo que es algo que está en plena transformación y que sirve las experiencias reales, sobre todo si van teniendo resultados y se van resolviendo problemas, el problema este de tener que meter tanto contexto uno, bueno, eso hace que tengas que dividir el tema. Por otro lado, necesitas. Estamos viendo también ya esto más en capacitaciones, esto de los rieles de agentes, de tener agentes orquestadores y agentes que son especialistas en determinadas cosas, cosa de justamente no tener que activarle todo el contexto en una interacción con el LM. Y si bien hoy todavía lo estamos viendo a teórico, ver algo hecho en la práctica nos avanza un montón también en ese sentido.

**Bruno Ruyu**: Bueno, ahí de vuelta, cuando quieras hacemos una reunión con los chicos que estuvieron trabajando en este proyecto, para contarte un poco hicieron y cómo está funcionando desde vista. Yo soy más usuario ya esto. La verdad que la experiencia me parece súper buena y de hecho todo este experimento de Cetera Mod liviano que te decía antes, que no necesita, que puede correr medio en cualquier. El objetivo sea que corra en cualquier infra y que no genere todo ese duplique, todo el Lake House, lo están construyendo usando esta herramienta para poder hacerlo con equipo, ¿No? Chicos ínfimos, dos personas.

**Inti BENITES**: Estaba la anécdota de, me la contó Hernán también, que es una empresa que no me acuerdo el nombre, pero que estuvo reunido, él que dice que le pidieron, tienen agentizado todo el desarrollo y con la automatización de que descubra a través de tickets que levantan bugs, o los clientes, o eficiencias propias que encuentre del proceso, que haga las mejoras, las desarrolle totalmente de forma automática y que las deje desplegadas en el ambiente de prueba y con la orden explícita de no pasar a producción. Pero dice la anécdota, no sé si es verdad. Yo te cuento la anécdota, que Bruno de esa empresa se levantó un día y tenía 50 cambios, puesto en producción y lo llamó al equipo y che, ¿Esto quien lo autorizó? No lo había autorizado nadie. Y que la gente que buscaba la eficiencia del proceso dijo que el paso de que lo tenga que aprobar un humano le generaba ineficiencia al producto y por eso lo eliminó.

**Bruno Ruyu**: ¿A ver cómo lo hicieron? No sé, nosotros claramente, el límite nuestro termina en un pull request, o sea, manda ahí y alguien tiene que aprobarlo. Y tenemos una persona o dos que se dedican a eso. Así que no creo nunca ir a nunca. Pero creo que iba a depender más de la configuración de GitHub y de cómo están hechos. Eso de Floyd, a ver si puede. No sé, no sé.

**Inti BENITES**: Lo cuento como anécdota porque bueno, Viene al caso. Bueno, chicos, perdón, no quiero sacar más tiempo. Me llevo yo a hablar con Nico y con Jaime de este tema y así le doy una respuesta a Ernie.

**Bruno Ruyu**: Dale. Ahí a disposición de vuelta para cualquier update o aclaración o ya pensar en hacer algo. Lo bueno que es rápido es hacer las conexiones y empezar a probar. No debería llevar mucho.

**Inti BENITES**: Perfecto, perfecto. Bueno, muchas gracias. Ahí está Cande en la reunión.

**Candelaria Villagra**: Sí, estoy acá, estoy acá. Me sumé, me sumé. Está escuchando cosas que por ahí yo mucho no sé profundizar, pero está escuchando.

**Inti BENITES**: Está bien. Bueno, no sé si vos tenías algo, Can. Perdón, yo ya estaba cerrando.

**Candelaria Villagra**: No, no, yo ya me junté. Es más, yo me llevé cosas del otro día, me juntaba con. Con Franco y no me acuerdo el nombre del otro chico, pero no, nada, me sumé más de oyente.

**Inti BENITES**: Sí, Estaba pensando Can. Bueno, después por ahí vemos si hay alguna posibilidad de agregar valor sumando Téramot al MCP de Apibanco, que estábamos pensando nosotros.

**Micaela BACHER**: OK, OK.

**Candelaria Villagra**: Yo había pensado otras cosas que estuvimos pimponiendo con Franco, pero bueno, está buena también.

**Inti BENITES**: Sí, porque creo que nada puede llegar a ser interesante ya algo más, no tanto conciliatorio. Como lo tenemos pensado nosotros, sino más desde el punto de vista analítica, podría llegar a ser.

**Candelaria Villagra**: Bueno, algo así, algunas cosas vimos, pero llevémoslo a ver cómo haría FIT con eso que estamos viendo del MCP más allá y te cuento cómo yo lo había pensado, que me llevé, que tenía que ver con vos y con Jaime también.

**Inti BENITES**: Bueno chicos, gracias

**Candelaria Villagra**: chicos, nos vemos.
