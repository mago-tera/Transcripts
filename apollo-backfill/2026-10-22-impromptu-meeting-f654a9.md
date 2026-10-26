# Impromptu meeting

**Fecha:** 2026-10-22T18:01:56.008+00:00  
**Duracion:** ~33 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Valentín Torassa Colombero <>, Ariel Franco <>  
**Externos:** Ariel Franco  
**Apollo ID:** 6ada57523629d10020f654a9

---

**Franco Ferrero**: Hola Franco, ¿Me escuchas bien? Yo te escucho. Me escucho bien ya, Sí.

**Franco Ferrero**: Bueno, buenísimo.

**Franco Ferrero**: Bueno, ¿Cómo estás? Bueno, estoy con Gustavo también.

**Ariel Franco**: Buenas Franco, ¿Cómo estás?

**Franco Ferrero**: ¿Todo bien? Ahí se está sumando Valentín, que es nuestro CTO, el encargado de toda la parte de seguridad. Así que más que nada también porque la última vez habíamos hablado tema de seguridad de datos, que yo no tenía mucha idea de cómo contestar, porque bueno, hay cuestiones capaz más técnicas que capaz Valentín se las puede contestar a ustedes de una manera mejor y para que les quede más claro también.

**Franco Ferrero**: Bueno, dale, no hay problema.

**Franco Ferrero**: Bueno, no sé si quedaron algunas dudas de la última vez o si querés que vayamos de vuelta a recordar algo.

**Franco Ferrero**: No, la verdad que nos trabó un poco ese tema, porque un tema de compartir información, entonces no avanzamos lo que es la aplicación del sistema, porque no teníamos tampoco mucho cómo probarlo.

**Franco Ferrero**: Bueno, a ver acá. Gracias, Valen, todo. No, te estamos escuchando antes. Te escuchamos, creo. Está muteado por eso. Puede ser.

**Franco Ferrero**: Yo estoy muteado.

**Ariel Franco**: No, no, no, Valentín,

**Franco Ferrero**: Acá también un poco la idea es que todas las dudas que tengamos sobre seguridad, tema de datos, Valen va a ser el que la va a responder, el que más sabe. Así que acá también más que nada para brindarles un poco de la tranquilidad que tienen el tema de la seguridad de datos con Theramot y que no es una cuestión de que nos están dando datos. Así también como te mencioné en el mensaje, nosotros estamos trabajando con la Segunda, que también es una compañía de seguros, capaz ustedes les interesa, porque por una cuestión de que nos comparten sus datos, que también trabajamos con aseguradoras. Entonces me gustaría también transmitirles eso.

**Ariel Franco**: Sí, sí, sí, lógico. Y con la misma modalidad que nos están ofreciendo nosotros están trabajando con la gente de la Segunda.

**Franco Ferrero**: Claro, a ver, el tema de la modalidad ahí es un poco. Nosotros trabajamos como un SAS. Después, bueno, nada, brindamos nuestros servicios de implementación, que eso van aparte para un tema de también hacer llegar bien el uso de cómo usar Theramot y de qué manera sacarle el mayor beneficio. Y además también hoy en día también les quería comentar que lanzamos una nueva versión que se llama Theramot Beacon, que lo que hace es corre en su propia infra, por una cuestión también de seguridad. Creo que también capaz les podía llegar a interesar eso. Ahí Valentín capaz tiene un poco más de información sobre cómo funciona eso que capaz les interesa más también.

**Ariel Franco**: Sí, sí, puede ser, Nosotros estamos abiertos a escucharlo, pero para que se entienda también que nosotros tenemos las mismas reglamentaciones que tiene que cumplir, por ejemplo, la segunda, como compañía de seguros tenemos un ente de contralor y tenemos un deber de guarda de datos y de resguardo de datos informáticos sobre todo. Para ello nosotros tenemos un proveedor de servicios informáticos para la administración de los recursos de la compañía, que es un proveedor tercerizado. Entonces en ese proveedor tercerizados, lo que ellos nos dan a nosotros son los datos, que serían nuestros datos, pero la estructura de la base de datos y la base de datos es de ellos, por los cuales ellos tienen una responsabilidad también con, por ejemplo, la superintendencia, con etcétera, etcétera. Y nosotros tenemos términos contractuales con ellos en los cuales nosotros si les brindáramos a ustedes el acceso a la base de datos, lo estaríamos violando, hablando contractualmente por términos legales, o sea, ellos me prohíben expresamente a mí darle el usuario y contraseña a cualquier proveedor ajeno a San Patricio, nosotros mismos o ellos, como el cartel enorme de prohibido acceso a cualquier persona ajena a la compañía. Eso es parte de un tercero más que de nosotros. Correcto. Entonces, de la misma forma que yo exportase la base de datos y trabajáramos no online, sino con una exportación en un backup, estaría también violando los términos contractuales de la exposición de la estructura de la base de datos que no me pertenece. Entonces ahí tenemos como dos puntos legales y contractuales contra un tercero en el cual más allá de la tranquilidad y la confianza, tenemos términos de legales que tenemos que cumplimentar con ellos. Entonces Por ahí, si ustedes tienen alguna experiencia que yo calculo que la segunda de primera línea está dentro de las top 10. Sí, pero no importa, por más que sea nuestro, la charla sería la misma. De alguna forma entiendo que lograron persuadir y saltar legalmente esta. Esta inquietud que me plantea mi proveedor, me dice de ninguna manera, no, pero Tegramot no me deja seguir continuando la conversación, ¿Me explico? Claro, de ninguna manera. Me dice, no, pero Gustavo, se terminó la charla, cambiamos de tema porque no vamos a llegar a ningún puerto en esos términos, porque ellos también tienen comprometida su estructura de base de datos con otras 39 compañías de seguro en el mercado. Pero bueno, nada, no puedo lacerar ni dañar la relación que tengo con este proveedor. Entonces, al no poder dar acceso fehaciente a la base de datos, no poder una réplica de la base de datos, ya iríamos a tablas. Yo ya ahí no sé cuánto es la eficiencia de Theramo para responderme, y si no tendría alguna queja por parte de mi proveedor tampoco, no creo. Pero bueno, más que una conversación, ustedes tienen algún elemento de persuasión legal como para decir, che, nosotros tenemos este contrato, revísenlo con ustedes, revísenlo con el tercero, vean estas directivas, más allá de. Estos son nuestros niveles de seguridad, estos son los niveles de seguridad, la descripción técnica, táctica y cómo fue su experiencia con la segunda también. Acá tenés el usuario, el SA y la contraseña. Hagan lo que les parezca. No creo que haya sido así. Si ustedes tienen esa experiencia ya enriquecida de cómo lograron penetrar en el mercado, que calculo que debe ser la parte más difícil. Después el resto, de verdad, todo bárbaro, no me cabe ninguna duda. ¿Nosotros tenemos experiencia con Project Capo, todos los tokens ya,

**Valentín Torassa Colombero**: no? Sí, de hecho,

**Franco Ferrero**: cómo se les trabó y no sé si lo van a escuchar.

**Valentín Torassa Colombero**: Es verdad.

**Ariel Franco**: Si tienen esa para pasárnosla, para ver cómo podemos saltar ese paso. El principal que no es de confianza, ya es un tema legal.

**Valentín Torassa Colombero**: Sí. Ah, sí, creo que se trabó, ¿No?

**Franco Ferrero**: Vos viste el tema de la segunda, ¿No?

**Valentín Torassa Colombero**: Sí, sí. Y el de Valian, que son las dos.

**Franco Ferrero**: Ahí está.

**Ariel Franco**: A veces pasa, no sé dónde escucharon.

**Valentín Torassa Colombero**: Si, no, escuchamos la mayoría bien. La verdad es que. Bueno, no es el. ¿Ahí se escucha, no? La segunda y Avalian, que bueno, acá son del conglomerado de AK. Las dos nos plantearon las mismas cuestiones de seguridad en general y de encriptación, y de cómo manejamos los datos también, porque era una duda de la segunda. Hace un tiempo sufrió una exfiltración que se hizo muy conocida, entonces supongo que también eso es algo que. Que les agrega más presión al hecho de que de nuestro lado, el hecho de que hacemos con esos datos es algo peligroso, pero también por un tema de governance, que yo como Yo soy ingeniero de ciberseguridad, y es como el principal tema, más allá de la seguridad, es también hecho de saber que tus datos están en un lugar concreto, que vos tenés un control sobre lo que entra y sale. En base a eso tenemos dos soluciones, una para la parte de del SAS, digamos, que es lo que ustedes contratarían sin tener que montar algo en su infraestructura, que sería Tenemos Beacon, que igual las dos lo tienen, pero son formas diferentes de solucionar el mismo problema. ¿Que son las normas de seguridad? Las normas de seguridad son un documento que se audita contra una auditoría externa, en este caso estadounidense, que te asegura el hecho de que todos los datos que entran en nuestra infraestructura, por más de que sea una copia, de ninguna forma son legibles o accesibles por nosotros. Y tienen controles que aseguran fehacientemente que eso, al menos en un control hecho por una auditoría, digamos, no se van a exfiltrar de ninguna forma y no hay peligro de exfiltración. Entonces todo eso es algo que de hecho son las soc. La norma que nosotros tenemos es un control que te piden sí o sí para trabajar como proveedor de software de cualquier empresa estadounidense. Y son generalmente los controles que más se tienen en cuenta, más allá de normas como las ISO, porque tienen una parte que conlleva documentación, y otra que es test de que todos los controles de seguridad que vos decís tener, efectivamente los tenés. Por otro lado, tenemos una solución que se llama tenemos Beacon, que corre on premise en la infraestructura del usuario. Eso hace que vos puedas asegurar el hecho de que el governance nunca sale de tu propio servidor, que estén en la nube, que estén en tu servidor físico, en tu fierro, pero ambas están securizadas por el hecho de tener esta certificación. Y otros controles que que yo doy fe como ingeniero de ciberseguridad que tenemos, que son un tema de encriptación at rest, del hecho de que si no tenés la privat key y la salt del usuario, no podés acceder a los datos, y que la auditoría que nosotros llevamos sobre la base de datos, que es algo que ustedes pueden consultar todo el tiempo en la página, es solamente lo que se llama app only, o sea, sólo se pueden agregar registros, pero nunca modificar ni borrar registros. Entonces si alguien, incluso un usuario de therapy, consultase eventualmente esos datos, hay un registro muy claro de que esa consulta fue llevada a cabo. Entonces tendrías como esa seguridad, el hecho de que vos estás muy seguro de quién hizo qué con esos datos, quién lo consultó, quién puede acceder, y tenés este control de auditoría. ¿Tema legal? Bueno, las soc tienen una etapa legal que tiene que ver con el SLA, que tienen que ver con los términos y condiciones, que justo ahora lo estamos, que todo el tiempo lo estamos actualizando con nuestros abogados. Entonces eso es otra cosa que les puede ser interesante consultar o leer, porque parte de hacer esta norma de seguridad es asegurar que toda la parte legal vos la tienes al día. Y eso es más que nada los que nos pidieron empresas como Bailen o la segunda, que también fue como un va y viene entre nuestro sector de ciberseguridad y su sector de ciberseguridad, que tenía una parte de legales y una parte de controles que aseguraban el hecho de que no estaban conectando sus datos a cualquier lado.

**Ariel Franco**: Claro, bueno, si lo tienen los términos y condiciones y todo eso, pásenoslo con el proveedor nuestro si podemos avanzar en esa línea. Vos lo que me decís básicamente es que podés hacer solo inserciones y no podés hacer ni update ni delet. Sobre la copia.

**Valentín Torassa Colombero**: Exacto, sobre la copia de hecho solamente lectura. Y sobre el control de auditoría, que es lo que me dice quién fehacientemente entró a consultar los datos, solamente se pueden hacer adiciones. Entonces vos sabés que tenés tu copia de base de datos seguramente, y que todos los que consultan tus datos desde nuestra plataforma, al menos, que no es todos los que consultan los datos real, sino sólo desde nuestra plataforma, es sí o sí auditable y no se puede cambiar.

**Ariel Franco**: Bien, bueno, y después no sé si tienen documentación sobre los perfilados para armar los contextos dentro de los prompt para limitar el acceso a la información. Eso no sé si lo haces vos o si lo hace alguna otra persona. Cómo es la documentación de los playground de delimitar y marcar desde hasta dónde puedan dar los contextos de información de los prompts que se le puedan hacer. Y eso por un lado. Y la dos serían los controles contra los prop injections dentro de la misma organización.

**Valentín Torassa Colombero**: Bien, son dos muy buenas preguntas, porque justo ayer di una charla sobre eso, así que me agarraste con el tema fresco. Básicamente nosotros no aseguramos solamente el hecho de que la gente pueda tener la tool segura a través de la sanitización de los prompts, sino que tenemos toda una defensa en capas que ataca a toda la infraestructura en varias partes. Es lo que se llama defensa en capas o arquitectura zero trust. Vos solamente das los permisos que tiene que tener para poder consultar lo que tiene que consultar. Entonces tenemos por un lado permisos de API, permisos del propio sistema IAM y seguridad en cloud, y después también sanitización de los prompts con la tool, que todo esto fue auditado por una empresa de pentesting de acá de Argentina que se llama Faraday, que fue la que nos aseguró que nuestro agent y y nuestra aplicación es segura tanto como API como AGE, que justamente como AI digamos. Por otro lado el prom injection es un ataque, en mi opinión es recontra interesante porque es la primera vez, de hecho las inyecciones a lo largo de Internet, nace el SQL, nace el cross site scripting y después llega una que era totalmente diferente porque era una instrucción que se le daba a un agente, o sea lenguaje natural. ¿Cómo limitas el lenguaje natural? Bueno, lo que nosotros encontramos es que el lenguaje tiene una entropía alta, digamos, y esto es lo que encontraron todos los frameworks que protegen de prom injection. Entonces lo que hacemos es limitar la source, Si adentro de tu tabla hay un registro que en realidad es una instrucción maliciosa para uno de nuestros agentes, el agente tiene el contexto de que eso lo está leyendo de la source del cliente y no lo va a tomar como una instrucción para llevar a cabo una operación, sino que lo va a tomar como eso. Dentro de este dato estaba esto implícitamente. Eso no puede ser tomado como una instrucción para mí, básicamente por cómo funciona nuestro landgraph también, pero también porque los agentes tienen un warrail contra eso. Pero nada, nos dimos cuenta, si vos pensás en el SQL injection que es cuando vos filtras la base de datos a través de un campo de escritura. Exactamente. Vos podés limitar el hecho de que el usuario te ponga una comilla, porque vos sabés que lo que te tiene que limitar es el algoritmo de escritura, o sea, la programación tiene una forma, el SQL tiene una forma, pero el prompt injector no tiene una forma, El lenguaje natural puede estar en cualquier lado, es poco limitable. Exacto. Así que nos pusimos a limitar la source y eso es lo que hace cuando lee una.

**Ariel Franco**: Pues sí, desde el origen donde es ejecutado el prompt.

**Valentín Torassa Colombero**: Exacto, esa es nuestra forma de protegernos y al menos la que yo estoy viendo, la que está llegando la industria por ahora, hasta que no se desarrollen métodos más sofisticados sin duda. Sí, que ya van a llegar, pero por ahora estamos en ese punto

**Franco Ferrero**: yo

**Ariel Franco**: vi muchas cosas locas, muy locas de inyección de promo, la atención por la creatividad que tiene en cómo violar la propia lógica de.

**Valentín Torassa Colombero**: Es una locura.

**Ariel Franco**: Claro, es una locura. Pawnean cualquier reciente y yo como guardián de los datos, imagínate que ya me metieron varias veces, entonces ya los niveles de protección son muchos, ya cuando te pasa más de cinco veces tomás medidas de seguridad mucho más rígidas que si no hubiera pasado nunca, porque las sufrimos todas, absolutamente todas. Ransomware, inyección de SQL, inyección de código por PHP, violación por fuerza bruta de claves con los usos de los chinos, entonces. Sí, sí, varias veces, nos pasó varias veces. Los chinos se dedican a constantemente a vibrarnos, básicamente.

**Valentín Torassa Colombero**: Aparte las aseguradoras son un.

**Ariel Franco**: No a grandes corporaciones.

**Valentín Torassa Colombero**: No, encima las aseguradoras son un objetivo súper jugoso para los ciberdelincuentes.

**Franco Ferrero**: Sí, por los datos de tarjeta de

**Valentín Torassa Colombero**: crédito, todo, de todo, De todo, sin duda.

**Ariel Franco**: Pero bueno, nada. OK, yo vería toda la documentación legal que tiene, la charla con el proveedor o podríamos ver incluso yo le comenté al dueño de la. En realidad no es el dueño que hace las cosas, digamos a Char, que es como el no dueño pero casi el dueño y sí, sí le había parecido interesante, pero después todos están ante la negativa total y absoluta, que es la barrera más grande con la que nos encontramos hoy. El temor de la implementación con el tema de seguridad.

**Franco Ferrero**: Franco Si, no, es un tema. A ver, para. Es un tema que lo vemos muy seguido en la mayoría de los clientes, entonces también por eso está bueno brindar esta confianza también demostrarles qué es lo que se arma por detrás de Telamot para que entiendan también de qué manera estaba arquitecturado todo.

**Ariel Franco**: Ni hablar, ni hablar, o sea, para ser sinceros y extremadamente claros, como es la postura que yo veo que tengo y la visión que tiene el proveedor también, yo veo que el 100% de la eficiencia de los agentes que ustedes crearon es actuar sobre bases de datos, no sobre LLMs, o sea, la experiencia de ustedes está sobre la base de datos y ese es el 100%, dice, che, pero si no tengo la base de datos, también tengo un lenguaje LM bastante bueno porque tengo el aprendizaje del anterior y le agrego una capa anterior a eso y si no me queré pasar por LM tampoco, o por backup también te puedo dar uno si me das las tablas. Yo creo que en cada uno de los niveles de seguridad que nosotros estamos mitigando, pierde eficiencia la herramienta y se va convirtiendo cada vez más en lo que es un lenguaje tradicional, como lo que hace Cloud, GPT o cualquier especializado en servicios profesionales, la herramienta de ustedes. Entonces, por un lado tengo la reticencia a entregar la clave que explota la máxima funcionalidad que nos vienen a ofrecer. Y por otro lado, tengo una eficiencia similar a lo que yo ya tengo. Hoy actualmente estamos como en esa encrucijada, che, o te doy la clave y funcionas bien, o no te doy la clave y funciona como lo que ya tengo. ¿Me explico?

**Valentín Torassa Colombero**: Claro.

**Ariel Franco**: Este es el cuadro en el que nosotros encontramos, obligamos la llave porque no vamos a tener ningún beneficio adicional al cual hoy tenemos.

**Franco Ferrero**: ¿Qué proveedor tienen de sistema ustedes?

**Ariel Franco**: ¿Sextemas se llama?

**Valentín Torassa Colombero**: Sociedad Ananina Sex o el cómic como Sex.

**Franco Ferrero**: Después también, bueno, les comenté lo de esta nueva versión que sacamos, porque de hecho, bueno, hay muchos clientes que por tema de seguridad prefieren que corra directamente en su infra. Y obviamente, a ver, es una magnitud un poco más grande y obviamente justo

**Ariel Franco**: nosotros estamos una migración de eso. Estoy llevando a cabo una migración de eso. Nosotros tenemos un housing en un DLR divino de 196 GB, hermoso. ¿Cómo se llama? Se está quedando base, quedó viejito ya, así que lo vamos a migrar seguramente a un Amazon, un AWS, un Oráculo, algo de eso. Estoy entrega para migrarlo. Ya, pero sí puede correr ahí eso. Yo estoy en recursos, estoy en 50%.

**Valentín Torassa Colombero**: ¿Con el modelo o sin el modelo?

**Ariel Franco**: El modelo está buenísimo, pasa que tiene Doctor tres.

**Valentín Torassa Colombero**: Claro, sin el modelo sí es realista pensar que puedo correr ahí, pero con el modelo tendría que ser Cloud el modelo, o sea, Cloud, no Cloud Atropic, sino Cloud Nube.

**Ariel Franco**: Sí, sí, sí. Para mejorar un poquito ahí los recursos que tiene. Prefiero un poquito menos de. De recursos, pero que sean más eficientes.

**Valentín Torassa Colombero**: Si lo jubilan al server y lo venden, no es mío, es del proveedor,

**Ariel Franco**: Seguramente le va a dar algún uso, pero bueno,

**Valentín Torassa Colombero**: soy de linda máquina.

**Franco Ferrero**: No tengo ni idea de qué están hablando. De algo que le gusta, como que

**Ariel Franco**: una copa horizontal con cuatro fuentes y sistema redundante, se frota una fuente, levantaba otra, entraba con.

**Valentín Torassa Colombero**: Entraba a venderle algo y le compraba algo.

**Ariel Franco**: Pasa, pasa, a veces pasa nada. Pero bueno. No, pásenos, pásenos todos los contratos legales, todas las. Adquiridos con esta gente de sistemas, porque también está la posibilidad de que si nosotros abrimos la puerta, vendo a traer nuestro. Ya nos pasó siempre en este hermoso proveedor que tenemos, que se te vuelve también un competidor porque cada puerta que abrimos vienen atrás un montón de gente, o sea, San Patricio fue siempre muy vanguardista en eso.

**Valentín Torassa Colombero**: Claro, claro. OK.

**Ariel Franco**: Ni nos replican todas las innovaciones y todos los avances que hacemos sin. Siempre vienen atrás nuestro como si fuéramos nosotros los early adopters de eso. Así que bueno, pásenos todo lo que tengan y lo vamos viendo, Lo vamos viendo. Si querés pasar y pásenme específicamente las descripciones de los niveles de seguridad que tienen para ti. No me digas, soy lo que escuché en mi vida. Pero si tenés la descripción, la hoja de datos o lo que fuera de la certificación que consiguieron, cómo la consiguieron, etcétera, etcétera.

**Valentín Torassa Colombero**: Dale. Sí, sí, te voy a pasar el reporte. El reporte tiene el informe de pentesting, evaluaciones que son de seguridad, de privacidad, así que si te das el tiempo de leerlo, aunque sea ojearlo, creo que te va a ser ilustrativo. También certifica ciertos procesos de desarrollo, así que puede ser interesante que le eches un ojo.

**Ariel Franco**: Dale, dale, dale.

**Franco Ferrero**: Bueno, muchas gracias.

**Ariel Franco**: No, por favor chicos.

**Valentín Torassa Colombero**: Gracias.

**Franco Ferrero**: ¿Lo pones en copia?

**Ariel Franco**: Dale, por favor.

**Valentín Torassa Colombero**: Buenísimo.

**Franco Ferrero**: Adiós.
