# Impromptu meeting

**Fecha:** 2026-10-08T17:30:59.519+00:00  
**Duracion:** ~22 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Maximiliano Majul <>, Facundo Ignacio Vivas <>  
**Externos:** Maximiliano Majul, Facundo Ignacio Vivas  
**Apollo ID:** 6ac7d88e40ea29001c20d1c3

---

**Maximiliano Majul**: Acá estamos, estamos Belén, yo, el Gonza que estuvo la reunión pasada y está Darío también, que el gerente del sistema, no sé si lo alcancen a ver en la cámara, no lo está tomando.

**Facundo Ignacio Vivas**: Sí, sí, se ve.

**Maximiliano Majul**: Bueno, hago un recuento, digamos, un poco de las reuniones que tuvimos antes. Primero tuvimos una primera reunión, Franco, que no estuvo Facu, estuvo otro de los chicos. Me parece que ahí hemos hablado de que estuvo Darío y hablamos de una primera opción de conexión. Después hicimos una segunda reunión para dejar en claro esa conexión, que estuvo Gonza, no estuvo Darío. Entonces la idea un poco poner ya como idea definitiva de cómo sería la forma en que nos conectemos, cosa que también lo escucha Darío que nos tuvo la reunión pasada y bueno también Gonza que nos acompañó la reunión anterior. Entonces un poco repasar lo que hablamos. La última reunión, Si puede ser,

**Facundo Ignacio Vivas**: dale. Había dejado yo creo, y es la que decís que hablamos del conector de Oracle G y bueno y demás cuestiones. Bueno, no sé si quieren arrancar, si tienen algunas dudas o repasamos de cero. Cómo sería cuento.

**Maximiliano Majul**: Yo lo que interpreté en la primera reunión, Facundo, yo entendí que con un DAN de la base Oracle subido a una dirección URL que ustedes nos iban a dar, se resolvían el tema de los datos. Después esto estuve de vacaciones, cuando volví Gonzalo, que está encargo de la biotecnica, me dice que particip y que esa alternativa del DAM no era viable. Conexión directa a la base disponibilizada en un entorno dema y fu.

**Facundo Ignacio Vivas**: Exacto.

**Maximiliano Majul**: ¿Cuál fue el problema de que se descartó o se cambió la primera alternativa, el DAN, porque esa es la opción que no cierra?

**Facundo Ignacio Vivas**: Claro, ahí no sé con quién habían hablado la primera vez, pero esa opción nosotros no la ofrecemos como servicio a ninguno de nuestros clientes. No ofrecemos infraestructura para que puedan levantar datos en nuestras nubes, sino que vamos por otro camino y es el de la conexión directa a las bases. Por lo que ustedes entiendo tenían una réplica o querían levantar una réplica, digamos que la. El trabajo de infraestructura y de levantar el DAM, nosotros no lo tomamos, se lo dejamos del cliente, digamos. En este caso,

**Maximiliano Majul**: si la opción es esa, vamos a tener que analizar

**Maximiliano Majul**: sí eso cambiaría. Sí, si es acá interno o cámara nube. Y ahí estuvimos analizando. Le había consultado en la reunión, Maxi era también que definieran ellos qué información para sacar en base a qué tabla, podíamos también exportar, digamos, no exportar toda la base de datos, inclusive temporalmente, no el histórico, porque lo que hace falta es solamente poner un año para atrás. Y esa definición, digamos, la información que ellos lo que van a tomar del sistema para quieren mostrar, para también sacar específicamente temporalmente. Y si es posible, las tablas que hagan falta. No todo. Por eso hablamos también de confidencialidad, para no sacar todos los datos de los clientes. Pero más allá de eso, el lugar interpretó que era la parte.

**Maximiliano Majul**: Fue lo que nos dijeron. De hecho ellos plantearon esa alternativa. Con esa opción no tenemos ningún inconveniente. ¿Quién participó? Gente de Telmo.

**Maximiliano Majul**: Esa parte quedó ahí pendiente. El donut es otra cosa, pero el tema donde subimos esa info era determinante también para seguir.

**Maximiliano Majul**: La gente que nos hace servicios DBA también provee entornos como AWS, Google o algún otro proveedor para subir lo que se defina. ¿Que hace falta, Gonzalo? Contenido del último año, toda la base completa. Pero eso tiene un costo adicional como está planteado. Costo caro nuestro.

**Maximiliano Majul**: Bien. Bueno, o sea, la única que tenemos es esta que menciona el Facu.

**Facundo Ignacio Vivas**: Sí, yo la verdad que no sé con quién habrán hablado, quizás se malinterpretó. La opción que nosotros ofrecemos de dump no es la de que ustedes suben un punto backup de la base de datos y nosotros posteamos la base, sino que ustedes descargan los archivos y nosotros le proveemos para subir en formato archivo, que es lo que habíamos hablado en la reunión anterior. Pero esta opción de hacer un backup y hostear nosotros una base de datos, no es algo que tenemos contemplado. Así que la alternativa es lo que habíamos hablado. Por un lado, si quieren trabajar con datos estáticos DAM, sería hacer una bajada de archivo, csb o parquet y subirlos a la plataforma y trabajar con eso. La desventaja es que se reniega un poco más con el tema de la actualización. Y después la otra alternativa es conectar nosotros a una base que ustedes nos disponiblen una réplica o lo que ustedes prefieran, con el usuario limitado a las tablas que ustedes quieran, y nosotros nos conectamos directamente ahí. El directamente no es tan directamente, porque salvo que la base esté disponibilizada, alcanzable de Internet, podríamos llegar. Pero también ofrecemos métodos de conexión. Lo habíamos hablado en la reunión pasada, tenemos túneles IPC como opción recomendada nuestra y principal. Y también tenemos la opción de túneles especial. Es para debatir y para que ustedes consideren en ese punto.

**Maximiliano Majul**: ¿Ahí cuando hablaste del TXT, digamos, es usted tiene un repositorio, lo leen? Ahí me quedó una duda, porque ponele que nosotros, los chicos hacen un estudio y se ve qué tabla necesitan y se exporta esa parte. ¿Ese servicio lo ofrecen o no? No me quedó claro

**Facundo Ignacio Vivas**: cuál sería

**Maximiliano Majul**: de los TXT o otro formato, sí de

**Facundo Ignacio Vivas**: los SB o Parquet o XLSX. Sí nosotros proveemos la API de nuestro backend y les damos el script para hacer la subida, eso sí se lo podemos disponibilizar porque lo hacemos con. Con otros clientes.

**Maximiliano Majul**: La subida en su repositorio.

**Facundo Ignacio Vivas**: Claro, exacto.

**Maximiliano Majul**: También esa es la otra opción. ¿Qué tabla son? Y le subimos todos los días, Exportamos todos los días la gente. Hacemos la exportación, las tablas que hagan falta, con el tiempo necesario que ellos requieran, por atrás, seis meses, lo que sea. Y eso se lo mandamos todos los días. Esa es otra opción. Pero eso también un laburo fino, digamos, que necesita interpretar todas las tablas que están involucradas, todas las relaciones.

**Maximiliano Majul**: No sé si vos tenés posibilidad de hacer eso.

**Maximiliano Majul**: Volumen de venta. Descartado, pero subimos todo menos los datos que no queramos subir.

**Maximiliano Majul**: Y exportación a archivos Excel de texto.

**Franco Ferrero**: Pero les hago una pregunta ahí también, un poco para entender por qué. También para entender el tema de no disponibilizar y no conectarse directamente a la fuente. También entender por qué capaz no prefieren hacerlo de esa manera, ya que capaz es la manera en la que hacemos con casi todos los clientes. Más que nada también para entender a ver si es un tema de seguridad de datos o un tema confidencialidad.

**Maximiliano Majul**: Seguridad, confidencialidad, performance.

**Franco Ferrero**: Estamos hablando de que sería mucho mejor la herramienta con los datos conectados a través de la fuente. Porque esos datos se van a ir actualizando también constantemente para el uso y el análisis de los datos.

**Maximiliano Majul**: A la base de producción, de ninguna manera a la base de reporting. No sé el impacto que tiene teramon sobre esa base. Se está usando para otras aplicaciones con Power BI. No sé qué impacto va a tener teramon. Y te doy acceso a esa base. El entorno que tenemos que está funcionando, no lo quiero tocar. La alternativa es darte acceso de otro man.

**Facundo Ignacio Vivas**: Nosotros la ingesta de datos la hacemos en Baches tratamos de cubrir para los casos que los clientes nos conectan la base de datos productiva. Entiendo que este no sería el caso. Trabajamos la ingesta en baches y bueno, la mayoría de los clientes cuando coordinamos la actualización de los datos, lo hacemos a la madrugada o a la mañana muy temprano, para no impactar en la operatoria que tengan durante el día. Y otra ventaja de la conexión a la base de datos es que si está preparada la base, podemos configurar una carga incremental y no tener que inyectar todos los días toda la base. Eso quizás sea una ventaja de hacer los dump de los gatos de parte de ustedes todos los días, pero bueno, obviamente para que lo pongan sobre la mesa, lo consider para nosotros cualquier forma es indistinta, mientras los datos estén y puedan ayudarlo y servirle a una maxi para hacer el análisis.

**Maximiliano Majul**: Y esa conexión batch que decís, ¿Tenés idea del tiempo que demora esa conexión?

**Facundo Ignacio Vivas**: Depende obviamente de la magnitud de los

**Maximiliano Majul**: datos,

**Maximiliano Majul**: Son 30, 40 GB, pero también tenemos a la madrugada, tampoco se hace proceso de copia, se hace el dump, todo lo demás que tenemos que hablar, ¿Cómo hacemos para mejorar lo que está? Porque también están requiriendo retención del cliente que tienen tan grandes para los reportes antes, entonces ahí nos pisaríamos la base de datos reporting sería medio inconveniente, porque tenemos que resolver primero para lo que está el requerimiento actual de la atención del cliente. Estamos pensando en adelantar la hora, adelantar

**Maximiliano Majul**: la hora de reporte, se genera, se

**Maximiliano Majul**: corren los strip, queda ahí sería no de madrugada sino de día. Se puede hacer uso, se puede hacer uso de esa base. El tema licenciamiento y todo, Los puertos también, los chicos tienen toda la parte de seguridad con intersex y todo lo demás, es cuestión de pensar de esa parte.

**Maximiliano Majul**: Bueno, lo llevemos a los tares, lo analicemos.

**Maximiliano Majul**: ¿Bueno y querés que comente un poco lo de COBOL? Llegó el caso Darío, un poco también lo que hablamos la vez pasada.

**Maximiliano Majul**: La única alternativa es que nosotros generemos archivo Excel o archivo de texto. No hay forma de que accedan los archivos.

**Maximiliano Majul**: Listo, eso quedó igual que la primera vez. Y llegado el caso, la secuencia la tenemos clara, digamos, para conectar y más

**Maximiliano Majul**: tenemos que resolver internamente. Tienen que ocuparse de conectar y después mandarnos nosotros el tema de IPC y todo para acceso a nuestras IPC.

**Maximiliano Majul**: Bueno, llevemos eso para analizar, vamos a hablar con la gente de la base de datos para considerar el tema este de si no veremos el tiempo de disponibilidad de la base de report.

**Maximiliano Majul**: Bueno, ¿Alguna otra duda ustedes chicos? ¿Alguna duda de nuestro lado?

**Franco Ferrero**: No, yo lo único, a ver, también quiero ¿Ustedes hoy en día usan Power BI para generar estos reportes, digamos, o sea, conectado Power BI a su base de datos o lo tienen vía un DAM también?

**Maximiliano Majul**: No, no es así. Se hace un DAM sobre una base de datos de reporting del día anterior y después tenemos el gateway de Power B y hacen las consultas. La gente de Atención al Cliente dentro de la misma base tiene procedimientos y estimo que hacen también consultas sobre la base para generar los reportes diarios.

**Franco Ferrero**: ¿Y ustedes pueden trabajar sobre esa base también, o no, o ustedes tienen que trabajar sobre otra base?

**Maximiliano Majul**: Se puede trabajar también sobre esa base, no habría problema. El tema que justamente estamos un tema a resolver, que el DAM y los procedimientos se dan bastante tiempo y estamos viendo hacer también un esquema según la tabla, tenemos tareas solapadas.

**Maximiliano Majul**: En resumen, no está funcionando óptimo ese esquema de reporte.

**Maximiliano Majul**: ¿Por qué decir el Power?

**Franco Ferrero**: No, porque a ver, pregunto más que nada porque también nuestra idea con las distintas funcionalidades de Theramot es que nuestros clientes ya no tengan que estar haciendo, o sea, usando distintas plataformas. Y de hecho, o sea, nosotros una de nuestras ideas también es que ya no use más Power BI, que se genere todo este esquema de reporting y análisis a través de Theramot. Por eso también pregunto lo de Power BI, porque sería algo como que capaz también a ustedes los ayuda a resolver esa parte.

**Maximiliano Majul**: Entonces, Franco, ahí te comento, nuestro plan mío y de Belén, digamos, esa es la intención, particularmente esa parte no la manejo yo, digamos, está como en otra área de la empresa. Hoy nuestro alcance es poder avanzar más adelante sobre eso, entre nosotros esto, digamos, pero hoy, digamos, yo hasta que no valide y funcione lo que yo tengo, voy a avanzar para allá, pero sí está dentro del alcance poder liberar por algunas cosas.

**Franco Ferrero**: No, no, perfecto. También, a ver, se los comentaba, creo que con vos lo había hablado, pero bueno, un poco más que nada para hablarlo.

**Maximiliano Majul**: Bueno, quedamos nosotros, hacemos un pequeño análisis interno, Franco, y vuelvo con usted.

**Franco Ferrero**: ¿Sale?

**Facundo Ignacio Vivas**: Muchas gracias, muchas gracias.

**Maximiliano Majul**: Rango gráfico.
