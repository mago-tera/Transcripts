# Demo Teramot | CIX BCP

**Fecha:** 2026-06-17T20:00:28.504+00:00  
**Duración:** ~43 min  
**Participantes:** Javier Villegas Herrera <jvillegas@bcp.com.pe>, Unknown_participant_600 <>, gabriel maximiliano puertas <>, Ken Hiraoka Tsuchikame <kenhiraoka@bcp.com.pe>, Piero Loyola Saenz <pieroloyola@bcp.com.pe>, Bruno Ruyu - Teramot <>  
**Externos:** jvillegas@bcp.com.pe, kenhiraoka@bcp.com.pe, pieroloyola@bcp.com.pe  
**Apollo ID:** 6a330954a98016000ff424c6

---

**Bruno Ruyu - Teramot**: Hola.

**Piero Loyola Saenz**: Hola.

**Bruno Ruyu - Teramot**: Hola Piero, ¿Qué tal?

**Piero Loyola Saenz**: Les doy el pase a los chicos de terapia. ¿No ingresan? No, todavía no ingresan. Ya les mandé un correo para saber si de repente están teniendo problemas para conectarse. Ahí está Justo. Hola. Hola Bruno, ¿Qué tal?

**Bruno Ruyu - Teramot**: Hola,

**Piero Loyola Saenz**: ¿Qué tal Bruno? Un gusto por su lado. ¿Se une alguien más o arrancamos?

**Bruno Ruyu - Teramot**: Está viendo que en la cita estoy yo y Valentina, que Valentina ya no trabaja más con nosotros y mejor hubiese sido que esté otra persona, pero si me das un segundo. Si no, lo puedo hacer yo sin problemas. Lo único, yo no sé si ustedes me ven, pero yo no veo a nadie.

**Piero Loyola Saenz**: No, no, no te veo y tampoco estamos.

**Bruno Ruyu - Teramot**: Ah, ¿Están con las cámaras en paz ahora?

**Piero Loyola Saenz**: Sí, sí, estábamos esperando.

**Bruno Ruyu - Teramot**: OK. No, bueno, lo puedo hacer yo. La verdad que acá me hago cargo de no haber revisado el invite para asegurar que estaba.

**Piero Loyola Saenz**: Sí, no, raro. Pero tampoco me rebotó el correo de Valentina.

**Bruno Ruyu - Teramot**: A ver si me. Un segundo hablo con Gabriel. Voy a llamar para ser más rápido. Si quiere hacer las demos, que la suele hacer él, yo lo puedo hacer de vuelta, pero prefiero más idónea. Ahí te paso, si podés sumar una persona, te lo paso por acá.

**Piero Loyola Saenz**: Dale. Sí, pásamelo.

**Bruno Ruyu - Teramot**: Que seguro tiene más preparadas las demos para que se gan. No sé si vale la pena que hable un poco del contexto de lo que hace Tedramon. No recuerdo si todos habían estado fácil

**Piero Loyola Saenz**: para ir ganando tiempo. Bueno, te presento. Como te comenté, yo soy parte del equipo de partnership del Centro de Innovación, que nos encargamos de. De hacer este match entre soluciones del ecosistema y poder trabajarlo con áreas internas del banco a través de pilotos. En esta oportunidad estamos con Ken y con Javier. Ellos son parte también del Centro de Innovación, pero están en un área que justamente se encarga de ver toda la parte de operaciones de data, de cómo podemos mejorar algunos procesos con inteligencia artificial. Entonces le presenté la solución y creo que queríamos ahondar un poco más a través de una demo, conocer también cómo han ido trabajando con otras instituciones y por ahí darnos alguna idea de cómo podríamos ir, cómo le podríamos dar una forma de piloto a esto, pero queríamos ahondar un poco más en la misma solución.

**Bruno Ruyu - Teramot**: Buenísimo. Bueno, entonces un gusto, Javier. Básicamente para. Seguramente ya lo vieron, pero para reforzar y también para que me hagan preguntas hasta que empecemos la demo. Como tal vez saben los modelos de lenguaje, los LMS no pueden trabajar directamente conectados a la base de datos y a los sistemas que tiene una empresa, porque básicamente no están diseñados para ellos, no pueden ingestar toda la información, no pueden trabajar sin criterio. La semana pasada Antropic publicó un artículo donde mediante la creación de skills, poniéndole contexto y actualizando metadata, lograron hacer cierta analítica sobre eso. Pero bueno, básicamente en el artículo que ellos mismos publican dicen lo difícil que es el equipo de trabajo que tuvieron que tener muy grande y que requiere todo un mantenimiento constante y que no llegaron a las métricas satisfactorias para poder hacer analítica y poder aprovechar la información. Lo que nosotros decidimos es básicamente, mucho antes que exista Claude, armar, entendiendo que los transformers, los LLMs que bastan, no están entrenados con base de datos, teníamos que armarle la estructura de datos para que puedan consumir. Así que lo que Theramo hace es básicamente disponibilizar un Data Lake House construido a partir de todas las fuentes que uno le carga, que pueden ser de distinto origen, distinta tecnología, y construye ese Data Lake House con estructura Medallion muy rápidamente para que después pueda ser consumida por lo que uno quiera. Eso podría ser consumido por un dashboard tipo Power BI, pero hoy nuestros usuarios que mayor provecho le sacan, lo usan con Cloud o con chatgpt o con cualquier otra AI que tengan un conector MCP, porque esa AI ahora entiende toda la información que tiene, la puede utilizar y puede crear nuevas transformaciones sobre esa información porque construye nuevas tablas en el ATA Lakehouse. No sé si es muy técnico o si fue poco técnico, ahí tal vez es mejor escuchar si quedó claro o si tiene alguna duda. Aprovecho a presentar a Gabriel, el CEO de Telamot, que va a poder preparar una demo seguramente más divertida de

**Piero Loyola Saenz**: tal. Un gusto.

**gabriel maximiliano puertas**: Perdón que entre tarde.

**Bruno Ruyu - Teramot**: No, acá yo les hacía la consulta, si tiene alguna pregunta o fue la verdad una presentación media escueta y no sé si quieren saber algo más o prefieren directamente ir a verlo por mi lado. Hay que ver la demo y ahí

**gabriel maximiliano puertas**: seguro ya me salen unas preguntas bien

**Bruno Ruyu - Teramot**: un poco de contexto, bien técnico y especialmente con data. Entonces si pueden hablar de manera técnica, sin problema. Perfecto. Bueno, mientras Gabriel lo va preparando, digamos, ¿Qué hace Telamo para construir ese ETL, digamos autónomo? Primero uno está conectado a las fuentes, lo que hace es explorar la información, entendiendo que los esquemas, analiza los esquemas, interpreta los esquemas, interpreta las tablas que hay dentro de cada uno e interpreta las columnas que tiene cada una de las tablas. Con eso genera metadata. También corre procesos de identificación de errores y findings de errores, básicamente para poder hacer procesos de limpieza de los datos, uniformizar los formatos de las columnas de fecha en todos lados, para que cuando uno haga el join no haya problema. Generación de categorías, búsqueda de nulls, duplicados, outliers, todo lo que haríamos los data engineers mano, corre procesos autónomos que lo generan. Cuando eso termina, construye, o sea, el modelo de data Lane es un modelo medallion en la capa bronce, ingesta todo, cuando corrió esos procesos de limpieza, construye una capa silver con todas las tablas ya corregidas y después se queda esperando para recibir instrucciones para construir las tablas en la capa gold, que son las tablas que se van a consumir desde Power BI, desde el MCP, vía cloud. Eso para que entiendan un poco mejor técnicamente. Ahora sí, te dejo Gabriel.

**gabriel maximiliano puertas**: Vamos ahí, si me confirman que están todos viendo. Yo creo que sí cuento un poquito. Digamos, nosotros, nuestra solución básica es tipo SaaS, o sea, en la que ustedes entran, se hacen una cuenta en particular, eso sería un workspace en el cual crean proyectos. Yo acá tengo uno que son el que nosotros utilizamos para las demos, donde cada proyecto una vertical de negocio en particular. Si les parece podemos usar esta. Claro. No sé si conocen, este es un dataset público que tiene transacciones así como de un dataset de un banco que es checo. Ahí yo entré en particular la lógica de workspace y project le permite a los owners, nosotros tenemos una lógica de usuarios en la que los owners y los administradores tienen control total como para manejar quién y qué ve cada información, a quién le habilitamos cada proyecto y ese tipo de cosas, que por cuestiones de privacidad interna es súper importante. Bueno, yendo al proyecto, yo acá tengo conectada una base que en particular, este es BigQuery, que tiene cargada, estos son datos sintéticos, que tiene cargada una base de datos con tres, seis, ocho tablas cada una referente al tipo de transacción o lo que se está haciendo. La base de datos es BigQuery. Acá tenemos nosotros, nuestra tecnología nos permite generar, estamos generando continuamente nuevos conectores. Yo elegí BigQuery simplemente porque nada, porque tengo los datos ahí, pero se puede utilizar muchos conectores y vincular muchas fuentes en un mismo proyecto, o sea, la idea de esto sería, no sé, piensen, tengo los transaccionales de un banco, tengo un CRM o algún otro sistema parecido propietario del banco, incluso Google Sheets, ya que hay mucha información todavía que reside ahí. Lo que les contaba Bruno, acá en este caso ya pasó, cada una de las tablas se genera esta ingesta de datos que le decía Bruno, que pasa por un esquema medallion. Acá estamos viendo las mismas tablas que conectamos ya en la capa silver, o sea, acá ya se sanitizaron y ya se generó la metadata necesaria para poder utilizarlo vía un LLM. Nosotros en la solución, nada, ponemos todo lo necesario para hacer un seguimiento de cómo va evolucionando la información, o sea, ponemos la query que va de bronce a silver y así. En esta en particular tuvo algunos casteos y nada, un casteo de fecha. Esto se hace automáticamente, o sea, nosotros no lo hacemos si exponemos lo que los agentes decidieron, decidieron ejecutar. Nada, esto tiene todas las distintas tablas, acá en particular hay dos que están, dos tablas Gol que están hechas, pero la idea es que juntos hagamos una nueva, vamos a hacer. Bueno, una vez que nosotros conectamos la fuente de datos y ya ocurrió ese proceso de sanitización, el siguiente paso es empezar a consumir. La forma que nosotros planteamos como la mejor es consumir vía un conector MCP, que acá para este proyecto nosotros tenemos cargado todas las credenciales, lo que hace falta para generar ese conector MCP, este conector se autentifica con los usuarios del proyecto vía log two, o sea que eso se hace automáticamente y solamente lo pueden usar los usuarios que están autentificados. Yo en particular venía trabajando en otra demo, así que voy a armar un chat nuevo, perdonen que cierro esto. Si yo le muestro acá al conector, ya lo tengo hecho un conector acá que se llama theramo MCP, ese conector tiene, estos son básicamente todas las tools que nosotros ofrecemos al conector. Esto básicamente son tools que te permiten inspeccionar las tablas, eventualmente crear nuevas, hacer previews o

**Bruno Ruyu - Teramot**: una aclaración por cómo habla Gabriel cuando dice te permite, en realidad le permite a Cloud.

**gabriel maximiliano puertas**: Que usa Cloud acá el usuario simplemente nada. Entonces yo le digo, vamos a usar Teramot, MCP, Workspace, Demos. Lo más probable que me diga que hay un Workspace para demos y que tiene varios proyectos. ¿Me va a preguntar qué proyecto? Eso simplemente porque yo tengo habilitado los proyectos. Bueno, entonces sí. That I said, Vamos. Ranking. Acá se está ubicando en el proyecto. Si yo les abro un poco por acá, nada, está usando las tools y ubicándose. Me dice, mira, tenés todas estas tablas. Estas tablas tienen que ver con transacciones tipo, operación, monto, préstamos, cuentas, bueno, todo esto que determina, digamos que tiene acceso Cloud, es básicamente metadata que le generó Theramo. Y en particular de estas tablas son otras tablas, posiblemente otras demos en la que generamos nuevas tablas. Un poco con esto es,

**Bruno Ruyu - Teramot**: Te iba a decir última, si con esta info que ven, se le ocurre algo que parece útil poder hacer o si no preguntar a Claude a ver qué sugiere. Última pregunta. Era Claude.

**gabriel maximiliano puertas**: Acá un poco lo que va a hacer Claude es interpretar lo que yo le pida. Qué sé yo, no sé, quiero correr un análisis de actividad de mis clientes para hacer nuevas ofertas. Lo primero que va a hacer es fijarse si en las tablas que ya tenemos armado no hay algo que ya funcione. Y después va a empezar a entender qué tipo de análisis conviene. Y ahí va a empezar una interacción típica de los LLM. Qué sé yo, le digo, ¿Qué tipo de oferta tenés en mente? ¿No sé, tarjeta de crédito, cómo querés segmentar la actividad?

**Bruno Ruyu - Teramot**: Ambos.

**gabriel maximiliano puertas**: ¿Puedo ir atrás? No, voy con ambos. Ahí va. ¿Querés excluir clientes que ya tengan el producto? Que ya tienen el producto.

**Bruno Ruyu - Teramot**: No mostra todo.

**gabriel maximiliano puertas**: Creo que ahora lo que está haciendo Claude es a partir de las tools que nosotros le ofrecemos, entender cuál es la mejor tabla para generar, para cumplir con eso. Yo le digo, sí, arrancamos, Miren, yo fui medio rápido, pero acá me dice, mi recomendación es incluir a todos los clientes con indicador de tenencia. Podés ofrecerle tarjeta a quienes no tengan ninguna. Ofrecer upgrade, classic, gold, premium. Eso maximiza el alcance de la campaña. ¿Te parece bien ese enfoque? ¿Bueno, me dice qué tablas va a utilizar de la base de datos que yo tenía conectado? Bueno, algunos datos. Acá lo que está haciendo es haciendo algunas validaciones y lanzó a crear una Gol que se llama Actividad clientes oferta tarjeta. Si yo me vengo acá y todo va bien,

**Bruno Ruyu - Teramot**: te tiró el problema de límite.

**gabriel maximiliano puertas**: No me digá.

**Bruno Ruyu - Teramot**: Bueno, yo te activo. Te lo activo.

**gabriel maximiliano puertas**: Vamos así. Sí, borra, borramos. Vos si querés explicarle qué está pasando.

**Bruno Ruyu - Teramot**: El dataset de demo lo tiene en el plan gratuito y se le terminaron las tablas que puede crear.

**gabriel maximiliano puertas**: Y me va a pedir confirmación, porque borrar es fuerte. El protocolo requiere confirmación explícita. Confirmá, confirmo.

**Piero Loyola Saenz**: ¿Hay quien, Fabi, tiene alguna consulta, algo de lo que quieran profundizar o alguna otra funcionalidad que quisieran saber? Si tiene Teramot. La consulta principal que tengo es el

**Bruno Ruyu - Teramot**: tema de seguridad de datos, porque acá en el banco son muy, muy estrictos de dónde podemos poner nuestra data. Buenísimo. Ahí nosotros obviamente, el día uno que empezamos esta compañía en 2021, entendimos que que íbamos a trabajar con datos de empresa. Así que ese día construimos todos sabiendo que íbamos a necesitar la certificación SOC. Ya tenemos, porque tenemos clientes que son Fortune 500 y obviamente están regulados y nos exigen. Dicho eso, Gabriel les dijo, esto puede ser consumido como SaaS. Yo ahí casi interrumpo porque obviamente no les iba a servir como anco. Nosotros lo podemos deployar en un tenant que sea ustedes. Lo que sí, hoy a junio, eso solamente puede ser hecho en AWS. Durante los próximos meses vamos a ir migrándolo también a otras nubes. No sé si ustedes tienen alguna nube particular o son multicloud.

**gabriel maximiliano puertas**: Javier, corrígeme, pero creo que nosotros estamos en Azure.

**Bruno Ruyu - Teramot**: OK, bueno, entonces no es algo que vamos a poder hacer ahora antes de mitad de año. En algún momento del trimestre siguiente seguramente ya pueda ser.

**gabriel maximiliano puertas**: ¿Igual, explorar en su en su tenant de Azure es un requisito o requieren otros requisitos Para cumplir con la normativa?

**Javier Villegas Herrera**: Nuestros datos deben vivir en Azure. Pero igual, como decía Ken, si vamos a alojar otra información, tenemos que pasar varios controles de seguridad para evaluar finalmente el riesgo, la criticidad de la información que va a vivir ahí.

**Bruno Ruyu - Teramot**: Bueno, esto cuando se ploya localmente, básicamente es un tenant de cliente, que básicamente es un servicio más dentro del Azure, un par de servicios más dentro del Azure propio. No hay nada que controlemos nosotros. Es simplemente la orquestación de una serie de herramientas. Es decir, la información no sale nunca de ese tenant, justamente. Y por eso que nosotros lo pudimos resolver, es porque nosotros no le enviamos la información a modelos de AI. No necesitamos hacerlo, de hecho no tendría sentido. Nosotros resolvemos todo localmente en ese tenant donde se corre acá el consumo que Gabriel hace vía cloud, obviamente puede ser por otro, podría ser por copilot 365. Si es el que tienen, si sé que usan. Con lo cual no es que la información se va a estar sacando a algún otro lugar. Es un storage local en el Azure del cliente en este caso. Pero obviamente sí, siempre que trabajamos con empresas grandes, hacemos todos los procesos de auditoría que el CISO requiere. Pero como para explicarlo, esto queda en una nube de ustedes, es como que se lo deployamos a ustedes y nunca sale de ahí. No hay una llamada información externa.

**gabriel maximiliano puertas**: Incluso ayer conectamos este MCP a una infraestructura Azure, es decir, utilizando los modelos que tenían hosteado en esa infraestructura. Así que confirmarle que sirve. Y después el otro tema, nosotros tenemos mucha experiencia con auditorías de clientes que nos auditan la tecnología para validar. Así que nada, eso también se puede hacer, incluso ámbito bancario, financiero. Pero bueno, sigo un poco con la demo. Una vez que libere espacio, digamos, MCP también tiene tools para, si yo tengo los permisos, obvio, tiene tools para ese tipo de gestión, liberar tablas o que ya tenía creadas. Ahí lo que me dice es, bien lanzado, hizo actividad, cliente, oferta, tarjeta. Esto debería aparecer ahora sí, Actividad, cliente, oferta, tarjeta. Esta, fíjense que ya la terminó. Esta es la tabla que nosotros le habíamos pedido. Acá yo tengo un preview y puedo ir a una descripción más profunda de qué es lo que se hizo y cómo se hizo la tabla. Lo que vemos acá es el lineage de las tablas, o sea, qué tablas participaron en ese detalle. Y acá está la query en particular que se generó. Salió bastante larga la query. La idea de esto es poner, como yo les decía, como esto es una herramienta de ingeniería de datos, para nosotros es muy importante exponer qué se hace con los datos en cada paso. Esta sería la query con la que armé esa última. Y esto en particular, porque ustedes habrán notado que esto también lo puede usar una persona que no sea técnica, si entiende lo que quiere hacer y lo puede resolver. Acá un poco hay descripciones que definen esa query. ¿Por qué es importante esto? Porque es como una memoria de cálculo para alguien que no sabe leer la query, pero además tiene una relación directa con esa query. Es decir, si yo cambio alguno de algún parámetro acá, por ejemplo el employment, si cambio una fecha o cambio algún tipo de filtro utilizando este texto también en lenguaje natural y guardo eso, eso va a correr y va a editar la query que generamos. De esta forma, la query que nosotros armamos y esta nueva tabla, que es una tabla Gol, vive en un ETL que es completo, es decir, la fuente de datos, si yo defino la frecuencia con la que actualizo, que esto puede ser horaria, bueno, qué sé yo, con la frecuencia que sea necesario y el horario STL corre y esa última tabla que acabo de crear se actualiza. Y después otra cosa es, digamos, esa tabla se puede seguir consumiendo vía Cloud. Yo ahora lo que puedo hacer acá, decirle OK, OK, armemos un dashboard

**Piero Loyola Saenz**: con

**gabriel maximiliano puertas**: inside y accionables de esa tabla. Mientras Cloud hace su magia, yo lo que les puedo mostrar es la posibilidad de que si ustedes activan esto, pueden, digamos, esa tabla que acabamos de crear vive en un servicio de AWS que es Atina, que digamos en Azure tendría su equivalente y ustedes pueden conectar esa tabla a alguna herramienta de BI. Si ustedes ya tienen dashboard armado o algún servicio que utilice esa tabla, la idea nuestra es que un usuario pueda pegarle a sus datos, los datos de origen a múltiples fuentes de datos, generar tablas o explotar esa información con un entorno que le permita entender esa de alguna forma bycodear pero con ingeniería de datos con con tablas y después consumir esa información. El consumo puede ser, el consumo puede ser vía Cloud o alguna herramienta que requiera. Ahora lo que está haciendo es viendo los preview, validando que está todo bien y va a hacer un dashboard al estilo Cloud.

**Javier Villegas Herrera**: Asumo ya conoce una consultita. Nosotros particularmente en el SIC ya tenemos un Lake House. ¿Esto que tan desacoplable puede ser? Porque si nosotros ya tenemos como que toda esa capa de ingeniería de datos de Gold, de Silver, Gold, todos esos para que esto sea como motor, o sea como que los datos ya lo tenemos trabajados y no sé si el nivel de metadatos que ustedes necesitan para construir, pero sí tenemos como metadatos.

**Bruno Ruyu - Teramot**: No necesitamos, aparte no necesita metadatos. Justamente construye los metadatos.

**gabriel maximiliano puertas**: Igual, contestando tu pregunta, es ideal tener un layout, porque puede ser nuestra fuente de información, si está más prolija, mejor. Lo ideal para los usuarios que consumen eso, que pueden enriquecer eso. No sé si me explico. Posiblemente le haya pasado que el área de marketing, si bien tiene acceso a su Lake House, resulta que hicieron un evento en tal lugar, y le mandan una planilla con todos los usuarios, y ellos quieren vincular esa información. Entonces, nada, ese usuario podría agregar esa planilla o esa información que tiene, y vincular el Lake House con esta otra información y armarse su propio análisis y propias planillas. Se puede utilizar ese Lake House, Como dice Bruno, nosotros construimos la metadata basada en Lake House y eventualmente ustedes la pueden enriquecer.

**Bruno Ruyu - Teramot**: Sí, cuando Gabriel dice nosotros, lo. Claro, no somos nosotros, es Theramon. Esto funciona sin empleados de Theramon.

**Javier Villegas Herrera**: De acuerdo. Mi duda era que nosotros seamos una fuente más, porque tenemos como que todas esas capas limpias, por así decirlo, y. Y en la última capa, generalmente nosotros hacemos todo lo rico que tiene para los negocios dentro del SIX.

**gabriel maximiliano puertas**: Incluso tienen ownership para segmentar qué parte del Lake House puede ver qué persona, digamos. Porque así como tienen reglas externas de privacidad, internamente también es importante ese límite.

**Javier Villegas Herrera**: Sí, sí, sí, lo tenemos ahí, como nuestro layout en realidad es como está segmentado por perfiles, y cada perfil puede acceder a cierto tipo de información, y a partir de ahí se conectan a Power BI para jalar información y tener todo eso. Pero sí, lo que me parece interesante es utilizar estas herramientas tipo Cloud o Copilot, para que hagan todo ese procesamiento, o toda esa capa semántica, por así decirlo, conversacional, para tener otra forma de consumir datos.

**gabriel maximiliano puertas**: Sin duda. Y la verdad que explota mucho a las áreas usuarias, les hace todo el sentido. La verdad que hacen cosas que son muy, muy, muy copadas. Son análisis muy profundos, que uno que es de datos no se imagina porque no está muy metido en el problema, y libera mucho el background, el backlog del área de datos.

**Javier Villegas Herrera**: Y en el caso que nosotros hagamos esta conexión, Perdón que te corté, pero justo tengo un par de minutitos antes del Terátreo. En ese caso que te decía que nosotros somos como una fuente más, ¿Qué implicaría que llevemos que haya un copiado de información por detrás hacia su plataforma, o es solo una conexión y viajan los datos No sé si podrían contarme esa parte?

**Bruno Ruyu - Teramot**: Suponiendo que hacemos el deployment en el Azure de ustedes, ahí podemos aprovechar que ustedes ya tienen la información estructurada y directamente obviarnos. A ver, lo normal es que en la capa bronce se haga el dump de toda la información, porque justamente ahí es donde uno se abstrae de todos los distintos orígenes. Entonces es como, bueno, ustedes lo hicieron, así que saben lo importante de tener las tres capas en el Lake House. Con lo cual lo normal sería ingestar y que esa información esté ahí y que la use para silver. Siendo que ustedes ya lo tienen bien armado y que es una fuente que estaría en el mismo Azure, uno podría armar un proceso que omita la bronce. No veo que sea un problema de fondo, no sé si uno le mete otras fuentes, no sé si medio que hace un lío con eso.

**gabriel maximiliano puertas**: En la infraestructura de ustedes, o sea, nosotros desplozaríamos ahí. Nosotros utilizaríamos algunos servicios de Azure que son serverless, o sea, después los actualizamos vía incrementalidad o haciendo copias, eso no es tan importante. Lo cierto que ahí nos saldría información de su propia infraestructura. Eso me parece que es lo más importante. Como dice Bruno, si los datos están muy sanitizados, es posible que nosotros podríamos ahorrar mucho storage ese deploy.

**Bruno Ruyu - Teramot**: Lo cierto que igual el storage no es lo que hace,

**gabriel maximiliano puertas**: ¿No? Porque nosotros es como que no estamos en la capa de transaccionalidad, entonces es todo serverless. En AWS se utilizan servicios s que

**Bruno Ruyu - Teramot**: son los mismos stores que hay en Azure. Es un storage súper eficiente columnar. Pero sí, ahí se puede ver. Lo estándar sería replicar la información en la bronce, porque si después uno le agrega otras fuentes, lo necesita para conseguir el flujo. Pero se podría ver de no tener que duplicar. Pero la verdad que el storage es barato porque se hace en forma eficiente. Bueno, ahí Gabriel, vos hiciste un.

**gabriel maximiliano puertas**: Ahí está terminando el dashboard. Esto demora un poco más, son los tiempos de cloud, pero esto no lo va a sorprender, es simplemente esta generación de Artifact que funciona muy bien en cloud. Esto en particular se puede compartir. Y nosotros tenemos. Bueno, nada, ahí me hizo unos heatmaps, me estaba dándolo activo. Yo acá lo que siempre me gusta proponer es que recordemos la cantidad de prompts que hicimos, o sea, si no hubiese tenido que borrar las tablas. Básicamente le pedí decime qué hay, me armó este dashboard, un área de negocio, acá me pone accionables, no sé, Oferta Gold inmediata, 200 clientes Upgrade Classic a Gold 110. Bueno, no sé, es posible que siempre nos pasa que este ejemplo en particular termina siendo, qué sé yo, funciona mucho, mucho mejor cuando los usuarios ven sus propios datos. Pero nada, acá le puedo pedir más detalles.

**Bruno Ruyu - Teramot**: Ahí mientras Gabriel lo hacía, yo en paralelo tuve otra conversación donde le dije que arme un modelo Machine learning, o mejor dicho, quedarme el dataset para hacer un modelo de Machine learning de probabilidad de default, y creo que ya lo debe haber terminado. A ver si ya terminó, porque eso, digamos, entiendo como la mayoría de las empresas, los equipos de data que tienen capacidad para hacer data science, suelen ser muy acotados y tiene un scope muy

**gabriel maximiliano puertas**: bajo la tabla que te hizo.

**Bruno Ruyu - Teramot**: Entonces le dije, bueno, si querés comparto yo la conversación que tuve, un segundo. Bueno, acá básicamente le pregunté si podía ver el workspace de check banking, me dijo que sí, me dijo varias cosas, digo, quiero entrenar un modelo Machine learning relevante, ¿Qué podemos hacer? Ahí me dijo un par de cosas, me recomendó el loan default prediction, le dije que haga esa go, me dijo lo que iba a usar, 1, 2, 3, 4, 5, 6. 7, estas 8 tablas de ahí iba a construir todo esto. Me preguntó algo, le dije lo más común, y lo construyó, o sea, mi input fue como mucho una oración y media. Y acá en Teramocha hay un. Está esta tabla que ahora Claude puede consumir. Claude, digo, de vuelta, puede ser cualquiera. Ahí Gabriel le estaba mostrando todo el info, como la unión, y ahora yo puedo venir acá y decirle, capaz que lo tendría que haber hecho en cloud code esto para que sea mejor, pero bueno, me puse a hacerlo en cloud

**gabriel maximiliano puertas**: directamente, le pedí que te haga el.

**Bruno Ruyu - Teramot**: No sé si va por.

**gabriel maximiliano puertas**: Ah, bueno, la cuestión de tiempo,

**Bruno Ruyu - Teramot**: podría haberlo hecho en cloud code y me lo hacía. No, ya está.

**gabriel maximiliano puertas**: Importante de este ejemplo es que digamos, la herramienta se adapta al usuario, digamos, si yo soy alguien de marketing, probablemente que le pida dashboard, pero sin nada, sin una cuestión de ciencia, edad o algo por el estilo, no se achicó,

**Bruno Ruyu - Teramot**: igual lo va a hacer acá para

**gabriel maximiliano puertas**: intentar hacerlo, no te preocupes.

**Piero Loyola Saenz**: Creo que sí nos queda claro cómo funciona Theramo, creo que era lo principal, ver cómo funcionaba, y por ahí seguro Kevin y Javi que se tuvo que retirar a otra reunión. Ahí le van a dar vueltas a cómo le podríamos encontrar alguna utilidad a esto. Muchísimas gracias por el espacio Bruno, Gabriel, sé que queda corto el espacio para todo lo que nos tienen que mostrar, pero nada, hay comercio en la interna con Ken y Javi y de encontrar alguna oportunidad de plotearlo dentro del centro de Innovación, ahí les comento si es que agendamos un segundo espacio. Pero nada, muchísimas gracias por por este espacio. No sé qué si quieres comentar algo más o si no cerramos la reunión.

**Bruno Ruyu - Teramot**: Está muy bueno, me parece muy interesante. De repente ahí ya lo conversamos a la interna, pero podríamos evaluar con el equipo riesgos de hacer un piloto con cierta data, data aislada que nos permitan ir a hacerlo.

**gabriel maximiliano puertas**: Y ese, te digo más, ese piloto, si ustedes anonimizan los datos y se pasa a poder compartir, nosotros lo ayudamos, pero se puede hacer con el tile free y lo pueden probar y explotar todo.

**Piero Loyola Saenz**: Justo eso le querías consultar Bruno, si es que ustedes tenían algún tipo de pricing o algún esquema para pilotos, que me imagino que sí, porque sé que ustedes ya han trabajado con con grandes empresas, entonces me imagino que ya han trabajado este esquema de piloto primero.

**Bruno Ruyu - Teramot**: Entonces solo para confirmar sí lo tenemos, mientras te comparto pantalla. Lo que decía Gabriel es muy interesante porque nosotros, porque Theramot permite que vos si le cargas una base de datos, no necesitas cargarle todas las tablas, ni siquiera todas las columnas de cada tabla. Si hay una tabla en la cual hay información confidencial que no te sirve para querés, no la cargas y nunca llega tela. Entonces no se puede hacer. Y nosotros generalmente, o sea, tenemos un tier que es gratuito, que normalmente esto para un piloto sobra, entonces es como que nada, hasta lo podrían hacer sin nosotros. Si no quieren entran acá, se hacen la cuenta y lo usan hoy en la tarde. Obviamente preferimos darle una mano a empresas, sobre todo grandes, porque entendemos que ahí maximizamos la chance de éxito, porque los acompañamos y les mostramos realmente el potencial. Así que de vuelta, si hoy quieren lo pueden usar sin avisarnos, si prefieren probarlo con nosotros, nos avisan y los acompañamos, que suele ser más eficiente. ¿Pero ya está definido la prueba gratis o Piero?

**gabriel maximiliano puertas**: Si, de repente vos decís, che mirá, me interesa, quiero hacer una prueba, pero si le quiero dar, no sé, a 10 usuarios y para hacerlo rápido, para no entrar en una lógica de proveedores o cosas por el estilo, nos avisa, lo hacemos que funcione y nada, eso. El tiempo y la disponibilidad de la herramienta está, así que si lo necesitan usar, entramos en contacto.

**Piero Loyola Saenz**: Buenísimo, buenísimo. Creo que nos queda súper claro. Nada, Bruno Gabriel, muchísimas gracias por por su tiempo y ahí me dio la tarea de revisarla con Ken, con Javi. Muchísimas gracias.

**Javier Villegas Herrera**: Excelente.

**Bruno Ruyu - Teramot**: Muchas gracias. Chau, hasta luego.
