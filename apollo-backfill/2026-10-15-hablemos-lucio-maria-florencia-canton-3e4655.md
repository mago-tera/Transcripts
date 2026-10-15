# Hablemos !  Lucio  (María Florencia Canton)

**Fecha:** 2026-10-15T13:09:08.280+00:00  
**Duracion:** ~87 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Canton Florencia <mariaflorencia.canton@crowe.com.ar>  
**Externos:** mariaflorencia.canton@crowe.com.ar  
**Apollo ID:** 6ad0e4d5655933001c3e4655

---

**Lucio Rojas**: Después te lo comparto. Están existiendo, esto para terminar, yo de entender.

**Canton Florencia**: Sí, obvio.

**Lucio Rojas**: ¿Cómo estarían? Termino de entender cómo coexisten los dos sistemas. Vos tenés la cuenta banco que te baja los saldos y demás y tenés el ERP Calypso.

**Canton Florencia**: Exacto.

**Lucio Rojas**: Que tenés que conciliar movimientos. ¿El cash flow que vos armas lo haces mirando Calypso o el banco?

**Canton Florencia**: ¿Como que yo tengo una doble tarea ahí, que siempre fue el punto que queríamos mejorar respecto de esto del cash flow, es que yo me bajo los movimientos del banco y yo por un lado cargo en Calypso, genero los recibos, genero la orden de pago, genero las extracciones de banco, lo que sea, y por otro lado como que nutro información, ese cash de la información del día anterior, me explico? Tengo dos trabajos, hay un retrabajo ahí,

**Lucio Rojas**: voto el data entry los hace manual

**Canton Florencia**: en Calypso y mientras tanto en Calypso sí se hace manual, pero en realidad todo lo que es la carga de facturas lo hacemos mediante un sistemita que nos desarrollaron, donde subimos la factura y el sistemita directamente te detecta todos los datos y vos le pones OK y se carga. Te detecta, o sea está basado en inteligencia artificial, con lo cual no sé te detecta que determinado proveedor, ya viste los que están bastante como que a mí. Y ahora lo que está desarrollando este chico que fue quien nos hizo la implementación de Calypso, es un desarrollo también para lo que es la carga de los recibos, es decir que directamente de la OP que recibimos de los clientes, perdón, sí de los clientes se cargue el recibo, ese todavía está en desarrollo porque hay un problema de Calypso que no nos toma bien, algo que no me acuerdo, no te mentir, pero vos

**Lucio Rojas**: después tenés que fijarte que lo que estés cargando el sistema sea coincidente con lo que. ¿Exacto, y ahora que estamos buscando? ¿Los reportes que me habías pasado del otro día, lo que estamos trabajando, que estamos buscando hacer o qué hicimos el otro día? Para que entiendas, yo esto lo hice sin entender nada su operación, o sea es 100% la base mínima de lo

**Canton Florencia**: que podemos lograr, o sea, lo que hicimos, la traba, lo que hicimos la otra vez fue, yo te compartí los saldos de clientes. ¿Bien, entonces con esos saldos de clientes lo que hizo, lo que armaste era otro que lo armó, no? ¿Bueno, sí, claro, lo que armó, fue como si fuera un análisis de esos clientes, me dijo bueno, me armó el aging de clientes, me dijo bueno cuánta deuda me deben, cuánta deuda tengo? ¿Vencía, no vencía? ¿Y te detallaba y decía che mira este grupo de cliente, te acordás que te armaba eso? Como que este grupo de cliente está sano. Ojo con este. Fíjate que se te dé tanto.

**Lucio Rojas**: Acá tenemos. Lo primero que yo hice fue las tablas que vos me pasaste las caras, no me acuerdo si los pasé a CB o vos ya me habías pasado CSV o me habías pasado.

**Canton Florencia**: No, solo te pasé Excel.

**Lucio Rojas**: Bueno, yo los convertí a CSV al medio para que la herramienta lo incorpore mejor. Después me conecté el MCP es la. Y fuimos acá a trabajar, me explicó los datos que teníamos, teníamos tablas de ventas, de indiguación, de compras, de tesorería, me explicó cómo se relacionaban, cuánto nos deben al 4 de septiembre, cuánto está realmente vencido y cómo se reparte por unidad de negocio qué deberíamos provisionar. Y ahí ya solo empezó a hacer todos los.

**Canton Florencia**: Para mí lo que sería interesante o también que es lo que más nos daría valor sería cómo podríamos con esa información más el historial de cómo nos pagan los clientes o una. ¿Cómo se llama esto? Una variable que te pueda decir o que podamos ir modificando día a día, yo te diga vas a cobrar tanto la semana que viene, tanto la otra, que eso es lo que nosotros en el cash quería hacer una proyección de cobranzas.

**Lucio Rojas**: Claro, no es el caso, Bueno, tener los egresos, pero por lo menos todas las cuentas por cobrar que tenés.

**Canton Florencia**: Exacto.

**Lucio Rojas**: Y las cuentas por pagar también la podría.

**Canton Florencia**: Sí, sí, sí, obvio. Yo porque justo agarramos los clientes, pero yo en mi cash flow proyecto todo y la idea sería eso. Tengo demasiada solapa. Si vos cash lo que yo tengo solapa, solapa, solapa, solapa.

**Lucio Rojas**: Vamos a hacer una cosa, yo voy a dejar de compartir y vamos a hacer un cambio de lógica. Vos me compartís a mí y yo te ayuda a vos a usar la herramienta. ¿Tenés cuenta de Cloud por las dudas?

**Canton Florencia**: Sí, tengo cuenta Cloud. Yo antes de la demo del otro día lo logué con Teramot. Bien, pará, déjame que yo había entrado y ahora me fui acá a la app Teramot. Comparte el link. Ah sí, estaba para que te comparto. Si, comparto. Ahí está.

**Lucio Rojas**: Este es el. Volvió para atrás a Crowe. ¿Cómo se pronuncia bien?

**Canton Florencia**: Crow. Crow. Y son las barritas, siempre nos confunden.

**Lucio Rojas**: Ahí está, ahí Crow. Finanzas, fuentes de datos arriba. Ahí, claro, clique finanzas era que yo había armado para mostrarles cómo era la gobernanza de datos, un ejemplo en vivo de cómo compartir las cosas. Pero bueno, nosotros podemos trabajar sobre este. Ahí vas a tener las cuatro tablas que vos cargaste en su momento. Vas a Estudio de datos, que es el segundo a la izquierda, ahí vas a poder, en donde dice Limpias e interpretadas, hacer una apertura de qué tablas tenés. Si vos tocas el dataset de antiguación, podía vista previa y podés ver la tabla ahí. Si bajas un poco esta parte, visualmente con este zoom es difícil. Ahí sí lo podes achicar.

**Canton Florencia**: Sí, a ver, para.

**Lucio Rojas**: Igual nosotros ya estamos lejos de mirar las tablas, siempre tratando de llegar lo más rápido posible a Cloud. Pero bueno, ahí vas a tener las cuatro tablas que cargaste. Si volvés atrás, vamos a ver cuáles son. Esta de.

**Canton Florencia**: ¿Para dónde tenés que ir? Al pipeline.

**Lucio Rojas**: Ahí sí puedes ver todas. Cuál es la diferencia. ¿Qué es lo que estás viendo acá a la izquierda? Estás viendo las tablas de origen, que son tal cual vos me las cargaste. Y a la derecha, en el rectángulo del medio, vas a tener las tablas que ya están sometidas a unos procesos nuestros que hacemos de forma génética. Para entender esas tablas, te voy a pedir de vuelta que entre a una tabla. Si te explico cuáles son esos procesos. Bien, vas a tener dos. El primero es este SQL generado, que lo puedes expandir. Qué está haciendo acá. Si bajas, quizás no haga ninguna transformación qué hace este primer proceso. Nosotros ahora no. No corregimos nada porque el sistema nuestro dedujo que los datos ya venían bien. Pero en caso de que tablas que vos descargues tengan problemas de calidad del dato, por ejemplo, distintos tipos de formatos de fecha, nombre, apellidos a la inversa, columnas vacías, filas vacías, este primer proceso lo acomod, se deja todo listo. Y en el segundo, que es el esquema, yo con esto te dejo de aburrir, hace un detalle exacto de que tiene cada columna y cada fila de la tabla. Entonces, con esto ya nuestros agentes pueden trabajar en generarte los análisis. Y vamos a ver la última parte. Que tenés que saber para ahora, como estamos trabajando esta es la tabla en sí, acá vas a poder ver la tabla en sí. Si volvés atrás a el tercer rectángulo, Ahí volvimos a la. El segundo a la izquierda. Donde dice resultados, son las tablas nuevas que nosotros creamos a partir de lo que vos me cargaste. Fíjate que esta no es una tabla que vos no hayas cargado, es algo que nosotros creamos para hacer un análisis nuevo. ¿Si abrís el origen que escribe ahí

**Canton Florencia**: está como colapsado el origen donde estaría?

**Lucio Rojas**: Ahí dice abajo del linaje, donde están los cuadraditos de su origen y está colapsado. Yo lo estoy apuntando pantalla como si estuviese.

**Canton Florencia**: Me suele pasar lo mismo ahí

**Lucio Rojas**: ese

**Canton Florencia**: rectángulo que está sin desplegar acá origen ya lo vi, está chiquito

**Lucio Rojas**: ahí tenemos que trabajar un poco esta interfaz, no te voy a mentir,

**Canton Florencia**: también la tengo acá, chiquito también es 80, no importa.

**Lucio Rojas**: Tenés todos los detalles de cuáles son las lógicas de negocio o las preguntas a las que responde esa tabla, que esto es lo que vos hablás con Claude en lenguaje natural. Clot entiende lo que vos necesitas y lo deposita acá. ¿Como se llama esto? Requerimiento funcional para crear la nueva tabla. Va a agarrar las dos tablas de entrada, son las que vos nos diste, el ítem de ventas y anticuación política de negocio, va a aplicar todas esas reglas de negocio que son las que vos trabajaste con Cloud, y va a crear la tabla nueva. Y todo esto lo va a dejar abajo donde todo donde es el SQL generado, que lo podés expandir también, y ahí ya deja la query que da origen al. Estos serían como tus fórmulas de Excel, pero a nivel datos datos esto ya va a quedar estándar y cada vez que vos actualices la tabla, o si estás conectada a la fuente en vivo, se actualiza. Entonces si vos le pedís un cash flow que haga eso, que tome todas las cuentas por cobrar, todos los vencimientos, todas las cuentas por pagar, inflación percibida, muchas variables, las va a bajar como lógica de negocio, va a entender dónde buscarla porque hizo todo el mapeo de las tablas y te arma esta tablita de resultados que queda siempre igual. Entonces vos ya tenés tu análisis hecho que se actualiza.

**Canton Florencia**: Estas preguntas, cuánto nos deben al corte y gin real. Esto es lo que vos le fuiste preguntando a Cloud, o sea vos subiste el archivo.

**Lucio Rojas**: No, no son las preguntas directas. Esto no es quería Cloud, es como que Claude va a ser intermediario,

**Canton Florencia**: vos

**Lucio Rojas**: va a ser usuario de negocio, y Claude va a ser analista de datos e ingeniero de datos, va a interpretar tu pedido y armar todo esto. Vos no tenés que escribir a mano nada de. Lo va a hacer todo solo. Ahí te va a dar la tabla final, que después la puedes consultar,

**Canton Florencia**: y

**Lucio Rojas**: después podés editar las instrucciones si hay alguna regla de negocio que no claro

**Canton Florencia**: que no esté correcta.

**Lucio Rojas**: Después tenemos dos o tres variables más que ya terminamos de repasar y pasamos a lo divertido. Están los dashboards a la izquierda. Si cliqueas el primero, le puedes pedir a Cloud que genere un dashboard para tener visualización de lo que estás analizando. Primero te lo va a mostrar desde Cloud en sí, y después lo va a traer acá. Si le pedís que lo cree en Telamo, ese dashboard tiene un link que si vos lo copias, se lo podés compartir a cualquier persona que tenga una cuenta en tu proyecto y mira directamente las tablas, o sea que si está conectado contra tu fuente de datos de envío, se actualiza. Y esto lo puedes modificar con un prompt también. Bien, y después tenemos dos cosas más. Una es el conocimiento a la izquierda también. Vos siempre que vas bajando reglas de negocio o lógicas o algunas cuestiones que vos interpretas que no son obvias para el modelo porque son propias del negocio, le puedes decir, guárdalo en el conocimiento de Theramo y ya va a aplicar esa regla a cada una de los análisis que hagas en el futuro. Y después la última, dentro de operación, si vos abrís, tenés alertas, que eso es nuevo, donde vas a poder configurar esto también todo desde Cloud, si clickeas nueva alerta, va a tener alguna UI acá, pero lo puede hacer desde Cloud. Vas a configurar acciones que respondan a reglas sobre los datos. Por ejemplo, si yo veo que tengo caja negativa, en algún momento me manda un mail, me avise. Todas estas son automatizaciones que puede hacer sobre los datos. Bueno, ya te súper aburrido, así que ahora vamos a ir a.

**Canton Florencia**: No, no, para nada. Me parece como wow.

**Lucio Rojas**: Pregunta, queremos. Queremos trabajar sobre los datos que ya teníamos o vamos a ir sobre nuevos.

**Canton Florencia**: No podríamos ir sobre los datos que ya tenemos.

**Lucio Rojas**: Bueno, entonces vamos a ir a Cloud y vamos a conectarlo.

**Canton Florencia**: Creo que lo tengo conectado para SOS Pro Perfecto.

**Lucio Rojas**: Usa ya Cloud Code. Lo mismo, tendrías que tocar un botón más,

**Canton Florencia**: que no lo entiendo todavía mucho,

**Lucio Rojas**: pero te deja hacer más cuentas matemáticas. Modelos puede servir para hacer modelos predictivos.

**Canton Florencia**: Bueno, pero eso está bueno para todo lo que yo quiero. Pues yo última. Yo le subo, por ejemplo, acá Cloud, le subo, no sé, las cobranzas de los clientes del último año. Bueno, último año básicamente ya se termina este. Me podría hacer modelo predictivo por cliente,

**Lucio Rojas**: responder algunas cosas. La cobranza sería ya cuando canceló la deuda cada cliente. Porque vos querés conocer su historial de pago.

**Canton Florencia**: Exacto.

**Lucio Rojas**: Y después querés predecir en base su historial de pago para adelante, cuánta mora tendrían.

**Canton Florencia**: Exacto.

**Lucio Rojas**: Bueno, y vos eso lo tenés en tablas del sistema.

**Canton Florencia**: Del sistema, sí.

**Lucio Rojas**: Déjame que me fije si se puede hacer sin problemas.

**Canton Florencia**: Eso estoy pensando. Si tengo que bajar, porque para mí en el listado de recibos no voy a tener. No voy a tener el link a la factura, ¿Me entiendes? Yo me tiro el listado de recibo. Me tiro el recibo, déjame que lo cheque. Que debo confesar que yo soy la que más entra al sistema.

**Lucio Rojas**: Deberíamos.

**Canton Florencia**: Me pasó la info.

**Lucio Rojas**: Lograr que nos conecte el sistema.

**Canton Florencia**: Sí, sería un golazo, porque además no sabes lo lento que creo que es una generalidad de todo lo que es. ¿Cómo se llama? On premise, se le dice. Porque puesto que no soy la más ágil en esto, para mí lo mejor yo podría sacar en realidad sería la cuenta corriente de los clientes. Porque tenés factura. Sí. Pero no sabes cómo está la paga. Yo cuando hicimos. Cuando hicimos la migración, lo que le pedí, pero nunca me lo hicieron, fue que yo quería un reporte me que me mida los días de cobranza, tal automático acá Calypso, recibo tal, pago tal, factura. Desde la fecha de vencimiento a la fecha del recibo hay 10 días. Desde la fecha de recibo hasta la fecha del cheque que te pasaron hay 20 total de pago.

**Lucio Rojas**: Pero eso lo puedo empezar a hacer ahora, cargando directamente los reportes. ¿A qué estás cargando

**Canton Florencia**: para dejar esto? Yo tengo que entrar acá por recibo. Para mí acá no vamos a tener. ¿Ves? No tengo. OK, factura está linkeado, no puedo sacar acá.

**Lucio Rojas**: No puedes bajarte directamente las tablas.

**Canton Florencia**: Sí, pero esto de recibos nomás, yo transmitarías y yo necesitaría saber qué factura me está pagando. Si no, ¿Cómo sé por qué?

**Lucio Rojas**: ¿Necesitamos el acceso a la base de datos?

**Canton Florencia**: Para mí sí, porque yo te puedo sacar listado de recibo de venta, pero yo te con listado de recibo de ventas no vas a saber qué factura me está pagando. Yo te saco la cuenta corriente tampoco. Porque en realidad es un movimiento lo que yo le pedí.

**Lucio Rojas**: Nosotros lo que hacemos esto es juntar como conectamos a todo el sistema, entendemos cómo se relacionan las distintas tablas en el sistema. Si vos hace una pregunta, lo vincula solo y te lo respondería en vivo. Yo creo que tenemos que lograr. No sé cómo es su equipo de sistemas internos. Estaban el otro día en la reunión, ¿No?

**Canton Florencia**: ¿Qué reunión? ¿Perdón?

**Lucio Rojas**: En la que tuvimos la semana pasada.

**Canton Florencia**: La demo. No, no,

**Lucio Rojas**: porque si no podríamos acelerar, pedirle a ellos. Esto está en premise, tipo. ¿Ustedes son los dueños de esta base de datos?

**Canton Florencia**: Sí, paso. Bueno, en la nube en realidad sí,

**Lucio Rojas**: pero depende de quién es el que tiene la base. Porque si ya tiene su equipo de sistema, yo puedo decir.

**Canton Florencia**: Decime la pregunta. Yo se la hago a Agus que es la de soporte.

**Lucio Rojas**: OK.

**Canton Florencia**: Soporte de Calypso, que encima es interno.

**Lucio Rojas**: Pregúntale cómo si la base de datos de Calypso la tienen ustedes en servidores propios.

**Canton Florencia**: Eso me parece que no.

**Lucio Rojas**: Servidores de ellos. Y en caso de ser servidores propios, ¿Cómo podrías acceder al módulo de finanzas para trabajar con eso?

**Canton Florencia**: Casi segura que está para la base de Calypso.

**Lucio Rojas**: Si no, hagamos así. Tenemos esto acá porque estamos yendo capaz que muy para adelante. Te ayuda a trabajar con lo que.

**Canton Florencia**: Con lo que tenemos. Claro.

**Lucio Rojas**: Y después naturalmente vamos a. Depende un poco del proyecto y la parte de avance. Pero estas uniones yo después voy a tener con ellos para conectarnos y para

**Canton Florencia**: mí tiene que ser con Agu. No sólo con los chicos de sistema. Con los chicos de sistemas. En realidad esto no está en nuestro servidor seguro.

**Lucio Rojas**: Ahora volvamos a ir a club. Hola Claude, conéctate a Telamotó, me sale

**Canton Florencia**: tipo por favor, puede pasar cosas. Gracias. La quiero usar. ¿Qué es esto? Para que te vea chica de chiquitito. Terap me pide que vuelvas a iniciar sesión y por eso no puedo conectarme, hacer la configuración desde conectores. Bueno, ya estoy conectada Telamente hay un solo Word. Sobre todo con los proyectos demo y finanzas.

**Lucio Rojas**: Demo, claro. Que vaya demo.

**Canton Florencia**: Esto le estoy diciendo que.

**Lucio Rojas**: Vamos a hacer una cosa, volvamos al conector así te soluciono esto de entrada. Y ahí donde dice personalizado, ahí pone permitir siempre y más abajo hay otro igual. Listo. Ya se debería de solucionar en las próximas iteraciones esto que te pregunt.

**Canton Florencia**: Anticuación de Belerrera. Voy a aplicar ventas.

**Lucio Rojas**: Acá puedes decirle que te recomiende, no sé si querés algo en particular o que te recomiende análisis que podríamos llegar a hacer.

**Canton Florencia**: No le podría preguntar. Vos decís que no Vamos a ir entonces por lo de la proyección.

**Lucio Rojas**: La proyección de. Están los datos acá para hacer eso más o menos.

**Canton Florencia**: Y lo que pasa es que en realidad no tiene forma de limpiarlo. Para mí o le pregunto, ¿Tenés todos los datos para proyectar? Pausa.

**Lucio Rojas**: Esto sería algo súper sencillo de que los datos.

**Canton Florencia**: Claro, sí, parcialmente. Acá tenemos escenario base. Me encanta por escenario base de corto plazo, no, tres meses, pero no parece sensorial inglés. Lo tenemos futurado, vencen después del 4 con su fecha de seguro de vencimiento. También tenemos la facturación y las cobranzas de agosto por cliente y por unidad. Lo que falta, la historia de más meses que esta señalidad y tendencia, falta el comportamiento real de pago por cliente. Claro, es esto.

**Lucio Rojas**: Mandar una captura del. Calypso y mandar una captura directamente así como está, para que sepa. Estoy usando esta versión de Calypso.

**Canton Florencia**: Esta versión encima va a dejar de funcionar, tengo que mirar a otra. ¿Hay alguna forma que me decías?

**Lucio Rojas**: ¿Hay alguna formA de yo poder facilitarte estos datos sin la conexión a la base entre paréntesis, bajando algún reporte? O. ¿Nos dice que hacer directamente?

**Canton Florencia**: Sí le falta ser que solamente hemos invitado de Tego en Tulanich pantalla. Lo último 6 a 12 meses. Con eso podemos calcular estacionalidad, gasto fijo y variable y la vida real de cobro, cuenta a pagar ante consumo, proveedores. Es tremendo. Escúchame, para, está bien, yo acá le puse. Ah, está bien porque no soy dónde estaba leyendo. Lee más allá. Claro, es cadenario impositivo, la guinal de los abonos, los archivos mucho pesar también pueden traer tu papel a un lado. Claro, a mí lo que faltaría, por ejemplo, también. Bueno, vamos a probar con esto para arrancar. Le bajo entonces la anticuación actualizada hoy le bajo la funda bar y debajo extra. Bueno,

**Lucio Rojas**: ¿Cuánto tarda generalmente en hacer esas descargas?

**Canton Florencia**: No sé, vamos a probar ese.

**Lucio Rojas**: Me voy a cerrar a mí. Ahí si que si me querés cerrar. No, pues ahí se.

**Canton Florencia**: Esto para los filtros. Sí, A Perón le puse fecha. Esto, bueno, tiene toda la historia.

**Lucio Rojas**: Tipo de salida. Esperá, elijamos el.

**Canton Florencia**: Ah, yo le puse Excel, perdón.

**Lucio Rojas**: Bueno, no pasa nada. Tratemos de cargar el Excel. Si, ese se ve mejor.

**Canton Florencia**: Y le pedimos un montón.

**Lucio Rojas**: Perfecto.

**Canton Florencia**: Entonces para esto es. Qué te dice que era esto de sorería. Bien, Después teníamos que ver compras, todo el monasterio compras. Porque después son tres razones sociales que yo tendría que tener. Pero bueno, lo bueno es esto, que si le conectamos a la base. Está todo ahí.

**Lucio Rojas**: Sí, eso está todo.

**Canton Florencia**: Y consulta, conectamos la base y yo, o sea, me saltearía un paso que sería el de cargarlo todo en el cash. Yo podría generar acá que directamente se cargue todo en Calypso. El problema es que no me da la información.

**Lucio Rojas**: Si vos mantenías actualizado el Calypso, el cash flow se armaría solo.

**Canton Florencia**: Claro, todo el tiempo no actualizado está por ahí. Lo que nos falta es alguna. Esto es AOE, ¿Nos falta alguna?

**Lucio Rojas**: Manda el screen de esto a ver si necesita algo más. No, el screen acá de esto que es el sistema. ¿Estás abriendo bien acá esto? Sí,

**Canton Florencia**: Ahora que se te va no puedes volver a. Descargar. Esto era proveedores. Después ¿Que más me pedía? No tengo anticuación de lo que no existe. Ítem de venta, tesorería, ítems de venta y de compra. Anticuación, One nailing down. No sé, solo yo sabe.

**Lucio Rojas**: ¿Y qué más te pedían?

**Canton Florencia**: Antigüedad hoy de clientes. Compra ítems de venta. Sí, Listo, se compra, ya está. Ventas, Tenés venta.

**Lucio Rojas**: Estoy preguntando mientras el otro día los chicos que eran más o menos que tenían poder de decisión eran los jefes, ¿No?

**Canton Florencia**: ¿Cómo eran los nombres, los socios? Marcelo, Mateo.

**Lucio Rojas**: ¿Y vos tenés llegada a ellos? No, porque creo que para avanzar la

**Canton Florencia**: conexión al sistema había pensado mandar un mensajito a Marcelo a ver si me daba el OK para avanzar. Pero de última

**Lucio Rojas**: creo que Juan le envió la propuesta.

**Canton Florencia**: Sí, para mí sería legal para shuvik. Estaba buscando. ¿Me vas a echar?

**Lucio Rojas**: ¿En una semana? Lo deberíamos tener conectado y andando, sobre todo por tiempos humanos, en tiempos tecnológicos.

**Canton Florencia**: Y qué requieren, por ejemplo, para que yo le diga que vaya adelantando. Agustina.

**Lucio Rojas**: Agustina.

**Canton Florencia**: Agustina es la de soporte de Calypso, o sea que le tengo que pedir a ella que me pase

**Lucio Rojas**: directamente es pedir acceso a un acceso de vista a la base de datos donde tenga el sistema. Son tres o cuatro campos, yo los lleno en un formulario y se conecta.

**Canton Florencia**: Bien.

**Lucio Rojas**: Es soporte interno sería. ¿Dentro de ustedes tienen alguien que se dedica en realidad?

**Canton Florencia**: Claro, lo que pasa es que nosotros también hacemos soporte y venta de software. Capixo, Calipso y SAP Business One para otros. Claro. Entonces tenemos el soporte interno.

**Lucio Rojas**: ¿OK, pero ella responde a Calypso?

**Canton Florencia**: No, respondo a nosotros.

**Lucio Rojas**: Y es la que maneja el sistema. Es la dueña del sistema.

**Canton Florencia**: Sería esa pregunta de mataste con lo

**Lucio Rojas**: que es duda, pero es como que ella es la cara visible del sistema para ustedes.

**Canton Florencia**: Claro, hoy en día sí. Nosotros cuando hicimos la implementación hicimos directamente con otro partner que llaman Mecalypso y después cuando ingresó a Crow directamente pasamos a tener el soporte de ella, pero soporte interno de sistemas. Tenemos otro otro equipo.

**Lucio Rojas**: Si querés podemos ir cargando, enteramos las otras mientras dale

**Canton Florencia**: para entera. Motovir directamente. No, acá no. Claro, buen dato.

**Lucio Rojas**: Fuente de datos, si querés hagamos un proyecto.

**Canton Florencia**: Nueva fuente, cargar archivos. Por ahora tengo ítems de compras. Bueno, supongo que me va a entender.

**Lucio Rojas**: Va a abrir ahí el. Tenés que ponerle el nombre a la fuente.

**Canton Florencia**: Proyección. No, Y me va a faltar otro, pero no importa, voy conectando esto que lo esperemos y vamos a ver cuánto le queda. Calypso me queda los ítems se venta todos y me faltaba la anticuación de clientes hoy.

**Lucio Rojas**: Bueno, esperamos o podemos arrancar. ¿Arranquemos un proyecto nuevo, así te queda todo limpio, no? Vamos haciendo eso. Enteramos ahí. Volvete a Crow, Create uno nuevo. Añadir proyecto. Cash Flow Floor. Este ponele acá. Puedo subirlos de a uno, no pasa nada. Si querés elegí solamente el Tesorería ahí en Cash Flow Floor, cargar archivos.

**Canton Florencia**: Voy a uno

**Lucio Rojas**: hacer más fácil actualizarlo. Tesorería y dale enter. Ahora te lo va a leer acá. Hay que esperar a terminar el flujo de conexión. Publicar automáticamente a la derecha. Bien. OK, eso fue raro. Vamos el próximo. Y este voy a prestar atención.

**Canton Florencia**: Nueva fuente.

**Lucio Rojas**: Sí, igual archivo. Si tocas ahí en clic te hace lo que estás haciendo arrastrándolo. Ese clic

**Canton Florencia**: no entendí.

**Lucio Rojas**: Ahí ya te abre directamente el escritorio.

**Canton Florencia**: Ah,

**Lucio Rojas**: creo que lo tenés en descargas.

**Canton Florencia**: Sí. Ah, está.

**Lucio Rojas**: No, y toca abril. No. Es cosas raras seguir haciendo como estaba haciendo

**Canton Florencia**: para impaga operadores abril está bien, Si le hago doble clic no va.

**Lucio Rojas**: Sí, no sé qué habíamos hecho que se fue Bien, hay que continuar.

**Canton Florencia**: Ahí me respondió Agus. Eso es la definición del servicio SAS Keringa Calypso, vos contactás algo similar a Netflix y toda la base de datos está en la nube de ellos tienen contratado servidores de Huawei si no me equivoco.

**Lucio Rojas**: OK, vamos a tener que hablar con Calypso Entonces ahí escribí publicar automáticamente abajo a la derecha y así vamos a ir publicando todas. Entonces después voy a necesitar una reunión con ellos para hacer la conexión a las cuentas

**Canton Florencia**: Y si necesito una conexión a un software, sería un software para la gente, no somos de datos. Necesito. Ahí le pregunté. Bueno, vamos de vuelta. Cargar archivos, Tuki, A ver si terminó esto. Oh dios.

**Lucio Rojas**: Te aviso ahí cuando hacía esos pedidos a soporte no creo que sean muy receptivos, ¿No? ¿Qué querés hacer? ¿A dónde querés conectar? Y ahí nosotros vamos a tener una reunión con ella probablemente estaría bueno alguno de los socios si se puede tener como bajada de línea cuáles son los pasos.

**Canton Florencia**: Dale, ahí me está escribiendo. No, conmigo primero. Mejor hoy después de las dos, tipo en agenda nos juntamos un rato y lo vemos. Dale. Bueno, esto como te darás cuenta, a veces creo que lo colapsé y yo no tengo mucha paciencia, por eso no entro mucho. Bueno,

**Lucio Rojas**: Bien, acá ya se están cargando las tablas de antelado, Buenísimo, así que faltaría una de esas dos.

**Canton Florencia**: Marqué. Reporte de antigüedad, No está solo con Monasterio El reporte sería el reporte de la antigüedad que usamos, la antigüedad del cliente, la antiguación de clientes sale consolidado de las tres, o sea que tengo que tocarlo antes de subirlo porque yo te paso información de una sola.

**Lucio Rojas**: No, pero eso se va. Se va a dar cuenta. Subírselo como está y que lo reg. Claro, capaz que si tenemos en rango va a ser mucho más pesado ese Excel para descargarlo la última se note lo baja pero va con dos años

**Canton Florencia**: porque es la antigüedad. Esto es la antigua. Un corte. Esto es.

**Lucio Rojas**: Tan raro esto pasáselo así como está, Claude. Así como está anda Claude,

**Canton Florencia**: Qué está

**Lucio Rojas**: raro el formato tiene que ser tipo. ¿Ahí agarra, no? Con el que estamos.

**Canton Florencia**: Sí. Bueno, ¿Qué le digo?

**Lucio Rojas**: Pone más, pone subir o añadir archivos, elegí de documentos, elegí el que estábamos viendo recién. Hay anticuación con cliente y si compartime esto a un CSV tabular para solamente tabular.

**Canton Florencia**: Ya lo borré, le saqué la otra info.

**Lucio Rojas**: Esto es para que lo pueda. Porque mira, si vos vas al Excel, lo tenías abierto, me parece. Si te explico que estamos haciendo. Se fue abajo. Está como no es una tabla tabla tiene esas filas arriba, tiene los filtros y demás. Entonces para que lo entienda, tiene que parecerse exactamente una tabla.

**Canton Florencia**: Pero para lo que. Lo que te complica es el filtro. Y esto acá te lo complica también.

**Lucio Rojas**: Claro, siempre la A, porque sabes qué

**Canton Florencia**: pasa en todas te la va a complicar.

**Lucio Rojas**: Y creo que ya lo estamos entendiendo. Igual lo cargó bien, por eso yo siempre paso.

**Canton Florencia**: Y ítem de compra en todas está.

**Lucio Rojas**: Y a ver, anda Telamot,

**Canton Florencia**: ¿Esto que es? ¿Nueva versión disponible?

**Lucio Rojas**: Estamos actualizando.

**Canton Florencia**: Pregunta basiquísima, pero no importa.

**Lucio Rojas**: Entra a cualquiera a compras desde el estudio de datos. Siempre lo ves. Entra ahí alguna.

**Canton Florencia**: Está bien, porque estoy dentro del proyecto de Cash Flow Floor. Listo,

**Lucio Rojas**: Bien. No es como la fila 1 dice esquema monasterio. Claro, es como que no la agarra muy bien, queda.

**Canton Florencia**: Algo como raro.

**Lucio Rojas**: Volvamos a. Voy a Clock.

**Canton Florencia**: Bien.

**Lucio Rojas**: Y pasar el resto de las que teníamos.

**Canton Florencia**: Bien. Para. Y yo tenía que bajarme Calizo algo más que eran las Ítems de venta, que yo no había podido bajarlo desde Monasterio. Bien. Los de Cloud. Sí. Lo que pasa es que los tengo acá todos. Cómo apagarme, Pasar Google Drive acá descarga.

**Lucio Rojas**: Ya te hizo con los cuadros.

**Canton Florencia**: Google Drive me lo pone por defecto porque yo hice la conector con.

**Lucio Rojas**: ¿Me hace un favor, Flor, ¿Me puedes abrir el Excel cuál quiera? Ahí está.

**Canton Florencia**: OK.

**Lucio Rojas**: Estaba tratando de entender algo que tenemos que arreglar.

**Canton Florencia**: Bueno,

**Lucio Rojas**: Bien. Yo voy a borrar de Telamot los que subimos recién, porque no lo vamos a subir de vuelta. Esta es la parte del setup, siempre es la más aburrida y la más larga. Una vez que tengamos los datos, yo te dejo jugar con el cash. ¿Nos falta alguno? Ya está.

**Canton Florencia**: Faltaba el Ítems de venta, que no sé si bajó. No lo. Y yo lo que hice fue saber qué pasa que está. Está todo 2025. 20 26. Así que le puse 2026 nomás. Después me di cuenta. A ver si eso mejoraba un poquito. Al menos. Y con todas las actualizaciones que tiene Cloud así como muy seguido, cómo hacen con los conectores y todo lo demás con Terabot, eso no es problema y lo vamos revisando.

**Lucio Rojas**: Un equipo que revisa, que va cambiando, porque es terrible. Sí, sí, es la parte más complicada del trabajo, mantenerse siempre a la orden,

**Canton Florencia**: Subiendo el resto. ¿Ya les guardaste todos? Fuente de datos, cash flow, fundamentos, listo. Como me decía que yo le pongo enter a casa, está no, continuar

**Lucio Rojas**: y ayer pull up.

**Canton Florencia**: Si, después estoy pensando, porque esto obviamente lo que vamos a tener acá es lo que ya se sabe, él podría proyectar con esta información para adelante. Va a faltar todo lo que sea para adelante, valga la redundancia, en el sentido de, por ejemplo, estimación de ventas de cada área, estimación de gasto, no sé por ejemplo acá, pero bueno, veamos qué nos arma con esto.

**Lucio Rojas**: Claro, acá voy a un cash flow

**Canton Florencia**: sobre lo sobre ya pasado,

**Lucio Rojas**: devengado sería, Y después tendrías que sumar una capa de proyecciones.

**Canton Florencia**: Y lo que sería interesante, para mí lo más importante sería como hacer escenarios, ¿Entendés? Como decir, bueno, estoy en este escenario donde considero que el aumento de sueldo va a ser de tanto que la inflación más irritante que mis ventas, voy a tener cobranza de 70%, escenario 2 más ácido, escenario 3, o sea, uno es el que tiene más probabilidades de pasar que ese. ¿Capaz que me sirva lo de los modelos predictivos, capaz no? Y después decir, che bueno, si yo estimo un escenario más positivo, un escenario más negativo, eso será para mí lo ideal.

**Lucio Rojas**: No es tan modelo predictivo, eso es más temática, es más lineal, como una regresión. Sí va a multiplicar por distintos ponderados o pesos, puede ser súper fácil eso.

**Canton Florencia**: Bueno, no, claramente los ítems de venta no quieren salir.

**Lucio Rojas**: Podemos trabajar sin esto, ¿No?

**Canton Florencia**: ¿Sí, la venta es lo que pasó y ya la venta la tiene que cargar las de agosto, lo único que va a faltar acá, la última, que

**Lucio Rojas**: podría ser, se las borramos igual o no? La tiene en otro lugar.

**Canton Florencia**: Ah, las tiene en otro.

**Lucio Rojas**: Sí, pero se podemos pasar.

**Canton Florencia**: Bueno, pero de última lo que puedo hacer es bajar de última las ventas. No se bajo de venta junio a hoy, ¿Te parece?

**Lucio Rojas**: Está bueno esto para probar la herramienta, un caso.

**Canton Florencia**: Y el sistema, como de vos conectar al sistema y ya te pedís, necesito que me traigas de, no sé, razón social, monasterio asociado, todas las ventas y así. Y te la trae. Claro.

**Lucio Rojas**: Ya tiene todo. Sí, tiene todo, nada más hablas y te hablas contra el sistema directamente. No tocaría más esta interfaz.

**Canton Florencia**: Sería tan feliz. Voy a ser muy feliz. Ítems de venta. Y esto la idea también es conectarlo con Visma, que es nuestro software de liquidación de sueldos y recursos humanos y demás de gestión de recursos humanos. Dijimos ítems de venta,

**Lucio Rojas**: Ben,

**Canton Florencia**: It's very hard. Bueno, le pongo la Y no, porque le puse todo el este año y no me lo tomó.

**Lucio Rojas**: Y si no el filtro. Puedes poner el mes de hoy, pero

**Canton Florencia**: octubre va a tener pocos movimientos.

**Lucio Rojas**: Antes que estábamos trayendo el histórico.

**Canton Florencia**: ¿Cómo?

**Lucio Rojas**: Antes estábamos trayendo el histórico.

**Canton Florencia**: Claro. Todo el año.

**Lucio Rojas**: Todo el año.

**Canton Florencia**: La primera vez que le puse a bajar a Cinema me va a traer toda la historia que era hace dos años que tenemos del primero de enero del 2025.

**Lucio Rojas**: Podemos ir jugando con los otros, sino mientras tanto. Vale, vamos mientras se descarga. Y bueno, ahora sí entra de vuelta a Telamot. Al entrar el proyecto, te hago una consulta.

**Canton Florencia**: ¿Proyecto, o sea, si yo estoy en conversación y me voy con esta cosa, tengo que decirle vuelta que entre?

**Lucio Rojas**: No. Podríamos haberle dicho, mira, caso.

**Canton Florencia**: Mantener la gracia escrito como si en proyecto de cosas que se aplican igual como las ventas, pero no puedo dar.

**Lucio Rojas**: Y decir que que las reglas se mantienen. Información de impuestos y sueldos no está en el sistema.

**Canton Florencia**: No, o sea, sí en realidad sí lo tiene como ambiente, tesorería, tiene que tenerlo. ¿Qué horizonte, qué detalle querés para el primer cash flow mensual, tres meses? Solo cuenta lo que ven.

**Lucio Rojas**: No, porque al revés puedes ponerle algo vos abajo.

**Canton Florencia**: Claro, lo que pasa es que Manuti no puede identificar cobro lo vencido según el atraso real de pago de cada cliente. Los concursados, los más de 90 quedan afuera. Es mentira eso, porque capaz que los clientes que me pagan más de 90, muchos me van a pagar con la misma forma que venían pagando. Mal, pero van a pagar. Trata de. Pregunto si me hace. Y a esos. Forma de.

**Lucio Rojas**: Proyecto final data. Ahí abajo.

**Canton Florencia**: No,

**Lucio Rojas**: Sí bien pasa solamente estando a CL.

**Canton Florencia**: ¿Esto era venta septiembre? ¿En auto tendría que pasar, no?

**Lucio Rojas**: Si le manda ese Excel, Explicale, decirle esperá, vamos a pasar primero esto CSV para poder cargarlo y después volvemos a hacerlo con esta información. Cargamos este y ya no nos faltaría. Lo descargamos y lo cargamos. Vamos a esperar dos minutos a que este sea. Ese. Tardó unos minutitos en cargarse y ahí ya te queda toda la tabla para esto. Antes vos te lo bajabas y lo cruzabas todo en Excel.

**Canton Florencia**: Esto es que en realidad, como te digo, yo no las proyecciones que la armo, la armo porque por ejemplo, quien gestiona las cobranzas en base a esa antigüedad que vos sacaste, las va proyectando, Entonces saben, o sea, el cliente Pepito que me debe a 90, sabe que más o menos de acá me va a pagar en la semana que viene, ¿Entendés? ¿Es como que está todo particionado, me explico? Quien gestiona la cobranza sabe más o menos el comportamiento de los clientes y lo va proyectando en función de eso. Ahora bien, para el de cash flow, yo encima soy más ácida, entonces digo, che, esto que Silvi me proyectó que vamos a cobrar la semana que viene y no sé si realmente lo vamos a cobrar la semana que viene. Entonces le pongo, bueno, para cuando yo el análisis le digo, che, esto que está en amarillo, porque los ex, esto le pongo un 70% que lo vamos a cobrar, no le vamos a cobrar el 100. Listo, esto ya está, voy a cloud

**Lucio Rojas**: y mira de vuelta el proyecto, cargué la tabla nueva y ahora sigamos con toda la información. Asimismo le tendría que subir los.

**Canton Florencia**: Cómo me dijiste algo que sí de

**Lucio Rojas**: esta misma forma le puedes cargar después lo que te estaba pidiendo, que era los sueldos y no sé qué otro.

**Canton Florencia**: Claro,

**Lucio Rojas**: Está pensando bastante. A ver, abrir, a ver qué está haciendo. Si tocas la flechita esa, A ver, abrimos alguna. Está mirando la tabla, voy a entenderla.

**Canton Florencia**: Clasificar por comportamiento de pago y a los de más de 90 días. Ahora armo el flujo de fondo 9-19 con dos escenarios de cobro. Literal, me la tomo

**Lucio Rojas**: ahí. Podrías usar algún modelo más inteligente también.

**Canton Florencia**: Yo no quiero que me hagan los escenarios, yo quiero que me. Está bien, dos.

**Lucio Rojas**: Por último, variamos esa parte. El modelo ese que usas, Sonet 5.5 entraría.

**Canton Florencia**: Lo tengo. El otro día nos hicieron una capacitación, nos dijeron que le digamos qué es lo que tienen que usar. No sé, vos sugerime algo, o sea que le digan. Perdón, le dimos una instrucción.

**Lucio Rojas**: Si, lo vi, que te dice que modelo usar.

**Canton Florencia**: Claro, o sea como que diciéndole. Si, vos analizá y empezar el modelo del más bajo hasta el más alto.

**Lucio Rojas**: Sí, sí, vi que te estaba tirando esas recomendaciones pero para este tipo de trabajo es usar Opus. El de arriba es mejor para esto que está haciendo. Sí, porque algo complejo.

**Canton Florencia**: No me acuerdo de cómo era el tiempo de uso de la herramienta. ¿Cuánto era el tiempo de uso de la herramienta de Cloud?

**Lucio Rojas**: Las ventanas.

**Canton Florencia**: Sí, eso.

**Lucio Rojas**: Si se te vencen los tokens, tienes hasta el mediodía, hasta que se te renueven. Si se te vencen al mediodía, después del mediodía tenés hasta la tarde. Si se te vencen a la noche, tenés hasta medianoche. Tiene tres ventanas. Bueno, ahora va a terminar de pensar y te va a devolver. Y ahí después vas a ir ping poniendo vos. No sé qué te podemos abrir. Usando cosas raras. Te está armando un Excel con el Cash Pro. Yo le pedía que te arme un Artifact. Claro, el Artifact es tipo el dashboard ese. Pero ahora cuando llegó al Excel, le pedimos que le cambie el artículo. Podemos usar para que te diga la base. Hacemos un Artifact que me deje mover variables y filtros. Entonces vos lo vas moviendo y te van cambiando las curvas. ¿Especificamos mucho?

**Canton Florencia**: No, Ya me encantaba en Excel. Estoy chequeando que los números sean. Antes de manártelo,

**Lucio Rojas**: Decile antes de ir a ver el cash flow decir, quiero que los Barnes tipo Artifact, con una línea base y distintas variables que yo pueda modificar para ver escenarios, como por ejemplo cobranza, ingresos. Son las variables que a vos te gustaría ver.

**Canton Florencia**: Si, son eso más que nada, porque después tendría. Si, sueldos. Pero la realidad es que no le pase nada.

**Lucio Rojas**: Estudia tardar otros cinco minutitos. Es una skill que te recomienda todos los modelos. Yo todavía digo Qué funcionaría rara. ¿Que saco? Club, entiendo. ¿Quién le hizo la capacitación? ¿Sabes?

**Canton Florencia**: BSL, ¿No son medios sociales con ustedes algo así, o no? ¿Cómo es para dejarme que te acaban de pedir?

**Lucio Rojas**: ¿Quién se las dio? Manu.

**Canton Florencia**: Manu. Manu Caro. ¿Estaba Tommy, vino un día ahora me dijeron que se fue a La Plata, puede ser? Y después viene otro chico que la verdad que no me acuerdo, proyecto cómo se llamaba esto.

**Lucio Rojas**: Y estudió la capacitación. Estuvo bueno.

**Canton Florencia**: Sí, re bueno. La verdad que súper interesante. Y eso que teníamos distintos niveles, porque hay gente que nunca había abierto Cloud y hay gente que ya había creado skills y demás. La verdad que sí. Muy bueno. La tremendo. Es cómo cambia todo minuto a minuto, Iniciales, cobros, Hora de cartera de Ensenada, See whatever. ¿Quiere haber sacado esto? No, Acá está medio raro. ¿Cómo puede ser que el flujo sea el mismo? ¿Escenario A y escenario B? Porque no le puse una dije nada. Es muy inteligente.

**Lucio Rojas**: ¿Qué hora se termina el otro? Yo el Excel ya me desacostumbré a verlo. Totalmente.

**Canton Florencia**: Te desacostumbraste a la Lexan.

**Lucio Rojas**: Sí, yo no miro más. Es más, no lo tengo instalado. Cuando iba a la facu sí tenía todo el.

**Canton Florencia**: ¿Vos que estudiaste?

**Lucio Rojas**: Yo estudié Negocios digitales.

**Canton Florencia**: Ah, mira. Sí. Acá la dan.

**Lucio Rojas**: Sí, en la U. A ver, ahí lo puedes abrir y vamos a ver qué hizo.

**Canton Florencia**: Así es. Abrirlo. ¿Vos decís que lo abrí?

**Lucio Rojas**: Sí, sí. Este lo puedes tirar para allá. La ventana esa.

**Canton Florencia**: No,

**Lucio Rojas**: La aldea derecha iba a llegar.

**Canton Florencia**: Ah, esto me gusta. Otro habíamos visto. ¿Bueno, ahora qué supuesto tiene en cuenta acá, pero días que se atraso, adelanta el cobro de toda la cartera y la facturación, sabe? Toda la cartera. Esto para mí.

**Lucio Rojas**: Bueno, eso se lo va integrando.

**Canton Florencia**: Claro.

**Lucio Rojas**: Puede abrir el chat, dice chat allá. Y ahí le vas pidiendo todas las modificaciones.

**Canton Florencia**: Perfecto. Para que dice la línea va a ser en gris y el escenario en color.

**Lucio Rojas**: Si no me puede ir mandando screens y pedir lo que. Te dejo, que son y media y tengo.

**Canton Florencia**: Sí, dale.

**Lucio Rojas**: Si yo te gustó.

**Canton Florencia**: Está buenísimo. Está buenísimo también entender cómo es el para qué quiero ir acá. Entender cómo estaba re cerca, estaba trabajando ahí. Entender cómo se llama esto, cómo subir la información a theramot y qué es lo que yo necesito subir y que no. Cuando conectemos la información para mí va a ser mucho mejor. Claramente. Y ahí tengo una pregunta, por ejemplo, rápido, no te quiero demorar más. Si vos tenés este artefacto, ponele, yo la quiero conectar directamente con la información que tengo, es. Obviamente voy a tener la información diaria del día anterior.

**Lucio Rojas**: Claro. Y ya se mantiene actualizado con eso todo el tiempo.

**Canton Florencia**: No tengo que hacer ningún proceso ni nada. ¿No es que tengo la tela decir actualízate, no? Bien, genial. A mí lo que estoy pensando, me faltaría agregar acá sería, además de la información que ya sabemos que falta, bueno, yo me quedo trabajando con esto, a ver con qué puedo avanzar.

**Lucio Rojas**: Después si querés, si tenés contacto ya con los socios y con la chica de soporte para decirle que las propuestas ya la tienen, y si quieren avanzar a la conexión, dale llamando soporte hasta llegar.

**Canton Florencia**: Yo ahora le mando un mensaje a Marce, le pregunto si ya tengo el OK, veo si ya me puedo entrar a tarde con AGU. Si necesitamos, te aviso última a la hora que coordinamos

**Lucio Rojas**: la reunión con sistemas.
