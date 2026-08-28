# BCR- Teramot POC DIYEE

**Fecha:** 2026-06-11T12:31:21.010+00:00  
**Duración:** ~28 min  
**Participantes:** Milagros Galassi <mgalassi@bcr.com.ar>, Ayelen Romano Bazan <aromano@bcr.com.ar>, Fabricio Riguetto <>, Lucio Rojas <lucio@teramot.com>, tomas rodriguez zurro <>  
**Externos:** mgalassi@bcr.com.ar, aromano@bcr.com.ar  
**Apollo ID:** 6a2ab118e89595001cd7b028

---

**Lucio Rojas**: ¿Qué tal Tomi?

**tomas rodriguez zurro**: ¿Cómo anda Lucio?

**Lucio Rojas**: ¿Todo bien? Bien. ¿Vos bien?

**tomas rodriguez zurro**: Todo tranquilo.

**Lucio Rojas**: Buenísimo. ¿Vas a estar vos solo o no dejaron solo?

**tomas rodriguez zurro**: La verdad que no sé si Emi se sube, Belu está de viaje, así que sí no se sube y Aye creo que ayer me dijo que se subía, pero no sé si se habrá complicado.

**Lucio Rojas**: No, no, igual hacía el chiste, son 31. Igual estaba, sabes que estaba pensando recién por ahí hasta que hacer eficiente las reuniones, por ahí hasta que agarremos la vuelta de las preguntas cómo me quieres hacer y demás. La reunión semanal tiene sentido, después yo propondría más algo cada 15.

**tomas rodriguez zurro**: Dale, dale, sí, obvio, más largo, no

**Lucio Rojas**: nos vamos a empezar a repetir temas. Así que nada, después de esto, una cada 15 va a andar bien. Yo ya te tomé como como usuario de referencia.

**tomas rodriguez zurro**: Listo, yo tomo el proyecto. ¿Hola

**Ayelen Romano Bazan**: buenas, cómo andan?

**tomas rodriguez zurro**: La verdad que para. No sé, teníamos dos consultas, una que te la adelantó Aye el martes creo que fue el tema de los tableros y la actualización, si es posible hacer tableros que estén como live, tomen los datos directo

**Lucio Rojas**: y la otra y la

**tomas rodriguez zurro**: otra no, para definir el esquema de la proof of concept, cantidad de tablas, usuarios, eso queda de nuestro lado. Si había una propuesta de su lado, no sé bien, no me quedó claro cómo avanzar.

**Lucio Rojas**: Ahí vamos con los demás. Pobre Aye, es como que toca un poco más la curva de aprendizaje y después cuando llega a ustedes quedan los temas un poco más pulidos. Cuando me preguntó cómo hacer lo de autenticación para dashboards, nosotros sabemos que se puede, es más, los chicos lo han probado, yo no tenía súper clara la respuesta técnica y lo que hace es una autentificación machine, que la herramienta que nosotros usamos para autenticar el MCP. En un momento cuando configuraste MCP pusiste rayo y client ID, Hiciste un client ID y un usuario, cuando te conectaste a MCP como que te autentificó contra nuestra plataforma. Bueno, para hacer esa autentificación desde alguna línea de código hice un tallo demás. Hay que coordinar esa lógica de autentificación que entendemos que es lo que te falló. Los chicos, yo ya pasé lo que escribí que me pasó ayer, me dijeron debe ser por esto, autentificación y ahí quedaría un poco más lo que solemos hacer en estos casos cuando hay que recurrir algo técnico, es que yo subo a vos con tu caso de uso, una cadena de mail con los chicos técnicos, un poco se solucione entre ellos y yo te voy siguiendo porque los muchachos ponen el mail, por ahí se dispersan. Dos semanas.

**tomas rodriguez zurro**: ¿Entonces para tener claro, la consulta seguiría siendo vía MCP y la API de Antropic, no? Directo al endpoint Atina, no terminamos resolviendo

**Lucio Rojas**: de esa forma más eficiente.

**tomas rodriguez zurro**: OK.

**Lucio Rojas**: Y ahí lo que haría es actualizar tu dashboard. Después ya queda de tu lado, por ahí podemos hacer que alguien lo investigue y que te ayude, pero queda un poco más de tu lado armar esa lógica para que se actualice el dashboard. Llamen un GP, que vi que lo estuviste haciendo igual, así que sería.

**tomas rodriguez zurro**: Perdón, perdón, no te escuché eso que

**Lucio Rojas**: vi que ya lo estuviste haciendo. Darle lógica al dashboard para que actualice. Actualizar el HTML o actualizas.

**tomas rodriguez zurro**: Sí, en principio sería actualizar HTML porque es una actualización diaria y cuando datos están subidos es simplemente actualizada.

**Lucio Rojas**: Hace un snapshot nuevo y lo cambia cómo. Hace como un snapshot nuevo de los

**tomas rodriguez zurro**: datos y lo cambia. Exacto. Sería como la IDE.

**Lucio Rojas**: Y nada, con esa misma lógica de la API Centropic y MCP podés llegar a armar algún chat como el que tiene el equipo que vimos anteriormente. ¿Te acordás?

**tomas rodriguez zurro**: Ponía como.

**Lucio Rojas**: Creo que tiene una similitud muy alta con la lógica esta del dashboard, riesgo de que los consumos de tokens quedan

**tomas rodriguez zurro**: un poco abiertos al público.

**Lucio Rojas**: Pero si hace algo de acceso controlado, por ahí estaría bueno alguna licencia y entra incluir lo otro. Entra aquí. Ahí incluí la como la feature del chat. Eso está bueno.

**tomas rodriguez zurro**: Sí, el tema directamente que se conecta alguna desarrollo propio al endpoint de Atina. Igual sigue siendo viable.

**Lucio Rojas**: Sí, sigue siendo viable. La respuesta que me dieron los chicos fue hacerlo, pueden City por ahora. Si vos querés hacer la otra opción, tendría que evaluarlo con ellos a ver cómo se hace y también poner contacto con vos.

**tomas rodriguez zurro**: OK, dale.

**Lucio Rojas**: ¿Vos que tenés alguna preferencia con lo de Atina por algo?

**tomas rodriguez zurro**: Sí, por el tema, el posible consumo. Si, ya pudiese ir explorando cómo es esa conexión para los desarrollos tanto de los tableros HTML como. Porque lo mismo la tablero HTML estamos viendo. La idea es después como que estén disponibles en un micrositio estadístico que a su vez tiene el chat y que el usuario puede ver tableros ya desarrollados, o el usuario externo, o hacer consultas ad hoc. Entonces, bueno, si ya tuviésemos esa conexión, entonces ya tengo más o menos alguna tabla de prueba para ver cómo reacciona en base a esa información que está ya estructurada de cierta manera. Sería básicamente el último tilde que nos faltaría para darle de alta el proyecto, por así decirlo.

**Lucio Rojas**: Yo entiendo que lo de MCP igual lo que hace es, con la llamada que vos le das, hacer como esa. Hace esa visualización a Tina, al encuentro Tina, está incluido dentro de la Tool, lo único que ellos te dan además una conexión que también te permite hacer otras cosas, ¿Entendés?

**Ayelen Romano Bazan**: Claro, pero ahí por el medio usa Cloud, digamos.

**Lucio Rojas**: Usa la P. Claro, claro.

**Ayelen Romano Bazan**: Pero ahí estaría consumiendo, Creo que lo que va Tomás es que ahí estaría consumiendo tokens de la cuenta de Cloud están usando. Claro. Y si lo quieren liberar al público en general, ahí el consumo se puede disparar muchísimo.

**Lucio Rojas**: Perdón, me había olvidado que ustedes querían hacerlo de su modelo propio.

**tomas rodriguez zurro**: Claro, claro, claro.

**Lucio Rojas**: El modelo mire a la tabla de Atina.

**tomas rodriguez zurro**: Exacto.

**Lucio Rojas**: Ese modelo mira a través de NCB. ¿No sería más o menos lo mismo poder permitir que se conecte tu modelo?

**tomas rodriguez zurro**: Creo que puede ser una opción, me tengo que poner a investigar, pero creo que puede ser una opción de modelos locales que se conecten vía MCP con Atina.

**Lucio Rojas**: Yo, porque el MCP tiene un montón de tools que instrumentan un poco la. La relación con nuestra herramienta y lo va eligiendo cómo llamar autónomamente, por ejemplo, te hace un Creative Table, te hace un Query Data, un Query cómo, te pones a ver las tools y un montón listadas y como que la va eligiendo en función de lo que necesita, y creo que salteárselo para ir a. A la tabla final es como perder un poco el desarrollo que nosotros ya hicimos por vos. También puede estar la opción de que vos veas la tabla e instrumentes algo que entienda la consulta natural y haga la QL sobre esa tabla, y al fin y al cabo reinventar el MCB. Claro, básicamente,

**tomas rodriguez zurro**: sí, sí. Estoy pensando, por lo que estuve viendo medio por arriba en alguna de las clases de la maestría, o sea, hay como modelos de lenguaje específico fine tuneado para hacer query directamente SQL, pero puede haber algún modelo más general. El último que sacó Google es disponible, público, que tenga una conexión MCP directamente, o sea, conectarse con MCP directamente y vivir local.

**Lucio Rojas**: Vamos a hacer una cosa, yo hasta acá se extiende conceptualmente, se entiende mi parte que te puedo responder. La semana que viene si querés esta misma reunión la hacemos un poco más acotada, técnicos para tener la charla bien, yo les explico bien qué es lo

**tomas rodriguez zurro**: que yo aprovecho también a indagar un poco más,

**Lucio Rojas**: ellos te van a decir bien, si te conviene ir por MCP, te damos la tabla. Yo entiendo que ellos están como un poco más reacios que antes a darte el endpoint de la tabla, porque es menos productizable que hacer una conexión, esto sería algo bien ad hoc para ustedes.

**tomas rodriguez zurro**: Después un par de bugs que tengo en la. En la plataforma, algunas tablas que creé que las eliminé y no se eliminan.

**Lucio Rojas**: Sí me lo querés proyectar, dale eso, querés borrar la old y no te la borra.

**tomas rodriguez zurro**: Sí, toda la pantalla. Ahí se ve. Esta había quedado que es

**Lucio Rojas**: una de

**tomas rodriguez zurro**: las silver de una de las fuentes, que yo eliminé la fuente y eliminé los archivos originales, o sea que alimentaban esa fuente, pero sigue estando la tabla. Y después también lo mismo con esta gol, que la copié para probar cómo era para hacer alguna adición en la tabla nueva y la eliminé y cuando.

**Lucio Rojas**: Si no te elimina.

**tomas rodriguez zurro**: No, claro, no se pudo eliminar y sigue estando ahí,

**Lucio Rojas**: es un bug y por ahora lo están sacando y lo van a arreglar. Y después lo otro, me dejas ver en fuente de datos la que no puedes borrar.

**tomas rodriguez zurro**: Para la que no puedo borrar de la silver, tiene este nombre horrible, batch, que la habíamos subido mal a los archivos.

**Lucio Rojas**: Sí proyecto,

**tomas rodriguez zurro**: después borramos esa fuente y subimos esta, que subió bien, con un nombre feo pero subió bien. Borré la fuente, borré los archivos de esta sección, era un solo archivo, lo borré esta sección y cuando quería.

**Lucio Rojas**: Para borrar la tabla, desde fuentes no se puede borrar una tabla.

**tomas rodriguez zurro**: Ah, listo, silver,

**Lucio Rojas**: por eso quiero ver cuál es la fuente que le da origen a la tabla.

**tomas rodriguez zurro**: Ah no, ya no aparece, o sea la borré, era una. Estaba por esto hace 13 días, ponele, porque ha sido el viernes previo a

**Lucio Rojas**: esto y no la habías actualizado. Si cliqueas eso te abre el. No, está ahí seleccionado.

**tomas rodriguez zurro**: No, no está ahí seleccionado. Bien, párate

**Lucio Rojas**: está, Fíjate dónde hace. ¿Lo puede expandir?

**tomas rodriguez zurro**: Sí, no, porque esta tabla estaba mal subida por eso era como muy.

**Lucio Rojas**: Es la última línea, pero la última. Acá.

**tomas rodriguez zurro**: DJB Se fue el 28 de mayo,

**Lucio Rojas**: estoy peleando la feature de que podamos cambiar por lo menos con un alias en el front.

**tomas rodriguez zurro**: Debía aparecer previa a esta porque ya fue el primero de junio.

**Lucio Rojas**: Yo la eliminé. La eliminaste y ya nos fijamos dentro

**tomas rodriguez zurro**: de esa que no está.

**Lucio Rojas**: No, ya no está. Eliminaste la fuente, eliminaste el archivo y te quedó la Silver. Excelente.

**tomas rodriguez zurro**: Por las dudas que llegaba como fuente en alguna otra, pero

**Lucio Rojas**: no porque te hace el select a esa fuente, o sea, tendría que ser. Para mí se borró la fuente de la UI y no se borró el back. OK, eso

**tomas rodriguez zurro**: bien.

**Lucio Rojas**: Bueno.

**tomas rodriguez zurro**: Bueno, eso entonces lo técnico y lo otro. Queda entonces la parte de definición del

**Lucio Rojas**: LO, pero después todo lo que es uso de la herramienta, creación de Go, aprender a manipularla, fue cómodo.

**tomas rodriguez zurro**: Por ahora tampoco pude dedicarle mucho a estas cosas porque tuve otros temas esta semana y bueno, Elu se fue,

**Lucio Rojas**: no

**tomas rodriguez zurro**: estuvo, que también era otra que tenía acceso al proyecto, pero por lo que estuve pimponeando. Bien.

**Lucio Rojas**: ¿Y en cuanto a si vos has trabajado antes con estos Excel, usar la herramienta te sirvió a vos para administrarlo mejor o es lo mismo que estaba haciendo antes?

**tomas rodriguez zurro**: Se hace más eficiente la consulta de

**Lucio Rojas**: los datos y creaste nuevas tablas entre varias tablas, ¿Llegaste a hacer eso?

**tomas rodriguez zurro**: Una relación. Una relación, sí. Pero que no la tenemos, o sea que la hicimos exclusivamente como acá adentro, que no la teníamos relacionada en las excels.

**Lucio Rojas**: Solamente en esta plataforma.

**tomas rodriguez zurro**: Sí, exacto.

**Lucio Rojas**: ¿A partir de qué la relación, sabes?

**tomas rodriguez zurro**: A partir de qué. Campaña y fecha.

**Lucio Rojas**: Campaña y fecha. Hizo como un compuesto.

**tomas rodriguez zurro**: Claro, exacto.

**Lucio Rojas**: Bueno, para mí ese es el valor más grande de la herramienta, poder juntar varias tablas y por ahí crear nuevas gol en base a fuentes distintas y después también hacer gold con base a fuentes únicas está bueno, pero al fin y al cabo es como un súper formulador de fórmulas de Excel.

**tomas rodriguez zurro**: Sí, sí, obvio. Por eso definiendo un poco más el code, tenemos un montón de cosas que relacionar que hoy no las tenemos relacionadas. Cuando queremos relacionarlas hacemos medio ad hoc y que bueno, un flujo de ingreso de camiones y salida de puertos y ventas. Hay muchas cosas para hacer, pero eso, por ahí teníamos esta limitación.

**Lucio Rojas**: La primer parte de transformación de Beyoncé Silver con escuela esta que dimos para acomodar un poco los ex, ¿Te sirvió

**tomas rodriguez zurro**: la verdad, o sea no vi la transformación de bronce a silver, o sea

**Lucio Rojas**: la que vimos recién de la query?

**tomas rodriguez zurro**: ¿Sí, a ver pará que me ubico? Lo que más vi quiere decir es de silver a Gold.

**Lucio Rojas**: Claro, vos mirás cómo crea la gold, qué es la. Pero antes cada una de las tablas tiene una transformación que se llama los fixers, que lo que hace es acomodar un poco el Excel antes de hacerle análisis.

**tomas rodriguez zurro**: Eso lo vi, o sea no vi como errores en las tablas de que haya leído mal los datos o procesado mal los datos de los Excel.

**Lucio Rojas**: Y además de los errores te sumó valor, puede ser o no te sumó valor que los Excel ya los prepare para hacer análisis o ya.

**tomas rodriguez zurro**: Ahí me parece que lo que sumó valor fue tirárselos a Cloud y que me los estructure bien, ponele.

**Lucio Rojas**: Ah, porque vos hiciste eso antes.

**tomas rodriguez zurro**: Claro, sí, o sea, la verdad que no lo habíamos. También tenemos cloud team hace 10 días en la oficina, entonces estamos también indagando la herramienta, pero hay Excel que tienen errores de carga de datos, que se los tira Cloud para que me los limpie con determinados criterios, me los acomode

**Lucio Rojas**: correctamente y bueno, eso olvidado completamente que habíamos hecho eso antes de subirlo a la plataforma. Lo que hace la plataforma, antes de que Clot sea muy bueno haciendo eso, hacía prácticamente lo mismo de una confusión y errores. Cuando vimos que Claud lo hacía también dijimos bueno, a partir de ahora tenemos que hacer que esta parte, claro, nosotros como producto se la hemos a Clot para que lo haga también. Bueno, después de la parte del pricing, de la proof of concept, acá nosotros lo que hicimos con el otro equipo fue hacer una propuesta más ad hoc, porque no conocíamos bien el caso de uso, los límites, y dijimos bueno, vamos a plantear cantidad de tablas, cantidad de golds y hacer una propuesta un poco más cerrada, ¿No? Entiendo que en este caso va a funcionar mucho mejor por el uso que están dando. Respetar el pricing de la herramienta. Ustedes están ahora sobre una prueba gratuita de la herramienta. Yo realizo una red y plan no esta sobre la prueba gratuita de la herramienta. La prueba gratuita de la herramienta contempla hasta cinco tablas bo productivas, o sea que cinco tablas que a vos te encantaron y que sabes que la usar para armar el dashboard, esa sería una de tu headcount y mientras que estés ahí tenés libertades de uso, nosotros no te restringimos nada. No es que Tire gratuito tiene menos funcionalidades que el primer Tire Professional. La única diferencia limitante limitante de cantidad de GB de carga y storage, y de cantidad de tablas que puede hacer información que ustedes están manejando. Tampoco va a superar los límites de la herramienta en el Tire. Y la cantidad de usuarios tampoco. Y la cantidad de tablas bol ¿Que creen? Creo que va a ser limitante. Así que ustedes pueden usar la herramienta hasta llegar a la quinta tabla, y en el momento que realmente tengan la necesidad de pasar a la sexta tabla, tenemos que hacer un arquero de licencia. ¿OK? Eso tomarlo como una herramienta. En el otro caso es un poco distinto, porque tenemos que hacer una conexión web, cargar muchas tablas. El caso era un poco más complejo al principio y decidimos encararlo así, pero lo llevo yo desde el principio, me parece más eficiente hacerlo así.

**tomas rodriguez zurro**: Bien, la verdad que no tengo idea igual de los pricing, después obviamente la decisión no corresponde a mí, la toma Emilce o el director del área,

**Ayelen Romano Bazan**: Nos

**tomas rodriguez zurro**: podemos mandar por mail, si no hay

**Lucio Rojas**: drama, está público en la página, yo seguido el proyecto. Estos son los pricing de la herramienta. Ya con un starter te deja hacer hasta 20 tablas, actualizando y consumiendo 20 dashboards y son 5 usuarios administradores. Yo entiendo que está usando Woz y Emilce, así que dentro creo que estaría muy bien. Y después en caso de escalar proporcionalmente se busca ir a un profesional o a un enterprise, donde ya Enterprise si es algo más por consumo. Y bien, entiendo que para su prueba va a ser lo más sencillo también, ustedes ir evaluando, ver cuánto será, quién tener y demás.

**tomas rodriguez zurro**: Listo, perfecto. Me llevo una captura de esto, lo charro con Eddy.

**Lucio Rojas**: También, tenés un poco de información.

**tomas rodriguez zurro**: Bárbaro. Entonces, bueno, me llevo esto. Me llevo lo de indagar en la posibilidad de que los modelos locales se conecten VMCP y saltear la API de Antropic, la conexión de MCP con Teram, o sea del modelo propio. Lo de las tablas y la actualización de los datos en las tablas HTML. ¿Incorporas en una cadena?

**Lucio Rojas**: Sí, eso te incorpora en una cadena. Y si querés ahí podés redactar un poco tu caso, explicar bien para que los chicos lo vean y a la reunión la definimos. Si querés algo un poco más entre vos y ellos y quien quiera sumar, yo ya lo subo a ellos directamente.

**tomas rodriguez zurro**: Perfecto. Y nada, la verdad que esto no pude avanzar demasiado porque tuve otros temas, pero la quiero agarrar y dedicarle unos cuantos días a.

**Lucio Rojas**: Y como te digo, ya la semana que viene cuando puedan definir bien, podamos definir bien cómo hacer la parte de actualización de los dashboards y demás, contémoslo cada 15.

**tomas rodriguez zurro**: Dale.

**Lucio Rojas**: Sí, sí, obvio, hacer lo que fuera. Cuando tenga algunas dudas, analizá y nos conectamos porque.

**tomas rodriguez zurro**: Sí, sí, sí, no tiene mucho sentido las semanales. Perfecto.

**Lucio Rojas**: Bueno, Tommy, no sé si tienes alguna otra. Yo tengo una pregunta para vos. Conectamos ya las vistas son las que le puedes agarrar y revisar si son las que necesitaban, Si hay más. OK, todo bien.

**tomas rodriguez zurro**: Si querés probarlo.

**Ayelen Romano Bazan**: Dale. Sí, sí, me conecto y lo reviso. Dale, perfecto. Gracias.

**Lucio Rojas**: Yo rehace el otro día porque cortamos y se dio vuelta Facu y me dice ya está.

**Ayelen Romano Bazan**: Lo que pasa que nosotros nunca pensamos que se podía conectar ahí, fuimos directo a las tablas. Pero sí, con las vistas es mucho mejor porque ya están procesadas, hay un montón de campos que no tenemos, que son justamente los que no hay que mostrarle al usuario. Así que sí, si vamos por las vistas es mucho mejor, son usos volts

**tomas rodriguez zurro**: directamente,

**Ayelen Romano Bazan**: Así que perfecto, pudieron cargar eso.

**Lucio Rojas**: Y para nuestro caso creo que también corre un poco lo mismo que el Hija también recién. Si nos vemos el martes que viene, puedo empezar a juntarnos para periodo de tiempo. Bueno, no sé si alguien tiene algo más, cualquier cosa.

**Ayelen Romano Bazan**: Listo chicos, muchas gracias.

**Lucio Rojas**: Gracias, hasta luego.
