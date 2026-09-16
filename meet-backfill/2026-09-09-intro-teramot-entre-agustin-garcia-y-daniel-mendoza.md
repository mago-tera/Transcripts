# Intro-Teramot entre Agustin Garcia y DANIEL MENDOZA

**Fecha:** 2026-09-09T13:00  
**Duracion:** ~47 min  
**Fuente:** Google Meet (Gemini)  
**Participantes:** danielitoleito@gmail.com, Agustin Garcia, Franco Ferrero  
**Externos:** danielitoleito@gmail.com  
**Archivo origen:** Intro-Teramot entre Agustin Garcia y DANIEL MENDOZA - 2026-09-09 13_00 GMT-03_00/Intro-Teramot entre Agustin Garcia y DANIEL MENDOZA_ 2026_09_09 13_00 GMT-03_00 - Notas de Gemini.docx

---

## Notas de Gemini

### Resumen

Evaluación de Teramot para la gestión de datos agrícolas con definición de arquitectura y costosDefinición y uso de TeramotPresentación de Teramot como plataforma de datos con inteligencia artificial para optimizar la gestión comercial agrícola.Demostración y arquitectura técnicaExhibición de integraciones, arquitectura de datos en tres niveles y paneles automatizados.Modelo de costos y cierreRevisión del esquema de precios por usuarios y tablas, concluyendo con la solicitud de propuesta comercial.

### Próximos pasos

[Franco Ferrero] Enviar información de planes: Enviar información de planes y estructura de precios de Teramot, incluyendo detalles sobre el consumo de tokens y costos por usuario.

### Detalles

Intereses de migración de CRM y definición de Teramot: Daniel Mendoza expone el problema de buscar una alternativa a HubSpot que sea flexible, intuitiva, escalable y compatible con correos institucionales (00:00:03). Agustin Garcia aclara que Teramot no funciona como un CRM, sino como una plataforma de datos impulsada por inteligencia artificial que consolida diversas fuentes de información para gestionarlas mediante modelos de lenguaje grande (LLM) como Claude, ChatGPT, Gemini o Copilot (00:04:32).
Aplicación en el sector agrícola y alimentario y problemática de gestión: Daniel Mendoza describe su modelo de negocio enfocado en la representación de laboratorios internacionales agroindustriales (pesticidas y contaminantes) y un laboratorio propio de microbiología y físico-química en Ecuador. Daniel Mendoza señala como problema principal el desgaste operativo y la falta de tiempo para dar seguimiento oportuno a más de 100 productores bananeros y 350 camaroneros con un equipo reducido de dos o tres personas (00:08:54). Agustin Garcia explica que Teramot permite conectar sistemas, descargar datos y utilizar LLMs para identificar clientes sin contacto en los últimos 8 meses y automatizar la creación de mensajes promocionales como borradores en Gmail (00:10:24).
Estructura organizacional para el uso de la plataforma: Daniel Mendoza consulta si la herramienta debe manejarse centralizadamente o de forma individual (00:13:33). Agustin Garcia propone una estructura de tres niveles: la parte estratégica a cargo de Daniel Mendoza, la operativa para cruzar datos y gestionar Teramot, y la ejecutiva para el equipo de ventas (00:14:58). Ante la observación de Daniel Mendoza sobre el uso de archivos manuales de facturación y Excel, Agustin Garcia indica que Teramot permite importar archivos o conectar sistemas mediante API para interpretar automáticamente los modelos de datos (00:16:47).
Demostración de conexiones y arquitectura de datos: Franco Ferrero comparte pantalla para mostrar el espacio de trabajo de Teramot, evidenciando integraciones disponibles como Azure, SharePoint, OneDrive y HubSpot (00:19:18). A petición de Daniel Mendoza sobre la distinción de tablas, Franco Ferrero y Agustin Garcia detallan la arquitectura de datos: bronce (ingesta inicial), silver (tablas estructuradas con metadatos) y gold (tablas curadas para cumplir objetivos analíticos específicos) (00:31:58).
Modelo de costos, licencias y consumo de tokens: Daniel Mendoza pregunta por las limitaciones y costos de los reportes. Agustin Garcia detalla que el esquema de precios de Teramot se limita a la cantidad de usuarios y tablas gold utilizadas, sin incluir las licencias de Claude o ChatGPT (00:24:18). Agustin Garcia y Franco Ferrero agregan que el conector MCP de Teramot optimiza la comunicación con los LLM para reducir el consumo de tokens, sugiriendo el plan de $20 de Claude o un plan superior de $100 para usuarios con alta intensidad de uso (00:26:54) (00:37:15).
Control de información y visualización de paneles en Teramot: Daniel Mendoza destaca su preferencia por Teramot al ofrecer un entorno independiente y privado para el control de los datos empresariales en comparación con plataformas públicas (00:29:19). Franco Ferrero realiza una demostración práctica de la generación automática de paneles (dashboards) a partir de tablas gold, exhibiendo métricas simuladas de oportunidades abiertas, valor de cartera, facturación, morosidad por sucursal y días de mora (00:30:47) (00:38:50).
Cierre y solicitudes de información presupuestaria: Daniel Mendoza comenta que conoció Teramot a través de una búsqueda de agentes rápidos de procesamiento de datos y un anuncio en internet (00:43:18). Daniel Mendoza solicita formalmente a Franco Ferrero que envíe por correo electrónico la información detallada de los planes de inversión, costos por usuario y referencias sobre el consumo de tokens para evaluar la adopción de la herramienta. Franco Ferrero acepta la solicitud de envío de documentación formal y ambas partes se despiden (00:44:34).

---

## Transcripcion

**Franco Ferrero**: ¿Cómo?

**Agustin Garcia**: Es el R Ay, ay. Vamos a ver si

**Franco Ferrero**: Vamos. A ver. Ah.

**Agustin Garcia**: Hola, Daniel,

**Daniel Mendoza**: Hola,

**Agustin Garcia**: ¿cómo estás?

**Daniel Mendoza**: ¿qué tal? Muy buenos días. ¿Cómo están, chicos? Disculpen la demora de 4 minutos, pero estaba en una pequeña reunión.

**Agustin Garcia**: No hay ningún problema. ¿Cómo anda todo?

**Daniel Mendoza**: Bien, gracias a Dios.

**Franco Ferrero**: ¿Cómo está?

**Daniel Mendoza**: Muy bien, muy bien.

**Agustin Garcia**: Qué bueno.

**Daniel Mendoza**: A ver,

**Agustin Garcia**: No.

**Daniel Mendoza**: vi Teramot en una publicación, le estuve leyendo qué es lo que estoy tratando de ver o hacer. Estoy tratando de migrar de haspot y ver otras alternativas que vayan de la mano con correos institucionales, que sea un poco más flexible, amiguero,

**Franco Ferrero**: Esto. M.

**Daniel Mendoza**: intuitivo y que de verdad sea para principes, o sea, escalable el tema, que sea en realidad escalable. Okay,

**Franco Ferrero**: Ok.

**Daniel Mendoza**: primero háblenme un poquito más. Déjame recordar su página. Dame un ratito,

**Agustin Garcia**: M.

**Daniel Mendoza**: déjame recordar su página para más o menos No estaba eh queriendo abrir cualquier CRM y compararlo o cualquier alternativa.

**Daniel Mendoza**: Ya, por favor, consígueme eso. Ya, háblenme un poquito de lo de lo de ustedes. Okay.

**Agustin Garcia**: Buenísimo.

**Daniel Mendoza**: reportes.

**Agustin Garcia**: Mira, te te cuento muy rápidamente. Nosotros no somos un CRM,

**Daniel Mendoza**: Okay,

**Agustin Garcia**: nosotros somos una plataforma de datos con inteligencia artificial.

**Daniel Mendoza**: perfecto.

**Agustin Garcia**: Sí.

**Daniel Mendoza**: Qué bacán, qué bacán.

**Agustin Garcia**: ¿Qué te permite esto?

**Daniel Mendoza**: Mejora.

**Agustin Garcia**: Básicamente, Teramot lo que te permite es consolidar tus distintas fuentes de datos, ¿sí? Eh, para poder unificar la información y después poder gestionarla y explotarla por medio de inteligencia artificial. Esto, ¿qué significa? que básicamente tú en en tu entorno puedes tener, así como me cuentas que tienes hotspot, puedes tener hotspot, puedes tener un IRP, puedes tener, no sé, un sistema, digamos, eh de parte de la gestión comercial, de la gestión operativa, el control de gestión de tu empresa, donde esa información se ingesta en Teramot y Teramot lo que te permite es trabajar sobre la información por medio de un Ll inteligencia. artificial que utilices, que puede ser clotch, GPT, Gemini o Copilot. ¿Sí? Entonces,

**Daniel Mendoza**: Mhm.

**Agustin Garcia**: ¿eso qué te permite? Te permite que, bueno, primero hacer análisis, automatizar análisis, generar reportes, dashboard, digamos, hoy lo que haces con Power BI, click tabló lo puedes hacer eh casi automáticamente con eh digamos con cualquier LLM. inclusive, pues, el dashboard y publicarlo automáticamente para que el resto de tu empresa o un grupo selecto de usuarios pueda verlo. Ese dashboard se actualiza a medida que las distintas fuentes de datos se van actualizando y básicamente todo lo que tiene que ver con la gestión de los datos y la información de reportería que se que se que utilizas se puede casi automatizar en un porcentaje altísimo,

**Daniel Mendoza**: una una consulta,

**Agustin Garcia**: ¿no? Sí.

**Daniel Mendoza**: si esto lo puedo traspolar para el equipo comercial y ellos están usando HPOT o cualquier otra, ellos pasarán la información acá y es posible que les genere algún tipo de reporte hacia pérdidas de ventas, consolidación de ventas, embudo de ventas o en este caso eh porcentaje de captación.

**Agustin Garcia**: Todo puedes hacer todo porque digamos que Teramot tiene una conexión MCP que ese MCP se conecta a digamos eh eh tu suponente cloud, ¿no? O chatpt. Entonces, digamos, a su vez eh Teramot tiene una conexión con con Hotspot y tiene una y aparte Cloud tiene una conexión con hotspot.

**Agustin Garcia**: Nosotros inclusive hoy en día usamos así nuestros RM. Entonces, tú puedes extraer la información de HPOT y sacar información constante, digamos, eh, y actualizar la información vía el MCP. Y eso lo puedes volcar a Teramot y viceversa. E inclusive si tú tienes otro sistema que tenga información relacionada con la venta,

**Daniel Mendoza**: Claro.

**Agustin Garcia**: puedes mezclar la información y puedes aprovechar. Inclusive si tú necesitas hacer una migración de hotpot a otro sistema, podrías por medio del MCP, del LLM, podrías descargar los datos a Teramot temporalmente y después crear en el nuevo CRM los eh las distintas oportunidades en el el en la fase que estaba cada una. Sí. inclusive también crear las entidades correspondientes, que pueden ser los contactos, los deals, eh eso es algo que digamos hoy lo puedes hacer.

**Daniel Mendoza**: De acuerdo. De acuerdo. Okay. A ver, entonces ya voy entendiendo. Esto me va a servir como un motor de reportaje de integración de áreas. Okay. Okay. Y se puede interrelacionar en cualquier tipo de sistema que actualmente use.

**Agustin Garcia**: Exacto. ¿Tú en qué industria estás trabajando?

**Daniel Mendoza**: A ver, eso, eso te iba a explicar un poquito. Mira, la empresa donde que comando, en la cual soy dueño, nosotros tenemos eh representaciones con laboratorios internacionales para el sector agro, básicamente en esto que sería pesticidas y contaminantes.

**Daniel Mendoza**: ¿Okay?

**Agustin Garcia**: H

**Daniel Mendoza**: Aparte yo tengo un laboratorio propio de microbiología y físicos y químicos.

**Franco Ferrero**: M.

**Daniel Mendoza**: O sea,

**Agustin Garcia**: Mhm.

**Daniel Mendoza**: estoy en la parte agrícola y en la parte alimentaria.

**Agustin Garcia**: Mhm.

**Daniel Mendoza**: Mi interacción con clientes básicamente son eh productores o exportadores del Ecuador, ya sea de cualquier tipo de fruta, verdura y también para producción eh nacional para proteger inocuidad alimentaria. Entonces, ¿cuál es el tema? Yo tengo una problemática en este momento de recuperación de clientes. Okay.

**Agustin Garcia**: Hm.

**Daniel Mendoza**: Este tema de la pandemia para mí fue un poquito complicado. Aparte estoy teniendo bastante interacción con laboratorios internacionales. Entonces no tengo un equipo de ventas tan amplio como para captar los

**Agustin Garcia**: He.

**Daniel Mendoza**: casi aquí en el Ecuador 100 y algo productores que están bajo certificación. Eso solamente en el agro, en banano, pero eh en Camarón hay casi 350 que votan lotes semanales. O sea, llegar a entender a esta a todo este nicho es bastante complejo si lo manejo con dos o tres personas. Entonces, se me come demasiado tiempo el seguimiento oportuno de cuándo tengo que llegar a tiempo. Okay. Entonces, yo puedo tener en este momento la atención a estos clientes, pero pasa que el siguiente mes tengo que atender a de estos y estos de atrás, ¿cómo me les doy el tiempo?

**Daniel Mendoza**: porque me desgasto mucho en tema operativo.

**Agustin Garcia**: Claro.

**Daniel Mendoza**: Entonces,

**Franco Ferrero**: Ok.

**Daniel Mendoza**: una de un es el tema operativo desgastante, la interacción con el cliente y alguien que le dé el seguimiento, porque a estas alturas tendría que hacer un pequeño descreme. A estas alturas, si yo estoy cada mes atendiendo nuevos clientes y dejando pasar por atender a nuevos, digo, ¿qué qué me está dando la alerta de decir, oye, este cliente lleva acumulado contigo tanta cantidad de venta, tiene la prioridad sobre el otro? ¿Ves?

**Agustin Garcia**: Claro, claro.

**Daniel Mendoza**: Es eso, eso. O aumentar más la estructura laboral y salarial.

**Agustin Garcia**: E es clarísimo el escenario que tenés. Mira, la realidad es que hoy todo esto eh lo puedes hacer eh digamos eh conectando tu Ll a a Hpot, a Teramod, descargar la información en Teramod. Inclusive también podrías eh conectar, si hiciese falta por medio de Apolo, que es un una herramienta que te permite, digamos, nutrir de información eh digamos eh tus datos, información de los prospectos. Sí,

**Daniel Mendoza**: Aha.

**Agustin Garcia**: como para que tú puedas inclusive en lo que puedes hacer aquí es de cuando tú conectas los distintos sistemas, eh, absorbes del CRM la información, la descargas en Teramot, en Teramot, la trabajas con el LLM, con cloud, con chatt, haces un análisis de cuáles son los clientes que no has contactado, no sé, pongo un ejemplo, ¿no?

**Agustin Garcia**: Después hay que ver los casos de uso puntuales, ¿no? No. en función de tu CRM, cuáles son los clientes con los que no has tenido contacto en los últimos 8 meses. Fantástico, listo, te sale una lista. tú ahí puedes eh armar, decir,"Bueno, estos clientes segmentámelos de por tal y tal eh criterio y a estos clientes les quiero ofrecer tal y tal cosa." Inclusive hasta podrías también si descargas toda la información podrías eh identificar eh si ya le ofreciste el producto o no, si eh se entiende.

**Daniel Mendoza**: Así es.

**Agustin Garcia**: Inclusive tenemos clientes que lo que hacen son análisis cruzados en términos de decir, bueno, yo quiero hacer una campaña comercial y promocional para este producto en particular, ¿no? Entonces básicamente ahí lo que puedes hacer es decir, bueno, ¿cuál sería mi cliente ideal? ¿No? Y por ejemplo, si tú también ya tienes tu IRP eh interno o algún sistema o si lo llevas en Excel porque Teramot, aparte de poder conectarse a distintas fuentes, también puede conectarse a a a Excels. Se le pueden cargar los Excel o referenciar si lo tienes en algún sistema online,

**Daniel Mendoza**: Bueno,

**Agustin Garcia**: alguna nube. Entonces, haciendo, levantando la información que tiene, puede hacer la comparativa de eh mira, este producto se lo estás eh comercializando a empresas de este tipo, entonces te segmenta los los prospectos para que vayas directamente a armar ese esa esas esas esos mensajes de de promoción.

**Agustin Garcia**: Ahora, inclusive si tú tienes todo conectado, esos mensajes de promoción se pueden armar automáticamente, te los deja guardado en tu Gmail como draft para que tú entres, lo revises y lo envíes, ¿no? Entonces, todo esto, digamos, es algo totalmente orquestable. Eh, Teramot sirve para consolidar la información de los distintos sistemas y hacerte de base, porque, por ejemplo, Hpot tiene mucha potencia, pero le falta información, digamos,

**Daniel Mendoza**: Es correcto.

**Agustin Garcia**: no te falta toda la otra parte de esto, ¿no? Entonces, eh eso yo creo que es una de las posibilidades que podrías aprovechar con esto, eh, y eh podrías, digamos, ganar eficiencia y productividad para no tener que ampliar, digamos, el personal.

**Daniel Mendoza**: Una consulta, ¿esto podría ser manejado más eficientemente por cada uno de los interactores comerciales más el gerencial o debería estar centralizado? ¿Dónde tú crees que estaría la mayor productividad?

**Agustin Garcia**: Mira,

**Daniel Mendoza**: ¿Que una sola persona dirija y concierte a los demás? Vamos por aquí. ¿Y lo entiende muy bien o cada uno en individual bajo su perspectiva?

**Agustin Garcia**: mira, yo en mi opinión y y viendo cómo funcionan varios de nuestros clientes Antes vos tenés como dos tres patas, te podría decir. Uno es la estratégica que tranquilamente podrías ser vos.

**Franco Ferrero**: Yeah.

**Agustin Garcia**: Sí. Ahora, esa estratégica vos vas a marcar cuál es el lineamiento estratégico que querés implementar, ¿no? Después vas a tener alguien más operativo que va a ser el que cruce la información, descargue la información, tal vez el que haga el uso más fuerte de Teramot Hotspot y los otros sistemas para mezclar esa información y digamos eh poder definir en función de la estrategia que vos ponés eh cuáles son los clientes a los que hay que apuntar y cómo. Sí. Entonces ahí tenés esa pata y después tenés el el el ejecutor, que podría ser alguien de ventas propiamente dicho,

**Daniel Mendoza**: No entiendo,

**Agustin Garcia**: que básicamente va a saber a quién tiene que ir a venderle qué. Sí.

**Daniel Mendoza**: no entendí.

**Agustin Garcia**: Entonces, y después, obviamente que el operativo eh puede ir sacando también estadísticas de cómo van eh funcionando las campañas que van haciendo, ¿no? Y cómo la los resultados que va teniendo esa estrategia que tú definiste, ¿se entiende?

**Daniel Mendoza**: Correcto. Sí,

**Agustin Garcia**: digo,

**Daniel Mendoza**: clarísimo.

**Agustin Garcia**: te lo pongo en estos términos, pero digamos eh todo va de acuerdo a la al a los recursos que tengas y las funciones que tenga cada uno. digo, la parte operativa y estratégica inclusive hasta la podrías hacer vos, o sea, eh porque digamos una cosa que tiene esto que una vez que vos lográs ese nivel de madurez y ese nivel de automatización, después son prompts que vas tirando, vas armando la información, la información que en el sistema y después digamos obviamente que alguien tiene que enviar el mail inclusive, bueno, eh participar de la reunión que va a ser eh digamos el resultado de esa estrategia, ¿no?

**Daniel Mendoza**: Es correcto. Es correcto. Me queda claro.

**Agustin Garcia**: Exacto.

**Daniel Mendoza**: Me queda claro la interacción que hace en este caso Teramot con el equipo, con el personal y con la información que se puede manejar. Y no solamente cuando me dices,"¿Sabes qué? Hay Exceles que se pueden descargar porque también a estas alturas todavía hay mucho archivo eh manual, mucho archivo que se descarga de de eh sistemas de facturación que son muy muy manuales, poco electrónicos. Entonces entiendo muy bien y qué bueno, qué bueno que se pueda se pueda interactuar.

**Agustin Garcia**: Total, eso lo podrías inclusive, mira, si tenés un sistema que es muy difícil de conectar por algún motivo, porque la la plataforma tiene la posibilidad de conectar los sistemas de diversas maneras, inclusive hay algunos sistemas que tienen API, nosotros también tenemos la posibilidad de conectarlo por API, pero en el peor de los casos eh si descargas un Excel lo podés eh ingestar en el sistema eh y te queda como si fuese una tabla más dentro de la base de datos, una o varias tablas más, ¿no? Entonces, básicamente eso a vos lo que te permite es empezar a trabajar de forma

**Franco Ferrero**: M.

**Agustin Garcia**: automatizada con todo esto, ¿se entiende? O sea,

**Daniel Mendoza**: Correcto.

**Agustin Garcia**: poder trabajar, digamos, tú desde cloud o chachipt ir referenciando a cada uno de esos datos como si fuese una entidad, porque también Teramot, ¿qué tiene?

**Agustin Garcia**: Tiene la posibilidad de interpretar los modelos de datos. Entonces, si vos subís un Excel con una tabla, digamos, interpreta qué tiene esos datos, esas tablas, ¿no? Entonces, vos no le tenés que estar explicando. Inclusive, si tú te conectas a un sistema, a un IRP tuyo, digamos, tú le puedes pedir que levante el modelo de datos y ya con eso queda y el y el sistema que tiene va aprendiendo. Entonces, vos no es que cada vez que lo vayas a usar,

**Daniel Mendoza**: Correcto,

**Agustin Garcia**: digamos, tenés que explicarle qué es cada cosa, ¿se entiende?

**Daniel Mendoza**: correcto. Sí, sí, sí.

**Agustin Garcia**: Buenísimo,

**Daniel Mendoza**: Me queda claro, me queda claro, chicos.

**Agustin Garcia**: buenísimo,

**Daniel Mendoza**: Okay.

**Agustin Garcia**: buenísimo.

**Daniel Mendoza**: A ver, me dicen ahí este que en la página que tienen una demo ustedes o puedes

**Franco Ferrero**: Sí.

**Daniel Mendoza**: enseñarme en una compartición de pantalla cómo es la funcionalidad un poco cómo se ve, cómo es la la interacción.

**Franco Ferrero**: Sí, cómo no.

**Agustin Garcia**: Sí, claro. Franquitoarle

**Franco Ferrero**: Ahí voy. Sí, sí, yo lo mostro.

**Daniel Mendoza**: Atento.

**Franco Ferrero**: Ahí te comparto.

**Franco Ferrero**: Estoy leyendo. Bueno, me mostrar

**Daniel Mendoza**: Sí.

**Franco Ferrero**: estos Teramot. Acá acá yo estoy dentro de mi workspace que generé para un cliente que es una demo. Generé yo unos datos Dami con con Cloud. Eh, te muestro un poco cómo es. Acá vos tenés la posibilidad de conectar la fuente de datos que vos quieras. Eh, acá directamente pones conectar base de datos y vas a tener todas las posibilidad, las distintas posibilidades en el caso de que usen otro que no que no se encuentra

**Daniel Mendoza**: A ver.

**Franco Ferrero**: acá.

**Daniel Mendoza**: Ahí estamos,

**Franco Ferrero**: Lo podemos.

**Daniel Mendoza**: ahí estamos con Azur nosotros estamos con SharePoint también y

**Agustin Garcia**: Ups.

**Daniel Mendoza**: estamos manejando el tema de HPOT. Entonces, okay, los veo ahí el OneDrive también.

**Franco Ferrero**: Entonces, buenísimo. A ver, también es un tema de que en el caso de que no haya alguno de los que vos necesitás, se puede evaluar para hacer una conexión. No es algo que que es complicado. De hecho, bueno, ya nombraste tres que usas y que están acá. Así que de hecho la conexión una vez que estás acá,

**Daniel Mendoza**: Sí.

**Franco Ferrero**: de hecho lo de Ayure es directamente poner los datos de la base de datos y ya la conexión y ya se ingesta, se ingesta la data.

**Franco Ferrero**: Después tenés la posibilidad también de cargar archivos, como te mencionó Agustín. la posibilidad de cargar archivos Excel si CCB como para ya directamente dejar estas tablas fijas. Acá en la parte de estudio de datos vas a ver que una vez cargados los datos a través de los distintos los agentes internos se va a generar toda una descripción de cada tabla y qué contiene cada tabla. vas a poder también tener trackado eh el SQL, que es decir de la manera en la que se generó esa tabla y y qué tiene. Y después, por otro lado, vas a tener una una un sector de conocimiento en donde vos le vas a poder dar un poco de contexto sobre tu negocio, regla de negocio que vas a querer, distintos joints que quieras hacer en las tablas para que los agentes de Teramot y después tanto Cloud como cualquier LLM lo pueda lo pueda entender y no se confunda siempre en lo mismo.

**Daniel Mendoza**: Correcto. Tam

**Franco Ferrero**: Después tener la posibilidad de poner que la que se hagan actualizaciones programadas. Normalmente nuestros clientes suelen trabajar con la actualización de eh todas las mañanas y trabajan el ayer, digamos. Entonces, esto está bueno porque ya cada 2 horas o cada una hora se puede hacer la actualización y funciona bien. No lo vas a poder tener en vivo porque en tiempo real es es muy difícil, pero cada una hora, que ya de hecho es una frecuencia bastante rápida que se actualice es es también bastante bueno.

**Franco Ferrero**: Y bueno, acá un poco vas a tener las distintas conexiones con los LLMs, con el paso a paso de cada uno, de qué manera vos lo vas a conectar a Cloud, chatt, el que uses. Y bueno, si querés te muestro a ver un poco desde cloud ahí,

**Daniel Mendoza**: Sí, por favor.

**Franco Ferrero**: ahí te muestro de cloud. Esp, te voy a presentar otra ventana. Ahí voy. Y acá y ahora desde Cloud directamente trabajar acá. Y yo acá le digo,"Conéctate a mi MCP de Teramot, a mi en este caso Workspace se llamaoup. Entonces, una vez Ah, bueno, vamos. Mira, un poco también para para mostrarte eh que no te mostré previamente, así ya te perolijo esto, perdón.

**Agustin Garcia**: Sí.

**Franco Ferrero**: Es que es dentro de dentro de Teramot. Vos contás con un agente interno en el que en el caso de que no tengas ningún

**Daniel Mendoza**: Correcto. Ok.

**Franco Ferrero**: MCP ni nada, puedas eh directamente trabajarlo desde acá. Entonces, de acá digamos eh qué tablas tengo.

**Daniel Mendoza**: Pero lo que quería saber es si yo tengo ya la datas trepada, eh, pregunta, ¿dónde genero el dashboard? En en, ¿cómo se llama?

**Daniel Mendoza**: En cloud o acá o en Teramot.

**Franco Ferrero**: O sea, vos podés generar los dashboard tanto en el agente interno como desde cloud y que el cloud lo suba a Teramot, que los vas a ver acá disponibles.

**Daniel Mendoza**: Si usara dentro de Teramot, ¿cuántos créditos obtengo? ¿Cuántos créditos tengo de reportaje en ese en ese sentido

**Agustin Garcia**: el eh Teramot.

**Daniel Mendoza**: o cuál es la limitante?

**Agustin Garcia**: Sí, Teramot, ¿no? O sea, para que te des una idea cómo es el esquema de pricing de Teramot. El esquema de pricing de Teramot está limitado por cantidad de usuarios y cantidad de tablas golds que se que uses. Por ejemplo, cada reporte que vos uses puede ser una tabla gold. Sí, hay distintos esquemas. E pero Teramo no incluye eh lo que son licencias de Cloud o Chachipt. Eso corre por tu cuenta. Sí.

**Daniel Mendoza**: No, no, eso lo comprendo yo. Lo que más quiero es,

**Agustin Garcia**: Okay.

**Daniel Mendoza**: a ver, si voy a usar Teramot y yo digo,"Okay, voy a centralizar mi información." Entonces, cojo SharePoint conectado, cojo mis tablas conectadas, cojo por ahí este HPOT para sacar este los leads conectados.

**Daniel Mendoza**: Listo. Entonces entro acá y digo,"Bueno, ¿sabes qué? Voy a armarme una tarea. Seguimiento al equipo comercial de prospectos. Eso yo lo puedo tener ahí y semanalmente o mensualmente generar mi reporte para generar la la la comunicación hacia los chicos, pero lo tengo que o lo puedo usar libremente desde Teramod, que veo que parece que sí, o necesariamente tengo que correr a cloud para que se conecte y lo pueda sacar. Eso, esa es la primera pregunta. Y la segunda pregunta.

**Agustin Garcia**: que una vez que vos generá el dashboard,

**Daniel Mendoza**: Hm.

**Agustin Garcia**: ese dashboard después eh se actualiza cada vez que se actualizan los datos. Sí.

**Daniel Mendoza**: De acuerdo.

**Agustin Garcia**: Entonces, en ese sentido ahí no tenés un problema. Ahora, si vos tuvieses que hacer otro otro reporte o algo y eh te conviene hacerlo desde cloud o de chachi pití,

**Daniel Mendoza**: De acuerdo.

**Agustin Garcia**: hay una cosa que es importante acá, ¿no? Donde, ¿cuál es una de las ventajas que adicionales que tiene Teramot? Es que digamos el conector MCP que tiene Teramont es superficiente en la comunicación con el LLM. Sí. Entonces, el consumo de tokens que vas a tener por el lado del LLM es bajo.

**Agustin Garcia**: Sí,

**Daniel Mendoza**: Ah, okay,

**Agustin Garcia**: hoy en día,

**Daniel Mendoza**: perfecto.

**Agustin Garcia**: ¿no? O sea, te lo digo porque Nosotros hemos comparado contra otros productos y los conectores no son tan eficientes, entonces el consumo de tokens es bastante alto. En este caso, inclusive nosotros tenemos clientes que usan eh Teramot con la licencia de $ de de cloud y lo usan perfecto. ¿Qué puede pasar? Eh, tenemos en algunos clientes donde hay usuarios que son superintensivos y que están todo el día generando y haciendo análisis, reporte, porque, ¿cuál es, qué es lo que pasa en esos escenarios? Y lo que pasa es que de repente te dice que te quedaste sin tokens, que esperes hasta dentro de 4 horas, ¿no?

**Daniel Mendoza**: Mm.

**Agustin Garcia**: Lo cual, por un lado está bueno, porque a vos te permite gestionar el presupuesto eh sin digamos tener eh imprevistos. Eh, y también por otro lado, ¿qué qué ha ocurrido? A esos usuarios que son superintensivos y que realmente con el plan de $20 no les alcanza, lo que hacen es le dan una un plan eh más alto, por ejemplo, el de 100, ¿se entiende? Y con el de 100 ya funcionan perfecto.

**Daniel Mendoza**: Okay,

**Agustin Garcia**: ¿Me explico?

**Daniel Mendoza**: okay. Sí, sí, claro. Ya.

**Agustin Garcia**: Buenísimo.

**Franco Ferrero**: Bueno,

**Daniel Mendoza**: Básicamente lo que quería saber es que si yo dentro de Teramot podría gestionar ya toda la información, subir, subir, subir y gestionar todo.

**Agustin Garcia**: Sí.

**Daniel Mendoza**: Esa es esa es una de mis de mis principales bases.

**Agustin Garcia**: La la respuesta es sí.

**Daniel Mendoza**: Entonces yo de aquí eso ya ya después que me integre con cloud o me integre con otra, entiendo, pero me gustó cuando tú puedes interactuar o tú puedes subir todito y tú dices,"Okay, esta es mi mi base de inteligencia de toda mi data." Ya sea que yo la subo,

**Agustin Garcia**: Claro,

**Daniel Mendoza**: que yo me conecte y desde aquí voy a trabajar unificadamente.

**Agustin Garcia**: exactamente. Uno, ¿qué hace con con Clud? ¿Conchip? le aplica el poder de procesamiento que tiene, ¿sí?, a la información que vos tenés.

**Daniel Mendoza**: Correcto.

**Agustin Garcia**: No sé, te te tenemos casos de uso de todo tipo. Tenemos desde análisis comercial de estos que te contaba de cómo pueden mejorar las ventas, de analizar la performance de un producto, ¿sí? Eh, hasta no sé eh análisis de control de gestión, cuentas a pagar, proveedores, digamos, eh proyección de cashflow, lo que se te ocurra.

**Daniel Mendoza**: Correcto. Вот.

**Agustin Garcia**: Porque básicamente el vos con el LLM lo que le estás aplicando es eh capacidad de procesamiento. Incluso hasta tenemos clientes que que aplican modelo de machine learning con esto para poder sacar información estadística, tipo de agrupamiento muy específico que que de acuerdo al negocio pueden ser superútiles. Y el costo no es algo, digamos, realmente no no no es algo prohibitivo que inclusive te diría

**Daniel Mendoza**: M.

**Agustin Garcia**: más, se paga solo, porque si vos tuvieses que poner gente a a hacer todo este trabajo, eh, seguramente va a ser más caro.

**Franco Ferrero**: M.

**Agustin Garcia**: Yeah. que eh las licencias que tengas que pagar entre Teramot y y y Cloud o CHPT y los sistemas que que tengas adicionales.

**Daniel Mendoza**: Justamente eso es lo que estoy estoy tratando de buscar, esa eficiencia de no estar llevando. Por otro lado, a mí el tema de de cloud me parece que compartir o subir en mis tareas toda la información de la empresa me los me lo me parece un poco impropio. Entonces, si busco una alternativa Teramot que es totalmente independiente, que es básicamente como un sistema propio para uno, para el recurso de uno y lo manejo dentro de mi propio sistema, como que controlo, se siente que se controla más la información,

**Agustin Garcia**: Exacto.

**Daniel Mendoza**: ya se siente que es más personal, que es propio,

**Agustin Garcia**: Claro,

**Daniel Mendoza**: ¿ves?

**Agustin Garcia**: claro.

**Daniel Mendoza**: Y entonces no me basa simplemente a lo que está en la calle, revuelve las cosas y luego las las trata de interactuar.

**Agustin Garcia**: Exacto.

**Daniel Mendoza**: Entonces, para mí sería un generador de asistencia financiera, asistencia comercial y trabajo de datos. Entonces,

**Agustin Garcia**: Claro.

**Daniel Mendoza**: simplemente tendría que tener una persona que me elabore correctamente los prom y simplemente con toda la confianza del mundo subo todo ahí y eso me lo interactúa. Ya. Okay, okay, okay, okay, okay. Y me hace más cosas que simplemente tener un tema de dashboard que me lo trabaje, que lo interprete y que lo resuelva. ¿De acuerdo? ¿Podrías ver cómo cómo se cómo se ve un dashboard eh ya ejecutado y luego cómo se se ve de cualquier ejemplo que tengas?

**Franco Ferrero**: Sí. A ver, ahí le estoy pidiendo que me arme uno, así te muestro cómo cómo los arma.

**Daniel Mendoza**: Ajá.

**Franco Ferrero**: ¿Ves? Te dice el estado de construcción. te muestra también esto. Está bueno para para ver también que veas que puedes ver de qué manera arma las tablas y de qué manera lo procesa. Y ahora me está haciendo los dashboards, así que una vez que están realizados los vamos a ver acá que ahora

**Daniel Mendoza**: Perfecto. De acuerdo.

**Franco Ferrero**: los está creando. Estos dashboard los arma todos en base a,

**Agustin Garcia**: Ah.

**Franco Ferrero**: en este caso, a las tablas gold que yo formé ahora que vamos a

**Daniel Mendoza**: Eso. A ver, déjame ver ese tema. Tablas gold. Ya. Dame la diferencia entre tabla silvervel y y tabla gold. ¿Qué significa? O básicamente, ¿qué es una y la otra?

**Franco Ferrero**: Bueno, a ver, eh, la principal, a ver, lo que tienen las tablas gold. Las tablas gold son tablas que vos formás a partir de los análisis que querés realizar. Esto lo que quiere decir es vos armás una nueva tabla a raíz de distintas puede ser información de que está en distintas tablas de una columna de cada tabla. Hacer distintos cruces de tablas para armar solo un análisis en base a lo que vos necesitas. Entonces te queda una tabla limpia, por ejemplo, puede ser ventas por cada por cada local, por ejemplo. Entonces, la venta por cada local, capaz tenés todas las ventas juntas y tenés una columna que dice cada local. Entonces, lo que hace las tablas go directamente te genera una tabla con las ventas de de ese local que vos le pediste.

**Daniel Mendoza**: De acuerdo.

**Franco Ferrero**: Es como que te genera una tabla limpia en base al análisis que vos querés hacer.

**Daniel Mendoza**: De acuerdo.

**Agustin Garcia**: Ahí para que tengas una idea, Daniel, o sea, este concepto de tabla bronce, silver, eh, plata o oro que es un esquema, es un patrón de arquitectura de datos muy conocido y que básicamente a medida que vos los datos entran en bronce, en plata y oro, es es el nivel, digamos, de de trabajo que hubo sobre los datos para terminar siendo los consumidos, ¿no?

**Daniel Mendoza**: Okay.

**Agustin Garcia**: Donde cuando estás una tabla goles ya están curados y correspondidos con la información necesaria para cumplir un objetivo puntual.

**Daniel Mendoza**: O sea, vamos de SharePoint, trabajamos la información y eso extrae una tabla.

**Agustin Garcia**: Sí,

**Daniel Mendoza**: A esa tabla, que podría ser una silver, se le aplica tal concepto de uniendo cosas, en este caso de Hpot y se crea una gold.

**Agustin Garcia**: exactamente.

**Daniel Mendoza**: De acuerdo. De acuerdo.

**Franco Ferrero**: No. Por ejemplo, acá vos en estudio de datos vas a poder ver las tablas silver y las tablas gold. Y las tablas bronce son del son de la manera en la que vos las ingestás.

**Daniel Mendoza**: La subiste. Correcto. De acuerdo.

**Franco Ferrero**: O sea, las ingestás a través de los agentes se toman ese tiempo y te generan las tablas silver, que son estas, ¿ves? que ya generan la metadata, digamos, de tu información y en base ya al análisis que yo le pido, genera la tabla Gold, que acá, por ejemplo, puedes ver que te muestra qué dos tablas usó para armar solo una tabla.

**Franco Ferrero**: Entonces,

**Daniel Mendoza**: Correcto.

**Franco Ferrero**: acá te explica lo que hace, las instrucciones que hace. Más que nada está bueno para tener un seguimiento de lo que es el estal columnas Acá está bueno. Puedes usar distintos tipos de de inteligencias, digamos. No es que solo usamos cloud. Nosotros internamente usamos cloud porque es el que más nos ayuda.

**Daniel Mendoza**: De acuerdo.

**Franco Ferrero**: Y ahora está consultando los datos y ya está armando el dashboard directamente.

**Agustin Garcia**: Daniel, yo te dejo con Franco porque tengo otra reunión, eh,

**Daniel Mendoza**: Claro,

**Agustin Garcia**: pero te agradezco el tiempo,

**Daniel Mendoza**: por favor. No, a ustedes, a ustedes, chicos. Gracias.

**Agustin Garcia**: por favor. Yeah.

**Franco Ferrero**: Chaos.

**Daniel Mendoza**: A ver.

**Franco Ferrero**: Usar el nombre. A ver, la realidad también un poco es que lo que te viste, la ventaja de Cloud, si querés, en cierto sentido, es que nosotros ahora ponerle en este agent estamos usando cloud, pero lo usamos dentro de nuestro agente.

**Daniel Mendoza**: Es correcto. Sí, sí, sí.

**Franco Ferrero**: Ahora, el volumen y la capacidad de análisis y de generación de reportes de cloud propio es mucho más fuerte que el del agente interno por una cuestión de capacidad y hay veces que,

**Daniel Mendoza**: De acuerdo.

**Franco Ferrero**: a ver, que es una realidad también muchos clientes nos pasa que, por ejemplo, nos dicen,"Che, la pero la licencia de Cloud es un es un es un gasto más." Y nosotros muchas veces le decimos,"Sí, son $20 que, o sea, ya con la licencia profesional de $ más, o sea, tenés la cantidad de token necesarios y lo bueno es que vos estás haciendo preguntas normales a CL, no le estás haciendo preguntas en las que tiene que usar muchos tokens. Es una cuestión más que nada de que al ya estar conectado a Teram con toda la información limpia, con toda la metadata a través de esa información, puede llegar más fácil a armar todo ese tipo de análisis sin tener que gastar mucho tokens.

**Daniel Mendoza**: M. Ahí dijiste ya la funcionalidad. Ahí ya me indicaste la funcionalidad. Okay, claro, claro.

**Franco Ferrero**: Es como que Exactamente.

**Daniel Mendoza**: Es hacer mucho más eficiente eh a cloud porque tú integras primero todo,

**Franco Ferrero**: Entonces,

**Daniel Mendoza**: limpias todo, lo pones más puro y simplemente Cloud viene hacia acá y dice,"Ah, no, mira, ya acá está todo lo que necesito." De acuerdo, lo entendí. Ya lo entendí.

**Franco Ferrero**: exactamente había armado el ver si quedó. Si no que le digo que lo vuelta este bueno, pero por ejemplo es lo que yo te decía.

**Franco Ferrero**: Bueno, justo ahora me estuve trabajando todo el día con Cloud, pero es un poco eso de decir de eh una que que vos ya le permitís a Claud los datos limpios, el esfuerzo que va a requerir es menor y ese consumo de tokens que capaz muchos clientes, o sea, también te lo explico porque eh muchos clientes le pasa lo mismo,

**Daniel Mendoza**: Mm.

**Franco Ferrero**: ese consumo de tokens no lo tienen que ver como algo preocupante, o sea, entiendo que muchas veces sucede, pero en nuestro caso es la idea es facilitarle también a Cloud para que use los menos token posibles.

**Daniel Mendoza**: De acuerdo. No.

**Franco Ferrero**: Ahora a través de HTML con todo va a estar desarrollando esta este dashboard de facturación de cartera. en la nube. Bueno, a ver, esto es lo que te decía de las descripciones que te van armando en base a las distintas tablas gold, que en base a eso arman los los dashboard, por ejemplo.

**Daniel Mendoza**: Oh.

**Franco Ferrero**: Entonces acá ves poner, me va a decir, tengo 40 clientes para armar este dashboard sobre la facturación. 40 clientes son seis periodos, seis suscursales. Total de filas 414. Entonces ahora te arma directamente el dashboard con la información de de esta de esta esta tabla gold,

**Daniel Mendoza**: Sí.

**Franco Ferrero**: digamos.

**Franco Ferrero**: Y ahora lo está armando y lo vamos a poder ver acá.

**Daniel Mendoza**: Ok.

**Franco Ferrero**: Y ahora nos va a traer los dos dashboards ya armados, porque le pedí los dos, no es que le pedí uno solo, por eso también se toma su tiempo, pero igualmente no. A ver, esto hay veces que capaz tarda así 5 minutos,

**Daniel Mendoza**: Ok.

**Franco Ferrero**: pero también hay que entender que capaz el día hay mucha gente que hoy en día lo hace a través de código SQL, todo esto, a través de Power B y cosas así que te terminan llevando capaz horas y

**Franco Ferrero's Presentation**: M.

**Franco Ferrero**: horas. Yeah. Cuando hoy en día directamente si Clodo, cualquier LLL logra entender y limpiar tus datos, puede llegar a ser todo mucho más rápido.

**Daniel Mendoza**: De acuerdo.

**Franco Ferrero**: Y ahí ya está armando el HTML para esto.

**Daniel Mendoza**: Vamos a ver.

**Franco Ferrero**: Chur ver qué está haciendo vos acá. Lo bueno es que puedes ir viendo qué qué está haciendo para también entender en qué

**Daniel Mendoza**: alabanza.

**Franco Ferrero**: está sin pregunta. Vos nos dijiste que nos viste un

**Daniel Mendoza**: Sí, este estaba viendo en YouTube y apareció su ¿cómo se llama? Como su publicidad y justamente estaba entrando a temas de Vitrix y algo así y de ahí saltó y como que me me salió un tema con su con su tema con Teramot.

**Daniel Mendoza**: Por otro lado, cuando ya vi eso, puse cuáles son los en en una búsqueda cuáles son los los agentes más rápidos en procesamiento de datos y en este caso CRMS y me salió en una lista la la la la la y me salieron ustedes y como ya había visto HPOD, había visto eh lo unos cinco CRMs más, dije, esto no dice que es un CRM, esto no dice que es. Entré, leí, leí, leí, pero de una vez lo lanzaba una demo. Entonces dije,

**Franco Ferrero**: H

**Daniel Mendoza**: hm, a una demo de una vez, no, primero quiero verlo, quiero probarlo, quiero quiero por ahí monitorearlo. Ah, no, pues si ahí dije, no, ya vamos a vamos a escuchar de qué se trata realmente. Entonces, ahora que ya me lo explican, porque la verdad que no lo había entendido en la página web de ustedes, ya veo que ustedes son un motor de interacción de datos, o sea, centralizan datos para hacer mucho más eficiente cualquier tipo de trabajo en inteligencia artificial. Entonces sí me sí da la espinita chévere, porque al final del día yo lo que menos quiero es estar subiendo en distintas plataformas de inteligencia

**Franco Ferrero**: ¿Ves?

**Daniel Mendoza**: artificial que se supone que es de dominio, o sea, no de dominio público, sino que pienso que entran muchas personas, lo suyo es más privado.

**Franco Ferrero**: Y acá está un poco esto de lo que es el pipeline que nos hizo.

**Daniel Mendoza**: A ver, veamos, veamos, veamos.

**Franco Ferrero**: ¿Ves? Las oportunidades abiertas son 50, valor total en pipeline, oportunidades ganadas, por ejemplo. Entonces, acá tenés prospectos,

**Daniel Mendoza**: Eso,

**Franco Ferrero**: contratado,

**Daniel Mendoza**: es

**Franco Ferrero**: reunión agendada, negociación, eh valor de pilban por vendedor. Todo esto son datos Dami, ¿no? son datos que generados club para una para una,

**Daniel Mendoza**: así. Bueno,

**Franco Ferrero**: ¿cómo se llama? Para una demo, pero más que nada para entender un poco, ¿ves? Conción de Rosario con frío email, valor de pipeline, como que te genera todos los dashboard en base a lo que vos le pidas. ¿Ves? Acá tenemos cobrancia de cartera, otro total cobrado con facturado, una mora por sucursal, clientes con mayor saldo pendiente, días de mora, como que te permite armar. Después de esto ya te arma distintas cosas que pueden llegar a ser muy muy buenas. Y bueno, eso es un poco el tema.

**Daniel Mendoza**: Ahí, ahí me agradó. A ver, este, ustedes tienen mi número de WhatsApp o mi correo, ¿verdad? Tienen mi correo. ¿Cómo son los planes de ustedes?

**Franco Ferrero**: Tengo correo los dos.

**Daniel Mendoza**: ¿Me puedes enviar, por favor, la información como tal de los planes que tienen? Y sí me gustaría una referencia de consumos de token, ¿okay?

**Franco Ferrero**: Perfecto.

**Daniel Mendoza**: Porque si tengo que contratar este este tema ya el plan básico que ustedes me dicen del 20 en en cloud, quisiera ver si lo aumento un poco más o no y quiero evaluar esa situación entre las dos opciones que ustedes me dan. Ya.

**Franco Ferrero**: Okay, entonces necesitas que te pase así. Ya, ya me enojendo y te mando todo.

**Daniel Mendoza**: Sí, formal, formal. Envíame poral cuánto sería el presupuesto en este en este tema de inversión. Ustedes me dijeron que por usuario o algo así. Por favor, pásame esa información bien porque tengo que definir a qué personas voy a tendría que interactuar con esto.

**Franco Ferrero**: Okay, dale. Perfecto. Bueno, muchas gracias.

**Daniel Mendoza**: Gracias a ti.

**Franco Ferrero**: Chao,

**Daniel Mendoza**: Nos vemos.

**Franco Ferrero**: Daniel, que tengas un buen día.

**Daniel Mendoza**: Chaoo.

**Franco Ferrero**: Ciao. Ciao.

**Daniel Mendoza**: Igualmente,
