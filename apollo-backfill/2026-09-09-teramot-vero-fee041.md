# Teramot <> Vero

**Fecha:** 2026-09-09T17:08:56.359+00:00  
**Duracion:** ~49 min  
**Participantes:** Veronica Barrios <veronica.barrios@hzgroup.com.ar>, Franco Ferrero <franco.ferrero@teramot.com>  
**Externos:** veronica.barrios@hzgroup.com.ar  
**Apollo ID:** 6aa19e3bb9b0e70010fee041

---

**Franco Ferrero**: Bueno, creo que ahí ya terminó de armar la tabla Gold.

**Veronica Barrios**: Si, vos sabes que sí, pero yo te muestro dónde quedamos. Terminó de armar, voy a compartir un segundito. A ver si aparece. A ver, te quiero mostrar porque esto, a ver, nosotros dejamos. Todos estos son los datos que traía la tabla. Claro, claro, bueno, yo después lo que hice fue ir a ver este archivo en la parte de tabla gol, y cuando me lo iba, lo iba a validar, o sea, después acá ella me dijo, digamos, como que me planteaba la cantidad de registros que había, todavía está construyendo más chequear, 12.439 facturas con órdenes de compra. Ahora sí, bueno, para, porque en un momento a mí me tiraba como que había detectado, bueno, me pedía controles, o sea, cuando yo voy acá a entrar a esta tabla, la tabla Gol, esto, está, Es esta, yo lo que le dije, Le pedí que me la. Para descargarla, o sea, cuando descargaba, claro, nada más me tiraba como 100 registros, o sea, teóricamente, ¿No? Todos los casos donde había encontrado de repente inconsistencias, no sé si.

**Franco Ferrero**: Y a ver, preguntarle sí.

**Veronica Barrios**: Entonces, bueno, en un momento dudé, dije, a ver, no será este, digamos, le volví a repreguntar, si este era el nombre de la tabla, entré a ese archivo, hice esto, lo que te acabo de mostrar ahora, le pedí que me haga un dashboard, y cuando me hizo el dashboard, que me genere el Excel Pi, vamos a crearlo acá, ah, es este, ya lo descargué, esto que está acá, acá, acá ya lo descargué, o sea, solamente. Ahí está, este era el tema, solamente me trajo este detalle, o sea, me hizo toda una explicación a nivel números, pero cuando, digamos, yo quiero ir a ver la muestra con los documentos para validar, digamos, dónde estarían las diferencias, solo me trae esto, es decir, como que tuve por un lado esto, que para la cantidad de datos que ella me mencionaba me parecía que eran pocos, salvo que haya hecho un top ten, es

**Franco Ferrero**: que vos, cuando vos ahí pones exportar CSV, se exportan solo las primeras 100 filas.

**Veronica Barrios**: Ah, OK, bien, bueno, dato número.

**Franco Ferrero**: Sí, entonces si querés puedes ir a Cloud. ¿Vos querés descargar toda esa tabla?

**Veronica Barrios**: Claro, yo quería descargar esta tabla, yo lo que quería era, porque un archivo como, a ver, con el detalle, como para poder hacer la validación de lo que ella encontró con las diferencias, digamos, no sé si de todas, pero sí agarrar algunas filas y digamos, por significatividad o definir algún criterio por repetición de proveedor y digo, hacer la validación.

**Franco Ferrero**: Entonces está bueno lo que decís porque le podés poner, si querés, me gustaría hacerlo como con un análisis de criticidad en base a, por ejemplo, si un proveedor se repite varias veces, o los montos más altos, más que nada para ver si ya te lo está tomando bien y validar eso, porque la realidad es que son, A ver, son 18.000 filas, que es un montón, no te va a traer todo, pero le puede decir que en base a eso te filtre en base a lo que más deben o cosas así.

**Veronica Barrios**: OK, OK. Entonces acá directamente le podría, digamos, proponer.

**Franco Ferrero**: Sí, sí, decirle mira, yo quiero corroborar los datos que me mandaste,

**Veronica Barrios**: Me gustaría corroborar.

**Franco Ferrero**: Más relevante. Si querés decirle en base a algo,

**Veronica Barrios**: o sea, en base a montos en moneda, digamos, más relevantes. En base a montos y repetición de proveedores. Y repetición, Perfecto, voy a analizar cosas.

**Franco Ferrero**: Más que nada porque viste, hay veces que es así, que si te trae tantas filas, a ver, ahí ves, o sea, no te lo vas a poder descargar, más que nada por una cuestión de seguridad y de cantidad de datos, entonces capaz siempre mejor, viste, decirle la manera de que los empiece a agrupar de otra manera.

**Veronica Barrios**: Bien, bien, bien. OK, OK, entiendo.

**Franco Ferrero**: Fijémonos igual que va haciendo, Y esto está bueno porque ya te los va a empezar a agrupar seguramente, me imagino que deben tener varios que son el mismo proveedor, capaz te los agrupa y.

**Veronica Barrios**: Sí, por patrón.

**Franco Ferrero**: Claro, después para el control es más fácil, porque capaz directamente lo haces todo junto.

**Veronica Barrios**: Sí, sí,

**Franco Ferrero**: Pero ya ponele, para también ir entendiendo ya el tema tabla, ya no nos falta nada, como que ya está funcionando bien lo que sería la auditoría.

**Veronica Barrios**: Sí, sí, o sea, a ver, en algunos casos, ahora pruebo esto a ver qué es lo que me arroja. Sí, a ver, esta era como la prueba más amplia, digamos, que estábamos buscando. Ahí estoy viendo que tira parte de fardos de consumo, eso son las compras de productos que suelen tirar mayores diferencias porque hay un componente de humedad, digamos, en fardo de cartón y todo eso que hace que se generen descuentos y demás.

**Franco Ferrero**: Ahí veo que lo dice, post consumo

**Veronica Barrios**: y preconsumo, son distintos materiales los fardos.

**Franco Ferrero**: OK, perfecto, Ya debe estar ejecutando la nueva tabla seguramente. Dejémoslo cargar ahí.

**Veronica Barrios**: Bueno, acá esto lo armó en un. En un formato Word. Exactamente, lo puedo pedir que me lo pase a Excel. Esto lo puede pasar a decir, me

**Franco Ferrero**: lo puedes armar directamente, te lo trabaja desde Word, Esto te lo hacen un token Excel. Igual estaría bueno chequear la info que te trae, que esté bien eso.

**Veronica Barrios**: Sí, eso es lo que voy a. La idea es eso, es bajar la hora y por eso, a ver, en Excel se lo pido, porque normalmente a veces lo que hace es generar, poner número de órdenes de compra y eso, que después a la hora de hacer análisis es mejor trabajarlo en Excel. Sí, sí,

**Franco Ferrero**: Bueno, ya te lo va a armar. Debe ser igual que tenía seis páginas

**Veronica Barrios**: más o menos. 5 Igual este lo voy a descargar. Lo vamos a descargar. Cuatro. Sí, acá. Bien, para esto lo voy a guardar.

**Franco Ferrero**: A veces está bueno también tener eso, porque también te dice, viste, distintos hallazgos que encuentra, como que va más por

**Veronica Barrios**: el aloe, las cosas que me fue tirando, No es que descarte todo lo que me fue tirando, lo fui guardando y lo fui analizando, digamos, aunque después haya generado otras pruebas, digamos, no, nunca lo dejaba de, o sea, todo lo que produjo lo miré, es así, no es que lo descarté. Volviendo acá, si quisiera, tengo una pregunta ya que te tengo, aprovechando que tengo en línea, si quisiera. Uy, ¿Que hice, que hice, que hice, que hice? No, este no, este es copilo. No, este para que lo quiero cerrar.

**Franco Ferrero**: No,

**Veronica Barrios**: acá, bueno, acá lo. Ah, no, acá está, acá generó el documento. A ver, acá. Este en Excel, a ver cómo lo cargó. El mismo.

**Franco Ferrero**: ¿No, no, no, que abriste el otro?

**Veronica Barrios**: Sí, ¿Para que cierro este? Este es otro análisis que fíjate que

**Franco Ferrero**: es el que dice.

**Veronica Barrios**: Este. Sí. Ah, tenés razón. Ahora sí, bien, el curvano esto, Sí, estos son de, mira, revisar órdenes de compra. Bien, bueno, ya, diferencias factura versus recepción. Ajá, bien. Estos son de fardos. Bien, Baraldi. OK, OK. Acá te dice,

**Franco Ferrero**: tenés la posición, todo, Si.

**Veronica Barrios**: Diferencia de pago. Si, lo que no estoy viendo, no sé si en la otra está. A ver, quería ver la cantidad por lo menos las órdenes de compra o los documentos, o sea, los documentos para. Porque claro, acá lo que me pasa es que digamos, me termina generando como un resumen de lo que encontró de cada empresario, de cada empresa y de cada proveedor, digamos que digamos, de cada proveedor. Ahora, si yo quisiera un detalle, y era la otra pregunta que quería hacerte, es decir, suponete que acá yo quisiera descargarme esto puro, sin la limitación de, o sea, bajarme el listado completo con las 18 filas, 18 mil filas, eso ¿Cómo hago para levantar la limitación en cuanto a los registros? Porque seguramente parte de esto va a ser la apertura de esto, entonces como para no pedir que me genere

**Franco Ferrero**: directamente. A ver, yo lo que haría en tu caso, o sea, vos querés ver del Excel, viste que hay un par que tienen 80 casos, ponele, eco urbano, sí directamente se lo decís a Claude, che, tráeme los 80 casos, esto que detectaste, probalo así yo después corroborar a mano, entonces ya directamente es como que lo vas haciendo cada vez más puntual, es decir, en vez de descargar todas las filas, ir tanteando una por una, le decía Claudia, armame para cada una de las empresas un archivo Excel individual con todos esos, tipo esa información.

**Veronica Barrios**: OK, perfecto, OK, entonces ahí va a

**Franco Ferrero**: ir línea por línea a buscar de cada empresa cada.

**Veronica Barrios**: OK, excelente, excelente, excelente. OK, OK, bueno, le voy pidiendo acá, pásame un detalle

**Franco Ferrero**: de cada proveedor, si

**Veronica Barrios**: querés un detalle de cada. Un detalle por documento, Luego acá factura, nota, nota de. All right,

**Franco Ferrero**: Y ahora ya empezar a

**Veronica Barrios**: hacer directamente justamente las tablas. OK, OK, veámoslo a ver cómo lo pienso aunque sea. Sí,

**Franco Ferrero**: Ahí lo está pensando.

**Veronica Barrios**: Cuando esté lista la descargo como formato, avísame para chequear esto, cuando te da estos carteles, avísame para chequear esto. Ahí te está diciendo, Bueno, ahora, ahora.

**Franco Ferrero**: Que me decís, no sé si te entendió

**Veronica Barrios**: lo que le pedí. A ver, vamos a ver qué. La tabla Gold sigue siendo la primera opción, o sea, independientemente después que yo le pida alguna variante tipo haceme un ranking de los proveedores más que presenta más diferencias o de las órdenes de compra que presenta más diferencia, los documentos que prestan más diferencia, la tabla Gol es la primera, la primera que tiró con todos los registros, ¿No es cierto? Sí.

**Franco Ferrero**: Y si le querés decir que use tipo todo de vuelta, es como lo mismo, no pasa nada, pero sí, o sea, ya usa de referencia esa.

**Veronica Barrios**: OK, Dice la tabla, el informe clasificados por riesgos, ahí tenés completo, descarga directo. Acá me pone también, me dice acá tenés el link para descarga directa. No, no hay ninguna descarga directa, o sea no había ningún link. La tabla de hallazgo Detalle. Doc también queda disponible en Téramo para consultar directamente cada fila de la columna con un alto riesgo para que pueda filtrar en Excel por prioridad las columnas que incluyen nivel de riesgo, sociedad, proveedor, documento de pago con fecha, monto, documento de factura con tipo, fecha, moneda y moneda local o moneda de documento creo que es, condición de pago, orden de compra, posición, descripción. ¿Necesitas algo más sobre estos proveedores? No, en realidad solamente la descarga que No, eso lo que noté que no me la. Al menos acá, salvo que esté esto, digamos, en el caso anterior quise entrar pero no, no, no.

**Franco Ferrero**: A ver si, ponele tra M vos el CSV de esa tabla.

**Veronica Barrios**: CSV, ¿Verdad? Es así, ¿No? El formato. Sí, exacto.

**Franco Ferrero**: Vamos a ver si entendió bien porque.

**Veronica Barrios**: Sí, sí, Ahí tenés el link.

**Franco Ferrero**: No, ponele, armamelo a vos acá en un Excel porque te trae un link medio raro. Voy a preguntar, no. Me dejé sola, perdón.

**Veronica Barrios**: No, pasa,

**Franco Ferrero**: Está bien el paso que estamos haciendo. Estaba confirmando con Lucio que era vía cloud, pedirle que nos descargue el CSV.

**Veronica Barrios**: Bien,

**Franco Ferrero**: Por lo menos no saltó error. Quiere decir que está la está generando.

**Veronica Barrios**: Sí.

**Franco Ferrero**: ¿Usted están acá en Buenos Aires?

**Veronica Barrios**: No, pero sí, sí, sí, sí, acá físicamente estamos en el Palomar, zona este. ¿Ustedes donde

**Franco Ferrero**: están todos en Rosario? Yo estoy en Buenos Aires. Yo soy Buenos Aires, pero originalmente todos rosarinos.

**Veronica Barrios**: Todos en rosarinos. OK. ¿No tenés que ir a Rosario?

**Franco Ferrero**: Sí, sí, tengo que ir. De hecho, a ver, yo entré hace no tanto, así que debería ir a conocer, viste, un poco todo, pero la

**Veronica Barrios**: verdad que sí la virtualidad todo esto lo permite, es increíble, Es buenísimo.

**Franco Ferrero**: En realidad de más eficiencia que obviamente que hay momentos que por estar virtual capaz no estás igual de presionado que en la oficina todo el día codeándote con gente, charlando con gente, pero bueno, la verdad te lleva a ser más productivo a veces.

**Veronica Barrios**: Yo pensaba que estaban todos en Buenos Aires, Mira, o sea que es de Rosario Tiramón, o sea, estaba basada físicamente Rosario ya. Claro,

**Franco Ferrero**: Porque ya se dio cuenta que es un dataset muy amplio.

**Veronica Barrios**: Ah, OK. ¿Esto lo entendés vos? Sí, Johnny, Si. Aparte tío, run una lo falló, voy a tirarlo, abrí el último, mira a ver acá este.

**Franco Ferrero**: Planean armar el Excel por partes con CCB intermedios.

**Veronica Barrios**: ¿Ajá, ajá? Acá dice tengo las primeras 100 filas de crítico, voy a extraer los datos por lote, llamar en Excel completo para ser difícil agregar a nivel 1.

**Franco Ferrero**: ¿Cómo se entendió bien? Está bien, Es que eso está bueno, viste que a veces se pone a repensar solo si se da cuenta que está haciendo cosas que son capas más complicadas que realmente es.

**Veronica Barrios**: Si, se autogestiona, se autogestiona para lo que lo que le pedí. Sí.

**Franco Ferrero**: Esto ya dice como que no puedo, Capaz está complicando mucho. Vamos a la pregunta de vuelta, decir en base a la tabla que armaste antes. Que se llamaba integridad, ¿No?

**Veronica Barrios**: Tráeme, Sí, que me traiga.

**Franco Ferrero**: Segmenta por proveedor.

**Veronica Barrios**: Segmenta por proveedor,

**Franco Ferrero**: una lista. Sí, de todas las.

**Veronica Barrios**: ¿De todos los casos, no?

**Franco Ferrero**: De todos los casos, de todos los casos. Y hace ponerle, si quieres decirle, haceme una hoja de Excel. Para cada proveedor. Con el detalle, agregale proveedor con el detalle de todos los casos de ese proveedor de todos los casos correspondientes. A ver si ahí lo hace un

**Veronica Barrios**: poquito, a ver, a ver, Voy a construir consultando proveedor por proveedor y explorando los datos. ¿Como? ¿Funciona ahora? Escalo el enfoque, consulto todos los proveedores con string, no se identifica esto como string, delimita las condiciones, las

**Franco Ferrero**: de formato me parece.

**Veronica Barrios**: Voy a crear una para. Averaka.

**Franco Ferrero**: No, pero poné generar Excel, a ver.

**Veronica Barrios**: Ah, para, sí, eso tío, exactamente, generar ex, porque es un formato.

**Franco Ferrero**: Proba tocando ahí donde dice generar Excel a la derecha.

**Veronica Barrios**: Ah, perdón, no lo había visto.

**Franco Ferrero**: Continúa, Vamos a ver, quiero ver si

**Veronica Barrios**: me quedé con eso de que es un formato JSX, no lo había visto

**Franco Ferrero**: nunca, No es JavaScript creo, o JSON, o sea, no pasa nada, pero es una cuestión. Quiero ver. Raro que le dijiste lo del Excel y te lo mandó, pero claro, son 39 proveedores lo que, o sea, te lo detectó bien. Sí, porque el otro ni siquiera avanzó nada, sí.

**Veronica Barrios**: No puedo descargar directamente desde s por restricciones de voy a crear y que genere el excel con 39 hojas, frenalo

**Franco Ferrero**: porque si no vamos a estar. Más que nada para que sea eficiente, ponele. Tráeme, o sea, si querés decirle de mis tres principales, de los tres principales que detectamos. Si querés pasar los nombres.

**Veronica Barrios**: De estos proveedores, de los dos críticos

**Franco Ferrero**: de esos tres, tráeme el detalle de cómo se dan esa diferencia de plata.

**Veronica Barrios**: Sí, de los proveedores, de los siguientes proveedores. Voy a poner los siguientes proveedores que son más críticos que eso, son los más críticos.

**Franco Ferrero**: El detalle de cada uno con todos los. Con todos los hallazgos sería. Monsieur bourgué. ¿Se te habla en inglés?

**Veronica Barrios**: Ni idea la traducción. Igual me hace la traducción,

**Franco Ferrero**: pero como que hablas en español, te contesta en inglés.

**Veronica Barrios**: Perfecto. Son.

**Franco Ferrero**: Ecourbano debe tener 87 filas.

**Veronica Barrios**: Sí, sí. ICI, Ahí vamos, viste, Mira, dice.

**Franco Ferrero**: Si, es verdad, uno por uno, eso. Bueno, lo veo mejor que antes,

**Veronica Barrios**: No se trunque.

**Franco Ferrero**: Ahí lo que te dice que como tardó un poquito más porque dividió las.

**Veronica Barrios**: Sí, voy a consultar en dos mitades para que no se trunque. 87 filas son 1 montón. Para. Se ve, para.

**Franco Ferrero**: Tengo los tres proveedores en disco, ahora genero el Excel formateado con una hoja por cada uno.

**Veronica Barrios**: A ver, acá está. Descargar,

**Franco Ferrero**: a ver cómo lo descargó. Parece bien por lo que dice ahí,

**Veronica Barrios**: el detalle parece razonable. Tira interior acá. Detalle. Pago, muy bien. Factura, Bueno, esto habrá que analizarlo. Sí, sí, ya que tenga esto ya es bastante importe. Pago, acá hay que ver la diferencia, puede ser que el orden de pago concentre varias facturas.

**Franco Ferrero**: Todo eso lo que me decís, se lo podés decir también como para que lo tome en cuenta. Por ejemplo, ahí hay un cero, no sé, capaz.

**Veronica Barrios**: Está bien el cero, no sé sí hay que. Sí, sí, esto lo voy a tener que. Lo veo, lo voy a analizar, digamos, lo que a mí me conviene ahora es no tirar, o sea, dejar esta consulta, hacer análisis sobre esto, ir pidiéndole que vaya mejorando el archivo que me va generando, digamos, o sea,

**Franco Ferrero**: A ver, un poco lo que se me ocurre es, vos cada vez le va a seguir pidiendo más detalle, por ejemplo, pidiendo más detalle vas a poder empezar a segmentar ahí en el Excel, y obviamente que cada vez le vas a poder empezar a agregar más cosas, lo que vos decidas directamente, así como me lo dijiste a mí, viste, lo de chequear esto, le decía a Clutch, tipo che, armame esto particular para cada empresa. Claro, hay veces que capaz lo que te va a pasar es al ser 39 empresas proveedores como nos pasaba, te va a tardar un poco más entonces, sobre todo si vas a ir una por una, pero más que nada eso.

**Veronica Barrios**: Bien, bien. Bueno, bueno, yo voy a analizar esto entonces, Franco, no sé, me parece como analizar y para que te quiero volver que me fuiste acá, acá dejo de compartir, entonces analizo eso y bueno, y volvemos a hablar a ver cómo les parece.

**Franco Ferrero**: Sí, sí, cualquier cosa escribinos, nosotros igualmente seguramente lunes, martes te vamos a estar escribiendo, a ver, pero nada, avisanos, o sea, venís con el uso, tenés dudas, mandanos un mensaje.

**Veronica Barrios**: Dale, perfecto, perfecto. Bueno, Franco, genial, muchas gracias. Gracias, hablamos, Chau, chau, chau, chau.
