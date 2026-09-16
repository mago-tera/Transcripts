# Intro Teramot AI (Maximiliano Majul)

**Fecha:** 2026-08-21T10:00  
**Duracion:** ~27 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** majul.maximiliano@gmail.com, Agustin Garcia, Franco Ferrero  
**Externos:** majul.maximiliano@gmail.com  
**Archivo origen:** Intro Teramot AI (Maximiliano Majul) - 2026-08-21 10_00 GMT-03_00/Intro Teramot AI (Maximiliano Majul)_ 2026_08_21 10_00 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Evaluación de plataforma tecnológica y automatización para optimizar procesos comerciales.Objetivos y problemas inicialesReemplazo de procesos manuales mediante chatbot y resolución de bloqueos en la interfaz.Funcionalidades y gestiónCreación de lago de datos con segmentación por marcas y control de acceso.Automatización y eficienciaAutomatización de reportes diarios y optimización en el consumo de tokens.

### Decisiones

Acordada
Gestión de información multimarca definida La gestión de acceso a la información para múltiples marcas se realizará mediante la creación de 'workspaces' específicos para aislar los datos y restringir los permisos por unidad de negocio.
Estrategia de alertas y proactividad establecida Las alertas y funciones de proactividad se ejecutarán mediante orquestación externa o agentes personalizados, dado que no son una funcionalidad nativa de la plataforma Teram.
Actualizamos la sección Decisiones con tus comentarios.
Danos tu opinión: Útil o Poco útil

### Próximos pasos

[Maximiliano Majul] Probar herramienta: Realizar pruebas con la carga de archivos Excel en la plataforma. Evaluar los resultados para determinar la viabilidad del uso del producto.
[Maximiliano Majul] Compartir con gerente: Presentar la herramienta al gerente de sistemas de la empresa la próxima semana. Analizar aspectos técnicos del producto con el responsable del área.
[Maximiliano Majul] Coordinar reunión seguimiento: Programar un encuentro con el equipo de Customer Success para avanzar en la configuración funcional. Definir el alcance de la prueba de concepto o demo personalizada.

### Detalles

Antecedentes y objetivos de la reunión: Maximiliano Majul, gerente de control de gestión de un grupo automotriz y de motocicletas que opera más de 10 marcas, explica que el objetivo es reemplazar los procesos manuales actuales basados en Excel y Drive con un chatbot para la consulta de información (00:00:01) (00:03:25). Maximiliano Majul menciona que intentó desarrollar una herramienta similar utilizando Replit y Cloud, pero busca una solución más robusta y eficiente tras leer sobre las capacidades de Teramod (00:02:03).
Resolución de problemas técnicos en la interfaz: Durante las pruebas iniciales de importación de archivos de Excel desde el CRM, Maximiliano Majul experimentó dificultades para avanzar en la configuración de la herramienta (00:03:25). Franco Ferrero identificó que el problema se debía a la interfaz de la guía de "primeros pasos" que permanecía activa y bloqueaba la visualización del botón de continuar, indicando a Maximiliano Majul cómo cerrarla para proceder correctamente (00:04:39).
Funcionalidades principales de Teramod: Agustin Garcia describe que Teramod permite crear un lago de datos (data lake) mediante la ingesta de información desde diversas fuentes, como sistemas SAP, archivos Excel o conexiones ODBC, sin modificar los datos en los sistemas de origen (00:05:58). El sistema permite configurar recurrencias para mantener el lago de datos actualizado y facilita la conexión con Cloud para auditar datos, fusionar tablas y realizar análisis complejos (00:07:01).
Gestión de usuarios y niveles de acceso: El sistema admite diferentes roles de usuario, incluyendo los denominados usuarios "viewers", quienes no necesitan licencia de Cloud pero pueden acceder a reportes y utilizar el agente conversacional para consultar la información disponible. Los administradores pueden gestionar estos permisos a través de configuraciones específicas (00:08:33).
Aislamiento de información por marcas: Para gestionar la información de múltiples marcas dentro de un mismo grupo, Agustin Garcia explica que Teramod utiliza "Workspaces" para segmentar los datos (00:09:41). Esta estructura permite que los administradores asignen a los usuarios a espacios de trabajo específicos, garantizando que los gerentes de marca solo visualicen la información correspondiente a su unidad de negocio, aunque la fuente de datos original sea compartida (00:11:07).
Automatización de reportes diarios: Maximiliano Majul consulta sobre la posibilidad de automatizar el envío de reportes diarios que actualmente se gestionan manualmente por correo electrónico. Agustin Garcia confirma que es posible automatizar la generación de estos reportes dentro de Teramod, de modo que se actualicen y estén listos a la hora requerida cada vez que la información base se refresca (00:13:26) (00:17:32).
Proactividad y alertas en el sistema: Respecto a la necesidad de recibir alertas proactivas sobre desviaciones o problemas en los indicadores, Agustin Garcia aclara que, si bien Teramod no cuenta con una funcionalidad nativa de agendamiento de notificaciones, esto se puede orquestar externamente o mediante la integración con Cloud (00:14:58). Franco Ferrero añade que los usuarios pueden generar agentes y tableros en Cloud que se actualicen a diario para detectar anomalías basadas en umbrales específicos de manera automática (00:18:47).
Eficiencia en el consumo de tokens y costos: Maximiliano Majul expresa preocupación por el consumo de tokens, basándose en experiencias previas con otras herramientas. Agustin Garcia explica que Teramod es eficiente porque optimiza las solicitudes hacia el modelo de lenguaje mediante consultas SQL y la creación de "tablas gold", lo cual evita el reprocesamiento innecesario de datos y mantiene los costos fijos y predecibles frente a otras herramientas públicas que consumen más recursos (00:19:58) (00:22:29).
Pasos a seguir y soporte técnico: Maximiliano Majul tiene la intención de continuar probando la herramienta y planea involucrar al gerente de sistemas de la empresa en una etapa posterior (00:18:47) (00:23:40). Agustin Garcia y Franco Ferrero ofrecen apoyo del equipo de Customer Success, la posibilidad de realizar una demostración con datos reales bajo un acuerdo de confidencialidad (NDA), y la disposición de asistir con dudas técnicas durante el periodo de prueba mediante contacto directo (00:19:58) (00:24:40).

---

## Transcripcion

**Agustin Garcia**: Hola, Maximiliano, ¿cómo estás? Espera, espera que no te escucho. Dame un segundo. No sé si soy yo o si sos vos. A ver. No, esto. A ver, N. Eh, me parece que tenés algún tema con el micrófono. Puede ser, porque yo no te escucho. Hola, Franco. Espera que no lo estamos pudiendo escuchar a Maximiliano. No se escucha.

**Maximiliano Majul**: Por acá me escuchan.

**Agustin Garcia**: Ahora sí,

**Maximiliano Majul**: Entré con el celu para no sé qué pasó y estoy con la cámara y la compu, así que vamos por la doble.

**Agustin Garcia**: no te preocupes, no te preocupes, ¿eh? A veces pasa.

**Maximiliano Majul**: Está bien, está bien.

**Agustin Garcia**: ¿Cómo estás?

**Maximiliano Majul**: Todo bien, todo bien. Un gusto. Gracias, gracias por el tiempo y la y el momento.

**Agustin Garcia**: por favor.

**Maximiliano Majul**: Les cuento brevemente, digamos, cómo llegamos hasta acá.

**Agustin Garcia**: Dale.

**Maximiliano Majul**: Tú sois gerente control de gestión de una empresa de Córdoba Argentina. básicamente un concesionario automotriz y de motos que maneja más de 10 marcas,

**Agustin Garcia**: Eh,

**Maximiliano Majul**: digamos. Y yo venía pensando con una herramienta muy parecida eteram. De hecho, la había empezado como a desarrollar en replicit bastante amateurmente, digamos, donde básicamente lo que hacía yo era en este MVP, digamos, subirle distintas planillas de Excel o archivos que exporto del del CRM de la empresa o del RP y en base a una reg de negocio y otras cuestiones, me había conectado con Cloud a través de Replit y le preguntaba cuestiones y me volvía. Bueno, la verdad que que lo hice durante dos o tres semanas, ¿viste? si lo va encaminando, retrocede, viste, arriba, repid avanza, retrocede, digamos, y no me termina de cerrar algunas cosas siempre de un lado muy amate.

**Maximiliano Majul**: Yeah.

**Maximiliano Majul**: Yo no soy programador ni mucho menos, sino más bien un entusiasta. Y bueno, eh llegué a usted, digamos, por una nota que leí en info ae laa la del tío J, no sé si la la leyeron. Y bueno, y ahí dije,"Bueno, che, esto lo que estoy tratando de armar yo ya lo tienen desarrollado. Eh, voy también por este camino en paralelo para ver si si ya lo tienen resuelto y y me favorece." Entonces,

**Maximiliano Majul**: mi idea, digamos, como gente contente y gestión es un cambio de paradigma en el cual nosotros todo el tiempo vamos y volvemos con con algunos ex, con algunos drive, digamos, o nos piden alguna análisis, lo devolvemos. Yo quiero cortar un poco eso y que sea la consulta de información sea a través de un chatbot donde cada uno pregunte lo que tenga ganas de preguntar ese día y eh empiece empieza esa interacción de análisis no solo con con esa información, sino con todo lo que pueda aportar la la idea del mercado, ¿no? Entonces, por eso llegué hasta acá. Ayer justo estoy deoc semana,

**Agustin Garcia**: Bueno,

**Maximiliano Majul**: entonces le pude dedicar un tiempo y quise me bueno, me hice la cuenta, la vinculé cloud y demás y cuando estoy tratando de hacer algunas pruebas importando algunos Excel que saco del del CRM y cuando lo lo importo no si se queda ahí no no me como que no puedo seguir avanzando, digamos.

**Agustin Garcia**: que se queda trabado.

**Maximiliano Majul**: Mir, qui le comprar tu pantalla.

**Agustin Garcia**: A ver, por favor. Sí.

**Maximiliano Majul**: Bueno, creé el espacio, hice la vinculación a cloud, lo tengo acá en el en el desktop.

**Franco Ferrero**: Ok.

**Maximiliano Majul**: Cuando pregunto me dice que no encontré un archivo y lo que me está sucediendo es

**Agustin Garcia**: H

**Maximiliano Majul**: que cuando quiero subir un Excel común, digamos, es este, por ejemplo, aparece acá, pero no le puedo dar continuidad a

**Agustin Garcia**: Sí.

**Franco Ferrero**: No, mira, tenés que tocar la cruz ahí,

**Maximiliano Majul**: está.

**Franco Ferrero**: sacar la de los primeros pasos y bajar un poco,

**Maximiliano Majul**: Sí.

**Franco Ferrero**: ¿no? Tocar la cruz directamente de los primeros pasos. Cerr guía. Y ahí te va a aparecer el botón de continuar para cargar ahí a la abajo,

**Maximiliano Majul**: Ah,

**Franco Ferrero**: en la derecha.

**Maximiliano Majul**: mir salam paso que parer la guía

**Franco Ferrero**: Igual está bien lo que decís porque es algo que que ya lo tenía visto,

**Maximiliano Majul**: porque

**Franco Ferrero**: así que me viene bien el

**Maximiliano Majul**: Ah, bien, bien. Y otra cosa,

**Franco Ferrero**: recordatorio.

**Maximiliano Majul**: cuando se pone contacto al soporte, ¿ves? Cuando clicas, no no te da ahí un poco de bola, por eso carga el ticket. digamos otra otra

**Franco Ferrero**: Okay, perfecto. Sirve.

**Maximiliano Majul**: cuestión.

**Franco Ferrero**: Ya, ya lo mandó.

**Maximiliano Majul**: Bueno, una una consulta, digamos, esto que yo estoy pensando,

**Maximiliano Majul**: M.

**Maximiliano Majul**: digamos, ¿Ustedes creen que Teramo lo lo resuelve de alguna

**Agustin Garcia**: Sí, totalmente. Mira,

**Maximiliano Majul**: forma?

**Agustin Garcia**: un poco eh hoy cómo te explico rápidamente cómo funciona Teram. Eh, una lástima que ayer dimos justo un webinar

**Maximiliano Majul**: Lo vi, lo vi,

**Agustin Garcia**: e sí,

**Maximiliano Majul**: lo, o sea, no lo vi en vivo, pero lo vi el de control de finanzas. Claro,

**Agustin Garcia**: correcto,

**Maximiliano Majul**: porque cuando me pasó esto me puse a ver videos y lo vi, lo vi, lo vi. Yeah.

**Agustin Garcia**: fantástico. Bueno, porque básicamente ahí digamos eh en el en el webinar Bruno lo que hizo fue básicamente digamos conectarse a fuentes de datos y procesar la información. digo, está bien, Bruno hizo una prueba con lo que es un SAP. Sí, pero así como puedes conectar un SAP, puedes conectar tus Excel. Eh, no sé con con qué CRM, CRP trabajas, porque hasta inclusive lo puedes conectar directo. Algunos en particular, eh, si tienen una conexión ODBC, los puedes conectar directo. ¿Y cómo funciona? Digamos, funciona que Teram aparte, digamos que te permite armar un datalake, ¿sí?

**Agustin Garcia**: Entonces, lo que hace es ingestar la información de tus sistemas a Teramod. Sí. O sea, que no los toca, no toca el sistema de origen, la data no se modifica ahí la trae inclusive a ese a ese a ese a esa ingesta se le puede configurar una recurrencia para que ocurra, no sé, x cantidad de veces al día, lo que haga falta para mantener ese data lake, digamos, eh lo más actualizado posible. Entonces, una vez que vos tenés eso, digamos, a partir de ahí conectás Cloud por MCP y podés, digamos, desde auditar los datos, gestionar la información, mercha tablas, hacer los análisis que hizo Bruno, eh inclusive digamos eh todo lo que se te ocurra con los datos lo vas a poder hacer por medio de cloud. Inclusive creo que ayer Bruno también mostró cómo es la generación de reportes y la publicación, porque digamos vos también podrías generar un reporte, publicarlo y que el resto de la empresa acceda a ese reporte, digamos, eh ya generado. ¿Sí? Entonces eh y aparte también tenés la opción de el agente conversacional que te permite hacer un chat with your data, ¿sí? O sea, conversar con tus datos. Entonces, eh no sé, a veces digamos hay alguien en particular puede que tener alguna pregunta sobre los datos, va eh si ve el reporte, ve los datos, escribe en el chat y el chat le responde, ¿no?

**Agustin Garcia**: Eh, obviamente que Cloud es mucho más potente. Este es un motor, un Llm tiene conectado el sistema, que tiene está pensado más para chat with your data, no para eh digamos eh tal vez funciones tan complejas,

**Maximiliano Majul**: Claro. ¿Es

**Agustin Garcia**: ¿no? Pero básicamente la idea es esa,

**Maximiliano Majul**: es la primera opción y después escala o o es una elección que hace el usuario, digamos? M.

**Agustin Garcia**: ¿eh? Yeah. es una opción, digamos que vos tenés ahí la posibilidad de de acceder a la gente y conversar con los datos directamente. Lo tenés como opción.

**Maximiliano Majul**: sin que le

**Agustin Garcia**: ¿Qué te quiero? Claro, porque ¿cuál es el tema,

**Maximiliano Majul**: clamos.

**Agustin Garcia**: digamos? Vos eh digamos que en en en el modelo vos podés tener usuarios que estén conectados con Cloud y usuarios que no. Sí, porque por ejemplo vos que vas a estar gestionando la información, vas a tener eh conectado cloud por MCP con una licencia tuya de cloud, ¿no? Fantástico. Capaz que algún par tuyo, digamos, tal vez después le das a alguien de sistema también para que gestione, ponele, pero después tal vez hay otros gerentes que a lo mejor no tienen cloud y que quieren poder acceder a los datos.

**Agustin Garcia**: Bueno, esos son usuarios, nosotros les llamamos usuarios viewers. Sí. Entonces, esos usuarios viewers son los que pueden eh acceder a los reportes eh y o usar el chat eh la gente

**Maximiliano Majul**: Bien, bien,

**Agustin Garcia**: conversacional.

**Maximiliano Majul**: perfecto, lo entendí clarísimo. Tengo dos dos consultas. eh cómo debería manejar, digamos, acá al ser es como que es multimarca, hay gerentes, digamos, de cada marca, pero a su vez, digamos, la parte más de soporte de la empresa, digamos, está centralizada, o sea, gerente control de gestión, digamos, de todo el grupo, ¿cómo debería manejarlo para o administrarlo para que cada gerente pueda acceder el devolv a la información de Wagen, el devor la información y no y no que esté que estén pudiendo cruzarse esa esas preguntas, digamos?

**Agustin Garcia**: Fantástico. Mira, hay básicamente que lo que nosotros tenemos un esquema por workspace, ¿si? Entonces,

**Maximiliano Majul**: Sí.

**Agustin Garcia**: eh en estos casos vos vas a tener un Wordspace para Volkswagen, un Wordspace para cada marca, por ejemplo, y dentro de ese Worspage y es más, hasta inclusive puedes llegar a tener una segmentación un poco más eh atómica, por así decirlo, porque vos a lo mejor y bueno, capaz que en Volkswagen hay hay usuarios que tienen que ver cierta información y otros que no o que ven una información distinta y no por y y no el uno no tiene que verla del otro,

**Agustin Garcia**: por ejemplo, ¿no?

**Maximiliano Majul**: Ahí está.

**Agustin Garcia**: Entonces ahí tenés esquemas para armarlo, que te permiten generar aislar la información por marca o por unidad de negocio, por ejemplo,

**Maximiliano Majul**: Porque la fuente de información,

**Agustin Garcia**: ¿no?

**Maximiliano Majul**: si yo conecto el CRM, digamos, va a ser una una sola la misma, digamos.

**Agustin Garcia**: Sí,

**Maximiliano Majul**: Entonces, o sea, la configuración del de los permisos,

**Agustin Garcia**: sí,

**Maximiliano Majul**: digámosle, corre entera mod, o sea,

**Agustin Garcia**: claro.

**Maximiliano Majul**: ahí es donde yo empiezo a tratar de de decir, este responde solamente cosas de jugador, este solamente responde cosas.

**Agustin Garcia**: Es que claro, es que directamente el usuario de Volkswagen que va a estar el Wordspace de Volkswagen no va a ver la información de los otros, ¿entendés? Vos como usuario administrador sí la vas a ver, pero ellos no se entiende porque vos das invitación,

**Maximiliano Majul**: Está

**Agustin Garcia**: vos lo lo incluís, eh, Uh. en en lo incluís en en digamos en una en un workspace específico que solo tiene acceso a lo que está en ese workspace, ¿entiendes?

**Maximiliano Majul**: Pero pero es pero por eso digo yo ponerle entro al al sistema nuestro que es un sistema propio, saco factura en un periodo y me tira toda la facturación de grupo, digamos, porque soy el control de gestión.

**Maximiliano Majul**: Ahora el usuario de Ford solamente le deja seleccionar la marca FOR.

**Agustin Garcia**: Sí.

**Maximiliano Majul**: ¿Cómo llevo? O sea, pero digamos la fuente de información es es la misma. En el Wordspace hago la configuración para que no se crucen las

**Agustin Garcia**: Ah, ya te entendí.

**Maximiliano Majul**: marcas.

**Agustin Garcia**: Vos tenés en la fuente de datos original tenés toda la información,

**Maximiliano Majul**: Claro,

**Agustin Garcia**: ¿no?

**Maximiliano Majul**: claro.

**Agustin Garcia**: Entonces, lo que vos tendrías que hacer ahí, que lo podés hacer incluso con cloud, eh vos lo que tendrías que hacer ahí es ingestar la información completa y después, por ejemplo, distribuís esa información. Es más, habría que tal vez habría que inclusive depende cómo sea la fuente, eh, vos la podés ingestar directo. Si se puede filtrar el origen, se filtra el origen y vos la a cada Wordspace le importás lo que le corresponde. Y si no, te traes todo a un Wordspace en particular. Y lo que haces ahí es ponemme en el Wordpace tal la información de Volkswagen, ponemme en el WordPace tal información de tal marca, ¿se entiende? Y va seccionando la información. No es que la fuente es una, porque como están eh digamos esquematizados los permisos el en el

**Franco Ferrero**: M.

**Agustin Garcia**: Wordspace, eh inclusive hoy hay una funcionalidad nueva que no sé inclusive si no te permite ese nivel de granularidad, pero a priori te diría se puede, sí se puede y creo que hasta pueden haber varias estrategias para hacerlo, así que eh sí se puede hacer eso.

**Maximiliano Majul**: Bien. Y y una una consulta más, nosotros eh todos los días, digamos, mandamos una información diaria que le decimos, ¿no?, que básicamente es un Excel que va a pegar a un mail, digamos, que tiene información clave de del acumulado al acumulado de hábiles y lo que está pasando en los meses anteriores.

**Agustin Garcia**: Sí.

**Maximiliano Majul**: Esa información nosotros no hacemos nada, digamos, llegamos por un programa, se aloja una carpeta y se manda por mail, digamos, no no pasa más que eso. que,

**Agustin Garcia**: Sí.

**Maximiliano Majul**: o sea, yo esa ese tipo de información la debería, o sea, obviamente conectar conectar el ter a a las fuentes y después dejar predeterminado de alguna forma esa misma esquema o modelo para que cuando el usuario inicie digamos le figure ese esa información. Esa es la forma de proceder.

**Agustin Garcia**: Sí, digamos, hasta inclusive se puede generar cierto automatismo para que, no sé, digamos, hasta hoy con algún motor que se los reportes se generan automáticamente y se actualizan cuando se actualiza la información de base.

**Agustin Garcia**: Entonces,

**Maximiliano Majul**: M.

**Agustin Garcia**: el reporte te lo tenés armado todos los días a la hora que necesitas con la información correspondiente, ¿no? Después eh digamos el la metodología envío y mira,

**Maximiliano Majul**: Yeah.

**Agustin Garcia**: hay varias opciones que eso tal vez lo podríamos ver en una reunión más técnica, pero digamos sí, porque tenemos un montón de clientes que con esto arman sistema de notificación, de quiebres de stock, de de no sé de x cantidad de cosas en distintas industrias. Así que en ese sentido habría que ver en detalle un poco el caso de uso, pero pero sí es

**Maximiliano Majul**: Bueno, y una una consulta más,

**Agustin Garcia**: posible.

**Maximiliano Majul**: yo tengo la intención, digamos, que que que el que todo esto sea de una forma proactivo, ¿no? O sea, que que cuando el usor inicie lo pueda ir alertando de de algunos desvíos o de algunas cuestiones que que no están funcionando del todo bien y y no siempre sea preguntando ese esa proactividad, digamos, eh la la da la va a dar la va a dar cl, digamos, o la da Teramod o se configura dentro de Teramod como lo tienen pensado forma.

**Agustin Garcia**: Eh, No sé si Teramo tiene un sistema de de de agendamiento, la verdad que ahí me mataste con esa pregunta, pero digamos te diría que a priori eso tendrías que orquestarlo por fuera, ¿entendés?

**Agustin Garcia**: Con algún gente, con algún digamos el LLM, con Cloud, digamos, porque digamos eh lo que hace esto es se corren procesos sobre la data, ¿entendés? Y vos eso lo podés automatizar, pero de tu lado, ¿entendés? No es no es una funcionalidad propia de Teramot,

**Maximiliano Majul**: Claro,

**Franco Ferrero**: Eso.

**Maximiliano Majul**: o sea,

**Franco Ferrero**: A

**Agustin Garcia**: ¿entendés?

**Maximiliano Majul**: debería subirle tablas de de metas,

**Franco Ferrero**: ver.

**Maximiliano Majul**: o sea, tengo la información real, digamos, de nuestra base, debería subir tablas de metas, digamos, y si la cuestión de desvís sería vía chat indagación, digamos, o generando algún reporte diario más o menos

**Agustin Garcia**: No, pero lo que no, bueno,

**Maximiliano Majul**: alerta.

**Agustin Garcia**: pero ahí digamos tal vez no no te estoy entendiendo bien, pero digamos vos tenés eh la información, si vos la tenés en una base de datos la información o en un Excel tal vez y ese Excel digamos se puede lograr un acceso directo para que Teramot lo ingeste regularmente. eh como no sé, ponerle un Google Sheet o algo así, digamos, la información se ingesta y cada vez que se ingesta se genera una actualización y cuando se actualiza se actualiza el reporte, ¿entendés?

**Agustin Garcia**: Entonces, cuando entra el usuario ya lo puede ver, digamos, eh eh en ahora si hay que enviar un mail o algo, ¿entendés? algún tipo de notificación o alerta, eso se puede, digamos, orquestar hoy muy fácilmente, pero no es una funcionalidad de Teramot. Teramot es lo que te permite tener el reporte listo ahí.

**Maximiliano Majul**: Perfecto. No.

**Agustin Garcia**: Nada, yo nosotros somos del área comercial, eh, si vas a hablar con el equipo, nosotros tenemos un equipo de customers. su que trabaja, digamos, en el onboarding y en el acompañamiento de los clientes. ¿Sí? Entonces, seguramente tenés una reunión con ellos y te va a decir,"Ah, sí, mira, p lo puedes hacer así, tu tuú, ¿entendés?" Como esto es la forma más eficiente, menos costosa, porque la tienen supercara, eh, digamos, eh, pero bueno, sí son casos bases, digamos, en ese sentido, digamos, pensar que la información se actualiza eh con la recurrencia que vos le configuras a la ingesta de datos, ¿entendés? Entonces, eh después se actualizan los reportes y después lo que vos necesites.

**Maximiliano Majul**: Perfecto.

**Franco Ferrero**: Ahí Un poco lo que se me ocurre también es que vos una vez que ya tenés la ingesta de datos que se actualiza a diario en Teramot, tanto sea desde Meta o o sean tus Excels, que se actualicen,

**Maximiliano Majul**: por

**Franco Ferrero**: vos desde cloud podés generar si querés dashboard que se te van actualizando también a diario para

**Maximiliano Majul**: ahí.

**Franco Ferrero**: poder ir viendo si querés esas métricas que vos decís,"Che, acá puedo llegar una alerta." Y también desde cloud vas a poder permitir que le decís que genere un agente que se actualice a diario y que a la mañana te diga si detecta alguna alerta o no. Entonces en base a eso se va a actualizar la mañana en base a las tablas limpias de Teramot. Y desde ahí vos vas a decir,"Che, bueno, acá tengo una alerta, acá

**Maximiliano Majul**: Claro,

**Franco Ferrero**: no.

**Maximiliano Majul**: en base al desvío de tanto por cento tiramos una Perfecto, perfecto.

**Agustin Garcia**: Exacto.

**Maximiliano Majul**: Eh, bien, bien. Eh, bueno, digamos, yo estoy como buceando un poco la herramienta, digamos, estoy aprovechando que tengo unos días libres y la verdad que me gusta la idea, de alguna forma la tenía pensada de antes y la vi resuelto un poco entera mod. Voy a estar probando la herramienta y si veo buen resultado, digamos, estaré más en contacto con ustedes, digamos.

**Agustin Garcia**: Totalmente. Y otra cosa que también con lo que podés contar es podés contar con hacer una probar la herramienta, jugá, fíjate, digamos, recién ahora vas a poder ingestar el Excel, ¿no?

**Agustin Garcia**: Entonces, eh pero hac todas las pruebas y yo lo que te sugiero, si querés, ponerte en contacto con Franco, conmigo y podemos coordinar una reunión con el equipo de de Customer Succes para que vos tengas una reunión y veas un poco, les contás eh y ellos te puedan ayudar con con digamos tanto con lo funcional, me imagino que con el tema de promteo, ¿no? Pero digamos lo que lo que te haga falta para lograr lo que necesitas lograr.

**Maximiliano Majul**: Bien, y una una última consulta, el consumo de de token, digamos, ¿cómo juega ahí digamos cuando cuando es el chat de Teramot? Digamos, entiendo que no hay consume token, es como una consulta tipo, no sé, CQL y ya cuando va entra cloud, entra en el sistema de cloud, digamos.

**Agustin Garcia**: Eh, el agente interno en las versiones más bajas tienes está limitado, digamos, obviamente que en los planes más más enterprise tiene otro nivel de alcance. De todas maneras puedes hacer muchas cosas.

**Maximiliano Majul**: M.

**Agustin Garcia**: Sí, está incluido en el plan. Eh, nosotros usamos Cloud porque Cloud es superpotente. Ahora, digamos, ¿cuál es la gran ventaja que tiene Teramot aparte de todo esto que estamos viendo? La gran ventaja que tiene Teramot también es la posibilidad de interactuar con un Ll y de forma eficiente también, ¿no?

**Agustin Garcia**: Y poder traducir los los las solicitudes en en Queries XM, en querer SQL, que son super performantes, ¿entendés? Entonces, digamos, hay otros productos de mucha menor escala, pero que son públicos. No sé, Sup, por ejemplo, te conectas a la base de datos con eh cloud, fantástico. El problema es que te come vivo con los tokens, ¿entendés? No es tan eficiente. Entonces, acá la verdad que no nosotros eh aparte es una es una es una consulta recurrente. ¿Por qué? Porque digamos vos contrataste. Fantástico. Bueno, yo te doy un precio y digamos que te digo, las variables puede ser estas, vos se monitorea. Es más, hasta me puede decir,"Che, eh, no, que no se pase esto, fantástico, no hay problema." Entonces, el costo es fijo, predecible. Vos en el tema de tokens, bueno, sí, si tenés el plan de de de de 20 o de 100, vas a lo sumo tendrás que esperar un rato, pero las empresas que tienen los las cuentas Enterprise, ¿entendés? Siempre el miedo está en,"Che, pará, esto me recontracome los tokens y no, la verdad que no, no tienen que ser operaciones. Consume,

**Agustin Garcia**: sí consume, pero digamos la integración con Teram Teramot es tan eficiente que no es algo entend

**Maximiliano Majul**: Claro. Sí, sí,

**Agustin Garcia**: que si lo matas obviamente consume más,

**Maximiliano Majul**: sí. Digamos, es clave, digamos, que interprete bien el mejor.

**Agustin Garcia**: pero no a priori te diría que no es algo grave.

**Maximiliano Majul**: Claro, porque cuando yo estaba hablando esta herramient, digamos, lo que pasó era eso, por ahí no terminaba de interpretar bien la información, entonces iba y volví volvía con consulta y en ese bar de cl, viste, me comía vivo, digamos.

**Agustin Garcia**: y bueno que es un poco es un poco lo que pasa. Entonces ahí esa es una de las ventajas competitivas también que tiene el producto, ¿entendés?

**Maximiliano Majul**: Claro.

**Agustin Garcia**: Que es la eficiencia en la integración con el LLM para que vos digamos no te coma vivo, ¿entendés? Eh, nada. Y también pensar que bueno que eh son también de acuerdo a a al tipo de de consumo que hagas. Vos pens que cuando vos generás un reporte o sacá cierta información, eh es se genera una tabla gold, ¿sí? Que básicamente lo que hace es hace la extracción de los datos y la deposita y después ya trabaja sobre los datos, ¿entendés?

**Agustin Garcia**: estadísticamente, o sea, no no hace otra proceso, otro otra otra creación que a lo mejor es un una operación de de más consumo, ¿se entiende? El resto es más analítico, ¿no? No. Y las consultas sobre los datos están superficadas para que,

**Maximiliano Majul**: Sí, sí. Perf.

**Agustin Garcia**: ¿entendés?

**Maximiliano Majul**: Yeah.

**Maximiliano Majul**: M.

**Agustin Garcia**: No es que le devuelve un un dataset completo, que eso es lo que pasa en otros con otros productos, que entonces te comes vivo porque vos cada cosa que le pasa media tabla y bueno, claro, te vas a quedar en en una hora te quedaste o menos, te quedaste sin tokens, ¿entendés? Entonces ahí eso es uno de los de las ventajas también que tiene el producto que está pensado para para ser eficiente.

**Maximiliano Majul**: Perfecto,

**Agustin Garcia**: Sí.

**Maximiliano Majul**: perfecto, perfecto. ¿Qué hablar? Eh, bueno, yo voy a salir, digamos, hoy tengo para para probarlo.

**Agustin Garcia**: Bueno,

**Maximiliano Majul**: Semana que viene seguramente también se lo comparte un poco el gerente sistema de la empresa para ver qué cuestión más técnica pueden llegar a surgir y seguemos en contacto. No.

**Franco Ferrero**: Dale.

**Agustin Garcia**: buenísimo. Ahí lo que necesites, avisanos y estamos. Y es más, si querés que hagamos una presentación con el gerente de sistemas, eh, también nosotros siempre lo que lo que hacemos generalmente es hacemos una demo con datos de de ustedes, ¿entendés? No necesariamente tienen que ser datos reales o en algunos casos la gran mayoría nos pasa muchas

**Maximiliano Majul**: Eh,

**Agustin Garcia**: veces firmamos en DA,

**Maximiliano Majul**: no pasa nada.

**Agustin Garcia**: pero ¿qué pasa ahí? Cuando vos podés ver, digamos, realmente la potencia de esto, eh, que que nada, viste, la verdad que cuando en las áreas de control gestión, no sé, un reporte de auditoría cuentas a pagar, lo hacemos en un rato y no lo pueden creer, ¿entendés? Como que chao, ¿entendés? Como que bueno, el reporte se hace en una hora. y ponerle que toman, no te voy a mentir, pero toman dos tr horas para validar que la información del reporte esté, digamos, eh correcta, o sea, que sea, digamos fidedigna. Y hay empresas que destinan trimestralmente 200 horas para armar ese tipo de

**Maximiliano Majul**: Sí, sí, sí, sí. Olvídate acá.

**Agustin Garcia**: reportes.

**Maximiliano Majul**: Seguro. Yo no estoy en esa parte, digamos, porque más de finanza, pero pero seguro,

**Agustin Garcia**: Claro, claro. Entonces, bueno, toda esa parte,

**Maximiliano Majul**: digamos.

**Agustin Garcia**: bueno, el ahorro es importante, ¿viste? Entonces, eh nada, fíjate lo que necesites. Avisanos si querés una reunión con el equipo de customer o si querés una demo con alguien más de la empresa o si quieren hacer una una demo con o una prueba concepto con datos de ustedes también bienvenido sea eso no sin ningún problema.

**Maximiliano Majul**: Perfecto, perfecto.

**Franco Ferrero**: Eso

**Maximiliano Majul**: Con seguridad vamos a avanzar una reunión asíamos un poco

**Agustin Garcia**: Buenísimo. Bueno,

**Maximiliano Majul**: más.

**Franco Ferrero**: para te dejé mi número por si por si estás haciendo pruebas hoy y te surgen

**Agustin Garcia**: fantástico.

**Maximiliano Majul**: Dale.

**Franco Ferrero**: dudas,

**Maximiliano Majul**: WhatsApp.

**Franco Ferrero**: preguntá también porque nos sirve también como feedback y para ir viendo cosas que capaz no entendés. Así que cualquier cosa me

**Maximiliano Majul**: Perfecto. Buenísimo.

**Franco Ferrero**: escribís.

**Maximiliano Majul**: Buenísimo. Muchísimas gracias. Muy amable.

**Agustin Garcia**: Gracias a vos,

**Maximiliano Majul**: Muchas gracias.

**Agustin Garcia**: Maxi. Que estés muy bien.

**Maximiliano Majul**: Igualmente,

**Franco Ferrero**: Chao.

**Maximiliano Majul**: muchas gracias.

**Agustin Garcia**: No.

**Franco Ferrero**: No.

**Maximiliano Majul**: M.
