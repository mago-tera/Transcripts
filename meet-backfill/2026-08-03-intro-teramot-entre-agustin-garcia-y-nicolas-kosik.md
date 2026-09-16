# Intro-Teramot entre Agustin Garcia y Nicolas Kosik

**Fecha:** 2026-08-03T12:29  
**Duracion:** ~33 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** nkosik@sidersa.com, jcardinali@sidersa.com, Agustin Garcia  
**Externos:** nkosik@sidersa.com, jcardinali@sidersa.com  
**Archivo origen:** Intro-Teramot entre Agustin Garcia y Nicolas Kosik - 2026-08-03 12_29 GMT-03_00/Intro-Teramot entre Agustin Garcia y Nicolas Kosik_ 2026_08_03 12_29 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Reunión de presentación para integrar Teramot y analizar viabilidad técnica en proyectos de automatización logística industrial.Presentación de TeramotSe introdujo Teramot como plataforma para unificar datos fragmentados y facilitar la implementación de inteligencia artificial. La herramienta automatiza la limpieza y estandarización de datos para mejorar la eficiencia operativa.Capacidades y despliegueTeramot soporta arquitectura Medallion en AWS con opciones de despliegue en la nube o local. La plataforma permite conectar diversos modelos de inteligencia artificial para realizar proyecciones y análisis.Evaluación del proyectoSe acordó revisar las especificaciones técnicas para un sistema de cubicación personalizado. La viabilidad del desarrollo dependerá de una evaluación técnica posterior sobre los requisitos del negocio.

### Próximos pasos

[Agustin Garcia] Revisar proyecto cubicación: Revisar la documentación técnica del proyecto de cubicación enviada por Nicolas Kosik con el equipo técnico de Teramot para determinar si es viable su ejecución.
[Agustin Garcia] Enviar presentación Teramot: Enviar la presentación sobre la plataforma Teramot a Juan Jose Cardinali y Nicolas Kosik para que puedan revisar los detalles del servicio.

### Detalles

Introducción y estado actual de proyectos: Juan José Cardinali menciona que actualmente gestiona aproximadamente 11 proyectos, incluyendo la digitalización de la academia de suministros, la implementación de un sistema de visión artificial (para el cual ya han recibido las cámaras) y un sistema SCADA (00:00:11). Agustín Garcia presenta a Teramot como una plataforma que actúa como habilitador para la implementación y el uso de inteligencia artificial, funcionando como un eje central para el manejo de datos (00:01:15).
Antecedentes del contacto: Juan José Cardinali señala que el contacto con Teramot fue solicitado por Héctor García. Agustín Garcia indica que verificará si existe alguna relación previa con el equipo a través de Gabriel Puerta, uno de los cofundadores que trabajó anteriormente en Tenaris, aunque no se confirmó una relación directa con Héctor García (00:02:21).
Propuesta de valor de Teramot: Agustín Garcia explica que Teramot resuelve las limitaciones que enfrentan los modelos de lenguaje de gran tamaño (LLMs) al procesar datos, los cuales suelen ser dinámicos y no lineales. La plataforma facilita la gestión y explotación de datos al permitir la creación de un lago de datos (Data Lake) unificado, conectando fuentes distribuidas como sistemas ERP, CRM y archivos de Excel que frecuentemente están fragmentados (00:03:55).
Automatización de limpieza y estandarización de datos: La plataforma permite ingestar diversas fuentes de información y automatizar la limpieza y estandarización de los datos según las premisas definidas por el usuario. Agustín Garcia destaca que esto mejora la productividad, ya que el personal de ciencia de datos no necesita dedicar una gran parte de su tiempo a la validación manual, puesto que la herramienta interpreta automáticamente el modelo de datos y crea la metadata necesaria al momento de la ingesta (00:06:50).
Integración de inteligencia artificial y casos de uso: Los usuarios pueden conectar LLMs (como Gemini, el cual utilizan en la empresa) a los datos procesados para generar proyecciones o modelos de planificación (00:09:17). Agustín Garcia comparte casos de éxito donde clientes logran reducir tareas de auditoría de cuentas a pagar de 10 días a 10 minutos, o generar proyecciones de planificación de planta basadas en variables como el dólar o la inflación en 20 minutos (00:10:48).
Mercado y metodología de prueba de concepto: Teramot trabaja con diversas empresas, desde grandes compañías como Coca-Cola, Johnson & Johnson e YPF hasta empresas del segmento medio (Mid Market) que pueden carecer de grandes equipos de analistas de datos (00:13:45). Agustín Garcia describe que su metodología incluye una prueba de concepto (PoC) utilizando los datos propios del cliente, la cual no suele tener costo, salvo que la extracción de datos requiera un trabajo extenso, con el objetivo de demostrar la eficiencia y productividad de forma tangible (00:15:15).
Capacidades técnicas y arquitectura: La plataforma ofrece un modelo de Software como Servicio (SaaS) basado en una arquitectura tipo Medallion en la plataforma AWS, cumpliendo con certificaciones de seguridad SOC (00:20:47). Incluye módulos para reportes de inteligencia de negocios (BI), motores de alerta para indicadores clave de desempeño (KPI) y la capacidad de conectar LLMs mediante protocolos MCP (00:18:05) (00:21:49).
Flexibilidad de despliegue: Aunque el modelo estándar es en la nube, Agustín Garcia menciona que Teramot posee variantes para implementar la API en la nube propia del cliente o en sistemas locales (on-premise) si existen restricciones de cumplimiento que impidan el movimiento de datos a una nube externa (00:05:29) (00:23:08).
Enfoque en datos frente a entrenamiento de modelos: Juan José Cardinali aclara que, aunque la plataforma es útil para mejorar la calidad de los datos, el enfoque de la empresa requiere herramientas para entrenamiento de modelos e inferencia (mencionando herramientas como Roboflow). Agustín Garcia confirma que, si bien el núcleo de Teramot es el manejo de datos, el sistema permite conectar cualquier modelo de inteligencia artificial, incluidos modelos propietarios que los clientes deseen utilizar (00:19:33) (00:23:08).
Necesidad específica: Sistema de cubicación: Juan José Cardinali describe el desarrollo de un sistema de cubicación (renderizado 3D de carga en camiones) que requiere adaptarse a reglas de negocio específicas no cubiertas por soluciones actuales como Easy Cargo (00:24:13). Agustín Garcia explica que, aunque el desarrollo de software a medida no es el núcleo del negocio, la empresa realiza este tipo de tareas para clientes grandes y está dispuesta a revisar la especificación técnica para evaluar su viabilidad (00:25:19).
Próximos pasos para el sistema de cubicación: Juan José Cardinali y Nicolas Kosik confirman que enviaron por correo electrónico las especificaciones técnicas del proyecto (00:25:19) (00:28:58). Agustín Garcia se compromete a revisar esta documentación con el equipo técnico y dar una respuesta, considerando que el plazo para cerrar esta condición es de dos a tres semanas debido a que trabajan en conjunto con la firma Globant (00:26:29) (00:29:59).
Modelo de precios: Agustín Garcia explica que el modelo de negocio se basa en la cantidad de usuarios y el volumen de datos. Indica que, para empresas con aproximadamente 50 usuarios, el costo mensual estimado se sitúa en el rango de los 3,000 a 3,500 dólares, destacando que el valor generado por la eficiencia y productividad suele justificar la inversión frente a soluciones de alto costo (00:30:55).

---

## Transcripcion

**Juan José Cardinali**: Hola,

**Agustin Garcia**: Hola, Juan, ¿cómo estás?

**Juan José Cardinali**: ¿cómo Agustín? Bien,

**Agustin Garcia**: Y vos,

**Juan José Cardinali**: bien,

**Agustin Garcia**: alegro, che, ¿cómo anda todo?

**Juan José Cardinali**: bien. Gracias a Dios. Arado la semana con un montón de cosas, pero

**Agustin Garcia**: Y sí, y sí, sí. Arranca el lunes y volvemos a empezar.

**Juan José Cardinali**: todo la cantidad. Sí.

**Agustin Garcia**: Vamos a hacer otra.

**Juan José Cardinali**: Acá la cantidad de cosas que tenemos son impresión.

**Agustin Garcia**: Bueno, pero para eso eso es bueno,

**Juan José Cardinali**: ustedes como es positivo.

**Agustin Garcia**: ¿eh? Eso es

**Juan José Cardinali**: Sí, sí, coincido, coincido. Nosotros estamos en una,

**Agustin Garcia**: bueno.

**Juan José Cardinali**: yo tengo alrededor de 11 proyectos diversos y muchos tienen que ver con la digitalización de la academia de suministros y muchos están ahí de implementarse. Sistema de visión, hay un sistema de visión artificial que ya están,

**Agustin Garcia**: Claro.

**Juan José Cardinali**: hoy me avisaron que llegaron las cámaras, ya se está trabajando para empezar la implementación. Todo el tema de Escada también ya se está armando y sí se está empezando a poner bueno esto.

**Agustin Garcia**: Qué bueno, me alegro. Bueno, sí, nosotros también. Por suerte estamos a full. te podrás imaginar que que bueno, nada, un poco la plataforma que tenemos es es un habilitador, digamos, para la implementación y el uso de inteligencia artificial. Eh, entonces te imaginarás que estamos eh a full, así que

**Juan José Cardinali**: Sí. Eh, yo yo te comento,

**Agustin Garcia**: nada.

**Juan José Cardinali**: yo soy ingeniero industrial de base y tengo un máster en operaciones y tengo estoy haciendo un máster en inteligencia artificial. Eh, contame un poco después de la plataforma.

**Agustin Garcia**: Mira,

**Juan José Cardinali**: Yo no tuve tiempo de meterme. Eh, vi que ustedes se dedicaban a los datos, digamos, análisis de datos el cor, digamos, de contar un poco eh trabajos industriales,

**Agustin Garcia**: sí,

**Juan José Cardinali**: si puede ser que hayan

**Agustin Garcia**: sí,

**Juan José Cardinali**: hecho.

**Agustin Garcia**: te cuento. Mira, yo tengo una presentación, pero la verdad que te lo voy contando y después si querés te paso la presentación como para así lo hacemos un poco

**Juan José Cardinali**: Sí,

**Agustin Garcia**: más dinámico.

**Juan José Cardinali**: sí,

**Agustin Garcia**: Te cuento un poco cómo

**Juan José Cardinali**: vos sos para vos llegas.

**Juan José Cardinali**: Yo te contacto por Héctor García y por parte de Héctor García y que me pidió que los

**Agustin Garcia**: Sí.

**Juan José Cardinali**: contacte. Vos tenés, sos conocido de él, trabajaste con

**Agustin Garcia**: No, no, con Héctor no.

**Juan José Cardinali**: él.

**Agustin Garcia**: Eh, de hecho, déjame que lo busco a ver si si por algún motivo alguno de los muchachos eh lo conoce. Yo creo que había un contacto, alguna relación, no sé si con eh con Gabriel, a ver, es uno de los cofundadores Cong. Gabriel Puerta. abriel puerta trabajó muchos años en de China en Tenaris, entonces no sé si vendrá por ahí el contacto, ¿eh? A ver, que acá me fijo, ¿no? Pero bueno, nada, eh, aprovecho y te cuento. Eh, pero sí, alguna relación hay, porque digamos eh yo ya los había escuchado, pero después nunca creo que en algún momento estuvimos en contacto con alguien, pero después la la cuestión no prosperó. Eh, pero bueno, aprovecho y te cuento. Yo te después te paso la presentación. Te voy a contar un poco eh rápidamente de qué se trata la plataforma.

**Juan José Cardinali**: Hm.

**Agustin Garcia**: La plataforma es una plataforma que básicamente te permite operar con datos y con inteligencia artificial.

**Agustin Garcia**: Sí. O sea, hoy en día hay el todos los LLM que que básicamente que hoy eh trabajan eh eh básicamente tienen una limitación para el uso eh de los datos. Eh, entonces ese es un poco el espacio que viene a a cubrir Teramot. ¿Por qué? Porque hace poco también Cloud Antropic sacó un paper que explica por qué ellos no tienen la posibilidad de trabajar con datos como digamos el público espera, porque básicamente los datos no son líneas de código, sino son entidades más dinámicas que requieren, digamos, como otro tratamiento. Inclusive también vos tenés algunos modelos, como por ejemplo Supase, que es una es una, no sé si la conocés, pero es una base de datos remota que tiene integración con cloud. Y bueno, vos podés conectar una base de datos, pero la realidad es que la transaccionalidad no es la mejor y, de hecho, tiene un consumo de token bastante importante. Y ahí es donde se demuestra un poco el valor de lo que es eh Teramot, que básicamente eh te permite, digamos, gestionar tus datos y explotarlos con inteligencia artificial. Eh, entonces, ¿por qué? Porque básicamente lo que te permite hacer eh Teramot es generar un datal. Sí. Eh, vos hoy seguramente debés tener datos distribuidos, información no consolidada, ¿no?

**Agustin Garcia**: O sea, por ejemplo, información de los proyectos, información de la planta, información comercial, información de logística, todos generalmente separados. Lo que pasa muy comúnmente es que vos tenés tu IRP con la información de base, pero después tenés sistemas, digamos, eh que no están unificados y consolidados en en una misma fuente o en un mismo datalake para que vos puedas, digamos, correlacionarlos y explotarlos y sacar valor a los datos que tenés, ¿no? Entonces, lo que te permite es tenemos varias formas, ¿no?, de yo te cuento un poco la base porque digamos la herramienta tiene distintas posibilidades de implementación porque hay algunas industrias en las que o por motivos particulares eh no quieren mover sus datos a una nube externa por cuestiones de compliance. Entonces ahí nosotros tenemos una versión que se implanta en el datalake de del cliente para que puedan hacer todo lo que te voy a contar directamente en en su datalake, ¿no? Ahora, vos lo que puedes hacer con Teramot es, por ejemplo, tenés el sistema del IRP, tenés el sistema del el CRM, por ejemplo, o el el sistema que usen para planificación y control de gestión, el planificación de planta también. Y por ejemplo, seguramente tenés algún área que trabaja con Excel todavía, ¿no?

**Agustin Garcia**: Entonces eso cuando vos querés ir a explotar la información es digamos realmente complejo. Entonces Teramot lo que te permite es ingestar las distintas fuentes, ¿sí? En un datalake, que es un datalake que es de ustedes. Básicamente nosotros lo que facilitamos es esa eh simplicidad y la disponibilidad de armar ese datalake rápidamente y después poder gestionarlo con inteligencia artificial. ¿Qué te qué qué qué significa esto? Digamos, todo lo que es la limpieza y estandarización de los datos lo hace la herramienta automáticamente según las premisas que vos le digas. Y después, por otro lado, a vos lo que te permite es

**Juan José Cardinali**: para un punto ahí. Eso es diría que lo más difícil,

**Agustin Garcia**: Sí.

**Juan José Cardinali**: ¿no? Digamos, tratar de limpiar los datos de las cosas más difícil que hay y ustedes tien como una automatización de esa

**Agustin Garcia**: Sí, exactamente.

**Juan José Cardinali**: parte.

**Agustin Garcia**: Hay una automatización e inclusive también digamos hoy en día también que se está trabajando muy fuerte con todo lo que tiene que ver con la gobernanza de datos, vos hoy podés armar un diccionario de datos, podés hacer una evaluación de la calidad de tus datos, la verdad que pronteando, ¿entendés?

**Agustin Garcia**: Entonces digo, el trabajo que hace un analista de datos, o un data science, que básicamente cuando tiene que armar una iniciativa nueva de datos, el 70% de su tiempo se pierde en la limpieza, en la validación de los datos. Bueno, eso lo resolvés muy rápidamente, eh, inclusive por medio de la inteligencia artificial, haciendo promps tus datos. Y eso es lo que ese es el el el habilitador número uno que tiene Teramot. ¿Por qué? porque te permite limpiar y consolidar tus datos de forma sencilla, ¿no? Entonces, esto es un un avance en eficiencia y productividad importante porque primero tu data science o tu analista de datos no necesita tener, digamos, una un conocimiento técnico profundo. Sí. Y no necesita tampoco tener un conocimiento profundo del negocio. ¿Por qué? Porque también Teramot, una de las ventajas que tiene cuando vos ingestás los datos es interpreta el modelo. Sí. te permite interpretar el modelo. Entonces, vos le pasás, ingestass una base de datos y automáticamente le pedís que arme el modelo, levanta y crea la metadata correspondiente y ya sabe que cuáles son las tablas que tiene la información de cliente, la de órdenes de compra, las de cashfow, ¿se entiende? Entonces ahí tenés un avance importante porque básicamente ahí ya tenés

**Juan José Cardinali**: H

**Agustin Garcia**: un terreno ganado en productividad grande. Después una vez que tenés los datos, primero que vos podés conectarle, no sé si hoy en día utilizan algún LLM en particular, no sé si usan Chachipit, si usan Cloud, si usaneme.

**Juan José Cardinali**: Sí, Gemini está como habilitado.

**Agustin Garcia**: No,

**Juan José Cardinali**: con un suite de Google que se usa en la empresa que entre otras cosas tiene

**Agustin Garcia**: perfecto.

**Juan José Cardinali**: Gemini.

**Agustin Garcia**: Bueno, entonces, ¿qué te quiero decir con esto? Vos, por ejemplo, te doy ejemplo ahora, si queremos me contás algún caso puntual que tengas en los cuales, no sé, vengas la planificación de planta o la proyección de de compras para lo que es la producción que vas a tener. Tengo clientes en los cuales arman modelos en función de para armar la planificación de planta. usan, arman modelos en función de ciertas variables, no entiendo que la variable, las variables van a ser distintas para las de ustedes, pero por ejemplo en este caso, como ellos eh alimentan el el canal de consumo masivo, digamos, por ejemplo, son muy sensibles al valor del dólar, entonces digamos van armando escenarios de proyección en función del valor del dólar, de la inflación, de ciertas cuestiones. Y esto lo pueden hacer, digamos, casi te diría, lo más importante es tener los datos.

**Agustin Garcia**: Una vez que tener los datos, después vos le aplicas el modelo de inteligencia artificial que uses sobre esa información y te permite, digamos, generar distintos escenarios supercetos, los cuales para vos tenés que hacer eso manualmente. Capaz que te lleva 3 cu días. Bueno, esto te lo arma en 20 minutos. No te quiero decir que vas a te te lo va a armar automáticamente y esa va a ser tu Biblia, pero por lo menos te va a dar, digamos, una base sobre la que vos puedas trabajar y en vez de pasar 3 días haciéndolo, haces esto en 20 minutos y dedicas un par de horas para analizarlo y validarlo y en función de eso ir tomando las variables que necesites. Te cuento esto como un ejemplo. Después, por otro lado, no sé, hoy en día tenemos casos que para todo lo que tiene que ver con control de gestión y la diferencia, mira, hace estamos haciendo un un piloto con una empresa, digamos, eh de que es eh fabricante de de de comestibles, ¿sí? muy grande y básicamente ellos ya tienen medido cuánto le sale un eh cuánto tiempo les consume la auditoría de cuentas a pagar en control de gestión, por ejemplo, ¿no? Y nosotros lo que hicimos fue ingestamos los datos, aplicamos un modelo de de inteligencia artificial, le definimos ciertos parámetros y el reporte lo sacó en 10 minutos, ¿entendés?

**Agustin Garcia**: Y cuando lo fuimos a validar, la realidad es que lo único que estaba desviado eran temas por falta de parametrización eficiente, digamos, como que nos faltó parametrizar algunas cosas y básicamente un trabajo que a ellos les llevaba 10 días, digamos, lo pudieron armar en 10 minutos y obviamente que después hay una serie de pasos en los que hay que validar la información, digamos, como que hay un trabajo, no es que te voy a decir que lo que te devuelve en la Biblia, pero el incremento reproductividad es realmente importante y esto también empieza a a generar un cambio en la forma de trabajar porque básicamente digamos eh vos antes pasabas estos chicos pasaban antes por lo menos entre una semana y 10 días armando los reportes, confirando todas las variables, todo y ahora eso es algo, ese tiempo lo utilizan para otras tareas, ¿no? Entonces, y así como te cuento esto que en control de gestión, que es un área en la que, por ejemplo, tiene muchos Excel, tiene la información del, como te decía, muy sin consolidar, ¿viste?, distribuida por el IRP, por eh eh distinta todo lo que tiene que ver con cuentas a pagar. Entonces, digamos, eso es un avance importante y esa es un área en la que generalmente hay muchísima tela para cortar, ¿no? Ahora, después también todo lo que tiene que ver con inteligencia comercial, eh digamos eh análisis de clientes, proyección de qué te conviene ir a ofrecerle un cliente otro.

**Agustin Garcia**: tenemos, digamos, ahí distintos casos de uso probados, ¿no? O sea, nosotros estamos trabajando con empresas como Coca-Cola, Johnson y Johnson en en el segmento de Langas. Estamos también con empresas como la compañía general de combustible, digamos, IPF, digamos, estamos eh trabajando con Cuenta Center, pero donde vemos casos de uso, digamos, eh importante, donde la productividad eh pega un salto muy importante. Obviamente que también empresas MAT Mid Market también están subiéndose a esta aventura y ahí también digamos que hay ciertas cuestiones particulares como por ejemplo es más común que en empresas un poco más chicas no haya equipo de de analista de datos grandes, ¿entendés? Alguien que se pueda dedicar a consolidar la información para que la puedas explotar. Entonces, en esos escenarios también hay eh digamos una implementación sencilla. ¿Por qué? Porque también la herramienta no requiere que vos tengas un conocimiento profundo técnico y como también interpreta automáticamente los modelos de datos, digamos que es una, digamos, un habilitador fácil Yeah.

**Juan José Cardinali**: M.

**Agustin Garcia**: ¿Se entiende? Entonces, lo que te permite básicamente es empezar a atacar lo que vos hoy, donde vos hoy tengas cuellos de botella,

**Juan José Cardinali**: Yeah.

**Agustin Garcia**: ¿sí? Eh, y digamos empezar a aplicarle esta eficiencia por medio de la inteligencia artificial.

**Agustin Garcia**: Entonces, digamos, vos seguramente tenés tema de planificación de planta o digamos proyección de compra de materiales o no sé, por ejemplo, también hay mucho en tema de proyectos hay mucho informe de proyecto que generalmente tenés muchas cuestiones a a analizar. Bueno, consolidando toda la información, ahí vos podés generar un reporte de forma muy sencilla y rápida, en la cual después vos vas a usar un tiempo para poder validar, digamos, esa info, dar digamos certeza de que el reporte es correcto y vas a seguir avanzando. Entonces, te genera un nivel de eficiencia eh que es no menor. Y eso también es lo que está empezando a a pasar en el término de nosotros estamos con mucha demanda porque, bueno, nada, eh cuando hacemos una prueba de concepto, nuestra metodología lo que siempre tratamos de hacer porque así yo te lo cuento y resulta un poco abstracto, ¿no? O sea, que bueno, sí te estoy vendiendo como un futuro mejor, pero bueno, después siempre está las dudas de que bueno, los costos, la realmente cuál es la eficiencia que se gana y entonces lo que nosotros buscamos hacer siempre es tratar de hacer una prueba de concepto con datos propios de ustedes, del cliente, porque el dato propio, digamos, ahí marca una diferencia porque vos conocés tu negocio y vos conocés, digamos, los KPI, los valores, los informes que se hacen hoy, ¿no?

**Agustin Garcia**: Entonces, hacemos una prueba de concepto que no en general no tiene costo, salvo que haya que hacer mucho trabajo en la extracción de datos y después aplicamos los casos de uso, vamos y resolvemos los casos de uso puntuales que ustedes tengan hoy, en donde hoy tengan, por ejemplo, cuello de botella o que necesiten sacar, digamos, otro nivel de insight de la información y los trabajamos en una prueba concepto. Y lo que termina pasando es que ahí se tangibiliza, digamos, esta productividad que yo te cuento, esta eficiencia. Cuando vos de repente ves que el informe que te viene llevando tres días a hacer lo tenés en en un rato y después solamente validar y seguir trabajando, eso es, digamos que realmente un punto de

**Juan José Cardinali**: Eh,

**Agustin Garcia**: inflexión.

**Juan José Cardinali**: parece muy bueno. Eh, entiendo, ahora sí entiendo qué es lo el core del producto. No te sirve, por ejemplo,

**Agustin Garcia**: Hm.

**Juan José Cardinali**: para generar un modelo de inteligencia, no te sirve, no te da los pesos de un modelo para que yo después pueda en producción inferir algo. Ustedes no lo hacen.

**Agustin Garcia**: Nosotros tenemos, como te contaba, nosotros tenemos, digamos, el That's Suite tiene distintos módulos y distintas capacidades de customización, ¿no?

**Agustin Garcia**: Entonces, el modelo base es nosotros tenemos un software a service que lo que te permite es ingestar tus datos, armar tu data lake y conectar por MCP el LLM que vos quieras, ¿no? Que por ejemplo nosotros usamos mucho cloud porque el cloud está muy avanzado en un montón de cosas, pero vos podrías conectar el que quieras para trabajar sobre tus casos de uso, ¿no? Ahora, después, como te contaba, la herramienta tiene un módulo de todo lo que tiene que ver con reportes de BI, ¿sí? Como por ejemplo, no sé, ustedes tal vez pueden estar usando tabló, pueden estar usando Power BI. Bueno, esto porque vos hoy con la inteligencia artificial le conectas tus datos y el reporte de BI lo armás en un rato con un prompt, ¿entendés? Y eso queda el reporte puesto se actualiza todos los días como si fuese Power BI y ahí te queda. Sí. Entonces ahí tenés otra pata interesante porque ya ahí cuando tenés que reemplazar licencias de de una herramienta así ya eh Teramo se pagó solo, ¿no? Entonces después vos conectas el LLM que el LLM te va in cloud te va a ayudar a trabajar específicamente sobre el caso de uso. Ahora, ese es el modelo estándar que nosotros tenemos. Ahora, nosotros también tenemos la posibilidad de eh trabajar con otros modelos, inclusive trabajar si ustedes tienen un modelo propietario de una inteligencia artificial que ustedes hayan customizado o si también

**Juan José Cardinali**: CL, no, eso lo Sí, sí,

**Agustin Garcia**: quisieran.

**Juan José Cardinali**: ahí lo que yo te yo entiendo está bueno. Trabajan con MCP, algo, un concepto relativamente nuevo.

**Agustin Garcia**: Claro.

**Juan José Cardinali**: Esa bárbaro.

**Agustin Garcia**: Sí.

**Juan José Cardinali**: Yo lo que creo entender el el cor del producto, si después podemos, yo estoy desarrollando algunas automatizaciones, estaría bueno cuando estén más por Sabida Producción eh volver a entablar un contacto para ver cómo se conecta esto. Lo que no me permite, yo trabajo mucho, por ejemplo, con una plataforma que se llama Roboflow, que ahí yo agarro,

**Agustin Garcia**: Sí.

**Juan José Cardinali**: tomo datos y entreno modelos y después me bajo el modelo, los pesos del modelo para hacer inferencia, ¿no? Te bajas mediante una app y la llamas, modelas y te te predice que va a pasar.

**Agustin Garcia**: Claro.

**Juan José Cardinali**: Ese producto no lo tiene. No sé, está buenísimo lo que vos me contas, pero eh es más te facilita mucho el trabajo de los datos, mejorar la calidad de los datos. Y después sí, como deciste vos, con cualquier prom que conectes,

**Agustin Garcia**: Hm.

**Juan José Cardinali**: con cualquier inteligente artificial que ll conectes, automáticamente vos tenés cualquier casi cualquier tablero que quieras, digamos, cualquier das que se te ocurra, pero eso sería, me parece que el valor agregado realmente es eso, ¿no?

**Juan José Cardinali**: de poder limpiar, hacer una limpieza de datos muy buena, mejorar mucho la calidad de datos y después sí está conectado obviamente a LLMs o otras inteligencias artificial, agentes que te permiten Ten. la productividad en todo el análisis de

**Agustin Garcia**: Exacto. O sea, digamos, vos puedes,

**Juan José Cardinali**: dato.

**Agustin Garcia**: digamos, primero y principal consolidar la info por el datalate que armás. Si ustedes no tienen un datalake, digamos, podría ser la posibilidad de armar un datalake. Segundo, la limpieza.

**Juan José Cardinali**: Eso queda eso usted ven la el almacenamiento en la nube,

**Agustin Garcia**: Sí,

**Juan José Cardinali**: ¿no?

**Agustin Garcia**: sí,

**Juan José Cardinali**: que

**Agustin Garcia**: exacto. Trabajamos nosotros eh trabajamos tenemos es un esquema Medalion en una plataforma AWS.

**Juan José Cardinali**: usted.

**Agustin Garcia**: tenemos certificaciones eh stock, digamos, de seguridad también porque somos auditados cada 6 meses por una cuestión de de la sensibilidad de tener data de de clientes. Eh, y bueno, y básicamente vos podés armar el datalate ingestando la info de los distintos sistemas. Los sistemas no se tocan, o sea, la información de base no se toca, hasta ingesta para que vos después la puedas trabajar y explotar.

**Agustin Garcia**: Entonces, ahí tenés el armado del datalake, la limpieza eh y estandarización de los datos. Después eh todo lo que tiene que ver con eh la automatización de la gestión de la calidad de los datos y eh la gobernanza de los datos. Después vos con esto también obviamente que lo que puedes armar es motores de alerta, ¿sí? Digamos, no sé, puntos de stock, punto de quiebre, digamos, cualquiera de los KPI que vos necesites trabajar sobre esa eh los datos que tenés. te pueden generar de forma sencilla y recurrente para que a vos, por ejemplo, tenemos clientes que digamos manda correos cuando, no sé, está cerca del punto de quiebre de un stock o hay una situación de cuentas a pagar o por el estilo, ¿no? Después ahí tenés todo el módulo de reporte de BI que te permite automatizar y tener los reportes. Digamos, hoy un reporte te puede llevar un par de días. Bueno, acá puedes armar el reporte y dejarlo disponible en un rato e disponibilizarlo para otros usuarios. Le conectas el LLN que vos necesites para trabajar sobre el caso de uso que te hoy digamos eh requieras. Y después también tiene las variantes del del producto que por ejemplo hoy lo tenemos en SAR Service.

**Agustin Garcia**: Si ustedes ya tuviesen un Data Lake podrías eh tener, digamos el API implementada en tu propio en tu propia nube o en tu propio sistema en premis donde tenés las mismas capacidades, pero en vez de haber movido los datos a la nube, lo trabajas sobre los datos donde vos ya los tenés. Nosotros trabajamos con distintos modelos de inteligencia artificial, más allá de de conectarte por el LLM, pero también así como vos puedes conectarte por el LLM, también si vos quisieras trabajar con algún sistema de LLM propietario tuyo o digamos una adaptación de algún modelo, eso se puede hacer sin ningún problema. también como para que vos, digamos, no sé, eh ya tenés una iniciativa interna en la cual estás trabajando con algo por el estilo. Ahí eso,

**Juan José Cardinali**: Buenísimo.

**Agustin Garcia**: el producto se se adapta también para eso.

**Juan José Cardinali**: Bueno, lo vamos yo estoy desarrollando algunas automatizaciones en planta eh te voy a estar contactando. Creo que está está bueno el producto para probarlo. Yo te comento rápido por qué estamos acá,

**Agustin Garcia**: Sí,

**Juan José Cardinali**: digamos, que es por otro tema,

**Agustin Garcia**: sí,

**Juan José Cardinali**: pero desde ya parece hiperinesante lo que comentabas y probablemente estemos probando la herramienta.

**Agustin Garcia**: buenísimo.

**Juan José Cardinali**: Nosotros queremos desarrollar un sistema de cubicación. ¿Qué es un sistema de cubicación? Te debes preguntar. Es es el renderizado de de camiones que vienen a cargar y su correspondiente carga. Nosotros queremos hacer un software probablemente asa service o llave en mano que nos permita rendir los camiones, el tamaño,

**Agustin Garcia**: Mhm.

**Juan José Cardinali**: el volumen, el 3D, los camiones y la carga que va a ir adentro y que el usuario pueda ir llenando el camión manualmente para verificar que si lo que planificó cargar entra o no en el camión y dejar el layout de cómo va va a

**Agustin Garcia**: Ok.

**Juan José Cardinali**: ser esa carga. Eh, hay algunos software en el mercado eh como easy cargo que hacen algo parecido, eh, pero tienen para nuestro para nuestras reglas de negocio no están preparados. Entonces, lo que queremos es algo que se adapte a la totalidad de la regla de negocio nuestra.

**Agustin Garcia**: Ok.

**Juan José Cardinali**: Yo entendí cuando a mí me pasaron la empresa Teramot, por lo que yo leí, entendí que no estaba dentro del scope de ustedes desarrollar una aplicación así porque se dedican a la data, ¿no? A hacer software de este

**Agustin Garcia**: Mira, eh yo te digo una cosa,

**Juan José Cardinali**: tipo.

**Agustin Garcia**: eh nosotros en algunos casos desarrollamos software porque tenemos clientes muy grandes que a veces nos eh solicitan cierto nivel de integración y ciertas cuestiones que eh hace lugar a esta e las tenemos que hacer,

**Juan José Cardinali**: Sí, las tiene que hacer. Sí, sí.

**Agustin Garcia**: ¿sí? O sea, digamos, tenemos con generalmente con los clientes más grandes.

**Juan José Cardinali**: hay hay negocio mayor que tenés que mantener y esto lo

**Agustin Garcia**: Exactamente. Ex. Y por ejemplo, no sé, tenemos eh iniciativas eh con desarrollos eh geoespaciales, ¿entendés? Con ese tipo de cosas que, bueno, si bien no es el core, pero bueno, nosotros lo hacemos, inclusive también eh lo desarrollamos y y lo potenciamos con inteligencia artificial. Entonces, dicho esto, la realidad es que a mí lo que me gustaría es lo voy a revisar con el equipo técnico como para ver porque digo ahí no sé,

**Juan José Cardinali**: Allez Hay una especificación técnica.

**Agustin Garcia**: tal

**Juan José Cardinali**: Tenemos hecha una especificación técnica. Se la mandamos, Nico.

**Agustin Garcia**: vez

**Juan José Cardinali**: Se por hacer se la mandamos.

**Nicolas Kosik**: Sí, sí, por supuesto.

**Juan José Cardinali**: Yanlo. Si si se animan a cotizar y tienen que técnicamente lo pueden llevar a cabo.

**Agustin Garcia**: buenísimo.

**Juan José Cardinali**: Bienvenido.

**Agustin Garcia**: Ahí yo si ustedes me pueden compartir esa documentación para que yo la revise con el equipo y nada y seguramente surja alguna duda o algo,

**Juan José Cardinali**: Sí.

**Agustin Garcia**: yo ahí vuelvo a ustedes y bueno y ahí les contamos y es algo que nosotros podemos hacer. Obviamente que en el caso de que nosotros eh esté dentro de nuestro alcance, inclusive también ahí seguramente nosotros trataremos de de de mostrar algún approach de cómo lo podríamos encarar como para también balear con ustedes si es He. que que puede puede ir por el camino que ustedes necesitan, ¿no?

**Juan José Cardinali**: Buenísimo, buenísimo.

**Agustin Garcia**: Sí.

**Juan José Cardinali**: Eh,

**Agustin Garcia**: Y bueno, si quieren,

**Nicolas Kosik**: No.

**Agustin Garcia**: si quieren podemos analizar esta iniciativa y si quieren después podemos ver algún tema en particular que eso que

**Juan José Cardinali**: bueno,

**Agustin Garcia**: vos me contabas, Juan, como para ver a ver qué cómo les podemos dar una mano también con eso.

**Juan José Cardinali**: tale. Eh, te comento, me parece que hace fit eh con un software que se está creando acá, ya está hecho en realidad que permite automatizar las guías de carga, decidir con un optimizador qué qué paquete va en cada camión.

**Agustin Garcia**: Claro,

**Juan José Cardinali**: Por eso tiene tiene asociado un montón de KPI que queremos reflejar y entiendo que por ahí

**Agustin Garcia**: claro.

**Juan José Cardinali**: una vez que ya la tengamos corriendo,

**Agustin Garcia**: Espectacular.

**Juan José Cardinali**: estaría bueno volver a contactarnos para ver cómo podemos trabajar toda esa data que se genera. Creo que eso me parece que es tenía un buen punto de de contacto con algo que ustedes ya tienen solucionado.

**Agustin Garcia**: Total. Sí, sí, sí. contar con eso, que lo que tiene bueno la plataforma que nada, lo que busca es digamos eh estandarizar, acomodar, consolidar los datos y después explotarlo. Y esto la verdad que es algo que digamos hoy venimos trabajando con distintas áreas. Antes nosotros íbamos con como apuntando a caso de uso específico, hoy estamos más abiertos a escuchar, a ver cuál es la necesidad y ver nosotros cómo los podemos ayudar a resolverlo. Y la verdad que en ese sentido hasta acá no viene funcionando bien y lo que nos termina pasando un poco es que bueno, tal vez entramos como por ejemplo en este sistema de ubicación y después vamos avanzando y tal vez, no sé, el día de mañana querés sumar otras áreas, digamos. La verdad es que es como que se te empieza a generar una cultura de trabajo distinta

**Juan José Cardinali**: No sé, no conozco la estructura de la empresa,

**Agustin Garcia**: que

**Juan José Cardinali**: pero imagino que son desarrolladores muy bien de distintos ámbitos, distintos y pueden abarcar casi cualquier proyecto de tecnología.

**Juan José Cardinali**: Más o menos las que yo conozco de tecnología son así.

**Agustin Garcia**: y sí,

**Juan José Cardinali**: Te piden algo,

**Agustin Garcia**: la verdad que sí que que viene un poco por ese

**Juan José Cardinali**: no sé.

**Agustin Garcia**: lado. Así que nada, si quieren podemos eh avanzar y empezar viendo esto. Nosotros lo podemos analizar y después vamos seguimos charlando.

**Juan José Cardinali**: Bueno, yo te la explico. ¿Vos tenés el contacto de

**Nicolas Kosik**: Sí,

**Juan José Cardinali**: Agustín?

**Nicolas Kosik**: ahí te acabo de reenviar el mail de la propuesta de la licitación con

**Agustin Garcia**: No.

**Nicolas Kosik**: los adjuntos. están las especificaciones del proyecto. Eh, decme si está bien. El mail que ustedes es eh Agustín.garcía@teramot. El del la llamada.

**Agustin Garcia**: Sí. Agustín.García. @teramot.com. Eh, ahí me llegó,

**Nicolas Kosik**: Perfecto.

**Agustin Garcia**: ahí me llegó.

**Nicolas Kosik**: Bien.

**Agustin Garcia**: Fantástico. Así que yo eh veo esto,

**Nicolas Kosik**: Perfecto.

**Agustin Garcia**: lo reviso con el equipo técnico.

**Juan José Cardinali**: Escúchalo.

**Agustin Garcia**: Ahí si están, me imagino que en ese pliego, ¿eh?

**Agustin Garcia**: E vamos a seguramente está el tema fechas, ¿no?

**Juan José Cardinali**: Yo creo que estamos a dos semanas de cerrar, dos o tres semanas de cerrar la condición porque estamos trabajando con Globan,

**Agustin Garcia**: Buenísimo.

**Juan José Cardinali**: con y ya le pusimos una fecha para cerrar este

**Agustin Garcia**: Okay, perfecto,

**Juan José Cardinali**: tema.

**Agustin Garcia**: perfecto. Buenísimo. Entonces, lo revisamos enseguida y nada y ahí nos guiamos un poco seguro con con la información que esté en el pliego.

**Juan José Cardinali**: Vos tenés una presentación, ¿no? Dicho.

**Agustin Garcia**: Y yo se las envío ahora como para que ustedes también puedan puedan revisar un poco los los

**Juan José Cardinali**: Sí, te agradezco. Sí, sí,

**Agustin Garcia**: pormenores de la plataforma.

**Juan José Cardinali**: sí, sí.

**Nicolas Kosik**: Perfecto.

**Juan José Cardinali**: Está la verdad que interesante,

**Agustin Garcia**: Sí,

**Juan José Cardinali**: interesante. ¿Qué hago qué de curioso? No más.

**Agustin Garcia**: sí, cómo no.

**Juan José Cardinali**: Yo sé que esto después depende de de las condiciones de cada uno de los negocios y demás. ¿Qué qué vale un un promedio de por usuario del servicio de ustedes por

**Agustin Garcia**: Mira, la verdad es que nosotros tenemos un modelo de de negocio,

**Juan José Cardinali**: mes?

**Agustin Garcia**: el cual está basado en cantidad de usuarios y en volumen de datos, ¿no? En general, la la restricción más importante es la cantidad de usuarios, pero la realidad es que los planes arrancan para de 400 mensuales a a después para arriba, ¿no? O sea, pero una empresa, no sé, empresas grandes con, no sé,

**Nicolas Kosik**: H

**Agustin Garcia**: 50 usuarios están en el rango de los 3000 3500 mensuales, ¿no? Obviamente que hay variables que que pueden, pero digamos la plataforma no tiene no no el costo no es una restricción la realidad. O sea, y lo que termina pasando un poco es que claro, cuando vos le hablas de eficiencia, de repente ven lo que cuesta la solución y lo que les ahorra o la la productividad que les genera es como que la ecuación supercierra, porque no no es una no estamos hablando de una licencia de $300,000 año como puedo

**Juan José Cardinali**: No, no.

**Agustin Garcia**: pasarte con una herramienta Word Class, ¿entendés? Entonces,

**Juan José Cardinali**: Sí, sí.

**Agustin Garcia**: eh los valores son bastante moderados y y y nada y trae mucho beneficio, por lo cual, digamos, se hace como interesante la

**Juan José Cardinali**: Está bueno,

**Agustin Garcia**: propuesta.

**Juan José Cardinali**: está bueno, está para para verlo. Así que bueno, eh creo que mi correo lo tenés,

**Agustin Garcia**: Sí, sí,

**Juan José Cardinali**: así que también.

**Agustin Garcia**: que tengo todo, así que yo les envío esto. Ahí recibí lo que me pasó Nico, y nada y seguimos hablando, ¿les parece?

**Nicolas Kosik**: Perfecto,

**Juan José Cardinali**: Excelente. Sí, sí, perfecto.

**Nicolas Kosik**: perfecto.

**Juan José Cardinali**: Bueno,

**Agustin Garcia**: Bueno, chicos,

**Juan José Cardinali**: Agustín,

**Agustin Garcia**: les agradezco mucho y que tengan buena semana.

**Juan José Cardinali**: igual,

**Nicolas Kosik**: Igualmente,

**Juan José Cardinali**: igual para vos y un gusto.

**Nicolas Kosik**: Agustín.

**Agustin Garcia**: Un gusto,

**Juan José Cardinali**: Nos chao.

**Agustin Garcia**: que estén muy bien. Chao.
