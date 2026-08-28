# Seguimento Poc BCR

**Fecha:** 2026-06-09T15:29:09.844+00:00  
**Duración:** ~35 min  
**Participantes:** Juan Peralta <juan@teramot.com>, Lucio Rojas <lucio@teramot.com>, Ayelen Romano Bazan <aromano@bcr.com.ar>, Nicole Schmidt <nschmidt@bcr.com.ar>  
**Externos:** aromano@bcr.com.ar, nschmidt@bcr.com.ar  
**Apollo ID:** 6a283986f6363b0014791dda

---

**Lucio Rojas**: That's a signal. Bueno, ¿Qué tal?

**Nicole Schmidt**: Cambiamos,

**Lucio Rojas**: Vinimos a una plataforma como la gente. Déjame decirlo, no estoy a favor de Mitsu. Bueno, pensé que estaba de vacaciones.

**Nicole Schmidt**: Volví anoche bien tarde y bueno, estoy un poco media enferma, me parece. Así que bueno, mi cara no es la mejor.

**Lucio Rojas**: A ver.

**Nicole Schmidt**: No sé cómo estoy en realidad.

**Lucio Rojas**: Estás con cámara apagada. Está igual que siempre. No sé si bueno o malo.

**Nicole Schmidt**: Bueno, no me siento ahí como. Ya los límites, ¿Viste? Ya durante el viaje me sentía mal y bueno, mis amigas me decían no llega, no llega. Y la pasé mal todo el viaje también.

**Lucio Rojas**: Que fueron. Supongo que por Europa.

**Nicole Schmidt**: Sí, sí. Me fui a Italia para cinco días a Sicilia.

**Lucio Rojas**: Bueno, buenas. ¿Qué tal?

**Nicole Schmidt**: ¿Todo bien?

**Lucio Rojas**: Ayelen ayer se sorprendió, se ve que somos vecinos. Y me la crucé a las 7 de la mañana tomando café en la esquina y volvió a las 7 de la noche. Yo seguía tomando café a la esquina en el mismo lugar, pero estuve todo el día tomando café, que justo me senté en dos momentos distintos. Tomé antes y después de ir al trabajo. Así que trabajé 12 horas.

**Ayelen Romano Bazan**: Cuando te vi, como que por un segundo la Matrix se me rompió porque yo, esta persona la vi sentada al mismo lugar hace 12 horas.

**Lucio Rojas**: Sí, es que estaba llegando del trabajo. Dije, no doy más, me voy a dormir, me voy a dormir, me voy a dormir. Dije, bueno, voy a hacer el esfuerzo. Me sentarme, tomé un café y con eso aguanté hasta la noche. Reflexionando, Bueno, perdón, la semana pasada no me pude unir, estaba también realmente muy enfermo, así que estuvo Juan.

**Nicole Schmidt**: Y

**Lucio Rojas**: si quieren contarme un poco resumido qué fue lo que pasó, Yo no entendí muy bien. Entendí que hubo un problema con la conexión a la fuente, pero hasta donde yo sabía, ya había quedado la fuente conectada. Entonces no sé qué tablas faltaron ahí, por eso hice la pregunta por mail. Pero si me quieren aclarar eso descontextualiza.

**Ayelen Romano Bazan**: Sí ahí en realidad la fuente estaba conectada y todas las tablas que nosotros te habíamos pedido estaban conectadas. Lo que en realidad hicimos fue ahí la prueba era de que si nosotros nos queríamos conectar de vuelta y traer otras fuentes, o sea, otras tablas, si podíamos. Y ahí fue donde nos generaba el error al crear una conexión desde cero. Digamos que nunca pudimos crearla, sino la que estaba creada era la que habían creado ustedes que funcionaba bien, pero si nosotros queríamos crear una, no podíamos.

**Lucio Rojas**: Querían testear su autonomía en un mundo.

**Ayelen Romano Bazan**: Claro, exacto. Y más que nada para entender si en realidad había algo que nosotros estábamos haciendo mal, o qué era lo que habían hecho ustedes para poder cargar esas tablas.

**Lucio Rojas**: Nosotros lo hacemos con Facu, lo señaló porque está acá atrás mío. No hacemos nada distinto a lo que han hecho ustedes, que son las mismas credenciales, lo único que por ahí él a veces se da cuenta por sistema que la conexión está caída y manda un mail y se la levanta, pero estaría todo funcionando. Y entiendo que si no pudimos conectarnos fue por un tema de que nosotros conocemos la maña a la UI para que se conecte, porque había algunos temas, después mandó Juan un mail explicándolo, pero eso lo cambiamos todo de la semana pasada. El conector ahora está como más friendly para el usuario. Así que nada, si quieren volver a hacer el test en otro momento me pueden comentar, pero quería ir más para sabiendo que por lo menos ya tenemos las tablas que necesitaban, poder por ahí ya empezar a probar o saber si ustedes pudieron tratar de hacer alguna gol, probarlo con cloth, si hubo algún problema en eso que nos falta.

**Ayelen Romano Bazan**: Sí, ahí tuvimos una reunión la semana pasada con los usuarios y empezaron a hacer las mismas consultas. Replicamos las consultas que habían hecho la otra vez, que nos faltaba información, nos faltaban tablas, cargar tablas, y ahora sí, con la información que tenemos pudimos obtener la información y generar los reportes respondiendo las preguntas que ellos querían.

**Lucio Rojas**: Perdón por no dejar de terminar, ya que te interrumpí, te pregunto. ¿Ustedes lo que hicieron fue primero mapear las preguntas que tenían ellos y armarse las gold con eso como para ya dejárselas?

**Ayelen Romano Bazan**: No, en realidad nosotros no llegamos a armar ninguna gold, sólo están todas las tablas conectadas y ellos empezaron a hacer algunas preguntas puntuales. Y la otra vez lo que nos pasaba es que el sistema no podía responder porque faltaba info y ahora esa información ya estaba, que es información puntualmente de ensayos. Nos pidieron por ejemplo generar un gráfico de dispersión para unos resultados de ensayo. ¿Eso en sí no generaría una tabla gold para mí guardado o que persista? Porque en realidad es una pregunta muy puntual. Nosotros en realidad en la tabla gold qué le tenemos que dar esa información tiene que estar, pero no solamente no tan filtrada para ese ensayo, sino sería una pregunta puntual de un reporte que ellos quieran ver en el momento y que lo generaron y lo generaron bien. El único error ahí, o lo que tenemos que modificar, es que nosotros internamente en esas tablas tenemos muchos códigos, por ejemplo de muestras, de ensayos, digamos, de solicitudes, que son códigos internos como de nuestro área de BI. Claro, Y no son los códigos que usa el laboratorio.

**Lucio Rojas**: Si, ahí te hace una tabla gol sin esos códigos, o sea, copiar la tabla y decir sácame los códigos.

**Ayelen Romano Bazan**: Claro, eso es lo que teníamos que hacer, como quitar todos esos códigos para que después cuando te los muestre no mezcle, digamos, y al usuario le muestre códigos, porque los códigos que ve el laboratorio están, pero el tema es que están esos códigos y también hay códigos que son internos que el laboratorio no entiende, entonces lo que tendríamos que hacer es sacar esos. Para sacarlos sí o sí que hay que crear una gold quitando esos campos

**Lucio Rojas**: y meterte en la conexión y deseleccionar las columnas. ¿Pero la verdad que yo prefiero preguntar

**Nicole Schmidt**: y conectarse a vistas desde the vistas de SQL se puede? Porque todo esto está arreglado y mejorado en las vistas, de hecho los cubos se conectan a esas vistas también los nombres de cada campo con separaciones tipo dice, no sé, nombre del producto, la columna a la vista, se escribió todo bien, se sacaron estos códigos, se puso todo lo que necesita, solamente el cubo. Capaz que desde un principio tendríamos que haber ido a la vista, no avanzamos

**Lucio Rojas**: nunca volver a cambiar, no pasa nada. Entiendo, está bien, inteligente lo que decía, ¿No? Vamos a hacer lo mismo, si ya resolvimos una vez. Y duplicar tablas. Bueno, déjame, dame un segundo que voy a ir a preguntarle al DevOps, capaz que yo digo que sí es porque tengo que mandar un mail diciendo que no, prefiero ahorrármelo. ¿Están bajo la misma conexión que ya nos dieron?

**Nicole Schmidt**: Si, están en esas.

**Ayelen Romano Bazan**: Lo que sí, cuando hacíamos la conexión, o sea ahora para elegir, te aparecían las tablas, las vistas no se veían, pero no sé si hay que seleccionar

**Lucio Rojas**: otra cosa ahí habría que otra pregunta.

**Ayelen Romano Bazan**: Dale. Hola Juan, ¿Cómo estás?

**Juan Peralta**: Buenísimo.

**Lucio Rojas**: Ayer todo bien, todo bien.

**Juan Peralta**: ¿Lucio sabe que están acá?

**Nicole Schmidt**: Sí, sí. Preguntar algo ahí en la misma oficina.

**Lucio Rojas**: Ahí va, ahí va. Sí, sí, no sabía que estaba, pero

**Juan Peralta**: dije capaz que se estaba haciendo algo Ahí volvió.

**Lucio Rojas**: Buenas. Bueno, ahí me fui a machetear con el agente de OPS. Sí podemos ver las vistas no hay problema, lo único que su equipo de infraestructura supongo que nos tiene que crear un usuario que permita ver esas vistas o redireccionar el usuario que ya tenemos o crean uno nuevo que mira las vistas o redirecciones que tenemos ahí depende si ustedes quieren tener las tablas y las vistas, o las tablas o las vistas, eso va a depender si queramos dos fuentes o si nos mantenemos con uno, pero bueno, sería una forma de solucionarlo. Lo único que tengo que tener es usuario nuevo a la base de datos y hacer la conexión de vuelta, como decía Nicole, capaz que es volver para atrás, pero para mí es más ir para adelante porque si no tendríamos que hacerlo de vuelta con las Go, salvo que sea.

**Nicole Schmidt**: Aparte tiene varias cosas arregladas ahí me parece, o sea, bueno, creo que justo lo hablábamos con Aye hace bastante y le digo, capaz que tendríamos que haber ido directo a la vista porque bueno, no solamente esto de la columna que decíamos, sino los nombres y ahora me entraba duda de que habíamos puesto algún que otro filtro que tenía que tenerlo sí o sí la información, o sea que capaz que desde un principio sí o sí había que ir a la vista. Nosotros de los reportes siempre también intentábamos ir a las vistas porque todo esto estaba mejorado en las vistas, cuando llegamos los cubos ya estaban hecho así, nosotros no lo hicimos, ya estaban hechos con las vistas y alguien ya había hecho esas vistas desde antes digamos.

**Lucio Rojas**: Bueno, no sé si ustedes quieren gestionarlo internamente, o sea, van a tener que pedir un usuario a la Teramot que sea de las vistas.

**Ayelen Romano Bazan**: Si, ahí me estoy conectando porque me generaba duda que con el usuario que generamos para Theramont no tenga acceso a las vistas, parecía raro, a ver si te.

**Nicole Schmidt**: No, si, no, sí hay que pedirle que le dé acceso a vistas, puede ser, por default a veces no tiene acceso a las vistas, para mí no

**Lucio Rojas**: las tiene porque nosotros no la vemos cuando seleccionamos las tablas

**Ayelen Romano Bazan**: yo tengo acceso sí entiendo que es el mismo usuario y estoy pudiendo hacer un select a las vistas conectado con ese usuario que es el de Teramond. Si quieren les comparto, no sé si hay que configurar algo más, pero a las vistas llegó desde la base de datos.

**Lucio Rojas**: A las vistas desde la base de datos. Le voy a pedir a Fago que se sume, así también lo vemos.

**Ayelen Romano Bazan**: Si, estoy conectada a desarrollo. A ver, les comparto, Avísenme ahí si están viendo.

**Nicole Schmidt**: Sí, ahí se vaya.

**Ayelen Romano Bazan**: Estoy conectada a desarrollo con este usuario que es el externo que creamos para theramon.

**Nicole Schmidt**: Estaba pensando yo. Si, es el esquema, pues viste que ponemos el esquema en la conexión de theramot,

**Ayelen Romano Bazan**: ponemos DBO, capaz de cambiar eso, pero el usuario ve las vistas, o sea me aparecen y ahí le hice un select a la vista y las veo. Tal vez es cambiar la conexión cómo está hecha.

**Nicole Schmidt**: Claro, porque acá el esquema es OLAP, capaz que sea eso. Bueno, no sé si ahí se suma Facu y.

**Lucio Rojas**: Estaba viendo si el usuario puede ver las vistas. Déjenme que lo chequeo. Quizá en la conexión, en la original que hicimos, no me acuerdo si seleccionamos todas las. Todas las tablas, porque actualmente en la herramienta no discernimos que es una tabla y que una vista consideramos una tabla, entonces por eso se ven todas juntas, una al lado de la otra, y quizás estaba el nombre de las tablas y nosotros no la seleccionamos ahí.

**Nicole Schmidt**: Yo no sé si me escuchaste que eso está bajo otro esquema, ese esquema OLAP, no DBO, y viste que la conexión ponemos DBO, no sé si eso tiene que ver.

**Lucio Rojas**: Entonces hay que cambiar el esquema.

**Nicole Schmidt**: Sí, me parece que apague. Sí, pero bueno, como son vista, no sabíamos si también había que hacer algo

**Lucio Rojas**: más, digamos, no deberíamos tener problema,

**Ayelen Romano Bazan**: O sea tendríamos que crear una conexión nueva. Todo igual, solamente que poniendo el esquema OLAPAR y seleccionan las vistas.

**Lucio Rojas**: Exacto.

**Ayelen Romano Bazan**: OK, a ver si.

**Lucio Rojas**: No sé si estamos viendo acá, si quieren que probemos hacerlo ahora o quieren que lo hagamos nosotros, porque como prefiero

**Ayelen Romano Bazan**: ahí si quieren les comparto y pruebo rápido una vez a ver si me funciona la conexión y si me aparecen las vistas y después nosotros seleccionamos bien todas las tablas para todas las vistas. Digo más que nada para ver si conecta,

**Juan Peralta**: porque acá.

**Lucio Rojas**: Ah, está, ya tienen todo perfecto. No se lo iba a decir.

**Ayelen Romano Bazan**: Esquema OLAP,

**Lucio Rojas**: ¿Cuántas eran las vistas más o menos?

**Ayelen Romano Bazan**: Ahora nos estamos conectando a 31, 32

**Lucio Rojas**: y las vistas que vamos a ir ahora más o menos las mismas.

**Nicole Schmidt**: Hay más, digamos, más vistas en la base de datos.

**Lucio Rojas**: Esto suele tardar en siete tiempos. Sí, sí, porque está yendo una por una a leer el esquema de cada una, se retarda y después pasa otro que también. Casi tienen dudas de conexión. Mientras tanto aprovechémoslo que Facu tiene pocos tokens de como plot. Después ya te. Eso es lo que no tenías que saber, salirte para atrás.

**Ayelen Romano Bazan**: No creo que toqué algo, yo

**Lucio Rojas**: no sé, no vi, pero déjame que me fijo, déjame que me fijo. ¿Qué pasó? ¿Vos tocaste afuera o como que volviste para atrás ayer o

**Ayelen Romano Bazan**: yo me haya dado cuenta? No, pero tal vez toque sin querer, no sé.

**Lucio Rojas**: Creo que sí. No sé si el reintentar funciona.

**Ayelen Romano Bazan**: No, o sea, tengo que crear la vuelta.

**Lucio Rojas**: Sí, ahí ya vamos a ver i que falló y esa borraca. Hay que quedar ahí como esperando que.

**Ayelen Romano Bazan**: Eliminar fuente. OK, yo ahí después tengo una consulta.

**Lucio Rojas**: Voy a avisar que se rompieron los documentos.

**Ayelen Romano Bazan**: No, tengo una consulta que es también más relacionada en realidad al otro proyecto de la DJ que estuvieron haciendo algunas pruebas, pero bueno, a nosotros también nos sirve. Ellos están generando algunos reportes en HTML conectados a las fuentes Gold que crearon en Teramont. Yo acá por ejemplo fui creando algunos dashboard, digamos, conectados a Teramont. Ahí la consulta es inicialmente el código HTML que te crea es con información estática. ¿Bien? Si yo quiero que esa información se actualice con la información que tengo en theramot, lo puedo crear y me conecta a través de la API.

**Lucio Rojas**: Hay como varias formas de solucionarlo. Una es por ejemplo desde cloud code. Me estoy yendo más a lo ninguna. Va a ser muy simple desde acá, más que pedirla todos los días de golpe. Una desde cloud code se puede programar como un prompt corra todos los días a tal hora, entonces vos le podés ir todos los días. Se llama cloud code. Creo que el comando es dispatch barra programar, algo así recién usado cloud co alguna vez.

**Ayelen Romano Bazan**: Yo no lo tengo, pero sí lo hemos visto.

**Lucio Rojas**: Es en realidad el mismo que tienen ustedes, nada más que bajarlo local y hay un comando que es. Loop, se llama comando y lo que hace es correr un prompt en algún intervalo. Entonces puedo decir todos los días quiero que me actualices este mismo dashboard volviendo a hacer la consulta a la tabla. Otra opción es que nosotros generemos o te demos a voz del endpoint de la tabla latina donde está la información y genere algún dashboard o algún código que vea esa tabla y actualice el dashboard. Pero para hacerlo más al estilo Power BI, que se actualice todos los días. Son las dos opciones que hay por ahora desde Clock. Si no, la otra es hacer más a demanda. No sé si se entendió la respuesta.

**Ayelen Romano Bazan**: Sí, porque en realidad ellos lo que están pensando es como generar reportes en HTML que después subirían por ejemplo en una página web o en algo que disponibilizarían al público. Entonces yo ahí entiendo que el código que ellos están haciendo ahora va a ser estático, fijo, y cada vez que lo actualicen tendrían que modificar el código HTML y volverlo a publicar. OK. Y después si no, preguntándole ahí desde Cloud me daba esta otra opción que me generaba conectado con una API de Teramont y me pedía como una API key de Antropic y como que a partir de esto era la forma de hacer que cargue los datos o que actualice. ¿Eso funciona? No,

**Lucio Rojas**: la PIC lo que hace. Vos la creas desde la consola de CL y lo que hace es como ponerle el modelo para que lo corra el código y quizás que con esa apki llame al conector de teleamot y actualice el código HTML todos los días. Pero creo que tenés como una. Una lógica sería lo que describía antes, armar como un backend chiquito, una lógica que actualice el dashboard. ¿Cómo funciona? Se tendría que probarlo más. ¿Algún ejemplo?

**Ayelen Romano Bazan**: OK. Porque a ellos lo que les estaba pasando, a ver si lo tengo, es que generaban el código HTML, lo veían bien como un artefacto digamos, dentro de Cloud, pero después cuando querían renderizar el HTML les aparecían los datos o no veían datos, y cuando fueron a investigar, como que fueron a ver el HTML, el código, y ahí les aparecía esto de que lo buscaba a través de la API de Antropic conectándose con el MCP de Teramont y eso entiendo, era como que los que les da error o no les funcionaba.

**Lucio Rojas**: Ah, y probaron eso, o sea ellos usaron la API y conectaron MCP, se hicieron APT y todo.

**Ayelen Romano Bazan**: Sí, entiendo que sí.

**Lucio Rojas**: No sé si esa es la mejor forma. Lo que sé que funciona mejor para esos casos es que nosotros le pasemos directamente como el endpoint de la tabla de Tina y que ellos hagan un código de backend que lo consulte con

**Ayelen Romano Bazan**: ese,

**Lucio Rojas**: pero la verdad no lo he probado.

**Juan Peralta**: ¿Oye, ese portal de reportería dónde está? Qué usa, o sea, construye, ¿Los construyen a todos así con HTML o ya tienen alguna, no sé, tipo Power BI? ¿Ustedes usan Microsoft?

**Ayelen Romano Bazan**: No, en realidad, para serte sincera, esa página todavía no existe. Es lo que ellos están pensando como solución final. Entonces lo que están probando en realidad, vieron también un vídeo de Bruno que recomendaba hacer los reportes con HTML, entonces están probando eso de decir, bueno, nos conectamos a Teramont con Cloud, generamos los reportes en HTML y después la idea, como eran estéticamente más lindos y les pueden dar otro dinamismo, publicarlos en una futura página web, que al día de hoy no existe, pero la idea era hacer esa prueba. Eso es lo que están haciendo, pensando en el futuro.

**Juan Peralta**: OK, bueno, mirá, a ver, porque una respuesta clara no tenemos. Sí tenemos lo de, como le decía Lucio, que requiere un poco más de trabajo de programación esto de hacerlo con Cloud Code, pero también lo podemos ver, investigar un poco y al menos traer una respuesta más concreta, decir che, te conviene ir por este lado o sacarlo y usar el endpoint ya lo que nosotros tenemos procesado y dejamos en Atina y consúmanlo de ahí directamente, porque de última esa llamada a esa gold que queda en Atina se puede consumir de cualquier forma ahí no hay, termina generando una especie de JSON si vos querés, entonces lo podés consumir programáticamente con la forma que vos quieras. Así que déjame que nos lo llevamos, lo vemos de qué manera es más simple, es más fácil hacer esa utilización del dato y ahí le damos un poco de acompañamiento para la próxima.

**Ayelen Romano Bazan**: Y ahí generalmente, digamos, ahora el resto de los clientes se conectan así desde Cloud, generan los HTML pero estáticos, digamos, sin actualización,

**Lucio Rojas**: ¿No?

**Juan Peralta**: Creo que vamos a decir lo mismo que sí.

**Lucio Rojas**: Sí, o sea, nosotros sabemos que se puede hacer la actualización de un dashboard desde los datos generados en Telamo, todavía no hemos hecho ninguno productivo, entonces sabemos que se puede hacer doble clic, doble clic, doble clic. Contame cómo tengo que todavía testearlo y decirte bien cómo es. Por ahí voy a hacer eso y les respondo más a eso. Hasta ahora se crean los reportes tipo HTML como si fuese

**Juan Peralta**: lo que venimos viendo y que hacen la mayoría de los clientes, una vez que está creada, la golpe directamente se consume sobre esa Gold y programáticamente todos los días dice, che, armame el reporte con estas características sobre la Gold, o bueno, tiene un nombre y la conversación lo va a recordar y lo van generando desde ahí el ecosistema Cloud. Y cuanto más robuste la organización ya tiene un Cloud Team. Entonces bueno, también convive en esa solución y una persona lo puede hacer, lo puede compartir el grupo, etc.

**Ayelen Romano Bazan**: OK, perfecto.

**Lucio Rojas**: Bueno, para resumir, ayer lo que ellos quieren hacer, no entiendo, Entiendo que quieren publicar en la policía todos los días, sé que se puede hacer, no te puedo responder ahora bien cómo es técnicamente que se hace, pero si, ya sé que me hace pregunta el juez, la llevo preparada, me adelante y de paso

**Ayelen Romano Bazan**: te la respondo también el jueves si quieren ahí a ver si puedo les paso la imagen que me pasaron ellos de la parte del HTML, cómo la estaban generando, o sea que la generaba Cloud en realidad, y cómo les mostraba cómo hacía la conexión con Theramo. Pero si, el jueves seguramente va a venir esa pregunta, no sé si acá

**Lucio Rojas**: me deja pasar por correo, si no.

**Ayelen Romano Bazan**: Ah, bueno, dale, se las paso, después le mando un correo.

**Lucio Rojas**: Lo que hicimos con otro cliente fue generarle las ondas de armar los dashboards, y sé que esos dashboards se están actualizando todos los días, pero no lo hicimos nosotros, lo hizo como una empresa que lo desarrolló y no sé bien cómo lo hizo, pero por eso te digo que sé que se puede hacer, pero tengo que preguntarles cómo hicieron. ¿OK, hicieron lo mismo que querían hacer los chicos? ¿Será otra?

**Ayelen Romano Bazan**: Bueno, creo que no tenemos otra consulta, o sea, de nuestro lado sería volver a hacer la conexión con las vistas y ahí, bueno, tendríamos todo el tema solucionado de lo que hablábamos antes, del tema de los nombres, de los códigos que son internos, que no deberíamos visualizar. Y después, bueno, la otra consulta sería con lo que hablamos recién, el tema de la generación de los dashboard a través de HTML y las actualizaciones o futuras publicaciones en alguna página web.

**Lucio Rojas**: Ahí eso ayer no lo piensan para support, no están pensando que el usuario final de ustedes haga eso, es para la otra.

**Ayelen Romano Bazan**: Claro, porque en realidad nuestra información es. Es privada, digamos, es confidencial y no se puede publicar así en una página web al público. En el caso de la otra prueba concepto sí, porque es información pública y la idea de ellos es disponibilizarla al público. Sí, obviamente. Igual esta parte de la actualización nos serviría no para publicarla tal vez en una página, pero sí para poder actualizar reportes internos.

**Lucio Rojas**: Bien. Y eso le llama a ustedes, los usuarios finales, más ustedes, Nicol, supongo, para saber el lado técnico.

**Ayelen Romano Bazan**: Sí, el desarrollo. Sí, pero después, bueno, ellos lo van a querer actualizar, No sé, ahí acá el dashboard que me generaba ya venía como con un botón actualizar y que el usuario entre, lo actualice, algo así.

**Lucio Rojas**: Bueno, después de la conexión, ahí me escribió Fagu, que es un túnel que tiene problemas, no sabe si es del lado nuestro o lado de ustedes, y lo está viendo, que él conecta las vistas y yo les mando un mail cuando estén.

**Nicole Schmidt**: Después.

**Lucio Rojas**: Entonces llegó como yo, todas las reuniones de la tarea, avisarles cuando estén cargadas las vistas y para el jueves les respondo bien lo de los dashboards, cómo se hace y no se puede hacer.

**Ayelen Romano Bazan**: Dale, perfecto.

**Lucio Rojas**: Y todo el mundo. Bueno. Bueno, nos vemos entonces el martes todavía viene, por lo tanto. Y trato de.

**Ayelen Romano Bazan**: Bien. Bueno, muchísimas gracias.

**Nicole Schmidt**: Gracias, nos vemos.
