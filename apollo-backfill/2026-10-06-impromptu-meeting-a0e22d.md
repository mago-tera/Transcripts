# Impromptu meeting

**Fecha:** 2026-10-06T14:36:53.426+00:00  
**Duracion:** ~18 min  
**Participantes:** Franco Ferrero <franco.ferrero@teramot.com>, Uriel Segaloff <>, Facundo Ignacio Vivas <>, Esteban Onocko <>  
**Externos:** Uriel Segaloff, Facundo Ignacio Vivas, Esteban Onocko  
**Apollo ID:** 6ac50bc6fe789b000ca0e22d

---

**Esteban Onocko**: Franco, ¿Cómo andás? ¿Me escuchas bien? Estás muteado. Ahí le pasé tu link a Uri también para que se meta.

**Franco Ferrero**: Dale, ahí ahora más que nada vemos cómo viene Uri. Si no, si, ahí yo le. Le pego un mensaje a uno de los chicos de sistemas y se sube también para ver el tema de la conexión, así ya les queda andando, ¿Viste?

**Esteban Onocko**: Dale, excelente. Sí, sí, ahí estuvimos creo que ya bastante avanzados, pero por ahí queda alguna dudita.

**Franco Ferrero**: OK, buenísimo. Así ya lo vemos. Y estuvimos agregando un par de funcionalidades. ¿Te cuenta? Si. Mientras de nuestra plataforma agregamos todo un sistema de dashboards y alertas. ¿Qué quiere decir esto? Lo que buscamos un poco con la generación de dashboard son todos para los reportes y análisis que se arman, son dashboards que quedan internos en la plataforma, que los generas con cloud directamente, se generan con HTML, o sea, son interactivos, tienen una capacidad muy buena de. De visualización y se puede compartir fácilmente. Además también un poco lo que estamos buscando con esto es que las empresas no tengan que contratar 200 servicios para hacer el análisis, sino que simplemente desde Theramo puede reemplazar también lo que es Power BI, Tableau y hacer todo lo que son estos análisis, Dashboards, como puede ser gráficos, o sea todo tipo de. De herramienta visual que sea para un análisis o algo, hacerlo directamente vía theramot. Y agregamos toda una parte de alertas, que la idea es decir, por ejemplo, vos tenés una lista de clientes de proveedores que tienen pagos de 30 a 90 días, vos podés generar distintas alertas, decir che, cuando tantos clientes superen el límite de tanta X cantidad de plata que me debe a 30 días, hacemos una alerta si yo le escribo o tomamos alguna acción.

**Esteban Onocko**: Claro, como para gestionar, digamos.

**Franco Ferrero**: Claro, avisos de alertas que vos quieras tener, dependiendo obviamente el caso de uso de cada uno, pero un poco es eso.

**Esteban Onocko**: Buenísimo, está bueno, está muy interesante, o sea, y aparte lo del HTML es muy portable, vos lo podés mandar así fácil a cualquier usuario y ya lo podría consumir como que la base de datos. Pero pará mi duda es la siguiente, o sea, estoy comparándolo contra un Power BI, ponele que se actualiza la base diariamente. Sí ya ese mismo link se actualiza,

**Franco Ferrero**: así como vos actualizas la base de datos que se actualiza en Theramo, Viste que nosotros, no sé si te acordás, habíamos hablado de lo que eran las tablas gold, que eran las tablas de resultados, de análisis de resultados, donde se hacían los distintos cruces de tablas qué hace Tenamo para para generar estos dashboards o estos análisis, estos reportes en HTML que genera, que de hecho, a ver, muchas veces podés poner filtros, viste, como que tiene un avance muy amplio. Lo que hace es, genera estos dashboards a través de una tabla gold, de

**Esteban Onocko**: una tabla a gold.

**Franco Ferrero**: Entonces a medida que la tabla, o sea, la fuente se actualiza, ¿Que quiere decir? La base de datos se actualiza, se van a actualizar las tablas silver, y como esas tablas silver se van a actualizar, las tablas gold que usan esas tablas silver van a tomar en cuenta la actualización que hizo y van a actualizar tanto la tabla gold, por ende se actualiza el dashboard que está vinculado a esa tabla. ¿Me explico o fue medio chino?

**Esteban Onocko**: No, no, entendí, entendí, o sea, está bueno, estoy pensándolo en la dinámica del día a día nuestra, porque tengo mucho, a ver, tengo hoy dos focos muy fuertes, por un lado es un tablero de negocios, que la idea es probar la herramienta con ese tablero de negocios,

**Franco Ferrero**: ¿Qué tipo de tablero?

**Esteban Onocko**: ¿Por ahora se actualiza mensualmente, entonces no es un desafío, pero queremos llegar a una actualización tipo diaria, viste?

**Franco Ferrero**: Mira, la mayoría de nuestros clientes trabajan, o sea, hoy trabajan el ayer con los datos realizados de ayer, tenemos una frecuencia que está probada que es eficiente de hasta dos horas, es decir, no

**Esteban Onocko**: sería una por día, o sea, eso está.

**Franco Ferrero**: ¿Yo te cuento, las pruebas que también fuimos haciendo es que hoy en día cada dos horas la actualización se hace al 100% de efectividad, como que es lo más hoy en día en vivo, si querés, lo más on premise que tenemos,

**Esteban Onocko**: OK?

**Franco Ferrero**: Pero bueno, la realidad es eso, que muchas veces la actualización nuestros otros clientes la hacen a las 7 de la mañana de todos los días, una vez, para ese día trabajar con los datos de ayer.

**Esteban Onocko**: Claro, eso vendría muy bien, o sea, te digo una cosa, te vas a reír, pero hoy agarramos la tabla que sale, tenemos conectado la SQL a un Power BI, el Power BI hace un montón de cosas, pero deja una tabla medio grosera, medio feita, viste, un poco amable a los ojos de un analista X, y a esa tabla la bajamos en un CSV y se la escupimos al Claude y se la tiramos para que haga cosas, y Claude obviamente hace maravillas, o sea, ni te quiera explicar a vos lo que hace, o sea, la NASA parece al lado de lo que hacíamos con cero esfuerzo, y bueno, lo que pasa es que seguimos peleando con la base, ¿Me entendés? Sigo depurando la base, entonces siento que

**Franco Ferrero**: si funciona bien la conexión, es como que ya directamente desde Thermo, creo que eso va a ser. Te soluciona el problema más grande.

**Esteban Onocko**: Claro, hasta te puedo interactuar mejor con las bases, en el sentido de que si bien hoy conect. Usar a Power BI como modelador de datos igual no tiene mucho sentido si tenés a alguien que lo hace mejor, me parece, o sea, bueno, nada, por eso quiero probar esta funcionalidad, ver qué diferencia me sale. Lo interesante es que ya lo tengo, entonces digo, che, pruebo esto, sería nuevo, inmejorable con lo que ya tengo, y puedo hacer un contraste muy fácil y demostrar si es bueno, si es malo, en tres, cuatro horas de trabajo ya más o menos tengo una versión

**Franco Ferrero**: comparación muy clara, ¿No? Obviamente, un poco también, un poco viniendo también a lo que decías vos antes de hoy en día lo que puede hacer Claude es muy amplio y es también mucho lo que me pasa con los distintos clientes, de decir, hay un alcance que tiene la plataforma que ni hasta yo lo puedo explicar, porque es un alcance de estar uno hablando con Claude y es el interactuando ahí, abriendo distintas posibilidades de análisis de ideas que se te ocurren, y como que está mucho también en cuanto más sabes usar Claude o sabes interactuar con Claude, cuanto más jugo le vas a sacar también, porque a ver, ahí el fuerte está en que Cloud ya entiende tus datos y ya sabe lo que vos haces, entonces si le empezás a dar distintas vueltas de tuerca, le explicas un poco sobre tu negocio, como que lo terminas. Al final termina siendo una herramienta muy potente, digamos.

**Esteban Onocko**: Sí, sí, sí. La ventaja de por ahí poder trabajar con lenguaje natural sobre algo que por ahí es complejo, para mí por lo menos, que soy un queso con la programación de hacer con el Power BI, este pibe me dijo en cabe 5, pero ya se consumió en 5.

**Franco Ferrero**: Ahí está.

**Uriel Segaloff**: Buenas, ¿Cómo andan? ¿Todo bien? A ver, estoy apretando el tema de la configuración del túnel VPN. Les explico. Nosotros tenemos un proveedor que es el que nos da soporte de todo lo que es configuraciones de entrada, entre otras cosas, de entrada salida de conexiones.

**Franco Ferrero**: Le dije a uno de los chicos que se sume de sistemas, así se lo explica vos también a él. Y entiendo que va a ser mejor, pero entiendo. Con lo que yo te mandé, pudiste avanzar algo o hay todavía algo, una traba que muestra que.

**Uriel Segaloff**: Esperá, espera un segundito que retomo el último mail, el último mensaje. Espera,

**Franco Ferrero**: Ahí se está sumando, así que.

**Esteban Onocko**: No daba nada.

**Uriel Segaloff**: Sí, a ver, yo le mandé esto que me has comentado de dónde se configura la VPN y bueno, estoy esperando que me pasen toda la data para poder hacer la prueba y configurarlo. Una vez que tenga eso, ahí sí vamos a poder ver cómo seguir. Pero bueno, necesitaba un poco que me pasen, que este proveedor que tenemos me pase esos datos para poder probar la conexión y una vez que eso esté ahí, se avanza. Que me dijo recién le mandé, le pregunté por el chat y me dijo que ahora en un toque me respondían el correo, que el correo se lo mandé ayer a las árboles. Así que nada, se supone que hoy voy a tener novedades. ¿Eso se puede?

**Franco Ferrero**: A ver acá si también tenés un par de dudas más técnicas ahí sobre la conexión, si querés preguntar a Facu.

**Uriel Segaloff**: OK, perfecto. Bueno, yo ahora estoy a la espera de que pasen bien todos los datos de que poner en cada campo, básicamente. Si querés Franco, bueno, vos tenés mi contacto, pásame el contacto de Facu y cualquier cosa le voy preguntando a él directamente por WhatsApp, así lo resuelvo más rápido. Pero bueno, se supone que hoy tenemos que ser novedades.

**Franco Ferrero**: Bueno, si les parece, a ver, si les parece bien, hacemos lo siguiente que es. Esperemos a que te conteste el pibe este.

**Uriel Segaloff**: Sí, dale.

**Franco Ferrero**: Yo te contacto con Facu como para que tengamos la conexión. Y Esteban, nosotros coordinamos una reunión mañana o pasado cuando ya tengamos la conectada. ¿Sí? Hacemos la demo y probamos la herramienta.

**Uriel Segaloff**: Dale. Bueno. Bueno Franco, espero que me pases el

**Franco Ferrero**: contacto entonces ahora, Facu, ahora pasame tu contacto y hablamos por ahí.

**Uriel Segaloff**: Listo, gracias. Chau, chau.
