# Hz Group <> Teramot

**Fecha:** 2026-09-03T18:29:44.722+00:00  
**Duracion:** ~37 min  
**Participantes:** Veronica Barrios <veronica.barrios@hzgroup.com.ar>, Lucio Rojas <lucio@teramot.com>, Vikingo <>, Franco Ferrero <franco.ferrero@teramot.com>  
**Externos:** veronica.barrios@hzgroup.com.ar  
**Apollo ID:** 6a99c6182ef8aa00186aed06

---

**Veronica Barrios**: Buenas, ¿Cómo va?

**Franco Ferrero**: ¿Todo bien? Se suma Cristian, ¿No?

**Veronica Barrios**: Sí, sí, sí, sí.

**Franco Ferrero**: Cómo vienen.

**Veronica Barrios**: Hay cosas que en general lo que informa lo informa bien y lo que informa mal es porque le falta información de otras tablas. Me pasa eso. Tengo el desafío, estoy así con un reporte que lo tiré varias veces, el más difícil de todos que es el de. Vamos a ver lo de las telas y después te comento esto, lo de este reporte.

**Franco Ferrero**: Cristian, ¿Cómo estás?

**Vikingo**: ¿Cómo anda?

**Veronica Barrios**: Chicos, hola.

**Vikingo**: Tratando de encontrar lo que hice para ustedes, porque yo hice un montón de pruebas. ¿Vos te acordás que con CSV no había ido, no? CSV no había funcionado porque el CSV podía tener comas y se rompían los campos y termina haciendo un extract de las tablas y subiendo a un SQL chiquitito. Estaba tratando de buscar los scripts, porque los scripts, eso lo que hacen es un select de una tabla de una base de datos y haciendo un insert en la otra y no pueden contando esas cosas. Bueno, independientemente de eso, ahí lo que mandó la gente de Process es, che, bueno, tapiola, estas son las tablas que está necesitando. El tema que la gente de Process empezó a mandar un poco la lógica de cómo ver que en teoría no debería interesarles a ustedes. Yo lo que necesito que ustedes me digan, che, ¿Qué tablas son las que necesitan? ¿No?

**Franco Ferrero**: Sí, yo le pasé. A ver, yo había mandado por grupo, que justamente creo que vi el mail ahí nos compartieron la cadena y creo que eran las mismas tablas las que teníamos. Eran dos tablas que habíamos pedido y había una tercera que venía, que por lo que había entendido que venía con un nombre específico de ustedes, que eso no sé si lo pudieron ver o no. Capaz ya con las otras dos, con la de ahí te busco el mail, pero con las otras yo por eso

**Vikingo**: yo estaba revisando un tema, porque digo, como el proceso es complicado, tengo que tener las tablas que son, porque si no estamos para. ¿Dónde está esto?

**Franco Ferrero**: Withitem era una tabla o LFW creo

**Vikingo**: que era para compartirme vos la pantallita esa, porque. Si yo abro el SQL por un lado, después se me complica por otro. Decime el nombre de una tabla, porque no eran muchas, ¿No?

**Franco Ferrero**: ¿Ven ahí mi mail?

**Vikingo**: No eran muchas tablas.

**Franco Ferrero**: No, no, no eran estas dos tablas. Eran dos tablas nomás cómo decís vos. Y LFW,

**Vikingo**: Dejame primero ver si están las tablas porque viste, o LFBW seguro nada más.

**Franco Ferrero**: Pero proceso

**Vikingo**: en una tabla Z, desarrollo propio de cada empresa. ¿Claro, ahí cuál es?

**Franco Ferrero**: Claro que ahí es. Deben tener un nombre ustedes. Propio.

**Vikingo**: Ella nos mandó un documento adjunto ahí. Yo he visto un PDF para que

**Franco Ferrero**: este.

**Lucio Rojas**: Sí,

**Franco Ferrero**: acá tenemos retenciones con WithItem en estas dos.

**Vikingo**: Pará, esa es otra WT. No, para se llama tipo de retención, por eso son varias tablas. Ves ahí Para tablas de retenciones de FI, W ítem y de retenciones withitem, Documento contable, proveedor, Tipo de retención. Ahí te está diciendo los campos.

**Franco Ferrero**: Claro, perfecto.

**Vikingo**: Después dice accediendo con número de SAP. Está bien, listo. Esto no está abajo. Listo, andamos para abajo. Número legal, el campo tanto más para abajo.

**Franco Ferrero**: No sé si importa este campo. No sé si importa.

**Vikingo**: Déjame ver si existen estas tablas, porque por ahí. Y no habla de las retenciones de las Z, No dice nada eso.

**Franco Ferrero**: Acá lo que dice era que las retenciones son las withitem. La LFW es el maestro complementario para identificar qué tipo de retención aplican a cada proveedor. Y nosotros habíamos dicho lo de los impuestos era lo que estaban por un

**Veronica Barrios**: lado, porque cuando yo le hago la consulta me dice solo tengo tabla de IVA, me falta percepciones y retenciones. Las percepciones son como pequeños impuestos que aparecen en las facturas. Esas son las percepciones y las retenciones es lo que se descuenta cuando se paga. Entonces lo que me.

**Franco Ferrero**: Perdón, ¿Será este campo que dice? ¿Nos trae los importes de los impuestos determinados en la factura y que se contabilizan?

**Veronica Barrios**: Debe ser. Sí, porque es así. Sí, porque eso está entre la factura. Sí no conozco este campo, ¿Qué es lo que dice? Pero sí

**Vikingo**: acá hay un tema blanco. Acordate que nosotros un momento cuando hablamos de esto dijimos no nos pregunten qué es cada campo, porque ustedes dijeron no, no, eso se encargamos nosotros porque ahí sí estamos fritos.

**Franco Ferrero**: No, no, no, sin duda, sin duda.

**Veronica Barrios**: Una factura no va a tener más allá del importe neto, digamos que es el P por Q, que es el valor en pesos o en dólares, más los impuestos. En los impuestos está el IVA, que el IVA me dice que lo tiene la tabla. Cuando le pregunto la inteligencia, Téramo me dice Cloud me dice lo que no tengo es la percepción entiendo, debe ser, no sé, esta tabla incluye todos los. Porque hay una parte que lo tiene el iva me dice OK, es la percepción.

**Vikingo**: Las dos tablas sí existen, pero déjame ver si tienen datos. Wititem tiene. ¿Sí tiene un montón de datos y la lfw debe tener un montón de

**Franco Ferrero**: datos A ver, perdón Cristian, querés fijarte si existe esta tabla keyword?

**Vikingo**: Pero no es un campo dice él. ¿No es una tabla decís vos?

**Franco Ferrero**: Me parece que es un campo, pero Claude ahí me dijo que era a la tabla com, La tabla se llama acá com, capaz tenés esa tabla también Y con las tres tablas estamos por lo que veo en este PDF Soporté.

**Vikingo**: Asterisk from. No existe esa tabla no existe. Con dicho campo accedemos a la comp. Esta tabla para que leo más en s es reemplazada por la tabla no pero no tala para salvo que sea no la jfh j no de la j SATA la k. O n b corta. No kont konx konx

**Franco Ferrero**: OK, y esta que dice prdc element

**Vikingo**: opqrc prc element prclment prc doble c no prcd prcd no prcd clust con hit items. Déjame buscar un cachito más abajo porque después tenés los nombres de las tablas empiezan con s sz son 200.000 tablas, yo tengo que buscar con el cursor cerca de 200.000 orden alfabético.

**Franco Ferrero**: Ahora estoy investigando. Si quieren lo que podemos ir haciendo total hasta tener la confirmación de esta última tabla podemos ir cargando las que ya sabemos que tienen lo que es las retenciones y eso.

**Vikingo**: A eso te iba a decir, yo lo que te la hago es te la cargo en la misma base de datos que tenía antes y te subo toda la base de datos, porque si tengo que hacer una base de datos porque cada vez que extraigo una tabla es un dolor de cabeza. Es decir, yo te había puesto una base de datos llamada teramont con todas las tablas que me habían puesto, yo lo que toca hacer es agregarte esta tabla en santa de esa base de

**Veronica Barrios**: datos,

**Franco Ferrero**: porque para vos eso no me lo puedes mandar como un backup de solo esas tablas.

**Vikingo**: No, tengo que armar para hacer un backup tengo que armar una base de datos. No hay un backup de una tabla.

**Lucio Rojas**: ¿No existe?

**Vikingo**: ¿Con el backup que yo te mandé eso lo restauraste en a un lado no?

**Franco Ferrero**: Claro, eso lo subimos directamente todo completo

**Vikingo**: Está bien Y ahora si yo te mando otro, puedes subirlo completo también reemplazando

**Franco Ferrero**: anterior, o sea lo podemos subir completo, pero eso lleva. Va a llevar un tiempo de la carga que lo que tarde cargar todos los datos, o sea me lo puedes enviar.

**Vikingo**: Todo completo. Va a tardar, decís vos. A ver, ahí veo.

**Franco Ferrero**: Si no, como vos las podés descargar esas tablas como CSV, pero acordate que

**Vikingo**: como CSV no andaba, ¿Te acordás?

**Franco Ferrero**: Sí, sí, sí.

**Vikingo**: Cuando lo hicimos el problema que pasa con el CSV, como son separados por coma y hay datos, texto, tienen coma dentro, se rompe todo. Si querés te hago una. A ver qué sale para fácil esto, Agarra esta de acá, yo les comparto, si quieren les muestro lo que tengo que hacer para que no me. Para que me crean que no hay soplayas al botella. Esto como decíamos en la antigüedad, que es rapidito soplarme ya no. Bueno, agarro la T CUR, le pongo de nombre, esto es. Entonces dijimos LFB, Perfecto. Ahora lfb está acá, LFW, vamos, todo lo que dice TCUR acá adentro, local, set, base de datos, salida, tenemos archivo, acá cambiamos el nombre, vamos a poner todo lo que es TQ.

**Franco Ferrero**: Listo.

**Vikingo**: Fue rapidita. Chiquita esta vez. Un tema que. Esta es una tabla de parametrización, por lo que veo.

**Franco Ferrero**: De parametrización, Sí, porque tiene.

**Vikingo**: ¿Cuántos registros tiene esto? Mira para abajo. ¿Cuánto tiene esta?

**Franco Ferrero**: Mil filas tenía.

**Vikingo**: Esta se llama, No sé cuánto, pero la podemos ver acá. A ver, select count, asterisco, from. 3 millones dice ahí, ¿No? 283. 931 de registros. Y la. Esta es esta y la otra que era la FLFB, LFBW. Esta tiene 39.584. Esa era rapidita. Esta me ha tardado un ganchito. Acá va por tres millones y pico. Listo, esto ya terminó. Son dos. Son dos archivos SB, Si a vos te van, te los paso.

**Franco Ferrero**: Sí. A ver, probemos.

**Vikingo**: Fíjate que tiene el header, en las primeras líneas tiene el header, después están los datos separados por coma. ¿Dónde crees que te lo mande? Estos dos.

**Franco Ferrero**: Mándamelo por mail si querés.

**Vikingo**: Déjame comprimirlo. Va a estar un poquito complicado. Comprimir.

**Franco Ferrero**: Entonces, Sori, para confirmar antes no lo

**Vikingo**: puedo pasar por método, tengo que pasar por WhatsApp si querés.

**Franco Ferrero**: Te lo paso por WhatsApp, yo lo bajo, No pasa nada.

**Vikingo**: ¿Dónde está el caso de soporte? ¿Cómo se llamaba el grupo? Hz

**Franco Ferrero**: Mago por ahí se sumó Lucio

**Vikingo**: Documentos y lo voy a mandar acá a ver si me deja. ¿He pasado archivos grandes por WhatsApp

**Franco Ferrero**: No, que acá me está mandando los archivos SB para cargar sol dos de las tablas que vimos, a ver qué nos pasaron Ahora nos estaría faltando una tabla que creo que es la de percepciones?

**Vikingo**: ¿Pero qué dijo la gente de proces con las percepciones? ¿Dijo algo? Esa parte me perdí No, yo no

**Veronica Barrios**: voy a hacer, le pedimos todo lo que pusieron en los medios. A ver, aguantame un segundo, no vi

**Vikingo**: que dijeran nada en contra, ¿Querés preguntarle Ver o percepciones? Si te dice eso ya sabe, vos

**Veronica Barrios**: le pusiste todo igual cómo vos cuando le pedimos, cuando le pedimos en el mail. Retenciones y percepciones, Retenciones y percepciones impositivas aplicadas y ellos respondieron

**Vikingo**: ahí tenés WhatsApp

**Veronica Barrios**: comento que respecto de las retenciones efectivamente serían las retenciones Retenciones dijo serían las tablas Wisitem o LFBW tal como lo mencionás, ellos en realidad hablaron acá puntualizaron de las retenciones

**Franco Ferrero**: y en el archivo dice que mandaron que las percepciones deberían estar en la tabla que se llama COM o RCD elements si la llegan a tener así o capaz tienen ustedes un esquema más un nombre de la tabla propia, es el tema, pero la

**Vikingo**: comp no existe, esta comp, o sea

**Veronica Barrios**: con el detalle que dio están las tablas de las retenciones, o sea ella lo que es retenciones dijo que son, esta acá lo comparto, que no son las mismas que están bajando me parece Width item o lfbw

**Vikingo**: bw tiene 23.000

**Veronica Barrios**: registros para 15 años ella dice ahí son, esas son las retenciones, por ahí

**Vikingo**: son los tipos de retenciones, Por ahí ahí te dice eso, son tipos de retenciones, son todas las retenciones.

**Veronica Barrios**: Bueno acá pone en este sentido te consulto si necesitan información adicional relacionada a compartidas abiertas o puede indicarnos puntualmente qué información requieren para poder ayudarnos. Bueno, acá les compartí el mail y acá nos compartieron lo que es, después los chicos nos.

**Vikingo**: Tipo de retenciones, porcentajes y todo, son tipos de edades, es un paramétrico este y la otra son las retenciones.

**Veronica Barrios**: Efectivamente.

**Vikingo**: Si vos te fijas, mira, para que

**Veronica Barrios**: no esté viendo la pantalla.

**Vikingo**: Acá está, acá está. Mira, yo te muestro, te comparto un ganchito acá. Ella está diciendo que en las tablas, en la tabla LFB, Tenés acá

**Lucio Rojas**: los

**Vikingo**: tipos de retención para descargar. Ah, para que tengo que parar porque estaba cosa. Ve que acá son los tipos de retenciones. Dice WIT, GGA, TANTO, un campo que se llama WIT, otro que se llama TANTO acá, bueno, y dice IG. Y en esta de ítems, acá están por cada empresa al año. Y acá está WIT, tal cosa para ir a buscar la retención correspondiente que en algún lado debe estar. ¿Cómo viene todo esto? A ver si me da bolilla, porque por ahí dos millones de registros va a tardar un cachito.

**Lucio Rojas**: Cristian, yo me meto un segundo para ver cuando determino las tablas las pasamos la otra vez yo haciendo un poco memoria, me habías pasado los SBs, pero habían roto porque tenían campos de texto libre donde había comas y lo que le decía Franco, si eso pasa de vuelta ahora. SB, lo que voy a hecho era el backup. Me habías creado un backup nuevo solamente

**Vikingo**: te tengo que crear todo un backup nuevo. Si, tengo que hacer mínimo me dijo no, porque ya lo cargamos todo ese backup.

**Lucio Rojas**: No puedes tablas no, no hay backup

**Vikingo**: de tablas en esa escuela.

**Lucio Rojas**: No. Y el que me había pasado que era de 40 y pico de tablas,

**Vikingo**: pero yo lo genero de un solo sal, te tengo que generar el mismo más estas tablas. Y él me dijo no, no puede generarme para cargarlo todo tenés que generarme de dos.

**Lucio Rojas**: Bueno, hagamos así.

**Vikingo**: Fíjate, fíjate si el CSV, porque ustedes se dieron cuenta rápido si el CSV caminaba o no. Caminaba o no.

**Lucio Rojas**: Sí, al token por los campos de esto libre.

**Franco Ferrero**: Sí, yo igual lo cargué a ver qué onda.

**Lucio Rojas**: Ese hay que ponerle.

**Vikingo**: Estos son archivos muy de. Salvo que en el WIT, acá en esta parte me están viendo, ¿No?

**Lucio Rojas**: Sí.

**Vikingo**: Salvo que acá una coma en algún lado y ahí te rompa, ¿Entendés? Bueno, todos importes de anuncios,

**Lucio Rojas**: si querés pasame el CCB, pasame el CSV y si no llega a romper, hacemos el backup. Hacemos el backup de las 47 más estas dos.

**Vikingo**: Sí,

**Lucio Rojas**: eso debe ser bastante jodido, pero vamos primero con el CCB. De cualquier cosa te mandamos para grupo,

**Vikingo**: aunque sea LFWT, el WIDM es el que no me. Es el más largo y es el que puede. Tranquilo. Bueno, dale, dale, dale.

**Franco Ferrero**: Y bueno, ahora si quieren hacemos una cadena de mails, nos conectamos también con los de Process para averiguar a ver bien qué tabla sería la de percepciones, la que nos estaría faltando para que

**Vikingo**: Vero pueda es la WIT Ítems, ahí están todas las retenciones y percepciones, te dicen.

**Lucio Rojas**: Tenemos duda de que haya alguna más, Perdón, yo entré tarde, si hay alguna más última, pasánosla.

**Vikingo**: Y no tengo ni idea yo agarramos el men que mandó Process y le

**Lucio Rojas**: dijo son estas tablas, dejamos esas tablas. Si podemos para hoy y probarlo, si no son, volvemos a hablar con la gente de.

**Veronica Barrios**: Lo que me está arrojando. Las cosas que le voy preguntando que me arrojando, las voy comparando con lo que está en los registros, a ver que está certera son o no, digamos, a ver, estoy validando el mismo registro, o sea le queda consulta, así que ahí nos vamos a dar cuenta al toque si hay algún número malo. Ya mismo la inteligencia cuando yo le pedí que haga toda esta, digamos, integridad, me decía hay una diferencia que no te voy a poder justificar, o sea, el IVA sí, pero el resto de los impuestos no tengo las tablas.

**Lucio Rojas**: ¿Y cómo venís con el uso? ¿Te sirve?

**Veronica Barrios**: Bien, bien. El que contaba Franco, hay cosas que, o sea, en general todo lo que trae, lo que trae está bien, hay cosas que las trae que no me responde a lo que digo, pero por un tema de que por ejemplo le faltan otras tablas. Por ejemplo, una de las pruebas que hicimos es el tema de que nos confirmen las diferencias que hay de precio entre la factura y la orden de compra. Ahí en ese caso, todos los casos que trajo estuvieron bien, pero a ver, esas diferencias estuvieron justificadas porque en el medio cayó una modificación de precio. Ahora, como no tiene las tablas de las estrategias de liberaciones. Claro, está bien lo que me informaba, o sea, yo decía bueno, fíjate con la estrategia de liberación ahí, fíjate si en el medio cayó una modificación de precio. Me decía, no tengo esa tabla. Así que bueno, lo que se hizo fue hacer una muestra de las más significativas y las que informó, informó algunas que las tengo que ver puntualmente con la gente de cuentas por pagar, pero el resto estarían justificadas. Por eso después lo que me está costando mucho, que lo tiré como tres veces creo que esta la última versión que me tiró, está bien. Así como vimos el tema de las diferencias de precio, también quisimos ver diferencias de cantidad. Es decir, cuando la cantidad recibida es diferente a la cantidad facturada. Bueno, ahí primero generó un archivo, estaba un poco incompleto, volví a generar otro también porque el tema es que, ¿Qué es lo que me pasaba? Si bien me pasaba la información, yo lo que le pedía era, bueno, cuando encontré diferencia, poneme el documento del W del módulo materiales, el documento W de materiales, del módulo fi lo mismo, la factura del módulo materiales y del módulo fi, las diferencias, las posiciones de la orden de compra, qué factura es. Entonces claro, a medida que yo al principio capaz se lo hacía, le preguntaba, me decía que lo tenía y me lo devolvía. Cuando le faltaba la mitad de la información, entonces se la volvía a preguntar. Cuando le volví a preguntar para que me cargue los datos que le faltan, porque en muchos casos yo fui como tirando, preguntándole, preguntándole, me fue dando reporte. Después en un momento me puse a ver a fondo que era todo lo que me había pasado. Entonces a lo mejor había algunos que sobre los que yo quería volver a preguntar, que ya los había borrado.

**Lucio Rojas**: ¿Por qué?

**Veronica Barrios**: Porque a medida que va generando, uno te dice, bueno, tengo todos estos, tengo esta memoria, pisame, o sea, cuál te

**Lucio Rojas**: descarto para generarte este nuevo, anotate el concepto, ya puedo empezar a interactuar con eso que es estable a gol.

**Veronica Barrios**: ¿Qué sería eso?

**Lucio Rojas**: Cuando vos le pedís un cruce de información que lo deja estandarizado. Entonces una vez que logra, dice bueno, yo quiero, vos me habías dicho que querías, no acuerdo ejemplo puntual, pero pone tienes un concepto, ese concepto quería una columna de acá, otra de allá, otra de allá, otra de allá. Lo que hace es armar la tabla con todos los conceptos y la deja fija.

**Veronica Barrios**: OK, OK. ¿Y eso Dónde se graba? ¿Dónde lo grabas eso?

**Lucio Rojas**: Lo grabante lo deja guardado en nuestra infraestructura y ya genera la tabla. Pero vos nada más le tenés que pedir a clock, creamos una tabla allá con esto, cada vez que vas a ver eso, lo va a buscar, ya está fijo. En el caso de que vos estés conectada ya directamente al SAP, eso se actualiza solo todos los días.

**Veronica Barrios**: OK, perfecto, bien. Esa no la sabía. Bueno, bien esta, la de diferencia cantidad, es una de las más complejas. ¿Por qué? Porque por un lado entonces yo, ¿Qué me pasa? Al principio yo le pedía de todo, después nosotros tenemos una, nosotros compramos diferentes, pero entre las cosas que compramos, compramos algo que se conoce como el nombre de fardos de cartón, cartulina, eso tiene humedad, entonces eso va con descuento. Cuando le pedía eso, le pedía todo junto, era una ensalada de documentos, agarré, empecé a decirle, bueno, haceme todos estos, pero los materiales de fardo, los que vos veas con este mpafopo, dejalo afuera. Y eso se lo pregunté, me lo hizo aparte, bueno, me generó la tabla ayer, tardó, tuve que decir todo esto que les dije de la cantidad del W, la cantidad de la factura que considere también, si hubo notas de débito, si hubo notas de crédito, porque las diferencias de humedad se descuentan con notas de débito y crédito. También si hay compensaciones entre posiciones, a veces me las informaba y después se compensaba. Entonces ahí es como que bueno, otra vez, son cosas que yo me fui dando cuenta también que cuando me lo generaba, capaz le volví a pedir lo mismo por la falta de información, le decía, bueno, ya que estás también fíjate si en la misma posición o la misma posición o la misma orden de compra se compensan las cantidades. Entonces bueno, entre el ida y vuelta, esas son las que más trabajo me dieron para que me genere un producto, que hoy por ejemplo hice como tres versiones, o sea, hice una versión, dos versiones, a la tercera las hice separadas. Ayer me generó la de fardos, que esa es la más como compleja de ver, digamos, por lo mismo a nosotros nos cuesta en el sistema verlo porque no es muy prolijo el pase de información. Y ahora me generó la tabla de todas las otras órdenes de compra, que es la que estaba viendo ahora. Después bueno, le pedí el tema de que me pase también le subí un. Estuve trabajando bastante. Después en otra, lo que hice es, le bajé el reporte de facturas apócrifas de AFIP y le dije, bueno, todas estas facturas, todos estos proveedores tienen actividad apócrifa o facturas apóficas en este periodo, Por favor, fíjate si nosotros tenemos registrado de estos proveedores a partir de este periodo facturas, efectivamente lo analizó, me generó un producto que efectivamente hay facturas consideradas apócrifas por afecto, que ver un poquito más con impuestos qué pasaron con esas facturas, digamos, pero en ese sentido laburo bien. El tema de la duplicidad de documentos también lo tuve que tirar algunas veces, como dos veces, porque digamos, o sea, yo le fui dando en algunos casos hacía el PROM, pero en otros casos lo hacía a mi manera y nada, me traía información, capaz le faltaba información como para, por ejemplo el tema de la factura duplicada, yo le decía fíjate que sea por proveedor y número de factura. Cuando me generó todo el reporte me di cuenta que muchos proveedores tienen notas de débito, notas de crédito, factura con la misma numeración, entonces fue otra vez a generarle, decirle bueno, pero fíjate también el tipo de documento, ahí en el tipo de documento hubo algunos que los calificó mal como facturas, pero en realidad notas de débito, crédito, pero líneas generales me generó un producto que lo pude validar y está bien, salvo uno que me duplicó el documento, después el resto de las líneas lo dio bien y no detecté facturas duplicadas ni notas de crédito duplicada. ¿Qué más? Bueno, ayer estaba viendo el tema de la prueba de integridad, esto que para esto sí necesito porque es una de las más importantes, que es partir de la orden de compra, pasar por toda la cantidad, el pedido con la factura con impuestos y ver si llego a ser todo el cruce.

**Franco Ferrero**: Ahí está, perdón, ahí cargué las tablas, ya cargaron, o sea que la pudimos cargar bien, no dio error, las pudimos cargar bien, así que estaría bueno probar,

**Lucio Rojas**: hay que auditarlo con Cloud, hay que meter a Claud a mirar esa tabla y fijarse que esté óptimo. Vero, gracias por todo lo que nos contás.

**Veronica Barrios**: Ahora este de las cantidades lo voy a terminar de ver, esta es la tercera. Si se me complica probablemente lo mismo que esta integridad, que son las más, como más pesadas, les pregunto a lo mejor porque estoy a lo mejor uno genera en el ida y vuelta, te vas dando cuenta la falla que tenés o la información, la falla que tenés vos cuando le pedís, la volvés a pedir. Estaría bueno como esa es una de las más pesadas, o sea, la verdad que la última que me generó bastante bien. Pero claro, a veces pasa que una posición, un remito tiene 20 líneas y en realidad la monografía es una línea. Entonces ahí tenés que empezar a. Ahí ya no sé, ahí me parece que es un laburo más el análisis de datos, de decir bueno, me pasó todo esto, tengo todo esto. Está bien ahí.

**Lucio Rojas**: Yo te propongo si querés, primero verifiquemos que las tablas estén bien y la semana que viene si querés.

**Veronica Barrios**: Dale, me parece perfecto.

**Lucio Rojas**: Una hora, una hora y media.

**Veronica Barrios**: Dale. Y te voy mostrando lo que traje.

**Lucio Rojas**: Da una educación sobre la herramienta, cómo crear una tabla, obviamente nada más, con el objetivo de que vos la puedas usar.

**Vikingo**: Dale.

**Veronica Barrios**: Podría ser, no sé, el lunes a la tarde lo pueden.

**Lucio Rojas**: Sí, déjame revisar.

**Veronica Barrios**: Para. No, dale, yo también así aprovecho a acumular y si lo vemos.

**Lucio Rojas**: Dale, genial, buenísimo. Así ya vamos.

**Veronica Barrios**: Dale. Diez puntos. Pregunta, ¿Esto ya está subido? ¿Lo van a probar? Y me avisan por chat cuando puedo hacer la prueba.

**Franco Ferrero**: Más que nada chequeo que esté todo bien. Igualmente también, mira, también como parte de la prueba, si vos también ya estuviste haciendo parte de este análisis que te decía, che, falta la retención, decile, che, ahora cargamos estas tablas nuevas donde tenemos las retenciones y las percepciones, ayúdame a hacer este análisis de vuelta, el que ya hicimos con estos datos cargados.

**Veronica Barrios**: Ah, bueno, eso lo puedo hacer, capaz lo hago mañana. Mañana le puedo. Ya quieren que lo haga ahora.

**Franco Ferrero**: Yo ahora lo veo bien y cualquier cosa igual te avisado.

**Veronica Barrios**: Dale, Dale, dale.

**Lucio Rojas**: Gracias, Cristian.

**Veronica Barrios**: 10 puntos. Bueno, gracias a todos. Gracias.
