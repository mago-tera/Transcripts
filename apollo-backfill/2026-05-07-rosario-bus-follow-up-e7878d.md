# Rosario Bus  - Follow up

**Fecha:** 2026-05-07T17:13:01.081+00:00  
**Duración:** ~50 min  
**Participantes:** Manuel Guillén <>, Lucio Rojas <lucio@teramot.com>, Caro <caro@brainstorm-labs.com>  
**Externos:** caro@brainstorm-labs.com  
**Apollo ID:** 69fcd3f95ffe790019e7878d

---

**Lucio Rojas**: Bueno, pongo acá el que graba las reuniones para mí, por si tenemos alguna. No sé si sacamos algún feed o algo para mejorar, llamemos fácil cambiarlo.

**Caro**: Sí, buenísimo, buenísimo, Lucio, bien vos, todo tranquilo.

**Lucio Rojas**: Pobre Manu, le estuve respondiendo los mensajes mientras estaba en reuniones toda esta semana, así que me de odiar.

**Caro**: Le contestate así todo, viste cuando uno contesta monosílabo.

**Lucio Rojas**: Sí, sí, aparte a veces me manda los mensajes y los leo y me quedan en visualización y él tiene el visto activado, así que se debe pensar que vamos a mil.

**Caro**: Pero bueno, lo importante es que respondes, hay voluntad.

**Lucio Rojas**: Bueno, bueno.

**Caro**: Lucio, ¿Viste algo de lo de Rosario Bus? ¿Viste que nos mandaron y nos volvieron a mandar? No, no volvieron a mandar, digamos, si bien al principio habían contado algo, ahora mandaron bien los datos.

**Lucio Rojas**: Claro, después de la reunión que escribí el mail para mandarles. Sí, mandamos el mail con lo que dijimos que íbamos a hacer. Sí, sí, estuve trabajando con eso. La idea era repasarlo. Yo lo que tenía entendido fue que el lunes Manuel me reenvió la cadena con los ex nuevos y con lo que ellos nos pidieron. Y estuve trabajando eso con Claude para llegar al prototipo que habíamos acordado. Y hablo con ustedes, si a ustedes les parece que está bien, avanzamos y si no le mejoramos algo.

**Caro**: Dale, Buenísimo, buenísimo, Lucio.

**Lucio Rojas**: Vamos a compartir. Pestaña pantalla. Compartí esta pestaña, la ventana de compartir. Así, así. Nos vemos en. ¿Estás viendo la pantalla?

**Caro**: Sí, estaba abriendo también los excel de

**Lucio Rojas**: ellos, pero

**Caro**: ahora nos vemos arriba y abajo.

**Lucio Rojas**: Si, yo ahí ya te veo más, creo, a vos, pero mientras vos estés viendo mi pantalla. Bueno, vamos a poco, vamos a hacer un repaso un poco primero de que era. Manu me había enviado esta pestaña, este hilo, que este es el mail que sacamos de la reunión. Por acá está que lo hicimos. Que bueno, él me mandó la reunión y armé esto. Y ellos mandaron distintos datos con pasajeros, sábanas, historiales de tarifa y demás. Y enviaron una guía del contexto. Esto es una línea, la línea 140, con banderas norte, sur y sur y norte. Y me mandaron datos de enero, abril, en el año pasado, abril de este año. Estas son las definiciones claves de qué

**Caro**: sábana para ellos muestra el cuadro. Sí. Abajo él estaba yendo.

**Lucio Rojas**: Diagrama de flujo con las unidades de negocio. Este diagrama de flujo. No dice mucho, en realidad no dice nada. Y nos explicaron qué tiene cada una de las tablas. Leímos eso.

**Caro**: Buenísimo.

**Lucio Rojas**: Esto es importante. No, pero no hace falta esto, porque. Lo hace solo.

**Caro**: Entiende solo.

**Lucio Rojas**: Está bueno para confirmar, no para que sepa que no se equivocó. Y nos pidieron siete cosas, como si fuese la tarea del cole. Analizar la curva de demanda para detectar picos, valles, cambios de tendencia en el tiempo. Identificar servicios y MV fuertes, coincidentes, MB, media vuelta. Detectar qué servicios de media vuelta absorben mayor o menor carga. Evaluar la frecuencia y la demanda. Detectar desbalances.

**Caro**: Como ver la curva, a ver si se siguen o no.

**Lucio Rojas**: Claro, en base a eso, detectar desbalances y evaluar impacto de cambios de horario. Después detectar patrones.

**Caro**: Ahí se puede hacer un simulado. En el último, cuando dice evaluar impacto de cambios de horario, por ahí se podría dejar un juego como diciendo la demanda es tu demanda, lo que vos podés cambiar es la oferta. Entonces que te diga, ponele que vos mirás la oferta versus demanda, y en algo no estás de acuerdo, y decís, bueno, voy a subir la demanda a las 8 de la mañana. Entonces que en algún lado te deje como jugar y decir, si subo dos colectivos, o pongo cinco colectivos más a las ocho de la mañana, y que te vuelva a graficar oferta. ¿Entendés? Oferta simulada versus demanda real.

**Lucio Rojas**: Sí, entiendo.

**Caro**: Bueno, se me ocurrió como idea, pero

**Lucio Rojas**: después vamos, está bueno. No estaba dentro de esto. Primero que ellos pidieron que nos habíamos puesto de acuerdo acá en armar un prototipo. ¿Por qué? Porque esto entiendo que todavía no es trabajo, sino que mostrémonos algo para.

**Caro**: Exactamente.

**Lucio Rojas**: Bien, bueno, vamos a generar un prototipo de sistema básico con las funcionalidades esenciales para poder mostrar cómo sería un análisis típico de interacción entre la oferta y la demanda, y la generación de un sistema de alertas ante algún comportamiento normal, para identificar oportunidades de mejora. Nosotros le dijimos que íbamos a hacer eso, le pedimos lo que necesitábamos, y ellos nos respondieron con otro pedido distinto, pero que sin embargo lo contemplé, porque no es mucho más que desmenuzar lo que nosotros dijimos. Nosotros dijimos, vamos a analizar la oferta y la demanda. Y yo bueno, si es amplio, hagámoslo así. Entonces, perfecto. ¿Bueno, ahora vamos a analizar un poco cómo fue que es el resultado y después te muestro cómo trabajé Y cómo quedó el prototipo? Bueno, el caso de uso definido para el prototipo Desde la línea 140, las banderas son las tres FFL y FLF, que son los sentidos, son las distintas paradas de los sentidos que lo recorren en días hábiles de la fecha que tiene el dataset y con fechas atípicas excluidas. Ellos mandaron un cuadro con fechas atípicas para que no las tengamos en cuenta porque iba a ensuciar el análisis yo como usuario.

**Caro**: Y fines de semana tampoco.

**Lucio Rojas**: No dice feriado, palos y eventos.

**Caro**: No, pero fíjate que es hábiles de luna abiertas y. Pero no sé si es un error porque justamente vos tenés que, o sea, ya sé que hoy la inteligencia artificial te lo detecta, pero no tienen que entrar en los promedios porque son casos distintos.

**Lucio Rojas**: No, yo iba a decir que para mí como usuario, yo tomo mucho el colectivo de esta gente, el que va San Nicolás, es un error que cometen porque nunca tienen en cuenta lo que pasa los feriados, es como que ellos dicen bueno los feriados no los contemplamos y los feriados son los días que más quilombos se arman con los colectivos.

**Caro**: Bueno, pero no se contemplan en los análisis, en este análisis de día, pero por supuesto que no tienen que ser boludo y lo tiene que contemplar, sino

**Lucio Rojas**: te digo que he estado en San Nicolás, el colectivo de ellos que es el Chapuí, que cuando hay un feriado es al revés, el día que vos más demanda tenés para el viaje interurbano, porque la gente se vuelve a su pueblo, te ponen menos frecuencia, o sea te ponen, si antes uno cada 15 no funcionaba, te ponen uno por hora y vos te comes fácil tres horas esperando colectivo. En realidad durante toda mi vida, siempre que iba a la facultad y a Business Intelligence y eso, yo quería resolver este problema puntual de este colectivo. Tengo la oportunidad, se los voy a decir, voy a decir.

**Caro**: Me parece muy bien,

**Lucio Rojas**: sigamos.

**Caro**: No puedo creer.

**Lucio Rojas**: Bueno, el análisis tiene siete etapas, que es lo que ellos nos pidieron. Tenemos el de la curva de la demanda, el de servicios y media vuelta, frecuencia versus demanda, desbalances, impactos de cambio horario, analizamos patrones y factores. Estamos Esto un poco más el trabajo que hice yo. Tomamos las bronce que nos mandaron ellos que son pasajeros cada 15 minutos, las sábanas de colectivos, los cambios de horario, las tarifas y las fechas especiales. Usamos el proceso de transformación de bronce a silver para sanitizarlos y creamos seis tablas gold para poder hacer los análisis y cruces relevantes, o sea que cada vez que ellos ahora nos actualizan la fuente de datos, este reporte se va a mantener estable, que no cambie más nada en su base o del reporte que quieran y armamos un dashboard para la visualización. Las tablas son estas, hay una tabla que es demanda línea 140, curva cada 15 minutos que analiza los pasajeros cada 15 minutos con tarifa vigente y semana del año. Esa tabla es esta. Tablas, Ejecutamos la query, vamos a ver la tabla te dice la bandera, te dice el día de la semana, la fecha, la franja, la hora, el importe, los pasajeros, pasajeros acumulados, semana del año, sentido de bandera, tarifa, bueno acá tiene para toda la semana y todos los pasajeros toma tres tablas de entrada de ellos que son las alertas de pasajeros cada 15, son los pasajeros cada 15 minutos, todo arranca por alertas porque yo le puse este nombre a la fuente de datos. Fechas especiales para el análisis, historial de las tarifas, acá tiene la descripción de qué tiene que tener cada tabla, esta tabla funcional de demanda de pasajeros cada 15 minutos, línea 140 en las dos banderas para los días hábiles de los periodos de enero abril de 2026 5 tiene que una sola línea por bandera y por colectivo, excluir fechas que aparezcan en las tablas vigentes, en las tablas de fechas especial. Así describió todo lo que tiene que tener y armó el SQL así Tenemos seis tablas que tienen todas son un poco las que explica acá,

**Manuel Guillén**: las que

**Lucio Rojas**: se hicieron y son las seis, las mismas están acá. Te voy a pedir tu mail para darte acceso a esto, Yo soy hermano y el tuyo es caro, Está acá en estudio de datos. ¿Estas son todas las que cargamos, que además cuando la mandaron fue por ejemplo, si ves acá la de las sábanas cuál es, tiene 32 tablas, OK? ¿Estas tablas no se pueden cargar directamente así como está el excel, porque solamente te lee la primera, entonces lo que tuve que hacer fue separar una por una como CCB para poder cargarla,

**Caro**: OK?

**Lucio Rojas**: Así que nada, buenísimo.

**Caro**: Igual en esta parte de tablas y el armado yo no haría tanto hincapié porque es más nuestro back, ellos aspiran, o sea nosotros tenemos que insistir en que se conecten directamente a su base de datos y que esto no lo tengan que hacer ni ellos ni nosotros.

**Lucio Rojas**: Claro, pero nada, como dato de color. Igualmente no lo hice yo me hice una gente que haga eso, pero hacerlo malo sería bastante tedioso, me hubiese llevado varias horas. Agarró una gente que le expliqué lo que tenía que hacer y lo hizo por mí mientras hacía otra cosa. Bueno, esta es la tabla principal, cruce oferta demanda, que acá te cruza toda la parte de la oferta con la demanda justamente. Y es la que más se basa el análisis, que es la primera. SQL bastante compleja. Y esto quizá lo sacaría porque no añade mucho a la diapositiva anterior.

**Caro**: No, para mí es muy técnico y en realidad ellos les importa más saber qué. Qué info tomamos y empezar a ver. Esto me gusta mucho más.

**Lucio Rojas**: Para mí, si no explicás esto, se corre el riesgo de que no vean el trabajo que hay atrás y no perciban el valor.

**Caro**: Bueno, puede ser, está bien, pero como más conceptual que el detalle de cómo la hizo. Si, no, como que. Bueno, nosotros te armamos aceitábl, no nos pasaste la info así. Así la llevamos nosotros contéramos.

**Lucio Rojas**: Esto lo preparé yo para mostrárselo a ustedes. Para mostrárselo a ellos. Es para acá primero verlo que estás haciendo.

**Caro**: Está buenísimo para mí.

**Lucio Rojas**: Esto es lo que vos hiciste.

**Caro**: Yo lo mostraría. Sí, sí, sí.

**Lucio Rojas**: Después editamos la otra para. Hacemos una pensando en ello. Esto yo hice para ponerlo ustedes en el mismo plano de lo que ya hice, así lo podemos seguir. Bien, ahora, esto es una app, no un reporte. ¿Por qué? Porque ellos dijeron que no querían tener, me quedó la frase en la cabeza, cosas sueltas que no se actualicen, sino que querían tener algo estático. En sí lo que vamos a mostrar es algo suelto, porque es un artefacto publicado disfrazado de app, pero es un pretotivo, porque se pide un pretotivo. Hacer la app llevaría esfuerzo que no estarían dentro del scope. Entonces yo mostraría el prototipo y si les gusta, lo construimos.

**Caro**: Me encanta. Mirá qué bueno.

**Lucio Rojas**: Esto lo quiero leer con vos porque me sirve a mí tampoco lo pude leerme todavía, pero te dice qué nos pidieron ellos, cómo lo resolvimos y qué datos tienen, y después lo podemos leer. Bien, el análisis del reporte. Así que ellos pidieron detectar cambios en la demanda y picos y valles, sin elegir los periodos a mano. Nosotros hicimos un promedio diario, por mes y por franja en ambos sentidos en paralelo con las fechas atípicas excluidas en el reporte de curva de la demanda, y para eso usamos los datos de esta tabla. Después nos pidieron identificar servicios fuertes o ineficientes a lo largo del día, lo resolvimos con cada servicio cruzado con la franja horaria, separando el problema del servicio del problema de la franja. ¿Y bueno, acá te dice cuál servicio tiene alguna ineficiencia, baja, aceptable o crítica,

**Caro**: para entender un poco lo que está mostrando ahí, que en la franja de 0 a 6 de la mañana hay pocos pasajeros por media vuelta, sería eso?

**Lucio Rojas**: Sí, o son servicios subutilizados con su franja.

**Caro**: Sí, mi única duda es, para mí, acá no se ven. Si, ellos nos aclararon que con la noche, la noche es un commodity que tienen que dar, entonces ya saben, pero la noche por una cuestión de compromiso con el Estado, no pueden bajar la frecuencia, igual no importa. Y después lo que no entiendo es si acá no te falta cantidad de servicios, porque no entiendo qué servicio, un 17 14 15, porque me llama la atención que por ejemplo de 19 a 24 te ponen 29,1, como que es el estado es bajo y 25, O sea, no entiendo por qué 25 9 es aceptable y 24 es mejor que 25.9. OK, como que no lo estoy entendiendo

**Lucio Rojas**: con este ratio, con la MBS media vuelta yo tampoco analicé bien el. Sí, sí, por eso fue más que trabajé en esto, en construir las tablas y el gráfico en sí es lo que quería que validemos.

**Caro**: Y vos fuiste muy rápido con la slide anterior que yo me quedé. Yo no te quería hacer una pregunta

**Lucio Rojas**: que la quería rápido, porque después podemos ir a la aplicación y leerlos bien de entendimiento, o sea, yo estoy haciendo mapeo de qué es lo que hicimos, qué reportes hay y por qué está, por qué ellos no lo pidieron, y después nos paramos a ver cada uno y decimos, bueno, hay que mejorar esto, esto y lo otro.

**Caro**: OK, pero para que te quiero preguntar algo del primero, igual ya sé que es rápido, pero en la curva de la demanda, porque está bien ese gráfico, pero es mensual, y yo entiendo que ellos mensual no les dice mucho, porque ellos analizan la, o sea, de hecho piden qué piden detectar cambios en la demanda, picos y valles, no tendría que independientemente de eso, ver cada 15 minutos. ¿Como que el promedio cada 15 minutos? Porque si no, no les dice nada, o sea, sí ellos saben que en enero no laburan porque no hay colegios. Claro, yo entiendo que la curva de la demanda que ellos quieren hablar, que ellos quieren analizar, es así lo entendí yo, por eso te pregunto, cada 15 minutos ver la demanda cada 15 minutos para entonces saber. Estoy pensando, pero puede ser que a lo largo, no sé si es un cuadro de doble entrada, ¿Entendés? Porque vos necesitas ver cada 15 minutos y tenés mucho baja demanda. A ver, vamos a la primera pregunta. ¿El objetivo es cruzar información y detectar sobreoferta, analizar la curva de la demanda? Sí, cada quince minutos.

**Lucio Rojas**: ¿Como que no, se llama tabla? Sí, cada 15 minutos.

**Caro**: ¿Sí, pero por todo lo que yo vengo escuchando con ellos, o sea, el primer gráfico está bien, pero no les habla para nada de lo que ellos quieren ver, o sea, digo, para sumarlo en el prototipo, ese gráfico lo podemos dejar, pero sí o sí sumaría un gráfico de cada 15 minutos, que puede ser por trimestre, ponele, o algo así, que ellos puedan elegir igual, pero entendés? Y que vos tengas la hora del día, entonces vos digas, no sé que tenés que elegir la fecha, fechas y bueno, en estos tres meses quiero ver y vos ves los promedios de cuánta gente Hay a las 8, a las 8 y cuarto, a las 9, porque yo entendí que esa es la forma que ellos quieren analizar para saber si a las 8 y cuarto tienen que poner más bondis. Bien, esto más como una evolución mensual que habla, pero que ya se la saben. Ya se la saben, claro. Ves por ahí tu segundo gráfico, a ver este, ves este

**Lucio Rojas**: Y eso por franja horaria.

**Caro**: Bueno, sí, por franja no, ellos lo quieren cada 15, yo lo dibujaría cada 15 y no sé si le tenés que dejar la posibilidad de elegir fechas, ¿Entendés? Tipo fecha inicio, fecha inicio, fecha fin, porque a veces lo van a querer ver en dos meses, a veces lo van a quere ver en seis, a veces te van a decir, no sé, no quieren ver enero porque ya saben que baja.

**Lucio Rojas**: El tema, vamos a pedir la clot, ¿Me podés armar un gráfico, analiza si escribe con C o con Z, no importa? En 15 minutos la demanda filtrada por fecha es importante, pero eso ya lo ven ellos, es importante ver cómo varía, cómo varía de una fecha a otra, Porque ellos ya tienen, cómo está distribuida cada 15 días, es lo mismo que ven ellos, si lo que nos mandaron, si no sería graficarle lo que ya tiene.

**Caro**: Bueno, o sí está bien lo que vos decís, o la otra sea que les deje elegir dos, como diciendo cómo era antes. Ponele que vos elegís, ponele que arranca el año, decir, bueno, de marzo a abril y quiero ver si hubo cambios. Entonces que también te grafique sobre el mismo gráfico, en dos colores, la de mayo y junio. Entonces vos te vas dando cuenta, che, mirá qué cambió respecto a marzo,

**Lucio Rojas**: está bien. Lo que ellos. Su pedido tampoco es. A mí la sensación de que ellos tampoco, bueno, acá no dijeron lo que quieren, pero que tampoco lo tenía muy claro. El otro día como que los pusieron en una reunión, sus jefes, a decir que teníamos que trabajar con nosotros y estaban viendo qué podían resolver sin ser muy explícito. Entonces tampoco es fácil.

**Caro**: No, no, por eso no es fácil. Pero yo también, digamos, yo me. Que por lo menos lo que yo tomé de la primera reunión, sobre todo con las chicas, la primera que tuvimos más con jefes, era esto. Como que el gran monitoreo que ellos ven estaba 15 minutos y quieren detectar, viste, esto que yo decía, cuando la demanda no sigue la oferta. Cuando la oferta no sigue la demanda, qué cosas pueden cambiar. Como que para mí ese es el desafío grande que ellos tienen. Después tienen que terminar de pensarlo cómo.

**Lucio Rojas**: Mira, mientras arma este, revisemos todo el dashboard.

**Caro**: ¿Dale? Sí, perfecto.

**Lucio Rojas**: Nos corremos de acá. Esto ya voy a mostrarte nada más cómo iba, cómo fui armando el trabajo y cómo llegamos al dashboard. Ahora lo miramos y vemos que puede pasar, porque tiene bastante más cosas qué tiene. La idea es, primero la parte de alertas. Dos tipos de una operativa y una estructural. Las alertas operativas, acá estamos simulando que estos están en producción, tenemos datos hasta abril. Entonces dice, bueno, yo tengo datos hasta esta fecha, la semana próxima, al último dato mío, ya tendría que estar haciendo esto para armar una buena planificación más óptima. Acá ya hay un problema, que yo no tenía esa información, que era un commodity lo de anoche. Me dice, tendrías que reasignar tres salidas de noche a mediodía, pasar de trece a diez salidas en la franja de diecinueve a veinticuatro horas, y de once, catorce salidas en la franja de once a catorce horas. Hacer un cambio cuantitativo de esos colectivos, porque tenés una subutilización a la noche y una sobre una falta de colectivos a la mañana. Entonces te dice, bueno, el impacto esperado es reducir el banking al mediodía, que tenés un desbalance promedio de 27 pasajeros entre coches sin agregar. Yo creo que esto entendían bien eso.

**Caro**: Igual mostrémoslo porque está bien, ellos después tienen que entender que le van a tener que cargar las reglas del negocio.

**Lucio Rojas**: Sí, claro, seguir tirándolo. Bueno, ¿Qué otra cosa le pide o le propone? Reducir la oferta nocturna en la bandera SN con una liberación de cinco turnos nocturnos recuperables como esfuerzo mediodía o reducción de costo operativo. Esto habría que ver hasta dónde se puede reducir. Eliminar el tramo nocturno del servicio s. Bueno, esto tampoco no es hace mucho.

**Caro**: En la noche que sí,

**Lucio Rojas**: eso habría que cargarlo, pero no lo han escrito en los datos, porque si no lo hubiésemos. No, que no creo que haya estado implícito.

**Caro**: No, no, lo dijeron en una reunión cuando nos pusieron contexto. No, no, no teníamos por qué saberlo, o sea, Manu y yo. Sí o no, porque no se dijo después.

**Manuel Guillén**: Buenas, Estoy con camarita apagada, pero estoy. Perdonen la demora, estoy con la gordita en brazo.

**Lucio Rojas**: Dale Manu, disculpe.

**Caro**: No pasa nada.

**Lucio Rojas**: Bueno, y Después te pide dos más. Activar protocolo post aumento tarifario. Han pasado 90 días desde el aumento del 23 de febrero. Revisar la curva del último mes y validar si la demanda se recuperó al nivel pre aumento. Por qué en el momento anterior coincidió con una caída sostenida del 39% en cuatro meses, sin medición formal aún. Decisión informada. Si la curva no se recuperó, considerar reducción adicional de oferta. Eso es inteligente, o sea, te dice que con los aumentos suele haber un patrón de que cae la demanda, de que baja.

**Caro**: Bueno, es algo re interesante que probablemente no sé ni si saben.

**Lucio Rojas**: Después tenemos alertas. Estas son operativas, estas son más estructurales, no hace falta responderlas hoy, que tenés una simetría sostenida entre sentidos. Este sentido que es el FLF supera al FFL en 11-16 meses, con un delta promedio de 95 pasajeros extra por día. Y la sábana programa una oferta casi

**Caro**: simétrica, lo que pasa que el que va vuelve. No sé si quieren forma. Es estructural como vos decís, no lo sé, ¿Entendés?

**Lucio Rojas**: Claro, vos decís que el que vaya vuelve y no tiene que volver. No tendrán dos puntos, Tienen dos puntos,

**Caro**: pero va por un lado y vuelve por el otro, no sé cuánto tiempo ahorra si vuelve derecho, ¿Entendés?

**Lucio Rojas**: No entiendo.

**Caro**: Yo entiendo. Por ejemplo, a la mañana muchos colectivos van al centro porque la gente va a laburar al centro, entonces todos esos colectivos van lleno y ponele que en una línea le pones 10 bondi de 8 a 9 y después vuelven todo vacío, nadie vuelve, pero el colectivo ya está en la calle, no podés hacer que vengan 10 y que no vuelvan. Pero no sé, capaz que te dicen sí, si vuelve en línea recta, en vez de demorar una hora, demora media hora y ya te sirve para volver a hacer el recorrido. Conocimiento que no tenemos.

**Manuel Guillén**: Además pasajero que va, vuelve. Ojo, porque en realidad hay personas que tienen distintas opciones de bondi para ir al mismo lugar, no te tomas el mismo por Santa Fe hay 200 colectivos que van tomando en línea recta hasta el mismo lugar y tomar cualquiera, eso suele pasar. No te digo todo, pero

**Lucio Rojas**: bueno, entendiendo esto, son más alertas estructurales, por ejemplo, hay cambios de horarios reactivos y otros estacionales, 8 cambios de 6 meses, varios respuestas a caídas que ya estaban en marcha, la oferta no se ajusta hasta que la caída es grande, con una inercia de dos, tres meses después del cambio te sugiere sistematizar tres horarios estacionales fijos. Son todas alertas que toma, que Claude define en base a la información que analizamos.

**Manuel Guillén**: Pero para, para. Una cosita importante, una cosa que para mí fallamos en transmitir en la reunión anterior. Voy a poner la cámara un segundo. OK. Una cosa que para mí fallamos el otro día, no scrolleemos rápido y demos por sentado, porque nosotros lo leímos, o sea, si está puesto en la pantalla lo tenemos que poder explicar y defender, si no, no lo pongamos, ¿Me explico? Porque el otro día es como que le quería. ¿Y también pasó con lo de Fabri en el consejo, o sea, lo que mostremos Tiene que ser 100% argumentado y defendible, si no me explico lo que digo? ¿Como que no lo pasemos? Bueno, va tirando cambio reactivo, no mostremos y digámoslo

**Lucio Rojas**: porque tiene sentido,

**Caro**: pero bueno, yo mostraría más lo práctico que el back, que eso es lo que yo elegí a Lucio. Independientemente que uno hace un raconto de esto, dice así se crearon estas tablas, yo creo que lo más importante es esto, que es a lo que van a tener acceso al día siguiente que es la herramienta que van a tener.

**Lucio Rojas**: Claro, yo. Porque son miradas distintas. ¿Vos Manu decís, bueno, si pone un dato lo tenés que mostrar, pero por otro lado, yo cómo puedo hacer para poner un dato que está bien sin haber tenido la reunión previa la información? Entonces yo estoy como más centrado en mostrarte a vos la herramienta. Está bien que el tipo del otro lado está esperando ver un dato. Entonces no es fácil junta esas dos puntas. No sé cómo lo podemos. Si se entiende lo que yo quiero decir.

**Caro**: ¿Qué quisiste decir? Conjuntar las dos puntas.

**Lucio Rojas**: Yo lo que estoy queriendo tratar de mostrarle a ellos ustedes, es la herramienta de lo que se puede construir. Porque si yo ya tuviese armado algo definitivo, que es defendible, que es congruente, que tiene sentido, no estaría en una reunión previa a presentar un proyecto, estaría en una reunión de cierre de proyecto y ahí sí lo podemos hacer. Yo lo que tengo que mostrarte es, tengo una herramienta que puedo hacer esto, no importa qué hizo, me interesa que veas cómo lo hace, vamos a trabajar en que esto quede bien hecho.

**Manuel Guillén**: Bueno, expliquémoslo de esa manera al inicio de la reunión, porque el otro día no lo explicamos así y hubo una expectativa que se frustró. Eso es lo que digo.

**Caro**: Para mí está bueno igual el comentario de Lucio, como diciendo, no importa si los cálculos están perfectos, yo te demuestro un esqueleto de lo que se puede hacer, pero el cómo está bien, por eso para mí es mucho más importante el qué el cómo forma parte, pero no entraría en detalle técnico.

**Lucio Rojas**: OK, lo decía con los dos puntos.

**Manuel Guillén**: No sé, yo lo que digo es que no nos pase lo de la otra vez. ¿Perdón, sí, pero digo, no tenemos muchas balas con la gente, viste? Y eso como que tengo un problema de que esto sea un display de algo que sabemos que no está cerrado y que lo digamos así. Pero expliquémoslo al inicio como para que ellos no esperen encontrar un análisis de interacción entre oferta y demanda acabado, sino la potencialidad de una herramienta que tenemos que aceptar el mecanismo de análisis.

**Lucio Rojas**: Bien, lo que pasa, yo he entendido que ese era el contexto ya de la reunión, no me imaginé que podía ser ya presentar algo final. Por eso dije lo de las dos puntas, porque desde el punto de vista, la perspectiva de las dos personas que nos escucharon, son dos chicas que están hasta las manos de laburo y que son especialistas en datos de su empresa, Entonces si vos la sentás a mostrarle algo, probablemente quieran ver un dato que está bien, no sé si puede hacer el ejercicio de darse cuenta que alguien está mostrando una herramienta que puede hacer algo y resolverlo, pero que todavía no está resuelto. Es como que para mí son. Pensando en el dato.

**Caro**: Sí, bueno, está bárbaro lo que vos decís Lucio, para que lo podamos explicar. Miren, esto hay que validarlo, hay que conectarlo a la base de datos, esto es un inicio de los cálculos, o sea, usted piénselo como general, no importa después el número, el número si les interesa que se calcule estas cosas, después afinamos el cálculo, pero hoy nos tenemos que poner de acuerdo en qué quieren que se calcule, en qué gráficos quieren ver, después si el proyecto avanza, afinamos a que el gráfico salga bien.

**Lucio Rojas**: Es lo mismo que pasó en la municipalidad, o sea. Yo estoy de acuerdo con vos, Manu, yo por decirlo así, me termina temblando cuando hago una pregunta y sé que el dato que me va a dar va a estar mal, pero es lógico, porque tendría que trabajarlo para que dé bien, si no, no tendría trabajo, pero tengo que mostrar al tipo de la herramienta, tiene que estar bien planteada el marco de la reunión, porque el tipo para mí que fue el otro día a verlo, que era el concejal, pueda ver que lo que teníamos esté andando y me miraba y me leía lo que estaba diciendo, que yo lo entiendo, él capaz que nosotros tenemos que. Ese ejercicio de plantear bien las reuniones,

**Manuel Guillén**: Yo soy muy autocrítico, pero porque por de obsesivo, no estoy diciendo que estemos mal encaminados, lo digo nomás porque viste, como que la gente ya de por sí una inversión, un cambio en la cultura, organización, guita, tiempo, te da bolas que un lugar, viste, como que Caro nos pasó con el otro cliente. Bueno, no es difícil, solo digo eso, como que construyamos el discurso, me parece perfecto, la herramienta me encanta, lo que estamos, lo que podemos mostrar, me pareció bien, no sé si vieron algo más ustedes, pero igual a mí me interesaba sobre todo que lo vea Caro, porque ella tiene la cabeza más ingenieril que

**Lucio Rojas**: yo, obviamente ahí primero para cerrar la anterior. Está bien Manu, que te ponga buena posición y nos digan chicos, hicimos mal esto, esto, el proyecto se plantea distinto. Porque si no, creo que es donde entra el sentido de lo que ustedes pueden aportar de valor sobre nosotros. ¿Porque ahí es donde hace sentido la relación, decirle bueno, yo voy, hago algo con la herramienta, ustedes plantean un proyecto, lo presentan, lo venden bien, que es lo que fallamos nosotros antes? Por eso tiene sentido que entren a ustedes. Entonces está bien esa posición yo la acepto y bienvenido de ese lado. Bueno, siguiendo con lo otro, Manu, lo que veíamos recap rápido, lo que habíamos explicado con Caro era que de las tablas que nos pasaron ellos, las cargamos a Theramot y generamos con Claude, entendiendo lo que ellos nos habían pedido y lo que nosotros habíamos prometido, el marco para analizarlo. Y ese marco son seis tablas gold que cruzan las tablas de ellos que nos pasaron. Son estas seis que están acá para poder generar los análisis. Los datos para poder generar los análisis ya están. Entonces. Entonces vos le preguntás a Claude sobre algo de lo que está acá, te debería poder responder lo que todavía no está trabajado. Que es lo que está bien que vos advertís rápido. Es cómo se le pregunta o qué se le pregunta, o hacer hincapié en el detalle. Yo por ejemplo, recién le mostré este dashboard a Caro y Caro me dice, no Lucio, pero fíjate que ellos querían verlo cada 15 minutos, no una evaluación del promedio diario mensual. Entonces yo digo, Caro, tenés razón, yo me preocupé más en que le podamos hacer esa pregunta a los datos, que el dato en sí. Se lo hice de vuelta la pregunta ¿Y qué pasó?

**Manuel Guillén**: Y te quedaste sin token justo.

**Lucio Rojas**: Y me Quedé sin token 4.7 desde las 12 del mediodía. Pero vamos a hacer que siga para que me responda bien.

**Manuel Guillén**: ¿Le pediste ahora cada 15 minutos esto?

**Lucio Rojas**: Ah, claro, le pedí el corte cada 15 minutos. Rápidamente armamos siete marcos de reporte en base a lo que ellos nos pidieron, que eran los 7 puntos. Cada uno de estos análisis que hay, que hay que trabajarlos, responden a una de sus solicitudes. Ahora hay que ver que lo que respondió y que lo que pidieron tenga sentido.

**Caro**: Eso no todavía, que eso es lo que estábamos viendo. Servicio A ver, yo quiero ver bien ese word donde decía los comentarios,

**Manuel Guillén**: el análisis requerido. Caro creo que al final.

**Lucio Rojas**: Sí, sí, Casi está.

**Caro**: Porque estoy en el meizo. Sí analizar la curva, identificar servicios, me da bajas fuertes o ineficientes. Mi única duda es que Claude te lo hizo como franja horaria de seis horas. Viste que Claude lo dividió, no sé si cada tres o cada seis.

**Lucio Rojas**: La primera cada seis y después cada tres. Es como que todo, yo creo.

**Caro**: Por ejemplo. Sí, igual la noche, como te digo, la noche no me gusta mucho. Si se puede por ejemplo de 6 de la mañana a 19 o a 20 o a 21, para que sea 40. De 6 a 21 lo abriría por hora.

**Lucio Rojas**: OK.

**Manuel Guillén**: Si, está bueno porque la alargada de los bondi creo que es a las seis, a las cinco y media la hacen por ahí, así que el corte de iniciarlo a las 6 está perfecto.

**Lucio Rojas**: Bueno, acá también Manu, para hacer un repaso del trabajo, hay otro canal. Ah, vos estabas donde hay alertas más operativas y análisis por cada una de las cosas que nos pidieron ellos. Otra cosa que se puede hacer, pero lo harco porque es un poco tipo, pero se puede hacer, es meterle acá un chat de IA que haga preguntas sobre por qué esos datos son así, o que analice estos datos. Esto se usa una API key de Antropic, que es como meterle clot adentro de su aplicación para que ellos le pregunten, por ejemplo, bueno, el servicio más vacío. Y le respondería en base a los datos para.

**Manuel Guillén**: Y le podés preguntar otra cosa fuera de eso.

**Lucio Rojas**: Ahora no, porque como dije recién, esto es un HTML, entonces quiero mostrar que se puede hacer esto. Claro, está ni siquiera local, o sea tiene. Le cargué preguntas y le cargué respuestas realidad. Entonces si yo le pregunto alguno de estos de acá, por ejemplo, dame un resumen de la línea, me lo devuelve, pero porque ya está cargado el resumen de la línea.

**Manuel Guillén**: Potencialmente esto podría integrarse contra los bases de datos.

**Lucio Rojas**: Sí, como un chat, como un modelo de COSO de cloud, que te responde, es como si preguntara acá a los datos, le pregunto acá, esto lo podemos agregar. Y que sea especialista sobre estos dashboard que tenemos acá. Entonces le puede responder, por ejemplo, si alguien le pregunta qué es NS, en el sentido, bueno, te responde por qué el análisis biocrítico, Bueno, te responde qué hacer en base a esta alerta que me dice que

**Manuel Guillén**: eso está bárbaro. Me encanta. Eso tiene revalor para mí.

**Lucio Rojas**: Si, yo justo lo agregué porque sentía que me faltaba cuando lo estaba leyendo yo no lo entendía, dije me haría bien uno de estos acá. Bueno, vuelvo a la pantalla y dejo de compartir, así los veo. Esto me lo pasaste el lunes, yo pude empezar a trabajar el martes a la noche, un poco ayer y un poco más hoy. Ya está cargado Teleamot, ya está generado los reportes y ya se puede iterar esto. La forma de como hizo recién, claro que se sentó, lo miró, conoce más el tema que yo, me dice incluso no tiene sentido hacerlo por día, vamos a hacerlo cada 15 minutos. OK, creo que hay tres opciones, hacer eso o lo hacemos entre o lo hacen ustedes o lo hago yo, pero equivocándome, o lo hacemos en conjunto con ellas primero habiéndole planteado el esquema, pero el tema que para eso tendríamos que tener el trabajo vendido y no sé si lo tenemos.

**Caro**: Yo en conjunto con ella no lo haría para mí. Yo ahí difiero, yo creo que lo afinaría un poquito entre nosotros, que no sé si quieren lo cerramos ahora o vemos un poquito más, pero yo lo afinaría y le iría a mostrar algo y si les interesa, se labura, se define bien cada cosa. ¿Pero como plantear una sesión de trabajo cuando no nos contrataron? No, porque perdemos tiempo nosotros sí, obviamente que nos digan, pero no me pondría a laburar en vivo porque pierden tiempo, porque no es la expectativa, nosotros estamos tratando de vender algo, tenemos que ser más concretos. Después si nos compran, sí por ahí se toda una reunión de trabajo, necesitamos

**Manuel Guillén**: una hora de hacer pruebas, nos comprometimos con ella a mostrar una demo que integre la otra parte de los datos que nos faltaban. Eso es lo que tenemos que mostrarle y listo, y decirle todo el speech que hablamos antes y ahí sí les parece que está bueno, que tiene potencial de laburo para ustedes, sí no, sí listo, les parece, le pasamos una cotización con todo esto, con las iteraciones, con el desarrollo, con el mantenimiento, si no lo pueden hacer ellos, etc. El costo de Téramo y todo bien,

**Lucio Rojas**: eso hay que venir.

**Manuel Guillén**: Yo no haría ahora, Caro, ahora en este momento, para mí lo ideal sería que lo vea vos Caro, que te tome un rato en algún momento y que lo mires tranquila y que le tires a Lucio lo que te parece lo que te parezca que hay que refinar y que él labura hasta el miércoles ponele, porque vos no estás hasta el miércoles. Planteamos la reunión para el miércoles.

**Caro**: Bueno, eso iba a preguntar por eso, para ver cómo seguimos. Yo si quieren con gusto me siento tranquila con el Word este, o sea quiero ponerle eso detalle a que la pregunta coincida con lo que mostramos, o sea que lo que mostró, aunque sea con poco dato, pero coherente con las preguntas. Yo me llevo esa tarea y se lo pasó a Lucio. ¿Cuándo quieren reunión? ¿Vos querés Manu, que esté yo

**Manuel Guillén**: y con ella? Sí. ¿Vos vas a querer verlo antes de reunirte con ellas?

**Caro**: No, yo lo voy a mirar hoy mismo, yo lo voy a la tardecita lo miro. Sí. Lucio, te pido si podés hacer vos los cambio porque no sé, yo ahí quise entrar a Theramo, ya no me entra, o sea yo ahora lo miro y le respondo a Lucio si les parece.

**Manuel Guillén**: Sí.

**Caro**: Y planteamos este.

**Manuel Guillén**: Para tu regreso.

**Caro**: Planteamos para mi regreso.

**Manuel Guillén**: ¿Tenés que estar vos Caro en esta reunión porque necesita cabeza de proceso, viste?

**Caro**: Bien,

**Lucio Rojas**: ¿Con las chicas que tuvimos el otro día o con alguien un poco más arriba?

**Caro**: Yo trataría de ir primero.

**Manuel Guillén**: ¿Tratarías de ir?

**Caro**: Si, Re no poder verle las caras, no me gustó para nada. Yo trataría de. Rarísimo.

**Lucio Rojas**: Está bien, hay que decirlo, si no lo decimos.

**Manuel Guillén**: Yo me llevo esa tarea. Yo me llevo la tarea de la logística de la reunión y como de cranear todo eso y ponerle fecha, organizar con ustedes y listo.

**Caro**: Yo en la reunión la semana que viene.

**Manuel Guillén**: Sí, al final sí.

**Lucio Rojas**: Yo pondré uno arriba, Manu, A uno arriba de ellos. Yo pondría uno arriba de ellos para que vean lo que. La potencia de la herramienta, porque para mí mostrarse a los otros es como mostrarle lo que va a reemplazar su trabajo, porque en teoría yo tendría que estar haciendo esos reportes, analizando esos reportes, para mí esto tiene más valor para el que toma la decisión o para el que quiere hacer que mejore su negocio y tiene que tener la validación del trabajo que ella también nos pidieron el trabajo que tenían que hacer, entonces está bueno,

**Manuel Guillén**: yo me ocupo de eso.

**Lucio Rojas**: No sé si están de acuerdo. Lo estaba planteando como lo que nosotros vemos de esto tantas veces, cómo que

**Caro**: no entendí tu comentario. Que no lo querés mostrar para arriba.

**Lucio Rojas**: No, al contrario que vos abajo lo validás, como decir necesito esto y está bien, me sirve, pero este de acá abajo nunca va a llegar a una decisión de byte arriba, Vea que le sirve a él lo que vos vas a hacer. El de abajo en realidad es más un compañero de trabajo nuestro, no,

**Manuel Guillén**: yo me llevo esa tarea.

**Caro**: Coincido, dale. Yo Imanu, te puse agenda posible el

**Lucio Rojas**: miércoles, a ver si coincidimos ahí Caro, estaría buenísimo. Bueno, me tomo dos, tres minutos más reuniones internas. Si yo te puedo pasar a vos, no sé cuánto te podés querés dedicar, pero si yo te puedo pasar a vos la conversación mía del cloud o un prompt que la retome y te doy el acceso al MCP de Tenode para que vos puedas instalar solamente, directamente el dashboard y no solamente hacer un análisis. ¿Te vendría mejor o preferís mirarlo, decirme mira Lucio, cambia esto y yo te lo vuelvo a mostrar?

**Caro**: Mirá, en situación normal no tendría ningún problema en hacerlo yo, pero tengo un problema que en realidad yo no estoy, de mañana al martes no estoy, Entonces la verdad que hoy tengo que viajar a Buenos Aires, luego hacer el celular en la ruta y si no te jode esta vez te paso y literal voy y la próxima sí me lo llevo y lo hago yo. Lo que pasa que yo ahora no los quiero clavar y no tengo mucha opción de hacerlo. Si fuese que te digo, si lo puedo hacer mañana a la mañana, lo hago en la mañana en la computadora,

**Lucio Rojas**: pero no, para saber cómo trabajarlo, hacemos así, dame un buen feedback, yo voy a terminar pasando a Clor y pasándote, poniendo un poco de mi cabeza por ahí, si algo necesito, que veo y después pasándotelo de vuelta y así lo vas mirando desde el celu, me va

**Caro**: diciendo sí igual no te voy a volver loco, no te preocupes, yo le doy una mirada profunda hoy y ya te mando todo.

**Lucio Rojas**: Para mí el trabajo era más lo otro era más entender las tablas, armar las gomas, mostrárselo a ustedes y tirarlo. Es el último 10%, no tiene sentido frenar ahora. Bueno,

**Caro**: Buenísimo Lucio, mil, mil gracias por tu tiempo, quedó muy bueno.

**Lucio Rojas**: Me bajo yo Manu saco mi record así si ustedes quieren hablar entre ustedes no se les meta.

**Caro**: Tranqui, así no te clavas con la interna, mi amor. Esa gordita la tengo que conocer, Manu.

**Lucio Rojas**: Bueno, no la Puedo sacar, no pasa

**Caro**: nada, yo sí ahí lo saco.

**Lucio Rojas**: ¿Vos lo podés sacar? Bueno, échalo. Yo uso este para después pasarle la transcripción a Claude.
