# 45 min w/ Juan (Mariela Niell)

**Fecha:** 2026-10-07T14:01:46.558+00:00  
**Duracion:** ~44 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Sol Soletti <sol@teramot.com>, Mariela Niell <mariela.niell@drogueriacomarsa.com.ar>  
**Externos:** mariela.niell@drogueriacomarsa.com.ar  
**Apollo ID:** 6ac65b062e5ae300185579ba

---

**Mariela Niell**: ¿Esperamos a alguien más? Sol.

**Sol Soletti**: Sí, creo que se iba a unir Lucio, Ya te digo. Dale.

**Mariela Niell**: Lucio, ¿Cómo estás? Buenos días.

**Lucio Rojas**: Buenos días. Se me ve mal, Voy a prender un poco más de luz.

**Mariela Niell**: No pasa nada, te vemos. Yo no suelo a veces prender la cámara por lo que consume en las reuniones y demás, y por la conexión a veces no la prendo, así que no, no se sientan problemas por eso.

**Lucio Rojas**: Bien. No, yo iba a ir a la ofi, pero lo que está lloviendo.

**Mariela Niell**: No, está horrible. Si yo me hubiese preguntado antes que se la haga llover, porque me gustaría estar en mi casa.

**Lucio Rojas**: Nosotros tenemos los jefes de viaje, Cuando el gato no está, los ratones bailan, el dicho. Así que es más como. Bueno, manera. Dado ayer la charla con los NDA, estábamos, recapitulo un poco también, pedazo de. Que tenga un poco de contexto. Estábamos en la versión SAS con Comarza, y estábamos tratando de destrabar una cláusula del MDA. Y en esa conversación tuvimos, les comentamos sobre la posibilidad de usar Beacon en vez del SaaS, que no solamente ayudaría por ahí tomarlo distinto, sino también es más cómodo para ellos poder estar en su infraestructura. Mariela, Sol viene de reunión porque es un poco quien es responsable del lado técnico de Beacon, junto con otra parte del equipo, y queremos contarte primero por arriba de qué se trata, y después que vos puedas preguntar y también ver los detalles técnicos que tiene, porque ahí a tu infra es distinto a.

**Mariela Niell**: Sí, desde ya, cuando yo te dije eso ayer, tenía en cuenta que yo tenía que hacer cosas del lado de mi infra y tenía que tener cierto requerimiento. Así que tranquilo, escuchamos bien.

**Lucio Rojas**: Bueno, lo primero es que las funcionalidades que trabajamos tanto en el Beacon como en el SaaS, tratamos que sean las mismas. No vas a tener cambio en lo que es la funcionalidad. Incluso está yendo hacia Bitcoin, así que podemos decir que Bitcoin quizás es un poquito más performante en algunas cuestiones. Nosotros tenemos este producto hace poco, por eso no lo ofrecimos en su momento cuando empezamos las conversaciones con vos, y surge de este tipo de relaciones donde por políticas de las empresas, por cuestiones legales, de restricción de manejo de información,

**Mariela Niell**: no puedo hacer nada contra eso, porque yo dependo de ciertas aprobaciones, que por más que mi lado, lo que sea presupuestario, y todo puede estar dado y no tengo ningún tipo de restricción, lo que es política y legal, tengo que acatar lo que me piden.

**Lucio Rojas**: Y eso lo entendimos. Y bueno, también junto con otro tipo de objeciones, como yo ya tengo los datos en mi infraestructura, tecnológicamente no me hace tanto sentido volver a replicarlo en su infraestructura. Me gustaría mantenerlos en la misma. Desarrollamos esta solución. Esta solución es un protocolo que funciona distinto, no lleva los datos hacia nuestro infra, sino que se deploya sobre su infraestructura. Y ahora vamos a compartir unos documentos y ahí solamente les explica mejor lo que. Sí, María, te adelanto, cambia la forma de contratación. Esto no es un licenciamiento, sino que es el contrato anual de adquisición del software que se puede pagar en 12 veces.

**Mariela Niell**: Perfecto.

**Lucio Rojas**: Va a simular un licenciamiento con la condición de que si lo contratás es hasta fin de año o hasta 12 meses corrientes.

**Sol Soletti**: Bien.

**Mariela Niell**: Después también necesito, porque obviamente al cambiar de metodología hay un montón de cosas que cambian en cuanto a los requerimientos no tecnológicos ni especificaciones técnicas, sino en cuanto a las que tienen que ver con el servicio, o sea, disponibilidad, actualizaciones, esto de permanencia, etcétera, etcétera. De última, para evitar tener problemas, me gustaría tenerlo claro para así dejo la parte legal afuera, firmamos y seguimos adelante. Nada más que para eso. ¿Está claro?

**Lucio Rojas**: Sí, ahí hacemos. Ahora te damos lugar a que vos hagas todas las preguntas, podemos hacer incluso un recorrido, así que yo voy a proyectar el documento que armaste vos. Y te sentís cómoda con ese documento como para explicar por arriba y cualquier cosa anda pidiéndome que me vaya scrolleando. Te comento, Mariela, Sol de viaje, entonces está desde el. Tenemos que ir viendo desde acá, te atendimos en vacaciones, sos un cliente importante, hay que tenerlo en cuenta. Bien, ahí Sol, ya está y se ve. No sé si te escuchamos.

**Sol Soletti**: Sí, perfecto. Bueno, como comentaba Lucio, Beacon nace de justamente esto de problemática que nos venía atacando, de qué pasa con el dato del cliente, con esos clientes que no pueden sacar el dato de su infraestructura, no quieren hacer ese manejo. Y bueno, es una solución pensada justamente para que no haya ese manejo de datos fuera de warehouse o propio cliente. Entonces, en sí, Beacon está pensado para correr en su propia infraestructura. En cualquier duda que vos tengas, si manejan AWS manejan Azure.

**Lucio Rojas**: Ahí mamos en PEMIS, no estamos en una SQL Server, no me acuerdo bien yo el detalle.

**Mariela Niell**: Perdón, estaba muteada, estaba hablando sola, no me di cuenta hasta después dije. Me siguen preguntando. No, no, nosotros en este momento sí tenemos mysql y el server obviamente está acá, así que no tenemos problema, la infraestructura la manejamos nosotros y accedemos a todo tipo de generación de conexiones que sean necesarias realizar, o sea, en cuanto a la infra, 100 factible cualquier tipo de modificación.

**Sol Soletti**: Perfecto. Bueno, en general lo que pasa con Beacon es que todo corre dentro de tu propio procesamiento, dentro de tu. Entonces lo que vos necesitas levantar obviamente la conexión con Silver Server no va a ser ningún problema, probablemente no necesitamos ninguna especie de túnel entre Beacon, entre Teramon sería y tu base de datos, sino más bien el procesamiento. Vos lo que necesitas tener es Virtual Machine, dependiendo de la cantidad de usuarios de esa virtual machine, para escalar en cuanto a requerimientos de procesamiento, lo recomendable 4 GB de RAM y un disco que puede ser interno o dentro de la propia infraestructura para almacenar los resultados que vayan teniendo al usar. Pero que son estas tablas web que probablemente ya estuviste utilizando en el producto que tienen ustedes actualmente. Serían solamente.

**Mariela Niell**: ¿Tenés algún estimado de la capacidad de procesamiento de acuerdo a la cantidad de usuarios?

**Sol Soletti**: Sí, aproximadamente con 4 GB de RAM para la Virtual Machine tenés entre 10 y 100 usuarios de uso, simplemente. Después escala, obviamente si necesitas 1000 usuarios de uso simultáneo que estén haciendo preguntas constantemente o generando tablas, resultados demás, probablemente puede escalar hasta 16 GB de RAM, pero con 4 GB de RAM nosotros tenemos una versión símil SaaS de lo que es Beacon, que es para usos, pruebas o pruebas de concepto, que está corriendo actualmente con 8 GB de RAM y tenemos aproximadamente 100 usuarios simultáneos y no usa ni el 10% de acople de la RAM al mismo tiempo. Entonces con 4 GB de RAM de base para la Virtual machine y gasto calculamos en AWS y en Azure, aproximadamente son 45 dólares de gasto mensual. Esto es un estimado, obviamente depende de cuánto es el procedimiento, cuánta cantidad de usuarios, pero lo que nosotros gastamos es de base. Eso. ¿Bien, después alguna consulta? En general, en lo que es actualizaciones de producto, claramente como dentro de tu infra no tenés las actualizaciones on demand, sino que son actualizaciones por medio de Podman. La descarga, nosotros mandamos la actualización por medio de Podman y eso se actualiza de acuerdo a si ustedes lo quieren actualizar en el momento, es un botón que le dan update, si no mantienen la versión que ustedes quieran mantener. Pero en general esa es la metodología en cuanto a datos, simplemente los datos van a quedar dentro de tu TENAN, dentro de tu propio premise. Nosotros no tocamos nada de datos, todo se maneja dentro de tu propia infraestructura. Lo único que saldría de tu red, si ustedes tienen un LLM de un proveedor digamos, antropíco, PN, el que sea, la llamada al LLM es lo único que sale de tu red básicamente. Pero también puede correr con DLM propio dentro de tu. Así que si tienen la capacidad de correr un LLM on premise, ya absolutamente tenés el encapsulamiento total de todo tu dato y de todo lo que vos quieras tener.

**Lucio Rojas**: Ellos estaban con plot hasta ahora.

**Sol Soletti**: Bueno, tanto Teramot como Teramot Beacon funcionan con API keys justamente porque tenés que hacer distintas llamadas externas para hacer la transformación de datos, las consultas y demás. Entonces el modelo que nosotros ofrecemos es o bring your own key, o sea tenés tu propia key, controlas tus propios gastos o compras la cuota vuestra de Bueno, quiero gastar 50 dólares de APK por mes, bueno, nosotros te ofrecemos la API y tenés que estar ese tope marcial. Pero en general son esos, como el funcionamiento es el mismo que el theramo convencional, el Theramot versión SaaS, solamente con premise tenés el gasto propio tuyo de infraestructura y el tema del API key del LLM, si lo querés gestionar ustedes con su propio LLM corriendo on premise o con un API key suya o nuestra. Y después bueno, los datos y las queda siempre en tu premise y la única salida sería fuera de la red para las llamadas del LL.

**Lucio Rojas**: Bueno, esto ya creo que es más funcional lo que está acá abajo. Sí trabaja que esto ya Marila vos.

**Mariela Niell**: Sí, sí, sí, esto ya no lo necesito. Esa parte, los requerimientos pasámelas después para que yo.

**Sol Soletti**: Esa es la parte que cambiaría Bitcoin de tela mosas convencional, que es justamente la infraestructura, obviamente un tena acotado. La infraestructura la manejan ustedes, nosotros lo que hacemos es ir, hacer toda la conexión con ustedes obviamente para dejar todo seteado y ver que todo funcione, que es parte del soporte natural de la instalación del servicio. Pero después generalmente ustedes manejan toda la infraestructura para que ustedes tengan obviamente el control total de su.

**Lucio Rojas**: Bueno, es todo. Vamos a ir sobre la demo del producto. Hasta acá solo. ¿Hay algo más que tenemos que ver de este documento o ya está todo?

**Sol Soletti**: No, en general, bueno, lo mismo que con tramo convencional, vos cuando generas una tabla resultado, eso se guarda en el tenat del SAS. En este caso necesitamos una partición de disco donde almacenando esas tablas resultados, por tanto sería la virtual machine que te mencionaba antes, con el procesamiento de acuerdo al escalamiento de usuarios que vos quieras tener. Y después el disco para ir almacenando, una partición de almacenamiento para ir almacenando todos los resultados que va a escalar de acuerdo a cuánta cantidad de data y tablas generemos. Exactamente.

**Lucio Rojas**: Le dejamos de decir ahora se llaman tablas de resultados en Bitcoin porque es más amigable para el usuario, no tan técnico. Mariela, ¿Hasta acá tenés alguna consulta o pasamos a algo más?

**Mariela Niell**: La verdad que hasta acá no tengo ninguna consulta. Lo que entiendo es que el contrato mínimo es por un año, después vos me dirás cuáles son los costos y cómo cambian los costos. Las actualizaciones ya me quedaron claras.

**Lucio Rojas**: Vemos si querés un poco la interfaz, cómo funciona y después vamos con el contrato. La interfaz cambia levemente, tratamos que sea lo más parecido posible al SaaS y estamos en ese camino. Quiero que acá entendamos que al ser un producto nuevo y tan novedoso, la iteración es bastante rápida y quizás de la interfaz vamos a ir mejorando algunas cosas. Así que de ese lado podés estar tranquila que va a seguir mejorando. Incluso lo que ya ves, algunas de las funcionalidades más fuertes que tenemos es que podemos desployar HTML. Por ejemplo, yo este lo hice acá recién tengo conectadas mis fuentes. Acá me perdí. ¿Donde están ahora fuentes?

**Sol Soletti**: Si, tenés que ir abajo al perfil, a vista detallada, porque bueno, justamente la UI de Beacon es bastante más distinta que la UI del SaaS convencional, porque está pensada para dos tipos de el usuario que quiere ir preguntar, entender de negocio, y el usuario que es más experto, sabe exactamente de la programación de todo lo que está sucediendo detrás de los datos. Entonces, en la vista detallada vos tenés toda esa información justamente que es un poco más abrumante en un primer vistazo, pero si tenés todo lo que es más técnico, sería las alertas, la actividad que está pasando con el nodo, que justamente es el nodo de procesamiento de todo lo que ahí tenés también los privilegios, los roles, las restricciones, todo un poco más técnico. Pero bueno, en esta parte es como la vista completa, la vista de tallares.

**Lucio Rojas**: Acá nosotros tenemos unas tablas que conectamos internamente, observabilidad, lo podemos mostrar porque son datos nuestros, así que no tenemos problemas, Vamos a tener todas las fuentes conectadas. Acá ustedes conectarían su MySQL va a levantarlo igual que como lo levanta Tegamot ahora, no haría falta el túnel porque estaría dentro de su estructura. En una segunda vista puedes ver las tablas de resultados que vamos creando, también podemos ver el estado, la cantidad de filas, la versión. Trabajamos con versionados de tablas gold para poder ir volviendo, yendo y viniendo las versiones. Y también se pueden compartir a distintos usuarios como veíamos antes. ¿Estas tablas están compartidas a toda la organización o yo podría elegir algunos usuarios en particular?

**Mariela Niell**: Lucy, vamos. ¿Recordás que nosotros te pedimos un cambio en cuanto a los perfiles? ¿Eso lo mantendríamos en esta versión?

**Lucio Rojas**: Bien, ese cambio era que el analista no pueda.

**Mariela Niell**: La realidad era que lo que pasaba era que si era miembro, no me acuerdo cómo se llamaban los perfiles ahora, pero había un perfil que podía manejar un montón de cosas, pero veía todo lo que era configuración y yo no quería, pero tampoco podía agregar archivos externos. Claro, fuentes de datos. Y yo trabajo con mi base de datos y a veces tengo que interactuar con datos externos, entonces yo lo que quería era que no me pudiera tocar. Claro, no me pudiera tocar la configuración, pero si pudiera agregar datos.

**Lucio Rojas**: Claro, es esto de acá exactamente.

**Mariela Niell**: ¿Eso lo podríamos mantener?

**Lucio Rojas**: Supongo que sí, Sol, No,

**Sol Soletti**: ahora mismo podés ver en la pantalla de Beacon está el mismo esquema de permisos justamente y distribuidos de una forma similar. Pero bueno, eso se puede ir charlando, no hay problema. Como dijo Andrucio antes, hay mucha iteración rápida porque es un producto que ya está más curado de aprender del producto anterior, del producto saca, entonces se puede iterar más rápidamente. Si vas a roles y permisos Lucio, ahí abajo de organización, en el site panel miembros, roles y permisos, Ahí tenés un poco.

**Lucio Rojas**: Vamos a salir, Mariela. Yo estoy como. Cuando ustedes me están. Cuando yo estaba explicando a ustedes cómo movernos por la interfaz, estamos más o menos en el mismo nivel console, porque te están armando y estamos ahí.

**Mariela Niell**: No hay problema, chicos. Yo por ahí, porque como ya hicimos un pequeño caminito con la otra versión, poder emparejar esta nada más, no es que fuera otra cosa, es un poco

**Sol Soletti**: nuevo para todos, pero bueno, hay errores y permisos. Pueden ver qué puede hacer cada una.

**Mariela Niell**: Perfecto, fantástico.

**Sol Soletti**: Pero bueno, general, usted lo que querrían sería un analista que no toque configuración, pero que sí pueda hacer todo el maneje de datos.

**Mariela Niell**: Exactamente, eso es lo que yo hablaba, porque bueno, obviamente que no quiero que ese analista me toque la configuración, pero sí que pueda agregar un dato externo. Estamos hablando de algo simple, chicos. Por ahí no sé si vamos a ir, no sé, la publicación de los índices de precios mayoristas del INDEC. Lo necesito muchas veces, que pueda agregar ese dato para que pueda trabajar.

**Sol Soletti**: Claro, sí, sí, sí. En Beacon existe un poco más de esa separación. Tenés el lector, que igual que en Telamo convencional, solamente podés ver o interactuar un poco con la información. Después el analista sí puede hacer esto que vos me decís, interactuar con la información, conectar fuentes externas, pero no puede eliminar ni tocar configuración más dura a niveles más bajos, digamos. Y después si tenés el administrador, que como ves tiene 22 permisos, a diferencia de 12 permisos que tiene el analista, que sí es un poco más esa configuración que vos me decías que no querías que tenga la analista. Entonces esa división está un poco más lograda, podemos decirlo, que es la que vos esperabas que tenga, pero también se puede, como te digo, ir adaptando al requerimiento que vos tengas.

**Mariela Niell**: Perfecto, gracias, Sol.

**Lucio Rojas**: Colecciones. Acá Sol. Para compartir las distintas tablas de resultados a distintos usuarios resultados,

**Sol Soletti**: lo que tenés que hacer es crear una colección. Una colección. No sé si tiene un poco de terminología de lo que es el uso de Amazon. En Amazon vos generas roles y perm. Tenemos, seguimos esa misma filosofía de que vos necesitas otorgarle a los usuarios los mínimos privilegios posibles. No tenés que otorgarle privilegios por las dudas, sino lo mínimo que ese usuario necesita para poder coexistir con ese. Entonces, en mi combo lo que haces es generar una colección. Una colección puede ser un conjunto de tablas que ciertos usuarios tengan permitido ver. Vos podés tener una organización centralizada donde están todos tus datos, y aún así que todos los usuarios que vivan en esa organización no vean todos tus datos. Entonces vos generás colecciones. Tenés una colección que es de economía, entonces solamente le das privilegios de tablas de economía a los usuarios que sabes que solo tienen que ver esas tablas. Y así vas a ir jugando con los sectores.

**Lucio Rojas**: Vamos a hacer una en vivo, vamos a elegir las personas y las tablas. Vamos a algunas tablas. Ahí puedo ver algunas columnas.

**Sol Soletti**: Sí, podés restringir por tablas.

**Mariela Niell**: Podés restringir columnas,

**Lucio Rojas**: Algunas columnas.

**Sol Soletti**: La restricción de columnas es a nivel del nodo de procesamiento. Entonces se da por ejemplo, personas funciona igual que con AWC. Entonces antes de ejecutar cualquier cosa, el nodo mira cuáles son los permisos que tiene esa persona. Si tiene una columna restringida, por más de que pregunte, repregunte y vuelva a repreguntar, nunca le va a mostrar la columna. Es más, probablemente si intenta buscar la vuelta, le va a dar el

**Mariela Niell**: muy agradecida.

**Lucio Rojas**: Solamente acá es con el mail directamente, ¿No, Lucio?

**Sol Soletti**: Sí, con el mail de la persona.

**Lucio Rojas**: Igual acá me voy a.

**Sol Soletti**: Esta parte está medio como que no está muy explorada, pero bueno, falta feedback. Ahora Lucy veo que está renegando un poco para que la colección. Ya sé que tengo que mejorar.

**Lucio Rojas**: No, pero igual está entendible. Está débil nomás. Está un poco débil. Hay que hacerlo un poco más user friendly.

**Sol Soletti**: Pero bueno, en general, si tenés esos niveles de roles y permisos, puedes crear colecciones para ver a quién le das tabla, a quién no. También podés generar organizaciones. Cuando las organizaciones vos podés dividir, es algo que es como una práctica común, como lo de los projects y los workspaces en términos convencional, podés generar distintas organizaciones donde cada organización tenga la fuente pertinente que querés que vean los miembros de esa organización. Y también jugar con eso.

**Lucio Rojas**: Acá en modelo podemos cambiar la API de un LLM que esté usando el chat, que ahora vamos a repasar cómo funciona. Desde acá ustedes podrían encontrar su propio API key para elegir el modelo. Acá me corregí, Sol, pero creo que estoy diciendo lo correcto.

**Sol Soletti**: Sí tenés. Bueno, básicamente soporta toda la gama de modelos que ustedes quieran, si quieren OpenAI, Afropic, Kimi, GLM, cualquiera con API Key o con el modelo proveedor que nosotros damos. Nosotros los benchmarks y el refinamiento de la aplicación lo hicimos con GPT-6 Luna, porque encontramos que es el balance entre costo calidad. Los benchmarks nos dan aproximadamente 98% de acierto con un benchmark de datos sucios, datos grandes, un ERP, y en general El costo por tabla resultado es de 0,0033 dólares, para que te des una idea de los.

**Lucio Rojas**: Después otra cosa importante es que podemos hacer alertas. Esto es como si fuese un nodo de n, donde vas a elegir la tabla, vas a elegir algunos criterios, y podés decir, por ejemplo, cuando el promedio de las personas que lo adopten se mueva más de más, eligiendo los parámetros. Esto desde MCP creo que funciona un poco mejor, ¿No?

**Sol Soletti**: Sí, PCOM tiene su interfaz gráfica, obviamente, porque es más amigable con el usuario, pero está pensado que estas funcionalidades que son más de desarrollo, se hagan desde el MCP, porque es una cuestión más fácil de llevar, configurar envíos de mails

**Lucio Rojas**: y demás en base a ciertas reglas. Esto puede servir mucho para todo lo que es la automatización de la reposición de stock, por ejemplo, en su caso.

**Mariela Niell**: Sí, eso es muy bueno.

**Lucio Rojas**: Y después genera artifacts, que vamos a ver cómo los generé.

**Sol Soletti**: Sí, bueno, los artifacts, quiero hacer una distinción acá, porque tenemos los dos motores. Tenemos un motor de dashboards internos, que funciona de la misma forma que funciona Power BI, por ejemplo. Y tenemos el motor de Art. El artifact es algo que nace de Antropic, de Cloud, que genera un artifact o un HTML por detrás. Pero nosotros adoptamos esa noción de artifact que puede generar tanto Cloud como Luna, que luna es de OpenAI, no tiene ni idea de lo que es un artifact, pero pudimos adaptar ese uso de los artifact a que ahora desde el agente interno de la IOI lo pueda generar también un modelo como Luna, o si le quieres poner KIMI, o le quieras un RM o. Entonces tenemos esas dos distinciones, porque uno es un motor interno gráfico, que es el de los dashboards, y otro es un motor generativo del LLM. El LLM te va a generar el artifact, que a fin de cuentas es un dashboard solamente, que es generado por el mismo LLM.

**Lucio Rojas**: Acá a diferencia, quizás para mí la primera diferencia es que el chat interno funciona súper, súper bien y eso es una ventaja grande que van a encontrar. Yo acá le pregunté, si este es un caso de uso interno, si me podía crear un HTML de uso de Beacon con el Observatory. Beacon sería nuestra plataforma, que la corremos sobre nuestra propia plataforma y Observatory es como le decimos a la base de datos de resguardo de acciones. Acá fue usando las distintas tools, como antes, fue a ver las sources, fue a hacer.

**Mariela Niell**: Te hago una pregunta, perdón, pero justo se me acaba de ocurrir por algo que dijiste. Al guardar nosotros y al tener el servidor local, o sea yo me voy a tener que asegurar un backup de esos datos. ¿Puedo backupearlos? ¿Tengo acceso? ¿Backupearlos?

**Lucio Rojas**: Creo que un requisito.

**Sol Soletti**: Sí, sí, sí vive dentro de tu disco, así que es la idea.

**Mariela Niell**: Está bien, pero bueno, si no llego, no tengo una conexión, no llego a donde están los datos, no puedo capearlo, por eso pregunto. A veces está tan cerrado que te dice no, mira, no podés acceder a los datos.

**Sol Soletti**: Hay cosas que se hace. Una re buena pregunta, porque nosotros cuando nos encontramos con este problema de los datos dijimos Bueno, ¿Qué hacemos? ¿Hacemos otra plataforma? ¿Hacemos Otro programa? No hacemos como dijo Luis al inicio, un protocolo. Entonces el protocolo es lo suficientemente agnóstico a todas las opciones, ya sea cloud, no habla ningún cloud, no habla ningún lenguaje, no sabe absolutamente nada de cosas de la industria actual, solamente habla su lenguaje, que es el lenguaje del protocolo. Entonces vos le podés enchufar cualquier disco, cualquier almacenamiento, cualquier cloud, que va a funcionar de la misma manera. Si rompió el disco que contenía todos tus datos, no hay problema, tenés de vaca. Pero otro disco lo enchufas tranquilamente y va a seguir funcionando con la idea del protocolo. Justamente es agnóstico a todo lo que le pase alrededor.

**Mariela Niell**: Bien, y las tablas Gold, ¿En qué formato se guardan?

**Sol Soletti**: Se guardan en parquet, porque bueno, es el formato que mantiene toda la metadata que se.

**Mariela Niell**: Perfecto, bien, fantástico. Listo. Perdón, Lucio, Seguí.

**Lucio Rojas**: No, Bien, acá quiero que veamos una cosa. No sé si Sol. Si, tenemos el detalle que hace cada tool, eso a veces es difícil seguirlo, pero miremos el tiempo. ¿Cuánto tarda en listar las sources? ¿Dos milisegundos? ¿Cuánto TARDA en describir capacidades? Que no sé que sea esa tool, pero 3 milisegundos. En hacer un overview del esquema, 23 milisegundos en hacer una autorización de Artefact, 2 milisegundos en Hacer una búsqueda dentro del esquema, 2.8 segundos, hacer una descripción del esquema, 23 milígundos. Esa es la velocidad con la cual se va moviendo esta solución. Después de menos de un minuto, bastante menos de un minuto, me dice listo, ya. Encontré en el Observatory una serie diaria de uso de Beacon con 45 fechas, del 3 de agosto al 6 de octubre. Preguntas, herramientas, personas activas, errores, duración, tokens, ni costo. No incluye preguntas ni identificadores personales. Algunos días tiene el costo sin informar, y en los primeros días varias métricas de los modelos. Eso construyendo la base a partir del uso. Y me hizo el gráfico de uso y me dieron también la tabla que me respalda el gráfico. Y yo le dije bueno, ahora deployámelo como HTML. Y acá tardó. ¿Cuánto tardó? Hizo cuatro llamadas, gastó 97 mil tokens, no me está dando el tiempo, creo que son estos 807s. Y usó todas las tools para crearme el artefact. Tardó 24 milisegundos, acá está. Crearon el artefacto y me lo dejó de proyecto.

**Sol Soletti**: Quiero acotar, en general, el tiempo de espera de Beacon se intentó de mejorar lo máximo posible hasta que nos chocamos con la pared del tiempo de espera de llamadas del LL. Eso es lo que consume el 95% del tiempo. En mayo escribí un artículo acerca de esto de Mozapli de Clarvicon, que me chicó, contra la pared de bajar el tiempo de espera de llamadas del LL. Se sigue intentando mejorar, pero bueno, esos 800 segundos igual también tienen en consideración que Picon nunca te va a crear cosas si vos no se las optás explícitamente. Nunca te va a borrar una tabla, nunca te va a borrar un artifact, te lo va a crear desde la gente sin que vos le dejes. Probablemente Lucio lo dejó corriendo, se colgó y después le dio a aceptar y se dio la cuenta de cuánto tiempo.

**Lucio Rojas**: Sí, sí, hice exactamente eso.

**Sol Soletti**: Pero bueno, en general, cuando vean si lo van a probar desde la gente, desde el SAS, los tiempos de espera son el 95% del LLM haciendo llamadas. Eso también depende mucho del modelo. Luna es un modelo bastante rápido, antes hicimos las pruebas con Sonep, que era bastante más lento, pero bueno, es ir viendo qué es lo que nosotros queremos, calidad, rapidez y.

**Lucio Rojas**: Consultas por día. Kumen tiene pocos usuarios todavía porque estamos empezando a llevarlo al mercado. ¿Cuántos errores diarios tuvimos? Creo que un día que no sé qué pasó, se ve que usó alguien que le pegó un error muchas veces. La cantidad de personas activas que tenemos por día, el costo que nosotros hemos asociado por día. Todo esto me hizo un segundo y vean qué lindo se ve y se puede compartir con el link, igual que los Artifact que vimos antes en la otra lección. Así que no sé, creo que la próxima barrera de velocidad sol cuando bajemos los va a ser la velocidad de la luz más rápido. Así que no sé Mariela, si tenés más.

**Mariela Niell**: No me quedaron dudas respecto de esto. Lo único que necesito para seguir avanzando es que me pases las especificaciones que me mostraste para que las tenga y pueda ver si hay algo que se me escapó en cuanto a requerimiento y demás. Así hacemos, tenemos de alguna manera la mejor performance. Y lo otro que me queda Lucio, es que me pases los costos en relación a esto.

**Lucio Rojas**: Después te voy a pasar la propuesta. Esto más allá de la propuesta, no es como el SAS que era propuesta y licencia, sino que es propuesta y contrato. Vamos a tener que firmar un contrato perfecto que lo vamos a perfeccionar un poco con Leales y después los vamos a compartir.

**Mariela Niell**: Bueno chicos, recuerden lo siguiente. Lo único a mí me hubiese encantado poder dejar esto ya medio cerrado antes de irme de vacaciones. Me voy de vacaciones viernes, pero por una semana nada más, no es nada. Pero por las dudas les aclaro porque no es que voy a dejar el tema colgado, pero bueno, si no llegamos a verlo lo tendremos que terminar de

**Lucio Rojas**: cerrar a la bolsa, no hay problema. Se me está desconfigurando absolutamente todo el PDF. ¿Ustedes lo ven bien? Yo lo veo medio raro.

**Mariela Niell**: Sí, yo lo veo.

**Lucio Rojas**: Lo veo súper raro. Esperen que lo voy a guardar en drive. Entonces seré yo el problema. Acá tenemos un poco de. De contexto, de contextualización del por qué pasamos del SAS al icon. Ahí con la compu se me estaría trabando. Denme un segundo que voy a dejar de compartir porque estoy pudiendo verlo yo. No sé qué le está pasando al visualizador de. Ahí está ahí medianamente se ve, Lo

**Mariela Niell**: veo, no tengo problema.

**Lucio Rojas**: Bueno, entonces, más mi toque. Esto es un poco lo que te veníamos contando, Mariela, así que.

**Mariela Niell**: Sí, sí, es lo mismo que estuvimos hablando.

**Lucio Rojas**: Voy a bajar directamente la propuesta. No me está dejando llegar la computadora. Dame un segundo que lo voy a subir a Drive y lo voy a ver desde ahí. Quiero hacer una consulta que me acaba de surgir. El tema del modelo de IA. Nosotros normalmente trabajamos con Cloud, usamos Sonet normalmente, no sé si podemos elegir nosotros o mismo Theramo elige qué modelo utilizar. Hay una diferencia, una diferencia principal. El chat que ustedes tienen en Beacon, eso va con API Key por detrás, y ahí pueden configurar las nuestras, pueden ser suyas. Eso es una cosa. Como ustedes lo vienen consumiendo hasta ahora, es por MCP. Y esto también se puede consumir por MCP desde Cloud, desde Cloud Code, desde Terminal, donde sea. Yo uso desde Cloud Code, por ejemplo, para trabajar con datos de implementaciones. Y ahí usan el modelo que ustedes quieren, porque es la licencia de 20 dólares que le pagan a Cloud y lo conectan por MCP, exactamente igual que el otro. No sé si querías agregar algo. Voy a presentarlo como medianamente. Como podamos hacerlo acá, Mariela. Lo que tenemos es una licencia de 12 meses que tiene un valor total de 30 mil dólares, que se puede tomar en 12 cuotas mensuales de 2.500, lo cual sería un licenciamiento similar al que ustedes tenían sobre el SAS. Esto tiene un. Sería una diferencia de 500 dólares mensuales, incluye hasta 20 usuarios, y cualquier usuario adicional que podamos llegar a agregar tiene un valor extra de 90 dólares. Si es un miembro que administra, un propietario, o si es un usuario de solamente vista Read Only, tiene un valor de 7 dólares mensuales y se hace después el pago mensual, que ahí ya sí sería símil a una licencia con la obligación de ser los 12 meses.

**Mariela Niell**: Ningún problema. En cuanto a la propuesta, te lo digo ahora, eso sí, no necesito nadie. Respecto de la propuesta, está perfecto. Obviamente, más allá de todo, el contrato de conf. Igual lo tenemos que firmar porque una cuestión política de la empresa, modificaremos lo que haya que modificar, porque obviamente que el contrato cambió porque es otro el servicio. Pasame vos. Supongo yo que además debes tener un contrato de servicio, porque cambia la propuesta.

**Lucio Rojas**: Sí, es un contrato de servicio de licencia de software. Lo vamos a enviar si querés a la vuelta de tus vacaciones para que nosotros también podamos trabajar un poquito de firmar todo. Y la contratación incluye cuatro sesiones de una hora y media con el equipo técnico y funcional para poder terminar de hacer toda la configuración, poder recorrer los features, hacerles un traspaso del knowledge a ustedes y también acompañarlos en algunas mejores gráficas de implementación a la hora de ir al práctico. Suelen servir bastante bien.

**Mariela Niell**: Perfecto, Lucio Sola, estoy de acuerdo con todo, les agradezco que sea mi vuelta. Si tengo algo menos que hacer ahora que ya no sé cómo sacar tiempo para hacer todo lo que tengo que hacer, así que agradezco que sea la vuelta, así que no hay ningún problema. Bueno, entonces espero tu propuesta. Yo vuelvo el día, no me voy muchos días, me voy el 9 y vuelvo el martes 20. Ya estoy operativo entre feriado y demás son 6 días hábiles, así que no es mucho, pero los necesito. Así que bueno, espero tu propuesta y avanzamos en función de eso, ¿Te parece?

**Lucio Rojas**: Dale, Mariela, muchas gracias.

**Mariela Niell**: Lo que es económico no hay ningún problema.

**Lucio Rojas**: Bien, entonces sigo por medio.

**Mariela Niell**: Sol, pásame ese documento para que yo vaya teniendo el equipo preparado.

**Lucio Rojas**: Sí, sí, ahora paso todo por mail, yo hago media hora, una minuta y pasamos todo y el contrato sigue reñido.

**Mariela Niell**: Bueno, muchas gracias. Gracias por el tiempo, gracias por el cambio de la propuesta y todo lo demás. Solo un gusto, nos estamos viendo.
