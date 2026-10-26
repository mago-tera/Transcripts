# Teramot calipso

**Fecha:** 2026-10-16T18:31:11.119+00:00  
**Duracion:** ~25 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, Canton Florencia <mariaflorencia.canton@crowe.com.ar>, Penalba Agustina <agustina.penalba@crowe.com.ar>, Facundo Ignacio Vivas <>  
**Externos:** mariaflorencia.canton@crowe.com.ar, agustina.penalba@crowe.com.ar, Facundo Ignacio Vivas  
**Apollo ID:** 6ad2735c1a09be001c40c328

---

**Lucio Rojas**: Hago el disclaimer, me llamaron el correo que me iba a traer algo muy completo justo ahora, así que capaz que baje y los deje con archivos. Ahí se debería estar sumando Facu, qué timing. Bueno, buenas. Los pongo en contexto rápido por si me tengo que bajar un segundo. Nosotros estamos trabajando con Grow, empezando a hacer una implementación de nuestro SaaS o una prueba de concepto. En realidad nosotros lo que tenemos es un producto que lo que hace es conectarse a fuentes de datos y generar toda una capa semántica. Y a partir de esa capa semántica disponible un MCP que sirve para hacer consultas, para generar vistas, para generar. Para generar alertas y demás. Sobre todo desde el fallo de negocio. Esta Flor que ella está probando del lado funcional, está trabajando con los datos.

**Canton Florencia**: Buenas, Flor, ¿Cómo andan? Perdón. ¿Todo bien?

**Lucio Rojas**: Para unos proyectos vinculados a cash flow, a todo lo que es la parte administrativa. Y estamos trabajando con DAMS de reportes de vistas, de Calypso. Y nosotros lo que buscamos como óptimo la herramienta es poder integrarnos a las fuentes y a las bases. Obvio que es un proceso que también hay que paralizarlo con el avance comercial y el proyecto, pero por lo menos para ya también saber cuáles son las posibilidades y la viabilidad de este lado. Ahí nosotros tenemos en realidad una forma estándar de conectarnos, que es yendo contra los motores de base de datos o donde están las fuentes. En muchos casos hay sistemas que están a un PREMIS y hay otros casos en donde son los dueños ellos de las bases de datos y te dan APIs o tenés que pedirle permiso, una consulta o una vista.

**Penalba Agustina**: Yo les mandé una documentación hoy a la mañana, no sé si la pudieron ver, sí eso se pueden conectar así, porque así tengo otros clientes integrados con su e commerce o demás.

**Facundo Ignacio Vivas**: Perdón que justo se me apagaron los auriculares, se me queda sin batería. No, te escuché lo último que me dijiste, Agus.

**Penalba Agustina**: No, que digo, mediante esa conexión vía API, yo tengo un cliente, por ejemplo, que no sólo consume datos, sino que hasta factura directamente o envía los correos o lo que sea. No sé, si quieren hacemos una pruebita. Les, les decía, yo les genero una licencia en un entorno de stage que tenemos de desarrollo y hacemos una prueba, porque ustedes necesitan consumir, no sé, movimiento, tesorería, supongo. Cobros, o pago, va por ahí

**Facundo Ignacio Vivas**: con respecto a eso, La conexión a este ERP requiere un laburo y un desarrollo nuestro para crear este conector que en definitiva sería custom para este tipo de casos. Estuve averiguando ahí un poquito porque no conocía la herramienta y por lo que averigüé, ustedes sabrán mejor, tiene dos modelos de negocio, uno en la nube y uno digamos on premise, no sé cuál están usando ustedes. ¿En la nube, o sea ustedes no tienen ningún acceso al SQL Server o a la base de datos del ERP,

**Lucio Rojas**: ese acceso existe para saber más forma de gestionarlo, por ejemplo pidiendo permiso a Calypso o hablando con Calypso?

**Penalba Agustina**: No, no, porque de hecho es una pelea mía como consultora cada vez que quiero armar una query comple, pero si tengo la experiencia de que esto que les digo de otro cliente que consume datos externos de manera externa desde Calypso y labura súper bien de esta manera.

**Facundo Ignacio Vivas**: Como poder, estoy seguro que se va a poder, de hecho con la documentación que nos pasaron creo que ya nos alcanzaría. ¿Lo único ahí, eso que hoy en día no podemos conectarnos directo, requiere el

**Canton Florencia**: desarrollo, ese otro punto que no lo habíamos hablado Luz antes o no?

**Lucio Rojas**: Sí, porque está las dos opciones o le pegamos a su motor, pero como no se puede por lápiz, entonces ustedes, vos Agus trabajas de soporte interno de Calypso, para que lo.

**Facundo Ignacio Vivas**: Exacto,

**Penalba Agustina**: miren por ejemplo algo súper sencillo, pero acá están las ventas de las chicas, hay un montón de info, bueno no importa, acá están los movimientos de ventas y desde acá, desde acá cada digamos browser que se puede interpretar como una tabla, cada tabla tiene un iconito que dice API.

**Facundo Ignacio Vivas**: A Tango, tenemos el conector, de hecho lo desarrollamos lo mismo, así que sería algo muy similar.

**Penalba Agustina**: Yo lo que les decía es, yo les pasaría este token para que un usuario pueda acceder a la información y después si quieren, si veamos en conjunto, porque claro qué tablas tienen que consumir y eso, pero sí, sería así, sí,

**Facundo Ignacio Vivas**: ahí en la conexión a theramot en sí el token digamos lo proveerían ustedes en el formulario donde ingresan la URL de la API que estimo que es pública, ¿No?

**Penalba Agustina**: Sí, sí, Crocalypso 365

**Facundo Ignacio Vivas**: completan con la autenticación de la API y hacemos el descubrimiento de las tablas digamos y después hacemos la ingesta. Lo que sí me serviría eso que me decís, que me generes una AP en algún ambiente como para que nosotros podamos probar el conector antes de largarlo.

**Penalba Agustina**: ¿Ibas a decir algo Flor?

**Canton Florencia**: Sí, yo iba a consultar para los que no estamos tanto en datos, tanto o nada en datos y sistemas, qué diferencia hay entre que ustedes directamente tomen información de la base de datos, que es lo que yo he hablado con Lucio ayer nos juntamos, o esto que es mediante este token que mencionaban

**Facundo Ignacio Vivas**: es más una limitación de del ERP Calypso que no te da acceso a la base, porque si ustedes tuvieran las credenciales de la base y lo tuvieran desplegado on premise, o sea en sus servidores, para nosotros incluso es más sencillo porque ya tenemos el conector de SQL Server, MySQL o lo que sea que corra esto y nos conectamos directo. El tema que el software este te limita y no te deja acceder.

**Canton Florencia**: Claro, mi consulta es en qué varía en cuanto a las propiedades de Theramot para gestionar información, ¿Me entendés? Digo para el usuario final no para ustedes lo van a conectar absolutamente nada

**Facundo Ignacio Vivas**: es lo mismo, llegamos a tener las tablas al final es lo mismo que conectarse a una base cualquiera. El análisis con AI se puede hacer igual y para el que lo consume no le cambia. Lo que sí nos va a cambiar es el desarrollo del conector, las pruebas del conector y el hecho de desplegarlo y probarlo directamente contra su VRP.

**Franco Ferrero**: Facu pregunta ahí para también entender un poco el hecho de la actualización se hace igual, o sea por más de que ya quedan cargadas las tablas que seleccionamos, que seleccionan ellas y ya directamente se actualizan igual.

**Facundo Ignacio Vivas**: Sí, sí, sí, eso funciona igual que funcionaría igual que un conector DV, con la excepción de que probablemente tendríamos que ver el tema de incrementalidad, no sé si se podrá hacer en la primera iteración, pero no sé de qué magnitud de datos estamos hablando, si vale la pena hacer una una carga incremental o si con una carga completa todos los días o con la frecuencia que ustedes quieran, no sea la madrugada o cuando haya poco tráfico, con eso alcanza.

**Canton Florencia**: ¿Y la idea, yo lo que tenía entendido era que yo al día siguiente podía obtener toda la información, con lo cual eso se debería ir actualizando?

**Facundo Ignacio Vivas**: ¿Y ahí tienen una estimación de la magnitud de los datos, cuánto, cuánto, cuántas tablas son, cuántas Rose tienen aproximadas?

**Penalba Agustina**: ¿A ver Flor y te pregunto yo si te parece por un qué información querés vos publicar? Las ventas los cobro en eso de

**Canton Florencia**: pronto más para mí tendría que ser por ejemplo lo que estamos viendo era el tema de unas proyecciones futuras, tendría que ser casi todo ventas, compras, cobros y pagos como mínimo, o sea todo movimiento de tesorería, todo ítems de compra, todo ítem se venta.

**Penalba Agustina**: OK, bueno está bien, no sé, digo, me hago unas queries y te digo Facu si querés después. Qué volumen es.

**Canton Florencia**: Claro, y esto que vos mencionaba Facu de un desarrollo así del conector, qué tiempo demora, qué implica

**Facundo Ignacio Vivas**: y te digo por experiencia, el de Tango del otro día lo pudimos sacar en dos o tres días haciendo pruebas y esperando que salga a producción, pero bueno no sé si vamos a tener la misma facilidad, por eso te digo, desconozco ERP, como funciona, sé que la documentación está y la vía un poquito para arriba, así que con eso tenemos algo para arrancar, pero no sé si nos vamos a chocar con cosas en el camino, por eso no te quiero dar un estimativo

**Canton Florencia**: de base, eso sería. ¿Claro y Agus te consultó, en el caso de Calypso como se llama el enterprise?

**Penalba Agustina**: Es Corporate.

**Canton Florencia**: ¿Corporate es lo mismo?

**Penalba Agustina**: Sí, a ver, eso que decía Facu es como por lo que preguntabas antes, o sea si es como la visión de cada uno, para mí es mejor que se conecten, o sea mi opinión es mejor que un externo se conecte vía API por una cuestión de seguridad y que tu base, que no acceda nadie a tu base de datos y es una buena práctica que un proveedor externo acceda mediante un token, porque a nosotros nos queda el registro de cuándo se conectaron ellos a leer tal cosa, digo hay como como muchos protocolos de seguridad de track que a mí por experiencia me parece mejor de esta manera que pegar directo a la base, pero ponele Corporate también usa lo mismo, en este caso siempre que vamos conectarnos con terceros es mediante una API, yo creo que no debería variar tanto desde Tango, no son tantas vistas tampoco. Ponele esto que me dice Flor son seis, o sea una vez que te conectaste ya después es la misma estructura y veremos cuáles son los campos que quieren consumir y eso,

**Franco Ferrero**: Los campos o las tablas o dentro de las tablas cada campo, ¿No?

**Penalba Agustina**: Porque, qué sé yo, ponele, yo te voy a decir, pégale a esta tabla, ¿No? Y por ahí el campo, no sé, las chicas guardan algo en un campo auxiliar 25, y yo te voy a tener que decir que es. Si, no, no. Hay cosas que no sé, Fecha y neto IVA. Eso es bastante claro. Pero después hay particularidades propias del sistema, que si van a querer armar un dashboard o algo, me parece que.

**Franco Ferrero**: A ver, no sé si no me estoy confundiendo, pero en el caso que nosotros traemos las tablas, en el caso de haber alguna que otra columna medio extraña, o sea, los agentes internos lo detectan eso, ¿No, Facu?

**Facundo Ignacio Vivas**: Para esos casos puntuales, por ejemplo, eso decís auxiliar 23, únicamente la persona que lo diseñó sabe, salvo que sea muy obvio que sea deducible por un agente, que podría ser tranquilamente. Pero para eso dentro de la plataforma tenemos la capa de knowledge, que es el conocimiento que configura el propio usuario usando cloud o algún agente de AI, en el que le puede decir, mirá, la columna que se llama auxiliar 23 significa tal y tal y tal, y se relaciona con tal. Entonces cada vez que vos haces la consulta por cloud o por la gente o lo que sea, a tus datos lo va a tener en su conocimiento, entonces ya lo va a interpretar. Pero por eso está bueno esa capa de conocimiento, para estos casos ambiguos en los que una gente no sea capaz de deducirlo, hacerlo a mano, más que a mano, explicárselo a Claudia, y que él cree el conocimiento que es el uso que le damos, con eso alcanzo.

**Penalba Agustina**: Bueno, ahí mira, mientras estábamos hablando ya le generé un token, ahora se los comparto al correo. Yo creo que sólo estaba Lucio, pero sumo. Este un ambiente de stage, así que ahí lo pueden probar. De hecho está actualizado uno o dos meses atrás, no es que está tan viejo. Y bueno, ahí ya podríamos comenzar las pruebas. Y si quieren les paso algunos endpoints de ventas, por ejemplo, para que vayan viéndolo. Y no sé si necesitamos otra reunión. Estoy.

**Lucio Rojas**: Dale, dale.

**Facundo Ignacio Vivas**: Yo creo que igual con la documentación, el token y se me tiras ahí las tablas o las vistas que sean principales, con eso podemos validar que el conector funcione y después nada, lo dejamos que descubra lo demás. Probablemente, bueno, después habrá que ver como el conector en el formulario, cuando uno hace la carga. Quizás tengamos que configurar cuáles son las vistas con el nombre exacto o algo similar, pero bueno, eso es una configuración de una sola vez que después ya queda

**Penalba Agustina**: OK. Y ahí una pregunta que seguro les pasa, pero nosotros tenemos dos tablas, dos tablas y una tiene una clave foránea y depende de otra. ¿Ese macheo lo hacen ustedes o es algo hablar eso?

**Facundo Ignacio Vivas**: Se trabaja todo internamente, se auto detecta la foreign key y se guarda en la metadata, digamos.

**Penalba Agustina**: Bueno, ahí les mando esto por correo que ya estaría y lo que necesiten nos avisan.

**Lucio Rojas**: Perdón, justo me llegó

**Penalba Agustina**: que me imagino estar esperando hace un montón.

**Lucio Rojas**: No, es que me dijeron que iba a llegar la semana que viene y nada, me llamó loco, me dice te abajo.

**Canton Florencia**: Bueno, bien, buena noticia para el fin.

**Lucio Rojas**: Bueno, entiendo que se pusieron de acuerdo con la conexión y después Flor, que haría que nosotros podamos ver la parte comercial con los Marcelos.

**Canton Florencia**: Sí, yo iba a decir eso. Si bien la parte comercial no estaba del todo cerrada, tengo lo que hay, pero no sé si esto del conector va a generar algún tipo de diferencia en la propuesta comercial originalmente que le pasaba a los.

**Lucio Rojas**: No, no, sigue siendo la misma.

**Canton Florencia**: Eso como para validarlo. Bueno, igual tengo entendido que esta parte está todavía pendiente, pero vayamos avanzando lo que podamos.

**Lucio Rojas**: Bien, bueno, después entonces tendremos otra reunión por ese tema, si viene candidato. Bueno,

**Canton Florencia**: los próximos pasos.

**Lucio Rojas**: Nosotros con generar la conexión, que entiendo que queda de nuestro lado, ya estaríamos listos para arrancar. Es automático el proceso de setup, si querés, de la herramienta y va a quedar todo conectado para poder empezar a repartir los usuarios y. Y trabajar con vos o con otras unidades de negocio. La implementación y la generación de Azures de tablas de consultas.

**Franco Ferrero**: Ahí también, sorry, o sea, una vez que tenemos nosotros desarrollado el conector, ustedes tienen que ver qué tablas van a querer que nosotros ingestemos, porque como tenemos que ingestar tabla por tabla, tenemos que ver bien ahí qué es lo que quieren ustedes, más que nada para saber qué buscan y en base a eso les cargamos las tablas que necesiten.

**Lucio Rojas**: Y vos le preguntás cuál no era

**Canton Florencia**: como para saber cuándo sería que nosotros teníamos que mandar algo más de información. Si Agus tenía que pasarle algún tipo de información puntual. Si con esto, el token que ya les compartiste Ya está. Yo hablo desde mi desconocimiento total

**Lucio Rojas**: con

**Facundo Ignacio Vivas**: la URL del API de Stage, el token que recién generó y una, dos, tres tablas para hacer alguna pruebita puntual.

**Lucio Rojas**: Ya estamos. Nosotros estamos bien y una vez se destractual que arrancamos.

**Canton Florencia**: Dale, perfecto. Buenísimo.

**Penalba Agustina**: Bueno, ahí le saco el correo.
