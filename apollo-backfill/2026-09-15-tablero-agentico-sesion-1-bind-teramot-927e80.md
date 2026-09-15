# Tablero Agentico | Sesion  1 (BIND /Teramot)

**Fecha:** 2026-09-15T13:32:46.442+00:00  
**Duracion:** ~60 min  
**Participantes:** Maria Ximena GONZALEZ <>, Sol Soletti <sol.soletti@teramot.com>, Lucio Rojas <lucio@teramot.com>, Isabel Moreno <imoreno@bind.com.ar>, Juan Peralta <juan@teramot.com>  
**Externos:** imoreno@bind.com.ar  
**Apollo ID:** 6aa95714cf39fc001c927e80

---

**Maria Ximena GONZALEZ**: Me dijo que le de 5 porque está cerrando, Si quieren aprovechemos. Si hay algún tema que nos comentaba, Pero está cerrando algo que le pidió Sebastián.

**Lucio Rojas**: Por ahora todo lo que tengo es sobre tu tablero, sobre lo que fuimos trabajando, supongo que

**Maria Ximena GONZALEZ**: como vean si estamos como listo para la sesión, esperamos Eva y arrancamos ahí

**Sol Soletti**: algo para anotar, ya que lo puedo anotar en la compu.

**Maria Ximena GONZALEZ**: Yo ahora si quieren le doy contexto rápido a Seba de donde estamos para que ustedes puedan ir mencionando

**Juan Peralta**: de paso yo también quería que esté, bueno, Sol me la robé, por ahí va a estar un ratito y después se va, pero para que también conozca Seba al equipo que trabaja en esto.

**Maria Ximena GONZALEZ**: Está perfecto. Perdón que ya estoy con ustedes, tenían ahí medio. Escuchame, aprovecho nada más un tema por si después no podemos hablar ahí estoy tratando de ubicar la FIA, viste, por lo otro, por lo de.

**Lucio Rojas**: Sí,

**Maria Ximena GONZALEZ**: ahí lo que me dijo ella que después regularicemos el tema de la carta oferta, yo le dije, estaba dentro de la ruta nuestra, pero bueno, me levantó el punto, me dice, che con NJ te está faltando una parte, le dije, sí, sí, sí, pero bueno, primamos, me dijo, no, está OK, pero por las dudas para que lo tengamos dentro de la agenda.

**Maria Ximena GONZALEZ**: Bueno,

**Maria Ximena GONZALEZ**: ¿Qué novedades hay en Téramos generales de avances tecnológicos, lo que se viene,

**Juan Peralta**: uff, eso, Beacon, que lo que están usando ustedes es una solución muy potente, después profundizar en cuestiones técnicas, pero

**Maria Ximena GONZALEZ**: lo

**Juan Peralta**: que logramos ahí es hacer algo que si querés no esas se puede desbloquear en infraestructura y esto es de interés en muchas organizaciones donde compartir datos, el modelo por ahí es diciendo, che, no estoy tan acostumbrado, o gran volumen de información, o sea que eso también pasa que es algo que no nos encontramos frecuentemente, pero que hay clientes que lo tienen, entonces muy rápidamente lo pueden proyectar en infraestructura, una máquina virtual de alguna forma y tenerlo corriendo en tu infra y cloud, Agnostic, o sea, sin importar qué nube tengas, o sea, para hoy, antes esta solución era muy importante para nosotros el tema de AWS y hoy en día ya no hay ningún problema, GCP, AWS, OCI? Hola Seba, buen día, ¿Qué tal? Muy bien, muy bien. Ese es el mayor breakthrough, el logro más importante del último tiempo y evoluciona rápido, es más liviano, es mucho más útil que decir, bueno, desconectamos los modelos y te los instalamos en tu infraestructura. Por eso ya era como abrir el código y dejarlo ahí corriendo y era otra cuestión de negocio y etcétera. Ahora quedó. ¿Lo dije bien, Sol? Estuve espectacular.

**Sol Soletti**: Muy bien, muy buena definición, excelente.

**Maria Ximena GONZALEZ**: Bueno, aprovechando, ya que arrancamos con la agenda que teníamos, doy breve contexto y le doy la palabra a Juan para que nos parquemos con el modelo génético. Lu estaba convocada con algo. A ver, Seba, la idea inicial que tenemos con esto es pasar de un modelo, si queremos, más analógico, a un modelo digital y agéntico. Se trabajó todo lo que fue arquitectura hasta la fecha de hoy y ya estamos en condiciones de empezar a generar delivery. Según la última reunión que tuvimos con vos, la idea es armar la célula de trabajo para justamente vos que sos el principal con el foco del consumidor y los constructores que salíamos nosotros en la parte de Theramo, y bueno, vos sos el principal stakeholder junto con Sole, que nos van a dar matices para poder avanzar con esto. Nos llevamos el tema del prototipado que hablamos la otra vez, te vamos a mostrar ahora qué es lo que pudimos lograr a la fecha, y a partir de ahora empieza todo el refinamiento para que veamos realmente y validar, que creo que va a ser importante también para Juan tu expectativa en términos de cómo vamos avanzando con esto. Hasta ahí Juan y te doy la palabra.

**Juan Peralta**: Dale. Bueno, gracias Fer. ¿Bueno, ese es el dónde estamos hoy? Y también algo muy importante, por unos minutitos nos va a ¿Cómo llegamos, cómo fuimos evolucionando? Y ese es un camino interesante. La organización BIM nos presentó unos desafíos importantes, sobre todo en esta última conexión de sistemas, sistemas de mucho volumen, 2000 tablas y eso. Bueno, ahí Sol, que es nuestra ingeniera estrella, que estuvo trabajando en el producto, nos llevó a pensar una solución que se adapte y que pueda trabajar mucho más rápido con una demanda de alto volumen, como era esto, sin estrangular recursos ni de nuestro lado ni desde su lado. Así que ahí creamos una solución nueva en espejo, para lo que es la idea inicial y formal de Theramot, pero mucho más liviana y que trabaja de una manera desconectada, podríamos decirle, y logra el objetivo de tener el contexto sobre bases de datos de gran volumen, como es esta a hoy. Logramos ese objetivo, empezamos a hacer el análisis de datos y empezamos a trabajar con esta migración de todo el proyecto CMI y hoy estamos en la primera iteración. Así que bueno, ahí también fue una presentación de Sol como área de ingeniería, y ahora viene la de Lucio, que es el implementador, la persona que tiene muy en claro cómo llevar, cómo implementar, cómo dejar materializada todo el concepto de Theramot, para que una organización lo pueda usar en diferentes estadios, ya sea desde la parte de ingeniería de datos, como nosotros podemos resolver y trabajar con gente de tecnología, o desde la parte del consumo de negocio, que es lo que hoy vamos a ver, que es la mirada tuya y la mirada del resto del equipo de ICSA, de GIME, que son quienes usan esta herramienta para poder dar solución a esos problemas que a lo mejor hoy tienen en necesidad de información rápidamente sobre todas las cosas que por ahí había procesos que llevaban mucho tiempo. Lo que vas a ver hoy, lo que van a ver todos, es el resultado de una iteración que empezó ayer, hará cuatro de la tarde creo. Mario Lucio terminó sus reuniones y se puso a trabajar para lograr el tablero, o sea, ese primer tablero que vimos de Cmifer, que ahí no sé cómo se llama esta pantalla,

**Maria Ximena GONZALEZ**: Pero es el cuadro de mando integral que tenemos. Y ahí para aclarar se sumó Lu, nuestra agenda comercial técnica.

**Maria Ximena GONZALEZ**: Hola, buen día.

**Maria Ximena GONZALEZ**: Perdona.

**Maria Ximena GONZALEZ**: Hola, hola. Tenemos conectado hoy todo el cor de casi 2000 tablas como Juan, después tenemos el corta y 1 tablas y tenemos todo lo que fue el ecosistema de toda la deuda que ya está versión. De otras fuentes que todavía no están, como puede ser TV Germán y en una segunda. Y a partir de esa fuente es donde empezar a trabajar le para lograr

**Lucio Rojas**: los Ahora solo custom, no tenés custom,

**Maria Ximena GONZALEZ**: tenés Gauss y tenés la base de cobranza. Esos son los tres drivers principales. Y ahí Lucio, te damos la palabra.

**Lucio Rojas**: Dale. Buenas, ¿Cómo andan? Ahí ya me presento Juan, estoy toda la parte de implementaciones. Quiero primero contextualizar un poco lo que vamos a ver. Yo me encuentro ayer con el proyecto, porque vengo trabajando distintos proyectos, y veo que tenemos que copiar la parte de renovaciones del CMI usando Telamot, conectado a las dos mil y pico de tablas, que me da la cuenta sin tener acceso a.

**Maria Ximena GONZALEZ**: Son 2000 tablas, el modelo completo, lo que reportes del código, tengo esto, algo falta. Bueno, el modelo completo son. En principio tenés que bajar todo, después empecemos a cegar, vamos a definir qué vamos a consumir. Pero no tenés manera

**Lucio Rojas**: en las dos olas.

**Maria Ximena GONZALEZ**: Capaz que los códigos de la gente.

**Maria Ximena GONZALEZ**: En realidad vos cuando tenés el modelo de datos conceptual y eso baja la base de datos, Inicialmente como no conoces cuál vas a necesitar, tenés que tener la que tengas, lo que tenemos hoy. Ahora, en base a eso vas a decir che, no necesito la tabla X y vas a poder inversa.

**Lucio Rojas**: Yo creo que sí dijo antes que

**Maria Ximena GONZALEZ**: el desafío era ver cómo

**Maria Ximena GONZALEZ**: hoy no lo podemos presionar, la tabla 1 requiere 10 tablas, la va a necesitar igual, pero no estamos seguros que no va

**Lucio Rojas**: a dar los 2000.

**Maria Ximena GONZALEZ**: Puede ser, pero digamos, en el proceso. Lo hizo. Acá es algo que tuvimos, que es la reingeniería inversa. ¿Vos el modelo lo ves? No, lo que se tomó es traer todo y ahora con la solución de teléfono vos podés entender los esquemas como está. Es muy engorroso todo. Porque eso, todo lo que decís lo entiendo ahora.

**Maria Ximena GONZALEZ**: Juan me dijo, primero fue encontrar una solución para trabajar con un tamaño tan grande de información. Capaz que encontramos.

**Maria Ximena GONZALEZ**: Sí, yo creo que va, pero el desafío que trae Juan es. Creo que ni siquiera en el grupo tienen conectado la base de datos.

**Maria Ximena GONZALEZ**: Eso entendí perfecto. Yo, perdón que soy un.

**Juan Peralta**: No, no, o sea, esto. Y yo te. A ver, parte de esta explicación viene del desafío de la ingeniería que eso implicó y que no quita que la afirmación, o sea, que lo que vos estás comentando vaya a ser cierto, o sea que no necesitemos las 2000 tablas y como bien dice Fer, hoy no lo sabemos. Y otra cosa que es más importante,

**Maria Ximena GONZALEZ**: ya sabemos que no vamos a necesitar

**Lucio Rojas**: las 2000, ya lo sabemos.

**Juan Peralta**: Bueno, pero ahora, y acá te retruco yo, en esa necesidad de información, a lo mejor en esas tablas que quedan por fuera, vos empezás a ver que podés obtener datos que te sirven para tomar decisiones. Y es importante porque nosotros también empujamos un cambio cultural en las organizaciones. Hoy en día todo el mundo está muy encerrado en lo que el sistema te propone, lo que clic te dejaba ver y estabas acá así y de esa forma. Entonces nosotros podemos replicar eso, obviamente, pero también te abrimos la puerta, che, estos

**Lucio Rojas**: son todos tus datos.

**Juan Peralta**: Hoy en la yema de los dedos tenés la posibilidad de empezar a interactuar con eso y encontrar algo qué no lo sé. Es el pensamiento fuera de la café. Exactamente. Esa es la génesis de Telamot, la idea de Bruno decirle che, dale al usuario la oportunidad de hacer lo que se le quiere, lo que quiere con los datos.

**Maria Ximena GONZALEZ**: Le voy a dar un solo ejemplo a Seba, pero para que me entienda la hoy por ejemplo en la unidad de negocios más no vemos el transaccional, monitores, inspecciones, más o menos por la

**Maria Ximena GONZALEZ**: línea

**Maria Ximena GONZALEZ**: qué sería transaccional.

**Maria Ximena GONZALEZ**: Todo el tiempo que están pasando operaciones, los certificados a la base de datos, hay problemas ahí, recurrir al banco, esto nos da potencia. ¿Nosotros directamente a consultar, decirle che, pasando algo, cuántas operaciones? ¿Cómo cuadrar más? Tiene una potencia de ver crudo que antes lo teníamos y vamos a ver más.

**Lucio Rojas**: Adelante, vamos al hueso.

**Maria Ximena GONZALEZ**: Así

**Maria Ximena GONZALEZ**: que se generó y que

**Lucio Rojas**: bueno, termina ahí lo que estaba diciendo, salir bien al grano. Partimos de todo el universo y teníamos que replicar el tablero que estuvieron construyendo ustedes tiempo. Y la potencia de estos modelos que quiero recalcar es la velocidad de iteración. De ayer para hoy replicamos lo que teníamos sobre el universo completo de las tablas, sin ser yo alguien experto en su negocio en sí, que es lo que nosotros traemos como valor con la herramienta. Ahora voy a ir directamente a la foto final, a cuál fue el resultado que tenemos hoy como tablero replicado y una solución agéntica anexa, donde se le puede consultar información en la hoja natural muestro como la torta ya cocinada y después si queremos volver para atrás para ver cómo lo hicimos, me hacen las preguntas y vamos retrotrayéndonos. Así que voy a sentar segundo quiero buscar viendo esta. Ahí ven todos bien,

**Maria Ximena GONZALEZ**: Esto no es Clixen, es el objetivo porque tiene mucho.

**Lucio Rojas**: Esto lo hicimos, lo hice yo de ayer para hoy, conectándonos a la base entera de Gauss y no me acuerdo el nombre de la otra fuente. Lo que hicimos fue replicar, replicar todo el modelo armado de tablas GO y el workout estaba en clics a partir de una ingeniería inversa. Partimos de la foto final y fuimos para atrás, teniendo la transcripción de la reunión y además el binario ahí.

**Maria Ximena GONZALEZ**: Déjame aclararle una cosita a Seba. No solo la base de datos, sino que lo que hicimos es lógica, que fue todo el récord de esos meses que vimos ese archivo de lógica. Se bajó un archivo, si querés. Es el contexto y esa la capacidad para cero con la negociación.

**Maria Ximena GONZALEZ**: Abajo. Se ve que en realidad para esto, por ejemplo, usaste unas 10-12. Ta, entiendo el diagrama que mostraste abajo.

**Lucio Rojas**: Claro, pero yo nunca hubiese sabido cuáles son esas. El modelo la selecciona rápido del Universo porque conoce toda como si fuese la base concreta. Una primera mejora que para mí es sustancial, es que yo la tengo. El detalle de cada una de las columnas que fui calculando en el cuadro planta integral, con una descripción de qué es y cuáles son las reglas de cálculo que tiene atrás, lo fuimos generando con los modelos. Entonces esto te permite chequear rápido un número y poder empezar a entender el porqué de los números que que tenemos detrás. También tenemos implícita las reglas de negocio, que después podemos profundizar, y una aclaración de qué tablas nuevas tuvimos que ir construyendo y de todas las tablas que se fue alimentando para poder armar el tolerante resultado. Tenemos una réplica en una primera instancia de lo que era el cuadro de mantel, con la cantidad de pólizas, primas y comisiones a vencer por mes en formato sábana. Cuáles son las cantidades renovadas, las cantidades no renovadas, y esto es nuevo, que es la cantidad de pólizas pendientes de renovación que antes no estaban calculadas.

**Maria Ximena GONZALEZ**: Aprovechamos para hacer una mejora de lo que hoy veíamos en clic, algo que no se podía lograr, que en la no renovación, lástimamente no renovadas y las

**Lucio Rojas**: que estaban pendientes, hundido el dato y

**Maria Ximena GONZALEZ**: no lo podías desagregar. Ahora sí lo podés desagregar manual.

**Maria Ximena GONZALEZ**: Sí, lo habíamos logrado, pero con clic no se había podido sacar esto.

**Lucio Rojas**: Bueno, tiene detalles como que se puede mostrar en millones.

**Maria Ximena GONZALEZ**: Una pregunta, ponele, voy a enero para tomar un ejemplo. Había 282 países a renovar por 846 pesos. No sé qué es eso.

**Lucio Rojas**: Son millones de pesos. Millones de pesos.

**Maria Ximena GONZALEZ**: 282. ¿Renovaste? 280. Prima que renueva, dice. ¿Está buscando la prima que venció o la prima a la que se renovó?

**Lucio Rojas**: Se puede preguntar esa.

**Maria Ximena GONZALEZ**: Yo podría decirle desde esas 282

**Maria Ximena GONZALEZ**: a

**Maria Ximena GONZALEZ**: cuánta prima se renovaron y ver qué tuvo la prima. Vale, vencí pesos se renovó en 10, qué sé yo.

**Juan Peralta**: Se puede ahí.

**Maria Ximena GONZALEZ**: Perdón, apuntate con eso. Uno de los cambios culturales que creo que va a ser potente para las preguntas. ¿Alguna pregunta tenés vos? La propuesta es tener el tablero como lo veníamos tocando, con información que se va a ir actualizando. Vas a tener la posibilidad, querés hacer un clic con algo, lo que antes hacía, y descargar información. Y eso es un poco, creo que Lucio está ahora demostrándote haciendo eso.

**Juan Peralta**: Ahora, la parte que vamos a empezar a trabajar con el equipo es en este tipo de iteraciones para ajustar conocimientos, ajustar criterios, que el modelo y los agentes entiendan a través de la óptica de ustedes cómo es este negocio. Más allá de que en general entiende el negocio porque lo contextualiza, pero como para que el grupo para BIN sea, no sé, renovación, sea renovación como ustedes lo entienden, más allá de que sea genérico. Esa es la interacción y la dinámica que estamos llevando adelante. Porque como bien lo dijo Bruno Lucio, y también es una premisa nuestra, nosotros no conocemos el modelo de seguro del negocio.

**Maria Ximena GONZALEZ**: De seguro. Claro, obvio, obvio.

**Juan Peralta**: Entonces hay cosas que van a ser iterables. Lo bueno, y que esto lo mencionó Lucio antes, la iteración es violentamente rápida.

**Lucio Rojas**: Ahí termino de mostrar la foto del tablero y después vamos a las preguntas puntuales y ordenamos la exposición. Después, ¿Qué más tenemos para ver? Podemos ver el acumulado en base a los filtros que nosotros vamos eligiendo de las cantidades de pólizas a renovar, las renovadas, el porcentaje de póliza y de prima renovada, las no renovadas, pendientes vencidas. Eso se puede ver siempre por apertura de mes o de año o de tipo de persona. Y acá podemos ir viendo siempre los filtros interactivos que nos van diciendo la cantidad, por ejemplo, de pendientes de renovación que ya están vencidas en junio. Tenemos un segundo gráfico que nos va mostrando la evolución de las renovaciones de póliza. Por ejemplo, vemos que en junio CAE casi al 46% la renovación en póliza, pero esta línea punteada es la póliza decidida, que es sobre el universo que todavía no está pendiente de decisión. Este es un dato que antes faltaba y parecía con el primer KPI que había un decrecimiento muy grande de renovación de pólizas. Y después podemos ver en

**Maria Ximena GONZALEZ**: en plata

**Lucio Rojas**: lo que es la renovación por

**Maria Ximena GONZALEZ**: una pregunta por el tema de tipo moneda, si querés comentar cómo está construido y si te marca una decisión.

**Lucio Rojas**: Ahí lo que hice fue usar la API del Banco Central para convertirlo a dólares, de dólares a pesos, de pesos a dólares, y después tendríamos que tomar una decisión. Ahí yo sé que estaba manejando dos momentos, que era uno el momento de renovación y el otro el momento del cobro. Yo lo tomé el momento de renovación porque no tengo datos el momento del cobro. Y eso puede explicar algunas diferencias.

**Maria Ximena GONZALEZ**: Pasa que acá sí o sí hay que tomar el tipo de cambio al momento de la renovación, porque no sabemos

**Maria Ximena GONZALEZ**: cómo se cobra, fecha, emisión.

**Juan Peralta**: Y esa es también una decisión tecnológica para que todos unifiquemos el criterio. Si vamos a ir por la API del BNA, bueno, la modelamos, la dejamos fija, agregamos el modelo y listo. Todo el mundo que es muy mala la API del BNA, by the way.

**Maria Ximena GONZALEZ**: Igual creo que. Juan, perdona, creo que por lo que

**Maria Ximena GONZALEZ**: hay, Porque al cabo después

**Lucio Rojas**: la consulté por API, la sumé el modelo y la crucé contra la información que ustedes ya tenían para poder calcular la renovación.

**Maria Ximena GONZALEZ**: Perfecto.

**Maria Ximena GONZALEZ**: Yo para bajar la sábana de lo que no renové, charlo con el agente o esto ya está previsto.

**Lucio Rojas**: Ahora vemos esa segunda parte que es súper interesante. Pero vos podés preguntarle la apertura de todo en lenguaje natural a la gente. Por ejemplo, yo de la apertura exacta, esta es una pregunta que me gustaría revisar de por qué había caído la renovación en junio. Me hizo una apertura por mes, por clima, por empresa. Antes de ir a eso, lo último que tenemos es una. Una sábana, una apertura por compañía, vencidas hasta hoy o de año completo. Por ejemplo, yo puedo ver por Allianz cuáles son la cantidad de pólizas vencidas, las no renovadas, las pendientes de vencimiento y las pendientes de vencer. Y lo puedo filtrar por riesgo, por agrupación de NON, que es de seguros generales, produciendo RT, por canal, por tipo de persona, y siempre me va también filtrando el ratio por compañía. Yo puedo ver la cantidad de póliza, pueden ser renovadas, renovadas, los ratios. Y después abajo tengo una apertura a nivel póliza, donde yo puedo filtrar por pendientes o por no renovadas, por agrupación y por mes, las pólizas próximas de vencimiento. Esto también lo está trayendo la base de datos.

**Maria Ximena GONZALEZ**: Yo le puedo pedir todas las pólizas que van a vencer en noviembre, ponele.

**Lucio Rojas**: Sí se lo puedo pedir desde acá directamente,

**Maria Ximena GONZALEZ**: Cómo van a ver cuando ya esté, porque ahora estamos en el Ártico. ¿Cómo vamos a verlo? Vamos a poner en este caso Eva a Lu para usar el tablero. ¿Qué alternativas tenemos?

**Juan Peralta**: Yo te iba a decir, una decisión de arquitectura, de si van a hacer rollout de licencias de Cloud. Si lo podemos implementar a través de Gemini. Viste esa pregunta que quedó en el aire, que como tienen Gemini Enterprise, esto mismo. Nosotros estamos haciendo de Cloud porque es la herramienta que nosotros digamos, el gran LLM que nosotros adoptamos como base de trabajo, como herramienta. En el caso de ustedes sería Gemini.

**Maria Ximena GONZALEZ**: Lo podemos Gemini Cloud, porque igual hay licencias también. Podemos ir por los dos canales.

**Lucio Rojas**: Eso es taxativo.

**Juan Peralta**: Hoy en día el tema de los modelos sube y baja, pero hoy en día Antropic Cloud es el que manda. Se puede implementar de esta forma. Podemos ver a lo mejor, bueno, después diferentes tipos de usuarios.

**Maria Ximena GONZALEZ**: Espera que le vean comentar a Seba. Está armado ahora en un negocio Artifact, que es dentro de Cloud. Lo está haciendo Lucio, después tiene que exponerlo para que lo puedan ver todo. La pregunta es de dónde lo vas a subir, sí desde Cloud. Eso, porque puede ser que alguien lo. Por ejemplo nosotros, no sé, puede ser que alguien lo haga por línea de comando, por Yemina. Hay. Por eso la idea sería definirlo por dónde Cloud. Hay licencias que están y otras que no. Seba tiene, imagino. Ya tenés, porque de hecho me dijiste trabajando Luce la tenemos que dar. Por eso era la parte del proceso. Entonces habrá que generar esa licencia y

**Lucio Rojas**: eso después nos tenemos que poner de acuerdo. Puede ser un Live Artifact donde esto se mantenga actualizándose. Nosotros podemos hostear este mismo dashboard desde Telamo, desde Beacon, y que ellos accedan por un link. Podemos, si quieren levantar alguna web app rápido en Verset, eso se ajuste ahí las opciones. Creo que Fer lo tenemos que definir entre nosotros. Pero son todas viables y rápidas. No tiene una apuesta en producción de tres meses.

**Maria Ximena GONZALEZ**: En principio yo diría la adopción que estábamos teniendo todos. Después veíamos el cómo, si querés. Pero para no infiltrar esto, le sumamos

**Maria Ximena GONZALEZ**: donde tiene cada vencimiento. Yo ya me bajo por día.

**Juan Peralta**: ¿Qué base es la que mencionaba Lu? Eso de Cardera.

**Maria Ximena GONZALEZ**: No tenemos otro reporte que hace Sime, que es venciendo el último mes, pero me lo actualiza todas las semanas, así se va limpiando lo que ya renovamos. Entiendo que es este mismo listado, pero sí me le agrega una lógica de poner quién es el responsable de renovación, que depende por riesgo en algunos casos, por quien se le ejecuta cartera.

**Lucio Rojas**: Eso me suena porque ya lo he trabajado y está bueno también una solución que ofrecemos ahí, que es ver la bolsa de cobradores o de reasignadores y poder reasignar en base a reglas, por si se está salteando alguna cuenta que está asignada distinto. Se puede hacer un montón sobre.

**Juan Peralta**: Qué KPI salen de ese listado, qué métricas buscas.

**Maria Ximena GONZALEZ**: No es un documento bien de trabajo que yo lo que hago lo distribuyo entre todo mi equipo comercial para que cada uno tome sus vencimientos y las gestione. Y hoy dependo de un reporte que genera SIME, que asigna. Entonces, si a esto le sumamos ese criterio de distribución, ya lo podríamos.

**Maria Ximena GONZALEZ**: Todo lo que queramos lo podemos hacer, porque tenemos todo para la base.

**Maria Ximena GONZALEZ**: Agarro la base cruda, la tiro a un cloud y a ver. Y después me vengo autogestionando que es lo que no debería pasar. Un modelo con los vencimientos, con la criticidad, es decir, de 0 a 7 está en rojo, del 7 a 15 está en amarillo, y quién tiene los vencimientos. Esto estaría bueno que ya.

**Maria Ximena GONZALEZ**: Nadie me lo da. Bueno, ahora lo vas a tener. La idea sería que necesitas que esta vista que tenés boca, la traslademos acá.

**Lucio Rojas**: Correcto.

**Maria Ximena GONZALEZ**: No sé si le sacamos una foto y ya está.

**Lucio Rojas**: Ahí muestro un poco las preguntas que le fui haciendo. Acá recién me habían preguntado que te iba a dar todas las pólizas a vencer en noviembre. Se las pedí, fue a verlo a la base y me las trajo. Me trajo las 10 pólizas más grandes también y me dio un. Una hoja de trabajo en Excel para poder descargarlo y verlo. Esto siempre es complementario al dashboard, que es lo que uno ve todos los días. También tiene la posibilidad de preguntar, por ejemplo, esta pregunta a mí me gustó, que fue, y le dije la prima que se renovó. Acá me había mostrado, me había hecho la pregunta de a cuánto se renovaba la prima. También me trajo la prima al final, la prima nueva, la diferencia. Yo acá le hice una pregunta que me gustó, que estaría bueno verla, que le dije Quiero que me expliques en clientes y en negocio la caída de renovaciones de junio. Si yo voy a junio, veo que hay un dato muy particular que pasamos de 96% a 46%. Dije, bueno, vamos a hacer una apertura a eso. Perfecto, tengo todo el detalle de junio.

**Maria Ximena GONZALEZ**: Acá va la apertura.

**Lucio Rojas**: Hay un universo de 925 pólizas con 438 renovadas, 11 no renovadas y 476 pendientes. Este es un dato muy importante que se está destapando al layo anterior. Me dice, vamos a verlo por negocio. Por negocio, Seguros generales, RT están bien y Caución tiene una caída importante. Esto tiene tres lecturas diferentes. Dice, bueno, cauciones del efecto bien seguros que ya conocemos, 564 pólizas, de las cuales 467 están pendientes. Esto no es pérdida, es el vencimiento masivo de cauciones chicas de inseguros que todavía no tienen cargada la renovación. En custom, Cada póliza promedia 34 mil pesos, así que inflan el conteo de pólizas, pero mueven poca prima. Esto es lo que tira abajo el porcentaje de pólizas por cliente. Nos muestra cuáles son los clientes que van venciendo. Me dice que hay un vencimiento importante en siempre me va haciendo una apertura muy grande de cada uno de los datos, mirando la base, incluso podés pedir recomendaciones de negocio, puede siempre hacer un doble clic. Eso para mí es el valor real de la herramienta.

**Maria Ximena GONZALEZ**: Ahora, no tenés limitación en lo que

**Maria Ximena GONZALEZ**: le podés preguntar, son todas las explicaciones, las preguntas que hacemos y que a veces nos está bueno porque va a dejar bien operaciones que no cargan, las operaciones de caución.

**Lucio Rojas**: Y si evolucionamos en el tiempo, lo podemos confutar como alerta. En realidad en el tiempo es cuando nosotros nos deseamos hacerlo. Entonces en vez de ir a buscarlo proactivamente, pasivamente, lo recibís, sentías reglas, si se vence así, de tanto monto, así me avisan. Eso está incluido dentro de la herramienta como una ficha. Después, lo último importante es que el modelo este razona y me va detectando diferencias entre clic, entre lo que yo hice y entre la lógica de lo que debería hacer. Y me va dando avisos de, por ejemplo, las primas y las comisiones en clic estaban infladas por un doble join. Son esas técnicas de datos.

**Maria Ximena GONZALEZ**: A veces había más Lucio, había desvío. Che, este dato no puede ser por ahora directamente el modelo te lo va a inferir y va a empezar a

**Lucio Rojas**: sonar como decía Lucy, me hipotetiza el porqué de eso en datos y me encomienda preguntas para hacer la negocio. Entonces yo me siento con Gmail, veo esta lista de alertas y vamos validando y vamos así mejorando el modelo para que se.

**Maria Ximena GONZALEZ**: Faltaría, o sea, más allá de esto que ahora nos pasaste, que es esta vista que necesitas por días de anticipación

**Maria Ximena GONZALEZ**: cuando lo use voy a verlo.

**Maria Ximena GONZALEZ**: A mí me falta el ejecutivo de cuenta.

**Maria Ximena GONZALEZ**: El ejecutivo de cuenta. El ejecutivo de cuenta.

**Maria Ximena GONZALEZ**: El responsable de renovación está afuera.

**Lucio Rojas**: Bien, un excelente.

**Maria Ximena GONZALEZ**: Está buenísimo que esté cargado en custodia.

**Maria Ximena GONZALEZ**: Hay ciertas decisiones. Tiene que empezar a pasar la operación porque si no el modelo empieza a

**Maria Ximena GONZALEZ**: estar custom o elegimos meterlo en la tabla anexa.

**Maria Ximena GONZALEZ**: No es una opción, tiene que ser en el custom.

**Maria Ximena GONZALEZ**: Yo ayer vi vencimiento que dice Luis Tubio, la empresa hace 7 o 8

**Maria Ximena GONZALEZ**: años no, por eso el campo de reposo no lo usamos, generamos nuevo porque no le impactamos.

**Maria Ximena GONZALEZ**: Hay que impactar en

**Maria Ximena GONZALEZ**: una de las cosas, yo puedo decir que cuatro que yo traje cuando vamos a hablar, es que los cambios tienen que estar en el origen. Si los cambios no están en el origen, es sesgo para el modelo, para cualquier otra cosa. ¿Entonces tiene algún modelo de cambio operativo en cuanto al tratamiento de los datos? Si eso no está, no le podemos sacar el cubo a esto. Entonces a lo que vos decís Lu, puede estar. Tenemos que pasar a empezar a trabajar sobre el core con estas variables. ¿Querés? Esperá, acá lo tenés. No, no, OK, OK, OK.

**Juan Peralta**: Yo quería ver las.

**Maria Ximena GONZALEZ**: Cuánto tiempo nos lleva esto que pasé ahí es la anticuación de las pólizas que tiene Seba y el responsable, por lo menos en la construcción a vista que les pase, pero tienen que hacerlo, no como lo tenés vos en el modelo general y que esté el delivery para que Seba ya por lo menos empiece a darle tratamiento y con lugar.

**Maria Ximena GONZALEZ**: El tema es que el responsable va diferente, ellos pueden tomar.

**Maria Ximena GONZALEZ**: Una de las reglas que propongo es mandatorio es el origen lo que dice, entonces vamos a trabajar en paralelo para que esos datos estén en origen.

**Maria Ximena GONZALEZ**: Nos va a llevar más tiempo, porque tiene razón Seba que lo venimos pidiendo que se impacte, ¿Por qué lo metemos en el medio con la rapidez de este chico?

**Maria Ximena GONZALEZ**: ¿Que habíamos conversado en algún momento, porque sabemos un dolor? No pasa esto. Vos decís Seba, respecto a los dos,

**Maria Ximena GONZALEZ**: Pero esto lo que tenés que hacer es póliza, pisarle el dato de responsable de renovación. Póliza, póliza. ¿Por qué? Porque hay.

**Maria Ximena GONZALEZ**: Toda una regla, no está sencillo como cambiar la sala al cliente va por colis.

**Maria Ximena GONZALEZ**: Claro, yo creo que lo que podemos hacer es bajar cartera vigente, pegarle esta misma regla.

**Maria Ximena GONZALEZ**: Perdón, conceptualmente no hay más bajada, está en el modelo.

**Maria Ximena GONZALEZ**: No, no, pero digo, para poder agarrar

**Maria Ximena GONZALEZ**: y decir che, esto tienen que mejorarlo, o sea vos te tenés que traer la póliza y le pegamos con esta misma regla responsable. El tema es que lo tienen que pegar rápido porque voy a hacer una

**Maria Ximena GONZALEZ**: salvedad y que era parte de lo que dijimos que no va a pasar. Yo voy a garantizar, no podemos hacer cosas que rompen con el tiempo, si después mañana alguien no administra la tabla, si alguien no lo carga en el origen, volvemos a la misma conversación hace años. Entonces si no entrenamos el cambio donde tiene que ser, Seba, con régimen, lo hablamos n veces, no va a pasar, no tenemos una tercera chance.

**Maria Ximena GONZALEZ**: Si no baja lo pego.

**Lucio Rojas**: Y bueno, ahora entonces si querés primer MVP

**Maria Ximena GONZALEZ**: y hacer un MVP chiquitito para verlan.

**Maria Ximena GONZALEZ**: Exacto, paralelo

**Maria Ximena GONZALEZ**: de que ese dato empiece a persistir en el FOR, si no estás en camino, ya lo sabemos, digamos, es parte del proceso. Y desde acá miro Lu y no paran. Y después tenía conversación con Mati, No,

**Maria Ximena GONZALEZ**: que ya lo hicimos una vez, ahora lo tenemos.

**Maria Ximena GONZALEZ**: Antes estabas largo porque te ibas mis para entender, ahora con un solo lenguaje

**Maria Ximena GONZALEZ**: natural le va a decir damos la vuelta.

**Maria Ximena GONZALEZ**: Lo que va a servir es que vas a encontrar una vez que lo impacten cualquier desvío. Hoy tenemos que volver a trabajar toda la cartera pendiente de responsable y si

**Maria Ximena GONZALEZ**: querés pegar el criterio sin asignar y me la manda y se la pido a Mati, pero dejen captarla ahora porque después si no la cartera se mueve y otra vez no pasa.

**Maria Ximena GONZALEZ**: Déjenme para hacer Chicago antes de que me vaya parte de esto.

**Lucio Rojas**: Seba, yo por ahora estoy con eso,

**Maria Ximena GONZALEZ**: te lo entregamos en lo inmediato para que revisar y vamos a empezar a tener daily, vamos a empezar a tener semanales, diarias.

**Maria Ximena GONZALEZ**: Por ahora estamos solo en renovación.

**Maria Ximena GONZALEZ**: No estamos en venta, estamos solo en renovación. Pero ya admite que ya está

**Juan Peralta**: muy rápido. Gracias.

**Lucio Rojas**: Bueno, muy bueno.

**Maria Ximena GONZALEZ**: Acá no con Lu para bajar. Esto último surgió.

**Maria Ximena GONZALEZ**: Igual podría haber ido a festejar, porque es hermoso lo que hicieron, la verdad.

**Maria Ximena GONZALEZ**: Muy lindo, chicos, gracias.

**Lucio Rojas**: Perdón, para entender, ustedes vincular el vencimiento a su cobrador y eso no lo

**Maria Ximena GONZALEZ**: tienen, Se llama ejecutivo de cuenta.

**Lucio Rojas**: Ejecutivo de cuenta. Bien. El sistema por falta de data entry. Pero vos lo tenés en un Excel paralelo o en una tabla paralela donde sí lo tenés curado.

**Maria Ximena GONZALEZ**: Sí, pero no queremos en un momento y discutimos sobre eso, no queremos vivir más tabla. Así que lo que vamos a hacer es poner en el sistema para que lo levantes.

**Maria Ximena GONZALEZ**: Bien.

**Maria Ximena GONZALEZ**: Responsable de renovación ya existe.

**Lucio Rojas**: Si la traes ahí podemos trabajar sobre dos cosas. Lo estructural, lo que dicen ustedes, hay que corregirlo de fondo y cargarlo. Si quieren ir inmediato, me pueden pasar la tabla y yo la vinculo. Si prefieren no hacer eso, para. No,

**Maria Ximena GONZALEZ**: Porque a ver, digo de nuevo lo que decía a Lui veníamos, si nosotros no corregimos de base la data, siempre un día se pincha la tabla, lo que sea, y siempre estamos con el C. Lo que tenemos que hacer es lograr que el dato esté en el origen. Eso por un lado, y va a costar y va a ser duro el camino, pero lo vamos a hacer en el inmediato, que es lo que necesitamos. La tabla equivalencia la armamos, sí no

**Maria Ximena GONZALEZ**: es tabla la fórmula. Si esto lo hiciste en 2 horas, ese if lo resolvés en 30 segundos. Pero después se va a una tabla que.

**Maria Ximena GONZALEZ**: La propuesta. Revisemos los IF, porque por ahí los hice eso, no hay una manera distinta. Llegamos al nuevo resultado, es obvio.

**Juan Peralta**: Esa iteración está buena porque nosotros podemos hacer algo solos y ahí necesitamos el curado del lado de ustedes y lo podemos iterar. Y también la idea es que esto lo vayan incorporando. Es una herramienta. Ese comentario que hice al principio, no vean a Theramot como la pantalla estática del clic. Esto es una herramienta, es construcción. Lucio, pero esto también se puede aprender, se puede luz, el sol, Bueno,

**Lucio Rojas**: se

**Maria Ximena GONZALEZ**: puede incorporar, es la idea.

**Juan Peralta**: Si no te voy a tener que

**Maria Ximena GONZALEZ**: cobrar después lo que le agrega este reporte, pero que después se los comparte Fer, es bueno, la responsación, ¿Que es esto que y la cantidad de días respecto al vencimiento? Como para tener una criticidad de tiempo,

**Maria Ximena GONZALEZ**: Juan, como para ponernos la sábana bien corta en este procesito que estamos y dar visibilidad que a veces lo que De nuevo, cómo los. Esto de la manera simple que entro a Seba para que quede habilitado y.

**Lucio Rojas**: La gente por MCP lo coordinamos para que pueda preguntar. El modelo de datos ya está armado, lo pueden sacar en donde hoy a mí el Artifact me da un poco más de duda, porque si bien podemos armar un live, Artifact tiene que vivir bajo la cuenta empresa de su organización para que lo puedan ver compartido, y a veces Clot es medio inestable con la renovación de datos. Ahí yo lo que trabajaría sería que el CMI viva en termo posteado en la parte esa de dashboard que ustedes vieron. Eso nos tendremos que poner de acuerdo para que sea lo más fidedigno posible a lo que vimos. Creo que ya se puede hacer.

**Sol Soletti**: Sí, básicamente yo ahora justo estoy trabajando en ese mismo Artifact Viva en otra parte que también se va a llamar Artifact, justamente para no tener que hacer esa traducción del Artifact a los tableros. Exacto, va a ser con HTML y con JavaScript, entonces va a ser exactamente el mismo fidedigno, pero va a mantener la actualización de datos, que es lo que nos puede darnos ahora Claude. Básicamente

**Lucio Rojas**: va a ser el mismo,

**Sol Soletti**: igual como lo vieron recién, o sea que

**Maria Ximena GONZALEZ**: estaría

**Sol Soletti**: como vieron ayer, que podían expandir la pantalla y solamente ver el Artifact como un link. Bueno, es eso mismo, solamente compartirle el link a Seba entre ustedes y solamente tienen que tener la cuenta logueada en Tenamot, pero lo pueden ver exactamente igual como se lo mostró.

**Maria Ximena GONZALEZ**: ¿Cuándo estaría esto?

**Sol Soletti**: Hoy y mañana.

**Maria Ximena GONZALEZ**: Ok,

**Lucio Rojas**: Estoy antes del 17.

**Maria Ximena GONZALEZ**: Estamos bien.

**Juan Peralta**: Después tenemos que hablar. Tenemos que hablar nosotros.

**Sol Soletti**: Yo ahora ya lo estoy haciendo, lo estoy armando como da la estructura de Beacon, es fácil de meter, pero ya apenas esté, les mando el link. La idea es, bueno, justamente esta que tengan una organización en Beacon y que la gente que usted. Ustedes no quieren que modifique este tablero, lo pongan como solo lector y eso sería todo. De todas formas, apenas en organización ya te pone como solo lector, así que no habría problema en eso.

**Maria Ximena GONZALEZ**: Y un solo lector igual puede hacer todas las consultas, lo que no puede mover es.

**Lucio Rojas**: Va a tener dos herramientas de trabajo. En una ventana el dashboard que está bajo un link, y en otra ventana cloud. Les pueden preguntar lo que sea de apertura, porque mira, el mismo modelo de datos, yo ahí lo que hice para que me responda mejor es armar un system prompt se llama, que es como que te verticaliza cómo tiene que responderle la persona que está hablando. Entonces para que le hablen lenguaje poco técnico, más de negocio, sobre todo para Seba, yo después se lo comparto y se configura en su club y pregunta. ¿Ahí tiene como las dos cosas?

**Maria Ximena GONZALEZ**: ¿Como para ponernos el plan hoy con qué podemos avanzar? Hoy les pasé el Prin ahí, Juan, que después te lo podemos pasar. Que mencionaban. Si lo podemos hacer hoy, genial, así mañana trabajamos ya disponibilidad y que ya puedan tenerlo.

**Maria Ximena GONZALEZ**: Mes tabla es porque hay clientes nuevos que vamos vendiendo pólizas. Entonces tengo un cliente nuevo, agrego esa tabla, le pongo quién es el ejecutivo de cuentas, yo te paso un estado ahora que va a servir para todo. Si, ese va a ser que no debería. El parche debería ser un lugar donde solo puedo

**Maria Ximena GONZALEZ**: Estos clientes no tienen un cliente asignado.

**Maria Ximena GONZALEZ**: No lo encontré asignado.

**Maria Ximena GONZALEZ**: Lo veo distinto. Para entender lo que vos estás diciendo, es ese cliente donde cambia, qué estás viendo hoy, que es venta.

**Maria Ximena GONZALEZ**: Clientes activos.

**Maria Ximena GONZALEZ**: Clientes activos. La base de cliente existe dentro del modelo. El dato está mal porque no lo cargan, pero si debemos prepararlo ya para que toque como tiene que ser. Digo, en el. ¿Mientras lo hacemos por fuera, como lo mencionamos, y de última la tabla la iremos actualizando, pero después para entender esa tabla, vos la tenés identificada?

**Maria Ximena GONZALEZ**: ¿Tenés algún reporte, tabla, parche? La realidad está de la póliza

**Sol Soletti**: también

**Maria Ximena GONZALEZ**: es cliente, pero acá lo tenés que buscar por cliente, aplicar por póliza dentro de un cliente que maneja lo de ART, lo

**Maria Ximena GONZALEZ**: de.

**Maria Ximena GONZALEZ**: ¿A dónde lo vamos a ir a buscar? A Custom.

**Maria Ximena GONZALEZ**: Ah, no está en Custom. Lo que hoy manejamos por fuera no

**Maria Ximena GONZALEZ**: está porque no lo carga.

**Maria Ximena GONZALEZ**: No, porque es esto que tenemos que modificar. Póliza, póliza.

**Maria Ximena GONZALEZ**: Porque es póliza, pólizA.

**Maria Ximena GONZALEZ**: Está bien, pero operador debería ir póliza, pólisA. En el cor. Entonces en aguanto tiene que estar. Hoy no lo hacemos. Entonces eso es lo que quiero trabajar

**Lucio Rojas**: en 2000 cuando vuelva.

**Maria Ximena GONZALEZ**: Mati, tenemos que volver porque esto ya pasó. Perdón el momento de catarsis. Hace ocho meses nos hicimos la charla, dijimos que lo íbamos a impactar, pero

**Maria Ximena GONZALEZ**: antes de eso ocurrió n veces. Claro, ya hice esto muchas veces de pegarle che, a esto hay que modificarlo

**Maria Ximena GONZALEZ**: y después, o sea hay que hacerlo, pero hay que hacerlo de una vez. Igual me parece bien que los chicos trabajen con el filtro que tenemos.

**Maria Ximena GONZALEZ**: Por ahora mandamos. No me gusta Panche, pero no importa. Por un lado vamos con la tabla esta, les pasamos más detalle, la tabla nexa, como vamos a llamarlo, se hace hoy, tiene que hacer dentro modelo alternativo y después cuando.

**Lucio Rojas**: Los pasos está bien, copiar la tabla que pidieron, dejarlo productivo para que lo tenga Seba. Pero antes de eso, casi bloqueante es poder validar con Gmail el dato, porque si no le vamos a liberar algo que no tiene el dato validado y va a ser para lograr una reunión con ellos para sentarme y amarrarnos un poco ahí

**Maria Ximena GONZALEZ**: manden ya mañana igual

**Maria Ximena GONZALEZ**: dame acceso algo y veo los números, parece más que tira clic es que acceso

**Maria Ximena GONZALEZ**: no te va a poder dar.

**Lucio Rojas**: Bueno, un script, le puedo manejar un acceso,

**Maria Ximena GONZALEZ**: le puedo pasar el cartucho que acabo de mostrar, TIR, el listado de no renovadas y pendientes y lo vemos en dos minutos. Hay alguna seguro que está mal segmentada

**Lucio Rojas**: porque ahí hay

**Maria Ximena GONZALEZ**: una. Yo lo que decía es replicar con todas sus falencias y ahí después, o sea, saber está bien construido.

**Maria Ximena GONZALEZ**: Ahí ya estamos. Ahí está diciendo que no es lo que está hablando acá, no está replicado porque tiene una lógica, no es que

**Maria Ximena GONZALEZ**: ustedes lo hicieron y arreglaron el problema que tenía click yo viste que pusiste que había operaciones que sumaba duplicado, Ahí mismo lo analizó, ahí solucionó el problema que yo ya había dado en clic y nunca me arreglaron y que por eso hago el manual. Abajo

**Lucio Rojas**: un poco con Lucio así, porque

**Maria Ximena GONZALEZ**: ya estamos pasados

**Lucio Rojas**: a dos minutos, estamos justos.

**Maria Ximena GONZALEZ**: Si querés darle, contanos Lucio, qué es lo que vos comentás.

**Lucio Rojas**: Yo si quieren hago esto, les paso a ustedes por el canal de Slack que tenemos, si quieren sumarse o por mail o por WhatsApp, el tablero con las alertas y los números y después pasarme por escrito que era lo que me había pedido la tabla de policía Rosé. Ustedes míralo y si me validan esos datos, yo me animo a soltar lo productivo. De última trabajando experiencia, cuando soltamos esto productivo y no tenemos validado el dato, es como trabajar, así que esa validación,

**Juan Peralta**: esto es bueno para todos, la velocidad que te permite alcanzar es muy adrenalínica y te genera ansiedad de cuándo esto ya se puede hacer rápido y también se puede hacer bien, por eso te lo digo mi amigo Fer, se puede ir muy rápido igual una cosa no va a quitar la otra, o sea, vieron, y esto por eso también se dijo ayer, tuvimos acceso, charlamos un poco y hoy a la mañana está presentado esto, o sea, no hay chance hablar con cualquier consultora, no existe que esto pase, entonces rápido se puede ir. Sí, pero pongámosle,

**Lucio Rojas**: A mí lo que más me preocupa es que yo no tengo el ojo, o sea, para mí ver 844 millones, 200 millones o 3 millones, lo mismo por no tengo el ojo del negocio, que es lo que ustedes quieren, así que me interesa que peguen esa revisada, se los paso y véanlo y con Sol trabajamos en ya ponerlo productivo.

**Maria Ximena GONZALEZ**: Buenísimo.

**Maria Ximena GONZALEZ**: Bueno, hoy cerramos sesión y mañana abro sesión nueva para ver si podemos tener la disponibilidad del tablero y bueno, empezar a integrar Lu se también habilitarle a Sol cuando venga ya la esperemos con el tablero.

**Juan Peralta**: Para ir ganando tiempo si se quieren hacer las cuentas en Teramot, así por la duda que les compartamos un link y le digamos, véanlo ahí.

**Maria Ximena GONZALEZ**: Perdóname, ahí tienen que entrar a Beacon.

**Juan Peralta**: Entramos.

**Sol Soletti**: Sí, sí,

**Maria Ximena GONZALEZ**: Para que se registren.

**Juan Peralta**: Exacto, ya por lo menos tienen la cuenta y bueno pues la agregamos a la organización, hacemos todo lo que hacemos nosotros.

**Maria Ximena GONZALEZ**: Excelente.

**Lucio Rojas**: Después les hace un link. Ahí va. Bueno, igual tiene

**Juan Peralta**: Jime, ¿Está Isa?

**Lucio Rojas**: Ah no está Isa.

**Sol Soletti**: Yo les mando, invite chicos.

**Lucio Rojas**: El comentario para la próxima si pasan la filmación de la reunión. Sí, obvio, me sirve el Transgil también, no solamente yo uso el tranfil para

**Maria Ximena GONZALEZ**: algo que hablando también con Juan, que yo le pedí, es todo ese conocimiento de construcción o desarrollo que vos muy bien hiciste, es algo que para nosotros necesitamos

**Lucio Rojas**: un ratito, yo tengo que enseñárselo

**Maria Ximena GONZALEZ**: y seguramente vamos a algún taller para llevar las buenas prácticas y cómo llegar nosotros a esos resultados, porque si después tenemos el cambio, mejora la idea. Justamente uno de los propósitos es no tener la dependencia, pues si no caemos, lo mismo que nos pasó con el banco,

**Lucio Rojas**: ahí ustedes marquen dos o tres personas que van a estar como encabezadas y yo me junto y hago todo el transfer de knowledge.

**Maria Ximena GONZALEZ**: Dale. Bueno,

**Maria Ximena GONZALEZ**: gracias.

**Maria Ximena GONZALEZ**: Chao. Gracias.
