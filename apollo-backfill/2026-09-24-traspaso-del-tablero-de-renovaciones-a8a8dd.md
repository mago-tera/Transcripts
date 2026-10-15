# Traspaso del tablero de renovaciónes.

**Fecha:** 2026-09-24T18:05:19.283+00:00  
**Duracion:** ~78 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Sol Soletti <sol@teramot.com>, Fernando Versari <fversari@bindseguros.com.ar>, Isabel Moreno <imoreno@bind.com.ar>  
**Externos:** fversari@bindseguros.com.ar, imoreno@bind.com.ar  
**Apollo ID:** 6ab578c4cae0530014a8a8dd

---

**Isabel Moreno**: Ventas, como te decía, y por otro lado estamos viendo otros soportes que seguramente van a necesitar. Así que vamos a estar armando algún roadmap de cómo seguimos con todo ese delivery de reportería en ese proceso. ¿Algo que a mí yo te quería preguntar es, va a surgir que hay seguramente fuentes anexas que no tenemos en el modelo central? No sé, te doy un ejemplo. Ahora estamos hablando de quizás ya vamos a meter breve con el presupuesto 2027, por ejemplo. Entonces eso por un lado, puede que esté toda la información histórica dentro de los COR, o tengamos que tomar alguna fuente anexa. Ese es un ejemplo. Otro es alianzas, que es uno de los puntos que queremos ver, que hay información central quizás en los core, pero hay mucha data que recolectamos de los partner, entonces uno le manda, no sé, un correo, el otro le manda, no sé, Excel. Lo que yo te voy a consultar ahí es, nosotros podemos subir sin ningún problema, digamos, esas bases anexas sin romper, por decir así, el origen. No el origen, porque el origen no lo vamos a romper, porque entiendo que estamos en la capa de abstracción, pero digo, lo puedo subir sin ningún inconveniente esos anexos, porque seguramente en esas verticales vamos a tener un híbrido, cosas que van a estar ya conectadas, centrales y otros van a ser anexos. Yo los puedo trabajar sin problema.

**Lucio Rojas**: Sí, eso un poco el fin de la herramienta, que no solamente te coordina una fuente o una o más fuentes core, sino que también podés hacerlo un repositorio de Excel, de CSV, todo lo que sea información anexa que vos tengas dando vuelta, lo cargas de herramienta en formato archivo. Ahí tenés que tener bastante cuidado que sea siempre en archivo. Bien, tabular, si es Excel todo tabular. Hoy recomiendo más directamente irme al CSV total del CSV vos tenés un link en tabular, lo deberías poder descargar como CCB sin problemas y cargarte los CCB a la misma consola que ya tenés hoy con las fuentes, lo levanta el modelo y desde clock mismo le decís, bueno, ahora vinculame también las fuentes que ya tenía con el CC. De nuevo, si vos querés modificar alguna tabla Gol anterior a esta nueva carga, va a tener que hacerla de vuelta, porque es un momento nuevo. Pero si querés usarlo para tablas que todavía no hiciste o tablas que ya tenés y sumarle eso, si ya tenía un presupuesto 2026 hecho como tabla y querés contrastarlo contra el 2027, podés pedir esa comparación.

**Isabel Moreno**: OK, ahí me quedé con lo que decías, porque digo, lo que ya está digamos dentro del modelo y gol es lo que ya tenés persistido, por decirlo así, con lo cual, por ejemplo, yo lo que no quiero es empezar a generar información que quede en mi sesión absoluta y que después no sea parte de la arquitectura, si querés, del ecosistema nuestro. ¿Entonces ahí cuál es la sugerencia? No sé, vamos a suponer que arrancamos con alianzas, que yo sé que alianzas tengo gran parte de eso, voy a tener algunas cuestiones que son del core, negocios, como me cubro, compara casa, no sé, Andesmart, Flecha, Boost, eso lo tenemos procesando en el core, con lo cual la data va a salir, pero hay otro que no sé, tengo Rentenia, no sé, Autonomy, bueno, si me viene corriendo la cabeza, todos esos están por fuera, entonces yo voy a generar, vamos a decir así, mi capa de. ¿Cómo se llama? Tabla de resultado en algún momento, y a esa tabla de resultado después le voy a tener que anexar los otros alls para ver cómo lo tomo, no sé si ese es el proceso que debo llevar adelante.

**Lucio Rojas**: Claro, vos lo único que tenés que tener cuidado para que no quede en su sesión, si vos trabajas, yo acá estoy viendo, te la motivas, las fuentes que cargamos, que tenemos el CRC, Si vos analizas algo de estas tablas dentro de la sesión de CL, y no lo generaste como una fuente de resultados, una tabla de resultados, que serían estas de acá, eso va a quedar en su sesión, no lo va a poder consultar nadie, si vos lo cristalizas como una tabla de resultados, eso lo puede consumir cualquiera que se conecte desde otra

**Isabel Moreno**: sesión, o sea, estos resultados son el homólogo de las GO, básicamente. Y si yo quiero hacer algo, porque a ver, lo que estoy pensando es para no tener que hacerlo como anexos o no, o esta cola acá, ¿Qué pasa si yo genero la source, genero porque vos generas tvcra, por ejemplo, no existía, no es algo nativo nuestro, si yo genero para alianzas, no sé, yo puedo generar un repositorio, una source nueva que sea alianzas y ahí voy tirando la data de las otras que no tengo dentro de los core?

**Lucio Rojas**: Claro, sí, esa es la idea de la herramienta. Yo acá puedo ponerle. Subí un archivo y elijo, no pasa nada. Y lo voy subiendo directamente le pongo un nombre a esa fuente, lo voy almacenando.

**Isabel Moreno**: Perdóname, puedo agrupar, puedo hacer una car. Yo sé que por ejemplo, no sé, cybersectem es todo lo que tenemos, no sé, el cor, eso tiene conexión por abajo y es. Si yo quiero hacer un repo, por decir Así, de todo alianzas, que va a tener, no sé, 10 archivos ahí adentro. Se puede generar esa estructura.

**Lucio Rojas**: Sí, que esté así, tipo como se. Fíjate que yo cargué este ahora.

**Isabel Moreno**: Claro,

**Lucio Rojas**: voy a elegir otro, Voy a elegir este y voy a elegir.

**Isabel Moreno**: Un segundito. Emi no está, porque por ahí está. Bueno, si ella viene un minuto y le contamos esto.

**Lucio Rojas**: Sí, Lucio, yo te sigo acá puedo elegir a qué fuente va.

**Isabel Moreno**: ¿OK, pero cómo hago para generar por ejemplo una nueva? Por ejemplo, ahí están todas las que vos ya tenés. Yo quiero generar un nuevo. Si querés un nuevo repo que sea alianzas.

**Lucio Rojas**: Quiero antes borrar estas que tengo y

**Isabel Moreno**: que adentro alianza va a haber, no sé, n carpetitas de las alianzas que con información complementaria. ¿Me entendés?

**Lucio Rojas**: Sí, sí, te entiendo. Perfecto.

**Isabel Moreno**: Hola Emi, te presento A Emi, Lucio.

**Lucio Rojas**: ¿Qué tal, cómo estás?

**Isabel Moreno**: Nuestra team de digital, así que te hace entender bárbaro, bien. Adepte a todas estas herramientas de este mundo agente. Así que tenemos acá un usuario clave, lo que estaba viendo ahora, que te aproveché porque justo lo estábamos viendo con Lucio, simplemente para comentarte a ver cómo lo veías y si te parece que puede ser un camino para lo de alianzas. Nosotros hoy tenemos acá conectado las fuentes primarias, por ejemplo, esta que está acá es Gauss, esta es. ¿Como se llama? Broker, esta es Cobranza, y otras son auxiliares que se van generando adentro. Entonces, repasando un poco las alianzas, teníamos por ejemplo, Me Cubro, lo tenés en el cor, Compara, lo tenés en el cor, Flecha U lo tenés en el cor, Andesmar lo tenés en el Corazón. Y vosotros no te las recito, pero todo el resto está por fuera. Lo que yo quería saber es qué información te llega a vos o cómo lo alimentás, Porque la idea sería que acá el modelo nos permite cargar esas anexas. Entonces la idea sería generar como alianzas que podamos complementar esa información para subirlo acá y después que vos ya tengas el 100% digamos de los orígenes para poder explotar la data y poder llegar al reporte que sacás todos los meses o la frecuencia que vos necesites. Entonces quería que nos comentaras por lo menos un poquito si esto qué tenés por fuera y qué te trae.

**Lucio Rojas**: Me cubro gauss, flecha gauss, compara en casa gauss, creicueltas, prendarios. Yo lo saco del CMI. Podría ser custom entonces.

**Isabel Moreno**: Esperá, si es non, si es broker, ya está, ya lo tenés porque está dentro de las formas.

**Lucio Rojas**: Pero está marcado para Jansa Friend está,

**Isabel Moreno**: o sea no está marcado. Si vos digo, me voy para atrás. En realidad vos tenés custom, lo tenés completo porque tenés el core, entonces si vos tomás algo que hoy toma el CMEI que es del FOR, lo vas a tener en modelo.

**Lucio Rojas**: OK, lo filtro nada más por grupo asegurado, ese filtro no sé si está

**Isabel Moreno**: en realidad acá no tenés filtros, acá construís data y después vos pones los filtros. Lo que teníamos, llegar a.

**Lucio Rojas**: ¿Si custom tiene un campo que es igual, creo que no es flujo asegurado, eso lo hace en CMI, pero que es? No sé. Canal, yo puedo traerme solo eso.

**Isabel Moreno**: Te lo cambio para ser más simple. Si vos hoy estás usando clics y usas una solapa o usas algún componente, lo que sale una vista, esa vista que vamos a hacer copy paste acá podemos pedirle al modelo como ejemplo eso y que lo busque, porque aparte de cargar de origen, cargamos la capa de lógica de Clixel, entonces va a saber interpretar y va a decir che, esto que me está pidiendo Emi ya existe, entonces te va a ayudar para poder construir esa misma información.

**Lucio Rojas**: Genial, eso de prendario lo saco entonces de custom lo voy a sacar. Custodia, después cree cuotas, asistencias, está por fuera, eso es información que nos manda.

**Isabel Moreno**: OK,

**Lucio Rojas**: Sí, podríamos tener un CCB.

**Isabel Moreno**: OK. ¿Querés explicarnos algo, Lucio?

**Lucio Rojas**: No, no estaba justo, honestamente le estaba preguntando a. Yo soy hijo de la UA distinta que teníamos que la otra, estaba preguntando cómo agrupar los distintos SB, una sola fuente, como van a ver acá, el DBSR, Inmigration, el Semi House, todo lo que ustedes suban aparte lo podían agrupar en una fuente nueva buscando la verdad cómo hacerlo.

**Isabel Moreno**: A ver, nada tranqui igual no te preocupes. Más que nada lo que me interesaba es que también sumar la EPI, porque para que ella vaya viendo, así ya puede empezar a jugar con esto. Y si después la fuente anexa o complementaria la puede tener temporalmente pone cloud y después vemos persistirla dentro de la arquitectura nuestra, bueno, vemos cómo y seguramente vuelva a encontrar la vuelta más rápido nosotros. Pero también para que vos te lleves Lucio, decir, no quisiera tener todas estructuras por fuera, sino que me gustaría tener como un repo centralizado, que serían todos estos S que tenés acá. Dentro de ese nosotros podés tener esquemas, porque vamos a tener como en este caso alianza, tenemos, no puedo decir 80-20 porque no es así, pero tenemos no sé, 60-40, digamos distribuido entre cosas dentro de los core y fuera de los core, pero que no quede en sesión del usuario. A eso me refería.

**Lucio Rojas**: Claro, además como un warehouse acá si querés un lay donde podés unificar todas las fuentes que vos quieras, de distintos orígenes, algunas bases de datos, otras en CSV, y todas esas fuentes las podés actualizar, todo lo que sea CSV en función de la periodicidad que vos quieras, agarrás, reemplazás el archivo, lo generás de vuelta y eso ya se cruza en la herramienta. Una tabla nueva de resultados contra la base de datos. No hay problema, ahí vos tenés que decir cómo subir todo. Sol, gracias por subirte. Estamos en una duda acá de UAL, más que nada porque sé que se puede. ¿Cómo hacemos sol para? No sé si nos escuchás.

**Isabel Moreno**: Sí, te escucho.

**Lucio Rojas**: ¿Para agrupar los archivos por fuente o crear una fuente con distintos archivos?

**Lucio Rojas**: Mira, cuando subís todos los archivos, dale a conectar.

**Lucio Rojas**: Ahora no se puede comprar el nombre de CH. OK, OK, entonces no la quería mostrar. Bueno, listo. Ahí Fer, pensé con que lo modificamos de última eso para que puedan tener como un repo para fundar todas las fuentes.

**Isabel Moreno**: Yo trataría de tener esto como si querés nivel 1 y después adentro de eso todos los repositorios, porque nos va a pasar por ejemplo con. Hola Sol, que no te saludé, perdón que arranqué y no paré de preguntar cosas, pero la idea sería generar como un árbol de jerarquías que tengamos ahí adentro, decir che mirá, estas son todas mis sources primaria, por ahí tenemos las secundarias que tienen que ver esto con datos, por ejemplo en este caso alianzas nos va a pasar con los presupuestos, entonces va a haber un montón de cosas ahí atrás que vamos a estar metiendo, pero que tenga alguna estructura, a eso me refiero más que nada es eso, si podemos. Y agrupadores, porque si no van a ser todos archivos tirados SB ahí al

**Lucio Rojas**: voleo, por ahí deberíamos tener uno para. Tenemos algunos proveedores de asistencia que no van a estar en custom, porque generalmente las para afuera haya un archivo para Cardinal, un archivo para IGS y un archivo. No sé si tenemos alguno más acá.

**Isabel Moreno**: Entiendo, o sea, por lo que yo entiendo ahí, corríjame Sol y Lucio podría tirarlo, digamos, como si fuera en el explorador de Windows donde lo tiro y ya está lo que queremos como organizarlo.

**Lucio Rojas**: Entonces

**Isabel Moreno**: si se puede armar eso, genial.

**Lucio Rojas**: Sí, tipo repositorio de carpeta para los archivos que va subiendo. Entiendo, no hay problema.

**Isabel Moreno**: Si tenemos eso, por ejemplo Alianza ya lo podríamos empezar a trabajar.

**Lucio Rojas**: Yo estoy prometiendo como si lo programase yo no, pero entiendo que se puede hacer.

**Lucio Rojas**: Bueno, sí, salvo las asistencias, todo el otro está buen custom, nos faltaría resolver esta parte de las asistencias, pero por

**Isabel Moreno**: ejemplo, pregunto nada más, todo lo que es autor, todo eso va.

**Lucio Rojas**: Debería estar cargado en custom, o sea

**Isabel Moreno**: que el track sería asistencia por juego. Bueno, nada, buenísimo, entonces con eso lo podemos armar. Yo trataría igual, Emi, de arrancar con lo que tenemos, en todo caso pues complementamos.

**Lucio Rojas**: Yo todavía lo que no sé es cómo llegar a campo al dato que necesito, o sea, sé que tengo que pasar varias capas, pero bueno, no sé.

**Isabel Moreno**: Después Juan, te voy a decir la buena y la no tan buena. Nosotros tampoco sabes cómo llegar, ahora estamos construyendo, pero nada, igual llegas rápido.

**Lucio Rojas**: Lo que sí les puedo mostrar cómo lo saco yo y qué dato uso para armar el reporte y cómo llevo ese dato, eso se los puedo mostrar en algún.

**Isabel Moreno**: Eso podemos alimentar cuando empezás a rondear. Pero digo, lo que estamos trabajando también con Lucio y Consol era. Estamos tratando de entender el modelo de cómo construirlo, o el mejor modelo. Entonces, por ejemplo, esto te decía, cuando Lucio empezó a trabajar que hicimos renovaciones, él se alimentó, no sé, por ejemplo, de la sesión que tuvimos se generó un md o un archivo de soporte para subirlo al modelo, después fuimos a Clicksense, hicimos print de todas las pantallas para ver, decir che, esto es lo que queremos lograr, después bajamos y fuimos y dijimos che, mostrame el esquema de esto y ahí empezamos a iterar, o sea fue todas iteraciones hasta que llegamos al resultado final.

**Lucio Rojas**: Por ejemplo Gauss yo sé que tiene un montón de tablas, yo uso el reporte de operaciones emitidas, bueno si vos

**Isabel Moreno**: tenés precisión de lo que usás, es más, podés subirla hasta inclusive el reporte, yo uso esto para que aprenda y después generar el.

**Lucio Rojas**: Si yo le enseño en mi sesión esta que me abriste, le estoy enseñando para todos.

**Isabel Moreno**: Bueno, eso es lo que decíamos acá, que en realidad vos tenés usted chicos, si estoy una barbaridad, me levanto, me dicen o lo corrigen ustedes, pero básicamente cuando empezás a trabajar la sesión va a quedar en tu hilo de sesión tuya. Ahora si después pasamos a tabla de resultado, ya ahí se comparte. Es como se comparte en el ecosistema, vos no vas a editar, pero sí posiblemente vas a necesitar generar tablas de resultados por si no te va a persistir el dato.

**Lucio Rojas**: Vamos a publicar esa tabla.

**Isabel Moreno**: Exactamente, cuando vos llegues y digas che mira esto es lo que realmente quería, le podés decir pásamelo a una tabla de resultados y eso es lo que los chicos vas a escuchar que hablan de las tablas gold. Entonces después cómo lo haces, por ejemplo lo podés trabajar con el artifact, capaz que ya hiciste algo de eso en cloud o no, pero bueno, básicamente como template digamos HTML que podés operar ahí. Entonces el dato que entiendo, salvo que me digas sobre otra cosa y así estamos funcionando con esto, pero digo mucho de lo que va a pasar, la que mayor expertise va a tener para llegar a ese dato vas a ser vos. Lo otro podemos trazar nosotros la ruta, decir che, pregúntale a esto, no sé, que te dé el esquema, vamos haciendo ese caminito juntos y lo que no excede a nosotros dan los chicos para dar más soporte si nos llevamos puerto.

**Lucio Rojas**: Sí, lo que decíamos el otro día con sobre también es como tener medio, no te digo un glosario, pero entender cómo le están llamando a cada campo, a cada columna o a cada cosa, como para decir, no sé, si yo le digo operaciones emitidas de Gauss, entiende que son operaciones emitidas de Gauss, ahí

**Isabel Moreno**: Sol y Lucio, digo, es un buen punto que nos comenta Emi, que algo hablamos, porque inicialmente cuando empezamos con esto con Juan, creo que lo que hizo es un poco justamente diccionario de datos y varias cosas ahí que La fui sacando. ¿Cuál sería la mejor práctica? Porque el modelo es amplísimo. Si vamos a hablar de Gauss, tenemos 1900 y pico de tablas, quizás armar todo ese modelo de cómo está hoy o cómo se llaman todas las tablas o los campos, no vale la pena. Ahora, ¿Cómo les parece a ustedes que no sé, Emi me decía recién, tengo que ir a buscar, yo ya sé que hay un reporte que es operaciones, ese reporte de emisión quizás tiene variables, y cómo generamos ese catálogo? Podemos pedirle al modelo, armame el catálogo en base a esta tabla. Ya el catálogo me queda para que siempre después la próxima vez cuando lo pida, ya sepa cómo hacerlo. ¿Cómo nos siguen con eso?

**Lucio Rojas**: Medianamente, si quieren podemos. Hagamos una sesión desde cero y busquemos llevar un resultado entre todos. Así cómo funciona. Doy por descontado lo que vimos la sesión pasada, Fer, las clases, Lucio

**Isabel Moreno**: y bien, ¿Dónde das clase?

**Lucio Rojas**: ¿En la UCA? OK, bien, Tecnologías aplicadas, por descontado eso, así cualquier cosita que haya pasado

**Isabel Moreno**: está bueno que está Emi, porque Emi va a ver un montón de cosas y le va a sacar cubo rápido.

**Lucio Rojas**: Voy a hacer una cosa, voy a hacer la demo como para vos, así cómo empiezo de cero, se puede subir. Cualquiera que no haya entendido alguna parte de atrás. Hago una consulta inicial para arrancar. ¿Tenés idea de que este era la primera vez que tú estás escuchando? ¿Sabés qué hacemos?

**Lucio Rojas**: Estoy en tema de lo que hacen y de hecho ya tengo acceso. Pero bueno, cuando yo quise ahora cuando hice el informe de alianza de agosto, como que intenté ver si llegaba desde mi sesión y no llegué, porque se ve que o le llamamos diferente o todavía no sabe qué estoy buscando. Pero sí estoy en te.

**Lucio Rojas**: ¿Y ese reporte usa tablas que vos tenés en alguna de las fuentes que tenemos cargada?

**Isabel Moreno**: Sí, Gauss usa Gauss.

**Lucio Rojas**: Uso Gauss y uso custom, que lo consumo más desde el non porque me es más rápido, pero en definitiva custom.

**Isabel Moreno**: ¿Por qué no hacemos si querés, que pusimos la otra vez con vos para alguno que esté en una fuente, por ejemplo, algunos de los? ¿Y después vamos a la otra historia, Por ejemplo, me cubro compara cuál te gustaría?

**Lucio Rojas**: Sí, cualquiera de esos.

**Lucio Rojas**: Cualquier reporte que. Vamos, un caso de uso, para entendernos. Cualquier reporte que tengas a mano y quiera copiar, si me lo pueden pasar, los copiamos ahora en vivo para entender bien punta a punta de la herramienta, ¿Les parece? No sé, Fer, si ahí te parece.

**Isabel Moreno**: Sí, sí, me parece perfecto.

**Lucio Rojas**: Te paso, por ejemplo, un reporte de. No sé, de Me Cura.

**Isabel Moreno**: Si tenés alguno del que vayamos a buscar ahora, por ejemplo, si tenés de Mecuro y te es más fácil, pasamos Me Curo y vemos. Me cur. Si querés otro, no sé, tenés mar, flecha, lo que sea. Porque si hacemos ese ejercicio, después ya el resto empezamos a trabajarlo en el cuerpo.

**Lucio Rojas**: ¿Pero ese es el de emitidas de lados o lo armo yo con el de mis tías de Gauss, y es

**Lucio Rojas**: donde me vas a compartir?

**Isabel Moreno**: Va a pasar el informe puro de Gauss, que es el que después le da origen. Para. Origen el reporte de mi tía y el que vos armas para el look and.

**Lucio Rojas**: El MCB. A veces se puede llegar a desconectar, pero tienen que reconectarlo desde el conector y le llega esto.

**Isabel Moreno**: Lucio, ¿Nos das un segundito nada más? Ya estamos.

**Lucio Rojas**: Sí, sí, para el reporte, para pasármelo. Sí, ahora te lo están pasando buenísimo. Hay soltaciones, Lucio.

**Isabel Moreno**: Ahí está. No tenés la dirección de.

**Lucio Rojas**: No,

**Isabel Moreno**: ahí te lo paso así. Se lo pasas directo y ya.

**Lucio Rojas**: Me lo pasan por Slack.

**Isabel Moreno**: Ya te lo pasa.

**Lucio Rojas**: Te lo paso por mail. Lo que estoy buscando es el legado, porque si la bajo tarda un montón en bajar, ¿No?

**Isabel Moreno**: Algunos ejemplos. Ahí te lo pasé a mí. Ahí te lo manda Lucy.

**Lucio Rojas**: Ah, bueno, tengo el de julio, ya. Está cargando porque tarda un toque.

**Lucio Rojas**: Mientras tanto que un reporte de gestión.

**Lucio Rojas**: De una sola alianza, después hago lo mismo con ocho, nueve alianzas, y vos

**Lucio Rojas**: te conectas al sistema, te bajas algunas tablas, las cruzas de cierta manera y generas este reporte. ¿Con qué periodicidad?

**Isabel Moreno**: Exactamente, ¿Con qué periodicidad lo haces?

**Lucio Rojas**: Ah, lo hago semanal y mensual.

**Lucio Rojas**: Bien. ¿Y siempre es la misma? Es como si fuese una función, la misma regla lógica. Vos te lo bajás y corrés lo mismo y llegás al mismo resultado. ¿Siempre o te cambia?

**Lucio Rojas**: No, siempre es lo mismo. Puede cambiar, Si, no sé. Porque lo que yo consumo es un reporte de operaciones emitidas. Si alguna se anuló o se anuló para atrás, ahí puede llegar a cambiar, puede ser dinámico, pero yo me lo descargo todas las semanas y me lo descargo una vez por mes para hacer reporte Y después si lo que cambia es por negocio por ahí uso otras lógicas u otros reportes para. Este en particular es el que te pasé.

**Lucio Rojas**: ¿Me lo pasaste por mail?

**Lucio Rojas**: Sí,

**Lucio Rojas**: ahí lo abro.

**Lucio Rojas**: Te pasé dos archivos. Uno es como la sábana completa que es el que descargo de Gauss y otro es el consolidado que me voy haciendo yo mes a mes con la info que saco de la sábana.

**Lucio Rojas**: Me cudo mi tío, supongo que es el.

**Lucio Rojas**: Ese es el legado que le cambié el nombre, pero.

**Lucio Rojas**: Voy a descargarlos. Ventas y negocios digitales y Alianza. Entonces debería estar en Gauss. Ese no lo voy a usar, voy a usar el otro en realidad.

**Isabel Moreno**: Perdona, no está en Gauss, o sea el origen de parte de esas alianzas vas a tener data de Gauss, pero el look and feel que te pasó con el cuadro. No, porque lo arman por fuera.

**Lucio Rojas**: El que dice ventas lo armo por fuera. El que dice emitido es el que me tira Gauss.

**Isabel Moreno**: OK.

**Lucio Rojas**: Con otro nombre porque le cambié el nombre.

**Isabel Moreno**: Tenés ahí lo que te llegó, Lucio.

**Lucio Rojas**: Ahí está escuchando Sol. ¿Se escucha? No estoy pudiendo pegarle el proyecto desde. Como que está enviando otro y no me deja cambiar ahí voy a probar con reconectar el M Cuad. No sé si escucha. Estoy pudiendo. Mientras tanto los mails que me mandan son estos chicos.

**Isabel Moreno**: Ahí estamos. Ese es el reporte que sacas de Gauss. ¿Y se llama así? Reporte o se llama.

**Lucio Rojas**: No, tiene un nombre en la plataforma. Es Operaciones. Reporte de operaciones emitidas. Y después el nombre del archivo cuando descarga es tipo CE

**Isabel Moreno**: Reporte de operaciones Emitida.

**Lucio Rojas**: Y esto es lo que permás vos.

**Lucio Rojas**: Claro, yo completo todo eso mes a mes porque encima tarda un montón en bajarse, entonces si llego a tirar de enero ahora puedo estar tres días para bajar

**Lucio Rojas**: el mesuro. Mi tío tarda el download.

**Lucio Rojas**: Si, tarda 1 porque son 20.000 registros aproximadamente por mes.

**Isabel Moreno**: Es uno de los negocios masivos que tenemos

**Lucio Rojas**: y eso está dentro del. Bueno, ahora sí me pude conectar a la fondo, así que empecemos a trabajarlo, qué es el paso de siempre conectado Beacon hay proyecto WW, que es su proyecto y decime qué fuentes tenés ahí.

**Isabel Moreno**: Me mataste con el BW.

**Lucio Rojas**: Esto es el ID del proyecto. Yo lo necesito porque mi usuario de Teramot tengo más de un proyecto, tengo uno personal, entonces para rutearlo le digo, anda el proyecto este, ustedes como tienen uno solo no tienen ese problema generalmente.

**Isabel Moreno**: OK, pues yo ahí lo que le digo es conectame directamente a theramot y opero sobre esa línea.

**Lucio Rojas**: Claro, sí vos tenés esa línea, yo como tengo varias, lo tengo claro que direccionar. Bueno, decime qué fuentes tiene. La pregunta bien, bien básica para arrancar. Y yo sé que voy a trabajar sobre el Gauss, entonces le decía unos

**Isabel Moreno**: pasos que está haciendo Para un segundito, Lucio. Primero tendrías que conectarte a theramo. Que es lo que. Lo primero, pedirle la conexión. Eso no lo vimos, no siempre, pero por buena práctica lo terminamos haciendo. Conectame para asegurarte que va a estar. Y después ahí está pidiendo que pidió las fuentes. Sí, igual ahora no te preocupes, después grabamos esto y lo hacemos. Pero digo, después te pide las fuentes para saber que aparecen todas las fuentes acá. Y vamos a pegarle a esta una que es la que está de.

**Lucio Rojas**: Le voy a pedir que me haga un EDA, que es un análisis exploratorio y descubrimiento de las tablas, para que ya empiece a interiorizarse el modelo que tiene. Y le voy a decir que me lo explique medianamente en formato de estos primeros pasos. Yo lo hago siempre para contextualizar el modelo y para contextualizarme a mí, porque también es importante como uno saber bien qué tabla está trabajando, pues no le puede decir cualquier cosa. ¿Entonces ahora qué hace? Usa el conector nuestro para llamar a las tools de descubrimiento de esquema. Lo que hace la tool de descubrimiento de esquema es manda a theramot a mirar cada una de las tablas del Gauss y entender qué es esa tabla. Entonces ya sabe eso y vos no tenés que estar usando las tablas. Después tenés una descripción del esquema, aparte de ver todo, ¿Lo entiende? Bueno, estoy mapeando la estructura. Gauss MPB tiene 1981 tablas. Ya identifiqué las tablas principales, que son las de pólizas, las de cuotas y la de siniestros. Y ahora estoy leyendo sus columnas antes de consultar los datos. Ya tengo las columnas de las tablas principales, ahora consulto los datos para leer. Estamos trabajando casi a nivel de Big Data, estamos analizando la tabla entera con la consulta que hicimos ¿Qué voy a hacer con esto? Voy a empezar a entender un poco esta base y le voy a mostrar la foto final de donde quiero llegar, que es el reporte que ustedes me pasaron. Así voy a buscar yo que solo lo conecte los puntos de tengo esto, llegaste a esto, bueno, voy a hacer esto en el medio para llegar. Y eso lo hace de forma automática. Si no sabemos a qué queremos llegar, por ahí un poco más difícil, voy a explicárselo, pero tendríamos que explicarles bien cuál es el reporte que queremos armar acá va a tardar unos minutitos.

**Lucio Rojas**: ¿Cuál le pasarías primero, el que armo yo o el que vos querés encontrar de Gauss?

**Lucio Rojas**: Era la duda que tenía. La pregunto de vuelta. ¿Esto no es una tabla de Gauss, ya? Es un cruce de tablas que se arma Gauss sería una tabla Gauss, ¿No?

**Lucio Rojas**: Sí, así me lo da Gauss. Pero entiendo.

**Lucio Rojas**: Claro, pero ponele atrás de esto, Gauss, está esto como una vista que tiene gauss. Está juntando cuatro o cinco tablas.

**Lucio Rojas**: ¿Sí?

**Isabel Moreno**: Para que salga esto, te voy a hacer una ejecución de.

**Lucio Rojas**: Bueno, entonces lo que yo voy a hacer ahora es pasarle este primer reporte y voy a decir, fíjate que primero le voy a explicar lo que quiero hacer. Quiero llegar a este reporte. Para eso me bajo una vista del Gauss y demás. Le voy a pasar esta vista, voy a buscar que la replique y después le voy a pasar el resultado tuyo para que trabaje sobre esta vista que vamos a copiar. Mientras va escribiendo le voy a explicar. Quiero generar un reporte final. Yo siempre lo hago mucho de darle el contexto. Cómo es el nombre del reporte final que generamos.

**Isabel Moreno**: Un segundito, Lucio, que estamos con una contingencia. Ya estoy. Like. Vamos a cambiar un segundo porque Isa tiene que salir, así que voy a cambiar. Voy a cambiar la sesión. Ya está.

**Lucio Rojas**: A mí me sirvió para ir escribiendo de paso.

**Isabel Moreno**: Ya estamos. Por las dudas. Lucio, tenemos que ver algo.

**Lucio Rojas**: Bueno, me vino ahí el espacio publicitario para que termine de trabajar. ¿Qué pasó? Yo lo mandé a hacer un EDA de Gauss para que entienda al respecto la fuente. Y esto es lo que vamos a querer siempre. Yo trato de arrancar por acá. Da el sistema central de pólizas de B Seguros. Es la base del sistema de gestión de la aseguradora. BIN guarda las pólizas, los endosos, la cobranza, los siniestros, las comisiones, la contabilidad. Todos los montos que muestro están en pesos, salvo que sería otra cosa. Las tablas 1981 tablas, casi todas están vacías, la tabla tiene 1000, la fuente tiene 1980 tablas y 29.000 columnas. Acá vemos de vuelta que no tienen descripción, así que la va generando y me va mostrando distintos conjuntos que son como de fijos que tienen las tablas que los agrupan. Dice bueno, las Z son 695 tablas, que son tablas de configuración de seguros, ramos, productos, PM, coberturas, tarifas. Las tablas CPH son 354 y guardan movimientos de seguros, pólizas, endosos, cuotas, aseguradores, mientras, demás. Y así fue pidiendo todas las tablas importantes para el negocio, me dice son CJOP que tiene 339 mil filas, que es la operación o póliza madre, contornador, productor, moneda media de power, canal comercial, carga, CEPOL. Se me fue describiendo todo. Después me hace un EA que son de los números. Me dice las carteras de pólizas, tiene 620 mil pólizas emitidas entre el 2023 y hoy. La fecha de arranque sugiere que la historia empieza con la migración al sistema. La fuente BIM migración apunta lo mismo, tiene el estado de las distintas pólizas, tiene 95% con estado A, otras con estado B, supongo que estado A es activa y es baja o anulada. Me ve las monedas, los totales en pesos y ve cuáles son los distintos ramos. El ramo 14 es AP colectivo con tantas pólizas, el 15 es riesgo varios con tantas pólizas. Así no hizo un mapeo completo, un descubrimiento de lo que tienen los datos, que acá no estamos ahorrando infinito tiempo, porque una vez que hicimos esto no lo tuvimos que hacer manual y ya podemos empezar a trabajar con agente sobre la base y sacar los reportes muy rápido porque Glo ya entiende todo esto.

**Lucio Rojas**: Perfecto.

**Lucio Rojas**: ¿Qué hice acá? Le dije, siempre voy, trato de ser lo más general posible con los objetivos que les doy y le digo bueno, quiero generar un reporte final que es ventas de negocios digitales y alianzas, etc. Que me contaste vos, digo de realista, una analista de B, perdón, no sé si sos analista o no, pero tenía que intentar un rato. Con periodicidad semanal o mensual, partiendo de un reporte de Gauss. El reporte de Gauss lo bajan del sistema, ya es una vista del mismo y se llama Me cubre omitido. Sé que tiene otro nombre, pero estaba guardado así se lo pasa así. Vamos a idea de la base de Gauss para entender las tablas. Ya hiciste B, vamos a copiar el reporte que baja en ellos del sistema como tabla de resultados. Así estamos trabajando sobre la misma base. Esto yo busco que lo interprete solo de cómo está generado, nunca le dije qué tablas usa, cómo se forma esa tabla ni nada. Y C, una vez con A y B hechos, vamos a generar el nuevo reporte de analista para dejarlo comenzar. Te doy los dos Excel para que levantes la lógica detrás de cada uno y me digas el paso a cero. Eso se lo dije hace tres minutos y lo puse a trabajar. Está usando las distintas tools que ya siempre vemos. Este primer tool es hacer un mapeo del Excel, lo está investigando para ver qué tiene, leyendo los datos del Excel y ahora no sé muy bien qué va haciendo, debe estar razonando cómo copiarlos,

**Isabel Moreno**: haciendo eficiencia, mientras que hago tal cosa hago otra 10 más.

**Lucio Rojas**: Muchas veces estos modelos es re loco, pero están haciendo algo y mandan a subagentes hacer otra cosa, y generalmente mandan a uno menos inteligente que dicen yo soy opu, bueno lo mando a hype o hacer tal cosa, mientras yo sigo con esto de que cuando termine me manda resultados. Corren agentes en paralelo,

**Isabel Moreno**: o sea acá no lo ves, pero por detrás decir que están corriendo los subagentes a veces

**Lucio Rojas**: si te dice no, creo que no

**Isabel Moreno**: lo está haciendo todavía.

**Lucio Rojas**: Si te dice mando a hacer tal cosa a tal agente y vos lo cumplías dos tareas en ejecución. Si yo lo abro, veo cómo está haciendo esto, no me dijo cuál es el modelo que usó y ya finalizó otras dos ¿Que es qué está haciendo? Está leyendo los excels, ahora está leyendo Gauss y está rearmando las filas. Bueno, acá no hay mucha más magia que un ratito a que genere y seguramente me va a decir cuáles son mis tablas go que tengo que armar para copiar el cubo emitido y después va a entender el cubo emitido como llevo hasta ventas de Noce.

**Isabel Moreno**: Y supongamos que ahora sabiendo que esto va a terminar y vamos a tener resultado y que lo que teníamos pensado para ahora era un poco transferir el tablero anterior. Supongamos que esto lo hacemos ahora y va a caer la misma suerte porque lo vas a tener en tu sesión el paso siguiente para que quede. ¿Que le vas a pedir? ¿Un MD, un README qué le pedís para que te haga que todo esto después sea transpolable a otra sesión

**Lucio Rojas**: y qué sería lo que vos querés extrapolar?

**Isabel Moreno**: Por ejemplo, todo el recorrido que hicimos ahora me lo quiero llevar para no perder el contexto y llevármelo a mi sesión para que después se me agarre y siga operando. Por ejemplo, el tema alianzas, lo que vos generes ahora en las tablas de resultados, que entiendo que esas son gol y estarían disponibles independientemente. Si yo tengo el pro,

**Lucio Rojas**: yo haría dos cosas. Lo primero que haría sería guardar el conocimiento entero, que lo guarda tipo de yamo, así yo próximo agente. Eso por un lado. Las gols también por ese mismo lado. Y por el otro le puedo decir a Claude, sí hace un MD con todo lo que aprendiste en esta sesión, yo lo paso a Emi, lo copia en la sesión de ella, de Claude y es como que revive ahí.

**Isabel Moreno**: OK. Que ese sería el más, digamos, lógico para la sesión de cualquier usuario que vayamos haciendo esto asistido, ¿No?

**Lucio Rojas**: Digo, claro, Vamos a esperar un rato mientras sigue. Yo no estoy muy seguro.

**Lucio Rojas**: Sí, perfecto, o sea es como. Por eso yo no podía ir directo al reporte, como que me faltaba hacer toda esta parte de entender la lógica de Gauss.

**Isabel Moreno**: El, o sea, podías llegar igual pero llegarías un poco más largo. Va a tener que integrar mucho más. En cambio si tenés estas herramientas por lo menos, como no, yo por ejemplo

**Lucio Rojas**: para sacar la prima, agarro el premio que me da y lo divido por 1,31. Ahí yo en realidad debería ir a decirle bueno, tráeme la prima que está en otro reporte.

**Isabel Moreno**: Totalmente. De hecho lo que hagamos en alianza, como tenemos que hacer ventas, también va a ser parte. Ya es como que estamos abordando una partecita del universo.

**Lucio Rojas**: Sí, yo creo que es entender de dónde sacar estos KPI. Son los mismos que después pide Seba para el de venta, el 360, una vez que llegamos como a emitido prima.

**Isabel Moreno**: Correcto. Y validarlo, por ejemplo en el de renovaciones, nos pusimos a jugar, entonces dije bueno, probalo vos. Yo no quiero probarlo probalo vos, porque vos sos el que tiene el número en la cabeza. Entonces cuando fue me dijo, mira, esto no puede ser, porque por ahí, no sé, vos tenés renovables o no renovadas, o es renovada, no renovada o no renovables. Me dice, agárrate estos dos casos y fíjate a ver si está. Entonces es viendo si lo que estamos desarrollando llegas a tener la lógica adecuada.

**Lucio Rojas**: Y si no, la otra que hago es bajarlo, pasárselo a Gemini y que Gemini me lo desglose.

**Isabel Moreno**: Pero acá, acá lazo porque estás sobre cada tapuna.

**Lucio Rojas**: Y el semanal que hago lo diseño en clock.

**Isabel Moreno**: Claro,

**Lucio Rojas**: porque es el personaje.

**Isabel Moreno**: Pero bueno,

**Lucio Rojas**: Estoy pidiendo el MD.

**Lucio Rojas**: OK, después eso ustedes me lo pasan.

**Isabel Moreno**: Perdóname Lucio, te quería preguntar, ¿Eso lo subís después en la sesión en contexto?

**Lucio Rojas**: No, este MD que estoy pidiéndole, yo le pedí al chat original mío de Claude, con el que generé el tablero de renovación, le dije necesito que hagan memoria de cómo armamos todo lo del tablero de renovaciones, le puse entre paréntesis, no lo otro que hablamos, porque después le pedí unos resúmenes de cómo habíamos trabajado para tomar memoria. Y le digo, y me genere un MD para contextualizar un agente de cloud code de la gente de BIN en cómo hicimos todos y ellos puedan sumar la vista de vencimiento de responsabilidad, así ustedes puedan sumar esta segunda vista que pidió Seba, que yo todavía no la sumé.

**Isabel Moreno**: Está bien, igual ahora perdona, ¿Estás trabajando sobre renovaciones? No, sobre lo de.

**Lucio Rojas**: Hice un cambio, hice las dos cosas para. No, Pero son justo dos tareas que llevan tiempo, así que voy a estar pensando un rato. Este lleva 11 minutos y me comí un poco. Stopongo que estará corriendo algún.

**Isabel Moreno**: Ahora te hago una pregunta. Cuando yo levante mi sesión de cloud de nuevo SMD que vos me pases.

**Lucio Rojas**: Claro, lo copias, le pegas el MD en el chat y ya entiende ahí todo el knowledge. No sé cuánto tiempo tardarán en correr estos agentes. Creo que no tarden mucho más, porque si no nos vamos a quedar. Este es el riesgo de hacer las.

**Isabel Moreno**: Sí, o sea, te tenés que hacer amiga. Va a ser tu mejor amiga.

**Lucio Rojas**: Sí, una vez que entienda, después son muchas alianzas.

**Isabel Moreno**: Cuando le tenés el modelo, si está ahí adentro, le vas a decir, che, tengo una alianza nueva cambia el producto,

**Lucio Rojas**: pero es la misma alianza.

**Isabel Moreno**: Es que sí decís lo mismo, subímelo a la bitácora.

**Lucio Rojas**: Acá está CMI renovación y BIM, cómo está construido, cómo está en texto por un agente de Cloud Code que trabaja con el conector de TCON a la organización de BIN, que explica qué es el tablero de renovaciones, cómo se construyó de punta a punta, qué regla de negocio aplica, qué trampas tiene las tools y cómo agregar la vista de vencimiento correspondiente. Todo lo que dice acá está verificado contra Custom en septiembre, donde algo quedó pendiente de confirmar un control y acá sé todo el MD, que justamente la función principal de este MD, no que lo lea la gente, así que te lo voy a pasar acá por.

**Isabel Moreno**: ¿Estoy pensando, este es el de renovación, o sea que si yo por ejemplo agarro esta vista que era la que faltaba por ejemplo de responsables, que es la que vos tenías el prim, yo tengo mi MD, lo bajé a mi sesión y ahora le digo che mirá necesito, voy a tener que modificar la tabla de resultado o generar una nueva tabla de resultado?

**Lucio Rojas**: ¿Generar una nueva? ¿No, las tablas de resultados son paralelas, vos podés tener RN, pero digo, por

**Isabel Moreno**: default me dice, o sea lo que quiero entender es, por default me va a intentar generar una nueva vista o va a decir che para que ya existe una tabla de resultados para esto, la actualizo?

**Lucio Rojas**: Justo lo que estamos queriendo hacer es algo que no tiene una tabla preexistente para hacer la vista esa de, ¿Cómo era el nombre? Renovaciones, no, de vencimiento por responsable, hay que hacer una tabla nueva. Entonces ya le explicó mi agente a tu agente cómo hacerla en este medio que te pasé, pero si tuviese que ver algo de renovaciones, retomaría lo que ya,

**Isabel Moreno**: lo que ya trabajó, o sea, si tengo que hacer una modificación al artifact este que vos ya desarrollaste, que ya lo tenemos disponible y le tengo que pegar, tengo que invocar ese artifact y decirle que ahora lo voy a modificar.

**Lucio Rojas**: Sí. Tiene que tener todo el contexto, de paso lo voy a decir.

**Isabel Moreno**: Te hago una pregunta más, si querés más técnica por ahí. A ver, si lo que quiero evitar es que ponele, no porque alguien quiera modificar, pero alguien quizás sin intención y quizás trabajándolo sobre el pronteo que no se vaya a romper esa vista, o sea, vos decís, che, tengo armado el tablero de renovaciones que ya lo está viendo, no sé de Sole, vamos a poner, Seba lo tiene y mañana venimos nosotros toqueteando algo, se lo plancho y lo reventé al tablero de nuevo cómo hago para. Existe manera. ¿Eso es corrol donde no le voy a dejar hacer algo existe alguna manera de que eso no se modifique y que no se toque?

**Lucio Rojas**: ¿Vamos a ver nuestras tablas por rol seguro podés gestionarle los rolls a las personas para que no puedan modificar tablas all o crear tablas nuevas lo que no estoy seguro y ahí no sé Sol, si me estás escuchando Fernando, por slab tenemos versionado sol de las tablas

**Lucio Rojas**: golpe y van a verse anterior siempre podés ver cualquier versión que vos quieras

**Lucio Rojas**: voy a tratar de traducir, creo que tenés versionados y podés volverte a la versión anterior si se llega a romper algo que? Escribí todo no se te escucha escribí por el chat, no se escucha nada y te vamos siguiendo ahí las instrucciones. ¿En pantalla acá tenés claro la versión, tenés B OK y B hace seis días y acá me faltaría solo nomás que me digas cómo acá está las versiones, cómo guardo la versión anterior

**Isabel Moreno**: OK y ahí, pero por ejemplo, esas son el versionado de la tabla de resultados es al darle resultado linkea con el

**Lucio Rojas**: artifact Sí vos ves el versionado del

**Isabel Moreno**: artifact también Claro, no pregunto simplemente para entenderlo, digo,

**Lucio Rojas**: no está mal entiendo, o sea, vos crees que si se rompió total de resultados OK, lo último, puedo ver para atrás?

**Isabel Moreno**: Sí, pero no quiero volver a regenerar toda la vista, o sea, ¿Hay alguna manera de dejar esto trizado?

**Lucio Rojas**: Ahí puso Sol, por ahora no está, estudia lo griego pero si puedes volver a traer una versión de azul esto lo tiene usaste Fer la versión de artifacts de. Eso mismo deberíamos tener acá pero ahí está diciendo que sí puso por el chat que lo va a agregar.

**Isabel Moreno**: Perfecto,

**Lucio Rojas**: yo creo que.

**Isabel Moreno**: A ver, lo de renovaciones ya que estamos viendo mientras que el otro procesa, lo vamos a estar viendo el lunes el lunes ya lo va a estar viendo Seba, Sole, van a estar trabajando un poco sobre eso vieron que les dije que estábamos con una contingencia, pero más que nada era porque estábamos viendo esa vista de renovaciones. Tenía el responsable de la última renovación o responsable de renovación mejor dicho, de la última y eso lo teníamos que impartar por custom. Así que estábamos viendo eso. Ahora en este momento es parte de esa vista que tenemos que construir. Si eso no está actualizado o sigue torcido, pero van a empezar a hacerle doble clic a lo que es renovaciones. Bueno, la idea sería después seguir como le dije, con venta. ¿Que parte de la venta? Bueno, ya estamos adelantando algo, estamos viendo alianza. Así que Vanessa me hizo,

**Lucio Rojas**: me devolvió la lógica de cómo tendremos que hacer esto. Muy parecido a lo que hice yo en un primer momento. Para renovaciones me cubro AP, que es el nombre del cómo se arma el reporte y pasos para automatizarlo. Revisé los dos excels y los crucé contra Gauss. Todos los números de ventas del reporte de la lista salen de la base de Gauss y los pude reconstruir al centavo. Queda una sola diferencia en anulaciones qué hay en cada archivo. Me cubre. Ahí se entiende mejor la parte de esa me cubre omitido Excel El export de Gauss es la pantalla de Gauss. Trabajar con operaciones emitidas filtrada por el producto AP Mecubro Ramo 14 AP Colectivo, Póliza 1477 y por la fecha de emisión. Este archivo cubre del 1 del 7 2026 31 del 7 de 2026 tiene 20.000 filas, una por movimiento 19.946. Trae 27 columnas póliza en dos operación, plan de cobertura 13 planes sobre todo laboral M fecha de emisión, vigencia desde iasta, prima, actualidad, premio, saldo, etc. Ventas, negocios digitales y alianzas. Excel La única hoja visible es mi cura P, una fila por mes desde enero 2025 con objetivos, ventas, primas, facturación, anulaciones, jornales, promedios, etc. Tiene tres hojas ocultas que se cargan a mano. Directorio, mayo, el presupuesto 2026, el forecast de todas las líneas de negocio, facturado, cobrado, un checklist por socio y CC, asistencias, objetivos. Deberías cargarlo tipo archivo ahí al Lighthouse para que pueda.

**Lucio Rojas**: Sí, después en realidad debería pasarle el que tiene ya todas las alianzas. Yo ahora te pasé una por Hola ejemplo.

**Lucio Rojas**: Bien, Bueno, ¿De dónde sale cada columna Fila de julio 2026? Columna del reporte venta. Valor de analista 19.946. ¿Cómo se calcula? Cantidad de espiras, póliza nueva, resultado de texto de Gauss. Lo copió. Copió Jornales, Anulaciones. Vos tenés 75 y él encontró 68. Facturación anulada. Vos tenés 28 mil pesos o dólares.

**Lucio Rojas**: Hay una diferencia que yo tomo prima y él toma premio. ¿Cómo calcula y se suma del premio? Yo en realidad debería tomar prima y

**Lucio Rojas**: ahí se lo podemos explicar ahora. Ahora solamente nos pregunte más abajo. La facturación neta se calcula de la facturación menos lo anulado. La prima emitida es una aproximación mensual de la facturación dividido 1.231. Se puede calcular exacta. Premio menos impuestos. Premio prima promedio promedio de vigencia. Tasa de anulación. Cocientes entre las columnas de arriba. Se calcula así. Me fue explicando en Gauss. Las pólizas nuevas son del tipo de operación 1 y las anulaciones del tipo 4. En las tablas de la diferencia en anulaciones, el Export trae siete filas marcadas como anulación sin número endoso y con premio positivo, unos 16 mil pesos. Son operaciones de reemplazo que no están en cargas de endoso. Por eso el analista 25 y 28 mil pesos. Cuando las 68 reales se suman son 44 mil pesos. Esto hay que refinarlo con P. Es lo que vos me estabas diciendo recién. Conviene contárselos a facturación neta de junio a diciembre de 2025. L. L. La fórmula resta la cantidad de anulaciones de dos filas más abajo, en lugar de restar el importe. En la de I a M, la prima neta cambia de definición a mitad de primero es h a cero. Y de septiembre 2025 para l. Acá yo la verdad estoy entendiendo muy poco lo que me está diciendo. No sé si a vos.

**Lucio Rojas**: Es más análisis y algunos manotazos que metemos a veces con las cosas.

**Lucio Rojas**: Tiene sentido lo que está diciendo.

**Isabel Moreno**: Yo lo anuncio por el tema de. Creo teníamos. ¿Como lo sé si le va a hacer la otra? Podemos llegar a sacar. Llegas a sacar, digamos que te muestre a ver si logra el resultado del dashboard para cerrar el ciclo. Y después habría que hacerlo contra la base completa, que es todas las alianzas.

**Lucio Rojas**: Claro, me dice a ella ya lo hice. B la tabla de resultados me cubre, la construyo yo directo de Gauss, con las mismas 27 columnas que el Sport y una fila por movimiento. Vamos a rápido. Perfecto, así ya tenemos, así vos ya con esto no volverías a bajar más el reporte de Gauss ni el reverb, ya quedaría acá. Y ahora dice reporte automatizado, tabla mensual armada sobre la B. Tabla de resultados con todas las métricas calculadas de la sección 2. Venta, facturación, anulación informal y las fórmulas corregidas. Planilla de datos, manuales, objetivos por mes pagados y no cotización en el CRM que se sube como archivo Beacon y se cruza contra la tabla mensual. Esto es lo que habíamos dicho hoy, hay que subirle los archivos para que los tengan, sin esto no vamos a poder trabajarlo. Actualización programada de las dos tablas los lunes, así el reporte queda al día, semana a semana. Salida un dashboard en Beacon con la misma grilla y un Excel exportable con el formato actual. Lo que necesito que me definas antes de crear las tablas. Nombre de las tablas, propongo, me cubro mi tío el detalle y ventas, negocios digitales y alianzas me cubro mensual. Así resumen, ¿Te sirven? Supongo que sí, porque es el nombre de las tablas, no cambia mucho. Las siete filas de reemplazo. Acá me está pidiendo detalles de lo que dijo antes. Las siete filas de reemplazo sin endoso las cuento con anulación. Cómo se ve el Sport, La prima, uso la prima de Gauss, premio menos impuestos. Vos mantengo el sobre 123 para no romper la comparación con los históricos. Esto vamos a tener que sentarnos a definirlo y vamos a tener que subir los objetivos y cotizaciones a Icon. Así que Ferra, te respondo, no quería llegar a esto, es el reporte, porque tenemos que definir esto y subirle los archivos a Icon. Lo que sí vamos a hacer es armar esta tabla, la tabla esta que bajaban de Gauss, ya que en Beacon y para la última, yo tengo una sesión con. Se me fue el nombre, nunca lo retuve conmigo.

**Lucio Rojas**: Sí, con Emi.

**Lucio Rojas**: Con Emi. ¿Hago una sesión con Emi y lo terminamos de cerrar o le paso un MD para que ella lo pueda retomar desde una sesión?

**Isabel Moreno**: Sí, yo haría las dos, o sea, si querés bajar el MD para que lo tenga, lo tengamos. Digamos ahí. Si se puede dejar la tabla de resultados ya expuesta ahí, genial. Y después hacemos una sesión a dos con Emi en todo caso para continuar, a ver si ya tenemos cómo hacerlo con todas las alianzas.

**Lucio Rojas**: Y si por ejemplo no tengo este archivo de Icon, le dicen ustedes a lo mal, como a los que están, viste que decía como subir a subirlo a Beacon, le digo, toma como objetivo, le paso un archivo con todos los objetivos, acá diciembre no lo puede tomar o sí o sí, tiene que estar en Beacon.

**Lucio Rojas**: Tiene que estar en Beacon sí o sí para poder cruzarlo, porque cruza sobre tablas que tiene en el warehouse, no puede cruzar, va a tener que subirlo ahí o acá hay un Excel con el objetivo, se lo subís ahí.

**Isabel Moreno**: La ideal es que esté dentro del modelo para que. Pero bueno, ahí entonces Lucio, como para ir dando un checkout, ¿Me pasarías, digamos después el md o por slack? Creo que lo íbamos a pasar el

**Lucio Rojas**: MD yo lo pasé

**Isabel Moreno**: y el de Me cubro y después nos confirmas si se puede generar la estructura esa para cargar los soportes.

**Lucio Rojas**: Sí, eso sí. Sí, ya te confirmo. Sería cuestión de cuando lo hacemos, que supongo que ahí te pasé por Slack dos cosas, uno es el MD y otro es un zip que me dijo Clot que le pase a tu clock, que supongo que tiene más archivos que necesita para trabajar abril después.

**Isabel Moreno**: Buenísimo. Cuando tenga el otro, este ya lo vamos a ir avanzando y seguramente lo que se venga es toda la parte de presupuesto que va a ser un poco más compleja. Pero antes de tirarte esto, vamos con alianzas y después te aviso cómo seguimos. Lo ideal sería como un roadmap para ir viendo ya definido qué es lo que vamos a hacer y. Y organizar los tiempos. Lo hicimos medio espasmódico, pero teníamos sesión hoy. Pero bueno, estuvo bueno porque ya por lo menos Emi se puede llevar una vista de esto y es un golazo.

**Lucio Rojas**: Sí, ahí si querés veo que armas bien ahí los proyectos, si querés vos armar algunos roadmap o qué vamos a ver en cada sesión. Yo me puedo anticipar archivos o algo, pasar por Slam y íbamos buscando huecos, así ya lo dejamos definidos.

**Isabel Moreno**: Dale, genial. Bueno Lucio, no sé si Sol está ahí de trasfondo, pero bueno, gracias ambos y seguimos.

**Lucio Rojas**: Dale, gracias. Chau, chau, chau, chau, chau.
