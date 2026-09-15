# Hablemos !  Lucio  (Veronica Daiana Barrios)

**Fecha:** 2026-09-09T13:00:25.656+00:00  
**Duracion:** ~61 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Franco Ferrero <franco.ferrero@teramot.com>, Veronica Daiana Barrios <vdbarrios@gmail.com>  
**Externos:** vdbarrios@gmail.com  
**Apollo ID:** 6aa166bd227ff7001035839d

---

**Veronica Daiana Barrios**: ¿Cómo va? Todo bien con algunas consultas que me anoté para mostrarles y para ver con ustedes.

**Franco Ferrero**: Bueno, bien, a ver, ahora se va a sumar Lucio, ir contándome, a ver,

**Veronica Daiana Barrios**: cómo te voy contando. Bueno, traté de hacer esa famosa, a ver. Sí, pero ahí justo yo traté, a ver, me generó un producto, viste, el PROM, o sea, después que vimos lo de las tablas y me dijeron, pero pro, ahora yo ese mismo PROM, digamos, lo volví a cargar y me trajo un producto que a lo mejor no es lo que yo, digamos, qué me pasa con lo que me trae, que es lo que yo, digamos, me reservé para esta reunión, hace que me cueste, en algunos casos me trae cosas que me es fácil la revisión y la pude validar y mucha información me la dio y me la dio bien, y me sirve como hallazgo de auditoría. Algún que otro caso marqué, como que me lo marca como un caso que podría ser de auditoría, y cuando yo lo veo, en realidad me sale otro dato. Eso me los marqué, fueron casos, a ver, son de las consultas, necesitas consultas que fui haciendo en relación al proceso que estoy viendo de pago, proveedores, pero lo que tiene que ver con, digamos, estas pruebas que más que nada que hacen a la integridad, que son las de mayor alcance, y acá sí es donde realmente necesitamos una inteligencia, porque yo tengo que construir esa prueba, me va a llevar un montón de tiempo, ahí le escribo el prompt con todos los datos que les mostré el otro día, o sea, como que me lo acepta la inteligencia, pero lo que me devuelve me hace muy difícil el análisis, es decir, no llego a tener, o sea, la apertura de la información no es suficiente como para que a mí me permita, digamos, llegar a comprobar eso que me está informando. Entonces es ahí donde se me complica, dónde lo noté más, o sea, cuando la pregunta sencilla, por ejemplo, suponete, quiero que me tires todas las facturas cuya fecha de contabilización sea anterior a la fecha del W de la recepción. Ese, por ejemplo, me trajo bastante información, en algunos casos me pasó, me formó una, porque yo le pedí que me muestre los días de diferencia, no sé, ponele, de 80 casos que me trajo, ponele, 70 estaban bien y 60 me trajo un número que nada que ver, que no sé dónde lo sacó, entonces igual me los marqué, esos casitos. Después, por ejemplo, me pasó, hice otra prueba donde me tenía que informar, era el tema de los documentos duplicados, ahí lo pudo abordar bien, lo único que hubo una confusión con el tema de los tipos de documentos, entonces capaz había algunos proveedores que tienen la misma numeración con las notas de crédito, las de débito y las facturas, entonces en algunos casos tomó como que una nota de crédito y una factura del mismo número, un mismo documento y capaz no lo era, pero en general informó bien cuando la pregunta era sencilla, el producto que traía me servía. Ahora, cuando le empecé a preguntar esto de la prueba de integridad, o otras dos consultas más que me anoté, que es por ejemplo que me diga todos los casos donde hay diferencia de cantidad entre el W y la factura, o por ejemplo lo que hice fue, esa es otra consulta que hice esta semana, que lo que hice fue, viste que nosotros al principio, la auditoría te dijimos, vamos a probar, queremos que nos informe todos los anticipos que no están compensados, es decir, cuando se desembolsó un anticipo y no se aplicó, que ahí se me complicó porque me traía información en realidad, o sea, como no está, como acá no está bien, no está prolijamente contabilizado los anticipos, dije a lo mejor como nosotros tenemos contabilizados dificulta la análisis. Entonces lo que hice, bueno, agarré un rango de órdenes de compra del 25 y 26 que sé que tienen anticipos, entonces esas órdenes de compra, le dije, de estas órdenes de compra fui bien clara, le quiero que te fijes primero si está cerrada, si tiene una factura de compra, si se dio, contabilizó la factura de compra, si la compensación se contempló la factura de anticipo, o sea se lo di bien como customizado, bien limitado, bueno, ahí lo que me devolvió, me devolvió un detalle de información que me complica el análisis, es decir, no me resulta ágil a la hora de salir a buscarlo, entonces como que me separé estos casos que son como los que de repente cruzan mayor información y ahí es donde a lo mejor soy yo la que estoy generando mal, por eso ustedes me van a decir, no, tenes que preguntarlo así, tenes que manejarlo de esta manera, tenés que hacer lo otro, pero bueno, digamos, son las pruebas como donde hay mayor laburo, se complica un poco más el tema de lo que trae y son las pruebas, digamos que en verdad, para nuestro entender, de lo que es un proceso de cuentas por pagar, son pruebas significativas, porque puede haber pagos que se hayan hecho que no se hayan compensado, porque puede haber que se haya cargado una factura que dice que entregó 8 y en realidad entregó 6 porque se está pagando por encima de lo que se recibió, o de repente que no se haya respetado todo el circuito de pago, es decir, ¿No es cierto? Entonces, bueno, yo si quieren les muestro cada uno de los casos y ustedes ahí me van diciendo, ¿Les parece?

**Lucio Rojas**: Si querés. ¿Cómo andás? ¿Todo bien?

**Veronica Daiana Barrios**: Bien, todo bien. Bien,

**Lucio Rojas**: yo quiero organizar un poco la reunión porque a mí también me tiene que servir para tomarme nota de algunas cosas. Vamos a hacer una parte cortita de 5 minutos. Yo necesito que me expliques bien concreto caso de uso, de uso me llamo a qué estás haciendo, ¿Cuál es el alcance, sobre qué lo estás haciendo? Y cómo decías antes.

**Veronica Daiana Barrios**: Perfecto, dale, dale, dale.

**Lucio Rojas**: Después de eso vamos a agarrar una de las preguntas que a vos no te respondió y trabajarla toda juntos y a partir de ahí te vamos a explicar la herramienta.

**Veronica Daiana Barrios**: Bueno, 10 puntos. Bueno, si querés vemos esta, la que más me interesa y la más ambiciosa para mí por lo menos, esta la de famosa integridad, que ya que estuvimos viendo las retenciones, es esa. Si quieren vemos. No sé les parece, Beresa, agarramos la

**Lucio Rojas**: que vos quieras, pero antes te pido que me digas. ¿Esto es una auditoría de cuenta?

**Veronica Daiana Barrios**: Esto es una auditoría del ciclo cuentas por pagar.

**Lucio Rojas**: Bien, esto lo hacen una vez al año esto.

**Veronica Daiana Barrios**: Claro, es así, o sea, esto un poco para ponerte en autos, ¿Cómo funciona acá el proceso, el circuito, la función de auditoría? Auditoría todos los años diseña un plan de auditoría, que es básicamente elegir los procesos que se van a auditar. Hay diferentes factores que intervienen en esa definición, la operación de la organización, el riesgo que tiene en sí mismo el proceso, las debilidades de control que se hayan encontrado en distintos procesos, en auditorías anteriores, alguna denuncia puntual que venga desde un gerente, un director, o una línea de denuncia, o sea, son distintos factores que lo que uno hace es decir, bueno, este año se van a revisar estos procesos, esos procesos, el alcance, qué procesos son, los propone Auditoría y los aprueba el directorio, particularmente Cuentas por pagar. Es un proceso que aunque funcionara bien y no hubiera ningún tipo de denuncia y estaría todo bien, es un proceso que cada tres años es obligatorio verlo. ¿Como así? Por ejemplo, te diría que compras se ve todos los años, porque es uno de los procesos en cualquier organización más riesgosos. Normalmente cuentas por pagar cada tres años. Se revisa por lo menos con el escenario que tenemos en esta organización, la última auditoría que se hizo fue en el 2022 y ahora hacemos en el 2026, volvimos a hacer el mismo ciclo.

**Lucio Rojas**: La base es las tablas de SAP.

**Veronica Daiana Barrios**: Exactamente. Esta auditoría tiene una parte, digamos, a ver, el grupo HZ tiene una gerencia corporativa, Share Service le dicen, que lo que hace es nuclear todo el laburo administrativo de todas las unidades de negocio que tiene. El grupo HZ tiene diferentes unidades, es un grupo que tiene diferentes unidades, tiene una unidad que se dedica a la fabricación de cartulinas, una unidad que se dedica a la fabricación de envases flexibles de polietileno, una unidad que envases, digamos, envases como estos, así lo ven esto, o sea, esto nosotros se labura con los monstruos del mercado, Unilever, Mondelez, digamos, por lo menos los clientes que hoy tenemos, se diseña este packaging, suponete que Mondelés venda este paquete de alfajor de arroz, y una vez que se diseña, el laburo es con el comercial más el de marketing de ellos, se hace una tirada industrial de tantas unidades para la producción que ellos tienen, que obviamente la producción que ellos tienen está alimentado su forca en función de la demanda que tiene el mercado, como para ponerlos en auto. Eso es lo que es la unidad de envases flexible de polietileno. Hay distintos productos que se hacen. Después tenemos también la unidad de envases de cartulina, que es lo mismo pero de cartón. Caso por ejemplo la caja de arroz de Arroz Gallo, ese es uno de nuestros productos, así hay de vinos, de celulares. Después tiene la unidad agropecuaria que se dedica a la explotación de cerdos y a la explotación forestal particularmente las unidades de agro no están montadas en SAP y esas las estamos viendo en esta auditoría, pero se ven aparte. Las que sí hicimos hincapié que están en SAP son las unidades industriales, esta que les acabo de decir,

**Lucio Rojas**: la amplitud de la carretera, o sea pasamos de

**Veronica Daiana Barrios**: cartón, es lo más lindo. Es lo más lindo o sea, por lo menos a mí que no me aburro, o sea, por ejemplo, no sé, ahora estoy viendo cuenta por pagar y capaz el mes que viene voy a ir a ver los cerdo, una cosa así. Es así, está bueno, pero ahora lo

**Lucio Rojas**: que hicimos fue hacer un download de las cuentas de SAP.

**Veronica Daiana Barrios**: Claro, de SAP, de la que tiene que ver con la parte industrial, es decir, si bien en la auditoría entra agro, agro, yo lo voy a ver por los sistemas que tiene, no hay tabla, no hay nada, me puedo llegar a servir el cloud, es decir, para subir las tablas y que me haga análisis, pero yo acá estoy Teramon lo estamos usando con las unidades industriales.

**Lucio Rojas**: Igualmente, si le sirve el comentario, si es tema y tablas. Y las tablas si las puede hacer lo mismo que acá.

**Veronica Daiana Barrios**: Bueno, por ahora, viste la prueba Olsen definió que sea solo SAP. Sí ellos usan Finnegan, no sé si lo conocen, es bastante más, para mí es como mucho más limitado, porque nos ha pasado, no sé, esto dato de color, ¿No? En las auditorías han surgido limitaciones del sistema y cuando las queremos como parametrizar a nuestra medida, SAM nos los permite, puede hacer un desarrollo. Finnegan es como que te limita en esto, es así, lo tomás o lo dejás. Entonces bueno. Pero bueno, en ese momento se eligió Finnegan, porque Finnegan tiene, se supone, todo un sistema de gestión que hace a las empresas agropecuarias que les sirve mucho, tal vez más que SAP. Entonces bueno, por el momento

**Lucio Rojas**: nos agarramos auditoría de cuentas por cagar.

**Veronica Daiana Barrios**: Exactamente.

**Lucio Rojas**: Bajamos las tablas de SAP y ahora vos estás cruzando.

**Veronica Daiana Barrios**: Y ahora lo que. ¿Claro, yo qué es lo que

**Lucio Rojas**: te respondes? Preguntas.

**Veronica Daiana Barrios**: Claro, yo lo que. ¿Cómo es? Bueno, definimos la auditoría de cuentas por pagar de las edades industriales. Este proceso está administrado por esta gerencia corporativa que se dedica, ni más ni menos a registrar todas las facturas de las unidades industriales y a generar el pago. ¿Entonces yo qué hago? Defino el alcance de ese proceso y en función de ese alcance empiezo con el conocimiento que hay y la historia que hay de ese proceso. Se analizan los riesgos que tiene, y en función de los riesgos que tiene, ahí definimos las preguntas que le hacemos a Theon para que me salga a validar. Por ejemplo, una de las preguntas que hice ¿Qué facturas fueron pagadas con una fecha de pago diferente a la que está acordado en el maestro proveedores, porque para mí eso es un riesgo? ¿Por qué? Porque acá se carga la factura y nunca se chequea el sistema. Por decirlo, por explicarles, el sistema no tiene un control de está pagando por encima del. No sé, yo acordé con un proveedor 90 días y usted está pagando a los 30 días. Yo sé que no hay una alerta. Entonces la gente de cuentas por pagar es un circuito, es un circuito bastante mecánico, bastante manual, no muy repetitivo, se pasan las facturas y no se controla eso. Entonces ahí lo que yo estoy haciendo es, bueno, a ver, tirame en el periodo. Lo que estoy haciendo ahora, si bien subimos las tablas del 2022 al 2026, al principio yo me llevé y empecé a preguntar todo el periodo, vi que tardaba, entonces lo que empecé fue como a achicar el rango, dependiendo. Hay algunas preguntas que sí las hice en forma extensiva, por ejemplo, le hice una consulta de facturas apócrifas, si había proveedores con una nómina que le subí a Cloud, le por favor chequeá si en este periodo se operó con estos proveedores. Me lo respondió, fue una pregunta bien, digamos, validarla, pero me dio un buen producto Cloud esto. Lo mismo de las condiciones de pago también. Pero bueno, ahora también, ¿Qué pasa? No es solamente ver las preguntas que yo le pregunto en función a los riesgos que conozco, sino también necesito que, como toda prueba de auditoría, necesito que me valide el proceso. Entonces, otra de las preguntas que les hice está quiero que me hagas una prueba de integridad, que es la que vamos a ver ahora, de enero 2026 a junio 2026, donde lo que quiero que hagas es que te fijes que el precio, el valor de las órdenes de pago, sea igual al valor de la factura total menos las retenciones, y que el valor de la factura sea igual al P por Q definido en la recepción más los impuestos. Y que el P por Q es como que la hice en cascada, o sea, que el P por Q que tiene la recepción sea igual a la cantidad y el precio que está definido la orden de pago de la orden de compra. Entonces, toda la integridad quiero que yo me haga y que me diga, le dije, y cuando valides eso, decime todas las que tienen diferencia, ya sea desde entre la orden de pago y el valor total de la factura menos las retenciones, o entre la factura y la recepción, o entre la recepción y la orden de compra, ¿Entendés?

**Lucio Rojas**: Si estuviésemos hablando hace tres meses, cuando. Si fuese la misma enunciado, ¿Cómo lo hubiese resuelto?

**Veronica Daiana Barrios**: ¿Cómo lo hubiese resuelto? Bueno, se hace una muestra. Lo bueno de esto es que lo que más nos interesó a nosotros es que va a agarrar todo, si yo lo tengo que hacer por mi cuenta, se hace una muestra a criterio. A criterio, normalmente se analizan los. Se tiene un mayor de proveedores del periodo, uno analiza la mayor cantidad de proveedores, los que mayor desembolso haya y se hace una muestra, ¿No? Suponete, yo lo llegué a armar porque antes que ustedes entiendan, esta auditoría la había arrancado, después la interrumpimos, después retomamos, había hecho una muestra en una de las unidades de 60 u 80, no 60. 60 órdenes de compra que se trajo todo, es decir, se empieza a bajar toda la orden de compra, se baja después todas las recepciones del material, después se bajan todas las facturas que hacen a esas órdenes de compra, y después se bajan todas las órdenes de pago que cancelaron las facturas con esas órdenes de compra. Entonces después lo que se hace es en un Excel, laburo de hormiga, uno a uno empezará hacer la trazabilidad, o sea, son kilómetros de Excel, digamos que te lleva un montón de tiempo construirlo. Esa es una prueba que fácil demora una semana tranquilamente y que en realidad es muy limitado al alcance, porque lo haces en 80, o sea, vas a elegir sí un muestreo muy claro, aleatorio, tal vez con criterio, como dice, bueno, se supone que el mayor riesgo está con los que tengo mayor desembolso, ahí donde puedo ver mayor riesgo, pero es muy limitado la cantidad de órdenes de pago que uno puede sacar, porque acá se paga todas las semanas.

**Lucio Rojas**: Yo agarro el maestro de proveedores que pone, lo tenés ahí en tu oficina, en una hoja que te bajaste, decir, bueno, voy a seleccionar 80 transacciones de cuentas por pagar que están vinculadas a estos proveedores y me las voy a bajar, me las voy a bajar. ¿Qué implica? ¿Con quién tenés que hablar? ¿Las bajas vos? ¿De dónde las bajas?

**Veronica Daiana Barrios**: Las bajo yo directamente en el caso del maestro de proveedores me voy a basar en las cuentas corrientes del módulo FI en la fbln es la de cuenta corriente de proveedores, o sea de ahí sale cuando digo mayor del proveedor, es decir, me bajo la posición abierta o la posición del saldo al 30 de junio, suponete que esta auditoría se se planeó de enero 2026 a junio 2026, entonces te bajas el mayor a esa fecha, ahí ves la significatividad y una vez que ves la significatividad lo que haces es bajarte toda la cuenta corriente de enero a junio, es decir, ya sea saldos, partidas abiertas, cerrada, todo, es decir todas las operaciones que hubo y ahí elijo las facturas, se van a elegir las órdenes de pago de mayor monto y esa orden de pago te va a llevar a la factura, entonces ahí ya me conformé la factura digamos, no cierto, o las cuentas de impuestos y después voy a la módulo materiales para ver los ingresos y después la parte de órdenes de compra de

**Lucio Rojas**: esos ingresos vos te metes a SAP y te bajas poner el filtro, vos ya te conoces todas las hace 4

**Veronica Daiana Barrios**: años y con SAP trabajo desde. ¿Porque yo antes de entrar acá trabajaba en otra empresa que tenía SAP que era Loma Negra y estaba ahí en el ahí en esa época para que en el 2009 ya, o sea más o menos 2008-2009 yo empecé a manejar SAP y o sea tuve después trabajando en un estudio grande, tuve algún otro cliente que tenía el otro, cómo se llama? Oracle, pero siempre estuve más en clientes con SAP, entonces me conozco un montón las transacciones de SAP, es como

**Franco Ferrero**: para

**Veronica Daiana Barrios**: mí es el mejor del mercado, pero bueno, qué sé yo, te pido que.

**Lucio Rojas**: Bueno, ya me queda claro entonces el caso de uso auditorías del ciclo de cuentas por pagar del año 2025-2026 usando SAP, esto antes vos lo hacías bajándote los reportes del sistema y ahora lo que estamos haciendo es descargar todo esto a Telamont y que vos con clon audites en vez de un muestreo. El universo.

**Veronica Daiana Barrios**: Exactamente, exactamente, es decir, la propuesta de 1.80

**Lucio Rojas**: auditoría que tuve.

**Veronica Daiana Barrios**: Que en la facultad no, bueno, yo cursé la UBA y auditoría no, tuve auditoría de contable, pero no de procesos, la vas aprendiendo día a día, así

**Lucio Rojas**: que bueno, bien auditoría de sistemas que me la da.

**Veronica Daiana Barrios**: Ah, claro.

**Lucio Rojas**: Que es algo parecido. ¿No? Digo que nosotros auditamos que el sistema, por ejemplo, represente el negocio.

**Veronica Daiana Barrios**: Claro. Bueno, muy bien.

**Lucio Rojas**: Que si yo estoy pagando un proveedor antes de plazo, me alerte eso el sistema.

**Veronica Daiana Barrios**: Claro, Bueno, es lo que vamos ahora. No, o sea, yo siento como que, digamos, yo empecé capaz con él, me acuerdo con el balance, el de no sé cuántas columnas, y ahora es como que si tuviera que volver a elegir, capaz me conviene mirar la formación de sistemas, porque no, ya no queda cerrada

**Lucio Rojas**: esta parte que era cortita. Esto para guardar mi caso de uso. Vamos a enseñar todo. Para eso quiero que hagas algo que creo que todavía no hiciste

**Veronica Daiana Barrios**: para acá. Esto era acá. Compartir. Compartimos, compartimos. Pantalla completar, ¿No? Sí, acá esto.

**Franco Ferrero**: ¿Ahora, mientras Vero te pregunto, a ver, a diferencia de ustedes tenían unas horas estimadas o no para el proceso de auditorías a pagar? Sí notas que hay ciertos, capaz procesos que se están acelerando, o sea, que hacerlo manualmente con esto.

**Veronica Daiana Barrios**: Mirá, muy buena pregunta. Te digo. Por ahora, digamos, venimos más o menos igual con el consumo de horas. ¿Pero qué es lo que noto? A ver, si vos me preguntás esto, no quiero decir que no me sirvió theramon. No, a ver, hay una realidad también. Primero, es la primera vez que se hace. Nosotros, yo hago una auditoría bajo esta modalidad, es decir, todas las auditorías siempre. Entonces es una forma distinta de trabajar. Eso es diferente. Después, otra cosa que también ocurre es, digamos, los productos que trae Tramon, a lo mejor, digamos, yo la información como se la pido y lo que me baja, si bien el sistema muestra una serie de casos, no me trae toda la información que capaz a mí me necesito para validar esa información. Entonces es como que si bien me trae son estos casos, ahora lo que hizo últimamente fue decirle, bueno, no sé, cuando le pedía comparación de factura con remito, le decía, tráeme el número de remito Saab, el número de remito de módulo material y el número de remito FI, para que me sea más fácil la búsqueda. Ahí es donde, a ver, ahí es donde noto, tengo un desafío nuevo de laburo que capaz no me estaría agilizando. Pero sí, lo que noto también es que, a ver, me trae casos de todo el semestre, digamos, yo tengo que hacer esas pruebas todo el semestre o los seis meses que estoy viendo, no podría hacerlo, digamos. Es como que si bien el tiempo más o menos lo mismo, teóricamente barre con todo. Entonces ahí es como que.

**Franco Ferrero**: Acostumbrándose al uso de nuevo y ya una vez que capaz tenés más traqueado lo que son los análisis que hace, capaz no tenés que ir revisando punto por punto.

**Veronica Daiana Barrios**: Exactamente, exactamente, exactamente.

**Lucio Rojas**: ¿Cuántas cosas tenía Ámbelo? ¿Trescientos y pico?

**Veronica Daiana Barrios**: No, nosotros teníamos, ya te digo, pará en el medio igual cayeron otras cosas. Un segundito, ya te digo, la teníamos por acá. Planificación.

**Lucio Rojas**: De auditoría, con horas

**Veronica Daiana Barrios**: acá están previstas y para acá no está.

**Franco Ferrero**: No, no,

**Veronica Daiana Barrios**: si no, para porque está esparcido.

**Lucio Rojas**: Si lo tenés en la mente igual.

**Veronica Daiana Barrios**: Si no habrán 200, ya te digo. Acá está 248. Ahí está, 248.

**Lucio Rojas**: Para un muestreo.

**Veronica Daiana Barrios**: Claro, exactamente, para un muestreo.

**Lucio Rojas**: Bueno, si quieren entrar a Theramo también

**Veronica Daiana Barrios**: mi pantalla, ven

**Lucio Rojas**: esto es Clot, no es Theramo. Bueno, desde Google,

**Veronica Daiana Barrios**: A ver acá. Ahí estamos.

**Franco Ferrero**: App Teramot. Com, busca si querés directamente en el buscador, ¿Verdad? App Theramo, Ya está logueada, entra el

**Veronica Daiana Barrios**: proyecto acá directamente, ¿Verdad?

**Franco Ferrero**: Y abro el proyecto al POC Auditoría. No sé si viste la posibilidad que tenés de hacer dashboards y eso.

**Veronica Daiana Barrios**: No sé. Si, no, lo que me pasaba era que cuando le pedía, digamos, siempre le decía una consulta, me lo preguntaba, ¿Querés que te pase un Excel con todos los casos o querés que te haga un dashboard? Entonces yo lo que hacía muchas veces, haceme las dos cosas. Primero me pasaba el Excel con todos los casos y después terminaba haciendo un informe con todos los casos, el análisis, digamos. Pero siempre desde Cloud, nunca.

**Lucio Rojas**: Ahí velo. Te explico. Nuestra herramienta, nuestra tecnología es una tecnología de ingeniería de datos. Nosotros dedicamos a entender sistemas con AI y a crear tablas nuevas a partir del sistema que ya existe, con lógica de negocio, sin un usuario técnico detrás. Entonces vos lo que estás haciendo G es que tenés a la mano una herramienta que ingeniería de datos, que te responde solicitudes de información de manera automática sin que vos tengas que estar cruzando tablas. Eso es como la base de lo que estamos haciendo ahora. Vos lo que haces es usar Cloud para esa herramienta, enfocarla en auditoría. Entonces lo que yo creo que vos tenés que lograr es a partir de todas las tablas que tenés cargadas, crearte las tablas nuevas que te respondan a tu necesidad de información y te la puedes bajar y después verla hacer dado hacer reportes.

**Veronica Daiana Barrios**: ¿OK?

**Lucio Rojas**: Te voy a explicar rápido cómo funciona. Si Vos ahí estás en fuente de datos, ¿Si? Nosotros acá es donde fuimos cargando todas las tablas. Ahí tenés el módulo Fi que está cargado, que tiene 26 tablas. Después tener la tabla de retenciones y percepciones, que son las dos que cargamos otro día y tenés tu que es

**Veronica Daiana Barrios**: la que cargamos ya, ¿Sí? Bien.

**Lucio Rojas**: Si vas a estudio de datos, que es el segundo acá, si querés subir una tabla nueva, después te enseñamos, no importa si abrís FI, ahí a la izquierda, elegí cualquiera de las tablas. ¿Alguna vez estés familiarizada?

**Veronica Daiana Barrios**: ¿Ninguna? ¿Hola, qué tal? No sé cuál, A ver, elijo cualquiera de las aristas

**Lucio Rojas**: ahí. Si querés cerrar, nosotros que estamos flotando ahí tenemos la crucecita. Crucecita qué te dice nosotros como Téramo te armamos una descripción exacta de qué es cada una de las tablas del módulo. ¿Descripción qué tiene esta tabla? Esta tabla tiene a modo de fila una transacción financiera única, incluyendo detalles sobre cuentas, montos, fechas relevantes, los datos que se han extraído y transformados de las tablas originales. Si vas a esquema, que es la segunda pestaña arriba,

**Veronica Daiana Barrios**: este. No, perdón,

**Lucio Rojas**: tiene una descripción columna por columna de esa tabla que te deja ver exactamente qué tiene cada tabla, ¿Sí? Y si vas a la tercera y bajas 1 poquito, Si me deja.

**Veronica Daiana Barrios**: ¿No, porque no me deja?

**Lucio Rojas**: ¿Para abajo, si quieres

**Veronica Daiana Barrios**: no me roleo para abajo, pero no baja con el cursor el mouse en la ruedita, no?

**Lucio Rojas**: Si puedes achicar un poco el zoom,

**Veronica Daiana Barrios**: entonces dale un segundito.

**Lucio Rojas**: Ahí puedes ver la tabla.

**Veronica Daiana Barrios**: ¿Sí? Ahí vamos. Ahí va. Ah, perfecto.

**Lucio Rojas**: Bien. Esto la idea es que vos nada más lo sepas, porque ahora se gestiona desde clock. ¿Y ahí si querés cerrar lo que dice tabla silver a la izquierda, tocaste la tabla hoy? ¿Viste que tocaste la tabla? No más acá fíjate que tenés tabla silver. Ahí dice tabla silver.

**Veronica Daiana Barrios**: Ajá, bien.

**Lucio Rojas**: ¿Qué son las tablas silver? Sí, son todas las tablas que nos cargaron a nosotros. Son subsistemas.

**Veronica Daiana Barrios**: Bien, bien.

**Lucio Rojas**: Y las tablas gold son las tablas nuevas que vos generaste a partir de hablar con CL. Estas tablas no existen en tu SAP. ¿Esta tabla las creaste vos?

**Veronica Daiana Barrios**: Sí, me dijiste algo la otra vez. Como predeterminar con tabla. Sí, tablas.

**Lucio Rojas**: Elegí alguna cualquiera.

**Veronica Daiana Barrios**: Esta. Vamos A ver esta.

**Lucio Rojas**: ¿Que tiene esta tabla? Acá tenemos una tabla, es un detalle de líneas de FC, NC y ND,

**Veronica Daiana Barrios**: que son facturas, notas de crédito y notas de débito, con precio distinto a

**Lucio Rojas**: la orden de compra entre 2024 y 2026, cuyo precio unitario difiere del precio de la orden de compra en más del 5%, incluyendo el número de documento contable de SAP fi serie 19, y de cada factura de crédito, nota de crédito, nota de débito. Las tablas que vos usaste para componer esta tabla nueva son esas cuatro. De ahí vos usas RBKP, RSG o KPO y BIPF. Entre esas cuatro está la información que vos le pediste. Clot para responderse. Eso generó esta tabla. Si vos abrís el origen, dice origen ahí.

**Veronica Daiana Barrios**: Ajá, bien ahí.

**Lucio Rojas**: Si querés devolver zoom, que yo veo poquito, un segundito. Sí, Ahí. Lee lo que dice cada una de las instrucciones.

**Veronica Daiana Barrios**: Instrucciones un Detalle de diferencia de precio entre orden de compra, factura, nota de débito y nota de crédito, agregando el número de factura SAP documento contable. Sería 19 para las facturas, notas de crédito y notas de débito. Después, segunda condición, el número de factura SAP documento contable FI, se obtiene, me dice la tabla BKPF filtrando iPad. Bueno, acá un código, qué sé yo, documentos, documento para verificar la factura, documento de verificación de factura, logística.

**Lucio Rojas**: Son todos los requerimientos funcionales que tiene la tabla nueva, o sea, son todas las cosas que vos le fuiste pidiendo a Claude, que Claude entendió voz y entendió el sistema y cruzó esa información. Y más abajo está la query de SQL, que si la expandir el botoncito. Bien, eso es como el código que genera. Y si vos vas a vista previa,

**Veronica Daiana Barrios**: a la derecha, vista previa, tenés la tabla.

**Lucio Rojas**: ¿Entonces, esta tabla que tiene? Tiene todas las líneas de FC, NC y ND, cuyo precio unitario difiere del precio de la orden de compra, más del 5%, incluyendo el número contable de SA. Cada columna es un detalle agregado de información. Así funciona. Te entiendo. Vos el sistema y genera las tablas con la información que le pedís y te lo responde. Esto cuando vos haces un pedido complejo, cuando haces un pedido simple, que es anda a ver que hay en esta tabla, no hace una tabla gol directamente a mirar la tabla silver, es como que va a mirar tu sistema y te responde que vos notas entre me fácil hacer una pregunta sencilla, se me complica. Con las complicadas podrás complicar. Requiere un poco más de trabajo.

**Veronica Daiana Barrios**: Claro, si, tal cual.

**Lucio Rojas**: Así que ahora vamos a. Y acá hay un detalle mucho muy importante, una vez que vos creas esta tabla, si estás conectada a tu sistema, esta tabla no se borra nunca jamás y se actualiza todos los días,

**Veronica Daiana Barrios**: todos

**Lucio Rojas**: los días vas a ver, o sea, pueden entrar el mes que viene y va a tener todas las. Todas las líneas cuyo peso unitario difiere del precio de la orden de compra de más del 5%. No tenés que volver a hacer nunca más. Una vez que lo haces ya queda y puedes configurar alertas incluso por ejemplo lo que puedo hacer en el caso anterior me gustó, interpreto que el pago de la cuenta se registra antes, que lo que decía el registro de cuando pagarlo me lo traiga esta tabla, entonces te lo hace una alerta, me la pagó antes. Entonces vos podés conectar esto, un dashboard, todas las cuentas que están pagando.

**Veronica Daiana Barrios**: Claro, claro.

**Lucio Rojas**: No solamente sirve para auditoría post mortem, sino sirve para auditoría en el momento.

**Veronica Daiana Barrios**: Claro. Lo que llamamos nosotros el módulo o modelo de auditoría continua que es ni más ni menos que esto, digamos, o sea, en controles claves de cada uno de los circuitos se crean como indicadores que son alertas. Exactamente. Es como que seguís viendo permanentemente esa actividad.

**Lucio Rojas**: Esto es envío contra el sistema.

**Veronica Daiana Barrios**: OK.

**Lucio Rojas**: ¿Así que qué vamos a hacer? Vamos a crear una de estas tablas que respondo a tu problema que te dolía. Para eso vámonos al plot de vuelta.

**Veronica Daiana Barrios**: ¿Te hago una pregunta que esto ahora que me hiciste acordar, porque cada vez que yo le hacía una pregunta? ¿Digamos, digamos, le hacía una consulta que tal vez implicaba esto, porque me preguntaba, bueno, si ya identifique, me respondía no, ya identifique todo lo que vos querés saber ahora para avanzar no tengo espacio, tengo que borrar alguna de estas tablas que creo que son estas eran las que había armado acá y me hacía borrar alguna, yo por ejemplo me acuerdo que esta era, no? Esta era, me hacía borrar, yo trataba de borrar, ponele, las que había tenido, me parecía que lo que me había generado, no le había terminado revisar, pero me parecía que era consistente lo que me había informado. No la borraba, o sea, las borraba y trataba de no borrar aquellas que sabía que eran las más complejas, que me las siga conservando porque podía volver la consulta. De hecho me pasó alguna en alguna de las consultas que le hice que borré y después tuve que volver a tirar y lo que hice fue como subirle el producto que me había hecho y le dije, bueno, esto fue lo que me hiciste vos una vez sobre esto, quiero que agregues esta información.

**Lucio Rojas**: Lo que pasa es que vos. Nosotros cobramos por licencia

**Veronica Daiana Barrios**: y eso limita la capacidad de las tablas éstas, digamos,

**Lucio Rojas**: sí estoy yendo con un programador, Nosotros cobramos por licencia y la licencia restringe la cantidad de tablas.

**Veronica Daiana Barrios**: OK, OK, OK. ¿Está bien o no?

**Lucio Rojas**: Una, dos. Si querés ir a Billing, fíjate, anda a administración.

**Veronica Daiana Barrios**: ¿Administración para dónde?

**Lucio Rojas**: A facturación, puedes ir y a ver los planes. Vos estás en un plan gratuito, incluye hasta cinco tablas Gold.

**Veronica Daiana Barrios**: Ah, OK, OK, bien, bien, está bien. No, solo para, si querés ir más

**Lucio Rojas**: abajo están los planes que te dejan hacer más, es decir, Royas, esto te deja hasta 20. Acabo de pedir que te lo. Que te lo suba mejor. Que es el fondo, el Enterprise. No le vamos a cobrar por eso, porque estamos en la prueba de concepto. Una vez termine la prueba se los cortamos y bueno, si ustedes.

**Veronica Daiana Barrios**: Claro, claro.

**Lucio Rojas**: No, está bien, le gusta, lo pueden seguir, pa.

**Veronica Daiana Barrios**: OK, bien.

**Lucio Rojas**: Ahora igual quiero ir a estudio de datos porque quiero hacer una cosa, quiero contar la cantidad de Gol que tenés. Más. ¿Tenés más de cinco? Cinco, seis, siete. Ocho. Ocho.

**Veronica Daiana Barrios**: No baja más.

**Lucio Rojas**: Eso es fal, ¿No? Sí, tenés ocho. Bueno, no importa, vamos a ir ya si querés, vamos a ir a Cloud y vamos a resolvernos un caso desde cero, así vemos cómo funciona. Causa un proyecto nuevo.

**Veronica Daiana Barrios**: Un proyecto nuevo.

**Lucio Rojas**: Lo primero que vamos a hacer es subir la inteligencia de Cloud Sonnet. Fíjate si tocas ahí dice. Son cinco.

**Veronica Daiana Barrios**: Sí.

**Lucio Rojas**: Ahí tenés distintos modelos. Los modelos más altos están más arriba, son los más inteligentes. Los que están más abajo son los menos inteligentes.

**Veronica Daiana Barrios**: Sí, sí.

**Lucio Rojas**: Más modelos abajo de todo. Podemos elegir para esto un Ocus 4.6, si querés elegir y pone toca de vuelta en esfuerzo elegí alto.

**Veronica Daiana Barrios**: Esto, me olvidé. Mira que te pregunté, podría haberle cambiado este y capaz tenía un producto mejor.

**Lucio Rojas**: Sí, te responde mucho mejor.

**Veronica Daiana Barrios**: Sí.

**Lucio Rojas**: Vamos a decirle conectate al Pyram, al Workspace o poné WS, así más fácil.

**Veronica Daiana Barrios**: Conéctate, cómo me dijiste. Conectate a W, me dijiste.

**Lucio Rojas**: A Téramot. Al WS. Dhz group. Y haceme una descripción en lenguaje de negocio.

**Veronica Daiana Barrios**: Una descripción en lenguaje de negocio. Así lo escribo.

**Lucio Rojas**: De negocio. Así no te habla. Tengo. Te habla un lenguaje porque vos entiendas.

**Veronica Daiana Barrios**: Sí, sí.

**Lucio Rojas**: ¿De qué tablas? Las tablas Silver.

**Veronica Daiana Barrios**: ¿Qué tablas Silver? Así.

**Lucio Rojas**: De tabla silver de las tablas silver. Ahí va bien. Y manda. Ahora va a usar el conector A T, que vos seguramente lo viste varias veces.

**Veronica Daiana Barrios**: Sí, sí, al principio lo pone dato, después ya me di cuenta, dejé de preguntar, pero era por qué.

**Lucio Rojas**: Ahí puedes abrir ese gris y tocas el. Puedes ver lo que va haciendo si tocas cada uno de esos tabs.

**Veronica Daiana Barrios**: Sí, esto siempre. Porque si le ponía un azul.

**Lucio Rojas**: Andate a personalizar

**Veronica Daiana Barrios**: izquierda.

**Franco Ferrero**: Acá personalizar creo ya lo tiene activado igual.

**Lucio Rojas**: Pero chiquillo. A conectores. Que el segundo tab abajo de personalizar, ya en la pantalla. Elegible. Baja un poquito esto. Se lo puso cambió.

**Franco Ferrero**: Toca los tres puntitos.

**Lucio Rojas**: No, no, esto ya tiene cuenta de. No puede hacerlo. Tiene cuenta de lo que te iba a hacer ya que no te pregunte más esas cosas.

**Veronica Daiana Barrios**: Ah, OK. No, no pasa nada. Igual yo se lo vengo. Es más, vuelvo acá a ver si volvió, porque me lo preguntaba igual me lo pregunto un par de veces y después ya me lo iba a preguntar y aún poniéndole. No me lo preguntes. Sí siempre viste.

**Lucio Rojas**: Ahora si querés pedir ganando tiempo, anda estudiando el prompt de lo que vos querés.

**Veronica Daiana Barrios**: Mira, era.

**Lucio Rojas**: ¿Lo tenés copiado en algún lado?

**Veronica Daiana Barrios**: Sí, en realidad, a ver. Si, este fue el que armé. Me parece un montón.

**Lucio Rojas**: Al final lo vamos a refinar entre nosotros. A ver.

**Veronica Daiana Barrios**: Copiar. ¿Lo copio aparte? No, todavía no, porque esto acá todavía está trabajando.

**Lucio Rojas**: Sí, lo copio. No, no, nunca toques Enter.

**Veronica Daiana Barrios**: No,

**Lucio Rojas**: arriba.

**Veronica Daiana Barrios**: A ver, para. Me lo copió bien. A ver si. No, porque eso es lo que me hacía el otro día. Para. Esto lo voy a.

**Lucio Rojas**: ¿Vos te acordás de lo que necesitas igual?

**Veronica Daiana Barrios**: Sí.

**Lucio Rojas**: Bueno, vamos a hacerlo de cero. OK. Decile qué es el objetivo general, lo más grande.

**Veronica Daiana Barrios**: El objetivo general es que, digamos, necesito que me haga. Yo lo llamo así, no sé si está bien definido, una prueba de integridad entre las órdenes de pago, las facturas, notas de débito, crédito de esa orden de pago, las recepciones o WE y las órdenes de compra que alimentan SWE considerando la cantidad y el precio.

**Lucio Rojas**: Bueno, escríbelo.

**Veronica Daiana Barrios**: Valides va con. ¿Creo que sí, con ese, no? Sí, Valí. Gracias, Valí, Necesito que valides. Necesito, necesito. No, no estoy viendo. De las recepciones, Entre los importes, nota de débito. Los importes y los importes.

**Lucio Rojas**: Antes de volver a esto, Sí, Necesito comprobar la integridad entre los importes de las órdenes de pagos, los importes de las facturas, notas de crédito y notas de débito conforme a las órdenes de pago. Los importes de recepciones.

**Veronica Daiana Barrios**: ¿Para que le voy a poner recepciones correspondientes a dicha factura? Sí, correspondientes, fichas, facturas. Y los importes de las órdenes de compra que dan origen a dichas recepciones. A dichas recepciones. Ahí está.

**Lucio Rojas**: Ponele abajo, sí pone punto, pone shift enter. Trabajo en un equipo de auditoría de puntas por cobrar, esa es mi especialización.

**Franco Ferrero**: ¿Por pagar, no?

**Veronica Daiana Barrios**: Sí, sí, sí, sí, entendí. Si, no, lo valida al revés. Muy bien, Sí, sí, trabaja un equipo de auditoría, cuentas por pagar.

**Franco Ferrero**: Para que entiendas también, un poco, Vero, es como que vos le estás dando contexto para también que entienda qué es lo que está haciendo y con qué fin. Más que nada así cambia a veces la forma en la que analiza lo que está haciendo.

**Veronica Daiana Barrios**: Bien.

**Lucio Rojas**: Cambia la forma en la que habla con vos.

**Veronica Daiana Barrios**: Bien.

**Lucio Rojas**: ¿Le hace shifter de vuelta? Sí, sí, haceme preguntas. Acá pone ask user questions.

**Veronica Daiana Barrios**: Ask con K, Sí, perdón, Ask user,

**Lucio Rojas**: entre paréntesis, en listitas,

**Veronica Daiana Barrios**: entre paréntesis esta afirmación,

**Lucio Rojas**: Ponele en listitas, si me entiende lo que quiero decir.

**Veronica Daiana Barrios**: Así, en listitas.

**Lucio Rojas**: Sí, en listitas. Después me van a entender que te estoy queriendo hacer en listitas para entender bien lo que necesito.

**Veronica Daiana Barrios**: Bien.

**Lucio Rojas**: Y salir el paréntesis y decime de qué tablas tenemos que mirar la información y qué tabla gol tenemos que construir. Bien.

**Veronica Daiana Barrios**: ¿Y decime?

**Lucio Rojas**: ¿Antes de mandar eso, vamos a abrir el artifact que te hizo? Fíjate que allá tienes como un expansor, Esa es una auditoría de las cuentas, de las tablas. Te dice vos en lo que cargaste tenés 29 tablas, tenés 7 de compras, 5 de proveedores, 4 de contabilidad, 3 de pagos, 2 clientes, 2 de logística, 3 de impuestos y 3 de confidencia. Y si vas bajando

**Veronica Daiana Barrios**: cada una de las tablas. Bien. Documentos, cabecera, fila correspondiente a asientos. Ah, está bien. Factura, nota de crédito, débito, compensación, contiene fecha de contabilización. OK. Está la madre para rastrear cualquier movimiento financiero. Relacionar. OK, perfecto. Partidas compensadas. OK, Bien. Con la cruz, ¿Verdad?

**Lucio Rojas**: Sí. Y mandémosle este pronto. Ahora te va a preguntar a vos. Confirmaciones que necesita para no inferir cosas.

**Veronica Daiana Barrios**: Bien.

**Lucio Rojas**: Si, no, infiel. Bien. Puedes desplegar y ver lo que va trabajando. Puedes abrir eso también.

**Veronica Daiana Barrios**: Siempre que haya flechita se puede. Perfecto. Entiende el objetivo. Recorrer la cadena completa. Claro, claro.

**Lucio Rojas**: Esas son las listitas que yo te decía, las ask user questions.

**Veronica Daiana Barrios**: OK. Todo. En realidad, a ver, capaz como. Me parece que lo acotaría al año, al último ejercicio cerrado.

**Lucio Rojas**: En realidad poner algo más. Algo más. Puedes poner lo que vos quieras.

**Veronica Daiana Barrios**: Vamos a ponerle acá. Enero de enero, 26, junio 2026. ¿Qué moneda querés? Uy, qué buena pregunta. Pasa que hay algunas que viste. La orden de compra está en dólares, pero después el pago está en pesos. Ambas monedas, local y documento.

**Lucio Rojas**: Puedes pedirle si quieres ambas.

**Veronica Daiana Barrios**: Incluir servicios. Estas son las peores hojas de entrada, además de recepciones. Sí, hay unas órdenes de compra que tienen hojas de recepción. Unas hojas de confirmación de recepción. Sí. Materiales y servicios. Sí. Largo.

**Lucio Rojas**: Todo. Esto ya tiene una estructura distinta. Como venías trabajando

**Veronica Daiana Barrios**: de lo que estuve interactuando hasta esto, ¿No? Si. No, algunas cosas me preguntaba, pero en realidad lo que me decía era. De esto, ¿No? Porque yo me acuerdo que cuando le subí al prompt, le decía el periodo que quisiera que mirara y no me habrá preguntado alguna vez.

**Lucio Rojas**: Está bueno no condicionarlo. Siempre voy al objetivo general, construyo el resto con él.

**Veronica Daiana Barrios**: Con las preguntas que te va haciendo. OK, Bien.

**Lucio Rojas**: Hola. Está tratando de resolverse. Puedes abrir si querés. Está tratando de resolverse todas las consultas que tiene. Mirando las tablas. Diseñando una estructura de reporte para materiales y servicios. Mapeando los pagos, los reportes de pago a partir de los invoices.

**Veronica Daiana Barrios**: Perfecto. Tengo todo lo que necesito para diseñar análisis. Déjame primero mapear la cadena de datos y ponerle estructura a la tra. Perfecto. Si, esto. Sí, esto me lo fue. Esto recuerdo que me lo. Estas afirmaciones me las iba tirando con las consultas que le hacía.

**Lucio Rojas**: Yo te decía, tengo todo lo que necesito y después no.

**Veronica Daiana Barrios**: Sí, sí, sí.

**Lucio Rojas**: Una vez que vos generes la tabla Go, que eso si no tenés tiempo, pueden terminarlo, yo no tengo otra reunión, puedes pedirle que te arme un dashboard con los descubrimientos que tiene directamente. Claro, puedes ponerlo 2, 1-1.

**Veronica Daiana Barrios**: Bien. Esto nunca me lo hizo. Perfecto. No, no, esto no. Ahí tiene la cadena completa de integridad, Tienen partidas de proveedores compensadas, donde el documento de compensación. Da detalle logístico de cada factura. ¿A qué se refiere con el detalle logístico? Sí,

**Lucio Rojas**: Ahí debe decir la tabla. Todo lo que tiene

**Veronica Daiana Barrios**: la famosa tabla Gol que le pedimos, es el dato que va a traer. OK, perfecto.

**Lucio Rojas**: Y esa es cada una de las filas, Una fila. La fila va a tener el código de sociedad, el nombre de la sociedad, el código del proveedor, la razón social, la fecha.

**Veronica Daiana Barrios**: Si, perfecto.

**Lucio Rojas**: Si querés, si querés ajustar algo, ajustamos. Si no, puedes decirle que la cree, así terminamos el proceso.

**Veronica Daiana Barrios**: Créala.

**Lucio Rojas**: Acá donde colígene, por ejemplo, la parte interna de Telamo, de los gráficos de usuario. Me llevo una semana, porque para que quede como yo quería, tenía que ir pidiendo un montón de modificaciones. Esto es súper maleable, vos podés ver el resultado, no me gusta, hay que cambiar esto porque. Y por yo necesitaba esto.

**Veronica Daiana Barrios**: Claro.

**Lucio Rojas**: Y va discutiendo, va discutiendo con. Tenemos que entender lo que estamos haciendo para discutírselo.

**Veronica Daiana Barrios**: Claro. Yo lo que hice fue que al principio me empecé a preguntarle muchas cosas y después lo que me fue generando lo fui viendo después porque quería ver en realidad, a ver, como toda inteligencia, cuando uno agarra a ver qué capacidad tiene, qué me puede responder, y no es que lo que automáticamente me generaba lo revisaba. Sí, miré alguno que otro, sobre todo las primeras preguntas que fueron las diferencias entre cantidad y precio, y después seguí avanzando con otras consultas y claro, capaz eso estaría bueno verlo en el momento que te genera el producto, ahí ya lo analizas y ya digo, yo hoy si lo tengo que hacer, es como que. De hecho lo que estoy haciendo ahora, cada vez que me genera algo, no lo dejo, o sea, si estoy analizando, me tira algo, estoy analizando otra cosa, bueno, termino con esto analizando y después retomo eso que me generó nuevo. Por eso también empecé al principio era todo metido en una conexión y después empecé a abrirlo por consulta.

**Lucio Rojas**: Yo me tengo que ir a otra reunión que no puedo. Quieren terminar acá la Gol, mostrarle cómo creó, mostrar el linaje y la Fer

**Franco Ferrero**: Sí, pero no pasa nada, termino esto un rato y después me sumo a la otra.

**Veronica Daiana Barrios**: Dale, genial. Si, aunque sea llegar a ver el producto donde. Bueno, lo descargo ahí donde me lo mostraron.

**Lucio Rojas**: ¿OK Bet, igualmente podemos agendar una próxima?

**Veronica Daiana Barrios**: Dale, sí, por supuesto. Sí, sí, sí, sí, sí, sí, dale, dale. Sí, sí, sí.

**Franco Ferrero**: Vamos a agendar otro horario esta semana si querés, o sea, esto más que

**Lucio Rojas**: nada para que vaya termin. Y si Fran, vos no tenés tiempo, Dulce, nos podemos conectar un rato, yo en una hora me puedo conectar de vuelta.

**Veronica Daiana Barrios**: Como quieran, como quieran, si quieren ir a sus reuniones y yo dejo esto, esperen que los vuelvo a poner que se me fue.

**Franco Ferrero**: ¿A las dos estás libre Vero?

**Veronica Daiana Barrios**: A las doce estoy libre, Cortamos ahora Yo dejo que esto lo siga tirando lo que baje, si quieren a las dos lo volvemos a ver, así cada uno van a sus reuniones aunque sean medio

**Franco Ferrero**: ya traje, hagamos así.

**Veronica Daiana Barrios**: Perfecto.

**Lucio Rojas**: Esto para que Claro, va a tardar uno o dos minutos más pero. Así que cualquier cosa puedes rapid. Bien, perfecto, perfecto, me hago el cambio.
