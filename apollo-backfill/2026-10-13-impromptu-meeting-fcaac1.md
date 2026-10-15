# Impromptu meeting

**Fecha:** 2026-10-13T18:01:47.428+00:00  
**Duracion:** ~44 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Federico Semino <>, Marco <>  
**Externos:** Federico Semino, Marco  
**Apollo ID:** 6ace7c65d5f9b2001cfcaac1

---

**Marco**: Sí, ahí se está sumando.

**Federico Semino**: ¿Cómo anda vos?

**Franco Ferrero**: ¿Todo bien?

**Marco**: ¿Cómo va? ¿Todo bien'?

**Federico Semino**: Bien. Perdón, venía General Paz y no encontraba dónde frenar.

**Marco**: Está bien, Bueno, ahí ya estamos.

**Franco Ferrero**: Bueno, nada, a ver, primero quería saber, bien, me pasó tu número, Gabriel, Fede, no sé qué tanto conocen de Theramot, si conocen algo o. Bueno, si no arranco, arranco de cero y les comento un poco bien lo que hacemos.

**Federico Semino**: Nos comentó un poco Belén, pero muy así por arriba, así que sentite libre de arrancar desde cero, digamos.

**Franco Ferrero**: Perdón, Belén, Belén López Dujubi de LBO,

**Federico Semino**: no sé si la conoces, ella fue la que nos pasó el contacto de Gabriel.

**Franco Ferrero**: Bueno, buenísimo. Bueno, mira, principalmente Theramo es una herramienta que lo que te permite es conectar todas tus fuentes desde base de datos, RM, RPS a un mismo lugar que es Theramot. Lo que hace es, cuenta con distintos agentes internos de Inteligencia Artificial que lo que hacen es, generan todo un Data Warehouse mediante toda una normalización y estandarización de esos datos, que eso lo que quiere decir es que se limpia, se hace una limpieza de los datos para luego poder trabajarlos directamente de cualquier LL, como puede ser Cloud o ChatGPT, y directamente empezar a hacer análisis, reportes, todo lo que tenga que ver con datos mediante cloud, chatGPT.

**Marco**: Franco, te hago una consulta hasta ahí, decime si te entendí mal, o sea, ustedes lo que. Hasta donde entendí, conectorizan con todas las bases de datos y arman el Data Warehouse, enteramon.

**Franco Ferrero**: Claro, o sea, en AWS está hosteado ese Data Warehouse, se genera toda una capa semántica para que vos, nosotros, digamos, somos un intermediario entre tu base de datos y Cloud.

**Marco**: Ahora, te hago una pregunta, esa es una opción, y llegado el caso, porque en ese caso el Data Warehouse les queda a ustedes, digamos que el día que uno corta el servicio, ese Data Warehouse se pierde. Correcto.

**Franco Ferrero**: Se elimina. También nosotros tenemos la opción de hostearlo en una infraestructura suya también, si ustedes prefieren eso, pero si uno, la realidad hoy en día lo hosteamos en AWS en un host nuestro.

**Marco**: OK. Y digamos como opción conectarse a un Data Warehouse de uno.

**Franco Ferrero**: Si, lo podemos conectar, y en ese

**Marco**: caso, digamos, el Data Warehouse es propietario de cada uno y ustedes colaboran en el armado o tienen capacidad de armado de ese Data Warehouse, Por ejemplo, Data Fear de SAP,

**Franco Ferrero**: Déjame averiguarte bien lo de Data FEAR puntualmente, pero tenemos varios conectores con SAP que lo vamos desarrollando. La realidad es que como ya tenemos varios sapiens, te digo, sin saber, imagino que no es un inconveniente conectarnos a otro servicio de SAP, digamos, si tiene API.

**Marco**: Te preguntaba porque digamos, en ese caso la conexión normalmente es del Data Sphere, que sería el Data Warehouse de SAP, hacia el ERP. Y después, digamos, no sé si ustedes de alguna manera se conectorizan, no sé, a través de un MCP o alguna cosa así, contra el Data Warehouse en este caso, que estaría en la nube, pero es propiedad nuestra.

**Franco Ferrero**: Lo que se me ocurre es que ustedes no dan un acceso a la vista como una vista pública y vía API lo conectamos a su data Warehouse directamente y trabajan desde el ERP directamente desde theramon.

**Marco**: OK. Y theramon, digamos, lo que te estaría, no sé si después ustedes por ahí tienen una demo, pero lo que te estaría viabilizando sería que vos de alguna manera a través de Cloud o chat GPT, puedas ir preguntando contra o generando reportes contra ese data warehouse.

**Franco Ferrero**: Claro. Si querés ahora les muestro un poco cómo es la plataforma para así también la visualizan. Nosotros también tenemos la opción de, si quieren hoy en día, hoy les muestro un poco la plataforma y podemos coordinar si quieren una demo más, más puntual. Ustedes nos pueden dar un caso de uso, si querés, algo que hoy en día esté llevando mucho tiempo, que sea más que nada algo que quieran solucionar y podemos hacer ahí, trabajar sobre sus datos. Una demo nos pueden dar unos datos. Dami Si no, si quieren podemos generar nosotros vía cloud, por una cuestión de seguridad, si quieren hacer una demo con su dato, lo podemos hacer, firmamos un NDA que estamos, lo solemos hacer más que nada por un tema de seguridad de datos y para que ustedes también estén tranquilos de que. De que está todo en orden. ¿Quieren que les muestre un poco ahí? Theramo. Este es el espacio acá donde van a estar los distintos espacios de trabajo. Acá, bueno, yo en este caso tengo un montón porque los tengo todos armados, pero este es un workspace que armé para una demo para un cliente. Acá dentro de un espacio de trabajo uno va a poder contar con distintos proyectos, que lo que hacen nuestros clientes normalmente arman distintos proyectos para cada sector. Ya una vez conectadas las tablas o una fuente o una base de datos a un proyecto, ya después puedes armar los distintos proyectos en base a ciertas tablas. ¿Lo que está bueno es que vos acá vas a poder tener distintos tipos de miembros, qué quiere decir? Que vos no le vas a dar todos los roles a toda la gente que vos le quieras compartir, le vas a poder permitir que solo lectura, que haga análisis desde el MCP o que sea un administrador y que pueda ver todas las tablas. Esto sirve más que nada por una cuestión de seguridad, de que si hay muchas veces que no quieren que todos los datos estén compartidos con los distintos usuarios que tiene Teramot, entonces disponibilizan ciertas tablas nomás para dependiendo el rol de cada persona, así pueden ir controlando directamente lo que quieren ustedes, digamos. Entonces bueno, y esta es la plataforma. Acá tenemos la conexión de las fuentes, que lo que pueden ver es que puedes conectar una base de datos o cargar archivos, tanto Excel, CSV o Parquet. Tenemos conexión con un montón, con casi toda la base de datos, en el caso de que no esté acá la que ustedes necesitan, la podemos desarrollar y no nos lleva mucho tiempo. Tenemos a ver, contamos con un montón y la realidad que hoy en día hacer la conexión es bastante fuerte, es bastante sencillo. Acá hace la conexión directamente a a tu fuente. Esto nosotros lo que muchas veces recomendamos es que al conectar directamente la base de datos y la fuente, te permite después poder en esta parte programar una actualización para tus datos. Esto quiere decir que lo puedas laburar siempre al día, o sea que esté siempre con los récords en vivo, cosa de que no tengan que estar constantemente recargando las tablas y la información y que puedan directamente trabajar con los datos actualizados.

**Marco**: Pero, o sea, hasta acá te entiendo, pero quién administra el modelo de datos de atrás de la base de datos, o sea, porque por ejemplo ahí te conectas contra SAP, pero Después adentro hay 570 millones de tablas, hay que después dependiendo de esas tablas hay que, no sé, modelarla o hacer ciertas cuestiones. Eso

**Franco Ferrero**: para modelar qué sentido elegir qué tablas cargan en el sistema, elegir qué

**Marco**: tablas, qué campos, qué relaciones entre esas tablas. Sí, exactamente.

**Franco Ferrero**: A ver, mirá, ahí te cuento un poco también lo que es elegir qué tablas quieren cargar. Eso es decisión de ustedes en base también a qué sector y qué información quieran usar. Si cargan todas las tablas, cargan todas las tablas. Esto es lo que vos decías un poco lo de relaciones entre tablas, eso es lo que generan los agentes internos nuestros. Es decir, los agentes automáticamente al hacer toda la estandarización, normalización de datos y todo ese data warehouse, generan un contexto de conocimiento interno que le va a decir qué hay en cada tabla. ¿Me explico? Acá si vamos a una tabla silver, digamos, te dice, acá podemos ver el esquema que te dice que identifica en cada descripción, tiene cada columna qué quiere decir, y además para cada tabla le va a poner una descripción que estaban cambiando para dependiendo cada tabla. Y cuando vos quieras hacer análisis entre distintos crook que involucren distintas tablas, lo haces directamente desde cloud, desde el MCP. Entonces vos por ejemplo acá quisimos hacer un presupuesto real, es un presupuesto versus el real, entonces cuando lo desarrollamos con Claude, acá directamente hace el cruce de tres tablas, explicó, para hacer el presupuesto versus real y esto, no es que yo le dije che en estas tablas tenés que buscar esto y esto y

**Marco**: esto, estas tablas, o sea como que lo derivó él.

**Franco Ferrero**: Claro, lo deriva solo en base a todo el warehouse que tiene y la información que tiene de esas tablas. Entonces además acá te muestra todo el origen, qué es lo que está pasando, de qué manera lo evalúa, que está bueno tener también traqueado la manera en la que lo desarrolla, porque al final y al cabo es código SQL, entonces acá vas a tener traqueado también qué tipo de análisis está haciendo, qué está tomando en cuenta, que no. Entonces esto te lleva a que puedas verificar también qué es lo que está tomando y no. Para la creación de estos datos además tenemos un sector de conocimiento, que es un poco también lo que vos me preguntabas, que en este sector de conocimiento vos le podés dar regla de negocios que tengan en su compañía, como puede ser distintas cruces, capaz cosas específicas que vos le quieras decir, que eso lo va a tomar siempre, primero va a tomar la regla de negocio, el conocimiento que le diste y después todo lo que está en el data warehouse. Entonces bueno, después una vez que ya se genera esta normalización de los datos, se genera lo que llamamos la tabla silver, que son las mismas 25 tablas que cargamos nosotros las llamamos de forma bronce, pasan a ser de forma silver, ya van a estar limpias y con los datos ya normalizados. Y después tenemos las tablas gold, que son las tablas de resultados que ahí comienzan los nuevos cruces de distintas tablas. Todos estos análisis que hacemos, también estamos agregando distintas funcionalidades, como pueden ser la generación de dashboards. Ahora agregamos toda una parte de Dashboard, porque también lo que nos está pasando es que muchos clientes estaban vinculando Power BI con Theramo, con Tableau, con distintas fuentes, y nos dimos cuenta que hoy en día la realidad es que lo más fácil y lo más sencillo es tener todo unido, todo junto, y además todos estos dashboards se van actualizando a medida que se actualizan los datos de la tabla. ¿Me explico?

**Marco**: OK, OK. Y hay una, digamos, la conectorización con las tablas, porque ejemplo de la base de datos, después cuando lo suben a su Data Warehouse, hay una replicación, o sea, no es que estás consumiendo en tiempo real, o sea, no estás tirando una consulta al sistema, por ejemplo a SAP, no, estás extrayendo los datos tipo un ETL y lo está llevando al, ¿Cómo es que se llama? Al Data Warehouse.

**Franco Ferrero**: Claro, exactamente. Ahí igual también si entiendo que entendés bastante de todo lo que es tecnicismo, si querés también podemos armar una demo y sumar a uno de los chicos del sistema para explicar bien todo lo que es el tema de conexión y de seguridad de datos, que muchas veces prefieren, viste, por una cuestión lógica que con gente que sabe más de lo que pasa de trasfondo.

**Marco**: OK.

**Franco Ferrero**: Y bueno, acá directamente a ver la realidad que Telamot cuenta con un agente interno que tiene los distintos modelos de inteligencia artificial. Nosotros recomendamos, y también en lo que hacemos internamente, lo trabajamos directamente desde Cloud, que lo trabajamos mediante un MCP, la conexión del MCP es bastante sencilla y la realidad es que una vez que ya tenés conectado el MCP, lo empezás a laburar desde Cloud y las funcionalidades que tienen son muchas.

**Marco**: OK.

**Franco Ferrero**: Si querés les voy a mostrar desde Cloud.

**Federico Semino**: Yo a diferencia, Juanjo, técnicamente soy lo opuesto, pero te hago una consulta, por ejemplo, si vos lo tenés conectado a Cloud, ¿Cómo funciona el tema de las licencias, o sea, ¿Tenés que tener una licencia por cada usuario para poder,

**Marco**: no

**Federico Semino**: sé, armar un Dashboard? Ejemplo, no sé, yo estoy en finanzas, Lucía, está en costo el que está en ventas, al momento de crear un Dashboard o de yo querer consultar, yo tengo que tener mi propio usuario de Cloud para poder realizar un dashboard. ¿Se entiende lo que quiero preguntar?

**Franco Ferrero**: Nosotros también por eso ofrecemos la conexión a casi todos los LLMs, porque la verdad que nosotros no ofrecemos el servicio de Cloud ni de chat GPT, sino que eso va cada uno por la empresa. Las distintas empresas usan distintos LLM, entonces dependiendo el manejo que tengan, van a tener sus distintas licencias. Muchas veces lo que hacen es comparten un par de cuentas de Cloud, que las vinculan a la cuenta de Theramo y directamente trabajan desde el MCP Cloud. Bueno, acá un poco para mostrarles el conector es así, acá lo vamos a poder ver en la parte de conectores, tenemos acá Dyramo, estas son los distintos permisos que tiene Cloud dentro de las herramientas que cuenta el MCP, son varias, no las vamos a ver detalladamente, pero la conexión es sencilla y una vez que estás acá en Cloud, vos venís y le decís conectate al MCP de Theramo y ahí ya empieza, ya genera la conexión y empieza a trabajar directamente desde Teramot. Vamos al huésped de demo. Entonces acá una vez que ya Cloud mediante el MCP ya está dentro del proyecto que nosotros queremos, dentro de nuestro proyecto, tenemos un montón de. De oportunidades de cosas que podemos hacer. Yo voy a arrancar por una básica, le voy a decir en base a los datos que tenemos, Qué tipo de análisis me recomendás hacer. Entonces esto le estoy mostrando un poco más o menos cómo funciona, por eso lo que le digo de hacer una demo capaz donde puedan ver el valor real con su dato, va a ser mucho mejor, porque vos me vas a poder decir, che, quiero ver qué cliente me debe a 90 días tanta cantidad de plata, o generarme una alerta cuando la morosidad sea mayor a X número. Como que van distintas reglas de negocio que las puedes ir armando en base a lo que vos quieras. Igual acá un poco a ver, son las distintas ideas, como que ya viene acá el ida y vuelta y el ping pong con Claude, de las distintas cosas que puedes ir armando en base a los datos que tiene la plataforma. No sé si hay alguno que le llame la atención a un análisis que le gustaría, o sea, son datos Dumi, pero bueno, como que genera análisis a raíz de los datos que tiene. Ya hoy en día tenemos clientes que directamente toda la parte de presupuestos y cosas financieras la están desarrollando con TheAmot. Y bueno, ahora estamos haciendo distintas evaluaciones, comparando una auditoría de cuentas a cobrar sobre ciertas horas estimadas de humano versus TENAM, digamos,

**Marco**: no puede ser cualquiera como para entrar a seguir explorando. Pero rentabilidad por cliente o corredor.

**Franco Ferrero**: Dale.

**Marco**: Pero además para saber la rentabilidad tenés que subir la base de costo.

**Marco**: Sí, lo que pasa es como que le da acceso a todo.

**Franco Ferrero**: ¿Perdón, como qué preguntaron?

**Marco**: No, no, o sea, a ver, una vez que estás conectado acá, los datos, el resto, digamos, es como que te lo entiendo porque es lo mismo que si le subís un excel con 10 planillas, 10 hojas adentro con distintas cosas y le decís che, haceme un análisis y te empieza a decir bueno, te puedo analizar esto, te cruzo aquello, Mientras los datos estén y tengan coherencia, nada, empieza a hacer 200 millones de análisis. Esa parte la tengo clara. Lo que supongo, pero bueno, no sé, ya después más técnico es que una vez que vos lo conectas a todo, en un caso como fuese SAP, a todo tu sistema, bueno, ahí no sé, digamos, la capacidad que tiene de interpretar, analizar o hacer los cruces con las tablas en función de cómo está almacenada la información, digamos, porque ahí está la información toda en crudo. Bueno, supongo que obviamente como lo está mostrando lo hace. Creo que ahí es la parte más.

**Franco Ferrero**: Por eso también un poco a ver esto, mostrarles una demo con estos datos. Dami Hoy más que nada para mostrar un poco el funcionamiento. Entiendo que yo que el valor real lo ves cuando lo ves trabajar sobre tus datos y sobre todo en una base de datos como SAP que tiene cada nombre de tabla con VSIC, VSAC.

**Marco**: Claro, sí, sí, con un montón de cosas.

**Franco Ferrero**: Es bastante quilombado. De hecho, a ver, estamos trabajando ya con clientes con conexiones de SAP, por lo que también por eso estamos. Podemos decir que ya con SAP lo estamos trabajando bien y que los agentes internos identifican bien qué hay en cada columna, en cada tabla y en base a eso generan todo un data warehouse para que lo puedas trabajar desde SAP.

**Marco**: Claro, sí, sí, sí, sí. Y digamos, ¿Ustedes tienen algún esquema de demo en donde dándole una conexión al sistema, nada, puedan extraer cierta información y después ver qué pasa?

**Franco Ferrero**: Sí, a ver, si quieren lo que podemos hacer, a ver, si vos decís, en vez de hacer la conexión entera, podemos, si querés, podemos cargar un par de tablas, lo que ustedes crean también que sea necesario para hacer una demo, podemos conectar la fuente o directamente que damp un par de esas tablas como CSV y las cargamos en un.

**Marco**: Tal cual.

**Franco Ferrero**: Acá también un poco para mostrarles es que acá a medida que van viendo,

**Marco**: perdón que nos arrimamos la cara, no es que la letra está chiquita, no,

**Franco Ferrero**: no se ve nada.

**Marco**: Para que digan qué pintones cómo están estos chicos.

**Franco Ferrero**: No, no, pero más que nada para mostrarle, viste, como que también está todo traqueado de la veces de lo que busca, de la manera está haciendo los cruces de la tabla y todo esto lo bueno es que lo podés ir, lo vas como fortaleciendo y entrenando para que entienda también qué es lo que uno quiere. Por ejemplo acá detecta que nos faltan datos, entonces esto está bueno porque siempre que falte algo o hay un análisis que no pueda hacer, te lo va a ir cantando y te va a ir diciendo también che me confundí, estos datos no los tengo, me falta esta tabla, entonces bueno, ahí me decís, che Franco, tenemos que cargar la tabla, Besic que nos olvidamos.

**Marco**: Sí, sí, sí, que nos olvidamos.

**Franco Ferrero**: A ver, generó estos supuestos en base a los distintos márgenes y bueno acá también te empieza a hacer como vos decís, como cuando le cargas el excel, te empieza a hacer distintos análisis y posibles mejoras para. Para lo que es el negocio, digamos.

**Marco**: ¿Un número estático hay posibilidad que sea dinámico?

**Marco**: No, no pregunta, no, todo dinámico, o sea, entiendo que es todo dinámico si vos después le decís no, a ver, en vez de abrirme el margen o qué sé yo, dentro de minerales o lo que sea, si va teniendo la información lo va armando.

**Franco Ferrero**: Si no, a ver, de hecho lo que les comentaba un poco es acá cuando se generan, estas son las tablas de resultados, que nosotros las llamamos tablas gold, cuando se generan estas tablas que se generan en base a cruces de distintas tablas, cuando la tabla fuente, que serían estas tres, se actualizan con la actualización programada de la fuente, ya vuelva a generar la misma tabla, o sea lo que sería el mismo dashboard o la misma tabla de resultados con los nuevos números ya actualizados.

**Marco**: Si vos decís respecto a la actualización en tiempo real, sería lo más cercano al tiempo real. La pregunta iba más que nada si por ejemplo tenías ahí un rubro o un determinado concepto, si vos podés ir abriéndolo y haciendo consultas sobre ese concepto, sobre ese porcentaje de margen que había.

**Franco Ferrero**: Bueno, a ver, es la idea mucho. Lo que pasa acá que bueno, por ser datos DU también es como que no es tan, o sea no es real, pero vos acá le podría decir, desglosame lo que hay en minerales.

**Marco**: Ahora una pregunta mientras vas así consultando, suponete que llegas, le decís bueno a esto, armame una tabla, o sea un gráfico, lo que sea, y vos decís, después te interesó como para quedártelo y que a lo largo del tiempo ir mirándolo eso de alguna forma, no sé, lo guardas.

**Franco Ferrero**: De hecho, a ver, acá en Téramot ya quedan guardados y se van, y se van actualizando. Vos esto también lo podés compartir, lo podés enviar como un link y directamente lo abrís con HTML y se les muestra el dashboard. Vos elegís también a quién le vas a querer compartir esos dashboard, pero son dashboard que ya quedan y los podés ir mirando, son código HTML y son muy buenos de desarrollar porque es sencillo la manera en la que se comparten

**Marco**: y desarrolla, pero te quedan dentro del, digamos, no sé cómo explicarte. Suponete que volvés, no sé, dos días después y esa tabla que apareció ahí, vos decís, ¿Querés que te grabe para que te la vaya actualizando en otro

**Marco**: momento para hacer un comparativo, para acumular

**Marco**: esa tabla después te queda como un reporte en algún lado que directamente actualizame esta tabla y la trae?

**Franco Ferrero**: Sí, sí, a ver, de hecho vos lo que podés hacer así un poco también para lo que es análisis comparativos, como les muestro acá pone, acá tenemos, bueno justo es un filtro de clientes, pero nosotros le podemos poner, hacemos un filtro que me va guardando la tabla por cada semana o por cada mes, así yo después las voy comparando en una tabla grande. ¿Me explico? Todas estas tablas las puedes ir guardando como distintas tablas.

**Marco**: Sí, sí, sí. ¿OK, pero y después cómo vuelvo a esta tabla por ejemplo, como la vuelvo a traer? Que fuera de lo que fue esta conversación,

**Franco Ferrero**: Fuera de esta conversación, digamos, no está guardado, está guardado entera MOT.

**Marco**: No, no, no, está bien, pero suponete esto acá ingreso por toneladas por kilómetro, me dio 0.79. Esto está puesto, no sé, a hoy, yo la semana que viene entro y quiero ver esto mismo pero con los datos de lo que se actualizó. ¿Entonces a dónde entro para decir che, a ver cómo está esta tabla hoy o sea, este reportecito que armó ahí,

**Federico Semino**: vos tenés la conversación en Claude, tenés la conversación y vas pidiendo información, llegamos a esta tabla, esto te queda replicado en un reporte dentro de Terama o

**Marco**: se graba una nueva tabla, digamos, con ya la información?

**Franco Ferrero**: Esta tabla se guarda como una tabla de resultados nueva que lo que hace que es.

**Marco**: ¿Claro, pero y de dónde la consulto?

**Franco Ferrero**: Queda guardada la tabla como tabla de resultados, que es lo que les mostraba antes. ¿Como son estos tres cruces, estas tres tablas? Esas tres tablas se generan mediante este código SQL. Cuando los datos de la fuente se actualizan, la tabla vuelve a correr este código SQL, entonces actualiza la tabla con los datos nuevos que vos tenés.

**Marco**: Correcto, está bien, la foto vieja pasa a estar de vuelta actualizada, pero a ver, volvé un segundito para, o sea,

**Franco Ferrero**: pero puedes pedir igual que te guarde la foto vieja también.

**Marco**: Sí, sí, sí, sí, tal cual.

**Franco Ferrero**: De hecho, a ver, creo que eso lo más sencillo porque si yo realizo el análisis para la semana que viene, le voy a decir, bueno, quiero hacer, o sea, actualizame esta tabla o directamente le digo, haceme la tabla actualizada hasta la semana pasada.

**Marco**: Sí, sí, sí, cambiarán la fecha. No, no, tal cual. Si, no, yo lo que decía era como si te quedase un menú de, no sé, el reporte de ingresos por venta, rentabilidad por cliente, zona, qué sé yo, no sé.

**Franco Ferrero**: Entonces eso lo podés hacer porque esta parte de dashboard te da toda una, toda una sección de filtros, digamos, que vos decís, vos acá podés poner ventas, podés elegir el mes y en base a eso vas evaluando los distintos movimientos.

**Marco**: Claro, pero vos para llegar a este dashboard, lo que arrancaste, o sea, vos le pediste en una charla, armame un dashboard que tenga, o propone un dashboard que tenga tal y tal cosa.

**Franco Ferrero**: Claro, lo genera mediante la tabla, mediante la tabla Gol, digamos.

**Marco**: Sí, sí, sí, sí, sí, sí, tal cual, tal cual.

**Franco Ferrero**: Lo que, lo que esté, también por eso le digo, si quieren ver el valor real, capaz con sus datos y ustedes entendiendo que hay detrás de esos datos le van a ver un potencial más fuerte y nada, también como les decía antes, que podemos firmar un NDA y ver los pasos a seguir, así también ustedes ven y prueban la plataforma.

**Marco**: No, no, yo lo que quería tratar de entender era cómo operaba, pero sí es lo que me imaginaba, digamos, cómo era, no sé. Después lo único que me queda así como una pregunta técnica, o un poquito más técnica, es digamos que le referencias desde afuera como para conectarse, porque es como que justamente si hay un data warehouse, por lo que estaba viendo, SAP tiene como ya modelos de ciertas tablas con ciertas cruces y demás cuestiones para, por ejemplo, no sé, resolver temas tocó ahora, si uno se evade de eso y conecta directamente las tablas propiamente dichas, o le tiras a muchas tablas, o tendrías que tener un diccionario de datos, algo que te permita decir, bueno, para por ejemplo sacar stock, te voy a inventar, ponerme de acuerdo, no sé, tenés que usar la mara con la, como decimos, con la B y la tal otra. Pero bueno, alguien te tiene que decir qué tablas conectorizar, digamos, ¿No? Para.

**Franco Ferrero**: Sí, sí, al 100%, pero también un poco también la idea de nuestros agentes es que hacen esa, todo ese entendimiento de las tablas, por más de que sea SAP sea complicado, tengan nombres distintos, todas las tablas lo que hace muchas veces identifica muy eficazmente todos los patrones, todo. Y también en el caso de detectar de que dice, che, para hacer este análisis me está faltando un número, y ahí te va a decir, che, muy probablemente esté en esta tabla que falta, que puede llegar a ser B, como decíamos, de lejos normal, y te dice, normalmente el SAP se llama tal nombre de esta tabla. Y ahí bueno, haces la prueba de si es realmente esa.

**Marco**: Claro, está bien. ¿Y una pregunta, el MCP, digamos, es lo que es lo que han desarrollado ustedes, digamos, desde Teramont o no necesariamente? Claro, o sea el conector, digamos, desde Teram, porque suponete que te invento, vos conectas Cloud con un conector, digamos, a una base de datos, ¿Dónde estaría, no sé cómo preguntarlo, como el adicional de Teramont sobre esa conexión directa, por decirlo de alguna manera?

**Franco Ferrero**: El valor está en toda la normalización y estandarización de los datos, que mediante toda esa capa semántica, Cloud puede trabajar sobre tus datos. Esto es un tema un poco más ya del LL, más profundo, que de hecho Claude mismo sacó un paper ahora hace poco hablando de la ineficiencia para trabajar con datos. Si quieren, si les interesa, después se los paso. Es un paper que a nosotros internamente nos sirvió mucho porque resolvemos algo que justamente Claude dijo que los LLMs no estaban todavía preparados para desarrollar y que le faltaba toda una capa de estandarización de datos que justamente lo que genera Teramot que te permite después trabajarlo eficientemente desde Cloud.

**Marco**: OK, bueno, estamos, la verdad que está muy bueno, no sé, después tendríamos que charlar internamente a ver un poco como uno podría ser, qué sé yo, o ver para probar o pasos a seguir.

**Federico Semino**: Estaría bueno ver la forma de hacer alguna demo con datos propios para verlo más real. Carla No sé, desconozco como Juanjo, pero la forma de extraer algunas tablas por el estilo,

**Marco**: se pueden extraer las tablas fijas o si no ver si se hace una conexión y de alguna manera ellos toman parcialmente ciertos datos como para hacer una prueba. Bueno, ahí después lo podríamos charlar o salvo que de alguna forma, no sé, ustedes nos dijesen bueno mira apuntá bajar esta, esta y esta tabla, aunque sea como decía vos, dampiar alguna de esas tablas parcialmente por decir de las tres tablas cinco meses, como para decir bueno algo que tenga alguna coherencia y los pasa como CSV o la forma que sea.

**Franco Ferrero**: Yo creo que a ver, capaz a priori eso, hacerlo más, lo más sencillo y lo más rápido sería dampiar un par de tablas y las subimos como CSV y después en el caso de que les guste la plataforma debemos de trabajar sobre la conexión, pero capaz más que nada identificar ciertas tablas, un caso de uso que usted le gustaría dar y en base a eso generamos una demo.

**Marco**: ¿OK,

**Federico Semino**: cómo te parece? ¿En caso de que avancemos por este camino, nos pones vos en contacto con la gente de sistema y junto con nuestra gente de sistema para que lo prepare, cuál sería la forma ordenada de avanzar para hacer estas pruebas?

**Franco Ferrero**: A ver, de eso lo manejamos, lo manejo yo con Lucio que es un compañero mío. Esto a ver, el tema de la conexión de la fuente, si más iría con la gente de sistemas. En caso de ser un dump de ciertas tablas, ustedes me las mandas por mail, coordinamos y las cargamos. Si quieren firmar un NDA hablamos y eso, coordinamos con con Bruno, con el firmante de nuestro NDA, así también nos ponemos en contacto si ustedes requieren de eso y podemos avanzar.

**Marco**: ¿Bueno, te hago una pregunta después, comercialmente cómo es el esquema de licenciamiento y todo eso? ¿Como licencia en el producto?

**Franco Ferrero**: Nosotros tenemos distintos planes, que los planes van en base a usuarios, cantidad de GB de procesamiento y distintas funcionalidades de la plataforma. El plan starter es de mil dólares que cuenta con 10 usuarios, 150 gigas de procesamiento y si no me confundo más de almacenamiento que de procesamiento. Y ahí cuenta también con 5 dashboards para lo que es los usuarios. Y después tenemos otro plan que es de 2000 dólares que cuenta con 25 usuarios ya y dashboards ilimitados. Y también la posibilidad de usar el agente interno de la plataforma.

**Marco**: Qué sería el agente interno, perdón,

**Franco Ferrero**: los modelos de IA que tiene incluido Tenamot en la plataforma, digamos, en caso ningún elemento, hay gente que usa el agente interno.

**Marco**: OK, OK. Bueno, nada, como decía Fede, vemos como organizamos y bueno, vamos dándolo así avanzando a ver cómo para seguir explorando lo.

**Franco Ferrero**: Dale, buenísimo. Yo estoy en contacto Federico, tengo tu número, así que estamos en contacto.

**Federico Semino**: Dale, yo después cualquier cosa te paso el mail también de Juanjo, bueno que en verdad quedó creo, no sé si te lo compartí a vos, se lo compartí directo a él a la invitación esta, pero si, después te mando el mail y así ya quedamos en contacto todos,

**Marco**: me parece que está en la agenda. Si, no, igualmente vos tenés el mail de Fede.

**Franco Ferrero**: Sí, tengo el mail y el número

**Marco**: de Fede, bueno, son nombre apellido, así que el mío es igual, pero JuanJosé Semino y después de ahí te pasamos el de Lucía también. Bueno, Lucía Werset, más difícil de escribir,

**Franco Ferrero**: pero bueno, después te lo pasamos, estamos en contacto. Muchas gracias.

**Marco**: No, bueno, muchas gracias a vos Franco, Gracias. Chau. Chau.

**Federico Semino**: Ahí quedó igualmente el Theramon Recorder grabando, tienen que para charlar dos minutos, si querés corto y armó uno nuevo.
