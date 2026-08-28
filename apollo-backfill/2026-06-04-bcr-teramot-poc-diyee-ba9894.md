# BCR- Teramot POC DIYEE

**Fecha:** 2026-06-04T12:30:59.560+00:00  
**Duración:** ~63 min  
**Participantes:** Emilce Terré /BCR <eterre@bcr.com.ar>, Lucio Rojas <lucio@teramot.com>, Tomas <>, Fabricio Riguetto <>, Milagros Galassi <mgalassi@bcr.com.ar>, Ayelen Romano Bazan <aromano@bcr.com.ar>, Belén Maldonado <>  
**Externos:** eterre@bcr.com.ar, mgalassi@bcr.com.ar, aromano@bcr.com.ar  
**Apollo ID:** 6a217f0603ec140010ba9894

---

**Ayelen Romano Bazan**: Hola, buenos días.

**Lucio Rojas**: ¿Buenas, cómo están? ¿Se escucha? ¿Voy a pedir que agregue dos personas hacia la Hola, buenas, cómo va?

**Ayelen Romano Bazan**: Sí, yo en realidad les había. Se las reenvié pero les reenvié el evento pero no les podía reenviar toda la serie que son Mili y Fabricio. No sé si ahí los pudiste subir.

**Lucio Rojas**: Está mi garage. No, estuve, tengo.

**Ayelen Romano Bazan**: Estaba enfermo

**Lucio Rojas**: hasta llega media tarde, estaba en otro plano, así que ahora estoy retomando un poco actividades. Sí, por eso me estaba viendo los mails recién y los tengo que agregar,

**Ayelen Romano Bazan**: si no para hoy sí los puede sumar. El tema era ese que no podía agregar después para toda la serie. Ellos tienen el evento pero sería para después.

**Lucio Rojas**: Mientras hacemos Doria que llega, Qué les pasó estudiando los mail con Juan mientras esperamos que se suma toda la currícula con el otro caso.

**Ayelen Romano Bazan**: No, ahí lo que nos había pasado es, te acordás que nosotros no podíamos, no funcionaba el tema de subir las tablas desde la base de datos, que yo te pasé el listado que eran como 30 tablas y ustedes las subieron y esas tablas funcionaron bien, o sea están cargadas. El tema es que nosotros no podíamos cargar tablas, o sea no podíamos hacer la carga de tablas. Entonces lo vimos con Juan y en el momento yo le mostraba que quería otra conexión y me pasaba lo mismo que quedaba como dando vueltas y no sabíamos bien cómo ustedes lo habían corregido para subir todas esas tablas. Ese era el problema que teníamos, como que no sabíamos si se había corregido algo o había algo que nosotros estábamos haciendo mal, pero no podíamos subir tablas nuevas desde la base de datos.

**Lucio Rojas**: ¿Bien, ustedes sumaron nuevas tablas que quieren ver? ¿Aparte de las que ya me pasó?

**Ayelen Romano Bazan**: No, no, era más que nada para ver si eso había quedado solucionado y si no, porque después cuando vamos probando con los usuarios nos van pasando que tenemos que agregar una tabla o algo y desde que empezamos como que de nuestro lado no lo podíamos hacer siempre viste que tuvimos problemas y demás, entonces queríamos ver que realmente eso haya quedado solucionado y que después podamos subir tablas nuevas.

**Lucio Rojas**: Ahí estuve más o menos sobrevolando un poco el tema esta mañana y siempre teníamos nosotros el tema que estaba caído a veces el túnel VPN, no sé por qué lado era, pero si no era eso también la UI es bastante caprichosa en ese flujo, así que hay que ser también cauteloso con cómo seguirla. Eso está re de nuestro lado. Obvio. Después está lo del túnel, que también creo que era un poco las dos cosas.

**Ayelen Romano Bazan**: Sí, lo del túnel exterior está funcionando, yo siempre que hablo con seguridad y red me dicen que está funcionando, o sea, por ahora no se cae en eso estaríamos OK. Pero bueno, nos pasaba ese problema que se conectaba, viste, que antes no llegaba, ahora es como que se conectaba y no nos dejaba elegir las tablas, pero bueno, ahora ya están las tablas cargadas.

**Lucio Rojas**: Bueno, genial. Eso es cuestión de ir como todas las empresas, viste, El sistema de una empresa, la culpa del otro. Bien, bueno, si quieren volvemos a este plano.

**Tomas**: Dalex, ahí compartí porque tengo un par de dudas.

**Lucio Rojas**: Dale, buenísimo. Un poco habíamos quedado para hacer un recap que habían cargado distintas tablas ustedes de Excel, habíamos visto cómo se cargaban y que iban a probar la carga y cómo funcionaba un poco la herramienta para. Buenísimo.

**Tomas**: La primera de las dudas es, ¿Se puede cambiar el nombre de la fuente? Porque una se subió con este nombre y la verdad que es poco intuitivo y además como a la hora después de hacer las tablas Gold están como carga fuente y después los archivos, el nombre, queda un choclo medio raro.

**Lucio Rojas**: Segundo que voy a entrar al caso de uso para ver bien. Si querés hacer clic en los tres puntitos a ver si lo confirmamos, pero estoy casi seguro que no. En configurar no. Una vez que creamos la fuente ya toma ese nombre de una OK. Y entiende eso también. Después el agente para armar el warehouse y hacerlo John, como tiene el nombre de la tabla, si querés podés eliminarla y volverla a subir

**Tomas**: la opción, pero para evitar el proceso.

**Lucio Rojas**: Lo que no afecta esto es a cómo entiende el agente las tablas. Igual no creo que haya problema de scout.

**Tomas**: OK, perfecto. Después lo otro fue que nosotros, bueno, a partir de lo que fuimos subiendo, inicialmente pensamos que la creación de las tablas Gold era a través de la herramienta directamente, entonces nos metimos a quedar desde acá entre instrucciones y el agente propio acá, o sea este chat. Y después ayer justo nos contó que en realidad no lo podés crear a través de cloud. Entonces bueno, Bet estuvo probando justamente eso, por ahí con casos de uso un poco más simples. En esta sí como que fuimos haciendo bastantes transformaciones, pero en la otra no, en la otra simplemente fueron unos join, o sea, como asignarle de una tabla medio key a otra los nombres de.

**Lucio Rojas**: Bueno, hicieron un poco el flujo inverso, porque siempre es como. Está bueno usar clop para las que son más difíciles de hacer, que te asista, y después más joins, por ahí las solucionamos por acá, pero buenísimo que hayan hecho los dos flujos. Si querés contame cómo te fue con este, el de Club Polillo lo conocemos más, sabemos que suele funcionar mejor. ¿Cómo te resultó?

**Tomas**: No, en este en principio bien, o sea, llegamos al resultado que queríamos, que básicamente era como. Simplemente como meter agrupaciones por campos y después joinearlo con otra tabla y hacer. Y después lo que hacíamos era al revés, o sea, metíamos todas las transformaciones acá, y después consultábamos a Cloud a ver si las transformaciones se habían hecho

**Lucio Rojas**: bien,

**Tomas**: si los datos cuando hacíamos la consulta desde Cloud tenían sentido. Y bueno, por lo pronto eso.

**Lucio Rojas**: Ahora si querés, ahora si llegamos, podemos probar de hacer algún error desde clock. Desde clock está bueno, porque si arrancaste de acá.

**Belén Maldonado**: Sí, perdón. Bueno, ahí se escucha.

**Ayelen Romano Bazan**: OK.

**Belén Maldonado**: En vez de crear una.

**Lucio Rojas**: A Claude o a

**Belén Maldonado**: la gente, está bien o es preferible hacer.

**Lucio Rojas**: No, no, está bien. En origen se tiene que guardar. No, en origen, instrucciones acá, perfecto.

**Tomas**: Cada una de estas es la instrucción.

**Lucio Rojas**: Es una instrucción esto para entender bien el flujo. Teramot está realizando la misma función que haría usando CL, no cambia nada en su funcionamiento, ya entendió cada una de las tablas y la relaciona a partir de lo que ustedes le están pidiendo. La única diferencia es que en la experiencia mejorada, para lo que nosotros entendemos como una mejor experiencia, es entrar a Cloud y hablar con Claude ya mucho más en lenguaje natural, o sea, sin tener que pensar las instrucciones. No sé cuánto tiempo habrán estado pensando instrucciones, me imagino que no fue poco, porque, o por lo menos, no sé, media hora. Esto desde Cloud es mucho más sencillo, porque nosotros le damos todo el contexto de las tablas que ustedes cargaron, y ya entiende un poco mejor lo que ustedes quieren hacer, y él crea estas instrucciones, Esa lista de instrucciones te las crea Cloud y las pega acá, y ahí genera la tabla y vos después puedes auditar lo que hizo haciendo una consulta a esta tabla que ya es gold, y también puedes conquistar la silver para saber de dónde vino lo que hizo. Y ahora tengo una tercera instancia que puedes consultar las bronce, o sea podés saber cómo estaban tus tablas de origen antes de que nosotros las modifiquemos en el medio.

**Tomas**: Las bronce no las veo directamente.

**Lucio Rojas**: ¿No las ves? No, pero las podés consultar desde clock.

**Tomas**: OK, listo.

**Lucio Rojas**: Les puedes preguntar que es como un poder.

**Ayelen Romano Bazan**: Y ahí. ¿Perdón, qué diferencia hay entre las bronce y las silver? ¿Cuando ellos suben el excel no se cargan directo como silver?

**Lucio Rojas**: Claro, para lo que es funcionamiento de herramienta no hay ninguna diferencia, nosotros partimos de la silver siempre. Lo que vos podés hacer en la bronce es si querés hacer alguna auditoría entre la primer capa de conversiones, mira por ejemplo anda alguna tabla silver Tommy si querés.

**Tomas**: Dale, voy a cualquiera.

**Lucio Rojas**: Ahí en detalles de creación puedes ver SQL generado, si querés expandirlo, fíjate que hace un select y trae todas las columnas, no modifica nada. No, Perfecto. Este donde dice from el compras granos actual, esa es la tabla que creaste vos, que subiste vos y las compras granos compra actual que vos ve desde la plataforma es la silver, y ese select distinct es la no transformación, que en este caso es un téramo de pasar de bronce a silver. A veces hay algunos campos que los modifican, que les hace algo con las fechas, con los nombres, con ciertas columnas.

**Belén Maldonado**: ¿Querés mostrar la de NCM?

**Lucio Rojas**: ¿Dale,

**Tomas**: para que NCM? Ah bueno, para esto es. La divido en dos, pero en la

**Lucio Rojas**: segunda aparentemente no puso nada nunca y capaz que en algún momento 100 filas de 4000 capaz que en algún momento cobra sentido y vamos a ver qué hizo. Bien, ahí está. No, no, es un poco lo que hace la herramienta para poder trabajar mejor esa tabla para después hacer los joins y hacer algún filtro. ¿La verdad que no encontramos muchos errores en esto, pero por ejemplo el otro día, en el otro caso que tiene, ayer hubo un problema con unos Wilson que los había castigado mal o algo así, no? Una tabla que tenía una era un

**Ayelen Romano Bazan**: valor entero y lo modificaba como fecha,

**Lucio Rojas**: ahí nos dimos cuenta por ejemplo lo

**Ayelen Romano Bazan**: hacía por defecto digamos, hacía eso cuando subía la tabla silver por defecto nosotros no le habíamos dicho e interpretaba esos números como fechas y los modificaba.

**Lucio Rojas**: Son decisiones que toma que por ahora nosotros no le estamos dando la libertad al usuario de guiarlo un poco en esas instrucciones, está en intención, pero bueno, por ahora si encuentran algo así, che, qué raro lo que hizo, pueden preguntarle a Cloud qué está transformando acá, y nosotros después eso lo podemos volver un poco atrás. ¿Por ejemplo en tu caso, ya está solucionado eso, ese campo de modificado? Eso era un dato, no era para dar. No creo que nos detengamos mucho en los casos de uso en esto, si quieren saber la diferencia está ahí.

**Tomas**: Bueno, esto

**Lucio Rojas**: por un lado, por el otro. Voy

**Tomas**: como esto de que tenemos históricos y los datos actuales, dividimos la carga en dos, por así decirlo, como hasta el año 20, para evitar que cuando carguemos, cuando actualicemos los datos, el proceso sea tan largo, dividimos los B por el compras granos, tenemos el histórico que es hasta diciembre de 2025 y el actual que es del 1 de enero del 26 al último dato, y cuando se actualice sale el dato semanal. En este caso actualiza esa, actualiza esta fuente, las tablas Gol dependiente, o sea, después obviamente

**Lucio Rojas**: hay uno que es, Todavía

**Tomas**: no lo creamos eso, que es básicamente la anexión de las dos fuentes silver, o sea como que pegar, esa no la hicimos todavía. Si yo la creo esa tabla gold y tengo los datos consolidados totales de una gold, ahí cuando yo actualice la fuente automáticamente va a actualizar la Gol.

**Lucio Rojas**: Sí, si vos tenés una sola Go, donde tomás esas dos fuentes silver para ser un unificado, un consolidado, actualizas una, se actualiza todo y vos incluso con puedes tomar esa all para hacer otra all también.

**Tomas**: Se actualiza todo ese flujo y se

**Lucio Rojas**: actualiza todo ese flujo.

**Tomas**: Ah bueno, porque eso justamente lo que tenemos hecho acá, ponele, o sea las DJB, que son todas estas fuentes de batch, primero las unimos, después las. Y después fuimos acumulando por campos y después la joineamos con la tabla de compras. Si yo actualizo DJB con los datos que salieron diarios, salen diarios, ponele, corre el proceso ese y se actualiza. Encajaba todo el flujo.

**Lucio Rojas**: Sí, perfecto, buen dato. Creo que sí,

**Belén Maldonado**: No, no ir con otra cosa.

**Lucio Rojas**: Ah, dale, cierro esto. Lo que sí vos puedes hacer, puede hacer recursividad de gol hasta dos veces. OK, o sea vos puedes hacer una gol con mucha silver, puede hacer una gol nueva que tenga mucha silver y esta gol y hasta ahí, no puedes pasar a una tercera capa. No se puede hacer una gol que use dos goles. Una gol que está hecha por otra gol. ¿Se entiende? OK. Es como una triple concatenación. Ya. Para eso tendríamos que hacer otro. Otro proyecto que use esa tabla como fuente. Listo, listo. La DJ.

**Tomas**: Claro, perfecto. En este caso nosotros. Pensé que habíamos hecho eso justamente y no tenemos dos.

**Lucio Rojas**: Claro, ahí tenés una. Esa es gol de gol. ¿No podrías usar ahora una tercera que use DJB compras? Lo que puedo hacer es pasar esa DB compras a otro proyecto como tal Silver. No entremos todavía en esa triple, triple incrupción.

**Ayelen Romano Bazan**: Y ahí cuando la pasa a otro proyecto pasa lo mismo después con la actualización, o sea, se actualiza la primer silver, se actualiza, saltó el flujo por más que esté en otro proyecto.

**Lucio Rojas**: Sí, sí, porque es una sola tabla compartida.

**Tomas**: Repetime eso. Si, yo la llevo si quieren.

**Lucio Rojas**: Vemos esta nueva feature. Queremos una nueva. Pongámosle a este como ejemplo.

**Tomas**: Agrega un proyecto.

**Lucio Rojas**: Sí, ponele. No sé, esto vamos a suponer que lo consume Belén. Vamos a hacer ejemplo. Crea el proyecto. Bien, ahí si quiere voy para atrás al workspace. Vamos a repasar una función porque me interesaba. ¿Déjame ver quiénes están en miembros del Workspace? No, en el de workspace. El del workspace es este, el de la izquierda.

**Tomas**: Acá se ve.

**Lucio Rojas**: Y tus dos tienes que darle acceso, tienes que darle nivel. No sé si quieres que tengan solo lectura o moverlo. Belén está administrador, entonces va a haber todo. Bueno, genial, no hay problema ahí. Bueno, listo, No pasa nada. ¿Donde está el de Belén? Agregara si querés al proyecto, pero creo que ya va a estar porque. Administradora en el Workspace. Claro, ya es administradora en el workspace, entonces ya está por default en todo lo que se crea dentro. Pero supongamos que Belén no era administrador, que era alguien que solamente podía ver el workspace o no estaba agregado el workspace directamente vos late solamente este proyecto, lo único que va a poder ver es este proyecto. Ahora volví al deteramo. Puedes ir a la función nueva de abajo. Abajo donde está el schedule, Abajo es compartir datos. Ahí puedes elegir qué darle a Belén para que ella consuma de tu warehouse. Entonces elegís compartir donde está, y ahí puedes seleccionar todas las tablas que cargaste, cuál le das vos para que ella consuma. Bien, ahí si querés podés seleccionar todas o seleccionar las que se supone que si fuese algo con segmentación de acceso o de roles que podría haber. Y también le puedes no dar ninguna tabla silver, por ejemplo, y darle solamente una tabla gold que es la que vos creaste.

**Tomas**: No me acuerdo los nombres. DJB acumulado. Ah, son estas.

**Lucio Rojas**: Listo. Si querés probemos con alguna de esas. Compartir ahí con las GO. Perfecto. Y ella ahora desde el workspace de Belén, si querés ir allá, proyecto, perdón, de Belén, Fíjate que ella no va a tener fuentes de datos conectadas porque nosotros nunca le cargamos nada, pero si vas al Data Studio tiene la Gol y ella puede crear sobre esas GO más GO puede consumirlas. Si ya tiene solamente acceso a este proyecto, su MCP sólo va a ver esto y no va a haber todas las tablas que vos cargaste el workspace.

**Tomas**: Perfecto.

**Lucio Rojas**: Esto está bueno para si en algún momento necesitan segmentar alguna información o si querés empezar a crear proyectos más limpios. ¿Por ejemplo, si ustedes son muchos, que veo que son muchos y van a estar seguramente muchos metiendo mano, vos no crees que en un proyecto empiece a haber como contaminación de gols? Porque ya perdés un poco la auditoría de todo lo que se creó, ¿No? Entonces podés hacer como una suerte de, bueno, estos son gastos de la fuente, estas son las cuatro Gol que nos interesan mirar a todos. Yo comparto esto para todo el mundo, y en base a esto, que el resto cree de lo que cree adentro de su proyecto, que lo que cree no nos contamine el proyecto todos.

**Tomas**: Perfecto. Vos podés tener un proyecto que sea, claro, las fuentes primarias y por ahí la concatenación, esto de lo histórico y lo coso para que cuando. Cuando la Gol que se concatenan o se anexan más que se concatenan para consolidar la información, un mismo tipo de información y evitar la carga de todos los datos históricos cada vez que se actualiza el flujo. A partir de ahí crear proyectos que tomen esas GO directamente y que las transformaciones ocurran ahí.

**Lucio Rojas**: Claro, sí, eso es un ejemplo. A veces lo pensamos con segmentación de usuario. Esto sería más como limpieza del uso, que no sea el mismo lugar donde metemos todos manos para cargar cosas. Estaría bueno que nada más cargues vos y que lo vayas dividiendo. Esto no estaba la otra vez que hablamos. OK, estamos metiendo esos cantes.

**Tomas**: Una duda, Babel, ¿Vos querés meter la tuya?

**Belén Maldonado**: ¿Sí, no era nada más que viste que se puede hacer consultas SQL sobre las tablas que vos subís, lo que te devuelve esa consulta vos lo podés descargar o eso directamente lo tenés desde Cloud?

**Lucio Rojas**: A ver, eso. Si querés podemos ir al de sistemas y hasta donde yo tenía acá, ya le hice, ya hice la aclaración con Ayelén en la otra POP hicimos un cambio de plataforma nosotros hace muy poco, y había cosas que se podían hacer en la anterior y no estoy tan seguro que se hagan en esta. Entonces a medida que surge vamos preguntando y desde acá ya veo que no.

**Belén Maldonado**: Claro, nosotros lo buscamos y no encontramos la manera.

**Lucio Rojas**: Un Excel quería llevarte vos.

**Belén Maldonado**: No, claro. Una consulta que quiero hacer así rápido para no tener que ir a Cloud, conectarme, todo eso, ¿Como le consultaba?

**Lucio Rojas**: ¿Y en qué casos te haría sentido preguntar SQL sobre hacer una consulta?

**Belén Maldonado**: Porque pone, no sé, nosotros tenemos una fuente de datos grande, que es tipo cuando pasa algo, no sé sacan las retenciones por dos días, entonces nos matan a preguntas todo el tiempo. Y a veces como que es la misma consulta pero que se va actualizando, no sé cómo explicarte, capaz que en una hora nos preguntan lo mismo. Entonces yo directamente ejecuto la consulta y veo que me.

**Lucio Rojas**: Bien, sobre datos que cambian.

**Ayelen Romano Bazan**: Sí.

**Lucio Rojas**: OK, ahí te estoy esquivando la pregunta. Creo que no puedes descargar la tabla. Eso lo voy a levantar, Perdón por la tos, estoy saliendo de una vez un kitty fuerte. Y después quizás te convenga crearte una Gol para ese caso, explicándole a Claude el tipo de preguntas que te van a hacer, usarla y después borrarla por ahí para ganar, no sé, el mejor de uso es como te parezca más fácil. Yo estoy yendo por el otro lado, ya conocí la herramienta, por ahora no se puede descargar. Lo voy a anotar eso.

**Tomas**: Yo tengo otra duda más, pensando en el otro objetivo que tenemos nosotros, que es la disponibilización al público de la información. Con él con ver estamos haciendo la maestría en ciencia de datos, entonces estamos viendo modelos de lenguaje, o sea, fine tuneado de modelos de lenguaje o creación de rags. Y una de las aplicaciones que se nos ocurría es un modelo, crear un chatbot, ponele textosql, Claro Text, que entonces vos le das el der de tu data warehouse y entiende entonces las consultas, transforma las consultas de lenguaje natural a SQL, hace la consulta y le devuelve al usuario también con un modelo de lenguaje Quen o Lama, le devuelve al usuario el lenguaje natural, los datos que extrae de SQL. ¿Hay ese acceso a los datos estructurados por fuera de una API de Cloud? Es posible.

**Lucio Rojas**: Bien. ¿Por qué sería por fuera de una API de Cloud?

**Tomas**: Para evitar los costos. Esto lo disponibilizamos al público y por el costo de que venga cualquiera, o sea, de que nada se dispare, porque bueno, hubo mucho.

**Lucio Rojas**: ¿Cómo lo consumirían?

**Tomas**: El público en sí, una aplicación web que atrás en un servidor nuestro corre esa aplicación. Bien.

**Lucio Rojas**: ¿Y ese qué modelo usaría? Ahí me perdí. La aplicación que tenían ustedes.

**Tomas**: No, lo entrenamos nosotros. Claro, o sea, viste que sí, fintuña, la verdad que no teníamos idea.

**Lucio Rojas**: ¿Y qué proveedor elegirían? ¿De algún cloud terminas volviendo, o algún chat GPT, algo de eso?

**Tomas**: No, no, descargar algún modelo. Lama o Quen y correrlo en un servidor local.

**Lucio Rojas**: OK, bien. No, sí, perfecto. Nosotros a veces ofrecemos la opción más fácil, más cara, más predeterminada, que decir, usa una API de Cloud, pegala a las tablas y. Y ponen un fraud y que lo consuman desde ahí. Entiendo que eso te gasta mucho más token. Y que tener un modelo corriendo en un servidor local, bien fightuneado, con un rack, está mucho mejor. Si, eso. Nosotros lo que podemos dar es el endpoint a las tablas.

**Tomas**: Ah, eso se puede.

**Lucio Rojas**: Gol en Atina.

**Tomas**: Perfecto.

**Lucio Rojas**: La llamas vía.

**Tomas**: Ah, bueno, se podría. OK. Bueno, esa es una grande duda, porque la verdad que es uno de los objetivos principales del proyecto, por así decirlo, de este estructurado de datos, disponibilizarlo al público de una manera, al público externo, de alguna manera amigable. Y para evitar los costos, y sobre todo aprovechando que con Belu estamos incursionando en este mundo desde la ciencia de datos y los modelos de lenguaje, tenemos

**Lucio Rojas**: ganas de hacerlo nosotros. Está buenísimo eso. Teníamos eso en la versión anterior, después hicimos el cambio, medio que no lo deprecamos, sino que lo mantuvimos en la versión anterior con los clientes que estaban. No era mucho eso. No, lo cambiamos. ¿Y qué hacía? Era un. Un chatbot, si querés, expuesto al que vos quieras, al público, desde WhatsApp, nuestra web, que lo que vos hacías eran preguntas libres. Lo entendía, tu pregunta la convertía SQL, entendía qué tabla tenía que preguntarle la que nosotros les dábamos, iba, corría la query, se la devolvía, la interpretaba, la convertía a texto y la respuesta exactamente

**Tomas**: lo que queríamos hacer.

**Emilce Terré /BCR**: Y eso lo habían podido. Porque WhatsApp es medio, viste, Problemático con la integración y las difusiones.

**Lucio Rojas**: La verdad que eso, está legacy está antes de que yo entre. No sé cómo lo han hecho, pero sí está productivo hoy por hoy. Pero bueno, lo dejamos un poco en la web anterior. Tendría que preguntar si alguien tiene ganas de resucitarlo para esta nueva, pero la verdad es que no sé si es

**Tomas**: prioridad,

**Lucio Rojas**: pero entiendo perfecto. Nosotros lo que hacíamos es, o lo que hacemos es usar uno de marzo de una. Y los costos 0.01 centésima de dólar por consulta, a veces 0.01, a veces 0.02, depende de la complejidad. No se van al. No se van muy lejos, ¿No?

**Tomas**: También uno de los objetivos de hacer el fine tuning o algo propio es

**Lucio Rojas**: que

**Tomas**: orientar las preguntas más que nada de agro. Entonces como bueno, tener por ahí ese, ¿Cómo decirlo? Esa mayor precisión por el hecho de que nosotros conocemos los datos y conocemos. Qué es lo que puede estar preguntando el usuario cuando hace una pregunta de cómo viene la comercialización de soja, ¿Entendés? Cosas así más.

**Lucio Rojas**: Es que ahí si, te entiendo también, Ahí te responde. Dale, que me hicieron venir a la mente justo un tema.

**Emilce Terré /BCR**: Te hicimos revivir algo del pasado.

**Lucio Rojas**: Tenía una actualización de una base de datos que está usando eso a las 9 y 35. Tenía que ver si anduvo bien o no y me olvidé. Bien, lo que hicimos con el fine tuning, nosotros se lo dimos, nosotros hicimos toda la infra y toda la arquitectura de cómo funcionaba, y se lo liberamos a nuestros usuarios, que serían en este caso ustedes mismos. Y le dimos en nuestra UI una sección de instrucciones, instrucciones generales para el modelo, instrucciones individuales por tabla. Entonces vos ahí podías terminar siendo un MD que se le cargaba al modelo como contexto, explicarle cómo responder al usuario. Es muy gaseoso, muchos casos de uso, pero un compañero le dijo yo soy hincha de Central, si llega a decir que soy hincha de Newell, tratame mal. Y nos divertíamos. Obviamente esto va segmentado para cada uno de los clientes, pero ahí toma el contexto de lo que vos le decís, le bajas todo el lenguaje técnico, por ahí bien de granos de bolsa lo sigue perfecto. Así que después nosotros si querés, podemos darte capaz que alguna o dos horas de consultoría en cómo armarlo, porque lo han hecho los chicos. Después habría que ver si. Si eso se cotiza, se puede hacer y cualquier cosa te ayudamos.

**Tomas**: La verdad que sí. Obviamente con Velum no somos técnicos, venimos de otro palo, somos economistas. Pero bueno, nos interesó bastante la posibilidad, incluso como pensarlo, no sé, en una especie de proyecto final de maestría, ¿Viste?

**Lucio Rojas**: Ah, claro.

**Tomas**: Y una aplicación real, útil para el trabajo y que en definitiva es uno de los objetivos estratégicos de nuestra área.

**Lucio Rojas**: 100%.

**Tomas**: Así que bueno, saber que está la posibilidad nos deja bastante más tranquilos.

**Lucio Rojas**: Si le funciona, después no los vende. Desarrollo. Nosotros hacemos más barato que revisa anterior y la última.

**Ayelen Romano Bazan**: Sí, perdón, quería retomar esa pregunta, pero me interesó la parte de. ¿Y ahora cómo nosotros podríamos acceder a los datos?

**Lucio Rojas**: Bien, en este momento.

**Ayelen Romano Bazan**: Claro, lo que dijeron en la pregunta inicial, si BCR hace este desarrollo del chatbot, ¿A dónde accederías a los datos? Si no es por la API de cloud, ¿A dónde estarían esos datos de información?

**Lucio Rojas**: Sí, al endpoint de Atina, que es el servicio de web donde nosotros, de AWS en realidad nosotros viven las tablas.

**Ayelen Romano Bazan**: OK. Y ahí están todas las tablas, o sea, Silver y Gold.

**Lucio Rojas**: Bronce, Silver y Gold. Están ahí las tres. Es a donde apunta la skill de lectura del MCP. Si vos le haces una pregunta al MCP, decir, mira esta tabla algo. Sí. Vas a ver que a veces te dice, estoy hablando con latino o algo así.

**Ayelen Romano Bazan**: OK. Y ese acceso no generaría ningún inconveniente, digamos. Eso ya lo están haciendo con otros clientes y demás. Ya está contemplado dentro del servicio, digamos.

**Lucio Rojas**: Sí, sí.

**Tomas**: Una pregunta más.

**Emilce Terré /BCR**: Perdón. Y hago una misma sobre esta, pero me apagué la cámara porque también tenemos mal Internet y lo mismo. Uno podría después a lo mejor seleccionar a qué tablas o a qué datos puede acceder esa conexión y no darle acceso a todo, digamos.

**Lucio Rojas**: No sé cómo quedarían ustedes segmentar eso poniendo. Nosotros no lo habíamos resuelto en su momento. En su momento no habíamos resuelto a qué tablas darle acceso al usuario final. Por ejemplo, si nosotros disponibilizamos el bot, ese bot iba a poder ver todas las Go que estén creadas bajo un caso de uso. Si usted hace un caso de uso abierto al público y quieren que un periodista no pueda preguntar lo mismo que algún socio o alguien que. Que tendría que tener otro tipo de acceso. Quizás tengan que crearles roles de usuarios, niveles de usuarios, creo que va por ahí tu pregunta, ¿No?

**Emilce Terré /BCR**: Sí, sí, sí, totalmente. Eso lo que se diría, digamos. Sí, tal cual.

**Lucio Rojas**: Sí, porque ahí sería como vos estás abriendo información a todo el mundo, sería información pública, ahí yo creo que un poco todos deberían poder consultar todo porque si no, no la abriría al público si no puedes dejarla expuesta. Pero a usuarios no.

**Emilce Terré /BCR**: Pero a lo mejor por decir algo, los datos ya trabajados, o sea, le damos acceso, después hay que ver datos que para nosotros son más críticos, pero bueno, las cotizaciones en Chicago están en centavos de dólar por buje y nosotros le permitimos acceder a una donde ya está convertida en dólares por tonelada, que es la unidad de medida que sustenta uso en Argentina, digamos.

**Lucio Rojas**: Para.

**Emilce Terré /BCR**: Entonces como que vos le das una tabla trabajada y no a la cruda, o sea, me imagino que es algo como darle acceso a las Go pero no a cierta Silver.

**Lucio Rojas**: Exacto, sí, esa pregunta, sí vos le das acceso a las tablas que vos querés, serían las Gol. Puede ser una Gol, puede ser dos Gol, No, claro, por eso lo que yo entendí mal es que vos querías que esas dos golpes puedan acceder gente distinta.

**Emilce Terré /BCR**: Bueno, igual lo que dijiste me hizo pensar que quizás que sí nos serviría, digamos, que haya dos tipos de usuarios para el socio darle acceso a más cosas que al no socio, no sé, pero bueno, ni lo pensamos.

**Lucio Rojas**: Ahí lo puedan monetizar.

**Emilce Terré /BCR**: Claro, tal cual. Pedirle de una y ahí pagamos parte de los costos del centavo.

**Lucio Rojas**: Bueno, por ahí lo podemos usar en el. Perfecto.

**Tomas**: Después cuando hacés la implementación y hacés el modelito que hace la conversión de texto a SQL y vos le podés asignar las tablas con el endpoint atina, las tablas exclusivas que consulte, que sean, ponele, no sé, crea un proyecto de Seago para servicios web pública, le pones todas las tablas ahí y le decís, bueno, listo, manejate con estas tablas y que le haces un der que gestione de tal manera y listo. Una cosa.

**Lucio Rojas**: Sí, sí, sí, sería así. Lo que no estoy tan seguro es de que vos cuando le acceso a la tabla, si ya viene con contexto porque va a estar viendo la tabla, habrá que hacer algún trabajo de que nosotros podamos devolverte a vos todos los archivos, los MD de metadata que generamos, pero entiendo que identificarlos y transferirlos.

**Tomas**: Eso medio que una vez que esté estructurado el esquema, pone capaz que le podemos, si no darle contexto a nosotros, más allá de lo metadata del sistema.

**Lucio Rojas**: Yo entiendo que a ustedes lo que les sirve de la herramienta, si no me equivoco, es poder hacer esta parte de cargar mucho Excel sucio, si se quiere, y juntarlos a algunas tablas. Era un poco lo que le dijimos en la primera reunión con Gabriel, si hacemos esto más o menos rápido, entendemos el modelo de datos, armamos las tablas finales, después lo otro es como que le corre por encima y se resuelve. Esto es lo que suele tardar.

**Tomas**: La duda era que si se podía resolver con algún desarrollo propio que corra local para evitar la disparada de costos.

**Lucio Rojas**: Sí, esa era la duda,

**Emilce Terré /BCR**: Sí, los costos de consultar vía cloud o último

**Lucio Rojas**: pago, no, sí, olvídate darle un LM abierto al mundo, por más de que vos se lo ante, capaz que alguno

**Emilce Terré /BCR**: malo nos mete ahí a correr algo que nos hace pregunta todo el tiempo, o sea, no sé, es como demasiado libre.

**Lucio Rojas**: Sí, después tienen que regularlo, porque de afuera capaz que le pueden hacer alguna inyección de SQL, le pueden hacer alguna pregunta.

**Emilce Terré /BCR**: A nosotros nos hace actualmente que, o sea, que scrapean nuestra web para obtener los datos y pasarlos a otras personas que están ofreciendo bases de datos, básicamente. Entonces quizás hacer un sistema de estos le facilitaría a las personas que están eso, que están scrapeando la web, obtenerlo. El punto esto es ofrecérselo al usuario, no sé cómo decir, individual, que quiere saber cuánto cerró la soja y demás, y. ¿Y siento que el mayor consumo va a ser de las personas que bajan nuestros datos diariamente?

**Tomas**: ¿Como cambió mucho el consumo de la información, y cada vez más el usuario quiere consultar lo que quiere consultar y no lo que le dan, viste? Entonces disponibilizar la info para que pueda hacer la consulta que él quiere ver, medio que es hacia dónde va, viste. Incluso hasta dentro de las empresas, cuando no sé desarrollan tablero, bueno, los que desarrollan tableros respecto de los que manejan los datos, es como que vos dame los datos y después yo veo qué hago con eso. Más o menos. No sé si es lo que un

**Lucio Rojas**: poco lo que vendemos, lo que tenemos vendiendo nosotros. Nosotros pensamos muy casi seguros de que esto va a converger en muchos años, en que estamos todos adentro de cloud o el que sea, va a cambiar y va a tener mucho MCP. Y usted como Es más, estaría buenísimo para mí que lo adopten ahora como innovación de ustedes como bolsa. Total, no les cuesta nada. Y para mí sería re novedoso decir, hola, la Bolsa de Comercio tiene su MCP, entra Chloe y pregunta los precio de tal grano, No sé las preguntas. Claro, pero conectado con ustedes, lo que le están haciendo en realidad es darle acceso a esto que ya armaron, y le dan su proyectito a cada persona, y ahí entra y se conecta.

**Emilce Terré /BCR**: Bueno, para mí esas son las cosas hacia dónde va de alguna manera, y que siento que nosotros podemos resolver también. No sé, también en un momento hablábamos de la tecnología blockchain y los que funcionan como oráculos, digamos. Entonces, bueno, si nosotros somos los que generamos esta información, o sea, creo que va a cambiar el rol de lo que nosotros hacemos en los próximos cinco años. Y bueno, el tema es que necesitamos arrancar por tener los datos un poco más limpios, donde resulte esto. Bueno, ese proceso es lo que nos está llevando, o sea, la verdad es que esto es una muestra que no llega ni al 0,1% de la cantidad de datos que tenemos. Y ese proceso que yo le llamo estructurar datos, yo al revés, yo soy economista y cero analista de datos. Este proceso de estructurar datos es lo que nos está de alguna manera la prioridad, digamos, para poder después pensar lo otro.

**Lucio Rojas**: Yo se las dejo, no sé si decir que la Bolsa tiene su MCP para consultar la información, no, estaría también bastante novedoso. Se conecte cada uno de su cuenta de criolla, preguntas como opción paralela, estaría divertido. Y no puedan tocar nada, modificar nada. Volamos porque nos fuimos al. Nos fuimos al extremo. Lo último que a mí me queda más o menos en la cabeza, de lo que estuve viendo cómo lo usaron, está bastante avanzado todo, es. Ver si pudieron llamarse con Claude y generar golds, porque me quedó un poco en la cabeza de que han generado

**Tomas**: las Golden y ahí para, ¿Querés compartir vos, Velu? Para así.

**Belén Maldonado**: Sí, no sé si me va a

**Lucio Rojas**: dar el Internet para compartir conectado el MCP.

**Belén Maldonado**: A mí lo que me pasó, porque yo recién quise crear una tabla, a ver, para, comparto pantalla y si me trabo mucho me dicen. ¿Estoy compartiendo Claud o que? ¿Estoy compartiendo?

**Lucio Rojas**: Sí, está comentando.

**Belén Maldonado**: ¿Están viendo la conexión a Teramond?

**Lucio Rojas**: ¿Está viendo?

**Tomas**: Bienvenido Belu.

**Belén Maldonado**: No, para, estoy componiéndome, Comparto toda la pantalla. Ahí ven. Bueno, a mí lo que me pasó fue esto, yo había creado una tabla de expo y acá le pedí ¿Puedes crear una tabla gol que sea igual pero para impo? Y le pregunté si quería que le diera los pasos, me dijo que no, que la podía inferir de la otra que había hecho y después me dice el proyecto está en el límite de las tablas gold, como que no podía crear más, y bueno, le pedí que elimine una y después dije no, pará, voy a intentar crearla desde Teramond y desde Theramount me dejaba. Entonces le pregunté ¿Estás seguro que no podés crear la tabla Gold de importaciones en la página? Sí puedo. Y me dijo esto, como que no entiendo si las tenemos como a estas tablas como multiplicadas, no entiendo.

**Tomas**: ¿Una hipótesis que se nos ocurría es que como nosotros DJB histórico la usamos para crear luego DJB acumulado y DJB compras? ¿Cuando usas una gold para crear otra gold, la duplica o simplemente es que nosotros la tenemos duplicada y hay que eliminar una cada una?

**Lucio Rojas**: ¿Ustedes no la ven?

**Belén Maldonado**: Duplica, o sea, yo lo veo, yo lo veo así, Yo solo veo esta así.

**Lucio Rojas**: Si tenés cuatro, el tema queda hasta cinco en la quinta, en la quinta se vería.

**Tomas**: Y me acordé de otra cosa que no. Que después preguntamos.

**Lucio Rojas**: A la quinta tabla te da el límite del plan fría de tarta, ahí yo tengo doble duero que la quinta te la. Yo no te dejó ver la quinta. ¿Esa conversación me la puede exportar?

**Belén Maldonado**: ¿Como la exporto ahí con el?

**Lucio Rojas**: ¿Al reenviar? No, yo en el sen.

**Belén Maldonado**: ¿Pero le pongo esta o no?

**Tomas**: Porque eso es dentro de la institución esa.

**Lucio Rojas**: Pasarlo por el chat si querés.

**Emilce Terré /BCR**: Dale.

**Lucio Rojas**: ¿Y desde Teramot lo pudiste crear?

**Tomas**: No, avanzó, pero no

**Belén Maldonado**: me daba la opción de Teramot, o sea.

**Lucio Rojas**: Ahí tengo que pedirte permiso. Lado sin permiso. Creo que es por el de privado que le diste el carácter de privado. ¿Quién está compartiendo era la otra duda?

**Belén Maldonado**: Es el mismo link,

**Tomas**: En uno de los procesos de carga de archivos subimos uno que estaba mal, después de acá lo eliminamos

**Lucio Rojas**: de archivos

**Tomas**: sigue estando como fuente y no supe cómo eliminar.

**Lucio Rojas**: Es un bug mapeado. Listo, ahí lo vamos. El pricing, Lo del pricing en teoría no es. No les debería dejar crear la sexta tabla por el plan. Nosotros tenemos un plan gratuito que hasta la quinta tabla Gol es de cero. Y ahora desde hace una semana, a partir de ya, un plan starter vas a valer 400 dólares. Y así escala hasta el Enterprise. Nosotros estamos en el marco de una prueba de concepto. No tengo bien la rama de si esta prueba de concepto va en paralelo con la de Ayleen, o están bajo el mismo. Está englobada bajo el mismo pricing y lo mismo que acordamos. Eso no sé quién de su lado lo gestiona, supongo que alguien que está en reunión, no sé si Emi puede ser.

**Emilce Terré /BCR**: No, porque me quedé pensando, me imagino que más tipo tesorería, porque yo no estoy nada al tanto de lo que está haciendo Aye, digamos. De lo que está haciendo Aye para el otro proyecto.

**Lucio Rojas**: Son cosas separadas.

**Emilce Terré /BCR**: Claro, pero obviamente haga la misma tesorería, con lo cual a la larga.

**Lucio Rojas**: Sí, sí, pero igual eso yo iba a investigar un poco, porque a mí también en su momento dijeron, bueno, hay que arrancar por acá. Sí, no sé si en algún momento se definió eso de.

**Emilce Terré /BCR**: No, yo de hecho al menos no sé, yo no tengo como aún el presupuesto. Entendí como que bueno, hoy hacíamos esta prueba y después nos van a pasar

**Lucio Rojas**: un presupuesto de la prueba de concepto para ver

**Emilce Terré /BCR**: qué nos proponen como solución a esta necesidad y cuánto costaría.

**Ayelen Romano Bazan**: Claro, ahí de nuestro lado sí teníamos una propuesta de concepto, pero estaba definida la cantidad de tablas, cantidad de GB que podíamos cargar de información y demás, pero estaba contemplado para la prueba de concepto que estábamos haciendo, la que estamos haciendo en paralelo con el laboratorio. Eso sí estaba todo definido.

**Lucio Rojas**: Entonces tenemos que hablar por. No sé si con Emi o con.

**Emilce Terré /BCR**: Aye nos puede contar su experiencia con el otro proyecto, pero me imagino que sí que conmigo no. Aye con el área en sí o con ustedes.

**Ayelen Romano Bazan**: Sí, ahí lo podemos hablar o también hablarlo con Dior, cómo lo manejamos. Pero sí, nosotros en este caso sí tuvimos que firmar una propuesta y una definición de cuántas tablas íbamos a crear y un tiempo de prueba de concepto y demás. Pero lo revisamos.

**Emilce Terré /BCR**: Dale,

**Lucio Rojas**: bueno, listo. Entonces yo llevo eso más al equipo comercial. De nuestro lado, hoy está Juan más, no sé si lo han conocido. Juan Sí, yo sí. Y vemos ahí lo del pricing. Eso ahora pido que lo destraben, así podemos seguir porque si no, no van a poder probar y pues armar puesto

**Ayelen Romano Bazan**: ahí. Yo tengo otra pregunta, perdón. Con respecto a los casos que habíamos hablado de datos que había que normalizar o Excel, que tenían nombres diferentes y demás, no sé si con eso ya se encontraron en alguno de los casos que subieron, lo pudieron corregir.

**Emilce Terré /BCR**: No,

**Tomas**: La verdad que por ahora, como toda esa parte de normalización que pensamos que por ahí va a ser muy compleja como tenemos ahora Claude, Tim, la verdad que la estamos haciendo con eso y no está siendo para nada. Todavía como estamos en este proceso medio de las relaciones esas como key, no sé, relacionar nombres de puertos distintos o que tienen nombres distintos en archivos distintos, no lo hicimos, pero bueno, el enfoque va a ser usar esa herramienta Bien.

**Ayelen Romano Bazan**: Y la idea sería usar la herramienta para hacer las relaciones de más y después guardarlo en la tabla Gold ya relacionado.

**Tomas**: Claro.

**Ayelen Romano Bazan**: OK, bien.

**Tomas**: No sé cuál es la opción óptima. Las tablas Gol, sean tablas que tengan como mucha información toda junta o tener muchas tablas Gol estilo Data Warehouse, consolide la información y después bueno, que las consultas hagan las relaciones.

**Lucio Rojas**: Sí, a veces se han usado alguna primera instancia de Gol para hacer normalización y después en una segunda instancia haces vinculación entre las tablas ya normalizadas, creas una nueva capa si querés de fuente de datos. Con eso nosotros te ayudamos con un bypass de datos, que es lo que te decía que había que hacer, de volver a cargar la tabla segunda instancia de Gol, primera instancia de Gol como fuente, ella es más como un warehouse, te damos esa flexibilidad. Pero te digo la verdad, si vos lo solucionaste con Cloud antes de subirlo, nosotros hasta incluso estamos pensando productizarlo eso, debatiendo esto muy interno nuestro, meter participa más del producto que cuando vos cargas el Excel te deje. Creo que hace eso porque lo resuelve perfecto.

**Tomas**: Sí, sí, o sea, la parte de normalización la verdad que. Y después lo que tener esto, mi duda es esto, tener embarques, ingreso de camiones a las terminales portuarias, tener una tabla de embarque y una tabla de ingreso de camiones Gol, porque como estos son datos diarios o datos semanales, ponele, hay que crear la tabla Gol esa para evitar la carga, que la carga sea de todo el batch de la historia completa, entonces cargar solamente último batch por así decirlo, los últimos datos, que sea más rápido el proceso, pero después crear una segunda tabla Gol que tenga en tal día terminales, embarques e ingreso de camiones. ¿Todo junta o cada una por separado? Y cuando una consulta la relaciona, se hace la relación en el momento. Eso es lo que no me queda duda.

**Lucio Rojas**: Más o menos no terminé de entender. Igual yo tengo la. Estoy superponiendo una reunión de las y media, si querés podemos hacer así. Yo voy a. Siempre tengo un teléfono entre el córner acá que me ayuda a hacer un poco un resumen de todo lo que hablamos. Es un claro con las preguntas y las respuestas y si querés copiamelo en mail ahí con la pregunta y te la respondo durante el día. Y me llevo yo principalmente en la cabeza lo de la cantidad de tablas que estaba dejando generar para solucionarlo rápido. Si podés velo ahí, si no me puedes compartir el link y que funcione.

**Belén Maldonado**: Todavía no funciona porque ahí lo puse público.

**Lucio Rojas**: No me sigue sin pasar. Sigue, pasame los screens nomás. Cuando yo copié el mail, eso que dijo, listo. Y Emil se después yo por lo otro chicos, de ver cómo llegamos el proyecto y eso.

**Emilce Terré /BCR**: Dale, perfecto. Nosotros hablamos con Aye para coordinar con todos los distintos tareas que estamos haciendo con Tela.

**Lucio Rojas**: Aparte igual ya tenemos el alta de proveedor, los NDA ahí, así que otro proceso, hay que ver la cantidad de tablas y de Gol y demás, que en realidad es un recálculo sobre el pressing estándar, pero hecho medida, más las horas de acompañamiento y demás.

**Emilce Terré /BCR**: Bueno, bueno, cuando vos digas nos dice

**Lucio Rojas**: sí eso lo hablamos y después última semana hago una cadena aparte de esos temas para no mezclarlo con la parte operativa, por así decirlo. Dale, perfecto. Bueno, gracias. Perdón Domi que te dejé a gamba con la última consulta. Yo la respondo.
