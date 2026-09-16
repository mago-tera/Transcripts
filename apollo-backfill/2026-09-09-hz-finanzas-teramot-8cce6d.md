# HZ Finanzas - Teramot

**Fecha:** 2026-09-09T14:02:34.170+00:00  
**Duracion:** ~79 min  
**Participantes:** Agustin Garcia <agustin.garcia@teramot.com>, Bruno Ruyu <bruno@teramot.com>, Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, Juan Ramos <juan.ramos@hzgroup.com.ar>  
**Externos:** Juan Ramos <juan.ramos@hzgroup.com.ar>  
**Apollo ID:** 6aa179a3bd4a7800208cce6d

---

**Bruno Ruyu**: Ochenta por ciento de velocidad, me limita

**Juan Ramos**: un toque, pero no.

**Bruno Ruyu**: Y por soy desde izquierda, yo soy diestra. Así que nada, la motricidad fina la

**Lucio Rojas**: tengo hasta recién con Franco estuvimos con Verónica, que es la chica que está usando Téramo. Viene bien, o sea le falta un poco la herramienta. Yo me anoté bien el caso de uso que están haciendo y cómo lo hacían antes para ver las diferencias. Cuando vos me dé el pie después hacer tu intro, eso lo cuento y cuento cómo el proceso.

**Bruno Ruyu**: Sí, para mí de hecho eso, desayudarlo, contarle W, o sea contarle un poco los updates. Yo le tiro ahí. Bueno, ¿Lo viste? Ahí está, mira. Y después yo diría y ahora Lucio te cuenta lo que están haciendo, así podemos pensar cosas. Mito,

**Lucio Rojas**: Pero está muteado.

**Juan Ramos**: Ahí estamos ahora. ¿Me escuchan? ¿Me ven? ¿Todo bien?

**Bruno Ruyu**: ¿Cómo estás?

**Juan Ramos**: Hace mucho que no hablamos con los que no charlé nada nunca. Bueno, ¿Qué tal? ¿Cómo andan?

**Lucio Rojas**: Un gusto. Un gusto Juan. ¿Todo bien?

**Bruno Ruyu**: Bien. Te hago una intro rápida de los que están. Está Lucio que es del equipo de implementaciones de Téramo y Customer Success, el más importante de la reunión, porque vamos a tratar de que te cuente lo que están haciendo con el proyecto de auditoría. Después Agustín y Franco son del equipo comercial también, para que se sumen y

**Lucio Rojas**: escuchen un poco y bueno, si vemos

**Bruno Ruyu**: que hay algo interesante pueden avanzar ellos

**Lucio Rojas**: también con temas y seguir.

**Juan Ramos**: Perfecto,

**Bruno Ruyu**: ellos ya saben, saben cuál es tu rol ahí en HZ Group. Y bueno, nosotros llegamos al proyecto que estamos haciendo ahora, Juan Manuel, así que súper bueno porque demora un tiempo, que es lo normal, es lo que nos pasa en general. Pero bueno, parece que se están caminando y hasta entiendo lo que están haciendo

**Lucio Rojas**: con Victoria

**Bruno Ruyu**: Verónica de consultoría, parece interesante. Así que antes de contarte te hago como un repaso un poco más genérico de Tegramot, de lo que hacemos y sobre todo porque hubo un montón de

**Lucio Rojas**: cambios de que hablamos última vez.

**Bruno Ruyu**: Básicamente en la medida que fueron mejorando las inteligencias artificiales, plot, chatGPT, Nos dimos cuenta que la mejor forma en la cual se usa Teramot siendo una herramienta para que esas mismas inteligencias artificiales hagan

**Lucio Rojas**: mejor su trabajo y en particular tiene

**Bruno Ruyu**: que ver con una limitante que tienen esas inteligencias artificiales, que es que básicamente fueron entrenadas con mucho texto, con muchas imágenes, con mucho audio, por eso leen y escriben perfecto, hacen imágenes, interpretan imágenes y hablan y escuchan, lo que nadie pudo y probablemente nunca pueda, es entrenarlo con base de datos, sistemas de empresas, porque las empresas no se lo van a dar y que se hagan millonarios. Entonces ahí es donde se está bloqueando el acceso de esas inteligencias artificiales a las empresas. No puedes conectar ChatGPT a tu SAP, 74 mil tablas, 15 años de historia, y pretender que hagan las cosas bien derecho.

**Lucio Rojas**: Hasta junio, era algo que yo decía

**Bruno Ruyu**: que pasaba en junio, Antropic, los que son los peadores de Clod, sacaron un trabajo, publicaron un post en su blog donde básicamente confirman esto. Ellos tuvieron que hacer un quilombo terrible para que pueda funcionar Cloud. Y que en resumen, tienen un equipo de, no sé, decenas de ingenieros de software dedicado a que eso funcione. Un mes que no trabajan pasa del 95 al 65 por ciento de precisión. Entonces realmente no funciona solo. Y nosotros desde el día uno le buscamos la vuelta por otro camino para que si funciona. Y entonces de alguna forma la arquitectura está, los sistemas que tiene empresa, SAP, Salesforce, Transacciones, sistemas propios, lo que sea, Excel también, Google Sheet, todo lo que sean tablas y base de datos en el medio, Theramo encargándose del ida y vuelta de esa info, limpiándola, interpretándola, para que la otra inteligencia artificial, cloud o chatGPT, o uno propio que nosotros ponemos, pero que atrás está, cloud o chatGPT, haga lo que el usuario necesite que haga, pero con la información y entendiéndola al detalle. Eso sucede en minutos. Con lo cual de alguna forma es muy amplio lo que hace, y por

**Lucio Rojas**: eso estamos enfocándonos mucho más en equipos

**Bruno Ruyu**: vinculados a finanzas, porque entendemos que el uso de SAP y sus herramientas satélites es bastante poco feliz, y que la mayoría termina dedicándose a usar Excel o a bajarse cosas y procesar y tener miles de trabajo. ¿Bueno, entonces dijimos, bueno, esto se puede usar en cualquier área, pero dónde? ¿En el U? Yo lo viví en YPF,

**Juan Ramos**: lo tengo yo lo vivo hoy, pese a avances que tuvimos y todo, viste, otra vez la puta madre. Seguimos con el Excel, seguimos con la bajada de SAP, con el extra contable, con el análisis paralelo, y bueno, son cosas que no logramos resolver. Bueno, todo lo que vos decís, para mí es música para mis oídos. Después tenés por su rol propiamente, al tipo de sistema que te dice no che, pará, mirá que son estas tablas, que las tablas y la info, etcétera, etcétera. Bueno, y ahí empezamos un debate, pero ahí empieza.

**Bruno Ruyu**: Es lo que nos pasa todos los días en nuestro día a día. Ya nos lo tomamos con soda. Pero nada, la idea era esa, ¿No? Que en algún punto también y a tal punto fuimos para el área financiera que le incorporamos algo que nos pedían todos, que son tableros de control adentro de Teramot. Entonces tenés que estar usando, si querés lo podés usar, Power BI, tablero, lo que sea. Pero ahora vos desde el chat decís, quiero entender lo, las cuentas a pagar, quiero lo que sea, hace un tablero para poder verlo y ya queda hecho, tarda menos un minuto y después lo puede compartir todo, puede entrar, la información está centralizada, está explicada, ahora lo mostremos el caso, seguro te va a quedar más claro. Así que nada, es un poco un repaso y Lucio, te doy la palabra

**Lucio Rojas**: para que cuentes lo que estuvimos haciendo y lo muestre.

**Juan Ramos**: Si quieren por último les digo un poco para que entiendan contexto más allá, se hizo el Discovery en su momento, automatizaciones, bueno y demás. Sé que ustedes vinieron también laburando en paralelo. Nosotros si quieren siempre fuimos bastante cuidadosos con tema Inteligencia artificial, Copilot creo que está a nivel general con ciertas cosas se permite usar. Después algunos casos estaban probando GPT y después estaba Claude, que te diría, Tenemos algunas licencias de Cloud, Teams, que ahí vamos usando muy, muy, digamos, muy a un nivel inicial, llamémoslo. Yo en mi caso de osado nada más, fui por el Cowork tratando de habilitar, no sé, solo una carpeta, algo muy puntual, con mucho cagazo, porque obviamente, no sé, Sistema me decía che guarda. Pero me mandé igual y ahí estoy un poco mirándolo, pero bueno, desde mis ganas y mi cabeza está para avanzar con todo lo que se pueda.

**Lucio Rojas**: Buenísimo, sí.

**Bruno Ruyu**: Y nada, nos quedó claro de que el día uno charlamos que vos querés

**Lucio Rojas**: ir para eso y que nada.

**Juan Ramos**: Sí, obvio, obvio. Si yo pudiera digo che, quién mañana se viene y está conmigo tres horas por día y revolucionamos todo esto, atrás vendrá otro que me va a decir el de Sistema, no, pará que esto, que pin, que pam.

**Agustin Garcia**: Bueno, pero

**Juan Ramos**: arrancaría mañana mismo.

**Lucio Rojas**: Te dejo Lucy, entonces si quieren entro. Perdón, una cosa, yo once y media

**Bruno Ruyu**: me voy a tener que ir, porque tengo que ir al traumatólogo, mi fisiología. Pero los chicos están mejor.

**Juan Ramos**: Seguimos acá y después vamos charlando nosotros. Despreocúpate.

**Lucio Rojas**: Bueno, Juan, ¿Cómo andás?

**Juan Ramos**: Bien, bien.

**Lucio Rojas**: Yo estoy más en la parte de todo lo que es implementaciones. Y estuvimos trabajando en conjunto con Franco y Verónica, en lo que es usar Téramot para una prueba de concepto en auditorías. También estuvo involucrado el responsable de auditorías. No sé chicos, si ustedes Se acuerdan bien el nombre.

**Juan Ramos**: ¿Diego, puede ser? Diego

**Lucio Rojas**: un poco lo que hizo fue marcar la cancha y dejar que Verónica esté probando. Lo que estamos haciendo es puntualmente usar TRAMOT para el proceso de auditoría del ciclo de cuentas por pagar, para la parte industrial de SAP. ¿Y que me contó Verónica que hacía antes que ella para poder solucionarse ese proceso? Tenía que entrar a SAP y bajarse una por una, las tablas que tenían la vinculación con las cuentas que quería analizar, tenía que muestrearlas. Y generalmente los muestreos lo hacía en base a los proveedores que más plata movían, porque más cuentas movían la muestra significativa. Lo bajaba a Excel, y empezaba a cruzar en Excel, una por una, las distintas cuentas que quería analizar, las distintas partidas, los distintos movimientos. Y creo que me dijo textualmente, en palabras de ellas, un Excel infinito, un trabajo de hormiga. Dijo, si no acuerdo mal para trabajar con un muestreo. ¿Nosotros qué hicimos? Nos pusimos de acuerdo con Cristian, más allá de las diferencias, nos pusimos poner de acuerdo para que nos pase el módulo FI de SAP, para cargar directamente a THE. Y ella ahora está trabajando desde Cloud para hacer la auditoría de cuentas por pagar, y no trabajar más sobre la muestra de los 80 prov. Sino sobre el universo completo.

**Juan Ramos**: ¿Bien?

**Lucio Rojas**: Y bajar los tiempos de lo que ellos tenían Presupuestado, que era 248 horas para la auditoría, a una fracción. Y en vez de trabajar con el muestreo, trabajar con el universo.

**Juan Ramos**: ¿Bien? Eso todo adentro del entorno Cloud, todo dentro de Cloud.

**Lucio Rojas**: Ella lo está haciendo con EI y usando nuestra herramienta, que lo que hace es ser la capa intermedia entre Plot y SA. Nosotros nos bajamos las tablas directamente, y estamos trabajando sobre unas tablas estáticas. Pero algo que yo le veo muchísimo valor acá, y siento que puede llegar a. A sumarle mucho a ustedes Que es, podemos trabajar sobre auditoría continua, no sobre auditoría estática de decir, bueno, ¿Qué pasó? Sino ya vincular las tablas y a partir que va actualizándose la información del sistema, tener alertas de distintos movimientos que no deberían pasar y que son riesgosos, como por ejemplo que se pague a un proveedor antes o después de la fecha pautada, porque el sistema no tiene una restricción de alerta para eso. Nosotros lo podemos generar como alerta en vivo y que ustedes tengan un sistema de alertas para eso. Esos son ejemplos de cómo estamos trabajando en auditoría. Ella por lo que nos dijo, le está sirviendo mucho para trabajar sobre el universo. Si les soy honesto, creo que le falta un poco de entendimiento de la herramienta para poder sacarle el provecho real que tiene. Estamos trabajando con ella, antes de venir acá tuvimos la reunión con Franco y con Vero para explicarle cómo funcionaba bien Theramo, paso a paso para que ella lo interiorice y estamos resolviendo una de sus preguntas de auditoría. OK, ahora, esto un poco la macro de lo que estamos haciendo, si querés que te diga. Los beneficios para mí son trabajar sobre el universo, no sobre el muestreo, trabajar sin errores humanos, dejar de cruzar cosas a mano en Excel, hacer la auditoría continua, y cuando le agarren el vuelo de la herramienta, lo van a hacer en una hora en vez de una semana, que es lo que les lleva. Bastante seguro estoy de lo que vi con el caso 2. Ahora tenemos dos cosas para hacer. Podemos revisar un poco cómo funciona la herramienta, si a vos te interesa algo de eso y ver qué más se puede hacer.

**Juan Ramos**: Bien, obvio, desde ya. Y digo más por algún mensaje también que crucé con Bruno, donde mismo Bruno, vos me habías dicho que había bastantes financieros que venían muy entusiasmados con todo. Véanme a mí como un tipo que desde el deseo está súper entusiasmado con todo. Creo que soy bastante osado en ese aspecto dentro del grupo. Así que nada, aprovechemos todo lo que pueda. Yo voy a hacer más un empuje que llamémoslo un iluminado de este tema, pero yo estoy, como le digo,

**Agustin Garcia**: para

**Juan Ramos**: todo lo que sea intentar probar y desarrollar. Obviamente no tenemos una billetera infinita, estoy hablando de cosas lógicas, pero me interesa mucho, mucho, mucho, y más para el área financiera. Así que veamos todo lo que quiera.

**Lucio Rojas**: Un segundo estoy configurando para mostrar y te voy a compartir pantalla. Estoy cerrando pestañas porque vengo, me subo directo de la otra reunión y me quedo. Voy a mostrar dos cosas. Voy a hacer un repaso rápido sobre Téramo para que vos veas cuál es nuestra herramienta y qué valor agrega. Nos vamos a ir a mi cloud para probar un poco la herramienta en sí y que vos hagas algunas preguntas sobre los datos y empieces a imaginarte un poco cómo puede llegar a funcionar esto en tu área, más allá del caso de éxito que estamos creando en auditoría simplificado. No sé cuánto te ha contado Bruno, pero a mí me gusta resumir Telamot como una plataforma que permite trabajar con tus bases de datos desde cloud o desde cualquier EDM y automatizarte todo lo que es la parte de reportería y ser un asistente muy inteligente sobre tus datos para tomar decisiones de negocio. Vos ahora, si querés soltar el SAP, ustedes tienen un SQL Server a una NL, no vas a poder restricciones técnicas de seguridad tecnológicas. Por eso necesitamos tener medio. Lo que nosotros podemos hacer es conectar directamente una fuente de datos a Theramo, en Este caso para ustedes sería una PostgreSQL, que es donde tienen el backup de la base de datos. Esto habría que coordinarlo con Cristian para que nos deje conectar la fuente. Y una vez que lo conecta, empieza la parte importante de qué es lo que hacen los agentes de Teherán. Lo que hacen es básicamente entender la base de datos y crear metadata de cada una de las tablas, además de arreglar la información que ya tiene el sistema.

**Juan Ramos**: Además de arreglar.

**Lucio Rojas**: Me dijiste, voy a. Hay más técnicos sobre eso en un segundo. No sé cuánto roce tenés contra SAP, supongo que lo has visto bastante.

**Juan Ramos**: Sí, pero cada vez menos te diría, porque ya no estoy metido.

**Lucio Rojas**: Bueno, pero si vos te vas a ver las tablas de SAP, no las entiende nadie, básicamente porque son abreviaciones o abreviaturas, tablas en alemán, que la juntan para hacer nombres de tablas y nombres de columnas. Entonces, si vos querés empezar a trabajar con información, no podés porque vos no sabés qué significa frggr fknum, además de tener que ser técnico datos para poder trabajar con eso. Entonces, ¿Qué hace Telamo? Sus agentes van y escriben una descripción de qué tiene cada tabla y qué tiene cada columna. Yo sé que la tabla ESSR es una tabla donde cada fila representa un registro único de transacciones financieras, incluyendo detalles como el número de documentos, fechas relevantes, montos asociados. Y me hace una descripción también de cada una de las columnas de esa tabla. Por ejemplo, la columna LZBIS es una columna de campo numérico que tiene el monto total de transacción expresado en formato s. Así te mapea toda tu base de datos y vos tenés una descripción en lenguaje de cada una de las tablas. Y este lenguaje es lo que entienden los modelos que no entienden datos. ¿Entonces qué hacemos? Metemos todo este paquete de información, que además está normalizado y sanitizado. Por ejemplo, muchas veces en SAP pasa que hay campos que están en formato numérico, formato de texto y son números, entonces no puede hacer operaciones matemáticas de texto. ¿Entonces qué hacemos? Nosotros lo convertimos a formato de número. Voy a ver si encuentro la que tenga esa particularidad. Bastante reglas de base. Bueno, por ejemplo acá fíjate que estamos haciendo un montón de transformaciones sobre la tabla para que esta tabla se pueda trabajar, si no, no se puede. Toda esa información nosotros la compactamos en metadata y que es como una descripción esta que leíste en distintas herramientas, y la ponemos adentro de un MCP. Un MCP es un modelo, un protocolo para que se vincule Cloud con nuestro sistema. Es como si fuese un API, es un conector, un conector que hace que

**Bruno Ruyu**: dos inteligencias artificiales pueden trabajar entre, intercambiar, trabajar con.

**Lucio Rojas**: ¿Y qué hacemos con esto? Conectamos Téramot a Cloud, que es a donde vamos a ir. Si yo voy acá a mi Cloud, veo que tengo conectado Telamot. Esto ustedes en HZ Group ya lo tienen, tenemos una cuenta de Cloud, H Group ya lo tienen porque Cristian lo configuró junto con nosotros. Entonces vos ahora puedes preguntar de Claude directamente contra tu SAP. Yo le digo a Claude, le dije recién con el Tata Telamot, acá usó el conector este de Téramo del que estamos hablando, a el workspace de HSTA Group, que es donde tienen las tablas de sus app. Y hacemos un resumen de negocio de cada una de las tablas. Y me fue diciendo esto que yo te marqué que cada una de las tablas en lenguaje natural, como si fuese alguien de negocio. Y puedes empezar a hacer cosas con esas tablas. Entonces acá me fue explicando, por ejemplo, la tabla BSIK es la tabla de partidas abiertas de proveedores y me dice que contiene las deudas pendientes de pago de los proveedores, es la foto del pasivo corriente de cada proveedor, las facturas que se deben, desde cuándo, bajo qué condiciones de pago, fundamental para el análisis de antigüedad de saldos y riesgos de limpieza. Entonces ahora vamos a hacer una prueba en vivo, le voy a decir, estoy sentado. De HZ Group, quiero saber qué puede hacer él, como, casos de uso, más tablas tenemos cargadas, señalas por impacto y hagamos vos directamente.

**Bruno Ruyu**: Perdón, interrumpo dos minutos y va a servir de interrupción, porque es algo acá, digamos, hay muchas herramientas que están empezando a comercializarse, que es hacerle preguntas a los gatos, eso la verdad que está bueno, es realmente fácil hacer, porque el problema es que primero tenés que ordenar toda la información, hacerle todas estas descripciones, tenés que mantenerlo acá. Vos podrías hacerle preguntas al gato diciendo bueno, ¿Cuál fue la última factura que entró? Cosas así, el valor está y listo, ayúdame a explorar todo, decime que hay y después construí eso que ahora va a sugerir, es ida y vuelta, no es solo veo que hay y te traigo una respuesta. Es empezar a usarlo para pensar en cosas y profundizar, entendiendo que ahora Claude, el ente más inteligente de la humanidad, puede laburar con tus datos al nivel de detalle que consideres necesario. Eso significativamente distinto a cuánto fue, lo puedes hacer, no digo que no, pero hay un valor mucho más grande en explorar cosas complejas que te las construye así.

**Lucio Rojas**: Me dice. Ahora vamos a leer un poco las ideas que te da, si a vos no te gusta y querés que hagamos otra, se lo podemos pedir. Esto es como hablar con un humano, literalmente. Y bueno, vamos desde la silla del CFO con las tablas que tenemos. Es una restricción importante.

**Juan Ramos**: Sí, si tuviera mil tablas te tiraría por impacto capaz otra cosa.

**Lucio Rojas**: Sí, y aparte son tablas que están reducidas al módulo FI. Bueno, un buen módulo para trabajar, pero para la parte de auditorías de cuentas por pagar.

**Juan Ramos**: Me quedé con un tema, si ustedes pensaran en Grupo HZ hoy, hoy nosotros tenemos SAP Reversión R, a futuro estamos yendo por una migración a HANA, pero hoy, digamos, si fuera, che, hagamos algo con muchas más tablas o con muchos más datos o módulos. ¿Es una complicación o eso es algo que igual se puede abordar?

**Lucio Rojas**: No, no es para nada una complicación. Cantidad de módulos y con cantidad de fuentes, o sea, si vos querés conectar el SAP de la parte industrial y el firmware de la parte agropecuaria, puede ser dos. OK, esto arma un dataware, juntar las fuentes en la nube y acomodarlas para poder trabajar y cruzarlas si querés. OK, bien. Entonces ¿Qué me dice que podemos hacer? Podemos hacer detección de pagos duplicados, podemos hacer triway match entre pedido, recepción y factura, Podemos identificar cambios sospechosos en datos bancarios de proveedores, podemos ver la antigüedad de los saldos, el aging de proveedores, podemos hacer compliance de retenciones impositivas, descuentos por pronto pago desaprovechados, esto está bueno. ¿Concentración de proveedores, cuánto gasto total, se concentra en los top 10 proveedores, cuánto? Segregación de funciones, el mismo usuario crea la solicitud, aprueba el pedido y contabiliza la factura. Esto viene de auditoría, factura sin órdenes de compra, análisis de medios de pagos y bancos, mapa de por dónde sale la plata, qué bancos, qué métodos, qué montos, utilización de si querés, no sé, pegar una doble I alguno y decime si te interesa alguno o si con este tipo de información se te ocurra a vos hacer alguna otra cosa, ¿No?

**Juan Ramos**: Por ahí veamos a ver el de el punto 2,

**Lucio Rojas**: ¿Qué es esto? Se facturó más de lo que se recibió, se recibió más de lo que se pidió, detecta sobreprecios, cantidades infladas y facturas sin respaldo, Impacto enorme en el control de FUR. Entonces vos agarrás y le pedís directamente a Clop que genere este reporte en su síntesis. Es una herramienta de reportería avanzada, trabaja con las tablas que vos tenés y te genera tablas nuevas sin necesitar un equipo de sistemas y un equipo de datos en el medio. Vos siendo negocio te generas tus propios reportes. Después sobre esto podemos generar dashboards, informes, análisis, modelos predictivos, forecast de ventas, lo que vos quieras, pero parte de los datos es generar nuevas establecidos. Vamos a una nueva tabla y vamos a hacerle acá un poco de prompting, vamos a decirle, vamos a crear tabla, saludo, adiós, chau, para después analizarlo en el informe. Dashboard, pero antes necesito que mires las tablas base y me hagas preguntas. De negocio que necesites para tener más. Y ahora vamos a dejar lo que vaya a mirar las tablas, te vamos a mostrar más o menos lo que hace. Dice, bueno, perfecto. Antes de armar nada, quiero entender bien los datos. Voy a mirar las tablas base en detalle. Para eso este conector, que es el conector a Theramo, si vos abrís acá, puedes ver lo que está haciendo. Está usando el conector de nuestra plataforma para ir a mirar las tablas, entender la información, razonar, mirarlas de vuelta, razonar y hablar con vos. Y en ese ida y vuelta está cumpliendo el rol de sistemas y de equipos de datos. A vos como usuario de negocio te empodera muchísimo, porque no tenés que estar del equipo de reportería algo, o bajándote las tablas y cruzándolas en Excel, o sea, directamente partís de tu objetivo, de lo que querés, y te genera el reporte en el momento. Yo creo que esto no va a tardar más de cinco minutos y vamos a poder ver.

**Juan Ramos**: ¿Ahora, vos acá estás metido dentro del conector de Theramo, agarraste tablas que te pasó? Grupo HZ, y dentro del conector de Téramo de Cloud, estás, bueno, pidiendo información,

**Lucio Rojas**: pidiendo información, pidiendo reportes. ¿Esto es lo mismo que está haciendo Verónica? Sí, sí, Verónica se está creando su. Se está auditando contra las tablas con CLOC. Las preguntas que ella definió para encontrar los riesgos en el proceso, se las hace a Cloud, mira las tablas y le responde.

**Juan Ramos**: OK, OK.

**Lucio Rojas**: Está pensando bastante para determinar. Bien, después esto, hablando con otros equipos de finanzas, ya sé más o menos cuáles son temas tan buenos. Sirve mucho para hacer predicciones tipo forecast y demás. Las ventas de los últimos años de tales unidades de negocio, de todas, y vamos a cruzarla contra distintas variables macroeconómicas e internas de rendimiento, y vamos a armar escenarios de ventas en base a esas variables. Esa variable puede ser inflación, supuestos sociales, como trabajamos con alguien de consumo masivo vinculado a los vinos, decía, bueno, si ganamos el mundial, las ventas son distintas y las perdemos. Entonces puedes predecir y armar modelos muy fácil y muy rápido, y empezar a hacer forecast basado en datos y no en cómo viene viento. Bien, bueno, vamos a hacer así, hacerme las preguntas. Le voy a hacer que me haga tipo cuestionario, así le respondemos algunas determinaciones que necesita para el reporte y no les va a armar. Me dice, bueno, ¿Qué sociedades incluimos? Todas las sociedades, solo las tres principales

**Juan Ramos**: ponen, si querés a este efecto ponen las tres principales.

**Lucio Rojas**: ¿Incluimos servicios o sueldos, materiales con recepción de depósito? Supongo que vos por ahí te hace más sentido estas preguntas.

**Juan Ramos**: Sí, sí, no pone materiales, insumos,

**Agustin Garcia**: ¿Desde

**Lucio Rojas**: qué año Analizamos todo el histórico,

**Juan Ramos**: salvo que te haga demorar mucho por ampliarle

**Lucio Rojas**: el rango, pero no, no nos cambia porque es cantidad de filas, es como más fila? ¿En qué modela comparamos los montos? ¿Todo en pesos, todo en moneda del documento o ambas columnas? Supongo que la moneda del documento debe ser. ¿Qué hacemos? ¿Pesos, dólares o las dos?

**Juan Ramos**: Y no sé cuánto te puede cambiar. A ver si pones ambas capas. Ambas.

**Lucio Rojas**: ¿Cómo manejamos la tolerancia de desvío? ¿Dejar desvíos crudos, definir umbrales, después flaguear con tolerancia del 5?

**Juan Ramos**: No, dejalo crudo.

**Lucio Rojas**: ¿Incluimos contratos Marco? No sé si a vos te ha sentido, a mí no me entiendo los

**Juan Ramos**: datos, no, Capaz que es un contrato inicial sobre el que se disparan después distintas compras, como que te diga un contrato entre grupo HZ y no sé, Aluar, te voy a vender aluminio por los próximos tres años, bla, bla, bla. Y bueno, no sé el impacto. Si querés poné incluir a ver qué te dice, o poné algo más tipo

**Lucio Rojas**: explícame qué incluyen los contratos marco también como para entender. OK, bueno, vamos a hacer eso, dale. Bueno, dame. ¿Que incluye? Está buena esta pregunta, más allá de que nos interese o no saber qué es los contratos marco, para que vos veas cómo te explica sobre tus datos cómo puedes ir vendiendo. Son acuerdos paraguas con un proveedor, donde se pacta un precio y una cantidad máxima por un periodo. No son pedidos de compra en sí, son el marco del cual después se generan órdenes de compras individuales que liberan cantidades del contrato. Si los excluimos, el true way match se hace solo sobre los pedidos de compra reales, que son los que efectivamente tienen entrada de mercancía y factura asociada. Análisis más limpio y directo. Lo que pedí lo recibí, lo que pedí es igual lo que recibí, igual lo que me facturaron. Si los incluimos, se agregan más o menos 6.500 posiciones que representan los topes teóricos

**Juan Ramos**: excluirlo si no a efecto de la muestra.

**Lucio Rojas**: Pero bueno, eso estuvo interesante porque fíjate la velocidad y la curva que tiene para responderte sobre los datos. Ahora, ¿Qué va a hacer? Va a levantar todos estos requerimientos que nosotros le pedimos, hacer un triway match con todas estas instrucciones y va a generar la tabla nueva, que es lo que es el cruce de información y el cruce de datos. Eso hace Téramot trabajando como ingeniero de datos, sin que vos tengas que hacer más que esto y esperar 5 minutos a que genere la tabla. Y una vez que genera la tabla, le puede servir dashboards, informes, que te haga riesgos en algunos casos. Saquemos el ejemplo este, si hacemos una tabla de ventas, puedes crearte directamente un dashboard en vivo para que te muestre las ventas conectados a la tabla, que están conectados al sistema. Y todo eso se lo pedís a Cloud sin tener que tener alguien que haga BI, sin tener bien carga Data Analyst, sin alguien que sea de sistemas que te esté proveyendo la información. Sos vos o tus equipos de control y de gestión, o tus equipos internos de datos dentro del área, que te responden con información a una velocidad distinta a la que antes había y que además le sube muchas posibilidades. Alertas, automatizaciones, forecast, modelos predictivos. Esto tiene, si se pone a jugar no terminas nunca. Así que vamos a esperar en un rato es el momento de espacio publicitario que necesito, porque suele tardar. Las queries más pesadas, digamos. Acá puedes ir viendo todo lo que va haciendo, que esto es lo que le digo, trabaja como analista de datos, probó que la QI funcionaba, le trajo 357.000 análisis, me parece, 357.000 filas con 35 columnas de tribu image y ahora va a generar la tabla nueva. ¿Qué tiene de bueno esta tabla? Que una vez que queda generada y vinculada a tu sistema, se actualiza todos los días. Vos no tenés que hacer este reporte de vuelta nunca más. Ya queda estandarizado y podaste incluso armarte un sistema de alertas.

**Juan Ramos**: Pero eso cómo es para vos tenías una tabla de datos que era estática.

**Lucio Rojas**: Sí, por eso yo ahora estoy sobre un.

**Juan Ramos**: Vos decís, si estuviera ya en una fase dinámica donde todos los días de alguna manera refresca tus últimas transacciones, no sé cómo llamarlo.

**Lucio Rojas**: Entonces, aparte yo ahora estoy estático, estoy sobre una foto un RAMP, me bajaron un periodo de tiempo de su base. Si yo conecto la base, se actualiza todos los días y me trae los cambios sincronizados día a día. Entonces vos trabajas con información viva y todo lo que crees se crea sobre información viva y te puede servir para automatizarte reportes. Por ejemplo, hay empresas donde trabajamos, donde tenemos automatizada la reposición de stock en base a las ventas que van haciendo todos los días y al stock de productos, hace una predicción de cuándo le va a quebrar en stock y ya lanza el pedido antes de que pase. Todo eso se puede hacer a partir de conectar la información en vivo.

**Juan Ramos**: OK,

**Lucio Rojas**: acá me está construyendo la tabla. Si yo me voy a thermo de

**Juan Ramos**: vuelta,

**Lucio Rojas**: la veo acá en proceso. Una vez se me Yo ya tengo el análisis hecho. Esto tarda 4 o 5 minutitos y podemos empezar a consultar sobre este análisis. Entonces vos vas a tener todos los. Las alertas de cuando lo que facturaste no igual a lo que recibiste y a lo que pediste. Justo este modelo está muy entrenado para auditoría. OK, terminó, terminó rápido. Pero si vas a lo que es más finanzas en sí, capaz que puedes encontrar algo más puntual de for, casi de estado de resultados. Ahora te cuento un caso que está bueno qué hicimos acá. Agarramos dos tablas del sistema, las cruzamos con todas estas instrucciones que le fuimos dando, que es lo que fuimos determinando con club, me generó la query de SQL. Creada esa tabla, esta tabla ahora está viva y Teramot lo guarda en su infraestructura. Entonces si yo ahora voy y le digo, Clot, fíjate que la tabla ya terminó. Se me un análisis de lo que viste para el reporte de auditoría para CFO formato artefact, es un HTML y vamos a usar un modelo bien inteligente. Así que agrupado. Cuento un caso que está copado. Trabajamos con unas empresas grandes que también usaban SAP y tenían equipos de cobranzas yendo directamente a la tabla, les costaba, tenían que ir al sistema y bajarse las tablas. Le costaba determinar cuáles eran las cuentas que tenían vencimientos en los próximos meses por la cantidad, por el volumen y cómo era el comportamiento histórico de pago de esas cuentas. Entonces usamos Telamo para hacer dos cosas. Primero, hacer un perfil de pago de cada uno de tus sería de tus clientes, clientes de tus clientes. Y sabes que este cliente generalmente paga tal día, que si se pasó de tal día ya es probable que entre en mora. Que este cliente es plausible de pagar antes de la fecha de todo el histórico de pagos que tuvo. En tantos estuvo en mora, en tantos no. Paga en efectivo, paga por tal banco, pagan transferencia, para que me entienda el concepto. Y generó un scoring. Si es un cliente riesgoso, o un cliente bueno, o un cliente excelente. Eso lo cruza con cada una de las fechas de vencimiento que están en tu SAP, y te arma un calendario que te va diciendo, como si fuese un Google Calendar, día por día, qué cuentas se te vencen, que tenés que cobrar, quién es el cobrador asignado, cuál es el historial de pago de ese cliente, y cuál es el riesgo del cobro. Y eso te deja a vos hacer dos cosas. Primero, ir a cobrar sin que se te pase nada por abajo de las manos. Y segundo, empezar a planificar. Si sabes que es un buen pagador, por ahí podés generar un cobro anticipado a la fecha de vencimiento, y bueno, empezar a jugar con esa plata.

**Juan Ramos**: Y ahí, en este caso que comenta Lucio, las cuentas corrientes estaban muy limpias, ¿No? Porque supongo que ahí puede ser todo un tema cómo están las cuentas corrientes, si tienen diferencia por retenciones no aplicadas, por bla, bla, bla. Las cuentas corrientes a veces son medias complicadas, y capaz que desde cómo uno piensa, ese proceso cierra por todos lados. Después cuando vos decís, che, el calendario me tiró que hoy le tengo que cobrar a Franco, Y Franco te dice, no, pará, si yo no te digo nada, estás viendo una retención que no aplicaste de hace seis meses, supongamos, imagino, podés parametrizarlo por relación deuda, volumen de compra, bueno, diversas cosas, ¿No?

**Lucio Rojas**: ¿Pero ahí qué pasó? Nosotros para construir este tipo de soluciones, sí o sí necesitamos alguien interno, analista, me la pega un poco el negocio. Es más, lo puede hacer solo. Nosotros no vendemos servicios, sino herramientas. También vendemos servicios, pero solamente se necesita. Y Cloud entiende muy bien toda tu tabla, tu SAP sabe cuáles son los códigos de retenciones, cuáles son los códigos de vencimientos, identificar esas cuentas corrientes, si están limpias o no, y limpiarlas en caso de que no. Y vos podés parametrizar todo, lleva trabajo ponerle para armar esta solución, estuvimos casi tres semanas trabajando con el equipo, y haciendo un poco de auditoría, veíamos las cuentas y corroboramos si esto era efectivamente correcto o no. Y si no es correcto, tenés que volver para atrás y pelearte un poco con Cloud y con Teramot hasta que te dé el resultado dado. Pero todo eso se va curando. Se va curando porque justamente la herramienta lo que hace es generar tablas y hacer transformaciones de datos. Y nada, si hay errores, se pueden ir ir mejorando. Bien, pero no estaban del todo limpias. Es más, yo tampoco tenía mucha idea ir a poner las tablas. Fuimos haciendo así como lo que vimos acá con vos, ir yendo preguntándole, che, tengo este error, ¿Lo viste? Puede tener un nivel de detalle súper riguroso a nivel fila. Entonces vos podés levaguear muy bien, o sea, podés irte muy bien. Bien, acá por ejemplo, ya nos hizo el análisis, lo podemos ver qué hizo. Fue. Miró la tabla esta que generamos a partir de las instrucciones que hicimos con vos en un ratito, Le pedimos que me haga el reporte, usó la integración de Telamot, fue. Hizo muchas queries de SQL, es decir que fue a traerse información de la tabla. Juntó toda esta información, usamos Fable 5, que es el modelo más alto que tiene Cloud hoy, y armó el reporte. Me dice, listo, ahí tengo el informe ejecutivo completo. Los tres números que le van a importar al CFO 155 millones de sobrefacturación neta, con 15 casos que concentran 600 millones, incluyendo uno con error de por 1.500. 5.628 millones en anticipo sin aplicar el trabajo expuesto. 3.569 millones de mercaderías recibidas sin factura. El informe cierra con un plan de acción de seis pasos ordenados por recuperar, contener, prevenir. Y acá tenemos el informe. Este es el True Match de pedido, recepción y factura. Alcance 357 mil 886 posiciones de compra. Tres sociedades que supongo que deben ser como empresas de grupo. Periodo histórico completo. Radiografía del proceso de compras. Cada posición del pedido fue cruzada contra sus entradas de mercancía y sus facturas registradas en SAP. La barra muestra dónde está parado hoy el circuito completo. Match perfecto. Es lo verde de cantidad y de monto. Cantidad o, pero desvío el monto con desvíos en cantidad y monto. Rojo recibido, sin factura, lo amarillo facturado, sin recepción, esta partecita y sin movimientos aún toda esta. Y acá tenés dos hallazgos principales, por ejemplo, sobre facturación, se pagó por encima de lo que entró al depósito, fuga directa en 16.152 posiciones. El monto facturado supera el valor de la mercadería efectivamente recibida por un total de 255 millones. Los 15 casos más grandes concentran cerca de 600 millones, son pocos identificables y accionables. Incluyen un caso de 136 millones en una sola línea, un fideicomiso del pedido E y una línea de fardo preconsumo con una diferencia exacta de por mil entre lo recibido y lo facturado. Patrón típico de error en la unidad de precio. Entonces vos te puedes ir a esto y le decís tráeme Exacto. De las dos casos que mencionas, esto es objetivo que te puedes ir metiendo a niveles cada vez más.

**Juan Ramos**: Qué haces eso, lo seleccionas y haces la apertura qué hiciste para copiarlo.

**Lucio Rojas**: Sí, agarré, copié y pegué esto, copié, pegué, se lo puse en el chat haciendo la apertura de todo. Esto es más como un informe. Después acá te marcó los riesgos y abajo te dio un plan de acción recomendado, dio casos prioritarios para la revisión inmediata. El fondo fiduciario que recibió 118 millones, que facturó 158, desvío millones. La observación es el mayor desvío individual de toda la base. Esto puede, como decís vos, puede responder no a un error, sino capaz que también a algo que no interpretó bien de los datos. Y eso se lo puedes decir y lo puede corregir, Pero lo bueno es que puedes responderte al porqué de todo.

**Juan Ramos**: A ver, para entender algo, Si fuera el caso, creo que es el anteúltimo, le podés pedir más detalle ese pasta celulosa, Clavín, no sé qué.

**Lucio Rojas**: Sí, sí, te puedes pedir todo.

**Juan Ramos**: Abajo te pone el plan de acción. A ver, sigámoslo y vemos.

**Lucio Rojas**: Me dice vamos a revisar los 15 escasos top con compras y cuentas a pagar, concentran 600 millones. Confirmar caso por caso si corresponde, nota de crédito, reclamo al proveedor o corrección contable. Depurar y aplicar los anticipos pendientes. Inventariar los 500, los 5.628 millones de anticipos abiertos, usarlos con recepciones posteriores y netear los aplicables. Definir políticas de antigüedad máxima, participo sin aplicación. Provisionar el recibo no facturado. Validar con contabilidad que los 3.569 millones de mercaderías recibidas sin facturar estén reflejados como provisión. Conciliar la cuenta grir y limpiar partidas anticipadas. Activar bloqueo automático de facturas con desvío. Auditar la categoría grabado de cilindros, que se ve una categoría puntual con muchas líneas de desvío sistemático, chicos. Y lo último, esto es lo que te decía, hacer un tablero de monitoreo mensual, donde esto ya quede estandarizado como reporte y vos no tengas que venir a buscarlo, sino que que te aviso. Y acá te hace un alcance. El alcance es el universo, los pedidos de compras reales, contratos marcos, cuyas cantidades son topes teóricos. Los montos comparan el neto acumulado de recepciones contra el neto acumulado de facturas por posesión y devoluciones ya enteadas. Parte de los desvíos de monto pueden explicarse por diferencias de tipo de cambio entre la fecha de percepción, la factura en compras en moneda extranjera. La revisión caso a caso lo determina. Tenemos que siempre. Esto es como un muestreo grande de todo universo y después no tenemos que meter caso por caso. Y ahí le vamos a ir agarrando con.

**Juan Ramos**: OK,

**Lucio Rojas**: acá me trae el caso 1. Fondo fiduciario. Fiduciario. El pedido 51 NN, posición 40 PP, planta SEX, proveedor Rafael Albanesi. Pedido una línea valorizada en pesos, precio unitario 1 y un tope original de 20 millones en pesos. La posición tuvo cuatro ciclos de recepción o factura. Los primeros tres machean al centavo. Ciclo referencia, recepción, factura, match exact. Exacto, exacto. Y acá hay uno que tenemos la referencia. La recepción es de 7 millones de pesos y la factura es de 143 millones, ya que facturamos 1 por 20 de recibo. ¿Qué pasó en el cuarto ciclo? La recepción se registró normal en pesos por 7 millones, pero la factura se registró en dólares 4 millones a tipo de cambio 349,95. 143 millones de monedas. Fue contabilizado automáticamente por el proceso batch, igual que todas las demás. Es decir, nadie la revisó manualmente. El desvío de 136 mil millones de pesos sale 100% de esa única factura. Las dos hipótesis a verificar contra el comprobante físico a la factura real eran pesos por 7 millones y se cargó con moneda dólares por error, se pagó entre veces de más o B el cargo era legítimamente dolarizado y la recepción se hizo mal. Entonces te puedes meter en cada una de las cuentas y mandar a alguien a revisar y acá tenés tu caso y así puede hacerlo todos los que te marcó acá. Bien, Así que bueno, nos estamos quedando un poco ahí sin tiempo. Si querés cierro la pantalla y cerramos un poco. Este es el poder de la herramienta. Acá estamos haciendo algo de auditoría, está buenísimo, funciona muy bien, pero también funciona muy bien para todo lo que es responderte preguntas de negocio, hacer modelos predictivos, todo lo que salga de tus datos y de alguien que necesite información. Nosotros ahora estamos en una PO con la parte de Diego, ni siquiera tenemos todavía la base conectada, solamente tenemos esa foto y están trabajando ahí y estamos tratando de educar un poco a Verónica para que la prueba funcione.

**Juan Ramos**: OK, bien,

**Lucio Rojas**: tiene relación con vos, pero para que al tanto y si vos te interesó, podemos también probar con algo del lado de finanzas.

**Juan Ramos**: Sí, me interesa. ¿Hay algo que ustedes entiendan para compañías como las nuestras que operen en SAP y demás? Algo que vos digas, che, esto ya lo usamos, ya funciona, es más fácil trabajarlo y verlo rápido, que ustedes lo puedan apreciar. ¿Hay algo que entiendan ahí que pueda ser el inicio de lo que revisemos?

**Lucio Rojas**: Hemos tenido casos de uso para nosotros, casos de uso siempre que salgan de SAP lo mismo, porque la herramienta funciona igual. Lo que tenemos nosotros es más expertise en algunas soluciones, como esto que te digo, armar un calendario de cobranza o cuenta por cobrar. Pero para mí la respuesta es lo que a vos más te duela. Hoy tengo algo en mente que me gustaría hacer.

**Agustin Garcia**: Hay una parte ahí Juan Manuel, que también es importante, que es una ventaja producto, es que cuando vos conectas app directo, la herramienta interpreta el modelo de datos automáticamente y eso te facilita a vos como usuario no tener que conocer el detalle de las tablas, los nombres que SAP codifica de una forma bastante particular. Entonces también eso te permite, digamos, como la curva aprendizaje en el uso de los datos es bastante suave por esto, o sea que básicamente el producto te permite interpretar las entidades que están disponibles y cuáles son las relaciones entre ellas.

**Lucio Rojas**: OK, OK. Algo que hicimos es un cash flow de caja a corto plazo, saber en base a todas las cuentas que vos tenías abiertas, cuál va a ser tu posición de caja los próximos 30 días. Eso es algo que también ha funcionado, pero son todos pasos de uso que como te digo, vamos sacando de lo que nos pide el cliente porque le duele. Claro, te puedo decir eso. Tenemos esos dos, tenemos cash flow a corto plazo, tenemos lo que es cuentas por cobrar para el equipo de coderanzas y si, si no podés ir vos con algo que si no te porta. Podemos.

**Juan Ramos**: OK, OK. Supongamos que, digamos, tendríamos que pensarlo en algún punto, podríamos suponer lo siguiente, piensen ustedes que el grupo tiene diversas compañías, no todas esas compañías tienen un presupuesto aprobado. Hagamos de cuenta que son siete compañías, no todas están en SAP, pero no sé si es relevante o no, no importa, hagamos de cuenta 5 en SAP y 2 fuera de SAP. Esas 7 tienen un presupuesto aprobado que empieza a correr el 1 de julio, 26, cerró el mes de julio, cerró el mes de agosto, estamos ahora corriendo los primeros días de septiembre. Imaginemos que yo dentro de mis responsabilidades digo che, tenemos que hacer todos los meses el cierre mensual de cada uno de los negocios, eso compararlo contra el presupuesto para ese mes que estaba presupuestado y para el acumulado. Si hacemos el cierre de agosto diríamos che, agosto cerró así, contra un presupuesto que decía que iba a ser de esta manera y julio más agosto, los dos primeros meses del presupuesto nos nos arrojan estos datos contra un presupuesto que iba a ser de esta manera. A partir de ahí conclusiones, bla, bla, bla. Y si querés adicionalmente como grupo una consolidación de que vos digas che, estos son mis 5 negocios, al mes 1 vendí 50, al mes 2 vendí 50 más, o sea a nivel consolidado voy 100 palos de venta y todo el estado resultado te puedas imaginar atrás siguen el presupuesto.

**Lucio Rojas**: Sí, te sigo porque justo un trabajo anterior así que vos estás queriendo hacer un control presupuestario contra lo que supongamos el control va sobre ventas y costos o va sobre nada más que partidas

**Juan Ramos**: de venta, costo, todo completo.

**Lucio Rojas**: Vos tenés el presupuesto hermano, como para variar, ¿Dónde los tenés armado? En Excel.

**Juan Ramos**: En Excel, sí. Ahí es todo extra contable, todo gestión, digamos.

**Lucio Rojas**: Sí, sí eso es contable y querés ver contra las cuentas de SAP cómo se fue ejecutando ese presupuesto.

**Juan Ramos**: Supongamos que el mismo cierre del mes a mes tiene parte de SAP y parte extra contable por algún ajuste que se le haga a nivel gestión, o sea nuestro estado de resultados, digamos que nos manejamos día a día o mes a mes, no es el mismo que te tira SAP, porque hay diversos ajustes que se pueden llegar a hacer extra contables.

**Lucio Rojas**: Pero bueno, vamos a tener un problema con la información que no tengamos a disposición. Es una clara. Podemos ir sobre la parte de SAP o si vos lo otro lo tenés sistematizado, también se puede cargar.

**Juan Ramos**: Creo que es algo que se puede sistematizado, digamos. Si no es apende por ahí un

**Lucio Rojas**: poco del formato de ese Excel. Nosotros trabajamos con Excel tabulares que se tienen que parecer exactamente una base de datos muchas veces yo cuando he trabajado con Excel se parece más a lo que el ojo humano le sirve ver, que no es lo mismo que una base de datos. Claro. Ahí vamos a tener una restricción. Estamos siempre sí o sí que sea tabular lo que no lo podemos ingestar. Claro, pero podemos probar de. Si vos me decís alguna sociedad para cotar un poco más la que podemos que estén SAP, Verdir sobre esa. Con este caso de uso.

**Juan Ramos**: Bien, bien.

**Lucio Rojas**: Que se puede hacer.

**Juan Ramos**: OK. ¿Más allá de esto que es más de reporte y revisión, por ahí si uno puede pensar cosas parecidas que hicimos con cuentas a cobrar, pensarlo en otras cosas, no? Digamos, sin limitarse, es tratar de ver qué se puede arrancar y seguir trabajándolo.

**Lucio Rojas**: Depende tanto de un caso de uso, casi siempre la mejor forma es conectar los datos, cuando nos acostamos al caso de uso, tratamos de resolver eso, agarramos y cosas que eran más fáciles de hacer y más rápidas. Entonces a mí como me gusta trabajar es primero lograr un acceso a los datos, que eso es súper importante y súper burocrático también, sencillo. Y una vez que tenemos el acceso a los datos, nosotros podemos incursionar un poco ustedes en ellos para mapear los casos de uso posible y ahí se elige uno sobre lo que ya sabemos que se puede hacer. Por ahí renegas mucho menos a tratar de acomodar la herramienta caso de uso que uno tiene en mente, veo más éxito. ¿Quizás podemos arrancar sobre investigar con las tablas que ya tenemos cargadas del módulo fi qué se puede hacer, no? Iba a salir un poco de lo

**Juan Ramos**: que teníamos ahí cuando decís las tablas que ya tenés, sería la parte esta de cuentas a pagar.

**Lucio Rojas**: De cuentas a pagar. Y si no podemos pedirle a Christian la conexión al SQL Server.

**Juan Ramos**: OK, o sea, la conexión, lo voy a decir bien a lo bruto, la conexión en tiempo real a la das a nuestra base de transacciones actuales reales.

**Lucio Rojas**: Eso si vos querés conectar, eso si vos querés ver cosas en tiempo real. Si a vos te interesa actualizar, analizar cosas para atrás y no te importa tanto el mañana. A nosotros Cristian ya nos ha pasado un backup de la base de datos y con eso se puede trabajar. Pero bueno, eso también a nosotros.

**Juan Ramos**: Pero vos lo que dirías de avanzar es en qué, Porque lo hablo con Cristian y para entender mejor. Avanzar en qué podríamos. Capaz yo no interpreto bien el pedido

**Lucio Rojas**: en qué punto a nosotros nos gustaría tener la base de datos conectada, y eso a nosotros nos deja hacer un montón de análisis de probabilidades de lo que se puede hacer. Entendemos que su base de datos también es robusta. Entonces cargar conlleva que Agus tenga alguna conversación comercial, Porque nosotros estamos en prueba de concepto. Creo que lo mejor que podemos hacer

**Juan Ramos**: ahora es

**Lucio Rojas**: cerrar la prueba de concepto que tenemos y avanzar un proceso más formal de conexiones.

**Agustin Garcia**: Hasta acá como que la idea era bueno, mostrar el valor de la plataforma realmente que puedan hacer tangible la eficiencia y la productividad que se gana. Me acuerdo que Diego en su momento nos había comentado que que tenían estimado en 205 horas lo que era este análisis que se hizo. Que entiendo que bueno, que con todo este trabajo está claro que esta primera prueba lleva cierta iteración, pero seguramente estamos bastante lejos de esas 205 horas. Entonces la idea acá es digamos, bueno, validar. Ahí ya Vero nos contó que nada, que se nota la diferencia y que lo se ha validado eso. Y bueno, la idea es ver de poder cerrar esta etapa de prueba concepto y ya ver de analizar y empezar tal vez en un servicio más formal, como para que también puedan ir sumando distintos casos de uso y que el uso no sea solo cuentas a pagar, sino que a medida que quieran poder ir sumando un poco también como parte del servicio, nosotros damos un acompañamiento para ir transfiriendo un poco el conocimiento y que también ustedes empiecen a tener autonomía, porque como te decía Lucho, nuestra intención no es vender servicios, nosotros solo vendemos la tecnología. Entonces, digamos, obviamente que queda un punto de contacto y hasta que eso ocurra, que logres autonomía, hay que transcurrir un camino. Pero bueno, la idea es empezar a ver si les interesa también ir empezando por ese camino, como para que ustedes puedan ir atacando cada vez más casos de uso, generar dashboard y empezar a aprovechar la eficiencia y productividad que les puede permitir la herramienta.

**Juan Ramos**: Y me quedé con un tema cuando me mostraste el informe, Lucio, vi que eran cosas 2023-2024. Eso porque la tabla que te pasaron no tiene info actual, o en realidad sería como una conclusión que no se detectaron anomalías durante 25-26-2024.

**Lucio Rojas**: Voy a preguntar,

**Juan Ramos**: ¿Vos me podés pasar ese informe o informe y detalles, no sé cómo llamarlo, para tratar de ver la consistencia con la realidad nuestra, como si son hallazgos reales, o el analista y me dice, no, Juan, esto es una boludez, pasó tal cosa y tal otra? No digo que delira el modelo, pero digo, no sé tiró fruta porque no está viendo tal cosa que nosotros manualmente hacemos, bla, bla, bla.

**Lucio Rojas**: Sí, yo te lo puedo pasar en otro formato que es PDF, porque el artifact este. Ah, no te lo puedo pasar así. Sí, te lo puedo pasar. Y estoy preguntando los datos, tenemos que tener en cuenta que esto es, los datos llegan hasta el 4 de julio de 2026. Por las dudas, capaz que nosotros no vimos las últimas anomalías, pero deben estar por ahí. Esto es una herramienta, nosotros hicimos una demo en una hora con preguntas muy.

**Juan Ramos**: A ver, ya que te voy a robar una pregunta más. Vos pregúntale de los últimos 12 meses, la anomalía que entiende más relevante. Así, si quisiera ver el dato rápido acá y bien actualizado con cualquiera, me lo dice, solo para sacarme la duda y ver en qué está.

**Lucio Rojas**: Perfecto, bien. De los últimos dos meses. Sí, está bien. Datos actuales. Ahí está, mira. El patrón de sobrefacturación más grande del informe está activo a junio 2026, con lo cual el bloque preventivo de facturas pasó de recomendación a urgencias. Supongo que me va a recomendar este. ¿Si querés puedo armarte como te puedo mandar este que estás viendo acá, te puedo armar uno parecido que detalle bien,

**Juan Ramos**: este último caso, el plazo, el rango del último 12 meses decís?

**Lucio Rojas**: No, el hallazgo más relevante. Dame un ratito que ahora cuando cortamos yo tengo otra reunión, pero te mando antes de la tarde solamente completo, sino el que mire ese caso en específico y vos podés auditar a ver si lo que hicimos tiene sentido. Y ahí nada, la salvedad, no sé si está bien o está mal. Si está bien, esto me deja mejor parado.

**Juan Ramos**: Si está mal, no, no, igual

**Lucio Rojas**: no

**Juan Ramos**: pasa nada porque puede ocurrir, sé que estamos ahí jugando con esto, no cambia

**Lucio Rojas**: mucha más fuerza siempre en manos de un analista interno porque el detalle, yo soy la escuela que sabe la herramienta. Y nada, creo que los pasos como preguntaba yo no sé si los tengo súper claros, pero es esto. Podría hablar con Bruno si avanzamos, que sea una relación un poco más formal. Nosotros en la actual concepto gratuita y con todo lo de Verónica auditoría, para nosotros el gol es conectar la base de datos y que ustedes puedan encontrar casos de bus. Requerirá mucha coordinación con Cristian de cómo hacerlo. Qué parte de base de datos, su base de datos es muy grande, eso tiene los costos, pero creo que va un poco por ahí los próximos pasos y supongo que lo llevarán eso más de la parte con agua.

**Juan Ramos**: Sí, yo creo que acá a veces lo que simplifica, si bien sigue siendo como ustedes dicen, prueba de concepto y demás, a veces la decisión simplifica cuando uno ve algo, llamémoslo revolucionario, que vos decís che mirá, realmente hizo esto muy fácil, muy rápido y me mostró algo que hoy, llamémoslo el trabajo rutinario humano y demás, no lo está enganchando. Entonces ahí empieza como a generarse ese ese deseo de dame más, dame más inteligencia artificial, dame más Theramot y bueno, siempre luchando contra los de sistema que te dicen guarda la base de datos, guarda esto, guarda lo otro, pero bueno, me puedo encargar yo, eso lo sabemos

**Lucio Rojas**: y por eso estamos acá con vos,

**Juan Ramos**: de luchar internamente contra los sistemas. Yo lucho y al final del día reporta mis historias, temas, a lo sumo me rajan a mí el día que algo se rompa Pero sí, es como que tiene que estar ese convencimiento. Claro, no sólo mío, sino de quién es mi reporte en ese área. Inventemos, el gerente contable hoy tiene, además de impuestos y administración, tiene cuentas a pagar. Si yo miro esto y este tipo lo ve y me dice, che, no, está está muy buena, detectó estas cosas que no las tenía, después fluye y sale como piña. Distinto es si viene el informe, che, no, pero esto no es así, esto ya lo vimos tres veces, Juan, vos te olvidás, yo ya te lo comenté en cinco directorios. Después arranca la cuestión natural de qué te dice la persona a la que le llevas el descubrimiento. Entonces yo buscaría lograr eso, de que cierre por ese lado. Y después si vos me decís cuál es mi mundo ideal, y sí, que yo llegue a la mañana y tenga siete cosas distintas en cloud, donde miro todo, interactúo, boludeo, pregunto, y los directores que laburan conmigo hacen lo mismo, es mi ideal. Y capaz que el del accionista, el ideal es si el día de mañana un equipo de 60 pasa a ser un equipo de 7 y hace lo mismo.

**Lucio Rojas**: Claro.

**Juan Ramos**: Pero bueno, después las cosas tienen que funcionar y no fallar. Y que el ojo humano esté detectando cosas que puedan ser errores, fallas, conclusiones erradas, bueno, ahí empieza un poco todo eso. Pero si fuera por una cuestión de visión, mirada y grupo HZ, me parece que es una esponja en ese aspecto. Lo que pasa que nos cuesta entrar en eso.

**Lucio Rojas**: Pero bueno, eso te digo, aprendimos un montón de varias reuniones que tuvimos con empresas grandes, que por ahí se siente reticente a esto, y la forma de entrar por negocio, por el top del negocio, y para que bajes del top de negocio, el caso de uso tiene que tener valor y que diga cheque.

**Juan Ramos**: Por eso digo, estamos viendo esto, ojalá, digamos, yo cruzo, yo quiero más que ustedes, que lo que me pasen, ese entregable sea algo que sí, mira, fantástico, porque eso me dice, che, mira esto, bueno, metamos además de esto, metamos cuentas a cobrar, metamos cualquier cosa, invento impuestos, metamos esto, che, vamos con todo el esquema nuestro de reporting, todo el esquema nuestro de forecast, pero bueno, es como que necesitamos esa sensación concreta de hay una mejora. Habiendo metido esto acá, o sea, para que vos te des una idea, yo desde mi ámbito de laburo, y me considero bastante ignorante en esto, todo el tiempo estoy usando inteligencia artificial en algo, o en que no sé, desafío un reporte del no sé qué, armo un informe sobre tal negocio, tal potencial esquema societario. Estoy todo el tiempo mirando algo desde otro lado. No es que cruzo base y hago locura. Sí, por ahí los cierres contables de esto que te conté los vengo midiendo un poco. A veces miro que hace la versión premium que tengo de GPT, después voy con Claudi, comparo, miro. Pero yo estoy en una etapa del hombre de piedra, al lado de lo que pueden hacer ustedes. Pero las ganas, digamos, me sobran. Es cuestión de ser bien efectivos. Hacemos tal cosa y pegamos acá. Y bueno, después iremos creciendo, ese es el punto. Pero yo no les puedo decir más que che, necesitas datos, dale, yo ahora hablo para que te abran el grifo. Pero tiene que aparecer algo después que sea superador en lo que hacemos y en la estructura que usamos para generarlo, etcétera, etcétera.

**Lucio Rojas**: Bueno, si te parece, para ir cerrando, yo te avanzo con este reporte que me pasó con el caso y seguimos trabajando con Velo. Nosotros a Velo le estamos haciendo como un apadrinaje que es para nosotros confundido. Lo vamos a hacer para que ella entienda la herramienta, la pueda probar y dé resultados. Si ella da resultados, a nosotros nos repaga adelante.

**Juan Ramos**: Igual te diría, te diría lo de ella. Capaz me mostraste un pedacito de lo que está haciendo ella, o me mostraste todo. ¿Pero ojo que a qué voy? Podría fallar algo en la mirada de ella o en la relación de ella con ustedes, y tal vez a mí no me interesa. Igual por ahí ella te dice, no, esto no sé, lo vi, pero no, que pin, que pan. Y capaz que yo vos me mandas esto y me empiezo a entusiasmar y me junto con el gerente que tiene cuentas a cobrar y me importa nada auditoría, voy porque me interesa a mí, no nos limitemos.

**Lucio Rojas**: Buenísimo.

**Juan Ramos**: Son cosas excluyentes, vamos en paralelo. Ojalá le encante, ¿Qué más quiero yo? Pero si no le encanta, igual no está perdido el tema. Yo lo quiero seguir, por eso te pedí la info. Y bueno, si es por mí, iría con todo, pero me sobran ganas, me falta cabeza para pensarlo.

**Lucio Rojas**: Bueno, te damos la mano con eso. En un rato paso una minuta con con toda la información.

**Juan Ramos**: ¿Te mando por Dale mi correo lo tienen, no?

**Lucio Rojas**: Sí, sí, sí, lo tengo, lo tengo y después

**Juan Ramos**: vayamos hablando y bueno, piensen ustedes cualquier propuesta yo la voy a escuchar y quiero hacerla.

**Lucio Rojas**: Buenísimo, buenísimo.

**Juan Ramos**: Hablemos pronto, ojalá hablemos pronto. Vuélvanme loco. Dale, gracias.

**Lucio Rojas**: Gracias, Juan.

**Juan Ramos**: Chau, chau. Hasta luego.

**Lucio Rojas**: Gracias.
