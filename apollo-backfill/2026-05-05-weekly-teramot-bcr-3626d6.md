# Weekly Teramot - BCR

**Fecha:** 2026-05-05T14:59:17.499+00:00  
**Duración:** ~61 min  
**Participantes:** read.ai meeting notes <>, Romano Bazán, Ayelen <>, Tomi teramot <>, Lucio Rojas <lucio@teramot.com>, Schmidt, Nicole <nschmidt@bcr.com.ar>  
**Externos:** nschmidt@bcr.com.ar  
**Apollo ID:** 69fa142c833fbc001d3626d6

---

**Schmidt, Nicole**: Buenas.

**Romano Bazán, Ayelen**: Hola, buenas tardes, ¿Cómo va?

**Schmidt, Nicole**: Perdón, estábamos en otra reunión y bueno, unos minutín tarde.

**Lucio Rojas**: ¿Nos escuchan bien?

**Schmidt, Nicole**: Sí, medio por ahí medio lejos, pero creo que vamos a ver. Lejos o me parece mejor. Si, no sé si por ahí steams de que tardar el sonido al principio.

**Lucio Rojas**: Bueno, ¿Esperamos a alguien más de su lado?

**Romano Bazán, Ayelen**: No, nosotros estamos.

**Schmidt, Nicole**: Creo que no.

**Lucio Rojas**: Vi que cargaron unas tablas, ¿Puede ser?

**Romano Bazán, Ayelen**: Yo estuve haciendo unas pruebas, pero cargué desde archivos Excel antes de tener el túnel, digamos. Con lo del túnel quise hacer la conexión pero me genera un error, por eso quería revisarlo con ustedes, porque no sé si hay algo que estoy haciendo mal o hay algo que no me está funcionando. Sí, acá

**Lucio Rojas**: reconociendo las voces. Bueno,

**Romano Bazán, Ayelen**: no sé si quieren que les comparta, No sé si ahí están viendo. Yo fui a agregar fuentes de datos SQL Server, puse el host que nos pasaron ustedes, el puerto, el nombre de la base de datos, el esquema, puse usuario y contraseña. Y me generaba este error.

**Lucio Rojas**: Ya traemos al que sabe.

**Romano Bazán, Ayelen**: Sí, ahí hablando con Tomás de nuestro lado, él lo que me decía es para mí, o sea, a mí me parece raro, pero lo que me decía es que la conexión en realidad yo la tengo que hacer desde el servidor, ellos como que el túnel conecta Teramont con nuestro servidor donde está la base de datos, pero yo esto lo estoy haciendo desde mi compu local, digamos, no debería entrar al servidor y hacer la conexión desde ahí,

**Lucio Rojas**: Porque está desde la web app y eso está tirando quizás ese mismo proceso, los chicos saben, pero

**Schmidt, Nicole**: podemos entrar al remoto y ejecutarlo. Tiene un navegador, o sea, sería entrar al remoto y abrir el navegador y entrar a hacer esta conexión.

**Romano Bazán, Ayelen**: Sí, yo probé, o sea, desde el remoto, viste que tenemos Internet Explorer del año, sería conectarnos desde ahí, pero por eso yo quería consultarlo ustedes, porque me parece raro que tengamos que hacerlo desde el servidor, o sea, nos limita a que tengamos que tener acceso y no sólo un usuario de base de datos, porque ahora nosotros sería con un usuario solo lectura a la base de datos, pero con un usuario de acceso al servidor.

**Schmidt, Nicole**: Pero funciona desde el servidor.

**Romano Bazán, Ayelen**: Claro, lo que a mí me parece raro es que cada usuario, por ejemplo, no sé, se lo damos a Brian, Brian va a tener que crear, tendría, si él quiere crear una conexión, la tendría que crear entrando al servidor.

**Schmidt, Nicole**: Sí, sí, obvio, obvio. ¿No, pero pensé que no, o sea, si funciona desde el servidor, entonces? Sí, es el problema de que desde afuera no entramos, digamos. Pero si funciona desde ahí. Pensé que no habíamos probado desde el servidor.

**Romano Bazán, Ayelen**: No, desde el servidor no. A ver,

**Lucio Rojas**: Ahí se está.

**Lucio Rojas**: Ahí se está sumando nuestro.

**Lucio Rojas**: Tomás.

**Lucio Rojas**: Esa conexión que hizo. Ay, es. Y la. Si, la base tarea pública, por eso va a ir a buscar como Internet desde la página. Por eso el túnel lo que hace específicamente es conectar nuestro origen de datos contra el origen creado. Ahí está Tommy. Tommy,

**Schmidt, Nicole**: buenas,

**Lucio Rojas**: acá estamos. Bueno,

**Lucio Rojas**: repasemos.

**Lucio Rojas**: El túnel quedó activo. Bien, genial pues aparte 10 puntos. Ahora, después de eso lo que hizo Ayelén es entrar a la web, completar el formulario como lo ves ahí, le da a conectar y le da error. El punto es, ¿Este paso lo hacemos ahí desde la web app o se tiene que generar algo en el entorno donde está alojado el servidor? No, no, esto tiene que ser todo desde la web. ¿Tendrías capaz un problema nuestro o falta buena configuración de nuestro lado? A ver un segundo que veo los logs. ¿La condición es SQL Server o no?

**Romano Bazán, Ayelen**: Sí, sí, la conexión SQL Server,

**Lucio Rojas**: ¿Qué más debo? ¿Podría estrear de nuevo la conexión?

**Romano Bazán, Ayelen**: ¿La creo vuelta? Sí, sí puedes por favor de cero o agrego directamente.

**Lucio Rojas**: Pone siguiente ahí. Gracias. ¿Puede ser que tengan una tabla sin datos?

**Romano Bazán, Ayelen**: Preguntó, ¿Alguna tabla sin datos? No, yo acá igual no puse el nombre de la tabla todavía, yo solamente puse la base de datos. ¿Tengo que aclarar la tabla?

**Lucio Rojas**: No, no hace falta.

**Lucio Rojas**: Dentro de la base de datos puede ser que tengo un error, que hay

**Lucio Rojas**: una tabla que se llama.

**Lucio Rojas**: Cómo es un error nuestro, Ahora lo resolvemos que andamos con problemas para SQL

**Lucio Rojas**: Server,

**Lucio Rojas**: pero la conexión y todo lo otro está perfecto. Falta este último paso nomás.

**Lucio Rojas**: Bueno, todo bien entonces ustedes no ven a eso. ¿Y después se puede hacer la conexión?

**Lucio Rojas**: Sí, sí, ya para hoy lo sacamos seguramente.

**Lucio Rojas**: Bien. Bueno, entonces hasta genial la conexión. Vamos a tener que esperar a Tommy. Por el otro lado, los otros pasos que teníamos pendientes, el diagrama de arquitectura

**Lucio Rojas**: para usar

**Lucio Rojas**: el MCP ya lo tenemos, lo hizo el equipo de DevOps. No sé si quieren que se los comparta ahora o directamente los comparto por mail para que.

**Romano Bazán, Ayelen**: Si querés pasarnos ahí. Es más que nada porque yo estuve hablando con Aníbal que es, viste, del área de seguridad y redes, y lo que quería era revisarlo primero y después si tiene alguna duda y demás, seguramente les pida alguna reunión como para verlo con ustedes, pero bueno, la idea era primero revisarlo él internamente y ver si está de acuerdo o si tiene alguna duda o algo que quiera que les aclaren, digamos. Pero bueno, la cuenta Cloud ya la tenemos, así que para lo que es la prueba de concepto la tenemos disponible, digamos, para probarla.

**Lucio Rojas**: Buenísimo. Mientras tanto, ustedes ya pueden hacer alguna prueba sobre las tablets que ya cargaron con MCP o esperamos a Aníbal que dé OK.

**Romano Bazán, Ayelen**: Podríamos.

**Lucio Rojas**: Ellos están en España, está más lejos.

**Schmidt, Nicole**: Yo salgo corriendo.

**Lucio Rojas**: Entiendo, entiendo, entiendo.

**Schmidt, Nicole**: ¿Igual las tablas que vos cargaste son de Excel? No son confidenciales.

**Romano Bazán, Ayelen**: Son tablas de localidades las que cargué yo ahora, no es información confidencial. Sí, esperaría tener el OK de Aníbal para después conectarnos cuando carguemos las otras tablas de solicitudes y demás. Pero esas tablas que cargamos ahora era para hacer una prueba nada más.

**Lucio Rojas**: ¿Quién que probemos ingresa en esta hora que tenemos?

**Lucio Rojas**: Así ya.

**Schmidt, Nicole**: Sí, por mí.

**Lucio Rojas**: Bueno, sí, Tom, vos ya está. Si tenés la necesidad de laburar, listo. Quédate tranquilo. Final de puntos, solucionamos un poco en vivo.

**Lucio Rojas**: Bueno, ya tienen Cloud, la licencia en la compu ya instalada. Ya está, Pau.

**Romano Bazán, Ayelen**: Lo que sí, bueno, tenemos en realidad es una sola cuenta que es compartida, y es la cuenta que está usando toda el área de tecnología. Así que. A ver, ahí ingreso.

**Lucio Rojas**: ¿Tienen tokens libres?

**Schmidt, Nicole**: La básica.

**Lucio Rojas**: La básica.

**Lucio Rojas**: Bueno, ahí estoy pensando. El MCP va a quedar. Si está sobre la cuenta, va a estar habilitado. Sí.

**Lucio Rojas**: Lo puedo usar Cualquier.

**Lucio Rojas**: A ver, no es que cualquiera que pregunte, pero sí,

**Schmidt, Nicole**: Claro, porque cualquiera que está con esta licencia puede tirar una pregunta y preguntar dentro de nuestras tablas.

**Lucio Rojas**: Exactamente.

**Lucio Rojas**: Usuario, binintelligence, contraseña. Si está logrado con eso. Todos los que accedan con ese usuario y contraseña, no quiere decir que se

**Lucio Rojas**: vaya a usar, ¿No?

**Lucio Rojas**: Porque por ahí el prompteo es medio específico.

**Schmidt, Nicole**: Claro. Yo lo que no entiendo que, digamos, lo están haciendo así. Lo que no me queda en claro es que supuestamente van a usar para desarrollar también y van a conectar otras bases de datos y van a conectar otras cosas a esa misma licencia. No me queda claro cómo va a funcionar todo eso. Cloud va a entender, tipo,

**Lucio Rojas**: Es un usuario y contraseña,

**Schmidt, Nicole**: todos conectamos ahí.

**Lucio Rojas**: ¿Cuántos son en tecnología?

**Schmidt, Nicole**: Bueno, no se la dieron a todos.

**Romano Bazán, Ayelen**: Claro, no se la dieron a todos, pero hay por ejemplo tres proyectos, o sea nosotros tenemos este proyecto y después hay dos proyectos más de desarrollo que van a usar esa cuenta, pero bueno, por eso están analizando. Después íbamos a crear una cuenta por proyecto cómo se va el dividendo, pero ahora es como que nos dijeron bueno para arrancar tienen esto y es lo que empezamos a probar.

**Schmidt, Nicole**: Te dejamos sin token, ya está,

**Lucio Rojas**: compart.

**Romano Bazán, Ayelen**: Bueno, acá estoy, No sé, no tengo ni idea cómo funciona nada.

**Lucio Rojas**: Vamos a usar dos cosas, TeamOT y Cloud. Primero si quieren empecemos desde Cloud, tienen que ir a donde está la cajita de herramientas en la izquierda ahí donde dice personalizar hay un símbolo de una cajita de herramientas, más arriba el penúltimo y ahí tenés dos cosas para personalizar todos tus chats, Skills, que son funcionalidades que vos le das a Cloud y conectores que son herramientas que vos le das cuando querés armar un agente, podés usar los dos al mismo tiempo, entonces enseñarle a hacer algo con distintas herramientas que vos les das. Nosotros desde Theramot creamos un conector personalizado para que puedan ejecutar consultas a las tablas y crear nuevas tablas, nuevos ETLs y desbloquearlo en infraestructura desde una conversación con Cloud. Lo que vamos a hacer ahora es conectar Teramo a Cloud. Hay conectores que son predilectos de Cloud y conectores que son personalizados. En el más te vas a poder encontrar con los dos, Si explora los conectores vas a ver todos los que tiene Cloud. Ya que hacemos un repaso de a todas estas herramientas te puedes conectar con un OAuth directamente con aceptar y la nuestra Etheramo tiene una configuración especial porque no está predilecta por Cloud, entonces tenés que agregar un conector personalizado donde pones. Y URL, eso lo propicia la web del Teramot, Tengo que empezar a hacer ida y vuelta,

**Romano Bazán, Ayelen**: bueno acá ya puedo salir ahí donde.

**Lucio Rojas**: El URL es primero. Y ahí añadís directamente. Ahora, esto es un pequeño truquito que conocemos los que trabajamos en implementación en los tres puntitos desconectar. Todavía, OK, elimina lo hay que hacer porque. Te tiene que pedir un token para eliminar el final y repetir el proceso porque tiene que pedir un token. De vuelta. Quizá lo podemos ver ahí. Bueno, si querés copiarlo desde Theramo generas un token que lo copias ahí, Le das un nombre.

**Romano Bazán, Ayelen**: Acá yo que tendría que generar un token, o sea quedaría uno solo.

**Lucio Rojas**: Sí es un token para la conexión, se pueden crear X tokens, cada uno genera la conexión, se lo copias. Y ahí

**Lucio Rojas**: está.

**Lucio Rojas**: Donde se requiere aprobación. Ahí puedes darle permiso, permitir siempre, sino después te lo pide mientras estás versando. Estos son los permisos para ver las tablas, para generar consultas y demás. Puede permitir de antemano o se puede ir dando la aprobación a medida que uno va interactuando con la herramienta y

**Schmidt, Nicole**: se los pide después.

**Romano Bazán, Ayelen**: Te lo puedo cambiar W.

**Lucio Rojas**: A ver los tres puntitos que te muestran ahora es actualizar la lista de herramientas. Bien, bueno, ahora volvemos a. Ahora tenés que volver directamente a lo que es la conversación con CL. Ahí ya entiendo que quedó conectado al USPACE, y ahora lo que se hace es llamar a theramo directamente desde la conversación con CL. Se hace la pregunta de conéctate a Thermo y decime qué tablas silver serían tengo conectados. Ahí carga la tool, empieza a hacer permisos de solicitud, donde se dice, ahí puede conectar. Ahora nos pidió el token de vuelta, ahí está, ahora sí, car token que

**Romano Bazán, Ayelen**: te pido acá de vuelta y que

**Lucio Rojas**: ahora entiendo lo que pasó, explico bien. Pero sí tenés que cargarle el token que te dio la

**Romano Bazán, Ayelen**: E, sí es

**Lucio Rojas**: el mismo,

**Schmidt, Nicole**: Te debe haber quedado una pantalla emergente, una ventana.

**Lucio Rojas**: Perfecto. Si querés para empezar a hacer consultas, podés pedirle que te haga una descripción de cada columna para entender bien con qué tablas estamos trabajando, pero ya ahí

**Schmidt, Nicole**: tiró un montón de data. Una es la conexión del estamos renegando con un problema de localidades, cómo se mapean los departamentos, las provincias, los códigos postales. Pero

**Lucio Rojas**: estás teniendo este dolor en el momento, ¿No?

**Schmidt, Nicole**: La relación entre AFIP y UDP, porque en realidad ahora es ARCA, pero existe un código en ARCA que te determina qué localidad es, que le llaman código onca. Tenemos un problema ahí, que no estamos pudiendo mapear unívocamente lo que tenemos en ARCA con lo que tenemos en nuestra base de datos, que es unificación de localidades. Ya tira ahí. ¿Qué pasa? Que si de cruzar esas dos.

**Lucio Rojas**: Vamos a dividirlo, a ver si podemos

**Lucio Rojas**: verle eso mismo así, o sea, armado ni estructurado, pero con detalle, diciendo, che, ARCA tiene esto, OK, el otro el UDP está otra cosa. Tengo problemas.

**Lucio Rojas**: Macheo Y sí, sí, porque estamos teniendo

**Schmidt, Nicole**: como duplicado de códigos de localidades, no sé. Bueno, ahí tendríamos que. Para nosotros el problema no es nuestra base, sino que el problema es la base de Onca, de Arca, de la fif en sí.

**Lucio Rojas**: ¿La tenés? Se puede descargar algo tipo.

**Schmidt, Nicole**: Y ahí voy a. ¿Cargaste la de?

**Romano Bazán, Ayelen**: Sí, acá en realidad yo cargué dos tablas, y después acá en tablas quise escribir algo, como que le escribí un par de instrucciones y algo hizo, pero no sabía bien cómo funcionaba, como que lo fui haciendo a mí como me pareció. Pero sí, en realidad lo que nosotros tenemos es una tabla con las localidades de UDP, que son las de bolsa, digamos, y otra con las localidades reales, las localidades de Arca. Y hay que hacer como el mapeo entre esas dos tablas.

**Lucio Rojas**: Me interesa que entiendan las diferencias. Esto que vos hiciste desde la generación de la herramienta, enteramos en sí que quisiste darle instrucciones, el resultado que va a generar la conversación con claridad, donde dice instrucciones, si querés ir a esa pestaña ahí arriba, eso que escribiste vos, lo va a redactar de ahora en adelante cl para generar la query SQL. La diferencia es que toda la iteración que vos tengas con Cloud, y al usarlo como asistente de de datos, con contexto de la situación, va a poder entender específicamente qué instrucciones darle para generar la tabla que vos tenés que hacer para solucionar tu problema. Entonces, la idea acá, si quieren, para empezar a trabajar con estas primeras dos tablas, y entender cómo funciona, tratar de hacer una Go, es describirle exactamente a Cloud donde tiene las tablas conectadas, cuál es la situación problemática que tienen ustedes con estas dos tablas. Y van a, espero yo, que sorprenderse con la capacidad analítica que tiene para decir, bueno, quizás hay que generar esta idea, hay que eliminar duplicados, de esta manera está pasando esto. Entonces, lo que yo sugiero para empezar en la media hora que tenemos, es entrar a Cloud y empezar a describirle el problema y entender qué nos propone con theramos para solucionarlo fuera de ese lado.

**Romano Bazán, Ayelen**: Yo acá puedo ver que se cargó en cada tabla, le tengo que preguntar. Acá.

**Lucio Rojas**: Puedes pedirle descripción de cada campo también,

**Schmidt, Nicole**: Porque ahí lo que te propuso es armar una tabla Gol, decía como para unir las dos, un preview de ellas, o crear una tabla go a partir de estas, o sea para unir, para hacer la relación como que arma una tabla puente, cómo sería cuando tira eso.

**Lucio Rojas**: Sí, no también.

**Schmidt, Nicole**: ¿No, o sea, porque no sé si estoy tan familiarizada con lo de cuando dicen gold y silver, qué significa? Si me aclara esa joya.

**Lucio Rojas**: Perfecto. Silver es esto que está previsualizando ayer, que son las tablas que vos le cargaste. La única diferencia, las tablas tal cual vos se las cargaste, nosotros la llamamos bronce y silver es una copia 95% exacta de esa, con una diferencia de un 5%, que es unos crafteos de fechas de normalización, unas columnas, eliminación ID que están duplicados. Lo que va a hacer la herramienta es en base a esas tablas que vos le cargaste, entendiendo la metadata, que por eso te puede devolver toda la información de que tiene la tabla, y haciendo queries a esas tablas te va a poder, vas a poder hacer dos cosas, o analizar en profundidad las tablas que te cargaste, o en base a esas tablas crear cosas nuevas. Esas cosas nuevas pueden ser tablas o análisis. Las tablas que vos crees van a usar como input la silver, que son las bodas. Entonces yo quiero resolver que no puedo hacer un show en estas dos tablas porque no entiendo cómo tomar un ID único. Bueno, empezás a explicar eso y Theramo entiende el problema con crop y te propone una tabla nueva, que si vos decís hacémela, la ejecuta y la deja desployada y vos después la podés consumir y se actualiza permanentemente.

**Schmidt, Nicole**: Claro, esa sería la tabla gol, Esa

**Lucio Rojas**: sería la tabla golpe.

**Schmidt, Nicole**: Y nuestro gran problema es que muchas de las localidades que están en la base de datos de bolsa, que es la no tienen cargado el código que corresponde a la de AFIP, y son tantas que no las podemos mapear a todas y hacerla toda manopla y metiéndole son muchas, y además como que no es medio difícil encontrar cuál es cuál, porque están escritas distintas las localidades, los departamentos, entonces como que directamente propuso algo ahí, como decir te armó una tabla gol para cruzar los dos datos, pero no sabía qué iba a hacer.

**Lucio Rojas**: Tenés que reenquiar una tabla A con datos de la tabla B, que puede ser lo más, incluso importantísimo que no tenés ganas de hacer. Se lo podés pedir y yo creo que podemos ver el resultado ahora en los próximos 10 minutos y ver qué pasa. Si querés hacemos eso. Responda a este pedido, se queda.

**Romano Bazán, Ayelen**: Sí, este pedido es. Esto es lo que estamos hablando recién intenté explicarle eso, a ver, no sé si seguramente me va a hacer alguna pregunta o algo, pero. Porque acá identificó justamente los casos de ID localidad UDP, y justamente ese es el problema que nosotros tenemos. Y yo lo que necesito, digamos, es completar esos casos que están en cero, que me los matchee con otra tabla y los identifique por descripción, que la provincia sea la misma y controlar que ese código UDP no se esté usando ya.

**Lucio Rojas**: Bueno, ahora vemos que si querés puedo ver qué query está haciendo ahí. Si desplegas el simbolito de theramo, es de acá. Abrimos alguna de las de resultado y podes ver en vivo cuál es. Va haciendo eso, por eso después queda persiste en. Vamos a esperar que responda. Y una vez que Claude entiende el problema, lo que hace es pasarle un archivo plano a Theramo con las instrucciones que tiene que usar nuestro modeling para llegar a esa tabla, que sería hacer por vos ese proceso que intentaste hacer de darle las instrucciones a mano. Después tiene otras ventajas que son a esto yo digo flujo de ida, que es cuando estamos creando algo, después podemos consumir esa información en un flujo de vuelta, decirle de toda la tabla que creamos, hacemos un dashboard, hacemos un análisis, hacemos un informe, vamos a usarlo para tal y cual cosa y le vamos

**Schmidt, Nicole**: a pedir que haga un script para actualizar esos códigos, la tabla de bolsa. Eso solucionamos un montón de problemas que hay en este momento.

**Romano Bazán, Ayelen**: Bueno, ahí lo que me está haciendo es yendo a buscar la tabla mapeo localidades. Ahí no sé si se va, porque en realidad es a la que yo creé.

**Schmidt, Nicole**: A esa la creaste en Terabot, la mapeo localidades.

**Lucio Rojas**: Te voy a hacer otro creo, si no me puedes pedir que haga otro. Voy a ver si les pide el checkout completo.

**Romano Bazán, Ayelen**: Y acá me parece que lo que le está faltando es información. La UDP tiene descripción.

**Lucio Rojas**: Como entiende todo el problema. Es bastante sorprendo cuando busco resolver algo. Como entiende el problema y propone.

**Romano Bazán, Ayelen**: Sí, como que ahora todo lo que está diciendo es todo lo que nosotros fuimos haciendo, digamos, como que tuvimos un montón de tiempo para ir haciendo todo esto y es todo lo que va diciendo. Y para mí no sé si tiene que él está hablando de la relación, porque nosotros tenemos localidad partido provincia y en una de las tablas no está la provincia directamente. Entonces me parece que lo que le está faltando es que le cargue la tabla que relacione los partidos con las provincias.

**Lucio Rojas**: Si quieres cargarla, que la podemos cargar

**Romano Bazán, Ayelen**: válidos de esa provincia, no solo el principal. Calidad partido.

**Schmidt, Nicole**: Pero no sería la tabla UDP y un bajo partido. Esa habría que hacer un exportar.

**Romano Bazán, Ayelen**: Si, hay que cargarle esto para mí partido. Lo que pasa que después acá tenemos el otro problema, que son problemas nuestros, que hay un montón de partidos que están mal cargados. Todo esto que estaba como no definido.

**Schmidt, Nicole**: ¿No? Y si no hay que sacarla directamente.

**Romano Bazán, Ayelen**: Si no esto igual está cargado sin UDP. Sin, o sea no es nosotros vía ya está mal cargado en UDP. Sí, es los problemitas generales que tenemos con UDP.

**Schmidt, Nicole**: OK, bueno, ahí se va a pegar una mareada capaz, pero si esto lo

**Lucio Rojas**: tendríamos que querés exportarlo y lo cargamos, ponelo en un Excel. Si querés decir a Claude que te haga un CSV con eso y lo cargamos.

**Romano Bazán, Ayelen**: Como que me lo copié en un Excel. ¿Vos decís que esto se lo puedo copiar directamente?

**Lucio Rojas**: Se lo puede algún chat nuevo de Cloud y usar a Cloud. Yo lo uso para.

**Schmidt, Nicole**: Quedamos sin token.

**Lucio Rojas**: Yo porque tengo la canilla abierta.

**Schmidt, Nicole**: No, claro, nosotros estamos ahí.

**Lucio Rojas**: Hacé de cuenta que tengo un hijo, me sale más o menos eso.

**Romano Bazán, Ayelen**: Yo la otra vez lo hice así y después esto se lo subí directo a Téram, fui por ahí hace eso. Vamos por el camino.

**Schmidt, Nicole**: El de la vieja escuela.

**Lucio Rojas**: Creo que CCB lo toma mejor, pero no se puede abajo. Yo a veces la corta se ve.

**Romano Bazán, Ayelen**: Sí, igual ahí. Bueno, no sé si vieron, pero recién lo de Cloud también me identificó como duplicados. Me puso el hecho de que hay localidades que tienen el mismo nombre, que justamente uno de los problemas que tenemos, que hay localidades que tienen el mismo nombre pero son de provincias distintas. Y ese es uno de los problemas que tenemos. Y dos, y acá.

**Lucio Rojas**: Acá elle observe un paralelismo así les va a aparecer a ustedes su warehouse cuando lo conecten. Ahí de falta algo, Ahí va a aparecer su webhouse cuando lo conecte va a tener ese mismo formato, vas a poder ver las tablas y todas las columnas que tiene. Entonces cuando conecten su web van a elegir qué tablas y qué columnas darle. Se puede elegir hasta ese nivel.

**Schmidt, Nicole**: ¿Pero va a aparecer como tipo fuente de datos ahí una sola opción que va a decir ponele DW Y adentro van a estar todas las tablas o van a aparecer todas las tablas ahí donde está partido Localidades?

**Lucio Rojas**: No, va a aparecer una fuente de

**Schmidt, Nicole**: datos nueva, una sola, y adentro van a aparecer, porque estas son tablas individuales, adentro van a aparecer todas las tablas

**Lucio Rojas**: hasta lo que pueden hacer incluso acá es, si quieren creamos un caso de uso nuevo para no mezclar las cosas,

**Schmidt, Nicole**: tipo que esto va a estar dentro del Data Warehouse también

**Lucio Rojas**: vemos cómo.

**Romano Bazán, Ayelen**: Sí, lo que pasa es que

**Lucio Rojas**: no, pero va a tener que esperar que se cargue la tabla. ¿Todavía no cargó la que?

**Romano Bazán, Ayelen**: ¿Y eso cuánto tarda?

**Lucio Rojas**: Y en un Excel como el que cargaste no tarda más de 15 minutos. Un warehouse como decíamos hoy, puede ya cargar una o dos horas.

**Romano Bazán, Ayelen**: Y eso cómo me di cuenta que

**Lucio Rojas**: cargó bien, puedes ir a la plataforma de vuelta. Y te da un cartelito que notifica ahí donde dice si lo leyes en proceso. Esto tomará algunos minutos. Se pone en verde.

**Romano Bazán, Ayelen**: Ah, y ahí está conectado. Está bien. Bueno, acá me encontró. Bueno, este es el problema que tenemos. Estas, las 9.000 localidades que tienen UDP.

**Schmidt, Nicole**: Ya te tiro un reportecito ahí, sacale captura y mandale eso.

**Lucio Rojas**: Podemos pedir dos cosas acá. Primero que te cree, pregúntale si yo quiero hacer una BO para solucionar esas nueve mil y pico de localidades, ¿Cómo lo harías? Ah, de una podés pedirle que ponga todo esto que entendimos en un PDF para mandárselo a alguien explicando el problema y te pone todo.

**Romano Bazán, Ayelen**: Lo que me genera duda es que como que pone 7 match, que entiendo que de lo que yo le dije, como que Puedo, de estas 9000 logró 7 matcharlas bien y 2 con conflicto.

**Lucio Rojas**: Pregúntale.

**Romano Bazán, Ayelen**: Y del resto, acá dice de las 9000 sin match, solo recupera nuevo esto. Se decía que las tablas de localidades no tienen un campo de provincia explícito. Ah bueno, justamente esto que me está pidiendo, la relación provincia partido, que es el Excel que cargamos recién, archivo, ya existen. El resultado es conservador pero confiable. ¿Están listos para auxiliar los dos conflictos de la esquina? Requieren revisión manual. ¿No pueden auxiliarse dos provincias distintas a la vez o preferís revisar los conflictos?

**Schmidt, Nicole**: Las dos que están mal tienen el mismo código UDP y distinto en el AFIP. Ahí va.

**Romano Bazán, Ayelen**: En realidad la esquina aparece dos veces, pero uno con Córdoba y otro con Santiago del Estero, y él le quiere asignar el mismo UDP porque encuentra dos la esquina.

**Schmidt, Nicole**: Claro, pero en la FIP hay dos códigos. Claro, tiene que ver. Claro, nuestra base de datos, cuál es la provincia, para saber cuál es el código UDP. Está bien. Te falta información para terminar. Matcha todo.

**Romano Bazán, Ayelen**: Sí, por eso acá dice eso, que le falta justo el XLS para hacer el match provincia partido.

**Lucio Rojas**: Lo que no les queda claro, decís, explícame esto, laboure, la gente.

**Lucio Rojas**: Ya, está

**Schmidt, Nicole**: bueno, está bueno.

**Lucio Rojas**: Por eso es tan importante. Dentro de todo lo que se puede hacer con Theramo, la parte de limpieza de datos, de entendimiento, de ordenamiento, es lo que después te permite llegar a estas conclusiones, solamente decir che, me ahorra porque le prometeo y resuelve. Sino que te vas haciendo llegar a conclusiones que a lo mejor en caso manual sigue habiendo un humano que está decidiendo y haciendo, pero antes hubiera sido manual, tirando los l fijándote con un

**Schmidt, Nicole**: disting tarda dos semanas más y acá en 10 minutos.

**Lucio Rojas**: Tal cual.

**Schmidt, Nicole**: No, que para mí hay que darle un poquito más de contexto, de explicarle cómo. Porque digamos, estas de UDP que nosotros llamamos es unificación y es una base de datos que se hizo a propósito para que todas las aplicaciones de la bolsa usen la misma localidad. Pasa con personas, digamos. Entonces cuando alguien no se va a cargar un cliente, ya sea en el laboratorio o en contrato, en donde sea, busca la localidad y eso se va a buscar esa base de datos y trae la localidad. Si no existe o no la encontraban a la localidad para cargar un domicilio, la creaban de nuevo. Pero esto está mapeado en todas las aplicaciones. Entiendo. UDP, si rompemos algo ahí, rompemos para todos lados. Como que yo le daría ese contexto de que esa base de datos UDP está conectado a un montón de aplicaciones que posiblemente se duplicaron porque alguien cargó mal a mano algo que ha pasado, digamos que la esquina, ponele, no la encontraron como la querían encontrar y la crearon y en realidad una igual entonces. Exacto.

**Lucio Rojas**: Lo raro. A ver, no es lo raro, hay un proceso que corre, que es cuando hace la primera analítica de los datos, que avisa que encuentra dos nombres iguales, la esquina con dos IDs distintos.

**Romano Bazán, Ayelen**: Sí es que en realidad esto de la esquina lo quiso hacer Teramund, o sea, esto no está identificado así dos con el mismo candidato.

**Lucio Rojas**: Lo que intentó hacer el forzado porque encontró los dos de AFIP, existen esquinas y evidentemente debe existir una en Santiago del Estero y una en Córdoba, pasa que quizás en el macheo de exacto tengan ustedes, habría que ver ese 26269 qué ID AFIP tiene, o sea si ahí tenés el SQL abierto, tira el SSL,

**Lucio Rojas**: yo eso no entiendo cómo responde tan rápido, para mí te llegue cuando va escribiendo responde muy rápido. Sí, sí, o cuando lo dejas tipo en caché ya analizó la pregunta que le ha sido, responde muy rápido.

**Romano Bazán, Ayelen**: La otra tabla,

**Schmidt, Nicole**: esto es un vicio, esto ya empieza a ser ahora podemos jugar acá

**Lucio Rojas**: el problema que antes te tardaba mucho tiempo era esperar 10 minutos que se caiga la tabla, es un cambio raro.

**Romano Bazán, Ayelen**: Sí, por eso aparte de todo este análisis que hizo ahora está perfecto y es todo lo que vinimos haciendo, entonces es como bueno ahora quiero, yo ya lo hice, necesito el paso adelante, venimos hace semana con este quilombo y la

**Schmidt, Nicole**: bolsa hace entre ella había problemas, se quejaban.

**Lucio Rojas**: Ahora algo que les quería comentar, lo que vos decías Niki, que tener cuidado con la base esa UDP porque si la rompe, le rompe todos lados, esto está trabajando con una copia de datos y que está desconectada del origen.

**Schmidt, Nicole**: No, no, sí obvio, es como yo digo, para cuando me haga el script yo ya estoy pensando en mi script final que se ejecutaría

**Lucio Rojas**: ahí, otro cantar. Igualmente.

**Schmidt, Nicole**: Está todavía laburando,

**Lucio Rojas**: generalmente maneja los errores

**Lucio Rojas**: solo te avisa nomás, pero si siguió, Así que ahí no te hagas, no te hagas historia e igualmente si vos le decís no sé te resolvió todo, armame el script para actualizar la base UDP o la tabla de UDP productiva en la base de datos de producción, bla bla bla, no sé, crearme una transacción para confirmar antes de borrar y le tiras todo eso, te hace el script con todo, Una consulta de validación previa y posterior como para saber cuánto registro había, te arma todo lo que vos quieras, es pedirlo ahí.

**Lucio Rojas**: Aprovecho que estamos justo en este espacio, está bueno para recorrer un poco Claude, ¿Han trabajado con Cloudfor alguna vez? Bueno, si quieren hago esta introducción breve, ustedes lo que están usando ahora es Cloud Desktop de Desktop, no la nube, lo que pasa, se puede bajar Cloud Desktop y se baja Git y algunos comandos a la PC local, el mismo plot común te dice cómo hacerlo y te instalas Cloud Code. Cloud Code lo que hace, tiene acceso a tu terminal, tiene acceso a tus archivos, puede publicar cosas por vos, entonces directamente le puede decir bueno genera un script y entra VS Code y lo hace, o lo puedes gestionar de terminal o decís bueno tomá el archivo que tengo en la carpeta y actualizalo con este script y directamente empezás a ejecutar con Cloudpad y ahí le podés decir bueno necesito que toda esta información que tenemos, hace un modelo predictivo, lo hace y lo ejecuta, es bastante más potente que el Cloud Web y vale lo mismo en realidad ustedes ya lo tienen, lo último tiene que ser baja, ahí

**Schmidt, Nicole**: estamos en tratativa por todo el tema seguridad y toda la cuestión para ver qué tanto aceptan, porque bueno también están con auditoría, aprobación, entonces bueno, procesos burocráticos que hablábamos la otra vez, de hecho a mí ya me cortaron las piernas, pero yo ya estuve a punto de instalarlo sin que sepan, pero ahora tenemos contraseña, todo para instalarlo, o sea que no podemos, Antes tenía libre y bueno ya no se puede instalar cualquier cosa, pero sí, sí sabemos y estamos, se está tirando todo para que sí y que lo vamos a hacer, pero está llevando su tiempo digamos

**Lucio Rojas**: y hay.

**Romano Bazán, Ayelen**: Perdón, una consulta, yo esto por ejemplo ahora que estamos preguntando las localidades, yo le puedo hacer también que pregunte y lo relacione con información, no sé si encuentro una tabla de AFIP que esté subida a Internet o con información por fuera de lo que yo le cargo.

**Lucio Rojas**: Sí, sí, sí, aye, podés, podés, pero ahí como que el resultado ya un poco más difuso porque es la búsqueda que hizo en la web. A ver, sí la respuesta es sí, vos le podés decir, che, validame esto contra la página del correo argentino, no sé, lo que se te ocurra. El tema que ya ese origen de datos no es de lo que vos tenés acá cargado, o sea, o poder se puede. Sí la respuesta es sí, ten en cuenta de que sale a buscar data, esa es la única observación para hacerte, que a vos le podés decir que sea la página oficial de Arcade Información Pública, mostrame el origen, dame la página, mirás y le das el OK. ¿Pero bueno, hay que decirlo digamos, porque ese cross check lo va a hacer y si lo va a encontrar, OK, lo encontré en Internet, viste?

**Schmidt, Nicole**: Sí, el problema es ese, que tampoco tenemos una fuente oficial y creemos que los datos también se cargaron. Medio vimos una tabla muy parecida en Internet, y es como que no sirve. En cierto punto entiendo que puede ser peligroso, porque está metiendo cualquier cosa sin saber qué está metiendo. Pero estamos en esa

**Lucio Rojas**: bajatela, esa tabla, cargala. Y hace la correa como para decir, bueno, esta es la que encontrábamos de este origen, tiene estas características, y le pegamos a esa. Y que no la vaya a buscar constantemente, porque por ahí busca en otro lado. ¿Y crees que está yendo a buscar esa tabla?

**Romano Bazán, Ayelen**: Sí, hay. ¿Más que nada porque ahora, como al hacerlo manual, hay muchas localidades que pasa esto, que no las encontramos, y terminamos googleando, bueno, tal código postal, a qué ciudad corresponde? Y si la realidad es que no tenemos ninguna fuente oficial que nos diga esto. Está bien, en muchos casos terminamos haciendo

**Lucio Rojas**: eso, porque el que tiene toda esa data debería ser Correo argentino,

**Schmidt, Nicole**: pero no, yo creo que es un problema que tenemos en la Argentina. No sé si escucharon algunas veces que hay un mismo código postal para dos localidades y no sé qué, y se envía cualquier cosa por cualquier cosa. Bueno, no sé si esa base de datos del correo también está bien. Hay un problema más grande. Hay que hablar con alguno de logística, de mercado libre, de algún lado, a ver cómo solucionaron todo ese temita.

**Lucio Rojas**: Correo argentino tiene una API que de última teniendo Cloud code, decir, che, de esta API bájame todo, te arma la app y te construye el dataset.

**Schmidt, Nicole**: Sí, en realidad debería de ser ARCA el que publique ese código, que es el que supuestamente le piden. Es para mapear el origen de la mercadería de grano, de qué campo salió. Y está como ahora solicitado, obligatorio, cuando vos presenta el CTG, la carta deporte. Entonces estamos tratando de mapear ese origen en sí, y debería de salir el código desde ese ARCA, para que nosotros después mapeemos nuestras localidades.

**Lucio Rojas**: Eso para la trazabilidad. Estuve reunido con un broker la semana pasada, y estaban con ese tema, y le b. Así en vivo, la demo no era específicamente para eso, pero querían obtener. Porque en la carta de deporte hay coordenadas del campo, o sea, tipo el PIN que te tira Google ma latitud y longitud. Pero en base a eso y el dato tipo dato catastral, pues está todo en la carta de porte. Armar el tipo un archivo KMZ, un polígono, porque hay un requerimiento. No me acuerdo ya ahora, se me olvidó a dónde tenían que llegar con esa data.

**Schmidt, Nicole**: Sí, sí, porque bueno, ahora a nivel legal está un poco siendo esto importante de que se mapee de qué campo sale la mercadería. Todavía no hay ni, o sea, hay un decreto por aprobarse, pero es como que a futuro se supone que deberían todos de saber de qué campo salió, porque hay cuestiones ambientales que están teniendo en cuenta. La Unión Europea dice yo no te voy a comprar salida si vos deforestaste

**Lucio Rojas**: el campo para mapear que no había

**Schmidt, Nicole**: salido deforestación ese todavía no se aprobó, pero estamos todos ahí a la expectativa. Se viene postergando porque se ve que tampoco hay producción suficiente para que el campo no haya sido deforestado, ponele. Entonces la Unión Europea se queda sin comer, básicamente. Entonces trata ahí en tratativa y imagínate que este quilombo de localidades fundamentales para poder saber bien de dónde sale todo. Igual de la bolsa se hizo un sistema que está por fuera de todo esto, pero nosotros queremos analizar esa información de los clientes que hoy tiene la bolsa ya.

**Romano Bazán, Ayelen**: Así que ese sistema encima viene acá también. ¿Por qué usar la localidad UDP?

**Schmidt, Nicole**: Sí, eso, o sea, lo tenemos que

**Romano Bazán, Ayelen**: arreglar ahí de base, porque lo usamos para todo.

**Schmidt, Nicole**: Sí, son todos los sistemas en realidad que están conectados de lo que sea, no solo laboratorio, está conectada a esta UDP, así que.

**Lucio Rojas**: Y sí, si, es maestro localidad.

**Schmidt, Nicole**: Claro, exacto.

**Romano Bazán, Ayelen**: Bueno, tenemos para jugar.

**Lucio Rojas**: Cierra acá por tema de horarios. Ustedes cuando terminen de ponerse de acuerdo con Claude, con lo que quieren hacer, le tenés que pedir que cree la OR, va a correr el proceso en Theramo y va a generar todas las instrucciones para hacer la query SQL y trabajar la tabla nueva que sería la Go, con todas las filas estas que mostraron enriquecidas con con la información que faltaba. Esa tabla la pueden consumir del mismo cloud para hacer informes, para hacer análisis, o la pueden descargar directamente como CSV o como Excel desde la web, pero tiene una limitante que hasta 100 filas. Para sortear eso nos pueden pedir un acceso por conexión a Power BI o a Excel por ODBC, que ya les mantiene activa esa tabla en la herramienta que ustedes quieran.

**Romano Bazán, Ayelen**: ¿OK?

**Schmidt, Nicole**: Bien,

**Romano Bazán, Ayelen**: ahí quedamos pendiente entonces que nos avisen cuando esté solucionado la conexión y que nos manden el esquema de la arquitectura para revisarlo con los niños.

**Lucio Rojas**: Te mando ahora con el resumen de la reunión. Bueno, nada, saber qué les pareció, qué les pareció la herramienta es interesante. ¿Cuál es la?

**Romano Bazán, Ayelen**: Me sorprendió que fue todo lo que hicimos durante este tiempo. Ahora es como que estamos en el mismo punto de lo que logramos hacer. Nos falta dar el paso adelante, decir bueno, lo solucionamos. Así que nada, yo me quedo ahí con la expectativa de decir bueno, estamos ahí, llegamos al mismo punto y cuando

**Lucio Rojas**: te quedes sin crédito, ahí me largo.

**Schmidt, Nicole**: Llenar esto es como la apuesta, ¿Viste? Después empezamos plata toda y arrancar.

**Lucio Rojas**: Yo te digo a mí, yo se me está yendo galaxia de 100.

**Schmidt, Nicole**: Sí, bueno, cuando demostremos todo esto, ahí ya supongo que van a soltar un poco más.

**Lucio Rojas**: Ahí está. Ese es el punto más valioso. No es que yo no lo haya hecho, pero bueno, hay herramientas que funcionan más rápido y el objetivo es acelerar el laburo, entregar más y es más entretenido, qué sé yo, trabajar de otra manera. Todo tiene, o sea, se postula de una manera de planteo como para que esos 100 aparezcan y no sean tan esquivos.

**Schmidt, Nicole**: No, no, y este problema es riguroso, o sea, no es que, o sea, si logramos esto y funciona bien y se hace el script, yo creo que ahí sí yo voy a pelearla con toda, olvídate. Pero bueno, lo tienen que aceptar ellos también.

**Lucio Rojas**: Bueno, seguimos los pasos y la idea es que para fin de, no sé, fin de esta semana, pues estamos a martes, creo que un poco antes, tengan esto mismo en el Warthouse y puedan solucionar esos problemas del Warehouse que también tiene. Bueno, perfecto, nos seguimos viendo por lo peor los martes a las 12.

**Lucio Rojas**: Igualmente, cuando les termine de cargar esa tabla, que minuto más, minuto menos va a hacerlo. Si prueban, si quieren sacar gente del correo, quedamos nosotros cuatro y estamos en contacto por ahí, usemos el correo y listo, con cualquier duda.

**Schmidt, Nicole**: Vale, genial, buenísimo. Bueno, gracias. Nos vemos.
