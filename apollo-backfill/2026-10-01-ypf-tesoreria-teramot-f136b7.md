# YPF Tesoreria - Teramot 

**Fecha:** 2026-10-01T15:03:05.015+00:00  
**Duracion:** ~61 min  
**Participantes:** Bruno Ruyu <bruno@teramot.com>, Franco Ferrero <franco.ferrero@teramot.com>, Lucio Rojas <lucio@teramot.com>, Paula Cordeviola <p.cordeviola@ypf.com>  
**Externos:** p.cordeviola@ypf.com  
**Apollo ID:** 6abe84967dd6a90010f136b7

---

**Lucio Rojas**: Y tengo los auriculares conectados. Voy a elegir acá.

**Bruno Ruyu**: Hay que ver si esta piba le dejan entrar a Team Sleeper.

**Lucio Rojas**: Hello. A ver, ¿Me escuchan bien ahí? Sí.

**Bruno Ruyu**: Bueno, ahí le mandé un WhatsApp a Paula.

**Lucio Rojas**: ¿Cómo se llama el de HZ que conoces vos?

**Bruno Ruyu**: El de HZ qué.

**Lucio Rojas**: El flaco de HZ que conoces

**Bruno Ruyu**: se llama Juan Pablo. Voy a ver si está acá en

**Lucio Rojas**: el evento, porque lo vi a este Cristian,

**Bruno Ruyu**: ¿No? Juan manuel ramos. Juan manuel ramos.

**Paula Cordeviola**: Buenas.

**Bruno Ruyu**: Buenas. Gracias, Pau. Tanto tiempo.

**Paula Cordeviola**: Tanto tiempo. Sí, sí. Todo bien.

**Bruno Ruyu**: Bien, todo en orden.

**Paula Cordeviola**: Me alegro, me alegro.

**Bruno Ruyu**: Bueno, sí, a Franco se le mete un poco de ruido. Acá está con nosotros Franco, que es nuestro equipo comercial. Y Lucio, que es del equipo de implementación, que es quien estuvo trabajando con el equipo de laboratorio.

**Paula Cordeviola**: Ah, buenísimo, genial, genial. Con Lau que estuvieron. Que estuvieron viendo como para ver si algo me podría impactar a mí.

**Lucio Rojas**: Eso vamos a contar.

**Bruno Ruyu**: Si querés yo te hago. Te hago pausa súper, súper rápido.

**Paula Cordeviola**: Dale.

**Bruno Ruyu**: Y después la idea era que Lucio te lo muestre incluso.

**Paula Cordeviola**: Ah, bueno, dale, dale. Y ahí después les cuento mi necesidad.

**Bruno Ruyu**: Dale. Una. Pero bueno, básicamente a mí se me ocurrió resolver este problema por todo mi tiempo encontrado de gestión ahí en YPF, que era conectarse a mil sistemas, a SAP, a todo lo de AppStream, sacar la info Excel, procesar para sacar tablero, para hacer análisis. Eso era el día a día de las 15 personas que estaban en control gestión. Entonces lo que construimos es esta herramienta que en lugar de tener que hacer todo a mano, o en lugar de tener que ir a sistemas o IT a pedir que te armen las conexiones, el Data Warehouse, que te mapeen la información, que te armen los dashboards, que todo eso que hace sistemas se haga solo. Entonces nosotros agarramos la herramienta, la conectamos a SAP, todos los sistemas que tengan, o a los EXE que usen, el que sea, y más o menos en una hora ya entendió toda la información que tenés, la mapeó, la documentó, le corrigió errores, si hay cosas duplicadas, si hay faltantes, si uno está en inglés y otro está en castellano. Hace todo eso que haría el equipo de tecnología y te deja que después desde una inteligencia artificial vos les digas qué necesitas. Y ahí es como les podés plantear desde armame los dashboards de tal cosa y tal cosa, tal cosa, o analízame a ver si acá hay un problema, o quiero hacer una optimización de. De cómo cobramos a proveedores, o quiero entender a quién le puedo prestar plata, ¿No? De golpe tenés a chatgpt o a Claude o a Semina, pero laburando con tu información y entendiéndola. Entonces es bastante amplio lo que se puede lograr. La clave es que es rápido y que es autónomo en el sentido de que no tenés que estar llamando a ningún otro equipo, lo hacen y lo que hay que saber es chatear. Si sabes chatear, lo sabes hacer.

**Paula Cordeviola**: ¿Cómo se llama la herramienta?

**Bruno Ruyu**: Teramot. Así que bueno, eso un poco a nivel general lo que hace es básicamente poder manipular información sin tener que depender de otros equipos de tecnología. Y los primeros resultados lo ves el primer día.

**Paula Cordeviola**: Perfecto.

**Bruno Ruyu**: Obviamente es como todo, lo tenés que ir laburando, tenés que ir chequeando. Pero por ejemplo, lo que tiene bueno es que cuando metes a la inteligencia artificial a trabajar con vos, podés hacer cosas que son buenísimas, como, no sé, vos tenés unos dashboards que te los hace IT en Power BI, y cada vez que querés cambiar algo, tardan un mes. Vos decís, no tenés que decirle a Theramo cómo calcular todo. Decís, mirá, yo quiero capturas pantalla, se lo pegás, se lo mandas y decís, reproducime este dashboard. Y te lo va a hacer desde el origen de la información. Es decir, va a hacer todas las transformaciones, va a combinar toda la información, va a hacer todos los cálculos y te va a hacer el dashboard sin que vos le expliques cómo. Obviamente algunas cosas vas a tal vez explicar, pero te acelera de una forma que era impensada. Hace gozal.

**Paula Cordeviola**: Sí, sí, sí, sí, olvídate.

**Bruno Ruyu**: Y eso es como la descripción general.

**Paula Cordeviola**: Genial.

**Bruno Ruyu**: Si querés Lucio, contá un poco.

**Lucio Rojas**: Me presento ahí rápido. Yo soy parte del equipo de implementación de Customer Access, trabajo con un tiempo y estuve yendo a YPF a trabajar con este caso puntual de cobranzas y explicarte bien qué hicimos, qué resultados hay, cómo lo hacían antes, como lo hacen ahora. Y mientras tanto trato de explicarte un poco de productos. Armé una presentación que cortita, son 10 diapositivas, trato de que lleve 10 minutos, pero para entender bien el caso y a probar la herramienta y a jugar un rato. Es lo realmente tenido. Así que anda preguntándome, frenándome, dale, dale. ¿Intercambiando Ahí chequeo que estamos viendo? No se ve bien.

**Paula Cordeviola**: Sí.

**Lucio Rojas**: Bueno, nosotros somos TER, Bruno es el CEO, el founder, Tenemos una herramienta, es un SaaS que se encarga de todo lo que es la parte de ingeniería de datos. Y estuvimos trabajando qué pasaba en el equipo de cobranzas puntualmente, que es que todo lo que era el BI y el análisis de información desde sus app llevaba mucho tiempo. Nosotros trabajamos una pregunta puntual que ¿Qué clientes están mal asignados en todo el ciclo de cobranzas, o están clasificados para ciertos equipos que por ahí no respondían a las reglas de ese equipo? Por ejemplo, mi equipo era para cuentas estratégicas, y adentro de la lista de cobranza de cuentas estratégicas, había un equipo que era de cuentas de otro tipo de sector. Entonces teníamos que asignar esos clientes mal asignados, teníamos que saber cuándo vencían esos clientes, cuándo iba a tener yo que cobrar, y qué riesgo tenían según su historial de pago y de edición. Entonces, responder esto no es sencillo, sobre todo de los datos, porque está distribuido entre varias tablas de SAP. BCT es una tabla de SAP que tiene las cuentas por cobrar, NA es el maestro de clientes, BSAP tiene las cabeceras para las fechas de cobre. Entonces vos tenés que cruzar toda esa información para responderte esta pregunta. Y generalmente acá está la. Y el negocio. Y toda esa iteración lleva su tiempo. ¿Y si queremos ver cuatro semanas para adelante, cuánto me va a vencer? Puedo ya tardar tres semanas o cuatro semanas en responderlo. Y esa pregunta ya no tiene sentido, o por lo menos no estamos resolviendo. Principalmente queríamos. Así que te voy a tratar de explicar cómo lo resolvimos directamente con AI usando theramo. Para eso hago una explicación de theramop, que es bien conceptual para que vos te la lleves. Nosotros lo que hacemos es conectarnos a todos los sistemas, múltiples fuentes de datos que ustedes tengan, puede ser sus app, APIs bancarias, los forecast que tengan, alguna planilla aparte, otras planillas con Excel, ROM, equipos y demás. Todo eso lo entendemos, lo sanitizamos, lo documentamos y resolvemos cinco cosas que para mí son muy importantes en lo que es BI. La coordinación de infraestructura, todo lo que antes. Sistemas. La automatización del data engineering, que es lo que hacía el BI también. Sistemas.

**Bruno Ruyu**: Los cálculos, todos los cálculos, o sea, te lo paso, tal vez al lenguaje no tan técnico, que todo corra bien, que se actualice a la mañana y todo eso funcione. Los cálculos básicamente, o lo que se hace en Excel hoy, o lo que justamente sistema te podría hacer en un Data Warehouse. Capa semántica es todas las reglas de negocio, todas las lógicas, pero escrita para que una persona la pueda leer. A este proveedor no hay que pagarle no sé por qué cosa, o no sé, esto se paga en dólares y esto en pesos, quedan escritas, o sea, las escriben en teoría para que cualquiera pueda leer la colección MCP. Nada, esto es una forma que las inteligencias artificiales quedan conectadas, si vos lo usás, eso no importa. Y la creación de tableros y ahora también alertas, vos le decís, che, si buscas, quiero que me busques desvíos, puede ser específica, decirle si en esta variable hay un debido de más del 2% contra el mes pasado, contra el presupuesto, mandame una alerta, o puede ser un poco más general, fíjate si aparecen cosas raras y avisame.

**Lucio Rojas**: Bien, entonces ahí. Gracias Bruno Retom ¿Cuál es nuestra propuesta de valor? Bien concreto es darle a este usuario que estábamos viendo acá, el analista de negocio, la persona de negocio, un empoderamiento muy grande en todo lo que es el trabajo con datos. Ahora, esta persona no va a estar ocupada en ver las tablas, entenderlas, cruzar todo lo que explicamos, y sí va a estar ocupada en hacer más y mejores preguntas de negocio, empezar estrategias, en optimizar ganancias, en hacer predicciones, todo esto respondiéndose preguntas con información y con datos contra un modelo de i, lo que antes llevaba horas. Hasta acá parece un pitch de ventas, pero esto es real, lo vamos a ver al final cuando lo probemos, qué nos dimos cuenta trabajando con el equipo de Tahua, que teníamos 547 millones de dólares a vencer en las próximas semanas, y esos 547. 405 son de clientes que ya estaban pagando tarde, tarde en relación a la fecha de cobro y también en su historial de pagos, porque fuimos, miramos cuándo pagaban, cada vez que pagaban, si pagaban todos los miércoles y ahora estaban pagando viernes. Sabemos que esa mora de dos días no es casualidad, sino que ya te puede indicar un patrón de atraso. También empezamos a evaluar cómo podíamos adelantar esa disposición de caja para poder jugar financieramente con eso. ¿Y puntualmente qué cambiamos? Que antes la reasignación de cuentas que dijimos que había que hacer, se hacía a mano entre cuatro equipos de trabajo y un trabajo manual de semanas tenía que reasignar 14.000 cuentas, mirar una por una, saber si ésta iba a un grupo, al otro.

**Paula Cordeviola**: Eso por las lógicas que Lau tiene para cada grupo, es como si cambiaba alguna lógica, lo analizaban y lo cambiaban a mano. Acá como que ya lo identifica y

**Lucio Rojas**: lo reclama, y no solamente cambiar para adelante, sino también para atrás. Ya había cuentas mal asignadas que había que conciliar. Eso se lo dimos todo a la IAI y la reclasificó automáticamente. Bien, armamos las cuentas corrientes que antes estaban armadas en Excel, que eran millones de filas, que tenías días de cruce por pedido para saber cuál era la posición de una cuenta, tenías que cruzar todas las partidas abiertas, las partidas compensadas, todo eso también tomamos auto en un momento y empezamos a cruzar fuentes de SAP que antes no se cruzaban para empezar a sacar información, las fuentes de partidas abiertas, de partidas compensadas, los maestros, los calendarios, los equipos, los tipos de cambio, todo esto se cruza autónomamente y llevamos los resultados que vamos a ver ahora. ¿Cómo lo hicimos? Lo hicimos en tres sesiones de trabajo de dos horas, donde la sesión 1 fue poder cargar las fuentes, poder hacernos de los datos, perdimos tiempo con eso que es natural, y en explicarle al modelo las reglas de negocios que ya estaban escritas, digamos, con el equipo. Eso en la segunda sesión ya salimos con todas las reasignación hecha, con las cuentas auditadas, con las reglas auditadas y con el calendario de vencimientos a partir del histórico de pago ya sabemos cuándo iba a ser cada uno. Y a la tercera sesión hicimos un scoring de riesgo por cliente para ver esto, cuál era la demora, cuáles eran los desvíos, cuáles eran las consistencias, inconsistencias.

**Paula Cordeviola**: OK.

**Lucio Rojas**: Terminamos reasignando 2.248 cuentas, identificamos cuál era el riesgo de pago de 16.000 clientes y trabajamos.

**Paula Cordeviola**: OK, ¿Y esto Lau ya lo está implementando o fue como una?

**Bruno Ruyu**: Fue una prueba y ahora estamos está en el proceso de conseguir sistemas y demás.

**Paula Cordeviola**: Sí, el FRIS y todo, la maren coche. OK, bien, o sea, esto fue como una prueba de decir che, yo podría

**Bruno Ruyu**: hacer esto, en 6 horas puedo llegar

**Paula Cordeviola**: a tener esto, y esto que es como una aplicación, una herramienta, o sea. OK, perdón,

**Bruno Ruyu**: igual prefiero que nos hagas preguntas, Pau, antes de seguir. Tal vez conceptualmente ya entendiste un poco la lógica.

**Paula Cordeviola**: Sí, sí, tengo mil preguntas para lo que yo necesito, pero si quieren terminemos y veámosla.

**Lucio Rojas**: Termino con esto súper rápido.

**Paula Cordeviola**: Ya hicieron también termino súper rápido con

**Lucio Rojas**: esto, si no llevamos más tiempo. Ya se entendió el valor. ¿Con qué nos quedamos? Con tablas listas para preguntar, que se actualizan a medida que se actualizan las fuentes, con la reasignación de cobranzas, que podemos ver quién tiene cada cuenta, cómo se gestiona. Tenemos ya la tabla de scoring de clientes, que sabemos qué clientes pagan peor que su historial, cuál es la demora promedio histórica de cada uno, cuál es el desvío, cuál es el percentil 90, que es la distribución de la campaña de Gauss. También sabemos quién vence cada semana y a quién llamar. Y todas estas tablas que armamos también las representamos gráficamente con dashboards, es lo que hace la herramienta. Ahora vamos a repasarlo, pero ya nos quedó todo el calendario de vencimientos, a quienes llamar, cuál es el estado de cada cuenta, cómo se reasignaron las cuentas, todo el scoring de riesgo de clientes vivos.

**Paula Cordeviola**: Y ahí te hago una consulta. Si surge una lógica nueva, ¿Cómo es esa customización o esa actualización?

**Lucio Rojas**: Bien, se habla con el modelo de que usamos y se le explica y el modelo lo cambia.

**Paula Cordeviola**: ¿OK, pero eso es como una interacción con ustedes como implementadores y se cambia o lo hacemos nosotros? Lo hacen ustedes directamente. Le digo esto, sumale tal cosa y

**Bruno Ruyu**: OK, o te mandan un mail. Le copias el mail, se lo mandas o te mando un documento. Se lo mandas y lo entiend.

**Paula Cordeviola**: OK.

**Lucio Rojas**: Hoy en día ni se lo mandas, que te lo lea directo. Bueno, esto un poco más de informe de lo que hicimos, lo voy a pasar rápido, pero ya sabemos quién vence cada semana, por semana, cuántos millones de dólares, cuáles son las cuentas más atrasadas. Y ahora sí vamos a ir a jugar un rato, porque es lo divertido, y vamos a hacerle preguntas en vivo al sistema. Podemos preguntar parados al momento de fecha de corte de los datos, podemos preguntar cuánto vencen las próximas cuatro semanas y cuánto está el riesgo, a qué clientes hay que llamar el lunes y quién los tiene asignados, qué cuentas están mal asignadas o duplicadas y podemos hacerlo. En realidad estas son preguntas para arrancar todas las preguntas a vos se te ocurra.

**Paula Cordeviola**: OK,

**Lucio Rojas**: repaso un poco la herramienta. Esta es nuestra herramienta, esta es Tela

**Bruno Ruyu**: Moto, todavía estamos viendo la presentación.

**Lucio Rojas**: Sí, eso no lo tuve en cuenta,

**Bruno Ruyu**: o sea mostrarle rápido la parte de la fuente y eso, pero esto es lo menos interesante.

**Lucio Rojas**: No hago detalle, voy. De hecho esto es para que vos veas. Nosotros tenemos un Sasuke, que es donde nosotros cargamos la fuente, las administramos. Acá puedes conectar directamente el SAP de la empresa.

**Paula Cordeviola**: Bien.

**Lucio Rojas**: Trabajamos con los dashboards, acá se pueden ver los dashboards que nosotros explicamos que habíamos creado una vista más linda. Esto queda directamente conectado a tu sistema y se actualiza.

**Paula Cordeviola**: OK.

**Lucio Rojas**: Esto dashboard los hacemos con AI. Nadie se puso a ver cómo armar los gráficos y cómo armar los cálculos. Lo más importante de todo esto a nivel funcional, a nivel técnico, tenemos muchas cosas para ver, pero estamos más sobre funcional, es que lo puedes conectar con cualquier modelo de AI que hoy en día está funcionando, hasta incluso modelos suyos propios o un agente nuestro interno. Pero también tenemos Copilot, que es por lo que ustedes trabajan y se puede hacer de cuenta como esta demo sobre COP,

**Bruno Ruyu**: creo que la prueba usted la hicieron con algunas empresas, no quieren y le ponemos y ponemos una inteligencia ahí adentro nosotros.

**Paula Cordeviola**: OK. Y a nivel mantenimiento, según entiendo ustedes hacen como toda la implementación y después hay algún tipo de mantenimiento o algún contacto con ustedes o cómo es la Mirá, Buenísimo.

**Bruno Ruyu**: En realidad lo que nosotros llamamos implementación es más que nada enseñárselo a usar, porque la verdad que la implementación es una reunión con IT que nos diga cómo conectarnos a la base de datos y ya funciona. Lo que sí hacemos es acompañar. A ver, nosotros podemos acompañar todo el tiempo que quieran y algunas empresas le dejamos un recurso trabajando casi permanentemente. En general lo terminan dando de baja,

**Paula Cordeviola**: porque sí una vez que ya llegaste al óptimo, llegaste al óptimo y entendiste cómo.

**Bruno Ruyu**: Básicamente pidiendo lo que necesitas, la formulación. Eso es lo que lo hace tan fácil, es como cada uno aprendió a usar chat GPT o cloud en la vida diaria personal. Porque te diste cuenta como che, no, bueno, le tengo que pedir esto así. Entonces lo que sí hacemos obviamente es asegurarnos que todo funciona bien. Nosotros tenemos monitoreando que todas las cosas estén. A veces pasan cosas, bueno, nos escriben, resolvemos, a veces nos piden que le agreguemos cosas nuevas, tratamos de hacerlo y acompañamos en eso. A veces pasa que quieren un nuevo proyecto, bueno, los ayudamos a pensarlo, pero como que en algún momento no nos necesitan tanto. Pero obviamente tenemos parte del contrato es el soporte.

**Paula Cordeviola**: Bien,

**Lucio Rojas**: volviendo Pau, ¿Cómo venís con AI? ¿Qué usas? ¿Está usando Cloud, ChatGPT, Copilot?

**Paula Cordeviola**: ¿Yo personalmente o acá en el equipo?

**Bruno Ruyu**: No, personalmente no.

**Paula Cordeviola**: ChatGPT o Club.

**Lucio Rojas**: Bien. ¿Estás ahí todo lo que es MCP, estás familiarizada? ¿Sabes?

**Paula Cordeviola**: No chicos, yo de tecnología no la tengo muy clara.

**Lucio Rojas**: Voy concreto sobre eso porque es un punto importante.

**Paula Cordeviola**: ¿Qué es MCT?

**Lucio Rojas**: Es un protocolo. Nosotros antes para conectar sistemas no estaba todavía todo lo de ahí, teníamos las APIs. Entonces si yo quería conectar un sistema con el otro, tengo que usar una API. Esto es lo mismo, pero para conectar cualquier sistema con la i. Entonces nosotros tenemos nuestro protocolo MCP, que es.

**Bruno Ruyu**: Hay un ejemplo muy fácil, Gmail. Vos querés que Cloud te lea los mails y te los responda sin tener que abrirlos. Le conectás.

**Paula Cordeviola**: Bueno, mismo acá ponele, tenés. Claro, a Copilot con Outlook, con.

**Bruno Ruyu**: Son esas los conectores MCP son herramientas que le va dando. Entonces está la herramienta de Teramon. Entonces Cloud o Copilot usa Theramo. Eso es un poco la idea.

**Lucio Rojas**: Por ejemplo, acá tengo mis MCPs. Estas son algunos sistemas que yo uso para trabajar. Tengo unos que desarrollé yo, tengo los de Mail y tenemos los de Theramon, que esto es el punto. Entonces nosotros desde Cloud o cualquier aislado, podemos trabajar con Telamo, que Teyamot trabaja con tus datos. Entonces por igualdad, vos podés trabajar desde Cloud con tu SAP de forma segura y también restringida, con todas las cuestiones de ciberseguridad en el medio. Entonces ¿Qué podemos hacer? Vamos a preguntarle a Cloud sobre tus datos.

**Bruno Ruyu**: Claro, ahí para explicarlo, hay un proyecto que es el de YPF Cobranzas, al cual le conectamos la información. En realidad nos pasó unos Excel y lo subimos, pero eran como 70 tablas más o menos. No, no, esto son un poco menos. Bueno, no importa. Era la información que necesitaba. Toda la información que necesitaba se conecta mientras más información le das, más cosas puedes hacer. Y listo. Este es el proyecto YPF Cobranz, Crédito Cobranz. Entonces ahora vas a Cloud y. Y le decís, vamos a trabajar sobre el proyecto YPF Cobranzas. Y listo, ya sabe sobre qué está trabajando y ya entiende.

**Paula Cordeviola**: OK. Como que ya le dijiste cuál era el proyecto. Y ahí ya le empezás a hacer preguntas sobre. Y entiende de qué le estás hablando.

**Bruno Ruyu**: Claro. Y lo importante no solo le haces preguntas, te responde, es que le podés pedir que construyan nuevos cálculos. Eso es lo realmente valioso. Es como si vos agarrás 8 excels y armas uno nuevo que se alimenta de esos ocho. Bueno, todo ese proceso de buscar la columna, hacer el buscar B, hacer una tabla pivot, sumar, agregar, eso. Entonces construye nuevas tablas de datos dentro de esa estructura que técnicamente se llama Data Warehouse, pero bueno, no importa, Construye USA. Construye USA. Y esto dinámica entre Claude y Theramot. Y además escribe conocimiento, es decir, escribe las reglas de negocio para que cualquiera que vaya a trabajar sobre ese proyecto, estén las definiciones claras para todas las personas y todas las inteligencias artificiales. Claro, para que vayan aprendiendo y mejorando.

**Paula Cordeviola**: Perfecto.

**Lucio Rojas**: Esta pregunta que hicimos acá, ¿Cuánto vence en las próximas cuatro semanas? Es la misma que teníamos de tesis, que tardaba mucho tiempo en responderse. La respondió en un minuto. Me dice, bueno, me conecté YPF a Crédito de Cobranzas, usé la tabla calendario de vencimiento, que es con la que nosotros estuvimos trabajando, que alimenta el panel de vencimientos, filtré los vencimientos del 13, del 7 al 9, del 8 de 2026, y tengo la respuesta corta. En esta semana te van a vencer 249.7 millones en 110 partidas. De este total, 130, el 52% está en riesgo. Es decir, corresponde a clientes con nivel crítico alto. Esto lo definimos en otra tabla que hablamos. Y casi todo ese riesgo crítico por semana. Cuántas partidas están abiertas, cuánto vence en dólares, cuánto está en riesgo y el porcentaje de riesgo.

**Paula Cordeviola**: Bien. Si quisieras le decís cuáles son los clientes.

**Bruno Ruyu**: Sí, de hecho ahí abajo te lo empezó a tirar solo.

**Paula Cordeviola**: OK, perfecto.

**Lucio Rojas**: Me dice, bueno, ¿Dónde se concentra el riesgo? ¿En cinco clientes? En Rising Argentina, que tiene 31 millones de dólares en cuatro partidas, y la primera vence del 24 al 7, el equipo asignado es cuentas estratégicas. Y así me fue abriendo con todas las distintas carteras a tener en cuenta. El universo son solo los vencimientos grandes partidas de más de 745 millones, unos. Es todo lo que está por arriba de 500 mil dólares. Por el resto del universo lo sacamos.

**Paula Cordeviola**: OK, la conversión a dólares.

**Lucio Rojas**: Sí, decime.

**Paula Cordeviola**: No, no, clarísimo.

**Lucio Rojas**: Ah, bien. La conversión a dólares usa un tipo de cambio fijo de tanto y en riesgo, significa que el cliente muestra hoy un retraso anómalo, resp. De su propio historial. Esto es una alerta, no es una predicción de IMPAU, es lo que. Y ahora le podemos empezar a preguntar cualquier cosa. Otras preguntas que teníamos armadas acá era, ¿A qué clientes hay que llamar el lunes? ¿Y quién los tiene asignados? Una buena pregunta, ¿Qué cuentas están mal asignadas o duplicadas? Eso ya lo resolvimos en realidad. Y bueno, acá ya tenemos un poco la libertad de.

**Paula Cordeviola**: De empezar a

**Bruno Ruyu**: la. Otra vez nos juntamos con Jorge Sumijana y el equipo de la mesa, y se le ocurrió preguntar cuánta plata se perdió o se ganó en dólares por ajuste de tiempo de cambio en demora de factura, o sea la factura eran 100 mil pesos y cuando tenía que pagar era mil dólares y después cuando la pagó era 800.

**Paula Cordeviola**: Sí, por la deuda.

**Bruno Ruyu**: Exacto, y le tiró eso en función

**Paula Cordeviola**: de este mismo proye, este mismo coso,

**Bruno Ruyu**: que con este mismo datos. OK, o sea lo puedes empezar a usar para.

**Paula Cordeviola**: Bueno, si quieren les planteo mi asociado ya a mucho de lo que hicieron acá, creo. A ver, lo que hago yo, o sea, yo tengo toda la tesorería y el planning financiero más de corto, y a ver, nosotros partimos de info que viene dada, que hasta también se podría mejorar, que como vos Bruno, conoces y estuviste mucho tiempo, conteo de gestión viene del presupuesto y la supa que van haciendo, donde hacen el económico, lo traducen a un financiero medio teórico, y esa es como nuestra base, pero más de largo, que decimos, bueno, esto es lo que dijeron, listo. Pero yo para planificar el corto me baso más en lo que hay en SAP, que en realidad antes no era tan así, o sea, era como que tomaba mucho de esa estimación teórica financiera que hacían, y yo lo que quiero es llevarlo a SAP puro digamos, hay info que me viene del equipo de cuentas a pagar que ya me viene dada, pero que la realidad es que si ellos arman algo que creo que también lo quieren automatizar y no sé si con Cris hablaste algo, O sea como que creo que también quieren buscar lo mismo. Yo lo que quiero es concentrar, o sea yo estoy como el nexo entre Lau y Cris, o sea, ellos tienen Lau, cobranzas, Cris, la parte de cuentas a pagar y yo es como que uno, la información de ellos dos, Cris me trae algo dado pero que para mí con esto se podría armarle las mismas lógicas que él dice y conectarlo directo. Y la parte que más cuesta es la de ingresos, ¿Por qué? Porque vos ahí Lucio, mostrabas como bueno, ¿Cuánto me vence esta semana, ¿Cuánto voy a cobrar? Un poco nosotros hasta donde quizás llegamos fue a OK, todas estas facturas vencen tal día y por ahí le puedo poner unos días de mora en función de su historia, pero lo que más me está costando es como reproyecto si esa fecha no se cumplió, o sea yo digo bueno, de Ryzen voy a cobrar, vence el miércoles, bueno por la mora que tiene yo sé que voy a cobrar el viernes, pero como entiendo si el viernes lo cobre o no y si no lo cobre, ¿Para cuando lo reproyecto? Ese es como el desafío más grande y lo que más nos cuesta. Y a partir de toda esa info nosotros hacemos un comité semanal donde mostramos la actualización del cash flow y explicamos los desvíos básicamente de por qué te dije que iba a tener esta liquidez y finalmente tuve otra y nada, creo que todo esto podría ayudar a una explicación muchísimo más fina de qué cliente se desvió, de qué negocio.

**Bruno Ruyu**: Ahí para mí es buenísimo lo que nos planteaste y lo vamos a hacer ahora porque lo que tiene esto y lo que yo siempre digo es más allá de poder responder preguntas a vos tenés a Claude, la entidad más inteligente de la tierra, para ayudarte en estas cosas, entonces yo lo que le preguntaría ahora decir exactamente el problema, queremos encontrar una forma para que a pesar de haber medido, digamos para cómo hacer para proyectar en el caso que no pagó, ¿Para cuándo ponemos el cobro estimado? Eso sería un poco la pregunta. A ver qué dice Claude y como él tiene los datos probablemente traiga una solución ahora.

**Paula Cordeviola**: OK. Porque muchas de las cosas que nos pasa es que el tiempo entre que vos registraste esa cobranza y se aplica con la factura que vos dijiste, es como que por ahí pasa un tiempo y es como que no sé si la cobre o no, como que hay una temporalidad y qué es difícil como de que obviamente cada vez queremos que sea menos, pero por ahí, por ahí lo cobre, pero no sé todavía que cobre.

**Bruno Ruyu**: Por eso no lo podés ver en SAP, Es una parte del equipo, o

**Paula Cordeviola**: sea, el que cobre algo. Sí, que de hecho está bastante agilizado eso y por ahí el recibo lo tenés el mismo día o por ahí al día siguiente, pero quizás lo que por ahí tarda un poquito más es la compensación de ese recibo, o sea, aplicar el recibo con la factura y capaz que yo sigo proyectando como tengo la factura abierta, que todavía no la cobré y en realidad ya tengo un recibo en la cuenta, que bueno, por ahí él me podría decir, che, igual fíjate que cobraste esto, por ahí es de esto, no sé sí que haga

**Bruno Ruyu**: como una especie de conciliación preliminar que

**Paula Cordeviola**: haga ese sí, o mirarlo a nivel cliente y decir bueno cobraste y si el cliente opera el 90 en un negocio, asumir que cobraste de ese negocio con él, bueno,

**Bruno Ruyu**: ese tipo de cosas, ahora no me acuerdo exactamente en dónde, pero lo que hace en realidad lo que él sugirió hacer y después hizo es armar como unas reglas que te dan un cierto score de aseguramiento de que estás machando bien. Entonces hace cosas como lo que dijiste, mira, si el mismo cliente y si normalmente paga y de esta lógica y tiene este servicio, bueno, tiene como un 90% de probabilidad de que sea esto.

**Lucio Rojas**: Entonces.

**Paula Cordeviola**: Ponémelo acá.

**Bruno Ruyu**: Claro, ponémelo acá. Eso lo puede hacer.

**Paula Cordeviola**: OK, o sea, básicamente mi objetivo es reformular todo el cash flow a partir de datos reales y como un poco más de, o sea, como poder armar algo más sistémico, que hoy por ahí es medio manual, viste, ay, cobre esto y lo pongo acá y lo saco de allá y después los desvíos es como que es medio,

**Lucio Rojas**: No digo que me encantaría mostrarte, pero bueno, otro caso de uso, no importa, pero hemos trabajado con con un cliente que estaba en SAP y lo que hicimos fue proyectar el cash flow a 30, a 60 y a 90 días en base a los datos en su SAP compartida abierta, conectamos el módulo FI y dijimos agárrame los cash flow proyectados.

**Paula Cordeviola**: ¿Y cómo ibas reproyectando?

**Lucio Rojas**: Bueno, eso todavía no lo pensamos, hicimos como la foto en el momento. Pero reproyectar no debe ser tan difícil, porque no.

**Paula Cordeviola**: Acá en IPS hay un equipo un poco de inteligencia artificial y datos y qué sé yo, que obviamente tienen un montón de laburo. Y es un poco lo que nos pasa con sistemas, que por ahí estás meses como para armar algo y por ahí sí llegamos a esa parte, como a la foto estática de OK, bueno, esta factura que vence tal día, más cierta mora, este es tu cash flow. Pero lo que a mí me está faltando y lo que creo que es el valor que necesito, es que se me vaya retroalimentando con la realidad y que esa retroalimentación de eso surjan los desvíos y que me explique que varió, digamos.

**Bruno Ruyu**: Para mí es totalmente factible. Y de hecho acabamos de hacer un proyecto con una obra social, una prepaga, que el problema de ellos es que tienen todo un volumen de gastos que son más o menos predecibles, pero después aparecen picos donde una persona tiene un accidente o alguien agarra una enfermedad oncológica y salen 2 millones de dólares. Entonces, y además lo que pasa es que ellos hay facturas que se enteran, o sea, le cae un costo y se enteran 100 a 90 días cuando les llega la factura de sanatorio, alguien tiene un accidente, lo meten, lo internan, lo operan, la obra social no se entera hasta que 90 días le llega la factura de internación. Entonces como que están 90 días medio ciego del número final. Básicamente nos pidieron, tenemos que hacer esto, primero conocer el dato real a hoy y después proyectame a 60, 90, 120 y 180 días. Y lo conectamos y empezamos a trabajar, fueron 4 o 5 reuniones y que queda funcionando. Así que son cosas que vos lo dijiste, el equipo de datos. Esto es un equipo de datos autónomo.

**Paula Cordeviola**: Tal cual. Sí, sí, sí. OK.

**Lucio Rojas**: En realidad estuvimos bastante tiempo para que sea.

**Bruno Ruyu**: Cuatro años, pero lo conseguimos.

**Lucio Rojas**: No, no, digo, el desarrollo de producto, lo que hicimos EPF, sí, lo hicimos rápido. Bueno, voy con la pregunta que hicimos y a ver qué respondía. Nuestro caso de uso es armar un cash flow a corto plazo. Tengo proyectados los cobros en base a SAT, pero en ciertas partidas cuando entran en mora me cuesta reproyectar ese ingreso de flujo, porque no sé para cuándo se reasigna. ¿Cómo lo resolverías? Primer enunciado. La segunda también. A veces cobro facturas y por desfasaje operativo veo la factura pero no la cuenta que la pagó, lo registran después. ¿Necesito marchar anticipadamente? ¿A quién corresponde esa factura? ¿Tenés dudas? Quiero soluciones posibles. Perdón, es lo que yo interpreté de lo que hablamos.

**Paula Cordeviola**: Sí, por ahí lo de la factura en realidad es, o sea, yo tengo una factura y tengo el cobro, sé que Ryzen me pagó, por ejemplo, pero por ahí no, ponele, por ahí opera, lo que nos pasa es que opera en varias unidades de negocio, entonces no tengo. Claro, nosotros el cash flow lo armamos por unidad de negocio, entonces no sé si sí me pagó combustible, me pagó algo de química, ¿Entendés? Eso es más que nada el match.

**Lucio Rojas**: Bueno, supongo que acá Claude lo identificó eso. Vamos a leer los minutitos de leer lo que dijo, porque siempre está bueno. Dice sí, tengo dudas, pero primero te paso cómo lo resolvería. Antes miré el histórico de partidas compensadas, unas 452.000 facturas de deuda real. Hay un hallazgo que conecta estos dos problemas. Lo que muestran los datos el 67 de la factura se compensa después del vencimiento, el monto es el 51 %, pero la mayoría de esos atrasos son cortos. La mediana es de 3 días y el 80% se resuelve en 11 días o menos. La cola larga existe y es predecible. Sólo una de cada cuatro facturas atrasadas pasa los siete días. Las que pasan los siete días tardan en total unos 20 días de mediana y un tercio de ellas supera los 30. El dato clave es que la mora que ves en SAP se mide contra la fecha de compensación, y esa fecha incluye el atraso en registrar el pago. Parte de tu mora es plata que ya entró al banco y nadie imputó todavía. Si resolvés el segundo problema, el primero se achica solo. Problema 1 Reproyectar, partidas vencidas. Hay tres opciones, de menor a mayor certificación y se pueden combinar a regla por cliente. Rápida se arma con lo que ya hay. La fecha proyectada es el vencimiento más la mora histórica del cliente. Día habitual a su día habitual de pago. Ambos datos ya están en la tabla de scoring. Si la partida ya superó esa fecha, se usa la mora del segmento. Es simple y explicable, pero da una sola fecha cuando en realidad hay incertidumbre. Igual está buena. B Curva de cobro condicionales. La que recomiendo para tu cash flow, en vez de preguntar cuándo entra la pregunta, Dado que esta partida ya lleva n días de vencida, ¿Qué probabilidad tiene de cobrarse en cada semana siguiente? Esa probabilidad se calcula con el histórico por segmento o nivel de riesgo y por cliente cuando hay historial suficiente. Por ejemplo, una partida de 100 millones con 10 días de atrasos se proyectaría así 55 millones en la primera semana, 25 en la segunda, 10 en las semanas 3 y 4, y 10 millones en más de 30 días o en riesgo. Así el cash flow se reproyecta solo cada día que pasa, sin que nadie tenga que decidir una fecha. También te da escenarios, el base con la mediana y el conservador con el percentil 80. Eso está bueno porque vas a ver si es en base a lo que puede llegar a pasar o algo. C Override del cobrador. Si el cobrador consigue una promesa de pago, la carga en un campo y esa fecha pisa el modelo, después de medir el cumplimiento de promesas por cliente y usarlo para ajustar cuánto peso darles. Después puedes medir cumpliendo el cliente y usarlo para ajustar cuánto peso da un circuito de carga, que puede ser una planilla o una tabla en telm. Así resolvería Claude el problema 1. Le podemos debatir algunas soluciones. Problema 2 Imputar cobros antes de que se registren. Para eso necesito una fuente que hoy no está en el proyecto.

**Bruno Ruyu**: Esto creo que era lo que no le planteamos bien acá Sí está todo, solo que el problema es a qué unidad de negocio hay que asignarlo. YPF tiene un montón de unidades o varias unidades, entonces ve la factura, ve el cobro, ve qué cliente, pero no sabe si es para un negocio 1, negocio 2, negocio 3.

**Paula Cordeviola**: Ahí habría que es como identifique si cobré o no, y si cobré como que no me siga reproyectando esa factura vencida porque en realidad ya lo cobré, y de alguna forma asumir que es del negocio tal como si todavía no está compensada, Perdón.

**Lucio Rojas**: ¿Y eso lo podría identificar con algún otro dato dentro de SAP, o sea, se hace el cruce de ver justo

**Paula Cordeviola**: ese valor de que sí, o sea, capaz que te pagaron el valor exacto de la factura y podrías decir che, te pagaron esto? Pero por ahí no, o hay veces que no sé, con un mismo pago, por ahí nos lo mandan por un mail y te dice te estoy pagando la factura tal, tal y tal, pero hasta que eso después el cobrador lo replica en SAP, por ahí no es instantáneo, digamos, por ahí es a esa demora que decía, por ahí tarda dos, tres días hasta que lo compensa.

**Lucio Rojas**: Ahí creo que lo entendí mejor. No

**Paula Cordeviola**: quiero identificar si ya cobro nada, si ya la cobre, dejar de proyectarla e imputarla a una unidad de negocio. Lo que necesito es que me diga si medidas la factura del cliente el día de cobro y asignar la unidad de negocio. Sí, creo que sí.

**Lucio Rojas**: Vamos a hacer una watch. Bueno, vamos a dejarlo pensar acá. ¿Para que está? Bueno, para ver el mecanismo de razonamiento. Lo que hace primero acá Bruno, ayúdame.

**Bruno Ruyu**: Esta palabra en inglés la tenés desenmarañando, Tenés un montón de. Se te juntan todos los. Una maraña hilos y lo tenés que

**Lucio Rojas**: no había escuchado nunca. Bueno, voy a desenmarañar cómo están los documentos que están desmacheados por estado y lo que hace es ir y mirar en las tablas del SAP cómo está la información. ¿Usa Telamot para eso?

**Bruno Ruyu**: Por ahora no lo veo. Teheramot es todo cloud, pero en esa parte cuando empiezan a trabajar juntos. Claro, fíjate esto incluso hasta le puede pasar objetivos de lo que tiene que hacer y Teramont lo hace.

**Lucio Rojas**: Claude razona, es más inteligente del mundo de la historia, nos sorprende todo el tiempo. Y Theramo es como si fuese su herramienta para trabajar con tus datos. Entonces es como que piensa y lo va usando cuando lo necesita, cuando está a disposición.

**Bruno Ruyu**: Claude está cerca del negocio y Telamo sería el equipo de datos y IT.

**Paula Cordeviola**: Claro, sería como el intermediario, el que tiene el dato, digamos.

**Bruno Ruyu**: El que tiene el dato y el

**Paula Cordeviola**: que lo entiende puede entenderlo. Claro. Para ustedes Claude es lo mejor de toda la CIA que hay.

**Bruno Ruyu**: Es cierto, los modelos nuevos de ChatGPT, los que salieron hace 10 días, son buenos también. De hecho nosotros hacemos un montón de pruebas internas en estos procesos, hay un montón de inteligencias artificiales atrás haciendo cosas y están las que entienden la información al principio, están las que responden y vamos midiendo cuál es que sale un modelo nuevo, a ver si es mejor que lo que tenemos o no, si es más barato, si es más caro. Y las últimas pruebas a ChatGPT le dio muy bien a los modelos de GPT. Es más, y quedaron en algunas partes, están los de OpenAI. Pero para el. ¿Para esta última parte, que sería el que usas vos como persona? A mí Claude me parece que está igual. Obviamente yo me pago todos y uso todos y voy probando.

**Paula Cordeviola**: Vas probando. Depende del tema para mí, o depende de lo que tengas que hacer. Es como alguno te dice. Para presentaciones está buena, esta para otra.

**Lucio Rojas**: Para presentaciones tenemos uno que está muy bueno.

**Bruno Ruyu**: Nosotros no hicimos una herramienta interna.

**Paula Cordeviola**: Ah, la hicieron ustedes.

**Lucio Rojas**: Esta es la presentación que viste. Esto es una guía que hace presentaciones, como flotan las cosas, está todo animado. Yo También me pago ChatGPT Cloud y algunas presentaciones.

**Bruno Ruyu**: Estamos los dos en la oficina. Estamos en la oficina, estamos a dos metros, pero nos quedamos cada uno de su compra.

**Lucio Rojas**: Bueno, ya que tengo.

**Bruno Ruyu**: No, a ver lo que hice. Conviven dos cosas. En las partidas abiertas conviven dos cosas. Factura positiva, los recibo el cliente sin aplicar las RC y RM. Negativos,

**Paula Cordeviola**: El cliente ya pagó el cobro, está registrado en su cuenta, pero nadie lo cruzó dentro de la factura. Mientras tanto la factura sigue abierta y vos la seguís. Proyect. Exactamente lo que me pasa. Números del corte, 27 recibos sin aplicar, 2000. Tienen facturas extras y recibos sin aplicar al mismo tiempo. En 783 de ellos, lo cobrado cubre toda su deuda abierta. Claro que eso también te pasa. Tenés tipo. Si vos miras la deuda a nivel consolidado del cliente, por ahí te da que tenés deuda a vencer, pero al no estar aplicada, como que no. Claro. Un dato importante, el match. Un recibo, una factura por importe exacto. Sólo cierran 249. Claro. Que ponele. Yo en realidad, o sea, mi proceso, yo los reales que serían los recibos, los voy recibiendo y computando bien, digamos. El tema es cómo reproyectar a partir de ese recibo que tengo. ¿Por qué? Por esto que lo tengo separado, como que no sé qué reproyectar. Si ya cobre todo y no tengo que reproyectar nada, básicamente. ¿Y a ver qué hice? Cómo lo. Bueno, una tabla de resultados en. Tenemos una fila por factura abierta con las columnas que pediste. Factura, cliente, estado de cobro, fecha de cobro, unidades. Se calcula por cliente en cascada. Importe exacto, mismo cliente y misma división. Confianza, alta combinación de facturas que suma el recibo. Ah, eso que decía por ahí te pagan con un solo pago varias facturas. Neto de retenciones, recibo más certificado de retención del mismo día suman la factura. Claro. Imputación, FIFO del saldo, lo que queda sin match se aplica a las facturas más viejas del cliente, que es lo que sabe hacer, Compensar. Confianza media. Para el cash flow es suficiente, la plata ya entró. Tal cual. Sí, es que en realidad a veces tenemos como esa doble visión de che, en realidad si lo miro por cliente también está bien, pero hay veces que como que por ahí es como cambiar la mirada, decir no, lo miro más por negocio, pero bueno, a veces está bueno de che, si está desviado en algún negocio o no, pero también se podría mirar a nivel cliente y como que ya miras deuda y listo. Con eso cada factura queda en uno de tres estados, Cobrada, cobrada, parcial y pendiente del café. Usan las cobradas y se restan las parciales. La fecha de cobro es la fecha contabilización del recibo y la unidad de negocio sale de la adición de la factura, así que sirve para validar cruce y para imputar la unidad aunque el match a la factura sea 2. Cuando SAP compensa de verdad, la partida desaparece de las abiertas y la tabla se limpia sola. Si ya la habías dado por cobrada, no te mueve el flujo. Ah, OK,

**Lucio Rojas**: dos cosas que me faltan confirmar. La unidad de negocio es la división de SAP, el campo. ¿Las notas de crédito cuentan como cobro?

**Paula Cordeviola**: No, las notas de crédito no. Para cash flow no son plata. Pero si cancelan deuda y habría que dejar de proyectarlas. Sí, en realidad las tenés que proyectar como neto de la factura porque vos vas a cobrar menos, digamos, No es plata. Pero debería igual proyectarlas para que me proyecte el neto de lo que tengo que cobrar, digamos.

**Lucio Rojas**: Bien, entonces ahora decimos eso entiende toda la lógica de negocio y le podríamos pedir que. Que termine de resolverlo y ya tendrías el problema resuelto. Con Telamo genera la tabla, eso se actualiza todos los días solo, sin que

**Paula Cordeviola**: vos vuelvas a hacer en función que vos le definas lo que querés, ahí te arma como la tabla que sería como tu input y te la va

**Bruno Ruyu**: actualizando y después le decís haceme un dashboard y va a usar esa tabla para consiste en dashboard y lo ves todos los días

**Paula Cordeviola**: y decirle que me explique desvíos diarios o semanales o lo que.

**Lucio Rojas**: Acá la quiere hacer. Pero bueno, frenamos porque ya nos queda cuatro minutos ahí. Pau, honestamente creo que lo podemos llegar a resolver el problema que tenés si vos haces el trabajo de conseguirnos las tablas o poder llegar a tener los mismos Excel que trabajamos con el equipo de Lau y te acompañamos y si nos ayuda a traccionar un poco eso, lo dejamos resuelto.

**Paula Cordeviola**: OK, sí. A ver la info. No sé qué tablas le pasó Lau, porque entiendo que el fondo es el mismo.

**Bruno Ruyu**: Es el mismo, o sea,

**Lucio Rojas**: hace bastante tiempo por atrás.

**Paula Cordeviola**: OK. ¿Ella que le pasó? Una foto estática.

**Lucio Rojas**: Bajo los costos. Bajo los.

**Paula Cordeviola**: Partidas abiertas.

**Lucio Rojas**: Partida abierta de SAP, partidas conversadas de SAP, partidas contabilizadas.

**Paula Cordeviola**: OK, Sí, sí, sí.

**Lucio Rojas**: ¿En Excel o en CSV? Algunas estaban en texto y tuve que compartirlas durante bastante tiempo a CSV. No sé por qué trabajamos en formato de texto, todas esas cosas, pero por ahí si tenemos los datos crudos.

**Paula Cordeviola**: Dale, OK. Sí, sí. Como para ver cuál sería el resultado y ver si sirve o no y.

**Lucio Rojas**: OK, bueno, sería una prueba de concepto cortita, como armamos con ellos en un día capaz casi virtual o presencial, lo deberíamos de resolver y te queda el

**Paula Cordeviola**: trabajo ya OK hecho.

**Lucio Rojas**: Para ver posible resultado.

**Paula Cordeviola**: Dale, dale, dale. Bueno, bueno, trato de bajar esa info y les comparto y vemos si coordinamos otra o nos juntamos. Dale, Buenísimo. Dale, genial. Bueno, mil gracias chicos por el tiempo. Adios. Ciao.
