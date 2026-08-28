# Hablemos !  Lucio  (jorge monti)

**Fecha:** 2026-05-06T18:00:40.967+00:00  
**Duración:** ~55 min  
**Participantes:** Victoria Reybet <>, Lucio Rojas <lucio@teramot.com>, Julieta Alvarez <>, jorge monti <jorgmonti@gmail.com>  
**Externos:** jorgmonti@gmail.com  
**Apollo ID:** 69fb8ed59d413f00215db564

---

**Lucio Rojas**: No sé. Hola, hola. Hola. ¿No te escucho o no escuchas? Hola, Hola, ¿Cómo va? ¿Todo bien?

**Victoria Reybet**: Perdón, tenía silenciado y desde la compu

**Julieta Alvarez**: no lo puede desactivar.

**Victoria Reybet**: Ahí supongo que los chicos se deben estar por conectar.

**Lucio Rojas**: Dale, sí, buenísimo. Yo estoy tratando de prender la cámara, pero no me está tomando el sistema, así que la voy así hasta que decida tomarla. Así que esperamos a los chicos y sí les avisé. Bueno, yo capaz que aproveche para reiniciar rápido la compu mientras se suben los chicos, así puedo tener la cámara que.

**Victoria Reybet**: Me vuelvo a conectar.

**Julieta Alvarez**: Allez.

**Victoria Reybet**: Ciao. Ciao.

**Lucio Rojas**: Todo bien.

**Victoria Reybet**: Buenas.

**Lucio Rojas**: Ahí nos escuchamos entre todos. Tenía un problemita de la cámara, así que reinicié, reinicié la compu y anduvo. Tecnología, lo primero que te enseña cuando algo no anda, tenés que prender y apagar y listo, se soluciona. No te escuchamos, Jorge, o quizás no te escuchó, Victoria, si escuchas.

**Victoria Reybet**: No, yo tampoco.

**Lucio Rojas**: Ahí está. Tomando otro micrófono. Estamos tranquilos en el puto. Si no paga y prende la compu, siempre funciona. Ahí te estamos escuchando lejos. Un avance. Te sigo escuchando lejos, pero te escucho muy lejos. Ahí te escuchamos bien.

**Julieta Alvarez**: No sé por qué se ve tan.

**Lucio Rojas**: Si van a un cruce, usan una cámara y una combo. Ahí está, Ahí está. Bueno, ¿Cómo andan? ¿Todo bien? Todo bien. Tanto tiempo. Retomando, retomamos situación. Bueno, ahora sí retomamos. Primero arranco antes de empezar a hablar, pequeña parte de disculpas de mi lado, que se fue dilatando. La cuestión, como lo hablé con vos, Jorge, las características del proyecto es que es algo que nosotros hacemos no con un costo de desarrollo, sino haciéndolo para también ustedes. Un amigo de Bruno ayuda en eso, tratar de hacer una aplicación que le funcione y por ahí uno lo van postergando otras prioridades. Perfecto. La seducción. Así que bueno, un poco la idea era empezar a darle un seguimiento, ahora que estamos más en órbita, a lo que es la idea, la aplicación hoy, retomar 10 minutos lo que habíamos pensado y poder mostrarles a ustedes una primera entrega de lo que sería la. La nueva aplicación para gestionar los presupuestos, lo que me parece que va a ser la mejor forma para que no vuelva a pasar esto de que se dilate es quizás marcar algunas reuniones, quizás virtuales, sin que ocupe mucho tiempo, si se enganchan con el proyecto, cada una semana o cada 15 días, donde yo pueda mostrarle cómo va avanzando. Y ustedes me van diciendo rápidamente el feedback, si piensan que puede ser funcional, si no, si hay que modificar algo y lo vamos trabajando. Perfecto, voy a levantar la app, Tengo que volver a levantar el host que recién reinicié la máquina, y cuando reinicie la máquina se me fue la app. Así que un segundo y acá está. Perfecto. Bien, vamos a hacer una presentación. Preparé una presentación muy rápida, hice con Claudio para retomar, para volver a hablar de de cuáles eran las cuestiones que habíamos definido en su momento. Y la idea es que ustedes me vayan diciendo, bueno, por acá no, por acá veamos la app, vea que le hace sentido o no, y así ya avancemos. Así que denme un segundito que abro todo. Bien, perfecto. Bueno, eso, compartir. Mientras hablaba estaba tratando de que se me comparta la pantalla, Entonces trato de pasar ultra rápido la diapositiva, porque la idea es ver la app, no una diapositiva. Sería más divertido ver ya todo trabajando. Pero un poco el problema era que nos habían planteado que tenían que gestionar presupuestos de obras entre tres partes, y estaba todo en Excel, que estaba en la máquina de cada uno. Y les costaba por ahí dos cosas, uno actualizarlo y la otra que tengan los tres información de lo que estaba pasando como en la macro, y poder analizar el negocio en sí y no tener una vista acotada de cada uno de los casos. Para eso me compartieron este Excel que estamos viendo acá, y yo no lo estoy compartiendo, voy a cambiar la forma de presentar. Voy a presentar este Excel donde teníamos distintas pestañas que formaban el libro, donde ustedes gestionaban las obras, tenían una donde armar el presupuesto, una que era la parte de administración, después teníamos la caja de estudio, la caja chica, y donde se generaban los certificados de honorarios y los certificados de avance de mano de obra. Todo esto lo que yo hice fue, entendiendo lo que ustedes me habían explicado, bajé cada una de las hojas del archivo y lo fui integrando con plot para que entienda cuál era la lógica de relación entre cada una de las hojas en sí. Por ejemplo, lo que vos vas certificando en los avances de mano de obra. Lo que se paga en caja chica está relacionado con el presupuesto, con la administración. Honestamente no me acuerdo cómo era el detalle, porque lo hice hace ya bastante, pero sí me acuerdo que tenía una lógica que nosotros la entendimos con Claude. Y lo que hicimos fue generar todo este mismo esquema lógico representado en una base de datos. Entonces armamos una base de datos que lo que hace es, en su momento habíamos hablado, crear distintas tablas que van teniendo cada una. Característica o un campo que representa, por ejemplo, lo que es el campo de obras, Un ID de la obra, un nombre del comitente, el tipo de obra, dirección, la ciudad, todos atributos de esa tabla. Después empiezan a relacionar las tablas diciendo, bueno, el ID de la obra yo lo uso para volver a llamar a la obra en el certificado de honorarios. Entonces si se arma toda la lógica que lo que tenemos que llevarnos de acá, y que es bastante profundo técnicamente, es que copia lo que nosotros teníamos en el Excel. Esto está todo hecho en base a mi criterio, combinado con la inteligencia artificial. Y con eso empezamos a plantear un desarrollo que tiene distintas capas o distintas olas. La primera ola o la primera capa de lo que yo empecé a plantear como esquema de trabajo en cloud, era copiar todo el núcleo operativo, lo que hace la misma ¿Que tiene que hacer el Excel para que no estemos haciendo cualquier cosa? Poder gestionar las obras y los presupuestos, una alta obra, un listado, un detalle, un cambio de estado. Poder generar un presupuesto con un costo base y un margen, que es lo que ustedes establecen. Poder tener tipos de cambio oficiales en vivo integrado para lo que es el cambio de pesos a dólar. Poder asignar subcontratistas a distintos rubros. Poder tener distintos ítems de trabajo en cada rubro. Y poder registrar pagos, ingresos y cajas. Pagos a subcontratistas con ajustes CAC, que me acuerdo que era el índice que ustedes usaban, que también lo tomamos de Internet para la actualización. Registrar los ingresos de las obras, los costos a los clientes, gestionar las distintas cajas, la caja chica, la caja de estudio, puede hacer los pagos a los contratistas. Hasta acá, esto fue lo primero que hicimos en laboratorio para mostrarlo a ustedes ahora y que me digan, ¿Tiene sentido? ¿Podemos ir por acá o necesitamos ser un refactor grande de cómo lo pensaste?

**Julieta Alvarez**: Por ahora lo veo lógico.

**Lucio Rojas**: OK, perfecto. Ahora la idea es que lo veamos en la aplicación.

**Julieta Alvarez**: ¿La idea de lo que planteaste tiene sentido?

**Lucio Rojas**: Sí, ya. Si la idea está mal planteada, ahí ya sería un problema más grave todavía. En una segunda instancia, que es hasta donde llegué, se pueden emitir los certificados de mano de obra con un porcentaje acumulado por rubro, con un ajuste de CAC, certificados por honorarios. Y esto genera un PDF que ustedes le pueden mandar a quien certifican o a quien están pagando. Esto ya se puede hacer. Ahora, lo próximo que quiero hacer es que puedan tener un análisis de Business Intelligence sobre la base de datos. Eso lo vamos a hacer conectando esto, que es una base de datos que nosotros levantamos en un servicio que se llama supabase, que es bastante barato, por eso lo elegí. Funciona bien para lo que queremos hacer, Conectarlo a theramot. A partir de conectar esta base de datos a theramot, ustedes desde Cloud, que es una inteligencia artificial que pueden usar desde su teléfono, pueden hacer preguntas, como. Acá, pueden hacerles preguntas a Claude, que van a poder ser como ¿Qué obra me están dejando más margen? ¿Cuánto hay pendiente de pago? ¿Subcontratistas hoy? ¿Cuántos cobramos? ¿Y cuánto facturamos en los últimos tres meses? ¿Qué rubros atrasa más en la obra? Todo ese tipo de preguntas ustedes las pueden hacer en tiempo real desde su celular. Los datos desde Cloud, en un momento se pensó en WhatsApp, pero yo entiendo que lo que querían hacer puede enviarle audios y hacerle preguntas a un chat. La palabra chat está medida prohibida en inteligencia artificial, sino un modelo que me responda en base a mis datos. Así que quizás Cloud desde el celular, una aplicación como la de ChatGPT desde el celular funciona mejor. Así que esto está integrado dentro de lo próximo que pensamos.

**Victoria Reybet**: Y Cloud, nosotros tendríamos que hacernos tipo nuestro, o sea, serían todos usuarios independientes. Tendríamos que pagarle a Claude como app. Digamos que se le pagaría chatGPT.

**Lucio Rojas**: Claro, la licencia de cloud vale 20 dólares y pueden hacer las preguntas desde ahí. Si ustedes ya tienen la licencia de chat GPT paga, podemos hacerlo sobre chat GPT y aprovechan la licencia que ya tienen. Para mí es indiferente, es lo mismo.

**Victoria Reybet**: Se va a tener hecho con Cloud.

**Lucio Rojas**: Todavía no lo tengo hecho. Si ya lo tienen pago a chatgpt, vamos ahí, si quieren usar Cloud, vamos por Cloud. Para mí es indiferente porque el conector es el mismo para los dos. Después ustedes decían el momento Cloud es mejor, por las dudas funciona mejor, te

**Julieta Alvarez**: consulto, no sé si lo tenés. Porque lo que nosotros pensábamos como WhatsApp, que es en realidad lo que más usamos, es eso de por ahí estar recibiendo facturas o boletas de proveedores, cosas, y por ahí la idea era como que eso reenviarlo y que ya automáticamente se nos cargue al Excel, No sé si eso ya está pensado en alguna etapa de esto o cómo se resolvería bien ese flujo.

**Lucio Rojas**: Bastante honestidad, no lo contemplé. Lo que es la carga de facturas,

**Julieta Alvarez**: sí, facturas en realidad no sé por decirte, pero más del 50% de la gestión que hacemos esto por WhatsApp, porque por ejemplo, suponete pagos clientes semanales, te lo mandamos en principio por WhatsApp con texto y después vale Excel, o sea que mucha de la información se maneja a través de WhatsApp. En realidad lo resuelve Claude.

**Victoria Reybet**: Yo lo que había entendido la otra vez que hablamos es que en lugar de mandar el archivo factura, PDF, jpg, sino que como para que no tenga que hacer todo el esfuerzo, no sé, cloud o quien sea, leer, sacar la data y meterla en una planilla, como que nosotros podíamos mandar la factura y escribir, creo que estoy flashando, como que si nosotros le mandábamos un mensaje escrito que decía pago pinturería, factura pinturería, 30 mil pesos, era como más sencillo que se cargue a ese Excel o a esas datos, que me mando un archivo jpg, PDF o lo que sea y que ahí tenga que exprimir todo eso

**Lucio Rojas**: bien, Bueno, o sea, lo que ustedes quieren es, antes cargaban el Excel a mano, leían la factura, cargan examen. Lo que yo hice principalmente en esta app, que es la que vamos a ver ahora, es poder cargar la información desde el celular, todos en una misma aplicación que está unificada, ahora vamos a hacer un recorrido entero, pero sigue siendo manual, ustedes van a tener que crear las cosas desde el mismo celular. Lo que quizás sea un paso más a sumar a esta ola de features o de distintas complejidades que tiene el sistema, es que ustedes le envíen esa factura o envíen un mensaje a Claude y que cargue por ustedes. La nueva factura. El nuevo ítem en la aplicación.

**Julieta Alvarez**: Y a lo mejor lo que dice Vico es, a veces lo que nosotros hacemos es yo voy a pagar, pago, le saco una foto al recibo y pongo que yo corralón, pago tanto. Eso lo puedo escribir.

**Julieta Alvarez**: Capaz el paso más sería mandarlo de WhatsApp, escribirlo en cloud.

**Julieta Alvarez**: Claro, sí se copia y se pegan,

**Julieta Alvarez**: Cloud, copiar y pegarlo, no sé. Si, bueno, es más fácil Excel

**Lucio Rojas**: sí. Si ustedes están en WhatsApp, quizás es mandarle un screen directamente a efectos de usar el celular. Es lo mismo que WhatsApp, porque es mandarle mensajes a un chat de inteligencia artificial en vez de una persona. La única diferencia sería cambiar la aplicación en la cual estás mandando. Lo que sí tiene un poco más de complejidad es entender yo cómo hacer para que Claude cargue lo que ustedes envían en la app. Eso lo tengo que pensar, me lo llevo como tarea. Entiendo que se puede, pero bueno, va a tener otra capa de complejidad.

**Victoria Reybet**: Sí, si, no, mostrarnos si querés hasta dónde hiciste, porque capaz que con eso también vamos re bien y es.

**Lucio Rojas**: Y vemos como les digo, o sea, es imposible que yo haya hecho algo para mí con el tiempo que pasó, con la época, por más que información lo del Excel es poca, para hacer un sistema, algo que ustedes digan está buenísimo. Entonces la idea es que lo vean y que me digan, mira, estos puntos están buenos, nos falta esto. La reunión para mí es para eso. Si ven por ahí en las caritas está la mía, la usted, y hay un azul que se llama The Motor Recorder, está grabando todo lo que estamos diciendo. Y yo después eso lo genero como transcripción y lo uso para trabajar en mejorar la aplicación con inteligencia artificial. Les muestro entonces un poco la aplicación y cómo la desarrollamos. Esto que está acá es cloud. Yo lo que hago, voy hablando con todo este chat para que me vaya generando la aplicación, las bases de datos, las distintas funcionalidades que yo le pido. Cuando grabe la reunión voy a pegar acá toda la información y decir, bueno, lo que hablamos, cómo mejoramos o para dónde redireccionamos la app. Pero esto básicamente yo escribo comandos y me ejecuta sobre la aplicación. Entonces yo acá quisiera agregar nuestra obra, subcontratos, cajas, uno más que diga un ejemplo. Esto para que entiendan cómo funciona. De cajas, Esto para que vean la facilidad que tenemos para iterar la aplicación, un poco lo que la herramienta inteligencia artificial. Entonces acá ahora me va a poner uno más que diga obra subcontratista, cajas y hola, que después lo tengo que sacar porque no sirve para nada, salvo que lo dejemos como un chiste interno también estaría bueno. Así que les voy a mostrar el flujo que se genera, que esto tendría que copiar lo que antes era el Excel entre las mismas funcionales. Y esto lo pueden completar ustedes desde su celular. La idea es que ponerle ahora adelante antes de esto una gente que lo complete por ustedes, si es que se puede. Déjenme evaluar también qué esfuerzo lleva la aplicación. Lo primero que hacemos es crear una nueva obra. Esto es como abrir un archivo Excel desde cero. No sé si quieren hagamos un ejemplo semi real o completemos lo a conciencia a ver si si tiene sentido lo que se armó. Lo primero que se hace el nombre del comitente. Empecemos con un ejemplo tipo caso de USA con el nombre de alguno de ustedes. Julia te uso el tuyo porque lo tengo ahí. Tipo de obra, una reforma acá no sé qué tipo de obras suelen ustedes.

**Julieta Alvarez**: Reforma, vamos a ver sí reforma por

**Lucio Rojas**: haber esto se puede editar así de fácil como debería aparecer el de hola no sé cuánto le falla, le falta, Me cambio de local, No sé qué hizo, acá está, mira, acá puso lol, pero yo ahí le tendría que decir mira no quería que esté acá, quería que esté acá. Entonces agarro, te mando un screen y digo, o vamos a hacer así, vamos a crear algo real abajo de no sé qué otro tipo de obra podrían tener acá. Interiorismo, le pego el screen y le digo. Y al interiorismo lo está editando, genera el código, lo actualiza los archivos que están creando la aplicación lo programa básicamente. Y ahora en varias veces nos tenía que aparecer interiorismo por acá, vamos a esperarlo. Elegimos interiorismo ya que estamos con el caso. Listo, interiorismo aparece en el dropboard, refrescarlo. A mí esto, perdón, me parece, Siempre me sorprendo cuando hago estas cosas. Interiorismo para que vean, no nos tenés

**Julieta Alvarez**: que mostrar eso porque entonces no, al

**Lucio Rojas**: contrario, yo prefiero que lo hagan ustedes, los ayudo. Así que yo lo pude exclusivamente para divertirme esto porque es excelente, me encanta hacer estas cosas. Dirección de mi departamento, Viví en mi departamento, Rosario. Estos son los datos que entiendo que ustedes estaban cargando en su momento fecha de presupuesto, el anticipo es lo que, en caso de que haya más 60% de anticipo, el margen del cliente es lo que ustedes les gana al cliente sobre el presupuesto, que eso entendí que es distinto a los honorarios profesionales que después cobran, que se factura por separado, me parece

**Julieta Alvarez**: un 5 y un 18.

**Lucio Rojas**: Está bien, 5 18. Eso lo dedujimos con Claude de la plantilla que me acuerdo. Y acá el costo base,

**Julieta Alvarez**: si le ponemos algo extra a la mano de obra, lo que sea, por si después hay algún incidente o algo, lo podemos hacer ver con ese 5 %.

**Victoria Reybet**: Claro, pero se la tenés que poner a toda la obra, no a cada rubro.

**Lucio Rojas**: Ah, claro, esta es la obra en sí, esto es toda la obra.

**Julieta Alvarez**: De última podemos poner menos. Hay un 1, pone.

**Lucio Rojas**: Bien, acá pongo 1. OK. Yo lo que había entendido, está bueno verlo, es que ustedes monetizan de dos maneras y si me dicen que no es así, está bueno si lo cambio. Una es el honorario profesional que ustedes cobran sobre la obra, o sea que si la obra sale un millón, ustedes ya el 18% que sería 180, pero que además otra forma de monetizar la obra es hacerle un markup al presupuesto.

**Julieta Alvarez**: Sí, pero no lo hacemos sobre todos los rubros, mano de obra o alguno en particular.

**Lucio Rojas**: OK, o sea que este margen de cliente no tendría que estar sobre el presupuesto en sí.

**Victoria Reybet**: Claro.

**Lucio Rojas**: Bien. Bueno, esto si está escuchando, toma nota de esto, le aviso, así después me aviso, así después me marca los momentos. Entonces esto lo vamos a modificar, lo dejo en cero. Entonces ahora ustedes con 18% el costo base del presupuesto.

**Victoria Reybet**: Perdón, interrumpo un segnín. Honorarios hay veces que está dividido, no sé, yo lo manejo todo junto, pero por ahí ustedes lo están manejando separado, no sé si el porcentaje que sea entero de toda la obra o a dirección de obra, una cosa de administración otra.

**Julieta Alvarez**: Sí, se puede dividir por. En realidad generalmente es verdad, dividimos dentro de un horario, tenés dirección, administración y proyecto. Sí, pero no, el proyecto estaría fuera de esto en realidad.

**Julieta Alvarez**: Bueno, pero sería como decías vos, de agregarle, después hablarle a Claude, agrégame otra.

**Julieta Alvarez**: En realidad dentro, como para hacerlo simple, dentro de ese honorario, de ese 18% tenés un 3 de administración y un 15 de dirección, generalmente.

**Victoria Reybet**: Bien, sí, o se puede dejar así y después la división se hace por fuera, o sea una final lo divide en caso de que sea necesario, por ejemplo.

**Lucio Rojas**: Si, tiene sentido. Vamos a lo que lo Ahora,

**Julieta Alvarez**: Capaz

**Victoria Reybet**: pensando en voz alta, capaz que está mejor que quede ese 18% para que después en cada caso, por ejemplo, de cada obra, a veces nos dividimos dentro de ese porcentaje entre nosotros, distintos sub porcentajes. Por ejemplo, no sé, yo ahora estoy haciendo una obra con Juli y yo por equis cantidad de tarea le pago un veinte, treinta, cincuenta por ciento, entonces quizás que al final nos puede hacer esa cuenta para nosotros como una división de honorarios entre nosotros, que a veces va ligado a la tarea y a

**Lucio Rojas**: veces no, o sea, a veces más

**Julieta Alvarez**: personalizado, digo, para que por ahí lo

**Victoria Reybet**: podamos personalizar y que lo tire en lugar de fijarlo del principio.

**Lucio Rojas**: Entiendo que esto después ustedes lo van a tener que dividir de cocina entre ustedes podemos hacer una sección directamente. Reemplaza acá mi ola, que sea división de honorarios y ahí contemplamos cómo se divide, ¿Les parece? Después lo sumamos. Perfecto. Entonces eso es el primer. Eso y lo del margen del cliente, fíjense que chaísimo, completamos el primer formulario y acá me dan tres, cuatro cosas la Así que vamos a estar con iteraciones, pero bueno, está bien. Acá convierte a dólares, validez el presupuesto y en cuanto comienza yo creo la obra, la obra me queda creada. Julieta, yo antes tenía otras, tenía a Valentín Baño y a mí, le arreglamos distintas cosas, así que esto van a ser sus nuevas hojas de Excel de todos, que lo van a tener en distintos presupuestos. Desde acá en Subcontratistas ustedes pueden agregar quiénes son las personas que ya están acostumbrados a que les hagan los trabajos de vuelta. Puse algunos compañeros de trabajo, nos reímos que le pusimos demolición a Gabriel. Bien, queda entonces. Vamos a hacer un ejemplo que haga acá. Especialidades también lo tendríamos que ustedes modificar en base a lo que quieran, pero Estructura eléctrica, carpintería. Te voy a poner a hacer paisajismo. Paisajismo, ya tengo a Sol.

**Julieta Alvarez**: Ah, bueno, dale, entonces. Chesería.

**Lucio Rojas**: Chesería. Bueno, dale, perfecto. Entonces vamos a la obra, Vamos a crear un nuevo rubro que entiendo que serían los trabajos que uno hace adentro del interiorismo de Julieta y no sé para qué sería. Entiendo que puede ser para arreglar una pared. Bueno, vamos de cuenta que se te rompió el cielo raso, vamos a decir. Entonces. Cielo raso se gira con dos R. Sí. Y con ese perfecto cielo raso del baño. Yo sé muy poco de esto, así que donde me puedo. No, me confunde, me dicen y va a estar, Jorge. Guardamos, entramos al rubro y agregamos los ítems de trabajo.

**Julieta Alvarez**: Estructura, ponele. Estructura.

**Lucio Rojas**: Cantidad.

**Julieta Alvarez**: Cinco metros cuadrados.

**Lucio Rojas**: Cinco cuadrados. ¿Y cuánto le presupuestamos por esto?

**Julieta Alvarez**: ¿Cien mil pesos? Ciento cincuenta.

**Lucio Rojas**: Setecientos cincuenta. Esto yo cuando lo hice me pareció que tendría que estar bueno poder ver usted primero presupuestan. Porque para mí esto, la aplicación armó la lógica al revés, porque primero vas a poner cuánto me sale el presupuesto y después me hace completar los rubros. Yo entiendo. El presupuesto sale de ahí, ¿No?

**Julieta Alvarez**: Claro.

**Lucio Rojas**: Entonces yo lo que haría sería pedirle que primero cree el presupuesto, vacío la obra con presupuesto, y cuando yo cierre los rubros, me presupueste y después le ponga el honorario y alguno de los rubros. Si hace falta un markup. Vamos con otro ítem. Adentro del cielo del baño. Puede ser. Bueno, no sé qué más lleva además de estructura, Jorge. ¿Cómo?

**Julieta Alvarez**: Emplacado.

**Lucio Rojas**: Emplacado y esto que llevan. Sé que no por algo hago trabajo de esto y no tengo ni idea. Perfecto.

**Julieta Alvarez**: Fijado. Pero se supone que está en realidad.

**Lucio Rojas**: Y ahora podemos empezar a registrar los pagos dentro de este rubro. No sé si acá haría falta. Se pueden registrar los cobros, pero atrás en el proyecto, esto sería lo que yo pago de lo que estoy presupuestando. Y esto te lo vincula con las cajas. Entonces acá la estructura, estos 150 son los 150 que ustedes presupuestan al cliente.

**Julieta Alvarez**: Claro, Eso que te decíamos nosotros el porcentaje que ponemos debería parecer como que nosotros no se lo decimos al cliente, porque en general a veces nosotros después lo usamos para cuando hay algún error poder absorberlo y que no se nos descuente el 18%, sino como que a veces terminamos ganando dos mangos.

**Lucio Rojas**: Entiendo perfecto. Esto. Sí. Acá de vuelta, un ejemplo. Nuevo ejemplo. Tipo de obra, departamento. Hoy, la semana que viene.

**Julieta Alvarez**: No, estaba pensando en el de mujer financiera que es.

**Lucio Rojas**: Yo lo uso para acá.

**Victoria Reybet**: Perdón, me quedé pensando en una cosita también. ¿Que anticipo? Nosotros tampoco pedimos.

**Lucio Rojas**: No, no piden.

**Victoria Reybet**: No.

**Lucio Rojas**: Perfecto. Estaba en la hoja.

**Julieta Alvarez**: En proyecto sí, algo para proyecto.

**Julieta Alvarez**: Claro, en proyecto sí pedimos un anticipo y después se paga contra entrega para la obra. Pero esto lo vamos. Estamos pensando para obra, o sea que no, porque

**Lucio Rojas**: bueno, hace sentido que esté dos saco los dos.

**Julieta Alvarez**: Sí, el de margen tiene que poner el imprevisto.

**Julieta Alvarez**: El margen estaría, o el margen, no sé si proyecto en algún momento se puede, porque en definitiva es algo que hacemos y que podría llegar a estar. Tenemos que ver cómo organizarlo, pero bueno, si querés lo acotamos a la obra y después vemos.

**Lucio Rojas**: Sí, empecemos con siempre unidad más chica de cosas posibles, porque si no, imposible. Fíjense que imposible si no empezar a terminar todo. Nos vamos a ir 100 veces por las ramas. Acá lo que hace es mostrar el cliente final te lo calcula el presupuesto con el margen este que vos te guardas. Entonces el cliente nunca ve esto margen. El cliente lo que hace es justamente prevenir que haya un problema. Julieta, volvemos al tuyo, cielo raso. Vamos a asimilar un pago. Pagamos hoy pagamos mano de obra, material, contrato. Hacemos cuenta que pagamos el material por la caja estudio, caja chica, no sé cuál sería.

**Julieta Alvarez**: Esas cajas en realidad van asociadas a cada obra también, no son cajas generales. Nosotros le llamamos caja estudia, lo que el cliente nos da por semana, y caja chica, lo que usamos para pagar cosas que no le pasamos la semana. Pero es de cada obra.

**Lucio Rojas**: Cada obra tiene su caja, ¿No?

**Julieta Alvarez**: Claro, es cada obra, porque pobre, no,

**Lucio Rojas**: estoy pensando, estoy pensando porque va a tener que. Ahora les voy a mostrar cómo se hace el maestro, el mayor de cajas. Hay que hacerle una agrupación más de cada vez que yo genero una obra, generar una caja.

**Julieta Alvarez**: Dos cajas por.

**Lucio Rojas**: Dos cajas por obra.

**Julieta Alvarez**: Algunas cosas las paga el cliente, otras la pagamos con la caja de estudio y otras con caja chica. ¿Está bien?

**Lucio Rojas**: Supongamos que esto es caja estudio, que es la plata que nos da el cliente por semana. Hicimos el pago de la estructura, el material, por 200 podemos 80 cac base, no sé cuál sería.

**Julieta Alvarez**: Yo te digo, te digo el de enero justo, justo lo tengo acá. El de enero era 19.209,4

**Julieta Alvarez**: y el

**Julieta Alvarez**: índice actual que es el de marzo es 19.771 con 20.771

**Julieta Alvarez**: anybody.

**Lucio Rojas**: Estate, Actualización del CAC, el ajuste.

**Julieta Alvarez**: ¿Y dónde hace el ajuste? Perdón, ahí abajo.

**Lucio Rojas**: Monto ajustado por el INSECAC, si querés lo puede hacer en dólares. El número de factura, hacemos cuenta que asociamos la factura 78901 y observaciones. Pago

**Julieta Alvarez**: marzo o semana del 30, 30 de abril.

**Lucio Rojas**: Esto un poco creo que respeta la lógica que tenía, debería respetar la lógica que tenía el Excel. Y yo voy guardando los pagos. Dependiente, generar otro pago, pago de mano de obra, cliente, descripción. Acá estaría bueno ahora que pienso que si yo un pago de mano de obra me aparezcan los subcontratistas. Y así va generando la unidad del rubro, podemos generar ingresos de la obra, que es cuando nos van haciendo los pagos los clientes, un pago parcial, esto sería lo que alimentaría la caja chica supongo, la caja estudio con mes nos dan 300.000, Así va manejando. Después puede generar certificados, tenemos un certificado de avance de mano de obra a día de hoy, de la última semana del cielo raso del baño, estaba en un avance del 50%. Observaciones, sin observaciones, Yo creo. El certificado está cobrado por registrar el ingreso está cobrado, si está solamente o no, puedo añadir el PDF para enviarlo al cliente.

**Julieta Alvarez**: Hermoso Lucio.

**Victoria Reybet**: Nosotros tendríamos que hacer eso con cada rubro siempre, O sea siempre certificaríamos por porcentaje, no por plata.

**Julieta Alvarez**: Se puede hacer al revés,

**Victoria Reybet**: porque nosotros por ejemplo toda la semana viene la Banili, te dice esta semana WhatsApp quiero un millón y dentro del porcentaje total tenemos poner a vernos cuánto es un millón, quizás si se puede poner un millón más que poner 20, 30, 40 por ciento.

**Julieta Alvarez**: La realidad nos hace que esa lógica para nosotros sea al revés, porque en realidad nosotros tenemos que estar a veces dibujando el porcentaje en función de lo que nos piden, porque lo que en realidad tendría que ser por avance de obra de nosotros decirle che se avanzó un 50%, en realidad no es así, viene el albanil y te dice che

**Julieta Alvarez**: quiero de esto igual lo que nosotros hacemos es verificar que eso corresponda, si él va a trazar, tratamos de que sí, pero en general es un monto

**Lucio Rojas**: fijo, vamos a pedir acá un avance, Me calculen porcentaje, los dos músculos, Ahora me va a modificar esto para que esta bande no solamente hay que pedirle a Claude que haga modificaciones, sino lo que yo hice fue levantar una base de datos que está corriendo y que se actualiza y guarda toda la información para que persista. Y después para hacer el despliegue también hay que elegir las distintas tecnologías. Esto yo lo tengo, no está público, esto hoy en día está desde mi máquina en un ambiente local y cuando ustedes lo quieran poder usar, tengo que publicarlo web y para eso se tiene que gestionar las versiones del código, poder subirlo a Internet, elegir la tecnología y demás. Pero bueno, esta primera instancia de generar o de modificar sobre lo que ya se generó es más fácil y estaría bueno que haya muchos de ustedes en esta parte. Fíjense cómo en un ratito me ayudaron un montón a mejorarla. Vamos a ver si me puede hacer el certificado por plata ahora. Listo, vamos a probar acá lo que me pidieron, certificado número 2, puedo ingresar, acá está, ingresa el monto del periodo. Si yo ingreso 20 mil, ahí me calcula. Ahí está, ahí lo hizo. Bueno, después otra cosa que nos faltó ver hasta acá, creo que no sé si faltó aclarar algo, yo lo que no entiendo muy bien es cómo se cierra la obra, cómo los pagos y los cobros y los certificados tendrían que ir descontando el presupuesto, el grado a base de ejecución de la obra. Eso acá me lo dice, yo tengo poca, no tengo tan fresco el tema, así que lo estoy refrescando mientras hablo con ustedes. Pero bueno, tendría que seguir la lógica del Excel.

**Victoria Reybet**: Sí nosotros hacemos como cierres mensuales muchas veces, o sea como semanales y mensuales, pero el total, digamos, donde se discriminan los honorarios son mensuales.

**Lucio Rojas**: OK, acá lo último que sería de este primer versión como para ver qué se puede hacer es las cajas. Podemos ver la caja estudio y la caja chica, que esto que decía tendría que volver a segmentarla por cliente, pero acá va registrando todos los pagos, los ingresos y egresos y la fecha. Le pedí que se parezca a mercado Pago, así es algo amistoso con la vista donde muestra ingresos y egresos, dólares y pesos de caja estudio y de caja chica, caja chica solamente pagué, si no tuviese yo cash, estaría un problema de. Así que nada, ya estoy, estamos casi sobre la hora, tengo otra reunión a las 4. Quería mostrarles esto, que ustedes me vayan dando feedback. Lo que sí voy a necesitar sí o sí es que le podamos meter mucho del lado de ustedes a que me digan cómo tiene que ser, porque como puedo deducirlo, pero después como ustedes lo usan va a ser distinto. Lo de el flujo de ida me lo llevo, lo voy a consultar con Claude, seguramente haya que hacer algo ahí en el medio, no importa qué, pero para que ustedes les puedan escribir algún chat de WhatsApp o de Claude que quieren y eso actualice solamente la aplicación esta sin que ustedes tengan que hacer lo que acabamos de ver, que así todo a mí me parece que ya es un avance respecto al Excel.

**Julieta Alvarez**: Sí, yo me lo imaginaba como si, puede ser algo así como en Mujer Financiera, no sé si viste el de Mujer Financiera, o estas aplicaciones que son como para gestionar los gastos de uno, que uno pone más.

**Julieta Alvarez**: Bueno, no dije nada, no sé cuál es.

**Julieta Alvarez**: Claude, no me escuches, no voy a ver esto.

**Lucio Rojas**: Pero ahora que pienso, creo que se puede hacer algo en lo que ustedes pueden directamente actualizar toda esta interfaz escribiendo o con audios, no sé cómo se va a llevar con el tema de reenviar una factura, esa factura la entienda y carga.

**Julieta Alvarez**: Eso se podría, como decía Vigo antes, lo podemos escribir, es un texto. Me parece que obviamente mientras más avanzando en esto que nos mostraste vos, está buenísimo. Nuestra primera idea, o por lo menos la mía que viene en un principio antes de la primera, era tratar de optimizar o agilizar toda esa parte que nosotros nos tenemos que sentar un día de la semana a hacer administración, por ejemplo, tratar de optimizar ese tiempo para usarlo en otra cosa y que todo esto que pasa vía WhatsApp, como decía, a lo mejor en un screen o reenviar texto a cloud o lo que sea, nos pueda agilizar todo ese trabajo.

**Lucio Rojas**: Buenísimo, melló el concepto, o sea, eso me sirve que me lo refleje, que es ahorrarnos tiempo. Así que vamos a tratar algo bastante sencillo. Y los cierres semanales, todo esto que ustedes vieron se guardan, base de datos, podemos conectar corte a motor y decirle te enseño a hacer el cierre mensual, hacérmelo todos los miércoles y eso en una instancia más futura se va a poder. Lo que entiendo que tenemos que resolver ahora es delimitar cómo va a ser la carga de obra y que la lógica funcione. Honestamente la que por ahí veo que me puede ayudar más en este tema es Juli, por el tema de que estaba con los ex, me acuerdo, en su momento los creaste, lo entendés perfecto, o si no podemos ir haciéndolo entre todos. Yo voy a no sacarle tiempo a dos, tres, quieren estar los tres, Perfecto, pero también vamos a necesitar una o dos veces hacer esto hasta que quede algo que esté al 100%. Yo no sé en cuanto estamos ahora, yo entiendo que un 80% quizás que estemos de cómo funcionar, capaz menos, capaz más, pero esto honestamente a mí me llevó poco tiempo, estuve ultra dedicado, así que si quieren podemos marcar esta misma hora la semana que viene o hacer algo antes y volver a lanzarlo dos, tres veces y yo mientras tanto leo esta reunión y les digo cómo resolver las cosas que más le interesan que son agilidades. Excelente. Bueno, nada, de vuelta disculpas por el tiempo.

**Julieta Alvarez**: No, gracias a vos, gracias en realidad por el tiempo tuyo, la verdad que bueno, y después si querés, sí quedamos, no sé vos.

**Julieta Alvarez**: Sí, sí, no hay problema.

**Lucio Rojas**: Yo los miércoles 4 puedo para no

**Julieta Alvarez**: por ahí no perder.

**Lucio Rojas**: Eso hace falta, eso hace falta, sí. Obligarnos un poco a ese ejercicio, o a mí por lo menos, si no después me llevan otras cosas. Buenísimo, bueno. Bueno chicos. Bueno, adiós, Chau.

**Victoria Reybet**: Chau.
