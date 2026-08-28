# Teramot <> Sitecno

**Fecha:** 2026-07-29T17:30:24.785+00:00  
**Duración:** ~12 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Estanislao Sallent <esallent@sitecno.com.ar>  
**Externos:** esallent@sitecno.com.ar  
**Apollo ID:** 6a6a3b871d0f5b001074eda1

---

**Estanislao Sallent**: Buenas.

**Lucio Rojas**: Buenas. ¿Cómo va?

**Estanislao Sallent**: Mandando unos mensajes. ¿Todo tranqui?

**Lucio Rojas**: Sí, todo bien.

**Estanislao Sallent**: Buenísimo, Gracias por tu tiempo ayer. Nada, fue. Estábamos desencontrados.

**Lucio Rojas**: Sí, sí. Igual era poco eficiente la forma que se me ocurrió de Santerlin, No, no,

**Estanislao Sallent**: si hubiera estado un poquito más liberado estaba bueno. Pero no, nada, se fue un día complicado.

**Lucio Rojas**: A mí no me jode porque dejo la pestaña abierta ahí al costado y me quedo haciendo otra cosa todavía más.

**Estanislao Sallent**: Bien, todo tranquilo. Bueno, ¿Qué pasó con la base esta?

**Lucio Rojas**: Lo que pasó fue que vos lo que hiciste fue conectar una que era una Postgres que tenía 1600 tablas y nuestro conector lo que hacía era un descubrimiento del esquema de cada una de esas tablas secuenciales. Se traía la forn key, la yul keys y después miraba la otra, después la otra 1 más n, y por la longitud de la base terminaba dando timeout por la cantidad de tablas, sobre todo porque no teníamos testeados casos tan anchos. Entonces nos encontramos con eso. Cuando vos lo conectaste, no te respondí al momento, pero sí puse al equipo a verlo. Básicamente estaba viéndolo y encontraron el fix y lo mandaron a cuatro cinco.

**Estanislao Sallent**: Ah, buenísimo. No, Osip, ¿Cuál es el? ¿Van a aceptar más cantidad o? Porque si no, lo que no sé si se puede hacer como el select de lo que se necesita, porque esta es la base entera.

**Lucio Rojas**: Claro, si, nosotros. Son cosas distintas. Lo que hicimos fue paralizar los procesos de escoba. También para el producto nos sirve. Sí, lo que vas a ver vos cuando tengas la. Primero levanta el esquema y te dice tenés todas estas tablas y vos ahí seleccionas y ahí vas a poder seleccionar las que vos quieras y esas son las que procesa la herramienta.

**Estanislao Sallent**: Lógicamente le puede aplicar filtros también para la cantidad, para los registros que quiero, o sea decir che, tráeme de acá hasta acá nomás,

**Lucio Rojas**: capaz que lo consulto y te mando yo por ustedes, porque

**Estanislao Sallent**: por ahí muy grande y por ahí no es necesario tanto. Pero bueno, nada, si ustedes se lo bancan, yo feliz laburo con eso.

**Lucio Rojas**: Creo que los registros no es tanto el problema. Sí, sí, son. Hemos cargado tablas miles de millones de fias.

**Estanislao Sallent**: Sí, me habías contado algo de eso,

**Lucio Rojas**: así que no es tanto el problema. Lo que sí más problema para nosotros es la amplitud. Y bueno, pensé que lo iban a tener para hoy, pero va a salir con el deploy esta tarde y mañana ya podría seleccionar las tablas que descargar. ¿Vos sabes cuáles son?

**Estanislao Sallent**: Si, me mandaron acá lo que yo tenía, la query, Viste que acá te había contado. Esto es una empresa, yo soy consultor y ellos tienen su equipo que les maneja él. El ERP sería. Entonces ellos me prepararon la réplica. Si, entiendo que esto es una réplica. Esta es la base transaccional del COSO. Esto es una empresa que vende telefonía, teléfonos y accesorios, toda la parte tecnología, televisores, todo Motorola. Y una de las particularidades que tiene, que es, tiene ahí único, tiene el email. Entonces tienen toda la base, todo el esquema transaccional basado en eso, informan ventas unitarias, no cantidades. Así que nada, lo que me mandó fue esto. Son tres bases distintas, o sea tres vistas.

**Lucio Rojas**: Necesitas ver tres tablas de la base 1600 que me pasaste. OK.

**Estanislao Sallent**: No, tres vistas que tienen tablas.

**Lucio Rojas**: OK, La base tiene vistas adentro.

**Estanislao Sallent**: Claro. Tenés ventas, nuevo, tarjetas propias y stock. OK, eso tiene adentro. Son tres vistas

**Lucio Rojas**: y adentro tiene las tablas. Yo no soy el que más entiende de esto, sinceramente, se lo paso a Fagu y lo ha.

**Estanislao Sallent**: En realidad es al revés, hay tablas y las vistas juntan datos de tablas y hacen todos los joins, digamos.

**Lucio Rojas**: Sí, sí, sí.

**Estanislao Sallent**: Pero vos entonces las tablas son estas 1600 que hay ahí. Se le quema completo. Yo haciendo estos select ya tengo lo que necesito.

**Lucio Rojas**: OK, Pues ya están las vistas dentro de la base.

**Estanislao Sallent**: Claro. Yo después agarro esto y creo las nuevas vistas que son las tablas gold con.

**Lucio Rojas**: Bien, perfecto. Bueno, capaz que con esto ya te lo podemos dejar conectado nosotros, no hace falta que vos selecciones nada y te aviso. Así que estaríamos con esto. Después cuando lo carguemos vamos nosotros a ver también cuál termina siendo el volumen real, lo que cargamos. Y te digo, si vemos que por ahí se pasa lo que nosotros definimos como plan free, hasta algo más de relación comercial, pero primero tengo que ver efectivamente qué terminamos cargando. Esto es. ¿Van a necesitar actualización Chrome con refresh o

**Estanislao Sallent**: no? Sí, sí, van a necesitar actualización bien semanal, no hace falta hacerlo en vivo.

**Lucio Rojas**: Perfecto. Bueno, una vez a la semana entonces hacemos actualización de tablas. Yo creo que para ya mañana pasado.

**Estanislao Sallent**: Después las transformaciones que necesito hacer cuando tenga esto hoy, ya están hechas en el proyecto. Que tengo armado con archivos que son bajadas de esto. Claro, por si ustedes quieren incluso mirarlo, no están tan prolijas y tan estables eso. Pero más o menos en esas transformaciones o en esos joins, sí creo que esto reemplaza tres archivos que hay hoy de cinco. Los otros dos seguirían siendo archivo. Eso manejatelo por si ustedes quieren analizar la cuenta completa. No va a ser mucho más de lo que hoy ya está usando archivos.

**Lucio Rojas**: Ya entendí lo que me decía yo me había perdido. Pero claro, ahora entiendo que las vistas vienen adentro de la base también, por más diferenciar los años y quedan persistidas como tablas. Ya entendí un poco. Bueno, lo conectamos. Te aviso después si querés las go que vos ya generaste. Mirá las gol que generé con los archivos esto y volvémelo a generar sobre la base.

**Estanislao Sallent**: Sí, sí, ya hice la documentación sobre las transformaciones que hicimos en la prueba y con esa documentación abro otra conversación y le

**Lucio Rojas**: ponerlo en PDF algo. Eso en un MD.

**Estanislao Sallent**: Un MD, claro.

**Lucio Rojas**: Y después vos con esto preguntan. Ya mira, ¿Qué vas a hacer? ¿Vas a llevártelo a una plataforma tuya que corre sobre tela? ¿Vas a confirmarlo por API?

**Estanislao Sallent**: Hoy el primer uso va a ser hacer un artifact con esto para que lo ejecuten acá internamente, lo usen los analistas. Es más, los artifacts ya están hechos, va a haber que reconectarlos y ajustar. Pero por ejemplo, un caso de uso es el abastecimiento, la recompra de stock te va consumiendo. Si, bueno, calculame. Tiene todas las fórmulas que le armé para calcular que tienen que comprar. Entonces tiene un tablero, se fijan la matriz y bueno, compro esto que está acá, compro esto o después es el análisis de la venta para la optimización comercial, la tasa de conversión del e commerce. Por ahora son ese tipo de casos de uso acotados. Después la idea que decíamos, tener que pasar un plan enterprise, o sea el primero no acuerdo cuál era, es para directamente hacer cosas para. Esta es una unidad de negocio, pero la base que estamos conectando es de la empresa entera. Entonces es hacer un módulo de control financiero de liquidaciones, ya más para que lo usen los administrativos, el CFO, etc.

**Lucio Rojas**: Buenísimo.

**Estanislao Sallent**: Bueno, vamos de a pasito.

**Lucio Rojas**: Sí, Después te voy a traer algunos de los founders para que te cuentes un poco lo que venía haciendo porque no sirve.

**Estanislao Sallent**: Está bueno, dale, Sí, sí, obvio, de una.

**Lucio Rojas**: Listo. Bueno, yo te dejo estundando y mañana te aviso.

**Estanislao Sallent**: Dale, chiflame nomás. Mira, Lucio.
