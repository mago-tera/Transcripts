# Entrevistas a ICP Teramot- Federico Orsi

**Fecha:** 2026-08-28T19:00:55.941+00:00  
**Duracion:** ~33 min  
**Participantes:** Federico Orsi <federicojorsi@gmail.com>, Lucio Rojas <lucio@teramot.com>  
**Externos:** federicojorsi@gmail.com  
**Apollo ID:** 6a91e2c57a04a2000c5cc7ab

---

**Lucio Rojas**: Ahora sí. Ahora sí. Decime si me escuchás.

**Federico Orsi**: Dale, te escucho. ¿Cómo va? ¿Todo tranquilo?

**Lucio Rojas**: Buenísimo. ¿Todo bien? Todo tranquilo. Todo bien para mí tanto tiempo. No sé si vos acordás mucho de la charla que te hice, que nos conociste.

**Federico Orsi**: Sí, me acuerdo. Fue hace varios años. No me acuerdo hace cuánto, pero sí, ahí en la UCA fue hace varios años.

**Lucio Rojas**: Sí, me acuerdo que habíamos hablado algo de finanzas, me acuerdo mucho del tema, pero había algo, me parece que finanzas

**Federico Orsi**: personales, la verdad que mucho no me acuerdo, la verdad tampoco a la uno, viste, no piensa de.

**Lucio Rojas**: Y otra vez.

**Federico Orsi**: Y me parece que había sido algo de finanzas personales, si mal no recuerdo.

**Lucio Rojas**: Sí, me acuerdo que habías ido medio escondido, porque vos estabas más como del lado austral, ¿No? Hacer mucha, mucha bulla. Sí, sí, me recibí el año pasado. Igual ya venía laburando de hace bastante en esto que te voy a contar. No te quiero robar mucho tiempo, así que. Nomás con vos, por las dudas, la reunión. Después quiero que me cuentes un poco de vos y por qué estamos acá. Yo te invito. Antes de recibirme, empecé a laburar una startup, vi que está relacionado con todo el tema de Rosario. Es una startup que es Venture Capital, tenemos inversión afuera, estamos yendo a buscar una serie A.

**Federico Orsi**: Me encantó este camping.

**Lucio Rojas**: Sí te la cuesta. Es de acá de Rosario. Y siempre nos dedicamos a resolver un problema, que era que los modelos de inteligencia artificial no trabajaban muy bien con los datos, sobre todo empresariales, en lo que es BB, por problemas de seguridad y también por problemas de restricciones técnicas, de que no entienden esas bases de datos. Entonces desarrollamos una plataforma intermedia que lo que hace es permitirle a cualquier usuario de negocio, sin ser técnico en datos,

**Federico Orsi**: sin tener

**Lucio Rojas**: la especificidad, un data engineer, data analyst, poder generarse su información. Que fuimos descubriendo que nosotros teníamos una tecnología muy potente, pero que para salir a distribuir la patentábamos y funciona. En muchos casos uso, pero para salir a distribuirla necesitas tener un enfoque en alguna ICP puntual y entender un poco los dolores de esa. Y en eso estamos.

**Federico Orsi**: Y hoy que armaron una. Yo chusmé un poquito la página,

**Lucio Rojas**: que

**Federico Orsi**: armaron un SaaS, digamos, que es para todo lo que tiene que ver con inteligencia artificial aplicada a la finanza, o sea, resolver automatizaciones, reporting.

**Lucio Rojas**: Sí, Ahora los método directo si querés, en el producto, nosotros lo que hacemos, nos conectamos a cualquier fuente de datos, no sé qué se te viene a la cabeza, pero algún SIP, algún sistema interno, cualquiera que esté trabajando ahí, algún tipo de empresa, y leemos, interpretamos toda esa base de datos y levantamos una capa semántica para que los entiendan. Eso, vos conectas toda tu base de datos a Cloud, ahora vamos a ver cómo funciona, pero a partir de eso puedes pedir todo lo que son tus reportes que vos haces con la parte finanzas, supongo yo, ahí está un poquito más de agua, pero armas todo el ETL que se dice, ya tenés el reporte automatizado, entonces a medida que se actualiza la base, se actualiza el reporte, ahora vamos a ver un ejemplo de cómo se crea eso, y algunos reportes que vos podés armar. Esto nace del dolor de cuando los equipos que nosotros suponemos, se bajan toda la información del sistema y empiezan a cruzar esas tablas en Excel, en macros y demás. Y nada, estamos empezando a ver que nos pasa. Yo tengo una ex compañera que me decía, entre una empresa corre una macro que me saca un resultado que no tengo ni idea cuáles son las fórmulas que hay atrás. Y la idea de esto es darle visibilidad a todo eso y que los equipos de control y gestión y finanzas se puedan armar sus propios modelos de datos. ¿Querés ver una demo ahí de la?

**Federico Orsi**: Y acá vos me estás diciendo que son aplicables, o sea, tienen algunas verticales de industria o alguna problemática puntual, ¿Qué tipo de reportes hacen batchets o resultados? ¿Tiene alguna especialización o es cualquier tipo de reporte que vos quieras?

**Lucio Rojas**: No, es cualquier tipo de reporte que vos quieras, porque lo que haces es dejar que el LL lo arme, yendo directamente a tu

**Federico Orsi**: los templates que ustedes tienen ya predefinidos, nutriéndose de los datos de las empresas.

**Lucio Rojas**: No tenemos templates, o sea, es una buena idea, por eso estamos construyendo como la vertical. Nosotros lo que hacemos es conectar la base de datos y darte a vos Claude supongo que está en contacto con todas las guías, y le decís a Claude cuál es el reporte que necesitas sacar, y como ya entiende perfecto toda tu base de datos, va y lo corre directamente y te lo devuelve y lo puedes empezar a analizar y a consultar toda esa parte, generación de la información. Voy a compartir. Vos en qué puesto estás. Bien. ¿La parte de finanzas, estás ahí escuchando un poco tu recorrido de ese lado?

**Federico Orsi**: Sí, sí. Yo tengo mi propia empresa, mi propia consultora, hacemos asesoramiento en finanzas corporativas, lo que es evaluación de empresas, M A, movilizaciones, toda la parte contable, así que tenemos varios clientes, pero toda la parte de asesoramiento corporate con la pata más corporativa. Está bueno, está bueno. ¿Quiere mostrar un poco lo que hace? Está interesante.

**Lucio Rojas**: Voy a compartir pantalla y ahí anda yéndome las preguntas. No sé hasta dónde llegas del lado técnico, pero la función. Esto es nuestra plataforma, que nosotros tenemos SaaS también puede correr en la infraestructura propia del cliente. Y lo que hacemos es generar los conectores. Acá puedes elegir las distintas bases de datos a las que vos te vas conectando. El sistema puede correr en múltiples bases de datos o nos podemos ir directamente al sistema en sí. Por ejemplo, tendremos conectado a SAP clientes. SAP tiene HANA, que es la nube, y SC que es la versión anterior. Snowflake también te puedes conectar.

**Federico Orsi**: También a QuickBooks te puedes conectar, sí. ¿A cuál QuickBooks tienen o no, Es

**Lucio Rojas**: algo específico del área?

**Federico Orsi**: Un software contable que con un montón de empresas que tengo en Estados Unidos laburamos, usamos QuickBooks, así que también puede estar bueno como para que lo.

**Lucio Rojas**: Lo vamos armando en el aire, un poco al avión de los conectores, porque generalmente va a ser la medida que te piden y eso está todo estandarizado. Y la velocidad de salir un nuevo conector es una semana. Lo vas poniendo, lo vas poniendo, vamos pidiendo lo de los clientes. Entonces acá hice un ejemplo donde conecté el SAP sintético anonimizado de un ex caso de uso que tenemos. Está llevado a una Bitcoin. Entonces nada, no sé si has trabajado directamente aparte de sistemas, pero ver una tabla de SAP es ver encabezados y tablas que uno generalmente no. No tiene forma de deducir de una manera lógica, pues se llama PC.

**Federico Orsi**: Ni idea de lo que estamos hablando.

**Lucio Rojas**: Genial. Entonces, ¿Qué haces? Vos tenés el sistema conectado a TENAM. Acá nosotros quedamos como metadata que se llama, que vamos diciéndole al conector, esta tabla significa eso, este dato está al tal lado. Esta tabla se vincula con esta otra de esta otra forma. Y ponemos todo adentro de un MCP, no sé si está familiarizado con todo lo que es la parte de mcps. Entonces conectamos todo el sistema del cliente. Y acá ya empezás a hacer todas las preguntas específicas y te empezás a interiorizar en los datos del cliente y te genera reportes a medida de ir charlando con Cloud. Entonces yo le digo acá voy usando la herramienta nuestra y le digo, bueno, puedes conectarte a Theramot, al webinar de control y gestión, que se llama así el caso de uso, porque lo usé para un webinar, y decime qué dato ves en mi fuente. Entonces te va diciendo que vos tenés 71 tablas conectadas a tu SAP, y tenés las que están relacionadas a Contabilidad y finanzas, a Controlling, activos fijos, a Compras, a Ventas, a Materiales, a Business Partners y demás. Entonces uno que empieza, empieza a generar información con el sistema directamente desde acá. Y Claude te va a buscar la información y ya te la deja estructurada. Vos ya te podés ir generando los reportes. Ya tenía unos reportes creados, habíamos creado a partir de la herramienta algunos estados de resultados, algunos flujos de caja, algunas tablas de rentabilidad, pero le dije, bueno, decime además qué otra cosa podés crear. Me dice, bueno, en base a todos tus apps que vos conectaste, puedes crear reportes de balances y posiciones financieras, las tablas a las cuales va a buscar la información y las cruza, puede hacer análisis de compras, análisis de ventas comerciales, hacer activos fijos y demás. Entonces la idea es que vos te sientes directamente contra un modelo a preguntarle qué reportes que es. Si nosotros queremos un reporte de balance y fusión financiera, le decimos a Claude, bueno, hagamos este reporte. Y te empieza a generar el cruce de información desde las tablas del sistema envío, ya te deja el transporte unificado. Dice, bueno, perfecto, vamos a hablar de un reporte de balance, situación patrimonial, entender bien las estructuras de las cuentas y los movimientos contables, las tablas clave, y va a mirar directamente el sistema y empieza a entender toda esa información para armar reportés, discutir un montón. Yo quiero formular así, la verdad que no soy muy específico de la parte de finanzas. Nosotros nos fuimos para SACP porque entendimos que es por ahí donde más hay problemas en control de gestión, de cruces de información, de necesidad de ir a las tablas y estar un poco lejos de la parte de sistemas que les puede proveer esos cruces de info. No sé qué has visto vos mientras esperamos que después si querés que te haga alguna pregunta la herramienta, pero qué has visto vos, tu experiencia en el área de finanzas, de problemas de acceso a la información, de reportes, si has visto mucho trabajar con Excel, bajada de plantillas.

**Federico Orsi**: Sí, creo que depende mucho del estadio de desarrollo de la empresa. Creo que cuando recién arranca esto, mucho más en Excel y después empiezan a tomar algunos sistemas. Igualmente no todos los sistemas tampoco son se puede generar toda la información con un clic, con lo cual si podés lograr todo esto está bastante bueno, porque por ejemplo, sí hay muchas empresas que laburan mucho con los Excel, que obviamente te lleva tiempo, tenés posibilidad de errores, cualquiera puede borra, saca y nada, no tenés registro, trazabilidad, y después si tenés otros casos de empresas que ya tienen su sistema, pero también el sistema tampoco es 100 confiable en muchas cosas, o sea generar reportes como vos querés, entonces después lo tenés que exportar y armar en Excel. El Excel.

**Lucio Rojas**: A eso iba, ponele, vos ya tenía un sistema definido, no tenía armada toda la operación de la empresa, y querés sacarte un reporte nuevo, querés un análisis de lo que viene pasando dentro de la empresa, cómo te genera esa información en lo que vos ves de tu cliente, de tu experiencia en el área de finanzas, tenés que llamar al sistema, tenés que pedir las tablas, hay que bajar, tiene que usar, cómo es un poco la dinámica que ves de generación

**Federico Orsi**: de información, en el caso que lo tengamos hacer nosotros en el Excel, Excel llevamos todo y lo mostramos como queramos. En el caso de que sea un desarrollo de sistema, tienen que hablar directamente con UDO o con el proveedor de sistema como para que le arma el desarrollo a medida de lo que necesita, que a veces hasta tiene un costo adicional eso ¿No?

**Lucio Rojas**: ¿Y cuál es un ejemplo de reportes que vos generás o que necesitas y que no están por default en el sistema o que tenés que generarte vos? ¿Estos templates que vos te imaginaste cuáles serían?

**Federico Orsi**: Y a ver, estado financiero típico, que es un estado resultado, un balance, un cash flow seguro, pero a veces con determinadas partidas que a veces no están en la contabilidad, que hace un EBITDA ajustado, o querés aperturarlo por unidad de negocio y después ver los márgenes o sea el Excel se puede toquetear un montón, pero obviamente está mucho mejor si te lo pasa directamente una IA, o mismo un dashboard con algunos KPIs, con algunos gráficos, también está bueno. Después una especie de presupuesto gadget para adelante, o algún variance, análisis, todas esas cosas las hacemos bastante bien.

**Lucio Rojas**: ¿Y qué hacen? Tipo, vos tenés tus clientes, ¿Se lo haces para clientes o lo haces internamente para tu empresa?

**Federico Orsi**: No, no, generalmente para terceros.

**Lucio Rojas**: ¿Y cómo te haces de la información esa que vos necesitas para hacerle el análisis financiero? ¿Accede a su sistema, te manda las tablas, te manda los resúmenes, el balance,

**Federico Orsi**: medio kilo? Depende del caso, en algunos casos entramos al sistema, en algunos casos nos pasan los Excel, que a veces vienen errores. Aparte lo que tienen que tener en cuenta también, que seguramente ya lo vieron, o sea, en Argentina está lo blanco y lo negro, lo hay, lo ve, entonces también muchas veces en la contabilidad no está todo, hay que estar. Una parte también complica, a veces puede llegar a complicarte un poco todo este tipo de cosas que haces, o mismo también a veces lo que se complica un poco, nosotros usamos mucho QuickBooks, por eso que era el que yo te decía antes, porque trabajamos mucho con empresas del exterior, no tanto con Argentina. A veces QuickBooks tiene limitaciones, como que no te logra hacer bien las consolidaciones de distintas empresas, y esas son algunas limitaciones que tenemos. Puede ser un problema para que lo tengan en cuenta también.

**Lucio Rojas**: Sí, acá la idea es que vos puedas cargar información de información de distintas empresas, o si vos tenés un grupo económico y usan distintos sistemas, estandariza todo para poder cruzarlo fácil. Pero bueno, a mí me interesaba puntualmente saber cómo estaban laburando hoy en día con esta generación de información, y también si estaba usando algo de AI en el medio. Si venís usando cloud, cómo hacer para usar la AI con los datos del cliente para hacer análisis, te animar a subirlo, como vienen Por ese lado

**Federico Orsi**: usamos mucho, a veces si subimos datos, somos muy precavidos en cuanto a ciberseguridad, creo que hay que tener bastante más cautela en algunas cosas, pero creo que en la práctica no se hace. ¿Qué más? Sí No, creo que la IA es fantástica. El tema es que bueno, hay que saberla llevar, entonces si tenés templates, a veces le enchufamos, viste, Quiero armar algo similar con esto. Ahora se te hacen mucho los HTML en vez de hacerlos en Excel, todo

**Lucio Rojas**: lo que son tableros, sí haces tipo el artefact, Le pedimos un análisis de reporte de balance y posición financiera, me dice perfecto, yo tengo que estructurar eso. Fue, miró las tablas, fue a ver cómo estaba esa información y empieza a autodebatirse de cómo se tiene que generar ese reporte para ya dejar todo. Y lo que hizo es meterse en el sistema, identificar las partidas, los activos, los activos no corrientes, los pasivos corrientes, los activos corrientes, el patrimonio neto, tuvo en cuenta todas esas cuentas y armó directamente la tabla. Acá en el sistema seguía estando, acá pedan solución patrimonial. Entonces a vos ya te queda definido el análisis nuevo, sin que tengas que volver a hacerlo, como que lo haces una sola vez. Y a medida que se actualiza el sistema del cliente, ya te automatizas. Esto lleva un reporte mensual, ponele, ya te queda esto creo que vos llamás el templo, te queda como el ETL hecho. Se dice que extraes los datos, los transformas y los mantenés vivos siempre de una misma manera. De una misma forma. Acá vos ya le podés decir directamente que te genere un dash o un análisis. No sé si tenía una pregunta, justo te interrumpí. Ahí en el medio.

**Federico Orsi**: Patentaron. ¿Qué es lo que tienen patentado con el software plataforma?

**Lucio Rojas**: Claro, nosotros lo que patentamos es la tecnología, que lo que hace es poder entender la base del cliente, estructurarla y disponibilizársela a la IAI para poder hacer lo de finanzas. Nosotros en el medio resolvimos muy bien todo lo que es la ingeniería de datos sería antes lo que tenía que pedir un equipo de sistemas, ahora lo pueda hacer agentes de IAI de forma autónoma. Este proceso que ahora nosotros estamos viendo acá y lo vemos automático, antes tardaba tres a seis meses algunas empresas hacer nuevos reportes o pedirse un sistema directamente del consultor del negocio, persona negocio de finanzas que se arma. Entonces la tecnología esa que patentamos, eso es la patente que tenemos en Estados Unidos. Y lo que estamos haciendo es empezar a ir a verticales. Te pedí que me haga un dashboard directamente con la tarea que hiciste, pero esto es un poco más el uso de cloud que decíamos. Pero bueno, acá sepan no robar de más tiempo. Más que una demo, la idea era una pregunta puntual, honestamente, sin que esto sea en ánimos de evento además. ¿Qué te parece la idea? Si sentís que es un dolor real, si escuchaste a alguien que haga algo parecido, te pueda llegar a servir en el área o la industria.

**Federico Orsi**: Sí, he visto varias gente que está tratando de hacer artes, estas cosas, por ejemplo con chicos están haciendo como una IA para facturas, deportes, la verdad que creo que está bastante piola, sea específico que haga alguien esta cosa. No lo vi, también le veo muchas veces como puedo decir, pero me pasa a mí mismo en mi consultora, o sea es como que siento que muchas veces la IA dónde está el valor agregado de algo que uno puede hacer con su propio cloud. ¿Yo creo que lo que tiene que ver ustedes es que están enchufados a los conectores, a todos los programas y eso tiene un lindo valor área, porque sí, a ver, yo creo que las empresas más grandes que tienen SAP por ejemplo, creo que pagan una fortuna de SAP, están bastante ordenaditas, pero sí, obviamente los reportes de SAP no son los mismos que teres armar, no? Mi duda es. Yo creo que sí, yo creo que está bueno, yo creo que está bueno si el software se logra enchufar en los sistemas de los clientes y vos le podés pedir que te genere los reportes directamente tomando ahí lo veo útil. Distinto sería si vos podés descargar lo crudo, lo tiras a cloud y armas tu propio report, que vendría a ser algo muy parecido, pero te lleva más tiempo y ahí creo que está la ventaja de lo de ustedes.

**Lucio Rojas**: ¿Sí, y la segunda ventaja sobre eso es que si vos tiras el crudo que te baja del sistema, se tiene que estar actualizando todos los meses, va a tener que tirar el club de vuelta y esto es como que ya queda enchufado y estandarizado, entonces ya sólo se actualiza a medida que se actualiza el sistema vivo yo de un lado y bueno, a mí quería charlar un rato con vos sobre eso, es un perfil que como te dije por LinkedIn está copado porque suma startups, valor más finanza, por ahí algunos consejos, algunos comentarios me sirven? ¿Mucho y creo que estaría bueno no?

**Federico Orsi**: Y eso puede estar bueno porque ya como que fijas un poco cómo va a ser la tabla, vos querés armar un pianel y ya fijaos acá, no se, querés armar un balance, OK, activo corriente con estas partidas, pasivo corriente con estas partidAs ya tenés una estructura de reporte sin que piense de cero. Creo que está bueno, está bueno. A ver, no te digo para nosotros, porque nosotros para nosotros no lo hacemos, pero sí puede llegar a estar bueno tenerlo en cuenta para unos clientes que necesitan reportes o cosas, puede ser una linda alternativa, así que yo lo tengo en cuenta.

**Lucio Rojas**: Sí, por eso era más que no tanto de venta. Sino te hago una pregunta más nomás. Ya te dejo tranca que a las 5 me dijiste tenía que dar clases. Si vos tenés que apuntar a una persona dentro de lo que es el mundo de finanza, de control y gestión, que sería la que dentro de una empresa se crearía estos estos reportes, un puesto que yo le pueda ir a hablar, ¿Quién sería dentro de todo el universo? ¿Tenés más o menos mapeado?

**Federico Orsi**: Para mí sería más tipo el CFO si es que tienen o más gerente de administración y finanzas o los contadores dentro de una empresa, pero me parece que sería más el líder o gerente de administración. Sí, sí, o el CFO en caso de tenerlo. ¿Pero bueno, para eso, para tener un CFO tiene que tener un poquito más de empresa, un poquito más madura,

**Lucio Rojas**: así que no te reto con miedo eso y analistas y eso demás no has visto? Nosotros trabajamos para YPF y los analistas agarraron esto y se hicieron internamente reportes para el resto del equipo. Quiero saber si algo particular de la pesa que los tenía o anda por todos lados puede ser.

**Federico Orsi**: Al final de cuentas el que va a generar el reporte va a ser el analista, no lo va a hacer el CFO, pero el analista cumple órdenes, con lo cual me parece que si vos tenés que elegir a alguien para ir a vendérselo, es al que toma la decisión, no sé si tanto al que lo usa. En mi caso, por ejemplo, mi consultora, yo los reportes no los corro, yo los leo cuando están listos, pero los analistas son los que cargan los datos, entonces para mí ir a venderle al analista no sé si es lo más útil, más allá de que sea el usuario final,

**Lucio Rojas**: algo más top to down, no entrar como por.

**Federico Orsi**: Y yo entraría más por el tema de lo mismo, o tal vez te diría, o tal vez hasta puede llegarse con los dueños de empresas, porque hay empresas que son bastante pyme que pueden ser. El dueño no tiene reporte y le encantaría ver cosas, entonces tal vez no sé si es tanto el gerente, tendrá que ver el perfil de las compañías, pero a veces los mismos dueños de la empresa no tienen ni idea número y lo hacen los contadores y esos contadores solamente liquidan los impuestos, no le dan información o reporte de verdad. En ese caso creo que también lindo caso puede ser dueño de empresas medianas sería, porque por lo que vi también el precio que tenía la plataforma usted no me parece caro para nada, con lo cual no creo que sea un dolor de cabeza para una empresa.

**Lucio Rojas**: Bueno, nada, son un set de preguntas esas que no quieres mucho tiempo, tratar de la mayor cantidad que puedo tener varias por semana para conocer un poco al usuario final, a distribuir bien el producto.

**Federico Orsi**: Está buenísimo.

**Lucio Rojas**: Bueno, por ahí. Así que bueno, gracias por el tiempito. No sé si tenga una pregunta más de la compañía.

**Federico Orsi**: Fantástico. No, te digo lo que sí está bueno saber lo que están haciendo. Creo que hoy va por ahí, así que en el caso de Zoe trabajamos bastante con, o sea, no tenemos muchos clientes porque nosotros una consultora a la vez, pero la mayoría son de afuera 60-70%. Pero te digo, en los casos que tenemos locales lo puedo recontra tener en cuenta para ganar. Así que obvio.

**Lucio Rojas**: Bueno, ¿De qué das clase? ¿Negocios digitales estás dando? No sé por qué me suena eso.

**Federico Orsi**: Todo finanza en confianza ¿Para qué?

**Lucio Rojas**: Para contadores.

**Federico Orsi**: Hoy tengo. Todo lo que yo hago.
