# Teramot - La Virginia

**Fecha:** 2026-05-15T14:31:56.090+00:00  
**Duración:** ~41 min  
**Participantes:** Gabriel Puertas <gabriel@teramot.com>, Gabriel Salcedo <gsalcedo@lavirginia.com.ar>, Nerina Di Pego <ndipego@lavirginia.com.ar>, Lucio Rojas <lucio@teramot.com>, Juan Peralta <juan@teramot.com>, Cesar Bellini <cbellini@lavirginia.com.ar>  
**Externos:** gsalcedo@lavirginia.com.ar, ndipego@lavirginia.com.ar, cbellini@lavirginia.com.ar  
**Apollo ID:** 6a073819840d2e00217eb146

---

**Gabriel Puertas**: Todo bien.

**Gabriel Salcedo**: Buen día, Lucio.

**Lucio Rojas**: Buen día, ¿Cómo andan?

**Gabriel Salcedo**: ¿Todo bien?

**Cesar Bellini**: ¿Qué tal? Buen día.

**Gabriel Salcedo**: ¿Cómo andan? Bien, todo bien.

**Gabriel Puertas**: Por suerte.

**Gabriel Salcedo**: Vamos a esperar a Nelina Damián hoy se tomó el día así que no va a poder sumarse.

**Gabriel Puertas**: Bueno, pasa nada.

**Gabriel Puertas**: Qué suerte,

**Gabriel Salcedo**: se arrancó el fin.

**Gabriel Puertas**: Me hace acordar a mi antiguo trabajo, tener los cascos ahí en el escritorio.

**Gabriel Salcedo**: Tenemos cofia también para ver.

**Gabriel Puertas**: Claro, eso te iba a preguntar por

**Gabriel Salcedo**: el tema y los zapatos de seguridad. Ya, siempre pues.

**Gabriel Puertas**: Pero los zapatos de seguridad son por seguridad o por tipo, No sé cómo preguntar. Por sanidad, digamos.

**Gabriel Salcedo**: La ropa que usamos, digamos, ya la usamos solo acá, nos cambiamos cada vez que entramos, así que esa parte ya está. Después son de seguridad cuando va a ser algún laburo que no se te caiga nada arriba o si se cae estar cuidando. ¿Dónde estaba antes? ¿En qué tipo de industria?

**Gabriel Puertas**: Ah, perdón, estaba en Techine.

**Juan Peralta**: ¿Que?

**Gabriel Puertas**: Siderúrgica. Ahí no había mucha sanidad, solamente que no te. Que no te aplaste algo.

**Gabriel Salcedo**: Bueno, ahí se va a estar por su mar de harina.

**Juan Peralta**: Hola, perdón por la demora, Fue un día de reuniones tras reuniones y me perdí en el momento de horario

**Gabriel Salcedo**: encima

**Gabriel Puertas**: se te van atrasando y vas arrastrando.

**Juan Peralta**: No, no, en realidad ya había terminado pero me perdí, me puse a hacer un resumen y me perdí.

**Gabriel Puertas**: Buenísimo.

**Gabriel Puertas**: Si quieren yo les muestro lo que hice que. Nada, la idea es más mostrarle la herramienta que lo que yo hice porque ahora van a ver todos los secretos, digamos. Así que vamos con eso mientras voy compartiendo. ¿Ustedes se acuerdan que nos habían pasado una serie de archivos que tenía todo un histórico de un año? Yo voy a sacar esto porque me resulta súper molesto, pero eso implica que

**Gabriel Salcedo**: los dejo de ver.

**Gabriel Puertas**: Yo que tenía acá, tenía las ventas, esto Kilo, el nombre de los archivos, Perdón, vamos por parte. Esta es la página de theramo, o sea yo lo cargué como si fuese un proyecto mío, pero bueno, la realidad sería que lo ideal sería que lo hagan ustedes con su. Su cuenta, con su servicio en particular. Yo tengo estos varios, pero digo en particular el de la Virginia es este, que ese funciona como si fuese un workspace donde ahí armamos un proyecto. Yo le puse de nombre dotación, pero la verdad que tiene más información. Y si cargo acá. Bueno, yo tengo cargado los archivos que ustedes nos pasaron, que como vienen con un CSV, yo los conecté de esa forma, los levanté y están la herramienta. Esto demora un poco. Esto que está en verde quiere decir que están listos para usarse. Eso quiere decir que los modelos de Téramo ya ingestaron los datos, levantaron metadata y entienden de qué va la información. Esa es la idea. Bueno, acá están los archivos como yo los subí, que simplemente esto es un drag and drop, ya lo suben así. Y acá nosotros tenemos una posibilidad de que ustedes puedan ver de qué van los archivos. Sobre todo se los quiero mostrar sobre todo porque por el nombre, o sea, nada. Este que se llamaba kilos disponible, stock, tiene los meses, los kilos disponible y material base en esas tres columnas. Después hay otro que era 24 meses, están levantados acá para los que entiendan, nada, es una query. Acá ustedes podrían escribir otra query y ver los resultados si les interesa entender un poco más de los datos que dispone. Y finalmente hay una cuenta de dotación, que yo después se las muestro cómo se usa nuestra herramienta. Nosotros, la idea está pensada que lo usen a través de un proveedor de inteligencia artificial. En mi caso yo lo conecté vía cloud, no sé si ustedes usan alguno. Si ustedes aprietan este botón, que son como los cablecitos, lo tenemos replicado acá también. Eso es para conectarlo con un proveedor de un LLM. Acá tenemos el instructivo, o sea, estas son las credenciales que se le generan para su caso de uso, y un instructivo de cómo conectarlo. Yo no quiero perder tiempo en ese detalle, pero yo lo tengo conectado acá. Si les interesa, podemos ver en un proyecto de cloud que se llama La Virginia, no sé si ustedes tuvieron oportunidad de ver lo que nosotros le mandamos, no importa. Acá lo que hicimos fue, yo le cargué esos datos acá. Yo voy a ir al inicio de la charla, y lo que le hice a Claude es, una vez que ya estaba conectado, fíjense que esto lo voy a borrar, me quedó una charla vieja. Yo acá lo que le pedí es, le digo, hagamos una tabla Go, que calcule la dotación en función de la información que tiene. Entonces él me dice, bueno, tengo las tablas disponibles, voy a explorar los datos del plan para entender bien las máquinas. Bien, tengo suficiente contexto, uso la integración y ahí lo que hace es generó una tabla go que calcula esa dotación, me calcula para cada producto, creo que ustedes le llaman producto, grupo, no sé cómo le llaman a esto, Café instantáneo, especie T, y para cada uno de los meses disponible del año, acuérdense que me habían pasado todo el 2025 creo que era, calcula la dotación acá. Después seguido a eso le pedí que me genere un documento, que el documento que les mandé, y a partir de ahora esto no sé por qué me lo hizo. Bueno, y acá tiene como esto, el dashboard, ese dashboard que habíamos armado se ve acá, no sé si ustedes pudieron, me dicen que no pudieron ver, pero bueno, nada, lo que hizo acá fue un dashboard donde tiene La dotación del 2025 seleccionada, digamos, diferenciada por cada uno de los grupos, cantidades y bueno, y nada, el mes que quieren calcular, el mes que quieren ver en particular. La idea de esto sería eso, es

**Juan Peralta**: info histórica, info hacia atrás, que es

**Gabriel Puertas**: la que nos pasaron. Y acá hizo un gráfico, este no se lo pedí yo, pero me pareció súper copado, que calculó un promedio de todo el 2025 y dibujó los meses que están por afuera, por arriba del promedio, por ejemplo marzo está muy por arriba del promedio, todo el año, algo así. Y acá diferenció entre dotación directa y los puestos fijos que tiene. Como lo fue armando. Yo lo que hice antes de reunirnos es esto lo voy a cerrar, el coso es pedirle, yo me imaginaba que ustedes nos iban a preguntar cómo se hacía el cálculo, cómo es que generaba el cálculo en función de los datos. Bueno, nada, yo acá básicamente le dije, mirá, en la anterior, estas son interacciones que yo tuve hace un rato, agarré y le explicarme cómo hiciste la cuenta de dotación, supongamos para el caso particular de Café, para que me dé un ejemplo. Buena pregunta, voy a buscar el SQL que se armó para armarte la tabla. Y me fue explicando cada uno de los pasos, eso todo con una base bien técnica de SQL. Y le mirá, no necesito que me lo explique con menos SQL y más didáctico de la fuente de info. Entonces lo que me armó fue este steps. Entonces, que a mí me gusta revisarlo con ustedes para que entiendan si hizo más o menos bien la cuenta me dice lo que hay en el archivo. Cada fila del CSV tiene una combinación de máquina, material y mes. La columna dotación ya viene calculada por SAP E, que es turno por operario de esta máquina. Entonces acá vemos por ejemplo la Bosch 2, paquete 250 gramos. En marzo tiene 2.25 turnos y la dotación es 4.5. Entonces me dice para la Bosch 2 produce tres materiales distintos. En marzo aparecen tres filas separadas, el siguiente paso las consolida en una sola. Entonces si yo me vengo acá, pone la voz 2 hace 2.25, 2.25, 2.25 le da 675 y la dotación le da 13.5.

**Juan Peralta**: Sí, pero ahí hay algo. No, pero hay algo que él diga lo está haciendo bien, lo está pensando bien, pero está mal. Y es que en el archivo nuestro, esas líneas están repetidas para cada producto. Porque la solución que nos daba Kit no lo podía separar. Pero los 2,25 es el total para todos los productos. Para la sumatoria.

**Gabriel Puertas**: Perfecto.

**Juan Peralta**: Que en realidad no es un error de la IA, es el archivo que le dimos. Está así.

**Gabriel Puertas**: En realidad la máquina.

**Gabriel Puertas**: La máquina tiene una fila por cada producto, pero la dotación.

**Juan Peralta**: Los turnos. Y la dotación es la.

**Gabriel Puertas**: Los turnos son por máquina y no por producto.

**Juan Peralta**: Exacto.

**Gabriel Puertas**: Con lo cual tenemos que ajustar eso para todos los.

**Gabriel Puertas**: Para todos los casos, no para nosotros.

**Juan Peralta**: Eso es un dolor, porque antes lo teníamos, como lo interpretó la IA, para cada cantidad de turnos necesarias. Después hacíamos la sumatoria. En un momento tuvimos un cambio de sistemas y no lo pudimos resolver.

**Gabriel Puertas**: Ahí está. Acabamos de decir que esto. ¿Que me está diciendo? Yo un poco la idea de esto es que ustedes entiendan que no es que nosotros somos consultores muy inteligentes, sino que en realidad para hacer todo lo que le hicimos a ustedes utilizamos esta herramienta. Y esta herramienta funciona increíblemente mejor si los que la usan son ustedes. Esa particularidad vos lo hubieses detectado en el inicio de la conversación. ¿Me explico? Me dice, esto es crítico el gobierno. De nuevo, uniforme. Ahí me dice, mira que la Bosch 1, 2, 4, 7 y esta, todas las filas tienen el mismo valor de turno de dotación y hay que tomar el máximo.

**Juan Peralta**: Esperá, pero ahí escuchá de nuevo. Bosch 1 2 4 7. Todas las filas tienen el mismo valor de turnos, pero ahí no. A ver, dentro de la Bosch 1 hay distintos productos, la cantidad de turnos y dotación de los distintos productos de la Bosch 1 terminan siendo el valor de Bosch 1, pero no es que Bosch 1 dos, tres tienen el mismo valor entre ellas. Si tiene el mismo valor es casual. ¿Se entiende lo que dice?

**Gabriel Puertas**: Sí, sí.

**Gabriel Puertas**: Esperá, ahora se lo explicamos.

**Juan Peralta**: Claro, pareciera que lo hizo bien y

**Gabriel Puertas**: vamos a ver acá dice la corrección es utilizar el máximo de turno y máximo de dotación por máquina y mes en lugar de la suma.

**Juan Peralta**: Claro, ahí está. En realidad no existe un máximo, es que va a ser el mismo dentro de la misma máquina, va a ser la misma cantidad de turnos y máquinas para todos los productos, porque el valor ya es sumatoria en ese caso.

**Gabriel Puertas**: Bien, ahí va a borrar la anterior tabla y va a ser una nueva con esa particularidad. Esta tabla, Nerina, la idea es que esta tabla que está generando ahora, ahora es parte de los archivos planos, porque estamos en esta demo, pero vos podrías conectarla a SAP que se actualice con la frecuencia que tenga sentido, puede ser diaria, puede ser mensual, puede ser, podemos

**Juan Peralta**: conectarlo a SAP directamente.

**Gabriel Puertas**: Y claro, esa es la idea.

**Juan Peralta**: Entonces vos estás sin hacer bajada, que lo leas directamente. Si, puede.

**Gabriel Puertas**: Y a la idea, digamos, te armas esta tabla y ya te queda hecho el pipeline de cálculo, o sea, esta tabla la hiciste una sola vez.

**Juan Peralta**: ¿Sí, digamos, la IAP va y busca información en SAP directamente?

**Gabriel Puertas**: No, lo que hace es, cada vez que vos, con la frecuencia que vos definís la actualización, suponte que definimos que vaya y mire SAP una vez al mes, entonces lo que hace va, mira, cuando le toca actualizarse, va, mira, levanta los datos y ahí corre todos los cálculos. Si ustedes quieren que sea diario, va, mira todos los días y corre por eso.

**Juan Peralta**: Pero está leyendo información de SAP, No es que vos tenés que bajar esa información de SAP a un CSV y después dársela.

**Gabriel Puertas**: Si hacemos el conector, lee la información de SAP. Claro,

**Juan Peralta**: Si había información que estaba en otros sistemas, o sea, si hay información que pudiera estar en otro sistema, también se pueden vincular y el mecanismo es exactamente el mismo. Si vos decís, bueno, no sé, quiero que este proceso se corra una vez por semana, bueno, se setea el refresco, entonces Tegramot toma la información una vez por semana, la trae y como decía Gaby, corre todo el cálculo todo el pipeline y deja los datos expuestos para consumo.

**Juan Peralta**: Perdón, insistí con la pregunta porque justo estamos

**Juan Peralta**: para nosotros, si vos me decís es con un Excel también se puede hacer, pero es un poco más rebuscado, hay que hacer más manualidad, hay que bajar el Excel, armarlo, subirlo conectado directamente a una base de datos o a una réplica de una base de datos, es el camino perfecto para nosotros.

**Gabriel Puertas**: Ahí lo que está haciendo, si ustedes se fijan, es calcular esa nueva tabla, fíjense que acá en la descripción ya puso que tiene que estar la corrección, que vienen con los turnos máquina, que se tiene que usar máximo, todas esas cosas. Entonces, como te decía Juan, ya lo genera, genera esa parte, eso se llama un ETL, Neri, es como decir,

**Lucio Rojas**: la

**Gabriel Puertas**: primera parte, la e del ETL, es la extracción de los datos, o sea, con la frecuencia que nosotros definimos, va y extrae datos de SAC, de SAP, los transforma. ¿Qué quiere decir esto? Justamente se fija los datos que necesita, suma lo que necesita para calcular cada una de las dotaciones y los carga en una nueva tabla. Esa nueva tabla es esta que estamos armando, esta dotación la A esa tabla Cloud o chatgpt o Copilot o el modelo que sea que utilicen, la puede ver y puede hacer otras cosas, o sea, ustedes van a tener la información ya lista a partir de esa tabla, la pueden conectar un Power BI o lo que sea, pero además que eso es lo interesante, pueden hacer otro tipo de análisis, tipo ustedes subieron ahora, cuando esto termine, ustedes subieron datos de producción y ese tipo de cosas, ahora le vamos a preguntar a Claudia qué análisis podemos hacer con el resto de la información que disponemos. Es una cosa así. Pero de nuevo, la idea es que entiendan que es como, digamos, tener un modelo que funciona como un asistente, no sé, si ustedes utilizan Copilot o lo que quieran, tener un modelo que tenga acceso a los datos con los que ustedes trabajan normalmente, los acelera muchísimo, tanto en la generación de la información que necesitan pasar, como en optimización y otros análisis. Es un poco la idea. Ahí terminó, vamos a ver acá. Esto en teoría ya está verde, esto me va a dar un preview de esa tabla, tiene valores un poco más bajos. Ahí lo que está haciendo Claude es, si ustedes se fijan, está mirando si, está mirando si lo que generó tiene sentido para lo que le habíamos pedido. Basicalement. Ahí está buscando la tabla. Y si se fijan, no sé, el resto de los chicos más técnicos, esta es la tabla que armó y esto es importante sobre todo para ustedes. Acá queda, acá queda disponible la query de SQL utilizó, o sea, se puede auditar un poco mejor y nada, revisar bien en detalle. Esto para nosotros es importante, porque si ustedes generan una tabla que calcula la dotación en cierta forma tienen que estar seguros de que la cuenta es exactamente lo que ustedes quieren. La única forma en esto es compartirles el código y que puedan ver exactamente qué se va a hacer. Una vez que esta tabla ya está conectada, todos los días se corre este código, no es que hay un agente recalculando cada vez que preguntamos o cosas por el estilo. Una vez que ustedes generaron esto y van actualizando con los nuevos datos, el código que se genera y que genera los nuevos datos de dotación o lo que sea, es lo que pase por este código que está aquí. Entonces eso a usted le da la certeza de que todos los meses o todos los días cuando actualicen información va a ser esa la información que tiene. Bueno, ahí lo que me está diciendo es, la tabla se actualizó con los valores correctos, la diferencia con la versión anterior es enorme obviamente porque estábamos multiplicando fuerte. Ahora, ¿Les gustaría que hagamos algo particular o generamos un nuevo dashboard con esta? Con esta tabla acá un poco preguntarle cómo quieren que sigamos.

**Gabriel Salcedo**: Para mí Neri, vos lo que yo entiendo que te serviría es cargarle por ejemplo los datos del próximo mes, entonces a ver si te da el cálculo que te resuelve si es similar a lo que vos harías. Yo creo que ahí se.

**Gabriel Puertas**: Hagamos una cosa más loca.

**Juan Peralta**: Perdón David, en realidad no lo puedo hacer en un próximo mes, tendría que tirarle el dato en los próximos 12 meses, o sea, tirarle el último. ¿Y que calculo?

**Gabriel Puertas**: Porque la fuente de información de esto es el dato de SAP de proyección, o sea, Si vos tenés 12 meses, te lo va a hacer para 12 meses en adelante. Si vos tenés un año, un año. Pero digo, mira, tenemos.

**Juan Peralta**: Esperá que me perdieron una cosa, ahí está calculando solo los directos, después faltarían todos los indirectos.

**Gabriel Puertas**: Claro, no, ya lo tiene calculado, solo que no lo está mostrando por eso, espera, mira, vamos a una cosa, actualicemos el DAS

**Gabriel Puertas**: con estos datos, ya tenemos un

**Gabriel Puertas**: hecho,

**Gabriel Puertas**: lo actualicemos con esta nueva.

**Gabriel Puertas**: Fíjate ahí lo que está haciendo, acordate que yo te había mostrado este

**Gabriel Puertas**: que

**Gabriel Puertas**: tenía números que eran medio exorbitantes porque llegaba a 250 personas para hacer café,

**Juan Peralta**: Pero igual, incluso en este mismo. Esperá, ¿Esos números qué son? ¿Qué es dotación? ¿Sumatoria anual?

**Gabriel Puertas**: No, este lo que tiene ahora. Van a cambiar. Olvídate de los valores.

**Juan Peralta**: Eso quiero ver los valores.

**Gabriel Puertas**: Por eso los valores los está actualizando.

**Juan Peralta**: Claro, yo. Porque con esa actualización de los valores me doy una idea si está en el orden de lo que es hoy o no.

**Gabriel Puertas**: Claro, claro. Por eso lo está haciendo ahora. Fíjate que dice reemplazando febrero a diciembre con valores correctos. Posiblemente me haga otro de estos dashboard, pero básicamente lo que te mostraba acá era la dotación por mes.

**Cesar Bellini**: La dotación por mes, por sector, entiendo que.

**Gabriel Puertas**: Exactamente. Y acá te lo abre por dotación directa y el resto de los fijos.

**Cesar Bellini**: A ver, mostrame un segundito más el gráfico de arriba. Claro, la dotación directa, los líderes vendrían a ser semi y limpieza son los indirectos, espacio, Bueno, es como que mezcla un poco ahí. Pero obviamente es mayor la dotación directa que el resto.

**Gabriel Puertas**: Claro, porque estos son valores fijos que surgieron de los Excel que nos había pasado Neri. Entonces esto, como no escalan con. Con la proyección, nada, quedaron demasiado chicos respecto a esto que lo estaba sobreestimando. Y ahí, Ahí está haciendo. Está corrigiendo. Acá lo que está haciendo es corregir esos datos del. El archivo HTLM que yo le estaba mostrando cuando llegue a todos los archivos corregidos, seguramente nos lo va a mostrar.

**Cesar Bellini**: Deberían ajustarse más a los que ya tenemos.

**Gabriel Puertas**: Deberían. Seguramente, seguramente que hay sutileza en el cálculo porque nada, estamos haciendo nosotros que no. Por eso la propuesta que lo hagan ustedes. Si ustedes se fijan, bueno, ahí están los números un poco mejor. No sé, Neri, si querés mirar alguno en particular. Por ejemplo acá yo estoy en marzo, esto es 2025, esto era plan 2025, que para T tenía 110 personas.

**Juan Peralta**: Le falta, está parecido.

**Gabriel Puertas**: Le falta, por eso es lo que te digo. Pero nada, la idea es que esa tabla ya te quede calculada. A mí me gustaría mostrarle algo más, porque esto es básicamente lo que consiguió hacer. Si yo me voy a T, ahí tengo GL, no me acuerdo que era GL indirecto, Yerba indirecto total. Y tiene toda la la dotación directa y el resto de los fijos es un dashboard, ustedes le pueden pedir que haga algo diferente, otra cosa que les guste. Lo que a mí me gustaría hacer con los datos ya calculados, es decir

**Gabriel Puertas**: ahora es que tenemos. Con el resto del.

**Gabriel Puertas**: Se va a poner a ver qué info tenemos disponible y lo más probable que haga algún tipo de análisis.

**Gabriel Salcedo**: Gabriel, si nosotros queremos probar esto, entonces la demo ya incluye que tendríamos ese acceso a terab y lo conectamos con nuestro LLM, que en nuestro caso sería Gemini.

**Gabriel Puertas**: Si ustedes quieren probar esto, incluye, si quieren agregar datos diferentes o que le haga más sentido también, bueno, lo conectamos,

**Gabriel Salcedo**: tendrían que dar acceso a alguna cuenta de Teheram o una cosa así.

**Gabriel Puertas**: Acétela, entrá, mirá, entrá Lucio, le escribís por ahí así yo no salgo de acá.

**Gabriel Puertas**: Sí, vamos yendo, vamos.

**Gabriel Puertas**: Una cosa Lucio, te pasa la app, vos hacete una cuenta, después dejame el mail, yo te voy a agregar a este caso de uso, pero si vos te querés hacer otro caso de uso con otro set de datos que te haga sentido, nada, te lo haces, o sea yo te voy a dar, yo te voy a hacer que participes de este que había creado yo, pero vos hacete uno con los datos que quiera.

**Lucio Rojas**: Ahí está, para que se lo hagan todos. La idea es que se puedan registrar, apenas se registran van a tener el caso de uso este disponible cuando nosotros se lo compartamos, que ya lo hacemos, y después si tienen alguna duda para seguir usándolo, podemos seguir viendo las próximas reuniones que teníamos en la demo y ayudarlos en eso. Estaría buenísimo que tomen como el ownership de la herramienta, como dice Gabo, bañen mucho más rápido, entendiendo ustedes el problema y solucionándoselo.

**Gabriel Puertas**: Y la dinámica es esta, o sea ustedes conectan, o sea lo único que hace Téramo es, son dos cosas que para mí son súper importantes, hace muchas más para que eso pueda pasar, pero digo, es lograr vincular los datos de ustedes con una herramienta de estas, es un paso importante. Esa vinculación es hecha con todas las normas de seguridad, sin enviar datos más de lo necesario, estos modelos y ese tipo de cosas, y además persiste lo que ustedes generan, en este caso lo que persistimos fue la tabla de dotación, pero nada, ustedes pueden persistir información de lo que haga falta cuando yo digo persistencia. Es una tabla cuyos resultados van cambiando con el tiempo, y a ustedes les interesa que eso se mantenga. Eso sería. A ver, ¿Qué me está diciendo? Tengo todo lo necesario. Producción total 30. 1. Ah, mucho.

**Juan Peralta**: Treinta toneladas. Treinta mil toneladas.

**Gabriel Puertas**: Treinta mil toneladas versus veintinueve de mayo vendidas. A ver, aplanar el pico de dotación concentrado en el que 1 la dotación de marzo es 52 mayor que la de enero. Esa diferencia se explica casi exclusivamente por la dotación directa más turno de máquina por los fijos. Si parte de la producción de marzo se adelanta a enero, que tiene stock alto y baja actividad, la planta necesita menos gente. Recomendación.

**Juan Peralta**: Está buena la recomendación. Quizás lo que le falta al modelo es que el producto es estacional. Tienes en marcha el producto, es estacional y que la vida útil es corta, y los grandes clientes no te aceptan mercadería con más del 20% de la vida útil consumida. Eso te explica.

**Gabriel Puertas**: Eso habría que agregárselo.

**Juan Peralta**: Te lo agregás y tal cual.

**Gabriel Puertas**: Materiales con Celtr 110 riesgo de quiebre de stock. Varios SKU vendieron más de lo que produjeron durante todo el año. Un Celtru mayor a 100% es sostenible si el stock de apertura es alto. Este detectó que vendieron más de lo que se produjo en el año. Alta variabilidad en ventas. Algunos SKU con 40% no sé que. Este CV material, como el 7990 tiene CV 58%. ¿Puedo preguntar?

**Juan Peralta**: Pero el desvío de venta tiene que ser o alguna cosa de eso, o

**Gabriel Puertas**: sea,

**Juan Peralta**: tiene que ver con el forecast accuracy. Alta variabilidad en ventas,

**Gabriel Puertas**: Exceso de stock en ciertos materiales. Capital inmovilizado. El material 80. 522 mantiene un promedio de 142 días de cobertura, casi cinco meses, cuando el estándar de la industria 30. 45. Mira, eso indica sobreproducción o una caída en las ventas no reflejada en el plan.

**Juan Peralta**: Una caída de las ventas o un café en saquito. Tal cual.

**Gabriel Puertas**: Mirá,

**Juan Peralta**: ahí Boli. Esta interacción es buenísima. Con el conocimiento que tienen todos ustedes Cuando el Gabo lo va leyendo, si

**Juan Peralta**: te hace sentido o no. Tal cual.

**Juan Peralta**: Ya lo sé, o sea, pero lo agrupa de una forma, lo muestra de una forma y te permite hacer otro tipo de análisis que por ahí la rutina te lleva a decir, yo ya sé que esto pasa y lo tengo controlado, porque ya sé que cayeron las ventas por menor consumo. Entonces lo bueno es que está armado ahí y lleva un tiempo al principio, que es el de la configuración, el de la estabilización, el que tenga el conocimiento, pero después ya eso queda y evoluciona, entonces ahí el valor empieza a verse ahí cuando se usa.

**Gabriel Puertas**: Por ahí no es tanto

**Juan Peralta**: una solución así, o sea, no es una solución enlatada, esto es una solución viva. Y como antes decía, le preguntábamos, che, ¿Qué calculaste?

**Gabriel Puertas**: ¿Qué pasó?

**Juan Peralta**: ¿Por qué? Explícame, o eso mismo del CV y etcétera.

**Gabriel Puertas**: ¿Acá esta que dice? Está medio loca. En octubre instantáneo cae a 27 personas turno versus 52 en junio, mientras el sell true de los principales SKU de frasco sigue siendo más del 100%. Eso sugiere que el plan de producción de octubre subestima la demanda real de ese segmento. Hay capacidad disponible de frasco y la BPK en ese mes podría usarse para anticipar stock antes del pico de verano. Muy bien, bueno, acá hizo algunos gráficos para. Uy, este no se ve nada. Con la producción. Uno gráfico con la producción, las ventas y este es el stock.

**Juan Peralta**: Y ese que dice dotación total versus sell true.

**Gabriel Puertas**: Lo negro, esto acá que no se ve es. Yo no puedo cambiar, yo lo tengo en dark mode. Claro, acá tiene la dotación y este es el porcentaje de venta sobre stock, digamos. Ese es el porcentaje y lo va, o sea, el gráfico de esto te mostró cómo vos tenías la dotación respecto a cuánto vendiste de más. Y así pueden seguir, no sé, si quieren podemos apretar en alguno de estos y hace un análisis más en profundidad de eso o lo que usted quiera.

**Gabriel Salcedo**: ¿Qué tanto nos recomiendan, ir por Cloud o usar Gemini que ya tenemos en la empresa?

**Gabriel Puertas**: Sin duda iría por Cloud porque hoy es el que mejor funciona. Incluso hasta si yo trabajase, esto muy a título personal, si yo trabajase en cualquier otro lugar, yo me pagaría la cuenta mía porque cuesta menos que Netflix y la verdad que me aceleraría un montón, pero. Y por las dudas no pagaría el anual porque dentro de dos meses, no sé, ChatGPT saca un modelo y te crees ahí y pagaste el anual. Así que hoy, hoy para mí el mejor es Cloud.

**Gabriel Salcedo**: Bueno, empezamos a probar con Gemini porque ya la licencia de Cloud, dependería hablar con sistema, pero ahí estaba queriéndome crear la cuenta, pero cuando le doy a iniciar sesión para continuar me queda cargando y no sale de ahí.

**Lucio Rojas**: ¿Bien, y antes te apareció el login?

**Gabriel Puertas**: Todo correcto,

**Gabriel Salcedo**: apareció iniciar sesión para continuar y ahí ya queda ahí colgado.

**Lucio Rojas**: Bien, y si entras a TENAMOD. Com estás ahí y tocaste Start Building y ahí ese problema. ¿Bueno, nos lo llevamos para?

**Gabriel Puertas**: ¿Lucio, no te crees? Queda en contacto con Gaby, así lo.

**Lucio Rojas**: Sí, sí, yo tengo el mail y también tenemos que uso.

**Juan Peralta**: Y bueno, una cosa, ahora en adelante yo estoy saliendo de vacaciones, justo hoy es mi último día, así que por unas semanas no voy a estar yo en todo caso para no atrasar. Si te parece Gaby y César les dejo el último plan, ahora nos ponemos de acuerdo y vamos por ahí jugando con Bernard, que nos vayan dando los mismos números y si no vamos buscando.

**Cesar Bellini**: Exactamente cuando tengamos disponible la demo vamos a hacer esa prueba.

**Juan Peralta**: Así que bueno, las próximas semanas cualquier cosa lo siguen.

**Gabriel Puertas**: Bueno, espero que les haya gustado.

**Juan Peralta**: Sí, tenemos que jugar un rato, pero

**Juan Peralta**: le van a agarrar el gustito.

**Gabriel Puertas**: ¿Bueno Lucho, vos te quedás en contacto con Gaby para ver si se hace en la cuenta? Habría que ver si César tiene el mismo problema. Yo calculo que sí, para mí puede que tenga. No, puede que haya algo de alguna VPN o algún firewall, quizás el firewall

**Juan Peralta**: de la empresa, algo. Yo intenté desde otras sesiones y pude registrar.

**Gabriel Puertas**: No tomen que eso como diagnóstico, síganlo. Luce,

**Cesar Bellini**: tenemos que probar Gaby con LB Internet o con una red más directa salida, a ver si pasa lo mismo.

**Juan Peralta**: ¿Alguna invitado, alguna menos restrictiva? Probablemente haya algo.

**Cesar Bellini**: Dale, bueno, les avisamos. Bueno, muchas gracias,

**Juan Peralta**: buen fin y buenas vacaciones.

**Juan Peralta**: Gracias, igualmente.
