# Agenda CS (Fernando  VERSARI)

**Fecha:** 2026-10-19T18:00:56.792+00:00  
**Duracion:** ~51 min  
**Participantes:** Juan Peralta <juan@teramot.com>, Lucio Rojas <lucio@teramot.com>, Matias Sanguinetti <msanguinetti@bindseguros.com.ar>, Fernando Versari <fversari@bindseguros.com.ar>  
**Externos:** msanguinetti@bindseguros.com.ar, fversari@bindseguros.com.ar  
**Apollo ID:** 6ad666e97bf5dc0010d1e30f

---

**Matias Sanguinetti**: ¿Cómo estás?

**Lucio Rojas**: ¿Todo bien vos?

**Matias Sanguinetti**: Bien, bien. Me subí un segundo acá por el teléfono que estamos terminando otra reunión con todos los chicos, así nos dejábamos colgado y los aguantas un cachito.

**Lucio Rojas**: Sí quieren que arranquemos y media.

**Matias Sanguinetti**: ¿Qué hora es? No, no, no, da 15 minutos máximo si no tenés nada que hacer y te quedas en línea.

**Lucio Rojas**: No, yo no tengo problema, me quedo en esta reunión.

**Matias Sanguinetti**: Dale, ahí corto, corto y ahí se sume Juan, casi. Juan, ¿Cómo estás? ¿Le avisas a Juan? Nos banca un cachito. Dale, dale, ahí ya subimos. Abrazo, Chau.

**Juan Peralta**: Chau.

**Lucio Rojas**: Dice que está 15 minutos demorado.

**Juan Peralta**: OK, volvemos a las y cuarto, así nada, Vuelvo.

**Lucio Rojas**: Ahí estamos. Comment

**Fernando Versari**: nouveau. Buenas. Buenas. Lucio. ¿Escuchan? ¿Me escuchas ahí Lucio?

**Lucio Rojas**: Sí, perfecto.

**Fernando Versari**: Bien, bien, perfecto también. Bueno, Mati no sé si vino por acá.

**Lucio Rojas**: Mati está en el teléfono descompuesto.

**Fernando Versari**: Sí, sí, me llamó recién, pero yo le dije que ya subía. A ver.

**Matias Sanguinetti**: Bueno, aquí estamos.

**Fernando Versari**: Ahí va. Sol está también.

**Matias Sanguinetti**: ¿No?

**Fernando Versari**: Bueno, todo bien Lucio, Durísimo hoy, durísimo. Bueno, ni te cuento por acá, ¿No, Mati? Ahí va. Bueno, te la hacemos corta, te cuento Lucio, aparte de lo que ya venimos trabajando, nos surgió un tema que nosotros estamos trabajando en todo lo que es una migración, migración de cartera, pero bueno, lo que es banca minorista, todo lo que sucursales del BIN van a parar al Patagonia, tomo operación Patagonia. Entonces en ese proceso nosotros toda la parte de seguros tenemos que ver nuevas interfaces que vamos a tener que estar trabajando con Patagonia. ¿Por qué vos decís, bueno, ¿Por qué te estoy contando esto? Porque en el proceso hay salidas de información que tenemos que hacer de novedades diarias y esas novedades diarias creemos con Mati que podemos armar como si fuera la estructura de salida o la IA o el FD, como queramos llamarlo. Desde el modelo Téramot tenemos ciertos layout que nos pasan el banco que tenemos que dar cumplimiento y queríamos ver con vos, sobre todo porque por ahí creo que en el modelo Téramo había algunas restricciones de salida de cómo puede hacerlo, pero quizá de Cloud no. Entonces era compartir un poco esto que tenemos que hacer. A ver si vos ves que estamos muy ya pasados de rosca y dice nos fuimos de viaje con esto que pensamos lo podemos hacer y no, o vos decís, che, no, sí, claramente lo pueden resolver.

**Lucio Rojas**: Bien, ahí tengo dos preguntas. Una ¿Cuál es el layout?

**Fernando Versari**: ¿Bueno, acá no sé si teníamos, Mati, para el de novedades, me lo pasaste vos o quién lo había mandado?

**Lucio Rojas**: ¿Un PDF, un Excel?

**Matias Sanguinetti**: No, no, son novedades en Excel, que entiendo que por lo menos los de Patagonia se tienen que bajar en. No sé si en CSV o TXT. Y después hay otro también que es un partner que tenemos, asistencia, que también es un layout un poquito más simple que hay que devolverlo en Excel directamente.

**Fernando Versari**: A ver, lo de la salida del Excel, yo entiendo, por eso era preguntarte con que nosotros podamos generar la estructura en archivo plano, respetando la estructura, después, bueno, veremos si lo convertimos o qué hacemos, pero. Hola, ¿Cómo andas Juan?

**Matias Sanguinetti**: Gracias, Juan, ¿Cómo estás?

**Juan Peralta**: Bueno, hola Mati.

**Fernando Versari**: ¿No tenés ahí Matiel de novedades? No.

**Lucio Rojas**: Y Fer, antes de. Vamos buscando novedades, pero una segunda pregunta que asumí que ya es sí la respuesta por algunas G, ¿Todo el origen de esta información está en Gauss, en Custom o en Cobranza?

**Fernando Versari**: Si, están Gauss, porque estos son todas pólizas que se emigraron, o sea, tenían una condición de póliza colectiva y ahora pasaron a individuales. Corregime Mati, si estoy siendo. Viven en. Viven en Gaussian.

**Lucio Rojas**: Tendríamos que armar como un reporte, o sea una tabla.

**Matias Sanguinetti**: ¿Se colgó o soy yo?

**Fernando Versari**: Yo te escucho.

**Juan Peralta**: ¿Perdimos, lo perdimos a Lucy,

**Fernando Versari**: puede ser? Tawada, Manuel, que lo haya mandado eso.

**Matias Sanguinetti**: Acá lo tengo. Ahí volví.

**Lucio Rojas**: Digo, me imagino una tabla o un reporte con una lógica de negocio que ya deje, un pipeline con los datos que ustedes tienen que informar y un proceso que todos los días o con la frecuencia que ustedes tienen que reportar, convierta las novedades al layout que necesitan y lo mande. Sería como es el punto.

**Fernando Versari**: Claro, ahí mira, si querés un segundito. Bueno, ahí está. Bueno, está el. Están compartiendo, no sé si se ve,

**Juan Peralta**: para avisarles que estaban compartiendo toda la pantalla.

**Fernando Versari**: Por un lado tenés el layout de la diaria y después uno mensual.

**Matias Sanguinetti**: ¿Ese no lo tengo, pero para que lo busque, no?

**Fernando Versari**: Si, tenés dos archivos, ejemplo, tenés uno que dice SGM y otro diario.

**Matias Sanguinetti**: Lo que no tengo es el. Este es de novedades. Después está el otro, Fer, el de. El de envío de base, Pisa Base, el otro que es más largo.

**Fernando Versari**: Base, Pisa Base. Me mataste con esa.

**Matias Sanguinetti**: El mensual de. Ah, no, perdón, me confundí con el de cobranza. Perdón.

**Fernando Versari**: No, no, por eso el de cobranza va por Gauss puro, porque ya lo tienen desarrollado. El tema es así, Juan, no sé si nos llegaste a escuchar, pero vuelvo un poquitito haciendo acá para que lo tengas. Con el tema de los cambios que hubo a nivel del grupo, donde todo lo que es sucursales de banca minorista pasan a manos del Patagonia, tenemos que trabajar la operación directo desde seguro, algunas cuestiones que antes hacía el banco, Banco BIM. Entonces en ese proceso tenemos dos grandes procesos. Uno, si querés, el de cobranza, que toda la cobranza va al lado de BIM, y ese layout o esas interfaces, el core nuestro las tiene, o por lo menos tiene la entrada, la salida y tiene un retorno y tengo que hacer algo de desarrollo, pero lo vamos a lograr rápido. Entiendo. Después, por otro lado, hay una serie de layout o de interface, tengo trabajo, que son novedades diarias, y esas novedades diarias, este layout no lo tiene el proveedor, no lo tiene Gauss, y llevárselo a Gauss ahora no tenemos tiempo, no llegamos, porque esto tiene que estar ya ahora, antes de diciembre lo tenemos que tener ya probando, con ciclo de prueba. Entonces se nos ocurrió con Mati el otro día, hablando de Che, bueno, para si la información está contenida en el core y lo único que hacer es un output con este formato de las pólizas que están, que son las que tenemos que enviar, bueno, tratemos de ver si podemos hacerlo bajo modelo Theramo. Ese fue un poco la conversa. Dicho eso, entiendo que la salida que tenemos que hacer es un TXT, ni siquiera es un CSV, es un TXT que tendría origen en los datos de Celaya o esa estructura, tanto en el diario, en el mensual, creo que son dos instancias y la información contenida está en el, con lo cual deberíamos, o entiendo que deberíamos poder lograr sacar esto.

**Lucio Rojas**: Bueno, digo, yo esto lo veo honestamente súper viable. Es más, creo que podríamos hacer, no quiero poner tiempo que no cumplamos, pero

**Fernando Versari**: trabajándolo con que esté para las 16 horas, Lucio, para las 16 horas está bárbaro, no te preocupes.

**Juan Peralta**: Vos sabés que si lo desafías, yo creo que va a tardar vos más tiempo en enviarnos el correo que Lucio en hacerlo.

**Fernando Versari**: Es más, ya está saliendo la novedad de Patagonia.

**Lucio Rojas**: Honestamente, ahí lo que realmente necesito es que ustedes me bajen bien, qué es lo que tiene que tener ese output en el sentido de información, o sea qué es lo que tenemos que estar informando bien documentado, o por lo menos si ya tenemos los Excel, por lo menos ver con esos Excel la lógica.

**Fernando Versari**: A ver, mostrame un segundito Mati. Los layout de nuevo,

**Juan Peralta**: es muy importante de STXT de tener la longitud de cada string. Por ahí en la base a lo mejor tiene más caracteres y trunca, viste que los sistemas no son.

**Fernando Versari**: Si, esto es a la vieja usanza, digamos.

**Juan Peralta**: Bueno, vos me tenés que decir la primer columna está eso

**Fernando Versari**: entiendo que está en el layout. A ver Mati,

**Juan Peralta**: porque eso es fundamental como para poder armar el.

**Matias Sanguinetti**: Acá está la longitud de cada uno, o sea tenés sumando todo,

**Fernando Versari**: entiendo que tenés el layout y aparte tenés de cada uno de estos un ejemplo de salida que son los TXT, porque ellos

**Lucio Rojas**: te pasan esto para importarlo, ellos ya te mandan formato.

**Matias Sanguinetti**: Claro, hay que respetar los formatos y hay unas tablas de conversiones de datos que están en el sistema, una codificación y ellos requieren otra codificación, no sé, por ejemplo acá ves tabla de. Bueno, está distinta, tabla de país 80 para Gauss, no es Argentina. Entonces hay que hacer esa conversión también de la codificación que te traigas, pasarla digamos a la de ellos, a lo

**Juan Peralta**: que está en este Excel.

**Matias Sanguinetti**: Claro, acá tiene el diario y la mensual que son iguales.

**Juan Peralta**: Hay una, pero ahí está tabla SIA, tabla DOC país que son las.

**Matias Sanguinetti**: Claro, te decía, acá tenés el diario porque ellos con otras compañías de seguro diariamente le envían novedades. Nosotros realmente no vamos a tener un volumen tan grande como para pasarlo diariamente, quizás negociamos algo semanal como hace un poco menos tedioso, más que nada por si hay alguna respuesta de errores para poder trabajarlas. Y está la mensual, ellos quieren todos los días que reciba información y un consolidado mensual, que hay una pequeña diferencia, me parece que solamente en este campo es la diferencia. Ves acá 999 para este tipo de operación. Y después están las tablas de conversiones que son hasta acá.

**Lucio Rojas**: ¿El consolidado mensual lo hacemos acumulando los diarios o lo hacemos con una corrida individual que sirva de close?

**Matias Sanguinetti**: Como quiera es un consolidado de todo lo que se fue enviando. Si nosotros le enviamos semanalmente hace un consolidado de 4.

**Fernando Versari**: A ver, igual está buena la pregunta ahí porque Mati, esto nosotros nos lo pasaron liso y llano. Yo lo que haría es primero lograr si quiere armar la estructura, ni siquiera digo con mucha data más que lo que está acá y las dos muestras que tenemos, a ver si logramos, si quiere sacar la estructura general. Y después si nosotros vamos a tener que tener una reunión con la gente de Patagonia para revalidar esos campos, decir che, porque seguramente acaba tema de producto, Mati, que vamos a tener que ver las conversiones, va a haber varias cosas que me imagino que esas definiciones vamos a tener que tener a nosotros en base a lo que se acuerde con ellos. Ahora

**Matias Sanguinetti**: que acá estamos asumiendo que toda la producción Patagonia ya la tiene en su core y que validamos ciertos datos y campos, y esto viene después, llámese lo que Cofer, productos, por ejemplo, todavía no hicimos la migración de la cartera a ellos, con lo cual también tenemos que transitar eso para que esto funcione. Si no funcionaría esto.

**Fernando Versari**: Lo que tenemos lograr acá un poco para Patagonia, es nosotros tener la celeridad suficiente para tener la holgura, porque esto va a empezar a iterar y no tengo duda que mandamos algo a che, no pinchó porque mandaste el código Pepito de otra manera, y nos comemos toda la banda de las iteraciones hasta que esto quede refinado por sentado. Y lo otro Mati, por las dudas que por la pregunta que hizo Lucio, es yo no sé si exactamente las 9 diarias son las mismas que envías en el mensual. Puede ser que por proceso fuese algo

**Matias Sanguinetti**: distinto, por lo que veo. Por lo que veo son las mismas, por lo menos en cantidad de filas. Acá tenés 27 y acá tenés 27, o sea en cantidad de filas aparentemente las mismas. La única diferencia que veo que te cambia el tipo de operación. Acá hay que identificarla según esta tabla que está por acá, y acá se trunca en 999, el resto aparentemente es todo igual.

**Fernando Versari**: Bueno, pero ahí podríamos hacer, una vez que logremos si queré, para no ir vacíos con esto, si logramos la estructura general de esto y vemos que se puede emular, que yo no tengo duda que se va a poder hacer, hacemos una reunión con la gente del Patagonia y nos sacamos las dudas de todos los puntos para poder ya ir al hueso de la data buena.

**Lucio Rojas**: Bueno, creo que son dos gols, o hasta incluso puede llegar a ser una o las tablas de resultados que tenga la sábana del detalle al día, y quizás el output sea código y. Y le peguemos a una API que levante los datos de la tabla y genere el output, para no meter ahí un agente inteligencia artificial en el medio. Porque la verdad es que si va a ser determinístico con código y una API y la tabla Gold, lo resolvemos. No sé si ustedes quieren ponerle alguna cosmética, algún front para que Patagonia entre y se lo descargue o que le llegue directamente por mail o.

**Fernando Versari**: Y lo que pasa que acá creo que va a empezar todo el tema de lo que nos están planteando ellos, que esto tiene que viajar vía SFTP, lo más probable que ahí con el banco, yo ya estoy viendo los métodos de transferencia, pero digo, ahora eso no me preocupa tanto en cómo se lo vamos a dar, sino en tenerlo y ya sea por correo o sea por cualquier medio decirle mira, ya los tengo y ahora cómo seguimos hasta que agarremos una prueba de ciclo completo y que sepamos que esto está todo bárbaro, ir bajando, digamos, haciendo check, porque tenemos mucha apertura de estos temas y entre todo el resto del bagaje que tenemos, se nos está haciendo medio pesado. Entonces el otro día con Mati cuando hablamos dijimos, che para, de operaciones, bueno, capaz que de operaciones el primer delivery que tenés es este, porque justo la operación de Patagonia que va a ser uno de los core. Entonces nada, pero ahí la idea sería bueno ir trabajándolo como hicimos con el resto y que después esto quede manos nuestra, obviamente, como venimos hablando, para controlarlo, para verlo y bueno, pero en sí necesitamos como esa. Creo que el primer esto de nuevo que encontramos con esto era sacar esto, porque estamos con la soga cuello. Bueno, no sé Mati, ahí si hay algo que quieras agregar.

**Matias Sanguinetti**: No, no, si logramos esto, que no tengo dudas que te quedan 28 minutos, las 4, el objetivo target. Si te quedan unos minutos, le estás

**Fernando Versari**: pidiendo si juega esto, porque juega muy bien al ping pong, viste, No le

**Matias Sanguinetti**: tiene,

**Lucio Rojas**: Viste que fue ahorrando con el tiempo. Los primeros 10 minutos no metía la pelota en la cancha,

**Fernando Versari**: me fui, lo dejé ahí con la paleta, iban todo afuera. Así, así fue más o menos. Volví a los 10 minutos, el profesor no sabía dónde meterse

**Lucio Rojas**: mucho que no jugaba, no tenía el top aceitado,

**Matias Sanguinetti**: y después tenemos un proveedor que dentro de varias de las pólizas que tenemos en Gauss, tiene un rider que es una asistencia, y eso le da una empresa, una compañía, un prestador del servicio, y también requiere un layout hoy, perdón, requiere información también del core de Gauss Hoy, como esa póliza está emitida en el sistema COR del banco, y nosotros en Gauss la administramos como una nómina, digamos, solamente una refacturación, hacemos, nos es fácil sacar la información desde el banco, por eso pensando en que podemos sacar, que vamos a tener toda la info en Gauss, y ahí surgió la idea de, si, bueno, armemos todos directamente desde el core. Y esta información es mucho más simple, porque no requiere una salida de txt, no requiere campo fijo, no requiere ningún tipo de codificación ni nada, simplemente es traer los datos que están en el sistema, respetando un formato mínimo, digamos, de lo que son las fechas, pero el resto es armar estas columnas y nada más, digamos, de un producto determinado. Esta creemos que es bastante más fácil incluso que la otra, que requiere otra salida, otro volumen incluso, y otra codificación, Lo veo un poco más simple, hasta incluso quizá podemos intentar hacerlo, creo que nosotros hay en Excel de 15 columnas.

**Fernando Versari**: Con lo cual yo haría esto, Mati haría los otros, las novedades, lo hacemos, o sea, con soporte, el otro metetelo vos como primer práctico si querés, y lo vemos juntos si querés, sí es

**Matias Sanguinetti**: un refinamiento que haya, que sea con ellos quizás, si no

**Juan Peralta**: el profe Lucio te corrige. ¿Quién está de punto de contacto para validar el origen de algún dato? En el anterior sobre todo.

**Fernando Versari**: A ver,

**Juan Peralta**: los datos están en cordón, Mati, a lo mejor están en siete tablas, tres columnas en una tabla, cuatro en la otra, o sea, nosotros podemos hacer esa suerte de ingeniería, de ir a. A buscar medio así, in the wild, alpajar la aguja, pero podemos, a ver,

**Fernando Versari**: con Isa podemos hacer pie, Con Isa podríamos hacer pie, si le explicamos qué es lo que hay, capaz que como ella también está generando modelos ahí abajo, ya está metiéndose en el juego, podemos ver. Pero digamos, de la parte operativa, Mati va a poder decirte, che mira, esto es por venta, por lo que sea, la parte operativa la tiene Mati, y después si tenemos que ir al punto

**Juan Peralta**: contacto, eso es para validar que estamos yendo por los encabezados y las columnas, para buscar la información correcta. Y la otra que nos sirve de prueba es alguno ya armado para decir che, no sé, Para febrero del 2026 armé este TXT.

**Fernando Versari**: Juan, ahí te mandaron los dos ejemplos.

**Juan Peralta**: Esto es nuevo, yo entendí que lo hacían a manopla y estaba.

**Matias Sanguinetti**: Cambio de negocio.

**Lucio Rojas**: Si quieren para arrancar yo mañana. Claro, reenviame el formato y los ejemplos de los txt y yo me involucro a ver si lo puedo resolver y lo revisamos, creo que así podemos ver, marcamos una reunión.

**Fernando Versari**: Todo esto para aclarar nada más, son todas interfaces que nosotros no. Nosotros interfaceamos con el Banco B todo esto. ¿Ahora cómo se va? Somos nosotros en el puente con Patagonia, entonces ellos.

**Juan Peralta**: ¿Qué quiere decir se va? ¿Cómo que dijiste? Como se va, o sea, por velocidad operatoria lo resuelven de cierta.

**Fernando Versari**: No, no se va, es que nosotros hicimos otra Carter, la vamos a mantener durante X años, ponele. Pero la operación cambió, o sea que antes Mati iba contra el banco y el banco tenía desde su core, le entregaba las interfaces de procesamiento al core nuestro, ahora somos nosotros con Patagonia, entonces el banco ya nosotros hicimos toda una migración de pólizas individual, lo cual me tomó un montón el volumen en operación, y somos el nexo contra Patagonia, toda la cartera al cobro va a ser nuestra responsabilidad directa. Entonces esto tiene que estar súper afilado, después ya veremos más quizás del uso más de los modelos genéticos para quizás controles que estamos viendo, por ejemplo toda la parte cobranza y eso, que no se vaya a depregar la cartera porque no sé, mandamos algo a procesar o bueno, todo eso, pero este es más de novedades operativas, yo creo que lo podemos armar.

**Matias Sanguinetti**: Ahí mandé el correo, Lucio.

**Lucio Rojas**: Bueno, después Juan, no sé si vos ves la parte. Yo me encargo de. Les mando por mail, supongo que para mañana tengo horas a la mañana, así que lo hago y les digo cada miércoles verlo.

**Juan Peralta**: Eso es confianza grande, Lucio, eso es confianza.

**Fernando Versari**: Vamos a tratar de aprender un poco de tu nivel de confianza. Es muy bueno lo que dice acá Juan, si nos transmitís eso, nosotros también nos enganchamos, así que vamos. Bueno, para ahora ya que están acá Juan, y aprovecho que está Mati también, o sea, te hice el enroque un poco con esto, porque esta semana la tenemos media heavy, y la verdad que hacer la segunda vuelta, esto de la inducción y esto lo dejamos para la que viene y lo que sí nos queda es armar el tablero de ventas, que bueno, Jime ya había empezado a armar algo, Emi llega la semana que viene, así que yo creo que la semana que viene recién ahí podríamos retomar un poco esto. Y yo estoy migrando, como le dije el otro día, porque me quedé a media tinta con el tema de mi doble usuario, así que estoy migrando todo lo que tenía en la personal a la corporativa, porque me viste por el

**Lucio Rojas**: slack que Sol te dijo que ya

**Fernando Versari**: estaba resuelto allá está bueno, era un tema.

**Lucio Rojas**: ¿Ustedes

**Fernando Versari**: habló con Antropic y por qué lo paraban? Bueno, después si no le pregunto, fíjate en el canal igual me dijo la gente del banco que sugerencia. Y esto Mati, aprovecho que estás por acá. Bueno, igual vos lo tenías con la corporativa, que no nos metamos ahí en el ranking de los personales porque puedan escorear todo eso y vamos a salir en la cartelera, así que por eso empecé a migrar. Así que nada, lo migro y ya está. Y Juan, nada, para nosotros que nos quedaba dentro la traza. Lo que sí no vimos nunca que te lo mencionara era el tema de gira, que tenemos que ver ahí si lo podemos subir en algún momento. Que entiendo que no me dijeron que no me dijeron que era con usuario servicio para el proyecto, porque como ese

**Juan Peralta**: acceso fue Sol quiero dijo que ya

**Lucio Rojas**: lo hizo al conector

**Fernando Versari**: tremendo, se entusiasmó

**Lucio Rojas**: porque le gustaba para su proyecto, entonces

**Juan Peralta**: bueno, podemos hacer la prueba.

**Fernando Versari**: Está bien, está perfecto. Bueno.

**Lucio Rojas**: Y les voy, les aviso por mail si queda algo o no y con una reunión cuando tenga una descripción. Y después lo de la segunda parte. Fer, la semana esa del 26 tengo que viajar a Buenos Aires por un evento, así que capaz que puedo también ir presencial, no voy a llegar a todo el equipo de vuelta para no trasladar a todos, pero hacemos híbrido, avísame

**Fernando Versari**: vos cómo viene tu agenda y vemos.

**Lucio Rojas**: Perfecto.

**Juan Peralta**: La última, antes yo tenía Shira, era tipo el último eslabón, antes estaba mueble,

**Fernando Versari**: contabilidad, Beherman,

**Juan Peralta**: o sea no hay un orden.

**Fernando Versari**: Lo que pasa que Beherman por lo que venimos viendo bastante, está bastante limitado en varias cosas y por ahora, o sea, estamos por ejemplo en otros procesos, por ejemplo para automatizar, que bueno, lo que estamos viendo con los chicos de Verbus y no sé, ni siquiera tiene la API para hacer importaciones, o sea está bastante, viste, lejos. Sí, a ver, quizás es una alternativa de trabajarlo como repositorios alternativos, donde vos tiras, no sé, los. Porque de hecho vamos a tener que transitar esas líneas donde va a decir che, me bajo los mayores y los dejo, no sé, en un repo y poder tomar esa data de ahí, por ahí trabajar la reportería más cross, pero no tengo ingesta de API y yo creo que no va a estar ahí. Pero bueno. Sí, perdona, algo que veníamos hablando, aprovecho también está Lucio acá con lo de alianzas y que puede ser para los otros. Habíamos hablado en algún momento tener una estructura del lado de Téramo para por ejemplo, los complementarios, es decir, lo que no está en datos origen, tener alguna carpetita, algo así, que podamos tirar ahí la data, por ejemplo, alianzas, pero que esté dentro del modelo, no que sea un esté en la sesión, ¿Me entiendes? Que yo vaya cargando documentos en la sesión, sino que esté, que lo pueda hostear ahí también.

**Juan Peralta**: Pero como conectar un Google Drive,

**Fernando Versari**: ni siquiera te digo Google Drive, pero ponele que tenga dentro de la estructura de ustedes. No sé, esto, yo me imaginé así, alianzas, alianzas, tenés todas las bases de origen y después tenés información adicional que no están los core que recolecta EMI de afuera. Entonces en vez de tirarla en una sesión ahí loca, porque no generamos alguna carpetita, un folder que me deje meter ahí la data y directamente ya la tengo dentro del repo Ahí eso,

**Juan Peralta**: Esa info cambia

**Fernando Versari**: esa info y si, va a cambiar porque es información de ventas, entonces es como que quizás pisas, pero no lo sé. Igual hay que verlo con EMI, a ver cómo.

**Juan Peralta**: Ahí tenemos que ver en otros casos. ¿Por qué? Porque cuestión técnica, esa source que vos subís, que es un formato del Excel que la podes subir a Téramoto, crea una silver y se asocia al proceso de datos, pero si después creas otra, subís otra, mañana va a crear otra silver, entonces a lo mejor ese reporte que estaba conectado a la primera no va a haber la segunda y tenés que hacer otros cambios. Lo que hemos hecho por ahí dejar un repositorio tipo base de datos, es un desarrollo, hacer algo pero que quede un poquito más ordenado y tipo con un importador o vos de alguna forma lo dejas en esa base de datos y ahí sí queda más el flujo ya queda armado transparente, porque hay que buscar datos de una tabla que se va llenando de forma incremental.

**Fernando Versari**: Por eso lo que me interesa mucho es ver cómo es arquitectura híbrida que termina para entender cuál es el mejor modelo.

**Juan Peralta**: Se puede, de alguna forma se puede, pero o va a requerir más trabajo inicial y menos mantenimiento, o más mantenimiento y menos trabajo inicial. Ahí hay que ver un poco cuál

**Fernando Versari**: es el aprovechamiento, por dónde vamos. Bueno, el resto nada, todo bien. NDA ahí por las dudas te menciona porque después no sé si vamos a poder hablar. Ya le pasé eso a Fiamma y me dirá, lo incorpore a ver si

**Juan Peralta**: podemos ir avanzando y yo necesito los conceptos.

**Fernando Versari**: Sí, lo de facturación. Dale, dale, dale. Si no soy mañana, mañana te lo paso.

**Juan Peralta**: Dale Fer, lo tengo a Mati de testigo, dale 13 minutos a Lucio, así que ahí te.

**Lucio Rojas**: That is.
