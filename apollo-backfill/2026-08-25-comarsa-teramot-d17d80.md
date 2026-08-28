# Comarsa <> Teramot

**Fecha:** 2026-08-25T15:03:03.712+00:00  
**Duración:** ~23 min  
**Participantes:** Mariela Niell <mariela.niell@drogueriacomarsa.com.ar>, Agustin Garcia <agustin.garcia@teramot.com>, Lucio Rojas <lucio@teramot.com>  
**Externos:** mariela.niell@drogueriacomarsa.com.ar  
**Apollo ID:** 6a8db43c1e55a2001cd17d80

---

**Agustin Garcia**: Hola Mariela, No te escuchamos.

**Mariela Niell**: ¿Ahora me escuchan?

**Agustin Garcia**: Ahora sí. ¿Cómo estás?

**Mariela Niell**: ¿Cómo va? Buenos días.

**Agustin Garcia**: Todo muy bien, por suerte. ¿Vos?

**Mariela Niell**: Todo bien.

**Agustin Garcia**: Me alegro mucho. Me alegro. No sé si esperamos a alguien más,

**Mariela Niell**: No de nuestro lado. No sé si Raquel se iba a unir a la reunión o no, pero bueno, eso después de última lo charlo con ella. Lo mío es simple, chicos, le voy a robar unos minutos nada más. La verdad es que lo estuvimos probando, tuvimos un par de datos de prueba, hicimos una consulta Gold, nos gustó, me interesa me parece. Hicimos el conector, la verdad que funcionó muy bien, lo conectamos a cloud. Me quedan dudas, dudas que tienen que ver con perfiles y planes. Vamos básicamente a eso, no tengo ninguna duda respecto a lo demás. Lo que me queda duda son más o menos lo que no puedo intuir, el tema de los permisos. ¿Los permisos son tablas de la base de datos o a consultas Gold o ambas cosas?

**Agustin Garcia**: Adelante. Sí, sí, te estaba dejando.

**Lucio Rojas**: Esta preguntando si los permisos serían los permisos de los usuarios que consumen de tu lado.

**Mariela Niell**: Exactamente, para armar información.

**Lucio Rojas**: Perdón ahí. En realidad los permisos son ambos. Vos podés gestionarlos a tu conveniencia a partir de una funcionalidad que tenés en la aplicación. Estaría bueno si vos la tenías abierta ahí como para revisarla. Si no te lo comento verbalmente, no hay problema. Que se llama datashare, está en el panel izquierdo, tenés la opción de datashear, y ahí lo que vos haces es compartir solamente tablas gold o tablas Gold y tablas silver, que son las de las bases de datos.

**Mariela Niell**: Y las tablas silver, o sea, yo puedo determinar a qué tabla silver puede acceder un determinado perfil. Sí, bien, perfecto.

**Lucio Rojas**: Vos podés elegir perfecto qué tablas puede usar el perfil. Pero para eso tenés que tener como el repositorio armado, que sería el otro proyecto donde ese perfil va a estar viendo para consumir esa información. Entonces de tu proyecto madre le mandas las tablas que vos elegís, tenés tipo un selector al proyecto del consumidor, y ahí a él le das el rol que vos quieras.

**Mariela Niell**: Una pregunta más, perdón Lucio, consulta es, ¿Yo puedo aislar campos? ¿Porque obviamente si yo te voy a subir una base de datos, no voy a decir, bueno, subo toda la base de datos porque no me conviene aislar un campo de una tabla, pero puedo aislar campos de la tabla a los perfiles?

**Lucio Rojas**: A los perfiles que vos le vas a dar la información tuyos internos.

**Mariela Niell**: Sí.

**Lucio Rojas**: Bien. ¿Qué tipo de campo sería? Sería nivel columna. Sería nivel fila.

**Mariela Niell**: Y a nivel columna voy a hacer nunca.

**Lucio Rojas**: ¿Y puedes armarte una Gol? Puede ser Gol de Gol.

**Mariela Niell**: Ah, OK.

**Lucio Rojas**: Armón una Gol que no tengo esas columnas y le pasas esa Gol.

**Mariela Niell**: Perfecto. Bien. Está bien. Es un gasto de una Gol, pero no importa. Vale. Lo vale. Y después tengo otra consulta más, que ahora sí voy al tema de los planes. La realidad es que primero se puede pasar de plan en plan, porque la idea sería, no quiero sobredimensionar y después que me quede grande, pero sí, bueno, quizás puedo arrancar con un plan intermedio y si después considero pasarme a otro. ¿Es factible?

**Agustin Garcia**: Sí, es factible. De hecho, nada, si querés contame un poco cuáles son tus expectativas de necesidad de uso y podemos ir adaptándolo y podemos armar, digamos, por algunos meses un plan a medida, digamos. ¿A medida? ¿A qué voy? Digo, no sé qué números estás manejando en cantidad de usuarios que sean más administradores, qué cantidad de usuarios, que tal vez si vas a tener usuarios más read only. Contame un poco. ¿Podemos armar más allá del precio de lista?

**Mariela Niell**: Claro. Mi idea es la nosotros actualmente tenemos esta distribución, porque sería la misma para casi todo, pero por eso no quiero que lo entiendan. Tenemos X cantidad de sectores. Para nosotros los usuarios están divididos en sectores, licitación, compra, atención al cliente, administración, una unidad de negocio que se llama renal. Entonces nosotros para cada sector de la empresa otorgamos dos licencias, o sea, para que se entienda, una licencia al jefe, donde la información obviamente es privada, y por eso es que el jefe hace determinadas cosas que no hacen los usuarios, y una licencia que comparte el sector, que capaz que son tres, cuatro personas. Entonces no quiere decir que no crean consultas o no hacen listados o que no crearían una consulta Gol, llegado el caso, pero una tabla Gol. Pero el tema es que es mucho menos, el trabajo que hacen es más de visualización que de creación. Entonces, ¿Qué pasa? Yo voy a tener en cada sector, por decirlo de alguna manera, dos licencias, una que crea muy poco y que más que nada consulta, y una que es la que genera la mayoría de las cosas, para que el resto para compartirla e información, obviamente que es privada y que no va a compartir con el resto de la gente, porque el rol es otro.

**Agustin Garcia**: OK.

**Mariela Niell**: Más o menos es eso. Entonces, si vos consideras en función de ese. Yo debo tener alrededor de unas 10. 10 sectores menos, te diría. 7 sectores son. En general son 7 sectores más su grupo. ¿Se entiende? Es una clave. Por sector más el grupo. Yo al grupo lo contemplo siempre como una. De hecho hoy tienen, comparten entre esas cuatro personas una licencia de cloud. ¿Por qué? Porque entre ellos es todo lo mismo, no es que hay un rango.

**Agustin Garcia**: Te hago una pregunta, porque también esto que compartan, digamos, no sé, digo, no sé cuál es el nivel de uso, pero vos podés tener ese usuario que va a tener una licencia MCP de cloud, que seguramente ahí con Lucio verán cuál es la mejor arquitectura en términos de datos, como la armen, ese data lake para, digamos, que los permisos sean eficientes también. Ahora vas a tener, digamos, una licencia por sector.

**Mariela Niell**: En realidad dos o dos.

**Agustin Garcia**: Bueno, pero digamos, los dos usan MCP, digamos. Los dos. Perfecto. Y después tenés más gente ahí, porque también, digamos, vamos a armar como un combo que tal vez tenga dos usuarios que tengan capacidad MCP por sector, y tal vez, no sé, dos o tres más que sean viewers, o sea que sólo puedan acceder a ver la información o los reportes que se cargan. Y aparte también ahí inclusive podés usar el agente, digamos, como no va a tener, digamos, licencia de cloud, pero esos usuarios también pueden usar el agente para conversar con la data, ¿Entendés?

**Mariela Niell**: Entonces, digo, va a tener y no necesito quizás, probablemente. Es más, podemos utilizar. Sí, me parece que puede ser una idea de dónde lo podemos encarar y probar desde el punto de vista de un plan customizado. Quizás.

**Agustin Garcia**: Por eso te preguntaba, quería entender un poco.

**Mariela Niell**: Yo lo que voy a hacer es dimensionar exactamente eso. Les voy a mandar un mail con cuántas, voy a ir a mirar a Claude, porque la realidad y qué uso le están dando y cómo le están dando. Voy a hablar un poco más con la gente, porque bueno, eso lo voy a tener que sacar de cada uno y de cada jefe. Y podríamos empezar por una cosa de esas, cómo es el tema de las visualizaciones de aquellos que no crean las.

**Agustin Garcia**: Las tablas Gold son usuarios Viewer para nosotros, y es una licencia que está como parte del combo en la página. Hoy no está porque eso está para las versiones Enterprise, pero lo podemos considerar, no hay problema. Entonces por eso te decía, digo, a lo mejor teniendo dos usuarios con MCP a Cloud por sector y tal vez puedes tener un paquete de dos o tres usuarios Viewer por sector, capaz que con eso estás OK.

**Mariela Niell**: Me parece que estoy cubierta porque si uno lo crea y el otro lo visualiza, estoy bien. Lo que no puedes tener uno por sector porque son trabajos distintos, pero dos por sector sí.

**Agustin Garcia**: Perfecto, perfecto.

**Mariela Niell**: ¿Bueno, yo voy a dimensionar exactamente los sectores con el tema de hablar con los jefes de cada sector, ahí sí voy a tener que hacer un trabajito yo para poder pasarle bien la información a ustedes y en función de eso avanzamos, les parece?

**Agustin Garcia**: Me parece bien. No sé si vos esto lo tenés planteado en algún plan de salida, producción en términos de. No sé si hoy ya usan Cloud.

**Mariela Niell**: Hoy ya usamos Cloud, de hecho yo lo conecté directamente con mi cuenta de Cloud.

**Agustin Garcia**: Ah, bueno.

**Mariela Niell**: Por eso ya lo hice hoy.

**Agustin Garcia**: Si querés considerar que por ejemplo, no sé, los primeros dos meses un plan, el mes 3 y 4 otro plan, digo tampoco son tantos, pero son 7 sectores, vas a tener 14 usuarios o si querés ya te armo una propuesta que tengas todo de entrada,

**Mariela Niell**: vamos a analizar con todo de entrada y en función de la propuesta y el relevamiento que yo hago, vemos en eso. Aguántame si querés antes de eso para que yo hable con los sectores de esto, capaz que en algún sector tengo un jefe intermedio y eso me ayuda a esto de las cuentas y de las cuentas Viewer como vos la llamás. ¿Entonces dimensionamos, me pasás el presupuesto y avanzamos en función de eso, te parece?

**Agustin Garcia**: Me parece perfecto. Así que revisá vos, avísame cualquier duda.

**Mariela Niell**: Sí, sí, las cuestiones es una vez, porque yo. ¿Nosotros probamos el entorno gratuito, que fue lo que probamos? ¿Tiene alguna app o es todo web?

**Agustin Garcia**: Todo web es todo web.

**Mariela Niell**: Bien, eso es lo preguntar. Era una inquietud, no sabía ningún lado. Consulta una interfaz de teléfono también tienen. ¿Lo podrían usar desde el celular con Android o iOS?

**Lucio Rojas**: Lo que vos podés hacer es usar Cloud, porque el usuario final, nosotros no lo vemos dentro de consumidor, sino dentro de Cloud. Entonces podrían usar Cloud desde la versión mobile de Cloud, que es lo que hago yo en realidad.

**Mariela Niell**: Sí, de hecho si lo usas, porque si haces el conector sí lo puedes hacer desde la versión mobile de Cloud, no desde Teramo pero sí desde Cloud

**Lucio Rojas**: tenemos un usuario europeo que una vez me dijo me voy modelando teles en el tren mientras iba paseando desde el celular.

**Mariela Niell**: Así que está eso también podemos contemplarlo para algunos usuarios que usan poco la notebook, la PC de escritorio está más afuera, quizás son los más, los que tienen cargos más altos y están todo el tiempo con el celular y no con una nota. Está claro, es por eso que lo pregunto Mariela.

**Lucio Rojas**: Ya más adelante. Nosotros ya la parte de customer success, una vez el cliente ya está enteramos, los acompañamos en eso, en determinar cómo cada usuario tiene usos y costumbres, si usa el celular, vemos de armar algún proyecto con algún prompt especial para que responda mejor, armar algún asistente por ejemplo de Visitas al Cliente en lo que es más terreno de campo para que le responda rápido con la información que necesita. En eso también nosotros lo acompañamos.

**Mariela Niell**: Perfecto. ¿Y me queda una pregunta, yo tengo

**Agustin Garcia**: otra también, pero

**Mariela Niell**: según la experiencia de ustedes, cuál es más o menos el tiempo de implementación? ¿Sé que obviamente cada uno va a variar de acuerdo a las necesidades, pero más o menos qué tiempo consideran que se maneja en promedio?

**Lucio Rojas**: ¿Qué base de datos tiene ustedes?

**Mariela Niell**: MariaDB, o sea vos, MySQL y ustedes

**Lucio Rojas**: son los encargados de todo lo que

**Mariela Niell**: somos la administración de la. De hecho todo lo que es infraestructura nos encargamos nosotros. Nosotros vamos, administramos nuestra propia base de datos. Y además esto es una cuestión, por una cuestión política, eso te diría, más subjetiva mía que de cualquier cosa. No pegaríamos contra la base de datos en producción, sino con una copia de la base de datos actualizada todos los días.

**Lucio Rojas**: Más que nada eso en el día se ingesta y al otro día ya se puede usar la herramienta.

**Mariela Niell**: Claro, yo no me refería sino a la implementación particularmente, porque de hecho yo los datos lo hice y una micro.

**Lucio Rojas**: ¿A cuánto tiempo lo adoptan las personas?

**Mariela Niell**: Exactamente. Ese proyecto de bueno, armo una X cantidad de tablas gold, funcionan bien, los usuarios están puestos a punto, se armaron los perfiles. Ese tiempo es el que yo quiero, no el otro.

**Lucio Rojas**: Yo creo que estamos en el orden de las semanas.

**Mariela Niell**: OK, perfecto.

**Lucio Rojas**: Yo creo que entre el orden de dos, tres semanas y siempre que lo arrancas con usuarios de prueba, mucho mejor tipo por área y le vas dando la herramienta, yo creo que eso en dos, tres semanas anda y después distribuirlo al resto de los usuarios, también lleva la parte esa de que adopte una herramienta nueva que también lleva un poco de contagio entre ellos, de órdenes, de semanas, no tiene más que eso.

**Mariela Niell**: Perfecto, bien, genial. ¿Entonces avanzamos Agustín Lucio con cómo quedamos? A mí me queda una consulta nomás. Material para capacitar a los usuarios

**Agustin Garcia**: tienen

**Mariela Niell**: disponible, tienen formato vídeo, texto,

**Agustin Garcia**: Lo que también se incluye como parte de la propuesta es el servicio de onboarding, básicamente los acompañamos a ustedes para que ustedes puedan hacer uso y explotación de la herramienta de la mejor manera. Entonces nosotros consideramos que una vez que se ingesten los datos, los vamos a acompañar, ahí vamos a hacer una sesión también para conversar de este tema de los permisos, para que ustedes puedan articular y estructurar la información de la mejor manera y también si necesitan y consideran, podemos hacer una sesión con los usuarios para. Generalmente nosotros si es una empresa grande lo que hacemos, hacemos un train de trainers, o sea, como que entrenamos a quien puede entrenar al resto para que digamos después digamos, no sé, es difícil coordinar con toda la gente interna. Ahora, si ustedes quieren que hagamos un entrenamiento, o sea, un entrenamiento, hacemos una demostración, respondemos dudas, le mostramos cómo funciona la herramienta, podemos agendar, yo creo que

**Mariela Niell**: según nuestra estructura y bajo el conocimiento de mis usuarios, por decirlo de alguna manera, lo que creo que deberíamos hacer es un entrenamiento nosotros con ustedes a dar la aplicación a usar con los usuarios, generar una serie de preguntas que tengan y aquellas que no podamos responder nosotros, esas sí se las daríamos a ustedes. Creo que ese sería el camino, porque es muy factible que en una primera reunión no tenga nadie ninguna pregunta y después tenga muchas, es lo que pasa

**Agustin Garcia**: habitualmente, por eso nosotros te decíamos esto de train de trainer, como para que ustedes. Bien, claro, y aparte también nosotros lo que buscamos es transferir el conocimiento para que ustedes tengan autonomía, eso no quiere decir de que después podamos tener una reunión, no sé, cada 15 días, tres semanas, una vez por mes, para ir viendo cómo va la cosa, a ver si necesitan sumar algún caso de uso, ver si hace falta que le demos apoyo en algo, porque nosotros lo que buscamos también es acompañarlos para que ustedes adopten y usen y le puedan sacar provecho, porque es nuestro objetivo y seguramente que hay en esas reuniones, o después verán cómo lo articulan con el equipo de customer, pueden ir despejando todas esas dudas también.

**Mariela Niell**: Perfecto, me parece genial. Y me quedó algo que me acabo de acordar, nada que ver, es. Todas las tablas golden que se arman tienen como. Ustedes le ponen la clave principal, ¿No es cierto?

**Lucio Rojas**: La herramienta lo hace por default.

**Mariela Niell**: Sí, lo hace por defecto. No hay forma de sacárselo.

**Lucio Rojas**: No, no, para poder.

**Mariela Niell**: No hay problema, me puedo acostumbrar a eso, pero lo intenté y no pude.

**Lucio Rojas**: No, igual lo podemos llevar como esas dudas están buenas, no pasa nada, pero

**Mariela Niell**: viste que uno está acostumbrado, entonces la quise sacar y puse. Quise poner la clave principal que correspondía y hubo caso, dice, bueno, ya está, no pasa nada, pero no hubo caso.

**Lucio Rojas**: Te jodió con los joins.

**Mariela Niell**: No, no me jodió con los joints, era una cuestión de normalizarlo como debía ser. Y viste que uno ya tiene la estructura y seguía insistiendo porque quería que fuera como correspondía y no necesitaba otra clave. Entonces no me jodió con los joints, la verdad que no lo hizo perfecto. Pero bueno, me quedó ahí y dije maldición, no quiere. Pero no, nada más. Nada más que eso. No fue otra cosa, Lucio, simplemente que lo probé con dos, tres, cuatro, y me di cuenta que no siempre está ahí, no hay forma de sacarla y lo intenté, así que hasta se lo pedí amablemente, lo quise forzar y no,

**Lucio Rojas**: no quiso tomar por default.

**Mariela Niell**: Sí, sí, no pasa nada.

**Agustin Garcia**: Termina con dos planes principales.

**Mariela Niell**: Por eso mismo, pero nada más. No es que no genera ningún tipo de error, porque no lo generó el error, porque me fijé si tenía eso, traía algún error. Hizo lo join, Perfecto, no tuve ningún problema, la verdad. Nada, en eso no tengo nada que decir. Así que bueno, listo, chicos. Lo que queda es determinar cuántos usuarios, que ustedes hagan una propuesta a medida y avanzamos.

**Agustin Garcia**: Fantástico. Cualquier duda nos avisan ahí. Lucho, No sé, perdón que te interrumpa.

**Lucio Rojas**: Sí, yo lo identifiqué un poco, Mariela. Es que vos pensás los usuarios de la plataforma, para más de un usuario final, como que lo comparten.

**Mariela Niell**: En realidad yo hoy lo comparto, pero con. Yo tengo esta particularidad hoy porque lo uso para las licencias de cloud, y el por qué es porque son personas de un mismo sector que están usando lo mismo, o sea, no es que tienen otra inquietud, no tienen la misma inquietud, ¿Por qué? Porque cambiará el cliente, pero los que hacen licitaciones, licitan lo mismo. No sé si me pruebo de explicar, pero con esto de los viewers lo puedo resolver. Entiendo que obviamente la licencia es por usuario, por estación de trabajo, entiendo que es así, eso no me molesta, lo podemos resolver con los viewers, por eso.

**Lucio Rojas**: Claro, eso sí, debo sincerar bien eso de quiénes son realmente los usuarios, o sea, las personas que van a consumir información, eso estaría bueno y después nosotros vemos que sea acorde también a licencia de usuario, pero identifique eso y estaría bueno saber bien cuántos son en personas

**Mariela Niell**: realmente es así, o sea, hoy hay un jefe de cada sector, ¿Para que hacemos la cuenta? Una licencia para cada jefe de sector y para cada gerente, que no están contados en eso porque no tienen un sector a cargo, o sea, mucha gente, sino que tiene muchos sectores que ya son jefes, entonces un par de cargos gerenciales que no tienen gente abajo, en realidad no es que no tienen gente, sino que tienen otro jefe. Y después tenemos los jefes de sectores que sí tienen gente a cargo, que usan lo mismo, pero no hay ningún problema porque lo puedo suplir con una clave, una licencia para el jefe, una para digamos, la mano derecha y otra para el resto del sector, o sea, de visualización, cuando digo la otra se entiende, ¿No? Entonces podemos suplirlo, no hay ningún problema, nos podemos adaptar esa estructura, si después a la larga esa estructura requiere algo más, lo veremos, pero inicialmente creo que está bien.

**Lucio Rojas**: Bueno, bueno, perfecto, entonces seguimos en contacto por.

**Mariela Niell**: Dale, no hay ningún problema, hoy mismo le estoy escribiendo con esa. Con esa cantidad de licencias. Gracias, hasta luego chicos.
