# Intro-Teramot entre Agustin Garcia y Maximiliano

**Fecha:** 2026-09-02T15:26  
**Duracion:** ~34 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** Agustin Garcia, Maximiliano Palmero, Franco Ferrero  
**Externos:** Maximiliano Palmero  
**Archivo origen:** Intro-Teramot entre Agustin Garcia y Maximiliano - 2026-09-02 15_26 GMT-03_00/Intro-Teramot entre Agustin Garcia y Maximiliano_ 2026_09_02 15_26 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Presentación de Teramot para unificación de datos y eficiencia operativa mediante inteligencia artificialFragmentación y unificación de datosTeramot consolida fuentes dispersas para análisis cruzados. Eficiencia operativa demostrada en casos reales.Metodología y capacidades técnicasSistema interpreta modelos sin requerir conocimientos técnicos. Generación de reportes automáticos y alertas proactivas.Evaluación competitiva y conclusiónDiscusión sobre ventajas frente a otras soluciones. Compromiso de mantener contacto tras escepticismo inicial.

### Próximos pasos

[Agustin Garcia] Compartir enlace: Remitir la grabación del seminario web sobre eficiencia en las áreas de control de gestión y finanzas.

### Detalles

Introducciones y propósito de la reunión: Agustín Garcia y Maximiliano Palmero se reunieron para discutir las funcionalidades de la plataforma Teramot, tras el interés de Maximiliano Palmero por un correo electrónico recibido sobre la herramienta (00:00:00). Agustín Garcia explicó que Teramot es una plataforma diseñada para consolidar diversas fuentes de datos empresariales en un "datalake" y gestionarlas mediante inteligencia artificial (00:02:28).
El problema de la fragmentación de datos: Agustín Garcia señaló que es común en empresas de todos los tamaños que la información esté dispersa en sistemas como el ERP, CRM y logística, impidiendo una explotación unificada de los datos. El objetivo de Teramot es funcionar como un "paso cero", curando y unificando estos datos para permitir análisis cruzados entre diferentes sistemas (00:03:54).
Integración con LLM y eficiencia operativa: La plataforma permite conectar el datalake con modelos de lenguaje (LLM) mediante un protocolo de contexto de modelo (MCP) (00:03:54). Agustín Garcia presentó un caso de uso de una empresa industrial con 950 empleados, donde la auditoría de cuentas a pagar se redujo de 205 horas a cinco horas, destacando la capacidad de la herramienta para liberar tiempo hacia tareas estratégicas (00:05:14).
Metodología de trabajo y propuesta de valor: Maximiliano Palmero cuestionó si el valor de la herramienta se limita a la lectura de tablas dinámicas, a lo que Agustín Garcia aclaró que los usuarios no necesitan conocimientos técnicos ni saber nombres de campos o tablas, ya que el sistema interpreta automáticamente el modelo de datos (00:08:06). Se propuso realizar una prueba de concepto (POC) enfocada en los puntos de dolor específicos del cliente para demostrar el valor real, en lugar de realizar una demostración teórica (00:10:17).
Capacidades de reporte y automatización: Teramot permite generar dashboards y reportes automáticos en cinco minutos, reemplazando la necesidad de que analistas de datos pasen días curando información y creando visualizaciones (00:11:36). Agustín Garcia enfatizó que la plataforma optimiza el consumo de tokens en comparación con otras integraciones de LLM, un factor clave para directores comerciales y de finanzas (00:12:52).
Casos de uso y alertas proactivas: La plataforma permite la creación de motores de alerta para anticipar quiebres de stock o analizar motivos de devoluciones, tareas que de otro modo requerirían proyectos complejos y costosos. Agustín Garcia reiteró que la herramienta permite aplicar modelos matemáticos y de machine learning sobre los datos de forma ágil (00:14:33).
Capacitación y soporte técnico: Maximiliano Palmero preguntó sobre la necesidad de capacitación técnica. Agustín Garcia aclaró que, si bien el equipo brinda asistencia sobre la estructura de datos y la creación de reportes, no dictan clases formales de "prompting", ya que el conocimiento del negocio por parte del cliente es lo que aporta mayor valor a la interacción con la inteligencia artificial (00:17:18).
Arquitectura, ingesta y roles de usuario: Sobre la arquitectura técnica, Agustín Garcia explicó que el sistema ingesta los datos de forma recurrente según la necesidad del cliente sin tocar la fuente de origen (00:20:05). El producto cuenta con versiones "in-house" para industrias con requerimientos de cumplimiento estrictos y define roles de usuario, incluyendo "member" para administradores y "viewer" para quienes consumen reportes (00:23:06).
Demostración de la plataforma: Durante la demostración en tiempo real, Agustín Garcia mostró cómo un usuario puede generar un reporte, como un plan de promociones para una temporada futura, interactuando simplemente con los datos a través de la interfaz (00:24:30) (00:32:08). Se destacó que el sistema permite la trazabilidad de las consultas realizadas a la base de datos para fines de auditoría (00:21:43).
Conclusión y diferenciación competitiva: Maximiliano Palmero cuestionó la necesidad de la herramienta dado que ya utilizan Claude y consultas directas a sus sistemas (00:27:38). Agustín Garcia argumentó que Teramot ofrece ventajas competitivas como el datalake consolidado, la eficiencia en el consumo de tokens y la publicación automática de reportes, elementos no presentes en otras soluciones estándar (00:29:12). La reunión concluyó con el compromiso de mantenerse en contacto, aunque Maximiliano Palmero expresó escepticismo sobre la necesidad inmediata de la herramienta para su operación actual (00:30:39).

---

## Transcripcion

**Agustin Garcia**: Buenas, buenas.

**Maximiliano Palmero**: Hol. Hola, Agustín. Buenas tardes.

**Agustin Garcia**: Hola, ¿cómo andan?

**Maximiliano Palmero**: Todo bien,

**Agustin Garcia**: ¿Todo bien?

**Maximiliano Palmero**: todo en orden. Ahí te escribí al chat que se suman dos más y les el link así nos vemos las ahí

**Agustin Garcia**: Perfecto, ningún

**Maximiliano Palmero**: sumamos.

**Agustin Garcia**: problema.

**Maximiliano Palmero**: Vale, ahí está, ahí estamos los tres que se conectan.

**Agustin Garcia**: Buenísimo.

**Maximiliano Palmero**: Estamos acá en la sala.

**Agustin Garcia**: A ver, ¿hay alguno esperando? No, están todos conectados, ¿no?

**Maximiliano Palmero**: Estamos los tres en la sala y hoy se conectan al al Me, pero ya te están escuchando.

**Agustin Garcia**: Ah, buenísimo. Bueno, ¿cómo andan?

**Maximiliano Palmero**: Todo muy bien. Todo bien.

**Agustin Garcia**: Me alegro mucho. Bueno, ¿cómo nos conocieron?

**Maximiliano Palmero**: Eh, me mandaron a Yo soy Nicolás, ahí me estoy conectando. Me llegó un mail, la verdad que no tenía ni idea quiénes son ni qué hacen. me llegó un mail, entré a la página, sentí curiosidad y organizamos la llamada.

**Agustin Garcia**: Buenísimo,

**Maximiliano Palmero**: Me tienes que aceptar.

**Agustin Garcia**: buenísimo.

**Maximiliano Palmero**: Eh,

**Agustin Garcia**: Ahí, ahí acepté. Perfecto. Voy a hacer

**Maximiliano Palmero**: estoy entrando.

**Agustin Garcia**: buenísima.

**Maximiliano Palmero**: Estamos.

**Agustin Garcia**: Fantástico. Bueno, bueno, buenísimo. Si quieren eh les cuento un poco.

**Maximiliano Palmero**: Dale.

**Agustin Garcia**: No sé si pudieron participar de hace poco hicimos un webinar

**Maximiliano Palmero**: No, nada, no,

**Agustin Garcia**: Buenísimo.

**Maximiliano Palmero**: no

**Agustin Garcia**: ¿Ustedes de de qué área son?

**Maximiliano Palmero**: finanzas, finanzas,

**Agustin Garcia**: Perfecto.

**Maximiliano Palmero**: contabilidad. de esas son las áreas que tenemos a

**Agustin Garcia**: Buenísimo, fantástico.

**Maximiliano Palmero**: cargar.

**Agustin Garcia**: Si quieren después les mando el link a la grabación de del webinar porque justo era un poco eh cómo lograr eficiencia en las áreas de control de gestión y finanzas. E les cuento un poco, les hago una breve introducción de qué es Teramot. Teramot básicamente es una plataforma que te permite generar un datalake que traduciéndolo al al español, al coloquial, básicamente es donde vos podés consolidar tus distintas fuentes de datos de la empresa y esas fuentes de datos las podés explotar eh y gestionar por medio de inteligencia artificial.

**Agustin Garcia**: Hago referencia a es algo muy común esto que pasa, inclusive pasan empresas de todos los tamaños que los datos no están consolidados en un solo lugar, ¿no? Vos tenés el sistema del IRP, tenés el sistema de logística, tenés el CRM, tenés, digamos, distintos sistemas que no es común encontrar que la información de cada uno de los sistemas se encuentra en algún lugar donde vos puedas explotar esa información consolidada, ¿no? Entonces, Teramot es, digamos, como primer paso te permite unificar esas fuentes de datos en un solo lugar para, digamos, poder explotar la data y hacer análisis utilizando no solo la información que viene del ERP, sino también complementarla con la del CRM, complementarla con las de los distintos sistemas que que puedan tener donde aporte valor, ¿no? Entonces, ese es el paso cero. paso cero después digamos porque para poder aplicar inteligencia artificial digamos que el paso cero es tener la información curada y unificada en un lugar donde vos puedas

**Maximiliano Palmero**: Ok.

**Agustin Garcia**: realmente eh trabajarla, ¿no? Entonces ahí cumplimos con el paso cero. El segundo paso es Teramo tiene la capacidad de conectar tus datos con un MCP. No sé si hoy ustedes usan Clot Cachipit, Gemini, algo

**Maximiliano Palmero**: Sí,

**Agustin Garcia**: internamente.

**Maximiliano Palmero**: usamos Cloud y Gemini. Gemin como consulta y CL más que nada por para generación de de código yas cosas internas.

**Agustin Garcia**: Buenísimo. Bueno, imagínate que esa es la ventaja competitiva número dos que tiene Teramot, que básicamente lo que te permite es integrar ese datalake, conectarlo con un MCP y con eso vos lo podés gestionar o explotar, ¿no? Voy a ir un caso para orientarlos un poco más. Voy a un caso puntual porque tenemos un montón de casos de uso con distintos clientes que empiezan a aprovechar, digamos, esto para digamos generar eficiencia y productividad básicamente, ¿no? Pero no sé, por ejemplo, una empresa industrial de 950 empleados eh trimestralmente auditoría de cuentas a pagar, ¿sí? 205 horas ya previstas por trimestre para hacer el el reporte y y el análisis de cuentas a pagar. Fantástico. Conectamos los datos. Eh, pudimos generar el mismo reporte en una hora. La primera fue una hora porque tuvimos que hacer varias iteraciones, eh, y después se tomaron 4 horas más, eh, para poder validar que la información era correcta. Sí. Entonces digo, para que ustedes se den una idea de qué se puede hacer, ¿no?

**Agustin Garcia**: Ahora, e esto ya no es que es un generador de eficiencia, sino que básicamente plantea la posibilidad de tener otra forma de trabajar, ¿no? Y aprovechar, digamos, ese superpoder que te da para, bueno, digamos, obviamente utilizar el tiempo en cuestiones más estratégicas y decisivas. Entonces doy ese caso, pero después distintos casos donde digamos por ejemplo un análisis de cashflow o proyección de cashflow en función de o por ejemplo también tenemos escenario de clientes que lo usan para ver la composición del costo en el margen eh y y cómo se compone por toda la información de producción, eh mezclando datos del IRP, de compras,

**Maximiliano Palmero**: H

**Agustin Garcia**: de eh y así sucesivamente, ¿no? O sea, y puedo contarles eh digamos casos eh por un rato largo.

**Maximiliano Palmero**: ¿Sabes? Te cuento un poco a mí lo que me pasa con todo lo que son estas herramientas de inteligencia artificial y demás y y mucho desconocimiento que tengo, ¿no? Pero, por ejemplo, vos recién ahí contas un caso que es eh bueno, ¿cómo vemos el costo industrial de de fabricación de aguas? Y a mí lo que no me termina de quedar en claro es hasta dónde puede llegar. O sea, porque eso llega hasta decirme, bueno, tenés un 10% de mano de obra, 40% de mano de obra directa, que son sueldos, cargas sociales y contribuciones.

**Maximiliano Palmero**: Y tenéis un campo de indirecta que son, no sé, la luz, la vigilancia, la limpieza, qué sé yo. Y pero, ¿qué más hace de eso? Porque ahí es donde digo, bueno, para y es desconocimiento puro, eh, porque en definitiva es me va a leer una tabla dinámica con los datos que yo tengo o dónde realmente me agrega valor

**Agustin Garcia**: Mira, e primero y principal de que vos no hace falta que le subas una tabla dinámica porque vos conectas tus fuentes de datos, por ejemplo, no sé, Una capacidad que tiene Teramot es que vos le conectas cualquiera la fuente de dato que que tiene ya eh digamos predefinida y te permite interpreta automáticamente el modelo. Entonces vos no tenés que estar vos no tenés que tener conocimientos técnicos siquiera, digamos, porque no no sé,

**Maximiliano Palmero**: Ah.

**Agustin Garcia**: por ejemplo, tenemos clientes que tienen SAP y te dicen,"No, bueno, no puede ser que me conecte conecte SAP y que automáticamente entienda el modelo." Sí.

**Maximiliano Palmero**: Ok.

**Agustin Garcia**: Yeah. lo hace. Entonces, vos como analista o como gerente, digamos, que quieras explotar la información, puedes hablar con tus datos hablando del nombre de la entidad. No tenés que saber el nombre de la tabla ni del campo, ¿se entiende?

**Agustin Garcia**: Vos le decís,"Levant el modelo de datos de esto que necesito hacer tal cosa." Y lo hace. Entonces, eso para hacerte como digamos una breve introducción al a qué puedes hacer, ¿no? Ahora, ¿qué puedes hacer? Puedes hacer lo que quieras, porque, ¿cuál es la limitación que tenés hoy en día? La limitación que tenés hoy en día es que, y aparte salió un paper de Antrópic hace poco que explicaba por qué ellos no tienen la capacidad de hacer una conexión a datos, que es lo que hace Teramot, que básicamente te permite disponibilizar tus datos contra eh el LLM, contra Clodo, contra Chachipt. Sí. Ahora, ¿qué cómo lo cómo lo usa hoy la gente? Porque no es que esto es algo nuevo. Hoy suben el Excel, ¿entendés? Entonces, pero los datos, o sea, suben el Excel, entonces es como es one time. Ahora, imagínate que vos tenés toda la fuente de datos que necesitás para el trabajo que hoy en día haces, ¿entendés? Tenés el todo lo que te mencioné recién, Sapier, PI, no sé lo que tango,

**Maximiliano Palmero**: Tá.

**Agustin Garcia**: eh, sale for, lo que ustedes tengan, ¿entendés?

**Agustin Garcia**: Ahora, nada, yo tengo clientes que entran y lo usan para explotación comercial, para saber dónde les conviene ir a hacer campaña o a qué clientes les conviene eh, digamos ofrecerle, qué mezclan eso con el sistema de de consulta del CRM para entender cuáles fueron las los las interacciones que tuvo el cliente recientemente, si hubo quejas. Entonces, ¿qué te quiero decir con esto? Y también te lo cuento para que tengas una idea, ¿cuál es el approach? Porque digamos nosotros no somos especialistas eh en control de gestión ni tampoco en en cuestiones específicas. Ahora, lo que nosotros hacemos es y lo que le proponemos a los clientes y nuestra forma de mostrarles el valor es,

**Maximiliano Palmero**: H

**Agustin Garcia**: mira, hagamos una prueba de concepto. Decme vos hoy cuáles son tus dos casos de uso que más tiempo te llevan, que digamos que más piedra te hacen picar. Sí. No sé, algo específico que che, mira, esto para nosotros es un dolor. Hacemos una ingesta de datos porque hacemos generalmente lo que primero buscamos es hacer una demo, después pasamos una configuración un poco más profundas y ese análisis que vos tenés que hacer lo hacemos con inteligencia artificial. Ahora, ¿dónde está la ventaja del producto? es la disponibilización de los datos con para contra el LLM, la eficiencia que tiene el conector.

**Agustin Garcia**: Sí, porque el conector tiene una eficiencia específica y aparte tiene toda una trazabilidad porque aparte de generar la metadata, vos podés ver si necesitaras por algún tipo de auditoría, necesitass ver qué hizo en cada paso eh en en la comunicación con la base de datos se puede ver perfecto. Entonces, vos ahí podés ejecutar el análisis que quieras. ese análisis te puede sacar un conjunto de datos que puede llegar a ser el resultado, ¿sí? Eh, que te permita tener la info ahí limpia y lista para que vos también la puedas analizar. Hoy en día te arma artifacts, esto te hace generar reportes en en 5 minutos. Nosotros también tiene un módulo de reportería que es como si hoy tuvieses Power BI, table, cualquiera de esos productos. Nada más que vos el dashboard lo hacés con eh digamos eh lo hacés con cloud, te arma el artefact y vos en el mismo cloud le decís,"Publicaste dashboard para el workspace tal que quiero que esos usuarios lo puedan ver." Y en 5 minutos tenés un dashboard y y no hace falta que un analista de datos esté curando la información por dos días y armando por otros dos días el dashboard para volver al negocio y que el negocio le diga,"Che, ¿sabes qué? Me falta esto y esto,

**Agustin Garcia**: vuelve otros dos días, eso ya no no corre más. Hoy tenemos clientes que compran el producto y reemplazan los sistemas de reportaje que tienen. Entonces, dicho esto, el alcance digamos eh es bastante amplio, potente el consumo de tokens en supermerado por la eficiencia del conector, porque aparte también hemos tenido muchos clientes que nos han dicho de entrada, está buenísimo, esto, pero vos me decís que esto sale tanto, fantástico, pero después esto me come vivo en toque, ¿no? Hagamos una prueba, hagamos una prueba, pruébenlo ustedes. O sea, total, hoy los planes que no son enterprise en en cloud, por ejemplo, el plan base es de el que le sigue diciendo,"Prueben con uno de $ úsenlo dos meses, se fijan ustedes." Y nunca empezó, obviamente que tenés un usuario que lo mata porque está sacando reporte. Yo tengo directores comerciales que están todo el tiempo ta dándole para sacar insight a ver cómo pueden crosselear, a quién pueden ir a buscar, quién pueden prospectar, porque aparte también ya de por sí club te permite conectarte a otras fuentes externas. Entonces, la mezcla de información es superpotente. Por eso yo los cuento en términos de que nada, esto también permite, digamos, como una forma distinta de trabajar, digamos, con donde hoy uno pasa más a a tener digamos eh esto te permite un superpoder que digamos que tu foco pasa a ser muchísimo más estratégico y ejecutor porque digamos la parte de trabajo manual y tenés un porcentaje grande que puedes ahorrar, ¿se entiende?

**Maximiliano Palmero**: Sí, por ejemplo, a ver,

**Agustin Garcia**: Pero

**Maximiliano Palmero**: yo le podría preguntar eh, o sea, funciona por eso de las dos maneras, ¿no? Como como dashboard y reportería y como consulta, como preguntándole cosas las dos. Decme de todas las notas de pedido que tengo abiertas a

**Agustin Garcia**: totalmente

**Maximiliano Palmero**: clientes, ¿cuáles tengo stock para entregar y cuáles no, por ejemplo, no le sacaría Yeah.

**Agustin Garcia**: eh mira Ten. La respuesta es sí. Tenemos clientes que arman motores de alerta con eso utilizando esto, ¿entendés? Porque hoy en día vos eh con inclusive con Cloud podés armar un motor de alertas que que básicamente te puede ir anticipando porque lo que se usa mucho también es para anticipar quiebres de stock, ¿entendés?

**Maximiliano Palmero**: Claro.

**Agustin Garcia**: Entonces esto te permite inclusive aplicar, digamos, modelos matemáticos o de machine learning sobre tus datos. que de otra manera eh nada, sí lo puedes hacer, sí lo puedes hacer, pero tenés un proyecto, involucrar gente, hacer una inversión que hoy

**Maximiliano Palmero**: Claro, alertas a los por ejemplo de,"Che,

**Agustin Garcia**: la

**Maximiliano Palmero**: esto no lo estás entregando, lo tenés, tenés un periodo de venta, lo tenés en stock y no te estás dando cuenta que lo tenés que liberar, está vencido, está por vencer, todas esas cosas,

**Agustin Garcia**: mira, estamos ahora justo en el medio, me sacar justo este caso de uso. Estamos justo ahora en un proceso haciendo algo así para una empresa muy muy de de consumo masivo que produce que básicamente analizando eh no los quiebr de stock, pero sí los motivos de evolución de toda la TAM, ¿entendés? Que tienen no sé cuántas cursales, no sé todos los países. Entonces nada, un análisis de de semanas, ¿entendés? Lo hacemos un rato. Entonces la respuesta es sí. Ahora lo que pasa que yo te cuento todo esto y es como que nada, parece como medio, viste, soplear y hacer botellas. La verdad que nosotros siempre lo que le proponemos a todos esamos una prueba de concepto si quieren con datos de ustedes que pueden ser datos reales o si quieren datos damis, pero datos que a ustedes les represente y que cuando vean el análisis digan,"Ah, sí, ahí va." ¿Entendés? y traen los casos de uso que que ustedes quieren explotar y con que quieren trabajar y los hacemos en un rato y ahí lo van a ver porque sí, obviamente que la parte de reportería y todos son como agregados que digamos te suma mucho, pero eso es donde van a ver bien tangible el valor.

**Maximiliano Palmero**: Una pregunta, Agustín, primero si tenés alguna demo para algo para mostrarnos para no hablar en el aire.

**Agustin Garcia**: Sí, claro. Mira,

**Maximiliano Palmero**: Y pregunto mientras lo buscas. Entonces, para confirmar la idea,

**Agustin Garcia**: sí,

**Maximiliano Palmero**: el valor agregado de tu servicio tiene que ver con los conectores, con el IRP.

**Agustin Garcia**: no te entendí la pregunta,

**Maximiliano Palmero**: Eh,

**Agustin Garcia**: perdón.

**Maximiliano Palmero**: yo puedo aprender a usar la inteligencia artificial y puedo aprender a a manejar una base de datos con IGA,

**Agustin Garcia**: Sí.

**Maximiliano Palmero**: pero nunca sabría no mi nivel de conocimiento cómo hacer con esa API, con esa conexión alp Ahí

**Agustin Garcia**: es eso es una cosa que te puedo decir ni te preocupes porque primero que es

**Maximiliano Palmero**: está.

**Agustin Garcia**: sencillísimo y segú Yeah. que nosotros tenemos un equipo de customés que básicamente se ocupa de acompañar al cliente para que pueda ir logrando todas las cosas. Y también por otro lado e para que sepas de que de que inclusive nuestra intención no es venderles servicios profesionales, sino que ustedes vayan absorbiendo el conocimiento para que después puedan trabajar de forma autónoma. Sí.

**Maximiliano Palmero**: ustedes ayudan,

**Agustin Garcia**: Mira,

**Maximiliano Palmero**: capacitan a los motores de búsquedas en la adecuación de los PR y todo eso.

**Agustin Garcia**: nosotros no hacemos, o sea, nosotros no hacemos, digamos, no damos una, digamos, como no hacemos una clase de, digamos, de de por así decirlo, de eh de cómo promptear, ¿sí?

**Agustin Garcia**: les damos como eh una ayuda de cómo estructurar los datos, cuáles son las mejores formas de de hacer, cuál es la mejor forma de estructurar los datos, las gold table, cómo generan los reportes, digamos, todo como para que ustedes vayan aprendiendo cómo usarlo y sacar el mayor provecho. Después, la verdad que aprender cómo se escribe el promp, eso es algo sencillo. Ahora te puedo asegurar que el prom que yo haga va a ser bueno, pero el que vos hagas con la con el conocimiento de tu negocio va a ser 10 veces mejor, ¿se entiende? Porque vamos, esto es una herramienta que cuanto vos eh más

**Maximiliano Palmero**: Te cuento,

**Agustin Garcia**: la usar, digamos,

**Maximiliano Palmero**: te cuento,

**Agustin Garcia**: en el que vas a poder hacerlo solo.

**Maximiliano Palmero**: te cuento de sanciones. Eh,

**Agustin Garcia**: Mientras te voy mostrando esto.

**Maximiliano Palmero**: nosotros tenemos

**Agustin Garcia**: Esto es Teramot. Sí. Acá yo tengo distintos espacios,

**Maximiliano Palmero**: Sí.

**Agustin Garcia**: ¿no? Para que vean. Yo creo que tengo acá un proyecto. A ver, tenemos setemos. A ver, puede ser el de Travels. A ver, estos son distintos espacios. Voy a hacer prueba rápida como para que ustedes también acá tenemos, por ejemplo, un dashboard.

**Agustin Garcia**: Pero bueno, si querés mientras preguntamme, yo mientras voy mostrándoles como cómo esto se conecta.

**Maximiliano Palmero**: Te preguntaba si si mal lo entendí, el servicio de ustedes se conecta directo a nuestro IRP o a una bajada de datos de nuestro IRP.

**Agustin Garcia**: funciona de la siguiente manera. La fuente de origen no se toca. Sí, lo que se hace es se se ingesta la información de esa fuente para eh digamos traer los datos.

**Maximiliano Palmero**: Oh.

**Agustin Garcia**: Ahora, esos datos se traen eh con una recurrencia que es la que ustedes definan. Por ejemplo, tenemos clientes que lo que lo que quieren que la ingesta se haga cada 10 minutos y tenemos clientes que para alguna fuente lo pide una vez al día, ¿entendés? Depende cuál es el objetivo y cuál es la necesidad. Entonces, según

**Maximiliano Palmero**: Es una bajada, es una bajada de que alimenta No. el sistema de

**Agustin Garcia**: Exactamente.

**Maximiliano Palmero**: ustedes.

**Agustin Garcia**: Estudos acá. Perdón, pero hace mucho que no hago demo Ah.

**Maximiliano Palmero**: Te decía que la sensación que yo tengo, obviamente la herramienta es muy poderosa, el servicio de ustedes puede ser muy bueno, no lo conocemos por ahí. Eh, voy a hablar de nosotros, todavía tenemos eh la información no está tabulada, no está depurada o no está tan no me siento tan cómoda con nuestra nuestra información al nivel de decir,"Listo, estamos preparados para que cuando voy y lo exploto no me trae todo sucio." ¿Entendés?

**Agustin Garcia**: Claro.

**Maximiliano Palmero**: Estamos más en una si se quiere estamos corriendo

**Agustin Garcia**: Pero el esa limpieza y transformación, esa limpieza y transformación la puedes hacer directamente con esto. Y es más, de hecho, en el proceso nosotros tenemos un montón de agentes que digamos estandarizan y limpian la información. Inclusive eh todo lo complementario lo puedes sacar y lo puedes gestionar directamente con esto, porque digamos vos antes que hacías el query SQL, mirabas la base tabla por tabla, eso ya hoy lo puedes hacer automáticamente con esto y en cada paso puedes tener exactamente el el el script SQL que ejecutó contra la base, ¿entendés? Como para inclusive auditarlo, ¿se entiende? Mientras te muestro, te voy mostrando ahora. No, no, no me acuerdo bien que tiene eh esta esta base, pero ahora lo vemos a ver que para que ustedes también vean cómo funcionan.

**Maximiliano Palmero**: Ahora la desde Cloud.

**Agustin Garcia**: Eh,

**Maximiliano Palmero**: o desde la interfaz del usuario para con las consultas y los

**Agustin Garcia**: ¿cómo? ¿Cómo?

**Maximiliano Palmero**: dashboard es desde cloud o enterament.

**Agustin Garcia**: Mira, eh, vos tenés, yo lo uso por cloud, nosotros usamos cloud porque, bueno, abandonamos chatt hace ya unos meses por una cuestión de de potencia.

**Agustin Garcia**: Eh, vos adentro de Teramot también tenés el modo agente que tiene un agente que te permite hacer un montón de cosas. gestionar la data, conversar con los datos, digamos, eh es menos potente que cloud, pero nosotros tenemos, digamos, eh varios tipos de usuarios y generalmente el licenciamiento también de acuerdo al flavor, porque tenemos distintos distintas versiones del producto, porque hay clientes que lo tienen implementado in house en sus en su data center porque hay algunas industrias que que no quieren sacar los datos por cuestiones de compliance. Entonces, nosotros tenemos una versión eh que se implanta. Eh, y eh te decía eso porque, bueno, de acuerdo al al al al a la versión del producto, pero siempre tenés el usuario member como que es el administrador que tiene Tak con MCP, que vos podés usar el producto por eh cloud, por chat, por lo que necesites. Y si no, también está el usuario viewer, que el usuario viewer el destino que tiene es poder acceder a la reportería. Sí. A ver si tengo acá, déjame ver, déjame ver si tengo algún dashboard. A ver acá. Entonces, mm, dashboard. A ver, no tengo. A ver. Ah, mira, acá tengo un dashboard. Por ejemplo, entonces yo acá tengo un dashboard.

**Agustin Garcia**: Esto era para una empresa que que de viajes muy grande que estaba viendo de cómo se hacían este tipo de cosas. Entonces yo generé este dashboard que lo publiqué directamente con Cloud. Entonces, si yo fuese un usuario viewer, solo voy a tener acá acceso a eh los dashboard que tengo disponibles para mi por mis permisos y por mi estructura jerárquica dentro de la empresa, porque no todos pueden ver todo. Y yo también tengo la posibilidad de conectarme con el agente para que la gente me poder conversar con los datos, ¿se entiende? Entonces, vos puedes usarlo por cloud, pero tal vez no, porque digamos no necesariamente vas a tener licencia de cloud para eh toda la empresa. ¿Me explico? Buenísimo.

**Maximiliano Palmero**: Sí.

**Agustin Garcia**: Entonces, por ejemplo, si yo voy a hacer una prueba rápida para que vean esto, yo hago el listado de tablas, obviamente que puedo seguir, digamos, escarvábando, le puedo pedir que me haga el modelo de datos, puedo, digamos, puedo hacer toda la parte digamos técnica de datos, la puedo hacer. Ahora, eh si yo quisiera, por ejemplo, vamos a pedirle algo raro, eh en función de eh la información de reservas que tenés, quiero que me armes una proyección de eh promociones para la próxima temporada.

**Agustin Garcia**: Entonces también esto van a ver que que ustedes ya deben saber cómo funciona, pero inclusive si vos eh ponés digamos que información erróne o faltante porque digamos le estás pidiendo algo y necesita más data, bueno, el mismo club también te va te va preguntando como para poder completar el análisis. Después cuando uno agarra, le va agarrando la mano, ya no necesitas que eso porque uno pone un promp completo que no deja lugar a duda, ¿no? Entonces acá puedes ir viendo qué hace. Inclusive vos también podés ir viendo, fíjate, ¿entendés?

**Maximiliano Palmero**: Yes.

**Agustin Garcia**: El request que hace, la información, lo que trae, ¿sí? toda la data que se entiende que va sacando, que es todo lo que va haciendo. Acá hice algo rápido sin pensar. La verdad no me acordaba tampoco muy bien que qué tenía eh la base, pero es más que nada para ejemplificar. Obviamente que lo ideal es, como les comentaba la otra vez, hacer esto mismo con un set de datos de ustedes y que ustedes traigan un caso de uso y lo resolvemos en el momento. Eh, y ahí es donde ustedes van a poder ver realmente el valor de esto, ¿no? Hoy en día, digamos que control de gestión, finanzas, administración es donde vemos que hay más eh es donde hay más trabajo manual y esto es una herramienta que aporta un montón de eficiencia.

**Agustin Garcia**: Después, obviamente que en marketing, en comercial, eh en compras también, en distintas áreas también tiene impacto. ni hablar en en compras donde de empresa grande donde hay licitaciones o ahí todo lo que es análisis de pliego y todo de respuestas es una cosa digamos muy muy de mucho impacto, ¿no? Tal vez fue un pedido un poco, quería que sea un poco más breve, pero acá te va diciendo todo lo que va haciendo. Acá vas viendo la interacción.

**Maximiliano Palmero**: A ver,

**Agustin Garcia**: Sí,

**Maximiliano Palmero**: entonces lo que estás haciendo, estás leyendo un tablero de de Teramot y haciéndole consulta desde ahí en vez desde

**Agustin Garcia**: yo le hice yo le hice una consulta,

**Maximiliano Palmero**: la

**Agustin Garcia**: le le pedí que haga algo sobre los datos. Imagínate como que estos datos son de ustedes, ¿entendés?

**Maximiliano Palmero**: que ahí no estoy entendiendo es para qué necesito Teramot,

**Agustin Garcia**: Porque

**Maximiliano Palmero**: porque esto mismo lo puedo hacer eh ahora con Claud y con mi sistema.

**Agustin Garcia**: vos puedes conectar tu sistema cloud.

**Maximiliano Palmero**: Sí. un MCP,

**Agustin Garcia**: Si ustedes pueden conectar sus sistemas a Cloud, tal vez no necesitan esto. Lo que pasa que hasta acá no no no vemos muchos

**Maximiliano Palmero**: Ah.

**Agustin Garcia**: sistemas conectados a CL que aparte sean eficientes en términos de consumo de tokens y que tengan todas las digamos capacidades adicionales. No, inclusive ni siquiera no sé qué tienen de IRP ustedes tienen SAP.

**Maximiliano Palmero**: No, no, no tenemos un sistema ya no hay favor

**Agustin Garcia**: Bueno, porque ni ni SAP tiene algo así hoy en día. Y

**Maximiliano Palmero**: porque usando que que sí lo estamos usando.

**Agustin Garcia**: info, bueno, si ustedes tienen MCP lo pueden conectar y ya capaz que no necesitan esto, ¿eh? O sea, hay que ver, digamos, después a lo mejor si tienen un alto consumo de token cuando tienen que hacer cualquier análisis, bueno, a lo mejor ahí puede llegar a ser Ne. una posibilidad que evalúen algo como lo que tenemos nosotros, pero la realidad es que bueno, esto lo que te permite es el armado del data lake, que ahí digamos imagínate que vos podés tener tu IRP y todos los otros sistemas consolidados en un solo lugar para poder explotarlo. la conexión al MCP, el agente conversacional para que cada área o cada grupo funcional pueda chatear con hablar con sus datos y después todo el tema de generación de reportes y publicación de reporte de forma automática, que eso es algo que que hoy tampoco está muy muy vigente en otras soluciones.

**Agustin Garcia**: Básicamente es eso. Si vos hoy tenés la posibilidad de conectar el MCP y test performante, tal vez no no estás la solución no es un no les va a cubrir una necesidad puntual, pero bueno, no sé hoy qué capacidad tienen con lo que ya usan,

**Maximiliano Palmero**: Okay.

**Agustin Garcia**: ¿tendés? O sea, eh, pero bueno, esto si ustedes les interesa, podemos hacer, no sé en qué corre ese IRP, no sé que tiene base de datos eh de base, pues seguramente debe trabajar con una base de datos comercial.

**Maximiliano Palmero**: Mira, no tenemos directamente APIC connecten, pero sí tenemos digamos el desde Cloud Code generan una como una consulta que se va actualizando eh al servidor directamente con el permiso. Entonces, de ahí va armando la la red portería, que digamos o bueno,

**Agustin Garcia**: Claro,

**Maximiliano Palmero**: los pan y después,

**Agustin Garcia**: claro.

**Maximiliano Palmero**: bueno, acá me imagino similar a Cloud, le puedes subir los eh las rutas y accesos a cualquier otra cosa que no sea el RP, por ejemplo, el CRM.

**Agustin Garcia**: Sí, claro. Acá le puedes conectar todo lo la idea, ¿cuál es? Es generar el concepto de datalake vos. El IRP es una de las fuentes de de de tu empresa.

**Agustin Garcia**: Tenés varias. digo,

**Maximiliano Palmero**: Sí.

**Agustin Garcia**: ahora para cruzar esa información también, por eso también armas el datalake. Entonces la idea es un poco esa. Acá terminó de armar el reporte plan de promociones para la temporada de verano 2026. Nada, fíjate vos que me saca, ¿entendés? Todo un reporte en función de información específica con proyecto con la base de datos. Honestamente, no no tengo mucho recuerdo de que hay en la base de datos,

**Maximiliano Palmero**: Ok.

**Agustin Garcia**: pero entiend vos podés sacar, digamos, esto es un ¿Se fijaron que yo escribí un renglón? No, no, tampoco le puse mucho mucha onda al tema, pero aún así saca todo un un informe específico que te puede dar un montón de insight para poder, digamos, Okay. trabajar con esos datos. Pero bueno, esto es un tema así puntual con algo que tampoco tiene mucho que con lo que ustedes tienen. le conectas tu fuente de datos o un set de datos específico y y ahí el el diferencial es poder automatizar parte de las tareas que tengan hoy, digamos, con con un proceso que les permita realizarlo de forma eficiente,

**Maximiliano Palmero**: Bien, bueno, perfecto, dale. O sea, nos quedó más o menos claro la idea de la herramienta.

**Agustin Garcia**: No.

**Maximiliano Palmero**: Eh, lo vamos a conversar un poco. Te diga que en principio eh no lo veo tanto, ¿no? más que nada por lo que estamos usando, pero pero bueno, estamos en contacto.

**Agustin Garcia**: Cualquier cosa me avis. Muchas gracias, chicos.

**Maximiliano Palmero**: Muchas gracias.

**Agustin Garcia**: C.

**Maximiliano Palmero**: Saludos.
