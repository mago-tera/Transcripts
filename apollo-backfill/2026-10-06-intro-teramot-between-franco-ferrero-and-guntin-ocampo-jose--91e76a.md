# Intro-Teramot between Franco Ferrero and Guntín Ocampo José Manuel

**Fecha:** 2026-10-06T18:06:27.477+00:00  
**Duracion:** ~41 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, Jose Ocampo <jose.guntin@ferromex.mx>, Pedro Larghi <pedro.larghi@synthesized.io>, Teo Gimenez <>  
**Externos:** jose.guntin@ferromex.mx, pedro.larghi@synthesized.io, Teo Gimenez  
**Apollo ID:** 6ac5423527a23b002091e76a

---

**Franco Ferrero**: Estás conectado al MCP. Una vez que estás conectado al MCP, directamente trabajas desde Theramo, perdón, trabajas sobre Theramot desde Cloud. Entonces acá creamos un chat nuevo, y yo acá le digo al Cloud, conéctate al MCP de Teramot, al Workspace, que es el espacio de trabajo de Ferromex. Entonces, a medida también, José Manuel, que vamos a ir avanzando, te voy a ir diciendo capaz preguntas que se te ocurren a vos, que pueden estar relacionadas a su operaria de hoy en día, del día a día, para también ver a ver si en base a los datos que tenemos, puede llegar a ver algo que de verdad le veas valor.

**Lucio Rojas**: Pedile que te haga una descripción de la. Y explicamos una cosa.

**Franco Ferrero**: Acá lo que hace es.

**Jose Ocampo**: Perdón, voy a ver muy for baby. ¿Que es un eda?

**Franco Ferrero**: Un EDA es un Decile. Sí, Decile.

**Lucio Rojas**: Es un descubrimiento de la base de datos para saber qué tablas tiene, cómo se relacionan, cuál es la lógica de negocio.

**Pedro Larghi**: Un diagrama de entidad de relación.

**Lucio Rojas**: No, ese sería un EDR, que también lo podemos hacer. Y te lo puedo. Este es más como una descripción funcional de cada una de las tablas, y te va a explicar la lógica de negocio que hay en la base de datos.

**Pedro Larghi**: Excelente.

**Lucio Rojas**: Se me está trabando la cámara, así que la voy a apagar.

**Pedro Larghi**: Sí, sí, sí, sí.

**Lucio Rojas**: Pero les explico rápido por qué Tiramot puede hacer esto. La verdad no conozco cuáles fueron las presentaciones anteriores que tuvieron, pero una parte muy importante de nuestro producto, sobre todo el inicial, es cuando los agentes se encargan de hacer una sanitización, una estandarización y una capa semántica de las bases de datos de forma autónoma. ¿Qué quiere decir eso? Nosotros vamos a recibir las bases de datos y vamos a empezar a ver ahí, Fran, si querés podés el producto tabla por tabla, to con la tabla silver y hacer el esquema. El segundo tabla por tabla, vamos a hacer una descripción de qué tipo de datos tiene, qué columna tiene, y esa columna qué información contiene. Entonces, toda esa capa semántica que decimos nosotros, que no es más una descripción de las tablas, de cómo se relacionan las tablas, de cómo se pueden juntar una con otra, lo generamos como conocimiento y se lo damos a los agentes MSP. Entonces ahora podemos tener un asistente que es experto en nuestra base de datos, sin haber escrito nada, sin haber transformado nada para poder usarlo. Y podemos trabajar directamente en las consultas y no en el proceso de ingeniería, que era lo que por ahí antes nos lleva más tiempo de BI.

**Pedro Larghi**: Lucio, te hago una consulta. Esto es un proyecto de migración de SAP ECC a SAP HANA, y bueno, en realidad la idea era que uno pudiera en el nuevo SAP ver el histórico por un lado en un solo lugar, corregime José Manuel si me estoy equivocando, y poder cruzar datos entre los nuevos y los viejos y confirmar trazabilidad

**Jose Ocampo**: y poder mostrar temas de auditoría, etc. Exactamente, es tengo acceso al dato, perfecto. Pero si tengo acceso al dato sin tener visibilidad de la trazabilidad de quién, ¿Por qué? ¿Porque los auditores se pueden preguntar quién sumó o restó esos dos pesos? Pierdo un poco

**Lucio Rojas**: el sentido. Correcto, genial. ¿Ahí qué hacemos? Nosotros hacemos todo este. Todo este mapeo de distintas fuentes al mismo tiempo. Entonces podrían conectar su SC y su HANA y los llevamos a un Lighthouse. Entonces dentro del lighthouse lo que hacemos es poner todas las bases de datos en la misma capa de infraestructura, bajo el mismo visualizador de SQL, en realidad está en s y se visualiza en Atina, en aw, y permitimos cruzar tablas entre sistemas. Entonces como los modelos ya entienden perfecto que hay en cada tabla, vas a ver que el maestro de clientes tiene este código en SAPCC, tiene este código en SAP HANA. Entonces si quiero cruzar el historia con información de un cliente, lo puedo hacer a partir de la vinculación de ese campo y lo va a hacer autónomamente para vincular los sistemas. Si querés FLAM, queremos alguna tabla. Buenísimo Pedro, es justo la razón de ser de la herramienta. Y José Manuel, ahora cuando queremos una tabla, vamos a ver toda la visibilidad y trazabilidad que vos estás mencionando cómo la manejamos nosotros.

**Franco Ferrero**: Vos decís la trazabilidad de esta tabla, Lucio.

**Jose Ocampo**: No, no, a ver, yo necesito la trazabilidad del pasado.

**Lucio Rojas**: Sí necesitas un.

**Jose Ocampo**: Entiendo.

**Lucio Rojas**: Vamos a ir primero de adelante para atrás, vamos al resultado final, que es la tabla de resultados, serían las nuevas vistas cuando estamos creando un reporte nuevo. Ahí si querés abrir presupuesto surreal, puede ser turnos y riesgos cualquiera para ver la query. ¿Qué hacemos? Vamos a cruzar las distintas tablas silver o las tablas ya curadas del Lake House para crear una tabla nueva. En el origen tenemos toda la documentación de cuál fue el requerimiento funcional que dimos para crear esa tabla, y abajo está la query SQL que le da origen a esa tabla. Entonces así puedes ver cuáles y cómo son las vistas nuevas que están creadas con una rigurosidad técnica a nivel ETL de saber cómo está construida esa tabla. Esto es determinístico, un ETL y se actualizar siempre igual que se actualicen.

**Pedro Larghi**: Lucio, una consulta te hago ahí. ¿Esto está muy bien, pero no necesita ser un usuario experto? ¿Es decir, todo esto lo hace la IA en forma autónoma o cómo lo hace?

**Lucio Rojas**: Ahí lo vamos a ver

**Franco Ferrero**: ahora, te voy a mostrar bien, pero para que te des una idea, o sea, esto lo hice yo ayer, me habrá llevado una hora, una hora y media como mucho. La verdad es que yo no soy alguien que entiende hoy en día de lo que hace Ferromex, ni un montón de análisis que a ver, obviamente después vamos a ir viendo los resultados y qué tablas generamos. Yo me fui asesorando con Claude, pero la realidad es que mucho la idea también de esto es que alguien que no sea experto le pueda sacar el mayor jugo posible a todos sus datos.

**Lucio Rojas**: Ahí Fer no sabe SQL, por ejemplo. Yo tampoco. Hay distintos niveles de bytecoding de datos. Si querés está que directamente va a la tabla final sin ver lo que creó, y el que se asiste con clock para generar el código SQL lo actualiza. Pero vos te puedes parar en cualquiera de los dos lugares. Volviendo lo de. Lo ejecutas desde cloud, desde Cloud, desde Cloud Code, y te dan las APIs, si querés después consumir esas tablas para hacer alguna web, algún flujo en está todo pensado para después sistematizarse en base a esto. Volvamos a la silver y veamos la qrisql que da origen de la silver. Acá lo que te dejamos en estos casos no va a pasar.

**Jose Ocampo**: ¿Por qué?

**Lucio Rojas**: Porque estamos usando unos datos demo que son. Se me voy a trabar la cámara, la voy a apagar, no puedo ver mientras estoy trabado, se me rompe el cerebro. Usamos los datos de un CSV, entonces con CSV lo armo Clot ya está bastante curado y no requiere de transformaciones de bronce a silver, de la capa cruda a la capa ya curada. Pero en el caso de que conectemos un sistema real, esta query SQL va a tener un montón de transformaciones de normalización, generalmente de fechas, de nombres, de nulls, de campos vacíos, que la herramienta decide arreglar autónomamente para poder hacer todos los cruces. Y todo eso queda acá con trazabilidad. Lo que vos me preguntabas está en lo tercero que te voy a mostrar. Francia avanzado. Tenés los registros de auditoría y tenés un detalle exacto de quién hizo cada cambio y en qué momento. Entonces no solamente va a tener los cambios, sino quién lo hizo y cuándo. Y un último apéndice de lo que es la gobernabilidad. Tenemos un conocimiento, no sé si lo querés abrir, que bueno, ahora lo podemos generar a partir de la conversión con Cloud, pero lo que hace es, vos le podés explicar a Cloud cómo es tu regla de negocio. Hay industrias donde un cliente no es lo mismo que un cliente en otra industria. Eso generalmente Cloud ya lo entiende, pero lo podemos ir almacenando acá, para que a partir de cada interacción se vuelva más experto sobre nuestros datos. Y por composición, mientras más lo usemos, mejor nos responda. Y esto sirve para vincular a distintos usuarios. Así que bueno, ahí Fran, si querés seguir con la demo, para mostrarles cómo se interactúa, cómo se crean nuevas tablas,

**Franco Ferrero**: Vamos a Claude a ver un poco. Le da que armamos acá lo que dice que armó 25 tablas procesadas para la demo. Lo más importante habla, bueno, ya empieza a hacer un análisis sobre una caída fuerte de puntualidad en Piedras Negras, que es un sector de México. Estos son datos que armó Claude. Acá te armó un panorama general. Los datos cubren un año y medio, de enero 2025 a septiembre 2026. Las tablas más grandes son embarques, la finalización del libro mayor mensual, la composición de factura de proveedores y la compra de órdenes de compra. Los maestros son más chicos. Podemos ver 148 clientes, 92 proveedores, 144 locomotoras, 1800 carros y 27 estaciones. La operación habla de volumen, ingresos, un ingreso mensual que va. Estos son análisis que va haciendo sobre los datos. Como te digo, a ver, estos números no van a ser los números que ojos, Emanuel.

**Pedro Larghi**: No importa. Esto es un ejemplo. Sí, sí, sí.

**Franco Ferrero**: Entonces, nada, como que acá ya te empieza a hacer distintas evaluaciones, te habla una caída de mayo julio, te explica el efecto de por qué se concentra ese cruce, qué fue lo que pasó, y el tipo de cambio. También cómo se factura el USD, como que toma en cuenta un montón de variables sobre los datos, que la verdad nosotros. A ver, como te digo previamente, yo no sé qué hace Ferromexica y lo fui armando con Claudia, me imagino también un potencial mucho más alto con alguien que entiende los datos y sabe sobre lo que está trabajando. Entonces, bueno, te habla también de la seguridad de los distintos vagones, del combustible, mantenimiento de los, en este caso de los ferrocarriles, y una parte de finanzas sobre cartera de clientes CAPEX. Y acá lo que habla es sobre la calidad de los datos y posibles fugas de compra. Y además agregamos todo un sector de recursos humanos para tomar en cuenta todo lo que es distintos tipos de clientes. Entonces acá le podemos decir a Claude qué tipo de análisis podemos hacer. No sé, José Manuel, si te gustaría ver algo en particular.

**Jose Ocampo**: ¿Sí, qué podemos explotar del lado de RH, por ejemplo, números de aumentos de salarios de Pedro, cuál fue el último aumento de salario, en qué porcentaje? Ese tipo de cosas.

**Franco Ferrero**: ¿Bueno, acá yo le pregunté a Claude, bien qué podemos hacer? Y en base a las tablas que tiene, te dice los distintos análisis que te recomienda hacer, como puede ser operación y servicio al cliente, en diagnóstico de puntualidad, rentabilidad por corredor, segmento y cliente, demoras en los carros, mapa de estaciones y fronteras, la distinta flota y mantenimiento y los costos de esas flotas, Un tema presupuestario, compras y proveedores, análisis de riesgo, qué tipo de incidente, centro de trabajo y causas de recursos humanos, que son dotación y costo laboral por división con rotación, antigüedad, altas y contras, ausentismo, licencias y novedades por división, cruzadas y estructura salarial y brechas entre divisiones.

**Pedro Larghi**: Bueno, ahí Franco, estaría bueno hacer una consulta, como dijo Juan Manuel, acerca de los incrementos salariales de la dotación.

**Jose Ocampo**: Un segundo, segundo

**Pedro Larghi**: del último año, no sé.

**Franco Ferrero**: Entonces digo, armemos un análisis sobre el

**Pedro Larghi**: incremento, sí, salarial de los colaboradores o del personal en los últimos 12 meses.

**Franco Ferrero**: Y acá lo que hace es, vuelve al SQL, vuelve a lo que nosotros le preguntamos, hace un código SQL para ir a Tenamot, y este SQL lo corre dentro de Tenamot para empezar a hacer la tabla de resultados, que son estas tablas Gol de las que nosotros hablamos, que es donde nosotros vamos a poder ver los resultados que nos va a dar.

**Lucio Rojas**: Me gustaría que se llene, perdón, un concepto que para mí lo explica bien. Esto es como si CLOT ahora pasase a ser nuestro equipo de datos, lo que, ojo, no reemplaza equipos de datos, sino que los hace más veloces porque se van a necesitar siempre. Y acá el punto es, le damos todas las herramientas y toda la infraestructura coordinada, entendiendo por infraestructura donde desarrollamos estas tablas, donde las alojamos y demás, para que Cloud pueda trabajar como ese ingeniero y se pueda resolver todos los problemas razonando de datos que antes teníamos que pedirlo ad hoc. Entonces nada más hacemos las preguntas y él tiene toda esta herramienta que nosotros le damos conector para respondernos y va a empezar a responder, a crearse tablas, a crearse dashboards, es el sentido final de la herramienta y de lo que construimos

**Franco Ferrero**: Acá algo bueno para ver es que me dice con los datos que tengo hoy no se puede medir el incremento salarial en los últimos meses, porque ninguna tabla guarda el historial de sueldos que encontré. Te dice las tres tablas relacionadas y me dice lo que sí puedo analizar hoy es el salario de ingreso contra el de quienes ya estaban para los 23 ingresos de octubre de 2025. Algunos casos del cruce por puesto, el cruce con el promedio de quienes ya estaban en esos puestos, por ejemplo acá lo que te hizo fue la diferencia entre los nuevos salarios de los que

**Pedro Larghi**: ingresaron versus los que ya estaban.

**Franco Ferrero**: Versus los que ya estaban. Para ver también qué diferencia tenés entre los antiguos y los que venís ahora contratando. Entonces acá te da una advertencia que dice son uno o tres ingresos por puesto, así que son señales para revisar y no conclusiones. Además el promedio de antiguos no distingue categoría ni antigüedad. ¿Otro análisis que se puede hacer con lo que hay salario según antigüedad, una persona con 10 años de ingreso y una de un año, están cerca o lejos? Sirve para detectar una compresión salarial, dispersión por puesto y división, quienes están muy por debajo, por encima de la mediana, por supuesto, variable sobre fijo en el último trimestre, cuánto pesan horas extras, bonos y compensaciones sobre el salario base, o

**Pedro Larghi**: sea, lo que quiere decir Franco es que no solo te hace lo que vos le preguntaste, sino que te sugiere otras cosas en base al conocimiento que tiene.

**Franco Ferrero**: ¿Claro, hay también un poco también para que entiendan el valor de la herramienta, es decir, hoy en día es como que al estar trabajando sobre Thermomix, ya una vez que Claude logra entender toda la capa semántica que tiene Theramot sobre tus datos, el alcance es muy amplio porque es como empieza a ser un ping pong entre Claude y vos de distintas ideas que se te van a ocurrir, le vas a decir a Claude, se me ocurrió esto, de qué manera lo podemos hacer o qué puedo analizar para este caso, qué tipo de alerta puedo crear para una brecha salarial? Como que es mucha charla, que así como digo, así como hace lo que yo pido, te va a ir recomendando distintas acciones en base a todo el análisis que hace de los datos que tenés.

**Pedro Larghi**: Y otra consulta Franco, suponte que, bueno, acá te dice que no tenés datos históricos en una tabla, por tanto no te puede ser el incremento salarial, no importa, pero suponete que lo hubiera hecho, ¿Dónde queda alojado todo eso para que yo el mes que viene no lo tenga que volver a repetir?

**Franco Ferrero**: Bueno, acá en Teramot lo que hace, cuando hablábamos un poco de la tabla de resultados, esta tabla de resultados, por ejemplo, yo acá hice una tabla que es de turno y riesgo, que lo que toma en cuenta es todos los colaboradores que ustedes tienen horas extra, incidentes que pueden haber en esas horas extra, y lo que hace es te arma una tabla nueva. Entonces esta tabla es una tabla de resultados que la llamamos una tabla gold. Cuando generas esa tabla gold, se genera con el cruce de estas cuatro tablas para generar una tabla, esa tabla se genera con todo este SQL que vemos. Entonces este SQL lo que hace es usar, toma en cuenta estas cuatro tablas y la información de estas cuatro tablas. ¿Entonces a medida que se van actualizando la información de la fuente silver, que quiere decir? Estas cuatro tablas que están alimentando a esta nueva tabla, a medida que se actualizan los datos de esas cuatro, se van a actualizar los resultados de la última. ¿Por qué? Porque el código SQL ya está armado y va a seguir trabajando y se va a seguir actualizando a medida que los datos.

**Pedro Larghi**: ¿Estamos de acuerdo? ¿Ahora, yo cómo vuelvo a ejecutar un listado, un informe o lo que fuera que creé acá como tabla gold digamos otra vez?

**Lucio Rojas**: Ay Pedro, eso se ejecuta autónomamente todos los días, ya queda determinado. Entonces vos le volvés a preguntar nomás a Clon y ya está la información ahí, es el sentido de la tabla, lo deja fijo y podés tener alguna skill que lo haga todos los días. Si vos querés hacerlo repetitivamente. José Manuel,

**Pedro Larghi**: no se te escucha. Estás en mute, me parece.

**Jose Ocampo**: Bueno, bueno, ahora sí.

**Pedro Larghi**: Ahí está.

**Jose Ocampo**: No seas malo, Franco. Podría subir a donde está el Comunidad, relación. Si te entendí bien, a nivel bronce yo tengo las datas, las tablas físicas, demo, dotación, demo, novedades, demo. Licenciado, para.

**Franco Ferrero**: Te corrijo rápido. Estas son las tablas silver. ¿Qué quiere decir esa? Las tablas bronce son las únicas tablas que son crudas, que son los datos de la forma en la que vos los ingestás. Ya Teramot trabaja sobre las.

**Jose Ocampo**: Déjame acabar, déjame acabar. Pero es que entonces, dotación, novedad, licencias, incidentes, ¿De dónde nace?

**Lucio Rojas**: Explicale si querés, Lucio, eso quizás es más gráfico. Cuando conectemos al SAP, tenés la BCID, la BCIK, que son las tablas del SAP. Eso viene de la capa bronce. Nosotros hacemos un dump en la versión SA, un DAM diario de la base de datos, una seguridad server, todos los días lo actualizamos y las B nunca las tocamos. Es un usuario de vista, sin modificaciones, no podemos alterar lo que es su modelo de datos. Lo que hacemos es tirarle una capa encima a la bronce, que corren unos agentes de normalización, sanitización y entendimiento de los esquemas.

**Pedro Larghi**: Eso genera las tablas silver.

**Lucio Rojas**: Si esas tablas vienen del sistema, esa es la respuesta. Nosotros lo que hacemos es volver a cruzarlas para crear gols. ¿Cuál es tu duda particular?

**Jose Ocampo**: Yo tengo tabla 1 a tabla 4. Esas son 100% bronce y 100% crudas. Y es más, en este caso yo las vas a extraer una sola vez y no necesito que todos los días vayas y revises si hay altas, bajas, cambios. Se hace la primera vez y no vuelve a suceder.

**Lucio Rojas**: No entendí. Tabla 1, tabla 4. Es un ejemplo, está dando un ejemplo gráfico.

**Jose Ocampo**: Es un ejemplo del bronce que no lo estamos viendo. De ahí hay un proceso todos los días en el cual va, consulta y actualiza nuevamente la capa silver. Y de la capa silver yo tengo las que tenemos ahí. Dotación.

**Franco Ferrero**: Te cambié porque. Para mostrarte justamente lo que estaba diciendo, que acá es cuando vos seteas la actualización que quieras programar para cada base de datos, para cada fuente que vos conectas.

**Pedro Larghi**: Franco, pero de nuevo, esto es una migración, así que vas a tener una sola actualización. Una sola. Entonces no va a haber actualización. Entonces vuelve para atrás y vemos el cuadrito.

**Lucio Rojas**: El estudio de datos lo muestra bien. Si querés. La bronce es la primer columna dice tablas de origen, eso nosotros ingestamos one time. Y la relación de bronce a silver, que era del medio, es 1-1. Por cada bronce hacemos una silver.

**Pedro Larghi**: OK. Nada más que sanitizada. Sanitizadas Y procesadas.

**Lucio Rojas**: Y procesadas. Y una vez que las tenemos sobre esa silver creamos las go.

**Pedro Larghi**: ¿Las go que son? Los queries resultantes de lo que yo quiera hacer. OK.

**Jose Ocampo**: Explotables y ya publicables.

**Pedro Larghi**: Exacto.

**Lucio Rojas**: Y podemos crear gols de gols de gols, o sea, podemos ir sobre varias iteraciones de goals, me creo toda una tabla de maestros, de una silver a una gol, y después sobre los maestros vuelvo a crear gols que son maestros filtrados por tal columna. Así yo después le comparto una unidad de negocio, una tabla y otra. Otra si quiero manejar la gobernabilidad. ¿Y usted acá ingestarían los dos sistemas, ingestarían el SC y el HANA?

**Pedro Larghi**: No solo el ecc.

**Lucio Rojas**: Y un one shot one time.

**Jose Ocampo**: Correcto.

**Lucio Rojas**: ¿Y ese CC donde lo tienen? ¿En una SQL? Bueno, ahí te comento nomás. Tenemos la versión donde no sé cuántos teras pesará el ICC.

**Pedro Larghi**: Serán como siete, ¿No, José?

**Lucio Rojas**: Siete teras.

**Jose Ocampo**: No, no, no, no. Mi base de datos, cuando esté 100% fría, cuando esté 100% fuera de uso, debe estar cerrando en una Y. 1.9 teras.

**Pedro Larghi**: 1.8. Correcto, sí, sí, porque era. ¿Te acordás cuando coticé lo de Synthesize? Era el segundo sabor. Sí, correcto, tenés razón. 1.7 ter.

**Lucio Rojas**: Nosotros tenemos una versión que a nivel funcionalidad es exactamente lo mismo que el SaaS, lo único que en vez de replicar su servidor on prem en nuestra infra, para hacer toda esta copia, corren su infra. Tienen ustedes que tener algunos requerimientos de server y otras cuestiones de hardware que necesita para correr el software, pero una vez que está ahí, va a trabajar sobre su infra sin duplicar esa información y tiene las mismas funcionalidades y funciona con un poco de mayor velocidad incluso que lo que viene. Pero bueno, es una. Es un detalle. Prefieren no replicarlo en nuestra infraestructura y eso les vuelve a dejar deployadas las tablas de resultados en su infraestructura.

**Pedro Larghi**: De vuelta,

**Lucio Rojas**: no se movería. Pero bueno, es una opción. De todas formas. Acá se los digo por el volumen. Nosotros licenciamos a partir del volumen de storage, y bueno, a nivel tera por ahí incurre en una licencia mayor a la que sería una base de datos. Entonces

**Pedro Larghi**: bien, y contame José Manuel, ¿Cómo lo ves? ¿Pensás que te interesaría avanzar en algún caso de uso? ¿Lo ves viable? No,

**Jose Ocampo**: sí lo veo viable, de hecho

**Pedro Larghi**: creo que es muy potente, ¿No?

**Jose Ocampo**: A ver, qué sucede en los últimos días, en el último mes hubo algunos ciertos cambios, esa parte donde nos habían dicho no, no podemos sobrevivir si no es con toda la data y con toda no sé qué, no sé cuánto, cambió bastante porque se demostró a negocio que ellos sobrevivían migrando 24, algunos con cargas iniciales y en algunos rubros donde sí requerían historia, con 24 meses sobrevivían suficiente. Punto número uno. Punto número dos, los reportes actuales o con esos 24 les da exactamente lo que requieren, especialmente para cualquier tipo de pelea o de aclaración con el sindicato que era nuestro peor, nuestro mayor este tema, ¿De acuerdo? Sin embargo, el tema general de histórico, retención de datos, data fría y poder atacarla, no solamente RH, porque RH nada más son de esos de ese 1.8 teras representan solamente 300 gigas, ¿Vale? Sino de forma general a partir del año 2, ahí sí tenemos que buscar que hacer. Obviamente no me voy a buscar el año 2, yo tengo que llegar el año 2 ya con la solución. Si vas de inteligencia de datos, de inteligencia artificial, un data lake, machine learning o qué chiflados vamos a usar, es donde estamos. Punto número uno. Punto número dos, mi directorio de transformación digital está bastante preocupado y ocupado en temas de inteligencia artificial y nos está pidiendo los diferentes gerentes tener propuestas y tener. Proyecto con acercamientos de IA. En mi caso, pues estoy pensando en Joule, podría ser una de las opciones. El tuyo cruzado de Cloud. La otra pregunta es, ¿Solamente trabajas con Cloud o tienes también gentes hacia Copilot,

**Pedro Larghi**: hacia eso lo vimos la primera reunión, El que vos quieras, digamos? Hay conectores con los más conocidos, es

**Lucio Rojas**: una integración, podemos ir sobre los modelos conocidos, Cloud, ChatGPT, Gemini, Copilot, o sobre algún modelo que ustedes propios corran en sus servidores si así lo llegan a tener, o con agentes nuestros internos que por detrás usan APIs de Androvic. Yo ahí invito. Nosotros más allá de la migración, hemos aplicado esta solución en empresas grandes, se pueden decir con contrato, empresas grandes de Petro Argentina y Orden, y siempre la solución de BI es muy potente para lo que es toda la automatización de ingeniería de datos desde el lado del negocio, transformación y de IA. Así que más allá de la migración que entiendo, si ustedes ya tienen los reportes armados, también nos podríamos conectar a esos propios reportes para que los consuman de esta forma, porque agiliza mucho la parte del usuario final y encontrar bastante valor.

**Pedro Larghi**: Sí, yo creo que una de las cosas que más aporta José Manuel es en esta nueva dinámica de la IA, que los usuarios de negocio empiecen en lenguaje natural a pedir cosas y salirse de la caja, digamos, empezar a pedir otras cosas que si antes un área de sistema no me hacía el listado, el reporte no lo podía hacer. Acá es como que te doy todas las herramientas para que vos juegues y obtengas lo que quieras obtener. Y eso es un diferencial me parece con Telament.

**Lucio Rojas**: Ahí ya más allá de mi juventud que a veces apelo, pero antes trabajé en un equipo de ahí en otra empresa, y si, una parte técnica más una parte funcional, y a vos te solicitan reportes todo el tiempo porque el usuario de negocio no tiene la capacidad de autoconstruírselo. Por eso me llama a mí la atención esta solución, donde vos nada más le da un entorno gobernado por vos, donde armas el nivel de capas gold que sabes que puede consultar, que son los datos a los cuales podría tener acceso, ya se puede dar curados, pero que se auto reporte y se hagan los tableros self service también es una saga de un. Aquí tengo una carga importante para el equipo de que se puede dedicar a otras cosas. Acá también se pueden correr modelos predictivos, flujos de automatizaciones n para algunos procesos puntuales. Hemos trabajado mucho con automatizar procesos de reposición de stock en varias empresas, con reglas sobre los datos y sobre las bases de datos y que se disparen procesos que envían los mails, se ponen mucho que está haciendo reportes para el negocio.

**Pedro Larghi**: Claro, nosotros con Ferromex se está viendo desde el punto de vista de una migración estática, fría y ya, pero si fuera algo que constantemente puedo ir actualizando y generando nuevas acciones, se potencia aún más. Exactamente. José, quisieras, no sé cómo querés avanzar, quisieras que te podamos hacer algún tipo de orden de magnitud, presupuesto por orden de magnitud, para que tengas una idea de si está dentro de una alternativa válida para ti o no. Ya en esta etapa, digamos.

**Jose Ocampo**: Muy buena pregunta y no estoy listo para contestarte eso. ¿No te puedo decir, o sea, válido? Sí, sí es válido, Que ahorita estoy enfocado en eso. ¿No lo sé, o sea, yo ahorita estoy, uno, migración, Dos, las propuestas que ya les mencionaba de uso o innovación con inteligencia artificial, ahí lo podría estar metiendo? Sí, si es candidato, no lo sé. Me atrevo a decirte que sí. Y va a la par de muchas soluciones similares. Por ejemplo, es muy similar a Locker de Google, bueno, sí, de Google, y el, ¿Cómo se llama? Green Lake, no es Green Lake, ¿Cómo se llama su Data Lake? ¿Tiene Big Lake, Big Data, o no sé cómo se llama su solución, pero es el Locker, que Locker básicamente es esto en versión Gemini, otro compañero estaba revisando, o uno de AWS, vale?

**Lucio Rojas**: No es una solución única del mercado, nosotros generalmente competimos por precio, esto es relativamente más barato que otras soluciones. Y también estamos en constante descubrimiento de features. Ahora estamos yendo hacia los gráficos, hacia las alertas, dentro de poco para presentaciones también se puede armar en base a los datos. No estuve en la conversión anterior de por qué no se puede compartir los datos para actuar. Entiendo que debe ser por algún entorno de seguridad o de compartir los datos. Asimismo, a nosotros nos interesaría que lo prueben porque queremos que cuando está en la mano del usuario se ve distinto. Podemos ofrecerle una prueba de concepto acotada, gratuita sobre algunas tablas si les interesan, con NDI por medio, no tener el tema de traspaso de información como bloqueante. Y sepan que nosotros estamos con SOC Type 2, que es la norma de protección de datos de terceros a nivel internacional.

**Jose Ocampo**: ¿El proceso es legalmente decir que se va a hacer esto y armar un NDA entre las dos partes, pasar por un proceso de revisión de mi equipo legal? Si va por ahí, dame oportunidad de cuadrar. Pero sí, o sea, la respuesta, Pedro es no lo sé, pero sí hace sentido porque es una herramienta similar al resto.

**Pedro Larghi**: Sí, a ver, tal vez como resumen, yo te podría decir, José Manuel, podemos avanzar con un NDA. Por un lado, te ofrecemos el que el director tuyo lo pueda ver si tiene interés en estas iniciativas de IA que está llevando adelante, y la prueba de concepto como herramienta para sacarle el mayor jugo a esto y que lo puedan usar ahí cuando está en el uso es donde se le ve el valor, así que podemos avanzar en esa. Perdón, podemos avanzar en esas tres líneas si te parece. Todavía no, respecto de la propuesta económica hasta que se despeje o se ponga foco en si van a avanzar con una solución de este estilo.

**Lucio Rojas**: Nosotros tratamos de obviamente sumar cosas sobre la competencia para que haga sentido y ponemos mucho a disposición nuestros equipos de implementación para poder ayudar a encontrarle valor a la herramienta, damos el know hack, know how que traemos de otras implementaciones o que sabemos que funcionan, ayudamos a automatizar procesos, todo eso a criterio de la POC, así que si lo quieren tener ahí también como factor de decisión, lo ofrecemos.

**Franco Ferrero**: Creo que José Manuel estaba hablando de dos pasos que tenía que hacer, como lo que era el tema de la migración de los datos y después lo de la propuesta de IA. Creo que también un poco lo que ofrece Theramot es un poco de las dos soluciones, o sea, tanto lo que es la migración de datos con el conector a SAP SCI, eso en dos días se puede hacer, o sea, dos días digo, creo que siendo pesimista, pesimista es decir, ya en un día tenés la conexión a SAPCC, ya tenés tus datos migrados en Teramot y ya tenés la integración con IA a través del MCP, como que siento que también es una integración que engloba un montón de distintas funcionalidades que bueno, también si están buscando hoy en día hacer una migración de datos y además distintas implementaciones de IA para trabajar con los datos, creo que la verdad es un buen feed que tenemos nosotros.

**Pedro Larghi**: Bien, ¿Te parece entonces José Manuel, avanzar de esa manera, firmar un NDA y pensar si podemos poner una ventana para una prueba de concepto donde lo puedas usar?

**Jose Ocampo**: Sí, de acuerdo.

**Pedro Larghi**: Bueno, el NDA obviamente vamos a firmar el que ustedes nos manden porque es más fácil que nosotros le mandemos algo porque los legales Ferromex deben ser mucho más duros que los nuestros, así que te dejamos esa actividad a ti José, de conseguir el NDA y bueno, firmarlo de nuestro lado, no va a haber inconveniente.

**Jose Ocampo**: Yo creo que va a ser más sencillo si ustedes me mandan una versión

**Pedro Larghi**: así

**Jose Ocampo**: de todas maneras van a ver, ya sabes este punto, ¿No?

**Pedro Larghi**: Sí, sí, van a cambiar. Está bien, perfecto. Igual es una ND y tampoco es tan complejo, así que bueno, empecemos de esa manera a ver si podemos llegar a una prueba de concepto donde lo puedas ver. Sacándole el jugo tú. Te robo. José Manuel, un minutito más. Tema la migración, ya en HANA, ya hablando en HANA directamente, el tema de TDM Synthesizer ¿Es momentum o todavía no? El tema de Test Data Management, la migración de datos de producción, ambientes de mandantes 300 de testing para. ¿Te acordás ese punto? No tanto.

**Jose Ocampo**: Sí, sí, sí me acuerdo. De hecho es como los tengo a ustedes mapeados, visualizados y vislumbrados. Este. Sí, sí me acuerdo. Ahorita qué estamos haciendo, estamos haciendo la prueba y la generación de plantillas de carga de datos maestros, de datos iniciales. Justo estamos en ese punto. Obviamente estamos en un punto de escenarios de prueba y de. Permítame un segundo.

**Lucio Rojas**: Sí,

**Franco Ferrero**: Bueno, perdón, nosotros nos tenemos que bajar que tenemos otra reunión, así que les agradecemos mucho por el tiempo. Cuando termina José, lo saludamos siempre.

**Pedro Larghi**: Espérame, Franco, espérame un segundito así puedo cerrar con José Manuel este punto. Si quieres

**Lucio Rojas**: yo me quedo ahí.

**Pedro Larghi**: Dale, si querés te liberamos a ti, Franco. Gracias, Gracias Lucio, que te quedaste ahí. Lucio, te cuento. Nosotros el producto que vendemos es. No.
