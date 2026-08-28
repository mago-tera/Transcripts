# Teramot <> Hz Group

**Fecha:** 2026-07-14T17:00:47.434+00:00  
**Duración:** ~60 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, Agustin Garcia <agustin.garcia@teramot.com>, Diego <>, Vikingo <>, Veronica Barrios <veronica.barrios@hzgroup.com.ar>  
**Externos:** veronica.barrios@hzgroup.com.ar  
**Apollo ID:** 6a567964ec962600185f5d19

---

**Diego**: Buenas. ¿Qué tal, Franco? Hola Agustín.

**Agustin Garcia**: Hola Diego, ¿Cómo estás?

**Diego**: Bien, bien.

**Agustin Garcia**: Me alegro mucho.

**Diego**: Acá estamos esperando el partido de Francia España.

**Agustin Garcia**: Semana decisiva, una.

**Diego**: ¿Qué te parece? Vamos a ver qué pasa.

**Agustin Garcia**: Hay que preparar el corazón para lo que viene.

**Diego**: Ya lo venimos, te digo, lo venimos preparando bastante todos estos partidos, si no nos morimos. Hasta ahora.

**Agustin Garcia**: Tremendo, tremendo, tremendo. Por Dios, De locos. Pero bueno, ¿Qué vamos a hacer? Nunca nos pasa que no sufrimos. Es siempre, siempre así, con un nivel de estrés alto.

**Diego**: Sí el domingo ya termina el Mundial, digo, no estoy preparado para que termine. Encima después en cuatro años vuelve, ¿Viste? Pero en cuatro años voy a tener cuatro años más. Ya esta edad. ¿No querés que pase?

**Agustin Garcia**: Tremendo, tremendo. Aparte como que uno siente un vacío porque decís ¿Quién juega? Ah, no hay, no juega.

**Diego**: Claro, ya viste ahora que no hay partido todos los días decir che, y hay ¿Quien juega? No lo juega. Uy, qué bajo.

**Agustin Garcia**: Tremendo, tremendo. Pero bueno, se está sumando Vero. Hola Vero, ¿Cómo estás? ¿No estás muteada?

**Vikingo**: Ahí estoy.

**Lucio Rojas**: Ahora me escucho.

**Diego**: No sé si se iba a unir Cristian también. Estaba invitado Cristian a reunión. Olsen

**Franco Ferrero**: estaba invitado, pero no.

**Diego**: A ver, ahí le voy a preguntar si se une.

**Franco Ferrero**: Dale,

**Diego**: Mandame el link, ahí te lo paso.

**Franco Ferrero**: ¿Tenés el link a mano? Si no, te lo paso. Yo igual le mandé la invitación.

**Diego**: Estaba la invitación, pero

**Franco Ferrero**: si querés, por las dudas.

**Agustin Garcia**: Hola Cristian, ¿Cómo estás?

**Vikingo**: Momento, momento, momento, momento, que estoy acá revisando unas cosas. Listo, acá estoy. Después de que yo subiera la base de datos.

**Agustin Garcia**: Mira, bueno, hay un poquito para alinear un poco la expectativa. Nosotros con la base de datos que tenemos, que ya es la que nos habían enviado la otra vez, podemos hacer una prueba concepto funcional donde podemos revisar los casos de uso que tengan. Diego Ibero. Obviamente que si hace falta repetir con datos más frescos lo podemos hacer. La realidad que también es un proceso para poder actualizar las bases. Así que lo que buscábamos era hacer una demo funcional para mostrarles un poco el potencial. También un poco ajustar un poco los casos de uso que veamos acá con Diego y con Vero. Si vemos que hace falta hacer doble clic en algo, podemos hacer una segunda vuelta. Creo que con la información que tenemos podemos sacar buena información. Creo que ahí el foco. Diego, corregime, pero estaba en revisar lo que son los procesos que ustedes tienen con lo que es la auditoría de cuentas a pagar, ¿Verdad?

**Diego**: Sí, sí, claro. Justamente estamos arrancando, o ya iniciamos una revisión de cuentas por pagar que está a cargo de Vero, y dijimos, bueno, qué mejor por oportunidad que hacerlo con una auditoría, que es un proceso, digamos, dentro de todo sencillo, que es ver órdenes de compra, facturas, ingresos, precios y bueno, todo lo que es el control interno de este proceso. Así que creemos que era una buena oportunidad para usarlo como un caso, caso testigo.

**Agustin Garcia**: Perfecto, bueno, buenísimo. Si quieren ya vamos directo a ver la herramienta en funcionamiento. No sé si ustedes quieren que empecemos con algo puntual como para que ya podamos empezar a disparar.

**Vikingo**: Yo tomé nota, Diego, algunas voy compartiendo que son las primeras inquietudes que nos surgen, o por lo menos la primera necesidad de validación de información necesitamos ante este proceso, sabiendo cómo es el circuito, digamos, la realidad. El tema es el siguiente, en este circuito, si bien se usa BIM, lo que ocurre es que la registración de la factura con los datos que trae la factura física, la termina validando el responsable o el agente de cuentas por pagar. Entonces una de las primeras validaciones que para nosotros sería interesante efectuar es poder validar precio y cantidad. Pero acá lo aclaro, contra el documento PDF que queda subido en SAP, versus con lo que es cantidad, la recepción efectiva hecha por planta, que sería el famoso WE, y lo que es precio de la factura con lo que está declarado en la orden de compra. ¿Por qué lo digo contra la recepción de planta, lo que tiene que ver cantidad y el precio con la orden de compra? Porque en definitiva la cantidad que se genera con el documento, la recepción con el WE, eso es la cantidad que pone efectivamente la persona que está en planta, que es la que toma contacto con ese objeto que se está recibiendo. Y el precio, en realidad ocurre lo mismo, es el valor que determina Cuentas por Pagar al momento de cerrar la orden de compra. Entonces ahí como que el control qué pasa Cuentas por Pagar, lo que ocurre es que registra los datos de la factura, del PDF, lo registra, controla y lo registra. Si está mal, lo puede registrar igual. Entonces por eso yo quería hacer, o pensamos hacer el control de, digamos, los datos de cantidad y precio que son definidos y registrados por agentes externos al circuito contra el PDF de la factura, digamos.

**Lucio Rojas**: Perfecto, perfecto.

**Vikingo**: Y ahí ver si se detectan.

**Agustin Garcia**: Sí, básicamente entiendo bien, lo que vos necesitas es, digamos, leer la factura, el formato PDF de la factura, para poder obtener lo que es la cantidad,

**Vikingo**: para

**Vikingo**: poder obtener las inconsistencias. ¿Por qué? Porque puede pasar, por ejemplo, suponete, suponete que. A ver, la factura, Te voy a poner un ejemplo cualquiera. Suponete que la orden de compra dice que se compran cinco unidades a cinco mil pesos y la factura finalmente después termina viniendo con otro valor. Pero ¿Qué pasa? Igual la persona de cuentas por pagar puede terminar poniendo el dato que está que cruza con la orden de compra y saltear la factura, digamos.

**Diego**: Claro. A ver, perdón. Mero quinta.

**Vikingo**: Sí, sí, sí, sí.

**Diego**: Aclara la ¿Cuál es el ABC del control interno en cuentas por pagar? Que haya que mach Orden de compra, factura y recepción. Por lo que entiendo que dice Vero, cuando uno carga la factura, si depende de una persona, puede poner el precio y la cantidad que quiera, que no se condiga con lo que dice la factura real. Entonces nosotros tenemos que controlarlo contra el documento.

**Vikingo**: Claro, ese es el punto.

**Agustin Garcia**: Perfecto. Entonces lo que tendríamos que hacer ahí es leer el PDF para obtener esos datos y poder variarlos.

**Vikingo**: Sí, exactamente.

**Vikingo**: El tema es que el PDF no lo tenés en la base de datos de SAP. Yo no sabía que iban por eso. PDF va por BIN y BIN se guarda en otro lugar, no en la base de datos. Es otra estructura, o sea, aunque está

**Vikingo**: juntado, Perdón, Cristian, aunque está juntado en

**Vikingo**: la factura, no está dentro de la base de datos. Sí vos lo ves dentro de la aplicación de SAP, pero está en otra base de datos por fuera de SAP, ¿Entendés? Es otra base de datos. Antes estaba dentro de SAP, pero eso nos llevaba a que la base de datos crecía indiscriminadamente porque la gente subía

**Lucio Rojas**: huecos al de base.

**Vikingo**: Lo que hicimos fue poner BIM, y BIM lo que hace, si bien te lo muestra todo junto, accede a otro repositorio de datos donde están los PDF, pero ni siquiera están en formato PDF.

**Diego**: Claro.

**Vikingo**: Está, Sí, binario. ¿Tengo que saber cómo es

**Lucio Rojas**: Verónica, esto vos lo haces una cantidad? ¿Con qué cantidad de PDF lo haces? ¿Lo vas corrondo cuenta por cuenta o tenés que trabajar con un volumen muy grande?

**Vikingo**: En realidad siempre va a haber un PDF por una factura que se haya cargado por un documento factura que se haya cargado.

**Diego**: La gran ventaja de trabajar con IA es no trabajar con una muestra, sino meterla a todo el universo. ¿La gran ventaja no? Si nosotros lo tenemos que hacer a mano, obviamente vamos a tomar un muestreo, vamos a agarrar X cantidad de factura y poner satisfactor. Pero bueno, si eso no se puede hacer porque no está la info, vayamos con otra prueba distinta.

**Agustin Garcia**: De todas formas lo que podemos hacer, si quieren este caso lo dejamos como en standby y lo que pueden hacer es tal vez enviarnos dos, tres facturas que tengan como para que nosotros

**Vikingo**: Yo te envíe la factura en PDF, que le va a ser más fácil leerla a la IA y otra cosa, que te la envíen un binario comprimido dentro de un repositorio que genera B, que andá a saber encima dónde no conozco la estructura de Bin intern, porque Bin internamente la graba en disco, su base de datos en disco, pero sé que tiene punteros a los binarios que no sé cómo lo. Es un tema muy interno de Bean eso. Es más, vos sabés que a Gerson Diego le pidió, la chica que trabaja con Néstor le pidió algo parecido y tuvieron que ir a buscar los PDF directamente, subieron los PDF que ellos querían investigar, tomaron esa pila de PDF y le dijeron bueno, investigame estos PDF, ¿Entendés? Iba por otro lado lo que hicieron ahí. Por eso

**Diego**: le podemos dar acceso a una carpeta con todos los PDF.

**Vikingo**: Es que no tengo la carpeta. No existe una carpeta con PDF. No existe más eso.

**Diego**: No existe más.

**Vikingo**: Cuando vos ajuntas la factura, SAP ahora la toma el Ghost s, la convierte en una especie de binario y la graba en otro repositorio distinto. Tengo que sentarme con la gente de B. Es más, Gerson lo quiso hacer porque la quería buscar en su momento y hablamos con la gente de Bing y no hubo caso. Era como la gente de Bing decía, la única forma de encontrarla es por dentro de esa. Si no, la otra es tenés que entrar al GUI de SAP, entra a buscar la factura, apretás el botón y te la descargas. Pero es todo un laburo que hay que hacer.

**Lucio Rojas**: Claro, eso es todo.

**Vikingo**: ¿Sensación eso, no?

**Lucio Rojas**: Disculpen ahí para no dar si quieren en este caso, la verdad trincado, sobre todo por cómo trabaja Telamo, que es más con estructura de datos tabulares, podemos mostrarle nosotros con. Con Franco, qué hicimos partiendo de los archivos que ya están en esa app, y cómo ustedes capaz pueden imaginar que eso les lleva otro proceso, dejemos este

**Agustin Garcia**: caso como en stand by, como para ver, después vemos si es posible resolver el tema técnico, tal vez. Contanos ahí, Vero, si tenés algún otro.

**Vikingo**: Sí, porque se me estaba ocurriendo a ver si esto tal vez capaz hay que trabajar con tablas. Eso es una prueba que yo tengo que hacer, tal vez esto me ayude. Un segundito que quiero entrar. Quiero entrar a una.

**Diego**: ¿Ustedes tienen algún caso hecho ya? Le muestra.

**Lucio Rojas**: Sí, nosotros preparamos algo para mostrarles.

**Vikingo**: A ver. Yo si no se me ocurre hacer esta comparación de precio cantidad, pero ya con la carga de la factura, digamos. Pero tiene que ser, es una plantilla que va aparte, digamos.

**Lucio Rojas**: Bien, le mostramos la herramienta, ustedes véanla funcionando, y creo que va a ser mucho más fácil imaginar después, si querés compartir, Fran, el chat en el que estuvimos trabajando hoy. Ahí les cuento rápido. Nosotros lo que hicimos fue partir del backup de su SAP que nos compartió Cristian, e identificamos algunas de las. Es el otro. Lo que hicimos fue, en base a alguna de las tablas que ustedes no habían compartido, particularmente las que son de cuentas a pagar, crear algunos informes o algunos cruces de datos que son generalmente comunes, auditorías de cuentas a pagar. Preguntamos a Claude qué podríamos llegar a hacer y armar un informe con hallazgos de esa auditoría al proceso de cuentas por pagar desde las tablas de SAP, y que haga un informe con los hallazgos y las acciones recomendadas, categorizadas por criticidad y por factibilidad de resolución, como para mostrarles cuál es el poder de la herramienta trabajando

**Agustin Garcia**: ahí.

**Lucio Rojas**: Fran, ¿Estás compartiendo el Telamo? No, el chat de CL.

**Agustin Garcia**: Esto que le van a mostrar los chicos es un reporte, digamos, genérico, creado en función de los datos que ustedes tienen, como para que tengan también una idea. Digamos que el reporte, obviamente que podemos ir a los casos de uso particulares, pero también tiene una potencia de evaluarlo de forma más genérica todo.

**Lucio Rojas**: Ahí les contamos rápido cómo funciona la herramienta. A TheAmot se cargan directamente las tablas de SAP, y lo que hace es generar archivos de metadata con esas tablas y poder disponibilizársela a inteligencia artificial para hacerle preguntas para tomar contexto, para auditar o hasta incluso para buscar ciertos patrones de los datos. Entonces lo primero que nosotros hicimos desde CLOT fue pedirle Teramot que nos diga qué tablas B están relacionadas con el proceso de partidas de cuentas a pagar. Así que ahí abajo si querés mostrar Fran, lo que responde en base a

**Franco Ferrero**: la respuesta, acá hablo un poco las flechitas como para que entiendan un poco también cómo funciona, es un poco de las distintas query que va haciendo a través de SQL para buscar un poco lo que nosotros pedimos. Entonces bueno, acá tenemos las tablas que

**Lucio Rojas**: nos trajo y describe que desde la base de datos de SAP, entonces ustedes tienen que administrar la herramienta y no la base de datos. Eso por ahí ayuda mucho alguien que no tiene la capacidad técnica de estar revisando la base de datos en sí o el SAMEN, sí te dice, bueno, tenemos una tabla de partidas abiertas de proveedores, es una tabla clave con importe, fechas de vencimiento, condiciones de pago, indicadores, débito, crédito y moneda. La tabla BSIK, vemos la tabla B y C, D que es la equivalente pero de clientes, no es cuentas a par directo, pero sirve si querés que usaran los tipos o notas de crédito relacionadas, ve otra tabla que es de ítems de factura de proveedor y así nos distrófica las 17 tablas que están relacionadas con el proceso con cuentas por pagar. Nosotros qué le pedimos en un chat anterior fue que en base a las tablas que nosotros encontramos de cuentas por pagar, nos genere análisis que suelen ser útiles para un proceso de auditoría de cuentas a pagar. Generar tablas es tomar de estas tablas base, cruzar con SID, estoy dando ejemplos puntuales para generar nuevas vistas, nuevas tablas que tengan información que sea plausible de una auditoría con un sentido y con una lógica. Entonces las tablas que nos creó más abajo, si querés mostrar, fueron una tabla de antigüedad con la antigüedad de saldo por proveedor, Un libro de maestros de partidas abiertas por proveedor con bloques, condición de pago, si tiene orden de compra. Una tabla que analiza la Calidad del Maestro de Proveedores, detecta si hay huecos, si hay duplicado del Maestro de Proveedores. Una tabla de la concentración de deuda por proveedor, para saber cuáles son los proveedores que más tienen deuda. Una tabla para.

**Vikingo**: Notas de crédito,

**Vikingo**: Ustedes generaban tablas auxiliares donde tenían información consolidada o algo,

**Vikingo**: pero

**Diego**: este ya es customizado para los proveedores.

**Lucio Rojas**: Claro, antes habíamos visto algo más genérico.

**Vikingo**: Yo le estoy preguntando a la gente de OpenText que me diga a ver si hay forma de acceder a los documentos, por ejemplo, PDF de factura, proveedores que están en ese storage especial que maneja, para ver cómo por fuera de SAP acceder de ahí. Porque ya te digo, no está el PDF puro, como ustedes lo supen.

**Diego**: Pero igual acá lo que está mostrando Lucio está bueno porque es lo que le está tirando, lo que le dice Cloud. Primero le dijo, bueno, che, en base a una auditoría tradicional de cuentas por pagar, en base a las tablas que yo tengo, decime qué le puedo pedir. Me parece bien, sigamos.

**Franco Ferrero**: Una cuestión es que, a ver, todas estas tablas que ponele que nosotros generamos a través de Cloud, ustedes también, al tener un contexto mucho más técnico de lo que tienen que buscar, lo que más les sirve, también va a ser un poco más preciso a medida que le den más indicaciones. Esto fue, mira, tenemos

**Diego**: alguna idea para entenderlo. Después le metemos nosotros los prompt más

**Lucio Rojas**: específicos para que tengan el contexto general. Yo partí del mail, creo tuyo Diego, que decías, necesito revisar el proceso cuenta por pagar. Con eso armamos todo esto, lo único que teníamos. Entonces, ¿Qué hicimos? Le pedimos a Claude que con su contexto genere muchos cruces que son comunes a una auditoría de cuentas por pagar. Y una vez que tuvo todas esas tablas armadas, más las tablas, su origen de SAP, le pedimos que arme un informe de auditoría. Usamos el modelo más potente de Cloud, que es Fabel 5, y armó, si querés mostrar AFACT con varios hallazgos de auditoría, y la matriz de acción, primero hace un resumen general que dice que siempre el informe clásico, el resumen ejecutivo que tiene una auditoría, después se lo pasamos para que lo vean más en detalle. Pero si querés ir más abajo, quiero que veamos la matriz y después vayamos a los hallazgos en particular. Esta matriz tiene dos ejes. En el eje Y tiene el impacto en alto, bajo y medio. Y en el eje X tiene la probabilidad de resolución en bajo, medio y alto. Entonces, el cuadrante de arriba a la derecha son los hallazgos de la factura sin orden de compra, de las facturas con dedos vencidas según el informe de CL, lo primero que deberíamos trabajar. Así fue categorizando los distintos hallazgos que encontró en base a las tablas, y abajo los describe uno por uno. Y esto es lo que me interesa que leemos, porque es donde creo que hay ju, qué es lo interesante. Cuando ustedes vean estos hallazgos, pueden hacer doble, triple o cuádruple pic. Le pueden decir a Claude, anda a la tabla y fíjate por qué esto hay 33 partidas abiertas. Y acá que te dice el primer hallazgo en el texto no pagar, le ponen una instrucción de no pagar, pero no lo bloquean por sistema, es un examen en realidad se debería bloquear y no queda bloqueado con sistema. Entonces alguien puede equivocarse, no leer el texto libre y pagarlo igual. Y eso es un proceso, lo sujeto a una teoría de procesos, no debería pasar. Entonces un hallazgo accionable.

**Diego**: Y de hecho todos esos no pagar los dijimos nosotros que decían no pagar, por lo menos el que está ahí.

**Vikingo**: De pulmen.

**Diego**: De pulmen. Nosotros dimos la orden de no pagar y por eso no se pagó.

**Lucio Rojas**: Y ahí hay 33 partidas abiertas. Con ese texto libre vos le podés decir a Claude, con las tablas de SAP, tráeme las 33 partidas y las ves una por una. Y Así están los 10 hallazgos. Pueden ir leyéndolo ustedes van a hacer un poco más de zoom, así lo van viendo.

**Vikingo**: Partidos históricos. Si, no estaba leyendo los títulos.

**Franco Ferrero**: Sí, si quieren más que nada los títulos, después si querés saber, obviamente te lo podemos pasar.

**Diego**: Y todo esto lo Deuda con proveedores vencida. Mucho no me interesa, sería si fuese cliente. Sí son proveedores, la verdad que. Alta concentración de foco. Proveedor. Posibles facturas duplicadas.

**Franco Ferrero**: Acá te da la información, obviamente capaz de esto, capaz de hacer algo un poco más, un hallazgo más general. Después podés ir metiéndole más, o sea, trabajando directamente de Claude, decir Bueno, de estas 194 partidas que encontramos, ¿Cuáles están duplicadas? ¿Cuáles son? ¿Dónde están?

**Lucio Rojas**: Claro, ahí si quieren leamos bien este, porque está bueno tomar un caso y a fondo para no los títulos. Dice posibles facturas duplicadas, pendiente de pago. Se detectaron 194 pares de partidas con el mismo proveedor, mismo monto y coincidencia de texto o referencia dentro de una ventana de 30 días involucrando $118 millones o de pesos, 45 pares son de alta sospecha, mismo día y misma referencia. Casos como gama, movimientos portuarios, seis documentos idénticos de 14 millones, el mismo día, requieren verificación antes de cualquier pago. Acción recomendada, revisar los 45 pares de alta sospecha contra factura física FIP antes de la corrida de pagos y bloquear preventivamente los sospechosos. Activar la verificación de duplicados de SAP. Mensaje F, error de advertencia por referencia, más fecha, más monto responsable, cuentas a pagar, plazo dos semanas. Te da un plan de acción sobre un hallazgo puntual en este cargo que están cargando de lo mismo. Y vos ahí le podés decir bueno, tráeme los 45 países hechos. Así como este, tienen varios hallazgos. Y ahora sí, ya volviendo a la generalidad de una priorización. De todos los hallazgos. Nosotros partimos para hacer esto de un supuesto muy general, que era lo que imaginamos como concepto de que podían llegar a ser. Creo que la herramienta en manos de Verónica, supongo con el control de Diego, va a estar mucho más orientada a lo que querían hacer y siempre partiendo de tablas. Ustedes después pueden si quieren, a partir de pasarle algunas facturas a Cloud, hacer que lea las facturas y realiza algún proceso, Pero Cloud con Tegamop, que es nuestra tecnología, lo que hace es darle todo el contexto y el acceso a todas esas tablas de SAP para poder consultar si los PDF están guardados en otra base de datos como texto binario. No vamos a poder consumirlo desde Tela, va a ser difícil, salvo que después Cristian nos diga que sí se puede. Pero yo en un principio no lo veo tan sencillo este caso. Y Kia está hablando de prioridades y de capacidad de resolución. Primero con lo que podemos hacer, trabajar con estas tablas y que veo que bastante tener trabajo. Así que es un poco el lo que mostramos de la herramienta. Ahora le pueden tirar algunas preguntas si quieren en vivo para ir resolviendo, ya que entienden cómo funciona, nos dicen y le preguntamos.

**Diego**: Ahora en el momento estaría bueno saber si algo. Siempre probamos es anticipo otorgado a proveedores que se encuentren pendientes de aplicación.

**Franco Ferrero**: Perdón, no escuchen qué pregunta quieren que le hagamos.

**Diego**: Muchas veces ha pasado. Muchas veces ha pasado y no sería algo loco de encontrar. Da anticipos a proveedores, proveedor factura y ese anticipo queda sin aplicar y se le vuelve a pagar la factura completa al proveedor.

**Lucio Rojas**: Pregúntale Fran, eso, explicale que a veces se dan anticipos a proveedores y después no se reparaciona la factura y se genera un doble pago. ¿Puede identificar algo parecido a eso?

**Diego**: A veces se anticipo proveedores que al momento de recibir la factura, la misma se paga sin aplicar el anticipo otorgado.

**Lucio Rojas**: Anticipo otorgado. Esto sería si vos das un anticipo y no lo vinculas contra el cliente

**Diego**: y el control se hace de manera manual, entonces muchas veces queda pendiente.

**Vikingo**: Claro, se carga. Normalmente el anticipo se carga dentro de la misma orden de compra. Entonces cuando llega la factura que se aplica en esa orden de compra, se carga en esa orden de compra, debería aplicarse el anticipo a la hora del pago, pero normalmente la factura de anticipo y la factura de compra final conviven en la misma, están nucleadas en la misma orden de compra.

**Lucio Rojas**: Explicar un poco eso, Fran, y decirle que te haga dos o tres preguntas antes para asegurémonos que él entienda bien el problema. Decirle, explicárselo, decirle haceme dos, tres preguntas para que responda el equipo y pueda asegurar

**Agustin Garcia**: acá.

**Diego**: Sí lo entendiste. No lo había pensado eso. Decir, hacer un par de preguntas para

**Lucio Rojas**: ver si eso lo.

**Franco Ferrero**: Ustedes a ver, vayan ayudándome, así también lo hacemos juntos.

**Diego**: A ver qué dice. Sí cuando ya la factura finanza. Bueno, sí se desembolsa además y anticipo que ha colgado muy bien, eso debería aparecer como partida con signo de deudor, convirtiendo con factura sacadora al mismo proveedor sin compulsar entre sí para armar bien el control. Quiero confirmar tres cosas, qué es lo que dice ahí abajo.

**Vikingo**: ¿Cómo se registran los anticipos en SAP normalmente?

**Vikingo**: Si, no, a ver, a los que estamos apuntando, entiendo que se registran con el indicador, el primero que dice indicador

**Franco Ferrero**: CM, cuenta especial tipo DOC E,

**Vikingo**: porque tengo entendido. A ver, estamos igualmente auditando el circuito, pero si no cambiaron las cuestiones, digamos, el procesamiento este es. Ya lo evitamos en algún momento este proceso y lo estamos volviendo a evitar. Se registran con el indicador CM cuando se aplica un anticipo, cuando se da

**Diego**: de alta un anticipo igual entendió bastante bien al problema.

**Lucio Rojas**: Sí, porque. Anticipos abiertos con facturas ya pagables del mismo proveedor prevenir.

**Vikingo**: Y el dos también, el segundo me parece. Ambos, ambos.

**Franco Ferrero**: ¿Cómo se vincula el anticipo con su factura? ¿Por orden de compra, dijimos, no?

**Lucio Rojas**: El tema que no tiene las órdenes de compra vinculadas. Esto es lo que hemos visto antes,

**Vikingo**: mira, por lo menos el anticipo se carga dentro de la orden de compra, por lo menos esto que estamos haciendo referencia. Con lo cual entiendo que si esa factura de anticipo se carga en la orden de compra, en alguna parte tiene que estar esa orden de compra asociada.

**Lucio Rojas**: Fran, quería cerrar el banner al costado.

**Vikingo**: Igual vemos que trae.

**Lucio Rojas**: Vamos a ver que ahí lo que hace es, a partir de las tools, que son las herramientas que ir a consulta, primero tiene la metadato, entonces entiende el contexto de las tablas, pero después tiene que ir a buscar datos en sí. Entonces para buscar los datos en particulares usa una tool, una herramienta dentro de CP que se llama Query Data, que lo que hace es ir y hacer una query de tabla para fijarse esa información, traerla, van a ver que va a hacerse la información y después va a razonar internamente la información que junta y nos va a elaborar una respuesta. Y esto hasta incluso se puede pedir que se estandarice. Que se estandarice una alerta. Entonces si la base de datos está conectada en vivo, cada vez que ve algo similar, un comportamiento anómalo, en este caso lo alerte antes de que.

**Vikingo**: OK, bien,

**Lucio Rojas**: Si tocas el identifico riesgo, a ver si está. Si se muestra cómo razona. Sí, ahí se muestra el razonamiento que va, que va haciendo el modelo. Entonces esto es muy interesante. Puedes ver cómo piensa los chips.

**Vikingo**: Listo. A ver, acá dice, Es poco que

**Diego**: dice el primero tiene anticipo y facturas que están por pagar. Eso no quiere decir que se haya

**Lucio Rojas**: hecho

**Diego**: el vínculo por tampoco probado.

**Lucio Rojas**: Eso es lo que le había dicho.

**Diego**: Vienen con EB, qué es eso qué

**Lucio Rojas**: entiendo yo los anticipo por lo que había visto hasta ahora en el comportamiento Ebeln. Podemos pedirle que nos lo explique. Mientras tanto es donde se registran las órdenes de compra, me parece. Y creo que no está bien vinculado la orden de compra con la factura, con el anticipo.

**Diego**: Bueno, pero puede pasar que muchas veces no machea el anticipo con la factura, ¿O no, Vero?

**Vikingo**: Sí, puede pasar, sí, sí, sí. Lo que pasa que sí no sé Si a lo mejor ese dato, porque digo, si el anticipo, la factura de anticipo está cargada en la orden de compra, digo, en alguna parte está hecha la vinculación, capaz habría que ver, digo, yo pienso, o sea, esto ya no lo imagino, capaz está haciendo la búsqueda, puede ser en algún campo o en alguna tabla donde no está ese dato.

**Lucio Rojas**: Y capaz vemos ahí la respuesta, que creo que es bastante explicativa, vamos a decir. Internamente es el número de orden de compra en SAP. Como SAP dice que se registra orden de compra, viene el alemán, el identificador único que SAP le asigna cada orden de compra cuando se crea, y es la clave que conecta todo el proceso de compras. La cabecera de la orden está en el KEP, en ECO, que es otra tabla. Su posición es en ECO, que es otra tabla. Muestra cómo arma todo acá, qué es lo importante. Cuando una factura o un anticipo se registra con referencia al orden de compra, está referenciando el campo de Belén y este queda cargado en la partida contable, que es lo que después se usa para hacer todos los macheos y dentro del sistema de SAP retomar toda esa lógica. Y te dice, en el caso de HZ, que es lo que había encontrado antes, que está. Lo que yo quise decirles, el dato relevante es que ese campo viene vacío. Casi siempre. Las facturas no se registran contra la orden de compra, es el hallazgo H de Maverick Bayen, que es una de las tablas que armamos para hacer sobre. Y los anticipos tampoco se registran. Por eso te decía que el vínculo anticipo y factura no lo podemos armar por EBR, como idealmente sería, sino por proveedor más monto más fecha. Es como que detectó una rota en la cara. Ahí podemos preguntarle si lo podemos buscar de otra forma o cómo se resolvería. Acá una salvedad que es importante aclararla. Puede ser que ustedes lo estén haciendo de esta forma, que no lo están cargando, pero también puede ser que cuando hicimos el traspaso del backup, ese campo se haya vaciado. No estoy del todo seguro, pero por las dudas hago la salvedad para no atacar directamente el proceso. Pero bueno, por lo que estoy viendo, creo que están.

**Diego**: Pero para, porque eso que acaba de decir a mí me genera, digo, ¿Es confiable la información que ustedes traspasan?

**Lucio Rojas**: Sí, sí, sí.

**Diego**: Yo no puedo confiar en eso. Todo lo que me traiga de vuelta, después lo tengo que rechequear y tengo que hacer el laburo, ¿No?

**Lucio Rojas**: Sí, sí, el 99% de las veces sí está confiable. Pero yo quería hacer esa aclaración por las dudas de que estemos eso y que haya un error. Pero podemos decir, le puedes preguntar al mismo club, siempre fíjate si ese campo realmente viene vacío o hay algún error en la consulta.

**Diego**: OK,

**Lucio Rojas**: bien. Ahí te dice que hay campos muy poblados. En otra, Vamos a ver que termina de responder. Siempre lo que tiene muy bueno, yo lo uso mucho cuando tiramos para procesos de discutir, valga la redundancia, algún traspié en algún proceso o algún error en los datos, es que te podés poner muy incisivo con la pregunta. Te puede decir, anda a la tabla a fijarte, explícame por qué, explícame cuál es la otra opción. Sí, explícame cómo vienen estos datos de la fuente, explícame el procesamiento que hiciste. Eso es lo que decía Diego, que siempre se puede repreguntar bien cuál fue el proceso y la lógica que aplicó.

**Vikingo**: Mientras que la factura se llama.

**Franco Ferrero**: Resultados concretos. Te dice también cómo lo piensas.

**Vikingo**: Se le puede preguntar capaz, no sé si ya es otra instancia, que si esa orden está cerrada, porque tal vez hoy, digo, por lo que leí rápidamente, tal vez esa orden de compra todavía no está cerrada. Por lo que veo hay un anticipo mayor de las facturas que se recargaron, ¿No? Pareciera, porque dice 18 facturas contra 50 facturas de anticipo, como que pareciera que hay una parte que todavía, o sea, porque tal vez todavía no está termina orden de compra que esté como en entrega final, digamos, como para sostener que bueno, quedó ese saldo, digamos, sin utilizar.

**Franco Ferrero**: Claro, finalización sería.

**Vikingo**: Sí, SAP tiene como, no sé, a nivel tablas, a nivel vista, hay una opción que se llama entrega final, que creo que está en recepción, que es un tilde de entrega final, están todas las posiciones de la orden de compra, digamos.

**Franco Ferrero**: Y esto es porque tenemos más anticipos.

**Vikingo**: Claro, más anticipos que facturas cargada. Entonces se me ocurre que digo, o sea, igual el análisis que hizo está bien, pero si la orden de compra no está cerrada, o sea, igual es un caso. A ver, puede ser que

**Franco Ferrero**: lo bueno de esto es que, a ver, ya como es como trabajar directamente con Claude, te abre mucho más las riendas a empezar a hacer preguntas un poco en base y cuanto más contexto le das y un poco más le explicas, teniendo también un contexto ustedes mucho más completo de lo que quieren, es capaz como hacer preguntas más puntuales.

**Vikingo**: Bien, sí, sí.

**Lucio Rojas**: Hay que ver si está dentro de las que le dimos para la prueba.

**Franco Ferrero**: ¿Ves? Acá dice a ver si se va a fijar si la orden de compra está marcada como terminada cuando los anticipos terminan abiertos.

**Lucio Rojas**: Claro, acá lo que pasa es que entiende bien el modelo de tabla y las columnas, entonces sabe dónde fijarse lo que es la base de datos. Es algo que por lo menos nosotros vemos en otros casos que no es tan sencillo tener conocimiento profundo sobre cómo está constituida la base de datos de SAP, sobre todo por el nombre de las columnas y por qué no es uno de. Hay perfiles que se vuelven muy expertos en chat por esto, porque es particular el modelo. Sin duda, hay que aprenderlo, lleva mucho tiempo aprenderlo y esto ya lo tiene incorporado. Y fíjate que si le pedís algo, sabe dónde buscarlo.

**Diego**: ¿Cómo estamos seguros que tiene todas las tablas que nosotros necesitamos que tenga?

**Lucio Rojas**: Bien, ahí lo que hizo Cristian fue pasarnos el backup de la base de datos.

**Diego**: Entonces, ¿Qué base de datos, Cris? ¿Vos pasaste todas las tablas?

**Vikingo**: Todo, Todo, todo completo.

**Lucio Rojas**: Un backup completo.

**Diego**: Ah, OK. Ah, bueno, listo.

**Vikingo**: Sí, a mí lo que acá me. Lo único que yo. Perdón por ser tan escéptico de esto.

**Diego**: No, dale, siempre viene bien un sombrero negro.

**Vikingo**: No, no, yo te doy otra mirada. La mirada de. Yo sé que lo que me está diciendo es realmente verdad hasta no verificar, porque hay un laburo tuyo, digo, si hay algo que vos haces, Diego hoy, es cuando vos levantás un riesgo de auditoría, estás 110% seguro.

**Diego**: Por eso yo estoy tranquilo de que esto no me va a reemplazar y no me voy a quedar sin trabajo.

**Vikingo**: No, no te digo eso. No, Vos tenés que validar. Si vos decís, mira, para validar esto yo tuve que hacerle 400 millones de

**Lucio Rojas**: preguntas,

**Vikingo**: o por ahí no estamos entendiendo bien a dónde queremos llegar, porque en algún momento vos te querés como che, ayúdame a hacer los informes de teoría con esta herramienta y no andar buceando en todos los datos de SAP que no me genera nada.

**Vikingo**: Ah, mira, ven acá.

**Lucio Rojas**: Para mí el valor está ahí, Diego.

**Diego**: Mirá, el amigo, eso lo acabamos de ver Eso es cierto. Son todos despachantes de aduana.

**Vikingo**: Está bien, hizo la U.

**Lucio Rojas**: Sí, no sé si para mí es

**Vikingo**: como que falta acá el tilde para decir, che, ¿En qué momento compruebo que lo que me está diciendo es realmente? Porque vos decías, Verónica, yo tengo uno que hice, ya me gustaría verlo con ese que hice para ver si llegó el mismo resultado.

**Lucio Rojas**: Claro, a mí me gustaría saber cómo lo haces antes, usar esta herramienta a corroborar que algo está bien. Porque lo que yo entiendo es que como dice Diego, no te reemplazan, sino que a vos te da la capacidad de, en vez de partir de una hoja en blanco, partir de todo, una fase de discovery, por lo menos hallazgo. Y por eso.

**Vikingo**: Tiene que entrar.

**Vikingo**: Claro, eso es lo que por ejemplo,

**Vikingo**: legin tiempo enorme acá es, che, te pregunto, sin entrar a las transacciones, seguro que tiene que ser mucho más rápido, pero el tema es cómo me aseguro que lo que me está dando es realmente llego a lo mismo que lo que hacía Verónica, forma manual.

**Lucio Rojas**: Por eso te decía que tenés la posibilidad de pedirle una auditabilidad al propio script, lo que hizo que te explique, si querés, puede pedirle las query SQL, puede decirle que vaya a la base a fijarse y hasta incluso que no se fije en la base, sino que se fije en la nuestra, sino que también se fije en lo que ustedes nos dieron, porque hay dos instancias que ustedes nos dan y como nosotros los levantamos y como lo pasa, podemos mirar los tres estadios. Nosotros hicimos la balonce y ha sido la bol. Nosotros trabajamos.

**Diego**: Yo te lo digo como auditor,

**Franco Ferrero**: a

**Diego**: mí esto me sirve. ¿Por qué? Porque por ejemplo, ahora me trajo el universo de todos estos anticipos están otorgados y están pendientes de aplicar. Bueno, obviamente que yo no voy a darme vuelta a escribir un informe con esto que dice ahí. Ahí ya entra el criterio profesional del auditor, que tiene que ser capaz de ver que eso realmente sea real. Entonces me meteré en la cuenta del despachante de aduana y corroboraré de alguna manera que esa guita se le dio, cuándo se le dio y chequearé. Pero ya me trajo el análisis, el caso para analizar puntualmente. Y de hecho te digo que eso que está trayendo es real, porque sacamos un informe hace dos días. Entonces digo, está bueno, primero por qué yo creo que la principal ventaja que tiene la IA para auditoría es no trabajar sobre muestras, sino trabajar sobre el universo. Eso para mí es lo mejor que tiene. Y después obviamente me trae, me reduce la auditoría a unos pocos casos que obviamente tengo que poner criterio profesional. Como cualquier pregunta entiendo que uno le hace a la inteligencia artificial. No imagino un abogado haciendo un escrito con inteligencia artificial, después lo tiene que releer, chequear y que no esté hablando boludeces, porque sabemos que delira también tiene delirios, ¿O no? Díganme chicos si no está equivocado.

**Lucio Rojas**: Por eso a mí me parece importante dos cosas. Nosotros usamos el ejemplo con los programadores. Nosotros a veces programamos para. Yo no soy técnico, lo uso para programar. Lo que hago es un 6, lo que hace un programador es un 9, un 10. Trae el criterio de entender qué es lo que le está devolviendo como código la inteligencia artificial y mirarlo, corregirlo y debatirlo. Y acá lo que nosotros te damos para eso, muchas herramientas que nosotros le sumamos a Tegamo, que son la posibilidad de ir a ver los datos y de explicar y debatir contra vos, con vos sobre las tablas.

**Diego**: Bueno, está bien. OK. Más allá ahora, lo que está tirando, entiendo que se usa de la misma manera que si estuviese interactuando directamente con Claude, pero a través de The.

**Lucio Rojas**: Lo mismo.

**Diego**: Probémoslo. Vamos a probarlo. Vamos a probarlo. Déjanos tener la herramienta y después te daremos un feedback de si nos sirvió, cómo nos sirvió, cuánto nos sirvió. ¿Te parece?

**Lucio Rojas**: Perfecto. Yo creo que esa es la mejor forma. Esto es usar Cloud nada más. Que tiene cloth, como un conector extra. Téramoto se configura con dos clics sobre las tablas. Nosotros queríamos hablar de eso un segundo, de las tablas que ustedes tienen que tener disponibles para la prueba. Vos Diego, habías mencionado que querías.

**Diego**: ¿Está bien al 30 de junio? Si, lo hacemos el 31 de mayo. Lo hacemos el 31 de mayo.

**Lucio Rojas**: Bien, vamos con eso. Listo, vamos con eso entonces.

**Diego**: Vamos a arrancar al 31 de mayo y después veremos si hay algo que amerita extenderlo el último mes, iremos y nos meteremos.

**Vikingo**: Pero acordate que la base que yo les Di a ellos.

**Lucio Rojas**: ¿De qué fecha, chicos?

**Franco Ferrero**: ¿Treinta de mayo dijiste?

**Vikingo**: Les dije el otro día eso y después me quedé pensando porque nosotros volvimos a hacer una restauración de la base de sandbox hace poco.

**Diego**: Lleva mucho tiempo esto de tener la base actualizada ahí.

**Lucio Rojas**: Eso quería hacer el. Siendo muy claros ustedes, nos pasaron el backup de la base de datos entera de SAP. Eso pesa 300 GB comprimido y 2 teras para mantenerlo vivo restaurándolo en SQL Server. Lo cual a nosotros nos incurre un costo y un mantenimiento que por ahí excede la PO. Lo que ustedes pueden hacer es, con el mismo clot que tienen ahí, la única digo, es listame las 20 tablas que son esenciales para hacer un análisis de. Nos pasan esas 20 tablas. ¿Como se?

**Vikingo**: No puedo pasarte tablas separadas de la base de datos.

**Lucio Rojas**: Ah, no, no se pueden bajar. No

**Vikingo**: es un motor de base de datos completo. Son 200.000 tablas más la Z. Yo te hago un backup de toda la base de datos. Si vos me pedís que yo empiece a entrar tabla por tabla y haga un extract de las tablas, un CSV

**Lucio Rojas**: a los últimos, ponele, con otros clientes,

**Vikingo**: ellos me pasan no sé qué tablas. Me tendría que decir qué tablas. No sé qué tabla.

**Lucio Rojas**: Claro, te decimos qué tablas y los

**Diego**: 200.000 tablas son 20.

**Lucio Rojas**: No, en realidad es que son 20.

**Vikingo**: Tiene claro que donde está la información son 20 tablas. Yo las 20 tablas me las dice y puedo hacer un bulk que es de esas tablas, llevarlo a un CCB.

**Diego**: Eso es lo que necesitamos, para qué mantener una tabla. No, no, no, por eso.

**Vikingo**: Si, es así. Sí, si, es así.

**Lucio Rojas**: Sí, sí, sí. Eso es lo que. Por eso decía. Preguntémosle a Clop.

**Vikingo**: Yo pensé que vos necesitabas un tabla sola nada más. No, eso no podía ser.

**Lucio Rojas**: Yo necesito las tablas esas para trabajar y las cargan al día.

**Diego**: OK, sumémosle todo lo que es proveedores, obviamente, y sumémosle también la base de datos de clientes, porque por ejemplo, a mí me interesa saber qué proveedores son clientes.

**Lucio Rojas**: Ahí, Vero. ¿Fran, podés volver a compartir vos y preguntarle a Claudia ahora cuáles son las tablas que tendríamos que tener para este caso? Y las pasamos ya a feliz Y que. Cuáles son las. Correspondientes.

**Vikingo**: Cuáles son las ta correspondientes.

**Lucio Rojas**: Cuentas a pagar Y pedirle que sume las dos pedidos y los dos universos que dijo Diego, que son los de clientes y proveedores.

**Vikingo**: Maestro de cliente y proveedores. ¿O tablas de movimiento?

**Diego**: Eso, maestro o movimientos y traemos el maestro.

**Vikingo**: Maestro son los datos, perdón, y movimientos es las dos cosas. Maestro pueden ser los dos maestros. Y operación, digamos, o sea de proveedores,

**Diego**: por supuesto, todo cliente, proveedores, todo, pero de cliente, con que me traiga el ABM yo detecto si sea cliente y proveedor, el texto está bien. Perdón, sobre la auditoría, el proceso de cuentas a pagar y pone que inicia desde la generación de la orden de compra, pasando por la recepción del servicio, la mercadería, Hasta llegar al correspondiente pago. Ese es más detallado, decime ver o si me olvido algún paso,

**Vikingo**: Ese es el ciclo.

**Lucio Rojas**: Bien, y después lo otro que pusimos después sobre sumando las cuentas de clientes,

**Diego**: lo dejamos que se me sume, además de todo eso que me sube el maestro de cliente, el maestro cliente solamente maestro cliente va a ser una sola tabla.

**Lucio Rojas**: Y arriba, después mueble la parte de arriba, te liste cuáles son las tablas ahí arriba todo, listame las tablas que querés correspondiente. Bueno, ahí nos va a devolver las tablas y esas las.

**Diego**: A ver cuántas.

**Lucio Rojas**: Esto lo sabes por la base y también por lo que entiende de contexto

**Vikingo**: el Conómetric CSV es con los nombres de los campos, las columnas, ¿No?

**Lucio Rojas**: Sí, el nombre del campo. Y. Sobre generación de REN compra está bien,

**Diego**: Mira, ¿Por qué dice pedir, pedir, pedir?

**Lucio Rojas**: Porque hay dos. ¿Nosotros que hicimos? Levantamos la base de datos completa, la restauramos SQL Server, y después eran, no me acuerdo si me dijo el de Bob que eran 17.000 tablas o 70.000.

**Diego**: Igual hiciste un stack, entonces, Y tampoco

**Lucio Rojas**: sabíamos con cuál iba a trabajar, entonces hicimos como un muestreo, después borramos la tabla por mantenerla, entonces ahí la columna esa de pedir o no, tendríamos que reemplazarla por pasarla actualizada. Pasan esas tablas actualizadas y nosotros las cargamos.

**Diego**: Bueno, por acá te dice cuántas tablas, cuántas tablas son en total, pregúntale a ver cuántas son y listo.

**Lucio Rojas**: Que las. Si nos fuimos a hacer de esas tablas puntuales y todo el universo de vuelta, para nosotros también es mucho más fácil.

**Diego**: Sí, claro, obvio.

**Lucio Rojas**: Después lo otro también se puede hacer, pero como digo, no en el contexto de una POG de poder levantar todos los datos o se puede hacer el conector directamente.

**Diego**: Son 31 tablas, ahí está.

**Lucio Rojas**: Si no se posee el conector directamente a la SQL Server con túnel. Eso para más adelante. Ya se mantiene todo actualizado en vivo en algún momento.

**Diego**: Esa es la que nosotros apuntamos a generar los indicadores y que me traiga las alertas en vivo.

**Lucio Rojas**: Claro, vos generas las tablas y ya queda. Genera los ETL y ya se actualiza todo sin de qué repetir.

**Diego**: Son 31 tablas. OK.

**Lucio Rojas**: ¿Ustedes necesitan el histórico, lo necesitan de un tiempo en particular, porque tampoco es lo mismo traer 20 años para atrás, no?

**Diego**: La última auditoría que fue en el año 2020.

**Vikingo**: En el año 2022. 2022 fue la última auditoría y habremos visto hasta junio 2022.

**Diego**: ¿Es mucho pedir cuatro años?

**Lucio Rojas**: Definitivamente, mejor que pedir todo, lo cortamos el último cuatro años

**Diego**: al 30 de junio.

**Franco Ferrero**: Bueno, porque más que nada las tablas que acá nos dicen que ya las tenemos en el proyecto, si las van a querer actualizar, las vamos a tener que pedir de vueltas.

**Diego**: Claro, sí, hay que pedir esas 31 tablas. ¿Que? Cristian, Cristian, es muy jodido hacer eso.

**Franco Ferrero**: ¿Qué cosa?

**Lucio Rojas**: No escuché.

**Diego**: Extraer esas 31 tablas nada más.

**Vikingo**: Sí, pero las tengo que extraer completas, no puedo parsearlas por fecha.

**Diego**: Para nosotros mejor.

**Vikingo**: Déjame ver. Estoy haciendo un script para extraer una nada más, a ver si con esa me va. Decime un nombre. Una de las tablas.

**Lucio Rojas**: A ver.

**Franco Ferrero**: Una de las tablas. Ek.

**Lucio Rojas**: Ahí pedí a Fran que te arme un. Arme un informe con un pedido de solicitud.

**Diego**: Cacao.

**Vikingo**: Sí, bueno, momentico. Punto ccd, a ver qué dice acá.

**Lucio Rojas**: Informe con informe.

**Vikingo**: Tan chica la tabla. No, error, digo error, no me pierdo mi resultado. Se puede sangar Open Connection entonces por ese error. Ah, no, no, para.

**Lucio Rojas**: Culpa.

**Vikingo**: Bueno, pásenme las tablas esas y me las pueden pasar en Excel anulado para así yo las almo les primero cómo se las paso.

**Franco Ferrero**: Dale Diego. Cristian, perdón

**Lucio Rojas**: ahí, Cristian, si querés dejar de compartir y si lo enviamos por mail y después ustedes, o la pueden cargar ustedes directamente la herramienta. Bueno, después lo vemos. Última te pasamos el bucket TC Cristian, para que lo cargues ahí.

**Vikingo**: ¿Qué cosa?

**Lucio Rojas**: Que después vemos cómo nos las pasan. Si, le pasamos el bucket s para cargar esas tablas nomás.

**Vikingo**: Tengo que ver cuánto ocupa en el CSV, por ahí las comprimo y se las mando, pero quiero ver un poquitito, a ver cómo hago la extracción más rápida.

**Diego**: Y una vez que Cristian tenga las tablas, ¿Cuándo podemos empezar?

**Lucio Rojas**: ¿Cuando nivel las carguemos? Generalmente las cargamos en el día, así que

**Diego**: hacemos una mini reunión para que nos enseñes, para arrancar, porque ya la auditoría está en curso y cuanto antes arranquemos mejor. Así ya. Y después puedo, podemos medir los resultados.

**Lucio Rojas**: Y ahí Diego.

**Agustin Garcia**: Y ahí Diego contá con que tengamos algunas reuniones recurrentes cada tanto, como para darles una mano por si se encuentran con algún tema puntual que no están pudiendo avanzar o que algo no les cuadra, cuenten con nosotros para poder acompañarlos en ese proceso también.

**Diego**: Buenísimo. Además aparte lo podemos medir, nosotros podemos medirlo mucho en horas. Nosotros más o menos para esta auditoría debería asignada, no sé, 200 horas, 205 para ver, bueno, che, mira, aplicando esto, inteligencia a través de Teramon, en vez de 200 la redujimos a tanto, o sea que en el transcurso que hago una auditoría, tal vez con esto puedo hacer dos.

**Lucio Rojas**: Claro, eso para nosotros es revalioso.

**Diego**: Claro, claro. Y realmente de eso me tengo que agarrar para darme vuelta y bueno, después ver qué onda, cómo sigue esto.

**Agustin Garcia**: Perfecto. Bueno, quedamos entonces en contacto y vamos avanzando, ¿Les parece?

**Diego**: Sí, sí, sí. Bárbaro.

**Agustin Garcia**: Bueno, muchísimas gracias por el espacio.

**Diego**: Gracias,

**Lucio Rojas**: tengan buena tarde.
