# Meeting with Bruno 60 min (Andrés Rabinovich)

**Fecha:** 2026-09-08T17:00:37.105+00:00  
**Duracion:** ~62 min  
**Participantes:** Bruno Ruyu <bruno@teramot.com>, Andrés Rabinovich <arabinovich@calice.ai>, Lucio Rojas <lucio@teramot.com>  
**Externos:** arabinovich@calice.ai  
**Apollo ID:** 6aa04de219211a001079df35

---

**Bruno Ruyu**: Your toll was definitely. Predictivos.

**Bruno Ruyu**: Habría que agarrar uno de los demos, eso de transacción, el de Apple, de

**Bruno Ruyu**: comptar la próxima campaña y analítica. Entró.

**Andrés Rabinovich**: Buenas.

**Bruno Ruyu**: Buenas. ¿Cómo va?

**Andrés Rabinovich**: ¿Cómo está

**Bruno Ruyu**: cámara?

**Bruno Ruyu**: Nos está cortando.

**Bruno Ruyu**: Sí,

**Andrés Rabinovich**: sí, sí, los veo, los veo.

**Bruno Ruyu**: Ah, buenísimo. Bueno, ¿Cómo andás Andrés? Bueno, acá Bruno.

**Andrés Rabinovich**: ¿Todo bien? ¿Cómo está Bruno?

**Bruno Ruyu**: Y conmigo acá está Gabriel con. Adelante Lucio,

**Bruno Ruyu**: abajo de la cámara.

**Andrés Rabinovich**: Sí, sí, a Lucio no se.

**Bruno Ruyu**: Bueno, buenísimo que nos pudimos juntar a mostrarte un poco la herramienta. Es algo que yo siempre supe que en algún momento podía ser de utilidad para lo que hacían ustedes. No me queda claro exactamente. Cómo charlando el otro día junto a Miro, creo que entendí dónde podría haber valor en particular con aparte de generar los datasets o armar los datasets, tanto para exponer resultados como para entrenar modelos. Así que no sé, Figuer, vos, porque vos lo va a explicar mejor. Le querés explicar a Lucio y a Gabriel lo que hacen, así ellos también pueden pensar cómo te muestran las cosas en línea. Apuntado eso.

**Andrés Rabinovich**: Dale, dale, dale. Bueno, nosotros así a grandes rasgos lo que hacemos es lo que se llaman ensayos virtuales, en lugar de lo que son ensayos a campo. Nosotros trabajamos para el agro, gran parte de lo que hace el agro es lo que se llama desarrollo de productos nuevos. Imagínense un maíz que quieren, una empresa de maíz que quiere poner maíces a campo, que rindan más, que le saque más rendimiento por. Por plantita. Entonces para poder hacer ese proceso, lo que hacen en general es tener un montón de plantas distintas, digamos, lo que serían como distintas familias de plantitas, todas de maíz, pero distintas como familias. Siembran todas y ven cuáles dan los mejores rendimientos y se quedan con esa. Si hacen una selección, lo que sería por la selección natural de Darwin, pero artificial, se quedan con las plantas que mejor funcionan.

**Bruno Ruyu**: El problema de ese. Que se morfó una campaña.

**Andrés Rabinovich**: Exactamente, o sea, tenés una campaña entera y esto además lo tiene que repetir varias veces porque fue un año particularmente bueno que hizo que alguna de las plantas fuera buena, pero si lo prueban al año siguiente, no. Entonces esto es un proceso que se repite muchas veces, se repite cinco, seis, siete campañas, hasta que finalmente tienen un material que sale a comercial que lo

**Bruno Ruyu**: hacen en una parte del campo.

**Andrés Rabinovich**: Hay de todo, hay lo que se llaman ensayos de micro parcela, que agarran un campo, lo seccionan, hacen parcelitas chiquitas, de poco área, y ahí prueban cada material. Y después cuando tienen que hacer ensayos a campo más grandes, usan más parte del campo, aparte tienen que hacer réplica, bueno, hay como todo un montón de complejidades logísticas. ¿Me dan un segundito? Un segundito, Voy a poner los auriculares porque hay un poco de ruido.

**Bruno Ruyu**: Acá

**Bruno Ruyu**: se escucha perfecto.

**Andrés Rabinovich**: Ahí está, ahí se escucha mejor. Tengo menos ruido.

**Bruno Ruyu**: Se escuchaba bien igual, pero bueno.

**Andrés Rabinovich**: Bueno, genial. Bueno, entonces básicamente lo que hacemos nosotros es acelerar ese proceso con lo que serían ensayos virtuales, en lugar de que vayan a campo a ensayar los materiales, hacemos nosotros los ensayos insílico, digamos, y los ayudamos generalmente a tomar decisiones más asertivas frente a los materiales que van avanzando a cada etapa del proceso. Entonces un pipeline típico de trabajo es que un cliente nos da datos de ensayos pasados, porque generalmente necesitamos, cada cliente tiene lo que se llama su germoplasma, que es el conjunto de variedades que ellos tienen y que son las que podrían llegar a ensayar, Nos dan de ese germoplasma ensayos del pasado, hechos en distintos lugares y distintos momentos, los resultados de esos ensayos, y con eso nosotros lo metemos en los modelos y hacemos los ensayos virtuales, los ayudamos a ser más asertivos. Ese proceso tiene un montón de etapas, y hay un montón de etapas que a veces son un poco manuales, por ejemplo, que estaría buenísimo automatizar, no sé qué habló Rama con vos Bruno, respecto qué se le ocurría a él que podíamos hacer sinergia ahí, pero a mí se me ocurre un poco esas etapas más manuales que tenemos, a ver si se puede automatizar algo de forma genética.

**Bruno Ruyu**: Claro, por lo que vos contás, uno de los, no sé, digo, yo aventuraría que uno de los problemas que vos recibís datos de ensayo pasado, en la forma en que las personas y los vicios te los mandas a limpiar, organizar, filtrar, Puede ser. Y en base en qué, o sea, la gente, me siento tentado a decirle gringo, pero no es efectivo sino porque obviamente tengo familiares que andan en ese rubro, pero digo, ellos, ¿Qué te pasa en Excel?

**Andrés Rabinovich**: Sí hay de todo, Me han pasado un dump de un SQL Server y no te dice nada, te dice toma, acaba la data punto back.

**Bruno Ruyu**: Claro, porque esperá, hablando de esto de los gringos, los clientes tuyos son clientes grandes, porque esto obviamente es para alguien que.

**Andrés Rabinovich**: Hay de todo, hay de todo, nosotros apuntamos más a clientes grandes, pero aunque sea un cliente grande, igual te puede pasar la data en un formato random. Pero pongamos que en general son Excel,

**Bruno Ruyu**: y ahí el tema de los Excel

**Bruno Ruyu**: un poco a mí me cayó la ficha el otro día cuando me contó Rami programa con las empresas que ya estaban ahí metiéndose en Estados Unidos, que eran monstruos grandes, dije bueno, pará, nunca había entendido bien ese perfil usuario, pero bueno, esto aplica a todos. Y como dice, si te tiran un punto bat, es el mejor escenario para teore, es cuando mejor funciona, entiende las cosas. Pero también agarramos Excel, CSV y Google Sheets, y lo que hace ahí es, en la práctica, el producto final va a ser un Data Lake House para construir data. Vos le pones todos esos orígenes y va a ser primero un proceso de interpretación de qué encuentra en cada lugar, mirando, si fuese una base de datos, va a mirar los esquemas, va a mirar las tablas, va a mirar cada columna, para nadie es lo mismo, de alguna forma, sin esquema obviamente, y va a interpretar la información de cada columna y va a correr procesos para entender

**Bruno Ruyu**: si tiene que hacer alguna limpieza de

**Bruno Ruyu**: datos y va a escribir metadata sobre lo que encontró. Con eso estructura la capa, o sea, obviamente la primera capa es el RAW, la segunda capa es la que ya está limpia, normalizada y con metadata. Y después digamos, ahí si querés termina la primer parte que es Data Engineering más inicial, limpieza de normalización y metadata interpretación. Y después lo que hace la segunda parte, que ahí nada, hay que ver de qué forma les puedo agregar valor, si es que le agrega, es con un conector UCP, un agente empieza a poder construir tablas en algún punto, lo que hace es construir tablas a partir de esa información y las tablas pueden usarse para lo que quieras usar. Algo tan básico como alimentar dashboards también, hacer dashboards.

**Bruno Ruyu**: Ahora hace un poquito lo que tengo

**Bruno Ruyu**: que definir dashboard,

**Bruno Ruyu**: y lo estamos usando

**Bruno Ruyu**: en algunos proyectos para hacer modelos predictivos con Cloud Code, diciéndole a theramos que le arme un dataset. Cloud Code entrena modelos, o sea usa Python para poner distintos modelos, ve los resultados, le pide un nuevo dataset, y así empiezan a iterar hasta converger algo que le convence y todo se transforma en un pipeline alimentado. Es decir, no es un one shot, después otra vez tenés que volver a hacerlo mañana o tenés un nuevo Excel y vuelve a empezar. No quedó un pipeline posta en la nube. Si mañana le querés agregar nueva info, le agregas y se construye on topo lo que ya estaba, se anexa y se utiliza. Y las tablas que quedaron en la layer final, las tablas calculadas, también sirve como input para otras tablas, con lo cual todo lo que va construyendo va ir armando un castillo cada vez más grande y más complejo, que la complejidad obviamente correlaciona con el valor que agrega.

**Bruno Ruyu**: Andrés yo por la duda me acuerdo de ver, capaz que no sea así, pero cuando vos decís te mandan datos en Excel, nos pusiste muy contentos cuando hablaste que te hicieron un DAT,

**Bruno Ruyu**: pero

**Bruno Ruyu**: digo, en el Excel puede ser que esté el campo dibujado en la celda y te pongan valores ahí. Nosotros eso no lo procesamos digamos. Claro, claro, procesamos tablas. Bueno, pero Clau. No, bueno, pero eso a él no le agrega valor, digo. No, no, Chat, si nosotros lo hacemos con Cloud, él también lo puede hacer con Cloud.

**Andrés Rabinovich**: No, en general las tablas son tablas razonables, Hemos tenido clientes, pero fue muy inicial, que eran clientes muy chicos que tenían unos Excel que eran cualquier cosa. La verdad que los Excel que nos mandan más fácil o más difícil, pero son tablas, son cosas razonables.

**Bruno Ruyu**: Identifica una semilla, una campaña, todo lo que ustedes hagan.

**Andrés Rabinovich**: Tal cual, tal cual. Lo que tenemos, uno de los problemas principales que tenemos es que nosotros le decimos tiny data a lo que manejamos, es como lo opuesto de Big Data, porque no es que son millones de registros y Excel volumen, por ahí es un excel que tiene 10-12 columnas y tenés 50 filas, 100 filas del excel y aparte cada cliente tiene que estar compartimentado, no se puede compartir información entre clientes, entonces es como que no podés aprender de cada cliente para engrosar una gran base de datos que después lo usas vos. Eso no se puede hacer.

**Bruno Ruyu**: No se puede por las cuestiones que ustedes firman tipo NDA o no se puede porque no tiene sentido.

**Andrés Rabinovich**: Ambas cosas, ambas cosas, o sea, por un lado sí. Generalmente se firma algo donde decís bueno, vos no vas a usar la información de tu cliente para entrenar modelos que después le sirvan a otro cliente que es el competidor. Entonces desde ahí tenemos una limitación, pero ya de por sí como son Germoplasmas distintos. ¿Y bueno, entonces

**Bruno Ruyu**: Andrés, ahí había nombrado como que uno de los procesos que vos hacías antes de correr tus modelos, entiendo que ya están definidos, son manuales, te dolían? ¿Cuáles son esos procesos? ¿Quién los hace? Porque por ahí es donde puede llegar a ayudarte.

**Andrés Rabinovich**: Bueno, son procesos típicos, exploración y limpieza de datos de cualquier proceso de Machine Learning o Data Science. Lo primero que tenemos que hacer es familiarizarnos con el dataset. Lo suele hacer alguien del equipo, lo hago yo, lo hace alguna de las otras personas, porque muchas veces nos regalan un dataset que ellos lo entienden perfecto, pero nosotros nunca lo vimos. No sabemos qué es lo que no sabemos, qué son los campos, que son los nombres de los campos, no sabemos las unidades en las que están las cosas. Por ejemplo, generalmente trabajamos con el rendimiento. El rendimiento es como lo más interesante de una planta. A veces el rendimiento te dice, no sé, 100 qué quinta, claro, quintales, kilogramos por hectárea, qué sé yo. Entonces hay todo un proceso ahí medio manual, de entender el dataset, de agarrarle feeling antes de poder pasárselo a los modelos de limpieza de datos de campos repetidos. Un ejemplo que nos pasó hace poco, tenían un tercio del dataset, eran campos duplicados, eran filas duplicadas. El tipo que lo hizo, hizo mal el join en la base de datos y. Y había datos que estaban como promediados, que no tenían que estar promediados, también se equivocó ahí. Bueno, qué sé yo, ese tipo de cosas. Hay que ver si un cloth te lo detecta, si un modelito,

**Bruno Ruyu**: ese tipo de cosas. Nosotros sí, claro, yo le tenía miedo a un Excel chiquitito, que esté súper agregado, tenga comentarios, tenga el dibujito, o

**Andrés Rabinovich**: sea, puede ser, pero en general es una tablita. Supongamos que es una tablita razonable, todo

**Bruno Ruyu**: eso que dijiste, no me imagino por qué no podría. El estándar de lo que hace, hacen cosas incluso más complejas, te puede tirar hasta liars para decir, che, acá porque el flaco escribió mal algo. Eso lo podemos habilitar o no habilitar.

**Bruno Ruyu**: Incluso vos le podrías, digamos, cómo funciona todo lo que te contó Bruno, vos ingestás los datos y después la última capa la armas con un agente. ¿Como se lo conectas a Cloud? ¿Le conectas Theramot a Cloud o a ChatGPT? Nosotros como vendemos eso normalmente en una empresa, le decimos, bueno, vos si necesitas un flujo de caja, qué sé yo, se lo mandas. Pero vos podrías armar como una especie de agente que sea especialista en llevar esos datos al esquema donde ustedes ingestan los datos ya curados, que sepa qué tiene que validar, qué no tiene que validar, que te haga un reporte y nada, cosa para preguntarle al cliente eventualmente que el flaco no lo supo hacer. Eso va a andar muy bien, porque vos le explicás, lo que termina haciendo Theramo es orquestando las herramientas para que un LLM pueda ejecutar todas esas operaciones de análisis, EDA, JOINS, lo que sea, incluso aplicar criterio y obtener resultados. Porque es una tabla, o vos eventualmente decís, bueno, mirá, no, hay cosas que yo no puedo asumir que son de una forma, las tengo que preguntar. Y automatizás eso, automatizá directamente la lista de preguntas que le tenés que decir, che, en este campo decime si son quintales kilo por no sé qué, o sacame estas dudas y el flaco te la responde y vos aceleraste. Claro, creo que por ahí va como

**Bruno Ruyu**: piña para ir a lo concreto. Yo creo que te puede servir mucho en ese primer paso, te digo porque a mí me pasa seguido y realmente me dedico a ver los datos que no tienen que ir un D y armar reportes en el día, y eso te va a acelerar mucho el paso previo a correr tus modelos, modelos predictivos, que has marcado el reporte para que

**Bruno Ruyu**: corra,

**Bruno Ruyu**: básicamente te tiras el backup, explícame cuáles son los tipos de datos, qué es un PÁBLA, cómo se relacionan, para no mender si querés y si tengo que correr este modelo, necesito un reporte que tenga estas características y el propio plot te lo da nosotros ahí vas a ir muy rápido. Y esos procesos digitales manuales,

**Bruno Ruyu**: yo lo que digo que en el modelo de negocio de ellos, ellos tienen que poder agarrar cualquier dato que le mande el cliente y esos datos llevarlo a una tabla específica que el input del modelo que sigue para ellos es así, Andrés.

**Andrés Rabinovich**: Claro, claro, claro.

**Bruno Ruyu**: Es como un agente que tiene que ser experto en llevarlo a ese formato. Después te lo queda. Aceleraste. ¿Che, y la última parte del proceso de usted cómo entregan? ¿Entregan un reporte o ellos?

**Andrés Rabinovich**: Y eso depende un poco del cliente, siempre es un reporte en PDF de lo que se fue haciendo, de los findings, de los resultados, también es un Excel, porque en general es como bueno, haceme recomendaciones sobre el germoplasma, entonces se le hace un Excel con las recomendaciones. Generalmente los modelos generan índices. Que son indicativos de cuán bueno o cuán malo es un germoplasma y todo eso va en Excel y muchas veces son dashboards y herramientas más interactivas cuando el cliente quiere poder interactuar un poco más y lavar un poco más. ¿Pero eso depende mucho del cliente

**Bruno Ruyu**: y el modelo de ustedes, porque yo me lo imagino ustedes como un input de datos, después vienen ustedes que hacen la inteligencia y el delivery, ese delivery de lo que sale de ustedes también, o sea antes de mostrárselo al cliente para ustedes que? ¿Un set de datos también?

**Andrés Rabinovich**: Claro, claro, sí lo podemos sacar en Excel o bueno, lo que venga que es un parquet o bueno, no sé.

**Bruno Ruyu**: Claro, porque nosotros una cosa que hicimos que funciona muy bien con estos clientes, cuando vos utilizas Cloud, el que más lo tiene es Cloud que te arma estos HTML que son como Dashboard, nosotros los hosteamos eso dashboard, o sea, Cloud te lo arma pero vos lo podés mantener actualizado en Teramor, entonces básicamente lo que creaste es un dashboard y eso como pata de delivery funciona muy bien, incluso podrías hacerlo interactivo, que lo consuma un cliente, que lo consuma vía Cloud, consig. Esas interacciones creo que está bueno, o sea, por ahí lo mejor podríamos hacer. Ahí seguimos con Lucio y nada, hacemos una prueba, o sea, si ustedes tienen un set de datos y lo quieren ofuscar o lo que sea, y hacemos una prueba de esto, digamos.

**Andrés Rabinovich**: OK, bueno, un tema que tenemos también por confidencialidad es que no le podemos revolear un set de datos a Cloud. ¿Básicamente?

**Bruno Ruyu**: Se lo pidieron o lo pusieron ustedes

**Andrés Rabinovich**: como en general lo piden. ¿Ni a Claude ni ningún que sea open source, digamos?

**Bruno Ruyu**: Mirá, lo que hace, nosotros lo que hacemos con Terabot es, nosotros no le revoleamos el set de datos, porque imagínate,

**Bruno Ruyu**: tenemos una empresa con 74 mil tablas de SAP, 15 años,

**Bruno Ruyu**: pero digo, independientemente si se pudiese, tampoco lo hacemos por la cuestión de privacidad. Lo que hace Teramot es, le revolea si querés a Claude un set de herramientas para que genere código y haga cosas, y Metadata es como le dice, mirá, tenía a disposición este set de tabla, esta tabla tiene los clientes, en esta tabla tiene la renta las columnas se ven así, asá. Lo que sí hay intercambio es si vos le decís, no sé, decime cómo van las ventas de enero. Flaco, va a ser una query exploratoria, la agrupa y te va a decir, venís vendiendo de esta forma. Eso sí se intercambia con Theramo.

**Bruno Ruyu**: Pero, y ojo que lo importante es, si bien que lo usas Cloud va por el MCP que como por la API, con lo cual está protegido, viaja encriptado, ellos no lo pueden usar por nada, estarían metiendo en el juicio más grande de la historia si de golpe hacen lo que no tienen que hacer, que es distinto a que si vos lo arrastrás o lo cargas directo a la versión web. Pero como dice Adrián, no es que no va toda la información SQL.

**Bruno Ruyu**: Básicamente lo usamos a Cloud para que genere el código SQL que después nosotros ejecutamos, si falla algo le decimos che, hiciste mal esto, entonces corrige. Y ese tipo explicado muy básico, pero digo, no sé si eso ahí sirve. Vos si conectás los datos en Teramot, datos que dan en tu cuenta de Teramot en AWS, creado una especie de DAM, se ejecuta sobre eso, tanto la fuente de datos, como los pasos intermedios, como los resultados. Lo que sí eventualmente, o sea, hay forma de, si vos querés hacerlo manual, pero no termina siendo muy productivo. Pero digo, si vos querés, como si fuese bytecodear con SQL, lo haces vía Cloud, pero no estás intercambiando las bases de datos. Nosotros esa cosa se la explicamos a nuestro cliente, las empresas lo terminan entendiendo. Es como decir, bueno, este ejemplo que yo te doy, decime cómo vendí en agosto. Y bueno, te va a decir, vendiste tantas unidades, qué sé yo, no sé. Eso sí fue y vino con Clor, pero vos no le pasaste toda la base de datos. Un poco la idea.

**Bruno Ruyu**: Y una más, si el cliente picante es grande y tiene guita, se puede hacer que corra en una nube propia de ellos, con modelos que corren ahí adentro para que no salga nunca.

**Bruno Ruyu**: Eso se puede hacer, obviamente hay que

**Bruno Ruyu**: cobrarle ese deployment, pero bueno, nada, tampoco es una locura, algo se puede hacer, no es inviable tampoco que hay que cobrarle mucho, pero bueno, tiene ese laburito

**Bruno Ruyu**: porque va a haber que hacer un deploy ahí. El otro. Lado te dijo Harry. Y también tenemos una gente que no usa Cloud, sino que usa la API de Cloud más en NCT. Entonces los datos nunca terminan productivamente en cloud, sino que usamos la API internamente y está embebido nuestro Saxo también. Interrumpí yo

**Bruno Ruyu**: no André. Así que por eso. Si vos. Digamos, ustedes lo que podrían. No sé, nosotros para mí la forma de probar el producto con datos que te hagan sentido. Nosotros ahora metemos. Tenemos datos de demo, ninguno del agro en particular, tenemos un cliente del agro, pero no tenemos datos como para poder hacerte una demo, no de estas de

**Bruno Ruyu**: macro broker que vende.

**Andrés Rabinovich**: Bueno, yo le podría pasar algunos datos que son sintéticos, pero basados en datos reales.

**Bruno Ruyu**: Si tenés las tres y tenés los datos, lo hacemos ahora a vivo. Pero si está complicado y lo preferís en otro momento, hace otro momento.

**Bruno Ruyu**: No, sobre todo por los sintéticos, capaz que tienen que hacer.

**Bruno Ruyu**: Ah, no, claro, tenés que hacerlo. No, olvídate entonces. No, hacelo tranquilo.

**Andrés Rabinovich**: Bueno, dale, dale, dale. Sí les puedo pasar eso y vemos

**Bruno Ruyu**: igual ahí metemos una col. Y lo hacemos ahí en vivo. Porque la onda es que ustedes entiendan la herramienta. Nosotros no hacemos consultoría.

**Andrés Rabinovich**: A ver, yo por ahí tengo. Claro, por ahí tengo algunos datos. Un segundito. Y por ahí, a ver si los tengo por acá. Tengo algunos ensayos sintéticos. Por ejemplo, esto es una base de datos. Pasa. Bueno, no tiene conocimiento de dominio, qué sé yo. A ver, se los paso.

**Bruno Ruyu**: No pase, no pase. Compartino y de última te guiamos. No sé dónde está, pero compartimos.

**Andrés Rabinovich**: ¿Pero cómo hago? ¿Les comparto?

**Bruno Ruyu**: Decía que nos comparta la pantalla.

**Andrés Rabinovich**: Dale, Así funciona. Y los puedo. Los pongo en otra pantalla. Si, los veo.

**Bruno Ruyu**: Y eso cada. Si, vos navega. Las hojas son medio parecidas. Las hojas del Excel.

**Andrés Rabinovich**: Un segundito.

**Bruno Ruyu**: Claro.

**Andrés Rabinovich**: Entonces esto es. Este por ejemplo es una base de datos. Esto nos revolvieron un DAM de SQL Server. Son datos sintéticos, así que no hay. No hay nada real acá. Pero la estructura sí, es la misma estructura. Entonces, por ejemplo, Este sería como la tabla principal, que es cada uno de las parcelitas que se sembró. Y cuánto fue el resultado, cuál fue el rendimiento.

**Bruno Ruyu**: Si querés podés entrar por el browser a. Entrar a nuestro WhatsApp. Y vamos a cargarlo a ver si funciona y ya lo dejamos hablando y probando con vos.

**Bruno Ruyu**: Claro. Se jugó aquel, amigo.

**Bruno Ruyu**: Estamos en un nivel de riesgo infinito. ¿Desde lejos, viendo cómo lo hacemos, asumimos, Asumimos así de confiado estamos o no?

**Bruno Ruyu**: Antes de venir.

**Bruno Ruyu**: Laburar con la densidad. Esto es básicamente vos para crearte bola uras por Workspace, Workplace son unidades individuales y dentro de los Workpace voy a tener más proyectos así que le da con el Your Workpace.

**Bruno Ruyu**: Sí, sí, es un tutorial de una suerte de Outlook Morph. Si queréis tutorial es para tu watch, si querés lo podes cerrar. Total estás con nosotros que somos un poco de tutorial en vivo. Ahí tenés la clara para cerrar a la derecha abajo donde está es una guía que te pueden contar, solo lo hacemos después.

**Andrés Rabinovich**: Les quería preguntar sobre el SOC que nosotros también queremos certificar. No, Soc hizo 27001. También le quería preguntar cómo le fue con este proceso, si costó, pero bueno pues les mandé esa consulta ahí.

**Bruno Ruyu**: Sí tenemos un equipo, un área que se dedicó a certificarlo.

**Bruno Ruyu**: Sí, o sea ustedes también tienen que

**Andrés Rabinovich**: certificar SOC y vamos a certificar ISO más que SOC, pero bueno, supongo que

**Bruno Ruyu**: son procesos, la idea era que ir por ahí, pero bueno, dale, metele a BLO que ahora conversamos un ratito porque demora un toque. Y ahí tirar el XLS que nos mostraste un descargo.

**Andrés Rabinovich**: En Excel. Bueno sí, en Excel porque tiene varias hojas.

**Bruno Ruyu**: Perdón, no te escuchamos, yo te interrumpí y te hablé encima.

**Bruno Ruyu**: Ahí va, ahí lo viste, ensayo continuo. Ahí lo que está haciendo lo subió y ahora hay una parte que analiza. Yo esperaría que cada una de las hojas te la suba como una fuente. No, no, digo porque depende un poco de la estructura del Excel. No lo vi entero. Y ahí publish.

**Bruno Ruyu**: Y ahora esto va a llevar un rato porque ahí están la gente haciendo su tarea digamos, viendo que hay, interpretando, corriendo algunos procesito para detectar cosas que tiene que corregir y bueno lleva. Lo loco es que si tiene 20 filas o 20 millones casi que tarda lo mismo porque va pasando columna por columna, entonces depende más de la cantidad de tablas y columnas que del volumen que tengan cargado.

**Andrés Rabinovich**: ¿Y por ejemplo acá cómo maneja el conocimiento de dominio? Y mira, este campo es el rendimiento, que es lo más importante. OK, listo. En este caso se llama weight, pero en otro se llama yield y en otro se llama kilogramo barra.

**Bruno Ruyu**: Ha mirá, algunas cosas las va a poder manejar sol porque se llama y los modelos saben que es y ya lo tienen claro. Dicho eso, ahí al costadito a la izquierda tenés Sources, Data Studio, Dashboards y Knowledge. En Knowledge es donde va a empezar a recopilarse el conocimiento. Hay dos formas de hacerlo, yo no conozco a nadie que haya hecho la segunda. La primera es desde Cloud o ChatGPT o el Agent, vas hablando y le va diciendo bueno guarda esto, Knowledge, o esto es importante, dejalo en Knowledge y es el agent el que lo escribe. Pero vos podrías entrar ahora y escribir si querés, en general medio que escribí, ya nadie escribe, pero podrías crear un documento o incluso subirle un archivo con cosas que ya tengas definidas vos, y eso se transforma en conocimiento para todo el proyecto. Así que cualquiera que use el proyecto o cualquier agente que use el proyecto van a tener en su prompt, digamos, el conocimiento este para que sea uniforme y consistente. ¿Vas a otro proyecto, hay otro Knowledge

**Andrés Rabinovich**: distinto, un presente es un workspace, no?

**Bruno Ruyu**: El workspace, ahí entramos en discusiones que yo he tenido mucho. Un workspace es más para una empresa

**Bruno Ruyu**: sería, como que vos tenés tu workspace y cada proyecto son distintas fuentes de datos que te dieron distinto cliente, Cada

**Bruno Ruyu**: source es un proyecto, cada combinación de source y knowledge y tablas.

**Bruno Ruyu**: Ahí aclaro, no necesariamente cargar una source en un proyecto distinto, vos podés tener mucha source dentro de un proyecto, otros excels, otros servers, distintos proyectos. Hace sentido cuando vos tenés que administrar por ejemplo, roles adentro de una empresa, que querés que ciertas áreas vean una parte de información y otras no, entonces vas compartiendo de un proyecto a otro distintas causas. Si vos querés separar a nivel tenancy las distintas fuentes que vas cargando, para que sea imposible que se crucen los datos de esos clientes, tenés que abrir distintos workspaces. Un workspace es una unidad y se subdivide en proyectos. Si vos querés separar clientes tenés que separar words.

**Andrés Rabinovich**: Claro.

**Bruno Ruyu**: Y va a poder ver todos tus proyectos.

**Bruno Ruyu**: ¿Vos no le das a tus clientes teheron, lo usas vos, digamos, o sea, a vos no te molesta mirar de varios clientes o sí?

**Andrés Rabinovich**: Sí, sí, es una buena pregunta. Bueno, no sé, no sé,

**Bruno Ruyu**: el día de mañana el valor para dárselo

**Bruno Ruyu**: si querés, para ir generando tiempo. Podemos conectar Telamo a CLOC mientras termina de.

**Bruno Ruyu**: Para que uses vos, no sé vos sí Cloud Cloud.

**Bruno Ruyu**: Digamos, si haces con clock desktop sirve para.

**Andrés Rabinovich**: No tengo cloud desktop, tengo uso online. Lo mismo

**Bruno Ruyu**: tenés una URL de servidor server URL si querés copiarla y con eso nos vamos a Plot directamente.

**Bruno Ruyu**: ¿Ahora lo que está haciendo con los archivos, lo que nos escala en el tiempo es que vos tenías muchas hojas, viste eso que te dije? Es como depende cada hoja va a ser una tabla individual. A nosotros nos escala en el tiempo porque tenemos que analizar hoja por hoja. Pero ahora termina. En un minuto debería terminar. Yo lo estoy viendo acá. No es que estoy haciendo el gurú, digamos,

**Bruno Ruyu**: un poco y un poco. Y si querés proyectarnos, nosotros seguimos viendo. Si querés ahí

**Bruno Ruyu**: si hace clic en

**Bruno Ruyu**: Andrés abajo y usa Settings. Ahí puedes ir a.

**Andrés Rabinovich**: Y los conectores deberían estar acá directamente.

**Bruno Ruyu**: Ahí termina el archivo, pero termina esto

**Bruno Ruyu**: que agregar un lector web, si quieres nombre Telamo o podes renombrarnos como quiera. Continuar si querés. Y son las dos de arriba. Final. Y ahora toca App y te va a ganar.

**Bruno Ruyu**: Ahora tenés que ir a Connect. Ahora tenés que ir al conector y ponerle Connect, me parece. De admin. Creo que ahora tienes que ir como en tu usuario Customize y abrir un chat.

**Bruno Ruyu**: Por eso te digo, los chicos de Cloud cambian esto todos los días, ¿No?

**Bruno Ruyu**: El tercero hay una mini barra izquierda,

**Bruno Ruyu**: el de arriba. Puso indebido el inglés.

**Bruno Ruyu**: Y ahora pueden ir a un chat

**Bruno Ruyu**: y pedirle que pruebe terapia. Encontré el conector conectado.

**Bruno Ruyu**: Ahí dice Connectors. Debería aparecer. Te va a hacer clic.

**Bruno Ruyu**: Dale a probar Disconnect. Para mí meterle Disconnect y volverme a editar.

**Bruno Ruyu**: Si a veces no lo encuentra.

**Bruno Ruyu**: Lo que estamos intentando hacer es que te lleve a tu login de Teramot y valide que vos sos vos, digamos, para que pueda acceder a esa email. Ahí probable que pruebe de vuelta, ¿No? Puede que le esté pasando. ¿No tenés otro pop up o una pantalla abierta en otro? ¿El buscador o algo por el estilo?

**Andrés Rabinovich**: ¿No?

**Bruno Ruyu**: Ahí está listo tu Workspace. Ahí está. Ahí está, sí. Decile.

**Bruno Ruyu**: Que envíe tu Workspace, ¿No?

**Bruno Ruyu**: Ya empezá a decirle lo que necesitas.

**Bruno Ruyu**: Te haga un EDA de la tabla que cargaste y te explique qué tablas tiene, qué tipo de cosas. Si querés cambiar el modelo, pueda subir un poco mejor.

**Bruno Ruyu**: No le gasté los tokens encima. Carol, muchacho, ponele pago.

**Bruno Ruyu**: Lo podemos gestionar desde donde estabas ayer en revista de conectores, si querés volver ahí.

**Bruno Ruyu**: Nada, deja.

**Bruno Ruyu**: Bueno, te explico lo que quería hacer.

**Bruno Ruyu**: Podés darle permiso para siempre son los

**Bruno Ruyu**: tools y que no te preocupes.

**Andrés Rabinovich**: Y ahí le puse.

**Bruno Ruyu**: Bueno y ahí estamos en tus manos, porque los datos no tenemos ni idea, te tiene que hacer sentido a vos, digamos, Deberíamos mostrarle enteramos cómo le armó el Data Studio, cómo están los cosas.

**Bruno Ruyu**: Si querés podés pedirle acá una pregunta buena, decirle yo necesito correr tal modelo, qué golpe de nuestro interno, para que usar tu dato,

**Bruno Ruyu**: Yo tengo duda. Esperá, hace un favor, volvé a te yo te quiero mostrar qué pasó con tus datos, digamos, para que entiendes, Mira, anda a ese lugar que dice Data Studio, o sea, vos llegaste, ya cargaste una base de datos, abrir ahí

**Bruno Ruyu**: nosotros

**Bruno Ruyu**: laburamos con un esquema tipo medalla, vos lo que cargaste son bronces, esas bronces pueden ser las que quieras, puede ser una base de datos, un Excel, combinaciones, todas esas tablas te la va a llevar a una capa silver con proceso de sanitización que ya ocurrieron. Eso es interesante que vos lo veas, porque nada, para ver qué hizo con tus datos, si vos abrís ese abril, debería haber 10, hay 10 tablas, eso debería coincidir exactamente con cada una de las hojas que tenía tu Excel. Si vos apretás en una de esas vas a poder ver, no sé, eso ahí es una descripción de qué es lo que encontró en esa tabla y esa query SQL es lo que hizo para llevarlo de los datos crudos bronce, podés expandir ahí, poder expandir y la ver un poco más, ahí podemos ver qué le hizo. Nosotros esto no lo manejamos, no sabemos qué hizo, porque básicamente nuestros agentes analizan esos datos y dicen uy, acá tengo que, no sé, ahí está casteando valores, posiblemente trate de sanitizar fechas o cosas por el estilo. Si vos te vas a la segunda columna que es el esquema, vas a tener una descripción de qué interpreta que tiene cada columna. Esto obviamente vos lo viste, no lo escribimos y ahí un poco lo que vos preguntabas, pero cómo interpreta cada cosa sobre esto podés, tenés cierta injerencia, después vemos cómo si eventualmente hay algo mal, lo podés cambiar. Bueno, el último es, si querés ver la tabla en sí, el preview ese, cuando vos conectaste Cloud Claude tiene acceso a todas estas silver, él entiende esa metadata que vos generaste, si se lo preguntás específico, hasta podés saber qué tipo de transformación hizo para pasarlo de bronce a silver, y a partir de esto vos podés construir. Entonces ahí viene lo que vos necesitas hacer de lo que vos nos contaste, vos decís, bueno, a ver, quiero llevar estos datos a tal formato o quiero hacer tal cosa. Él va a empezar a hacer los joins entre capa silver para cumplir con lo que vos decís. Esos resultados van a ser tablas gold, que la vas a ver acá con la misma lógica. Va a ver de qué tabla vino, cuál fue la query SQL que se hizo, dónde está. Eventualmente la podés bajar. Es un poco lo que pasó con tus datos en ese tiempito.

**Bruno Ruyu**: ¿Cuando termine de repasar toda la parte

**Bruno Ruyu**: de la metadata y preguntarle qué tablas

**Bruno Ruyu**: nuevas puedo construir a partir del set de datos que tengo? Si es algo más esperativo o si vos querés algo más puntual de que ya sabes que cernó esa data, también se lo puede decir. Y acá Cloud se va a encargar más de ir construyendo las nuevas tablas o las nuevas vistas que. Así que ahí lo dejamos en las manos. No sé si quería hacerlo más exploratorio, ya tenía algo en mente.

**Bruno Ruyu**: Me gustó.

**Andrés Rabinovich**: A ver si lo saca.

**Bruno Ruyu**: Está muy bien. Si querés, mientras lo va haciendo, desplegale eso y te muestro lo que. Porque por el tema de desplegar, ahí donde dice mapping, bueno, dale, OK. Y te mostramos un poquito cada una de estas son tools que Cloud puede usar de las herramientas que les pone Telamo. Entonces, eso que te diga, fíjate, por ejemplo, está haciendo query, exploratoria, ese tipo de cosas. Acá te hizo un gráfico. Vos eventualmente este gráfico lo podés. Si vos tuvieses un conector que se actualiza, podría hostear este gráfico y que se mantenga actualizado en la medida que va a actualizar los datos. No sé si el gráfico está bien o no.

**Bruno Ruyu**: Y después cuando termine le puede decir, dejalo todo como un dashboard entero. Normalmente ya queda hecho y actualizado. Vende tu Excel, está.

**Bruno Ruyu**: André, ¿Ustedes qué vistas arman para correr los modelos? ¿Cruzan la información?

**Andrés Rabinovich**: Usamos para. Los modelos están pre entrenados. La información de cliente no se usa para entrenarlos, sino que los pasamos por ahí, salvo que haya que tweakear algo. Alguna vez nos pidieron que estuviera más ajustadito a algo.

**Bruno Ruyu**: Pero tenés que preparar alguna tabla puntual para eso.

**Bruno Ruyu**: Claro, claro.

**Bruno Ruyu**: Podrías pedir que ya lo genere.

**Andrés Rabinovich**: Lo deje generar

**Bruno Ruyu**: como CCB si querés y borrar modelo. Si tu modelo borra doble.

**Andrés Rabinovich**: ¿Sigo un poco confundido de cómo hace Cloud esto sin leer los datos o los está leyendo?

**Bruno Ruyu**: No, mira, abrí ese. ¿Que está haciendo? Abrítese ese, desplegarlo, Fíjate, abrí en ese preview table que dice ahí, lo que él hizo es, nosotros le dejamos así una query exploratoria y se trae ese set de datos. Esos datos que están ahí, sí los conoce, Si vos vas a ver otro, no sé, resalt alguno de esos, son queries que Claude. Claude le dice a che, correcta query y tráeme los resultados. Y así él va interpretando de esa forma, para después nada, ver cómo te arma la gráfica. Vos le pediste un boxplot, seguramente esos valores son agrupaciones que él va armando para armar gráfico. Creo que está haciendo eso. Lo que vos le pedís,

**Andrés Rabinovich**: o sea, a ver si entendí, Claude pide un preview de las tablas como para entender la estructura, arma los queries, hace un select, o sea, usa esos query.

**Bruno Ruyu**: A mí lo que. Lo que me gusta explicar, no inventamos nada análisis de datos, lo que nosotros hacemos es automatizar ese proceso o dar las herramientas a un LLM para que pueda laburar como ingeniero de datos tuyo, que vos lo puedas bycodear, que es lo que está haciendo ahora. Entonces, ¿Qué hace? Si vos le pedís un pibe, le decís, che, necesito que armemos un boxplot de esto, los flacos tienen que poner a ver qué son las tablas, cuáles son los nulos, analizar, no sé cómo quedan los bigotes del box plot, cómo queda la. Todo eso está haciendo Cloud, está haciendo todo eso con herramientas genéricas que nosotros le damos y te arma ese tipo de gráfico. Lo bueno que tiene Cloud, tiene muchos criterios, o sea, funciona obviamente mucho mejor que lo que podría llegar a ser un analista de datos estándar, porque conoce más del campo que cualquier otro analista conoce Internet. Entonces ese tipo de análisis va a ser muy bueno y más si lo utiliza alguien como que sabe interpretar. Vos capaz que mirá un valor de eso y decís, no, acá hay algo raro. Si se lo decís, él va a investigar y posiblemente muy rápido encuentre un tema.

**Andrés Rabinovich**: Está buenísimo.

**Bruno Ruyu**: Incluso lo que yo hago a veces, bueno, fíjate todas las infos que hay, mi objetivo es tal, dime que hay

**Bruno Ruyu**: que hacer, qué me sugería hacer.

**Bruno Ruyu**: Eso vale un montón, porque puede traer ideas, pero tal vez no se tuvieron. Es más, le planteás objetivo, dejá de

**Bruno Ruyu**: pedirle tareas ahí Andrés hay un detalle, vos hasta ahora no hiciste ningún cálculo que persista, o sea, vos le pediste un boxplot, él agarró y empezó a ver todas las tablas silver y se trajo los datos que le gustaba, eso va a quedar en esta sesión. Ahora vos decís, che, este gráfico está buenísimo, yo la verdad lo quiero, nada, siempre si vos se lo pedís va a armar una tabla go para poder construir esos box plot y después esos resultados van a persistir, es un poco la idea digamos del esquema medallion y que vos puedas armar tablas que después persistan.

**Andrés Rabinovich**: Y digamos, está bueno, está bueno. Dónde la data que subimos, ese Excel que subimos, eso vive en un

**Bruno Ruyu**: AWS, Sí, que hoy que este que usaste vos, el default SaaS en nuestra propiedad, pero se podría poner en uno que sea propiedad tuya o propiedad del cliente,

**Bruno Ruyu**: Vos a ese, o sea tenés, vos cuando te armaste en Workspace apareces como owner, nosotros, viste con las certificaciones y todas esas cosas,

**Bruno Ruyu**: no, no me voy a entrar, pero si quieren entrar

**Andrés Rabinovich**: yo

**Bruno Ruyu**: en dos minutos tengo una llamada.

**Bruno Ruyu**: Bueno, te decía, vos al ser owner, nada borra los datos y esos datos de nuestra nube tienen que desaparecer, porque parte de lo que nosotros certificamos no se vinculan, nosotros no tenemos acceso a estos datos como individuos, digamos, es esto, alinear lo que te dice Bruno es eventualmente vos decís, che, la verdad que yo tengo, tengo una cuenta en AWS, tengo los servicios, todo esto se sube como archivo, los servicios de C, podríamos utilizar esos servicios y que los datos queden en tu infra, pero obviamente ya deja de ser el servicio SaaS.

**Bruno Ruyu**: Yo Andrés te saludo, me tengo que bajar y se conecta Lucio, siguen ellos, buenísimo.

**Andrés Rabinovich**: Chau Bruno, gracias.

**Bruno Ruyu**: Ahí André, por la duda, eso que armaste vos, entra todo, es un que tenemos nosotros, eso tiene algunos límites de cantidad de usuarios, ese tipo de cosas, podés seguir cargando Excel, o sea le podés pedir, pegar todo lo que vos quieras, con Cloud te podés armar las tablas Gold, poder armar dashboard, o sea, ese dashboard que vos hiciste lo podés publicar en Tegram, compartirlo, usar los nobles, probá todo lo que vos quieras, cualquier cosa, si te cruzas con algo, ya sea te bloquea por el air frío, lo que sea, habla con nosotros y nada, estamos para ayudarlo. Yo lo que me imagino de lo que estuvimos hablando. Asumiendo que estos son datos de input que te pasaría algún cliente de ustedes, similares a lo que te pasaría a un cliente de ustedes, yo agarraría un ejemplo de cómo usan ustedes el input de su modelo y le diría Claude, che, llevá los datos así como esto y a ver qué te hace. Y ahí te va a empezar a armar tablas Gol con esas salidas, esas tablas gol te la podés bajar vos. Le decía a Claude, che me quiero bajar esta tabla gol y te va a mandar un link, te lo baj Y nada, cualquier cosa compartamos los contactos y estamos a disposición.

**Andrés Rabinovich**: Tema costos, cómo se maneja, cómo funciona eso o no te escucho. Recién, no se escuchaba perfecto, no sé qué pasó. Tema costosa, mira, nosotros si te vas

**Bruno Ruyu**: ahí anda uno que es billing ahí al último de ese, nosotros tenemos, bueno vos estás, ese que vos tenés en free, ese te va a permitir subir más fuente. Creo que podés usar dos usuarios. El primero que aparece es ese starter que nada, tiene un poco más de usuarios. Nosotros limitamos la cantidad de GB carga que vos uses, dos o tres cosas más y de ahí vamos subiendo. ¿Qué nos pasa normalmente? Que la mayoría de nuestros clientes están en enterprise, pero no porque sea más caro, sino porque más ajustado un poco la necesidad. Capaz que vos no decís, che yo necesito más almacenamiento porque la verdad que voy a tener menos usuarios. Encontramos por ahí un punto, eso lo vemos, la idea de precio está plasmada acá. Esto lo estamos, viste que nosotros igual que ustedes somos starter, lo estamos revisando todo el tiempo. Pero digo, es más o menos un poco el concepto de idea que tenemos.

**Andrés Rabinovich**: Está buenísimo. Espectacular, espectacular.

**Bruno Ruyu**: Dale André, igual cualquier cosa ya quedate usándolo y cualquier cosa nos preguntá.

**Andrés Rabinovich**: Bueno, dale, dale, dale, lo vamos a chusmear un poquito más ahí en detalle.

**Bruno Ruyu**: Ahí está nuestro mail, en el mail nosotros dedicado a esto, al soporte, así que cualquier cosa podés escribir por ahí.

**Bruno Ruyu**: Lo que iba a decir, que si algún compañero tuyo lo quiere usar sin comerse los users, puede hacer el mismo caminito que vos y ser un usuario diferente. Nosotros controlamos, así que entra con el

**Andrés Rabinovich**: PRI, dale, dale fe y labura y labura. Bueno, muchísimas gracias a ustedes. Muchas gracias. Un saludo. Chau, chau.
