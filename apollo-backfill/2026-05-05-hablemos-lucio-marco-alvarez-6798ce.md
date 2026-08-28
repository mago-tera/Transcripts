# Hablemos !  Lucio  (Marco Alvarez)

**Fecha:** 2026-05-05T14:01:51.996+00:00  
**Duración:** ~43 min  
**Participantes:** Lucio Rojas <lucio@teramot.com>, Francisco Javier Bonalli <francisco.bonalli@sembraevolucion.com.ar>, Marco Alvarez <marcoalvarezit@gmail.com>  
**Externos:** francisco.bonalli@sembraevolucion.com.ar, marcoalvarezit@gmail.com  
**Apollo ID:** 69fa028c6c17e200196798ce

---

**Lucio Rojas**: Hola Fran, ¿Qué tal?

**Francisco Javier Bonalli**: Hola Lucía, ¿Cómo estás?

**Lucio Rojas**: ¿Todo bien? ¿Vos? Che, Fran.

**Francisco Javier Bonalli**: Bien, todo bien.

**Lucio Rojas**: ¿Está bien? ¿Anduvo la cámara? ¿Esperamos a alguien más?

**Marco Alvarez**: Dame un segundo que estoy confirmando que si viene Santi. No, empecemos.

**Lucio Rojas**: Un segundito. Estoy. Perfecto. Bueno, ¿Qué tal? ¿Tanto tiempo? Hace una semana que ya.

**Marco Alvarez**: Sí, pasa volando igual el tiempo te digo.

**Lucio Rojas**: Sí. Oh, me da, para mí pasó en cualquier momento. Estamos brindando Navidad. Sí, sí. Yo la verdad que siento que la última vez que nos encontramos fue hace muchísimos.

**Marco Alvarez**: No fue hace mucho. Creo que no pasó ni un. Habrá pasado un mes casi.

**Lucio Rojas**: Puede ser. No pasó un mes, pero siento que fue hace dos, tres meses, en otro rango temporal. Bueno, bien. Me compartieron los datos. Buenísimo. No sé si lo hizo alguno de ustedes. Me acuerdo que habías dicho que querías usar una fuente de datos media complicada para ver cómo funcionaba la herramienta. ¿Habías dicho eso?

**Francisco Javier Bonalli**: No me acuerdo.

**Lucio Rojas**: Puede ser. No sé quién dijo. Vamos a hacer algo difícil, a ver si sale. Espero que no lo haya hecho tan difícil. Así que lo cargamos directamente a Teramot y la idea es poder hacer una demo, una demo MCT en vivo, para que puedan ver la funcionalidad de la herramienta y después cómo se crea la conexión para ver las tablas en T desde Power BI. La idea es poder hacerlo en vivo desde cero, recorrer todo el pipeline y generar el ETL en esta hora que tenemos y después consumirlo desde Power BI. Ahora mi pregunta ¿Alguno de ustedes tiene ya disponible Cloud en la versión paga?

**Marco Alvarez**: No.

**Lucio Rojas**: Entonces vamos a hacerlo desde mi computadora y ustedes siguen el proceso y van guiando las preguntas que quieren hacerle. Acá estamos viendo. Quería hacer primero una aclaración que fue que esta semana migramos lo que es nuestra web app a una. Cambiamos toda la UI en vistas de mejoras. Así que esto es lo que yo había presentado con ustedes en la demo anterior. Y ahora vamos a trabajar sobre la nueva UI, que a efectos prácticos tiene las mismas implicancias, pero tienen mejores funcionalidades. Así que vamos a trabajar directamente sobre esta nueva versión. Dentro del Workspace creé el proyecto de Sembra Evolución y cargamos las tablas que habíamos pasado. Así que ahora les voy a agregar a este worksuit para que puedan trabajar. Si quieren me dedican sus mails, así los voy

**Francisco Javier Bonalli**: Francisco Donelli, Ahí tenés mi

**Lucio Rojas**: apellido, lo voy a copiar directamente desde la. Dale, desde la llamada. Una vez que ustedes entren y ya puedan manejarlos los datos, me bajo del workspace y los dejo. Hospitalidad tienen ustedes, Tienen que recibir una invitación al mail y ya van a poder entrar después de la demo a probar por ustedes mismos.

**Francisco Javier Bonalli**: Perfecto.

**Lucio Rojas**: Lo primero que hicimos fue cargar la fuente de datos que ustedes nos disponibilizaron y creamos las distintas tablas Silver. ¿Ustedes nos compartieron cuatro tablas, no? Creo que sí de pruebas de licencia, una tabla de origen de compra, una tabla de PPH y una tabla de ventas. Acá lo que podemos hacer es usar el editor de SQL para generar queries sobre la tabla y hacer alguna. Alguna consulta si quieren revisar qué fue lo que se cargó. Estamos viendo las tablas que cargaron. Esta es la de ventas, tiene distintos campos de ventas, de soja, de tecnología, quits y demás. Y una vez que tenemos estas tablas silver creadas, que lo que hace tela cuando generar el traspaso de silver de bronce, que era la tabla tal cual ustedes la pasaron a silver, es un proceso de normalización y estandarización de la data que ya habíamos hablado, donde tenemos que poder ver cuál es el código gener. Tengo problemas con la nueva ibex. Yo también estoy entendiendo la nueva. La nueva UX es nuevito, nuevito salió, Así que hizo la modificación. Por lo que estoy viendo, no generó ninguna modificación de un banco en particular en las primeras tres tablas y en la última, que es la tabla de ventas, hizo algunos CAS de distintos formatos de fechas y de días para dejar la tabla lista para el análisis. OK, eso me fui a fijar a la web anterior porque no lo encontré en esta. Voy a consultar y les digo dónde. Y ahora vamos un poco a lo que es la parte más interesante, si se quiere, y donde me interesa que me ayuden con las preguntas, porque yo no conozco muy bien el set de datos, no lo exploré, más que nada para poder hacer la demo, la situación más real. Lo primero que hicimos es crear un conector a thermo, como estuvimos hablando la última vez de su caso de uso en particular. Los datos para generar este conector se encuentran este simbolito donde proporciona una URL y un client ID. Se crean el conector en términos, suponiendo que creamos un nuevo. Se carga la URL, se carga la autenticación de cliente. Una vez con eso agregarlo, ya van a tener el conector a su caso de uso para trabajar las tablas de G. No lo creo de vuelta, porque ya tengo y no me va a dejar. ¿Así que una vez la interfaz que ustedes ya conocen, como cualquier elem, sería hacer pregunta? Y decirle que. ¿Me has dicho?

**Marco Alvarez**: Perdón Lucio. ¿Pregunta, se puede usar con Cloud y se puede usar también con Chachipití, no?

**Lucio Rojas**: Sí, se puede usar con los dos.

**Marco Alvarez**: OK, ahí nosotros ya tenemos licencia de Copilot. ¿Podrías analizar? Claro, analizar o ver con el equipo a ver si más adelante podría realizarse una conexión con Copilot justamente por tema de licencia. Porque analizando un poco lo que es el tema Presupuesto, Cloud y ChatGPT vale 20-30 dólares cada uno. Y nada, nosotros ya tenemos contratado Copilot, que es algo que ya está pago dentro de las licencias como para analizar.

**Lucio Rojas**: Hoy en día no está el conector desarrollado a Copilot, no entiendo bien por qué. Creo que la restricción del lado de ellos.

**Marco Alvarez**: Sí, puede ser, puede ser, me imagino.

**Lucio Rojas**: De todas formas no se pierde la funcionalidad de Téramo, ya que esto que vamos a ver que generamos y creamos desde Clock, se puede hacer internamente desde aplicación. Vamos a ver los dos caminos, pero se puede trabajar de igual manera. Igualmente me gustaría mostrarles cómo se trabaja desde Cloud, porque desvelo un poco la potencia que tiene la herramienta. Y bueno, dale, entramos la conexión. Hace una llamada a Téramo y te dice, bueno, encontré cuatro tablas Silver en lo que es tu herramienta. Una tabla que es de prueba de licencias. ¿Ustedes están viendo otra pantalla?

**Francisco Javier Bonalli**: Sí, nosotros estamos viendo resultados, se ve solamente Cloud.

**Lucio Rojas**: Claro, La pregunta fue la misma. Silver, tengo generar cada una y generar respuesta. Encontré cuatro tablas en la capa Silver. Tengo una Silver de prueba, donde hay una tabla de licencias por productor que contiene del productor junto con el estado agrupado de su licencia, la tecnología asociada y el tipo de licencia útil para analizar la distribución de licencias por tecnología y estado. Hay una tabla Silver de prueba de tablas de orígenes de compra. La tabla origen de compra por campaña registra de dónde proviene cada compra realizada por un productor. Bueno, estas son un poco las tablas que Armadu Test y lo que se puede empezar a hacer ahora es analítica sobre estas tablas. No sé qué tipo de información les gustaría generar o qué tipo de tabla podría generar, pero se la podemos empezar a pedir, interactuar con Claude para que las modele, enteramos. Así que si quieren me pueden guiar acá. Le puedo pedir a Claude que sugiera análisis que son útiles para el negocio.

**Francisco Javier Bonalli**: Dame un segundo, por favor. Ahí tengo que hacer una pregunta. Lucio, ¿Cómo es?

**Lucio Rojas**: Sí, tenemos que generar una nueva pregunta a Claude para.

**Francisco Javier Bonalli**: Bueno, perfecto.

**Lucio Rojas**: Empezar a ver qué hacer con estas tablas que le cargamos y dejamos lista para.

**Francisco Javier Bonalli**: Vamos con una fácil. ¿Le puedes preguntar cuántos quits tienen compra sin licencia?

**Lucio Rojas**: Bien, Ahora lo que hace es ejecutar una query sobre la tabla. No me dejó ver la poli que generó. Llama a la tabla, obtiene la respuesta y responde. Acá lo que ocurre es que hace una pregunta, una pregunta simple que no requiere de cruzar distintas tablas para generar una respuesta. Entonces iteramos, ¿Entienden eso? Y genera una query a una tabla en particular. Eso es una forma de usar Teramot. Y se le puede decir también que. On comprend licencia. ¿Está bien lo que estoy suponiendo? Ahora lo que le podemos hacer también es pedirle que genere una query en particular sobre una tabla silver. Y en base a eso genere un dashboard o haga un análisis comparativo de una situación. Por ejemplo, hay quits que compran con licencia y sin licencia. Entendí por contrapuesto. Y tratar de armar un gráfico y una explicación de por qué está sucediendo esto. Acá siempre estamos trabajando con una sola tabla y con queries a esa misma tabla. Estos datos supongo que le hacen más sentido a ustedes que a mí. Ahora los podemos revisar. Está yendo un gráfico que muestra la distribución de quits en dos universos distintos. Los que tienen licencia registrada, los que compraron sin licencia, válida, con licencia, tabla de licencias. 29 mil tienen licencia aprobada, 6 mil están en proceso, 760 fueron rechazadas.

**Francisco Javier Bonalli**: Y se puede. Le puedes escribir para que modifique, por ejemplo, ese mismo gráfico. Decir, no sé, poneme los valores

**Lucio Rojas**: dentro

**Francisco Javier Bonalli**: del gráfico,

**Lucio Rojas**: ¿Qué valores serían?

**Francisco Javier Bonalli**: No los valores de cada columna, esto sí, 100%.

**Lucio Rojas**: Por eso cuando ustedes me comentaban de armar todo lo que era el dashboard en Power BI, tiene sentido cuando uno quiere generar gráficos que se actualicen cuando se actualizan los datos y ya dejar algo que introduzco los gráficos y generar algo que uno mire todos los días. Pero si quiere hacer un gráfico sobre un dato en un momento puntual. La mejor forma es usar alguna herramienta de inteligencia artificial que genere gráficos en base a. Igualmente ahora me gustaría mostrarles a ustedes la potencia de la herramienta en sí, que es generar nuevos pipelines y estructuras de datos para hacer análisis que no están a la vista en las tablas silver propiamente dichas. Entonces me voy a decir en base tablas silver que tengo, que son las 4 que me pasaron análisis. Entonces empezamos a hacer algo más de descubrimiento de los datos y más data science, empezando a pedirle a la herramienta que cruce datos, entendiendo el negocio, entendiendo el contexto. Con las cuatro tablas que vos pasaste, podemos hacer una nueva tabla usando toda esa información que tenga algo un poco más valioso de utilizar. Por ejemplo, una tabla que pueda pronosticar el riesgo incumplimiento por productor, hacer una de la evolución de ventas por estado de licencia entre 2022 y 2026, hacer una tabla que analice el perfil de compra por origen y biotecnología, hacer una tabla de productores activos sin licencia por campaña, o una adopción de biotecnología para su cumplimiento. Si esto a ustedes les hace sentido, debería por la herramienta tendría que responder en base al negocio. Pero bueno, si hay alguna que les parece que es interesante generar, se la pedimos. Teram va a generar esa tabla, y ya no desde Clock, sino de TER,

**Francisco Javier Bonalli**: o sea, se va a formar una nueva tabla a partir de la que nosotros cargamos.

**Lucio Rojas**: Sí bien, bueno, no sé cuál les interesa generar.

**Francisco Javier Bonalli**: A ver, vamos a ver, vamos a probar alguna. No, está bien. Evolución de venta por estado de licencia,

**Lucio Rojas**: el 2 vamos a pedirle eso, y uno directamente se lo pide. Acá lo estamos pidiendo a TheAmot a través de CL, pero esto mismo ustedes lo pueden hacer sin tener clot. Ahora vamos a ver cómo para que se entienda que no es restrictivo. Les voy a mostrar mientras va trabajando, y después les muestro cómo hacerlo desde la propia herramienta, que si bien acá te muestra todas las cuellas que decía, si bien desde la misma herramienta de Téramo se puede hacer lo mismo, la experiencia es un poco menos amigable, si se quiere decir, ya que entendemos que Claudia es la mejor forma de consumirlo y lo que ponemos, pero no restrictivo. Acá está creando la tabla Gold Nosotros le decimos tabla Gold a las nuevas tablas de análisis que se hacen en base. Descargaron. Acá está creando la Gold Table, le da un nombre a esa nueva tabla y así una descripción. Esto lo está haciendo theramout en Sile. La descripción es que va a ser una tabla con una evolución anual de volúmenes de venta de soja agrupado por estado licencia. Permite analizar tendencias de cumplimiento y detectar si el volumen operado sin licencia crece o decrece en el tiempo. Genera la descripción funcional de la tabla. Y acá está haciendo la creación de la nueva gota. Mientras tanto les voy a ir mostrando cómo hacer esto mismo, visualizarlo, su paso. Estamos entregando vuelta. Este es su proyecto. Acá van a tener las tablas que cargaron. Esto es la tabla silver que ustedes fueron generando vuelta. Tienen un editor SQL para ver que tiene cada silver. Y acá a la derecha hay este simbolito que es un chat. Este chat internamente tiene una API de Antropic que lo que hace es que Claude esté dentro de la herramienta de Tailout. Entonces ustedes no tienen que pagar más licencias que la de theramot en sí. Y con eso pueden hacer el mismo flujo, la misma pregunta que hicimos allá, copiar y pegarla. Hago la misma pregunta. ¿Este chat se comporta de la misma manera que CL? La única diferencia que bueno, por ahí hace que la experiencia sea un poco menos amistosa, es que no genera gráficos o no genera artifacts, o que no se puede vincular con alguna otra información que ustedes tengan en su cloud.

**Francisco Javier Bonalli**: Me hace la tabla, me la bajo y hago el gráfico de manera manual, ponele.

**Lucio Rojas**: ¿Sí? Eso también puede hacerle bajarte como CCB o puedes conectarla a Power BI, que es un poco lo que vamos a ver ahora en la segunda parte, que esta tabla ya se puede dejar nomás disponible. Power BI se actualiza todos los días. Si acá hubiésemos elegido alguna de estas tablas y pedirle que la ejecute, haría exactamente el mismo proceso que hizo desde PRO. Entonces vamos a ver un poco cuál fue la tabla Gold que creó y cuál es el resultado de esa tabla. Dice, hace una descripción donde pide agrupar por estado de licencia y calcular la suma de ventas de soja para cada año y el total general. Incluir también la cantidad de quits distintos por estado de licencia. Y cada fila debe representar un estado de licencia con sus volúmenes anuales agregados. Y como tabla de origen usó la tabla de ventas. También hay otros casos, por ejemplo una BOL que creé yo anteriormente para probar, donde se puede usar más de una tabla de origen al mismo tiempo. Yo generé otro análisis donde analizamos la venta de soja por productor con licencia y el origen del canal, Donde pidió una fila por qui de productor con nombre de productor, venta de soja por año, estado de licencia, tipo de licencia, tecnología, biotecnología y origen de COM. Y después es una serie de descripción de requerimientos funcionales, le digo yo, que son las características que tiene que tener esa tabla, para después interpretarlo y generar la Q. Una fila por quit de productor. Acá te da la letra de neuralidad, después te dice que jone las cuatro tablas usando el quit como clave. Te pide tomar el nombre del productor desde la tabla PPH productor, si no existe, usa razón social de origen en compra como fallback para las ventas. Sumar los valios 2022-2023 2024-2025 es hoja por quit, tratando el null como 0. Eso es 1 problema que tiene la tabla que tenía muchos nulls. Con toda esa descripción genera la query SQL que podemos ver acá. Toda esta es la query que genera automáticamente la herramienta desde pedirle necesito una tabla que analice las ventas de soja por productor, genera toda la SQL. Yo la verdad mucho SQL no sé, no puedo ver qué tan compleja es, pero veo que los distintos cálculos, los gasteos y los join que hace son complejos. Es una query bastante extensa. Y con toda esta query que genera la herramienta, deja la nueva tabla ya en producción, genera una nueva tabla para hacer el análisis de esta dimensión de negocio que uno quiere corroborar. Y después en caso de tener licencia de cloud, le voy a decir así, las tablas web que tengo, Devolver las dos que creamos y le puedo decir, bueno, generamos un análisis con un dashboard. Y la otra opción, que es un poco la que. Vamos a pedirle sobre la que me piden ustedes.

**Francisco Javier Bonalli**: Ese informe, es en PDF, me habías dicho.

**Lucio Rojas**: Puede ser en PDF o puede ser un dashboard que se publica en versión web. Las dos, un gráfico. Y por qué. Demanda. Y es verdad, que certero. Las vamos a dejarlo trabajar mientras vemos el resto de flujo. OK, Bien. Bueno, entonces ustedes conectaron las cuatro silver, generamos estas dos tablas GO para analizar las ventas de soja por productor y las ventas de soja por año. Y una vez que tenemos estas tablas que se mantienen en producción están alojadas en un servicio de Amazon Web Service que se llama TINA, donde la pueden consumir, y todos los días en función que se actualice la base de datos, se actualizan las tablas LTL. En caso que ustedes actualicen los archivos y los archivos tengan las mismas columnas y sean las mismas tablas, se va a actualizar.

**Francisco Javier Bonalli**: Perdón, ¿Y esas tablas cómo se actualizan? ¿Eso que es? Marco lo saca de Salesforce.

**Lucio Rojas**: Bien, ustedes digan. Nosotros para probar archivos de Excel, en caso de querer actualizar esos archivos de Excel. Y son estos cuatro que cargaron, estos cinco. Estos cuatro se seleccionan y se carga la nueva versión y te hace el upload directamente. Esa actualización actualiza después las tablas que uno tiene generadas en el PT. Esa es una opción que es más manual y uno tiene que hacerlo todos los días o cada vez que quiere actualizar. La otra opción es hacer un conector directamente a Salesforce donde eligen las tablas y las columnas que quieren actualizar y todos los días a las 9 de la mañana por default corre el proceso de actualización y actualiza todo el pipeline de datos. Puede ser de cualquiera de las dos formas. Bien.

**Marco Alvarez**: Yo, perdón Lucio, los tengo que dejar, tengo justo una reunión ahora, después Fran me pasas a ver cuál es tu punto de vista y bueno, lo vamos debatiendo.

**Francisco Javier Bonalli**: Perfecto Marco.

**Marco Alvarez**: Gracias Lucio. Perdón.

**Francisco Javier Bonalli**: Gracias Marco.

**Lucio Rojas**: Gracias a vos, a ustedes.

**Francisco Javier Bonalli**: Tengo unos 10 minutos más Lucio, así que no quedamos.

**Lucio Rojas**: Dale. Espectacular generación del PDF. ¿Hizo todo el análisis? No, me lo puso en PDF. Perfect. Acá estoy usando Sonet 4.6, que es un modelo bueno, pero no el mejor. Si se usa Sonnet 6.4 te genera PowerPoints que son increíbles. Yo ya lo usé para la presentación. Está creando el HTML, digamos.

**Francisco Javier Bonalli**: Eso depende si contratan Cloud y qué versión los traten.

**Lucio Rojas**: No, Cloud se contrata independientemente y vos elegís el modelo y en base al modelo que elegís consume más rápido o más lento el token que tenés.

**Francisco Javier Bonalli**: Ah, bien, ahí entendí.

**Lucio Rojas**: Igualmente vos lo que podés hacer hoy, como está la herramienta, si querés tener toda la parte de gráficos quin es conectar estas tablas que generaste, que se llama Montenegro, actualizando cada vez que actualicé la fuente de origen de datos a Power BI, se genera una configuración de autenticación donde se le da acceso a las distintas tablas que uno quiere ver, por ejemplo, creamos esta nueva tabla de evolución de ventas de soja por estado de licencia. Se da acceso a la tabla y te brinda las distintas opciones de autenticación que vos necesitas. Generar un conector a Power BI. El conector a Power BI se canaliza por lo que es. Yo ya lo hice, pero quiero que veas un pantallazo por si en algún momento lo tenés que hacer. En particular con herramientas, nosotros te damos soporte para que entiendas cómo es. Se genera un conector que es ODBC, desde la máquina tenés que bajarte un driver que es directamente una descarga, y se genera un conector DNS. Donde en las opciones de autenticación se elige este y se completa. Todos estos campos son los que a disposición acá. Entonces tienes que hacer un copy paste de cada uno. Hasta completar todos y probar la conexión. Eso yo ya lo generé. Entonces después venimos a Power BI, creo que ya la tiene contratada, obtener datos, se dije ODBC, que es el driver que recién configuramos. Desde este driver se selecciona. Y se genera la conexión. Acá se genera la conexión a todas las tablas, va apareciendo, va cargando y una vez que carga te dice bueno, tenés estas tablas Silver, tenés estas tablas Gold, que son las que creamos recién, y genera una actualización diaria de estas tablas en Power BI para usarlas como Dash holográficos. Vos estás viendo, Sí, el Powerwide, el Power, pero no estás viendo lo que dice navegador. No, no, eso es porque compartí, la verdad que del Meet me vuelve loco. Bien, ahí está. Vas a ver todas las tablas que creamos, se seleccionan, te lleva un popup que es para autenticar, seleccionas esta tabla y ahí te dice bueno, voy a crear la versión preliminar. Te muestra la tabla que creamos y cuando le das a cargar automáticamente ya la ves en Power y se actualiza todos los días. Entonces la conexión es bastante sencilla. Vamos a esperar que la cargue, veas que es verdad. ¿Hasta acá qué te parece la herramienta? ¿Cómo la ves? ¿Está buena?

**Francisco Javier Bonalli**: Sí, tengo que evaluarlo, Lucio, en verdad lo estoy comparando todo el tiempo con clic, nosotros ya usamos mentalmente, pero bueno, lo tengo que parar un poco. Y charla un poco con Santi también. Está muy bueno. Yo para lo que Power BI no uso actualmente, tengo que empezar a usarlo, así que viene genial.

**Lucio Rojas**: Está pegando la. Está cargando la. Una pregunta, aprovecho que voy a cambiarle el DNS o el timeout que puse. Acá. Me dio un error porque configure 300 segundos de timeout y superó el timeout, el request. Entonces. Te hago una pregunta. Terminamos de ver el informe que creo y demás, cuando decís que lo compras con clic, a nosotros nos interesa tener ese feedback. ¿Hay algo que puedas hacer desde TeamOT que no estás haciendo clic o viceversa?

**Francisco Javier Bonalli**: Sí, a ver, la herramienta que vos me estás brindando. Por eso yo te preguntaba, yo puedo ir modificando los cuadros, vivo el momento. Eso es lo que más me interesó de la herramienta, por eso te pregunté de poner los datos de la barra y demás. Y lo que es clic es un desarrollo. Cada vez que es una modificación es un desarrollo. Es más estático. Es estático, por lo menos como nosotros lo usamos. Esto me interesa que sea. Que es dinámico y que yo el usuario lo puedo cambiar cuando quiero. Es cuestión de escribirla ahí.

**Lucio Rojas**: Y lo que es clic te permite a vos la generación de nuevas tablas, nuevos BTL.

**Francisco Javier Bonalli**: ¿No? En el momento. Con desarrollo.

**Lucio Rojas**: Es con desarrollo, claro. La gente sabe de clic.

**Francisco Javier Bonalli**: Sí, pero yo soy ingeniero.

**Lucio Rojas**: Bien, bien. Ellos directamente, bueno, lo hacen a la. Nosotros un poco lo que planteamos como hipótesis es, voy a compartirla, este tiempo que nosotros nos tomamos, que fue 40 minutos en ver qué tablas teníamos disponibles, pedir un nuevo análisis que nos genere esta query, que es una query realmente, no es una query trivial, la que genera bastantes líneas, toda esta Cuelli entendiendo las tablas, entendiendo el pedido. Después generar el análisis sobre esa query en tiempo real y volcarlo en un PDF que muestra la evolución de las ventas, la composición por volumen del año, la distribución de los quits y responder a la pregunta de por qué crees en las ventas sin licencia. Tomo 40 minutos. Y esto es algo que sin duda se puede hacer que esté resuelto, pero no a la velocidad de iteración que nosotros damos por 50 dólares. Ese es un poco el valor detrás de la herramienta. Y después que bueno, crea pipelines de infraestructura que se mantienen deployados en la nube y se actualizan con constantemente. Si querés yo te voy a compartir este informe para que lo leas.

**Francisco Javier Bonalli**: Compartímelo. Yo me tengo que ir a otra reunión y lo voy a charlar con Marco, él es el que decide todo el tema de las licencias y demás y el presupuesto está metido en eso. Pero espectacular, la verdad que es recontra útil.

**Lucio Rojas**: Bien, bueno, ¿Vos qué rol tenés?

**Francisco Javier Bonalli**: Yo soy el que prepara los informes, básicamente sería el usuario.

**Lucio Rojas**: ¿A vos te serviría?

**Francisco Javier Bonalli**: ¿Sí, tengo que charlar con él igual, viste? Pero muy interesante la verdad.

**Lucio Rojas**: Bueno, entonces te envío el informe para que lo veas si a vos te sirve y querés hacer otra prueba o mostrárselo a alguien más a disposición.

**Francisco Javier Bonalli**: Te iba a preguntar antes de irme, me dijiste que no ibas a dar acceso como a la demo para hacerlo nosotros. Ah, perfecto, listo.

**Lucio Rojas**: Sí, sí, yo envío un mail y lo tenés un tier gratuito donde te dejo probar sin problemas la herramienta de tela. Y bueno, después lo que es Cloud, eso ya lo gestionó Empresa, nosotros parece que somos revendedores de Cloud porque estamos haciendo todo el tiempo que lo compren, pero creemos que nuestra herramienta se aprovecha mucho más de esa forma. Yo que lo uso todos los días, la verdad que cambia la vida, creo

**Francisco Javier Bonalli**: que todo el mundo se está volcando

**Lucio Rojas**: por cloud y vale 20 dólares, así que bueno, nosotros siempre motivamos a eso. Y si no también ofrece la alternativa de uso que también es buena.

**Francisco Javier Bonalli**: Bueno Luis, la verdad que muchas gracias, súper claro, impecable y espero el reportecito. Bueno, después voy a charlar con Marco.

**Lucio Rojas**: Bien ahí en vivo. Ahora cuando me llegue el resumen de la. De la grabación que tiene acá el Team Recorder, mando un mail con el Summer y pongo el reporte ahí.

**Francisco Javier Bonalli**: Muchas gracias.
