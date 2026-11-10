# -*- coding: utf-8 -*-
# Version espagnole (Espagne, tutoiement « tú ») du lot 1 des guides coachs.
# Base : tools/en/coachs/batch_1.py. Droit, taux et organismes : tools/intl/_faits-ue.md et
# tools/intl/_faits-es.md uniquement (consigne : tools/intl/_brief-coachs.md). Le PAR-Q+ n'est jamais reproduit.

ENTRIES = [
    {
        "fr": "fiche-client-coach-sportif",
        "slug": "ficha-cliente-entrenador-personal",
        "title": "Ficha de cliente para entrenador personal: qué debe incluir",
        "description": "Ficha de cliente para entrenador personal: qué apartados incluir, qué datos son de salud según el RGPD, qué no escribir y cuánto tiempo guardar cada dato.",
        "body": """
<p>La respuesta corta: una <strong>ficha de cliente para entrenador personal</strong> cabe en siete apartados: contacto, condiciones, objetivo, práctica deportiva, salud, mediciones y seguimiento. En cuanto recoge una lesión, unos antecedentes médicos o las respuestas a un cuestionario, contiene datos de salud, y en España esos datos están especialmente protegidos por el RGPD y la Ley Orgánica de Protección de Datos (LOPDGDD). Anota solo lo necesario, pide el consentimiento del cliente y guarda la parte de salud aparte.</p>

<h2>¿Qué debe incluir una ficha de cliente?</h2>
<p>Aquí tienes una estructura de ejemplo. La última columna indica cómo tratar cada apartado, porque si algo es o no un dato de salud se valora caso por caso.</p>
<div class="tablewrap"><table>
<caption>Apartados propuestos como ejemplo, con una lectura prudente del RGPD.</caption>
<thead><tr><th>Apartado</th><th>Qué anotas</th><th>Tipo de dato</th></tr></thead>
<tbody>
<tr><td>Contacto</td><td>Nombre, email, teléfono, contacto de emergencia</td><td>Dato personal ordinario</td></tr>
<tr><td>Condiciones</td><td>Horarios, lugar, material, bono o cuota, fecha de inicio</td><td>Dato personal ordinario</td></tr>
<tr><td>Objetivo</td><td>Las palabras del cliente, plazo, motivación</td><td>Ordinario, salvo que revele un problema de salud</td></tr>
<tr><td>Práctica deportiva</td><td>Actividad actual, historial deportivo, preferencias, intensidad buscada</td><td>Ordinario, revísalo caso por caso</td></tr>
<tr><td>Salud</td><td>Respuestas al cuestionario, molestias que comenta, consulta médica que le has pedido</td><td>Dato de salud</td></tr>
<tr><td>Mediciones</td><td>Peso, perímetro de cintura, frecuencia cardiaca, sueño</td><td>Trátalo como dato de salud</td></tr>
<tr><td>Seguimiento</td><td>Tests, sesiones, cargas, sensaciones del cliente, decisiones tomadas</td><td>Sensible en cuanto se cruza con las mediciones</td></tr>
</tbody>
</table></div>
<p>Guarda las palabras exactas del cliente para el objetivo. «Subir andando hasta casa sin pararme en el segundo piso» te servirá más que «cardio» cuando elijas un test o midas un progreso.</p>

<h2>¿Qué datos de una ficha de cliente son datos de salud?</h2>
<p>El RGPD llama datos relativos a la salud a los datos personales sobre la salud física o mental de una persona que revelan información sobre su estado de salud, pasado, presente o futuro, sea cual sea la fuente: también cuenta lo que te explica el propio cliente, aunque no venga de un médico. Los antecedentes médicos, las enfermedades, los tratamientos y la discapacidad lo son por naturaleza. Una lesión también informa sobre la salud física, así que guárdala con el resto. Trata igual las respuestas a un <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">cuestionario de salud</a>.</p>
<p>El peso depende del contexto. Un peso elevado puede revelar una obesidad, y el peso cruzado con el número de pasos o con las calorías ingeridas puede convertirse en un dato de salud. La frecuencia cardiaca, el peso y la altura también pueden ser sensibles, sobre todo si vienen de un reloj o una pulsera de actividad. No he encontrado ninguna clasificación escrita de los datos de sueño, así que trátalos como datos de salud por prudencia. Tu ficha reúne todas estas mediciones en un mismo sitio: aplica al conjunto la regla más protectora.</p>
<p>Para guardar estos datos, pide al cliente su consentimiento explícito, separado de tus condiciones generales, después de explicarle qué recoges y para qué. En la UE, tratar datos de salud está prohibido en principio, salvo excepciones, y ese consentimiento es la primera: vale para fines concretos y el cliente puede retirarlo en cualquier momento, con la misma facilidad con que lo dio. En España se aplica además la Ley Orgánica 3/2018 (LOPDGDD), la autoridad de control es la Agencia Española de Protección de Datos (AEPD) y un menor solo puede dar su consentimiento por sí mismo a partir de los 14 años.</p>

<h2>¿Qué no debes escribir en la ficha de un cliente?</h2>
<ul>
<li><strong>Un diagnóstico.</strong> Escribe, por ejemplo: «le duele la rodilla derecha al subir escaleras, lo comenta el 12 de enero, derivado al médico». No añadas por tu cuenta el nombre de ninguna patología. No interpretas los datos de salud de un cliente: en cuanto una señal te plantea dudas, lo derivas a un médico.</li>
<li><strong>Detalles médicos que no necesitas.</strong> Te basta con saber si hay una indicación médica y qué límites fija. Una copia de una receta o de un informe médico no tiene sitio en tu ficha.</li>
<li><strong>Juicios sobre la persona.</strong> Un cliente puede pedirte acceso a sus datos y, en la UE, tienes como máximo un mes desde que recibes la solicitud para responderle; si es compleja o recibes muchas, puedes ampliar el plazo dos meses más, siempre que se lo comuniques dentro del primer mes y le expliques el motivo. Escribe cada línea como si fuera a leerla.</li>
<li><strong>Lo que no cambia nada en tu sesión.</strong> Para cada campo, pregúntate qué harías distinto con esa información. Si no tienes respuesta, borra el campo.</li>
</ul>

<h2>¿Cuánto tiempo guardar la ficha de un cliente, y dónde?</h2>
<p>Fija tu propio plazo de conservación, comunícaselo al cliente y borra la parte de salud cuando ya no la necesites, normalmente al terminar el servicio. Las facturas siguen otra regla: según la Agencia Tributaria, con carácter general se conservan durante el plazo de prescripción, 4 años, y más tiempo en algunos casos. Así que separa el expediente administrativo del deportivo: podrás borrar uno sin tocar el otro.</p>
<p>En la UE, aunque trabajes solo, la exención del registro de las actividades de tratamiento para empresas de menos de 250 empleados no se aplica si tratas datos de forma no ocasional o si tratas datos de salud, y tanto el seguimiento habitual de tus clientes como sus datos de salud entran en esos casos: tienes que llevar ese registro, al menos de esos tratamientos.</p>
<p>En cuanto al almacenamiento, en la UE tienes que proteger los datos de tus clientes con medidas técnicas y organizativas adecuadas al riesgo, como el cifrado. Con datos de salud, un chat de WhatsApp o un archivo sin protección encajan mal.</p>

<h2>¿Cómo mantener al día la ficha de un cliente?</h2>
<p>Ábrela en la <a href="/coachs/bilan-forme-premier-rendez-vous.html">valoración inicial</a> y, después de cada sesión, añade tres cosas: qué se ha hecho, cómo se ha sentido el cliente y qué cambiarás la próxima vez. Anota también los resultados de los <a href="/coachs/tests-physiques-nouveau-client.html">tests físicos</a> junto con las condiciones en que se hicieron.</p>
<p>Enseña estas cifras al cliente. Un metaanálisis de 138 ensayos y 19.951 personas (Harkin, 2016) indica que seguir el progreso ayuda a alcanzar los objetivos, con un efecto mayor cuando el resultado se registra físicamente o se hace público. No trata solo del ejercicio, así que tómalo como una referencia.</p>
<p>Relee el apartado de salud cada vez que cambie la situación. Un dolor nuevo te lleva a la misma regla: lo anotas, no lo interpretas, lo derivas.</p>
<p>Esta guía es solo informativa y no sustituye el consejo de un abogado ni de un delegado de protección de datos.</p>

<h2>Puntos clave</h2>
<ul>
<li>Siete apartados bastan, y cada campo debe cambiar algo en tu sesión.</li>
<li>Las lesiones, los antecedentes médicos y las respuestas al cuestionario son datos de salud. Trata igual el peso y el sueño, por prudencia.</li>
<li>Anota hechos sin interpretarlos, separa la salud de la facturación y fija un plazo de conservación.</li>
</ul>
""",
        "faq": [
            {"q": "¿Cómo hacer una ficha de cliente como entrenador personal?", "a": "Prevé siete apartados: contacto, condiciones, objetivo, práctica deportiva, salud, mediciones y seguimiento. Anota solo lo necesario y guarda la parte de salud aparte, porque en España la protegen el RGPD y la LOPDGDD. Sirve tanto una hoja de cálculo protegida como un software para entrenadores, siempre que el acceso sea seguro."},
            {"q": "¿Una ficha de cliente contiene datos de salud?", "a": "Casi siempre. Las lesiones, los antecedentes médicos y las respuestas al cuestionario son datos de salud, y el peso y el sueño también pueden serlo, sobre todo combinados con otras mediciones. Ante la duda, trátalos así y pide un consentimiento explícito, separado de tus condiciones generales."},
            {"q": "¿Cuánto tiempo debe guardar un entrenador personal los datos de sus clientes?", "a": "Fija tu propio plazo, comunícaselo al cliente y borra la parte de salud cuando ya no la necesites, normalmente al terminar el servicio. Las facturas siguen otra regla: según la Agencia Tributaria, con carácter general se conservan durante el plazo de prescripción, 4 años."},
        ],
        "sources": [
            {"t": "Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo (Reglamento general de protección de datos), artículos 4, 7, 9, 12, 30 y 32 y considerando 35. 2016.", "u": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Grupo de Trabajo del Artículo 29. Position Paper on the derogations from the obligation to maintain records of processing activities pursuant to Article 30(5) GDPR. 2018 (en inglés).", "u": "https://ec.europa.eu/newsroom/article29/items/624045"},
            {"t": "Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"},
            {"t": "Agencia Española de Protección de Datos. ¿Qué son los datos sensibles? Preguntas frecuentes.", "u": "https://www.aepd.es/preguntas-frecuentes/0-conceptos-basicos/FAQ-0004-que-son-los-datos-sensibles"},
            {"t": "Agencia Tributaria. Conservación de facturas y documentos sustitutivos. Folleto Actividades económicas. 2026.", "u": "https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_10-facturas/5_10_7-conservacion-facturas-documentos-sustitutivos.html"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
        ],
    },
    {
        "fr": "bilan-forme-premier-rendez-vous",
        "slug": "valoracion-inicial-primera-sesion",
        "title": "Valoración inicial: cómo hacer la primera sesión con un cliente nuevo",
        "seo_title": "Valoración inicial: cómo hacer la primera sesión",
        "description": "Valoración inicial con un cliente nuevo: cómo prepararla, qué preguntar en la primera sesión, qué hacer ante una señal de salud y cómo cerrar la reunión.",
        "body": """
<p>La respuesta corta: una buena <strong>valoración inicial</strong> sigue cuatro pasos: escuchar el objetivo, detectar lo que necesita una opinión médica, medir un punto de partida sencillo y proponer un plan claro. No he encontrado ninguna norma que fije su contenido ni su duración. Te sirve para decidir si puedes empezar, con qué intensidad y en qué dirección. No haces ningún diagnóstico.</p>

<h2>¿Qué preparar antes de la primera sesión con un cliente?</h2>
<p>Tres cosas que envías antes te evitan perder la mitad de la reunión:</p>
<ul>
<li><strong>El <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">cuestionario de salud</a></strong>, para rellenarlo antes de venir, con una explicación de qué haces con esos datos y la petición de consentimiento.</li>
<li><strong>Los detalles prácticos:</strong> lugar, ropa, agua, duración prevista.</li>
<li><strong>El tipo de cita:</strong> gratuita o de pago, lo dices desde el principio. La guía sobre la <a href="/coachs/seance-essai-coach-sportif.html">sesión de prueba</a> trata esa cuestión.</li>
</ul>
<p>Llámala valoración inicial o valoración de la condición física, nunca «chequeo de salud»: esa expresión crea una expectativa que no puedes cumplir.</p>

<h2>¿Cómo hacer una valoración inicial en una hora?</h2>
<p>No he encontrado ninguna recomendación que fije la duración. Aquí tienes un reparto de ejemplo en 60 minutos, para adaptar:</p>
<ol>
<li><strong>5 minutos, el marco.</strong> Explicas qué va a pasar y con qué se irá el cliente.</li>
<li><strong>20 minutos, escuchar.</strong> Objetivo, historial deportivo, limitaciones, preferencias.</li>
<li><strong>5 minutos, la seguridad.</strong> Repasas el cuestionario con el cliente.</li>
<li><strong>20 minutos, el movimiento.</strong> Dos o tres tests sencillos, con calentamiento si el protocolo lo prevé.</li>
<li><strong>10 minutos, los siguientes pasos.</strong> Resumes y haces tu propuesta.</li>
</ol>
<p>Los <a href="/coachs/tests-physiques-nouveau-client.html">tests físicos</a> fijan un punto de partida. Esperan si el cuestionario o la conversación plantean una duda de salud. En una primera sesión, deja margen: nada máximo con alguien a quien acabas de conocer, y ninguna prueba que corresponda a un médico. La Alta Autoridad de Salud de Francia (HAS) recuerda que la prueba de esfuerzo con análisis de gases se hace en centros especializados, con médicos formados.</p>

<h2>¿Qué preguntas hacer a un cliente nuevo?</h2>
<p>Preguntas abiertas, y un cliente que hable más que tú:</p>
<ul>
<li><strong>«¿Qué te trae por aquí justo ahora?»</strong> El motivo del momento suele decir más que el objetivo declarado.</li>
<li><strong>«¿Cómo sabrás que ha funcionado?»</strong> Obtienes un criterio concreto, con sus palabras.</li>
<li><strong>«¿Qué has probado antes y por qué lo dejaste?»</strong> Detectas los obstáculos antes de que vuelvan.</li>
<li><strong>«¿Cuántas sesiones te caben de verdad en la semana?»</strong> El plan se construye sobre esa respuesta.</li>
<li><strong>«¿Qué te gusta hacer y qué no harías nunca?»</strong> El cliente conserva el control de una parte de las decisiones.</li>
</ul>
<p>Este último punto importa. Una revisión de 66 estudios (Teixeira, 2012) muestra una relación constante entre las formas autónomas de motivación y el ejercicio, y la motivación intrínseca predice mejor la adherencia a largo plazo. La mayoría de esos estudios son descriptivos: establecen una relación, no una causa. La guía de la HAS va en la misma dirección para la entrevista motivacional: identificar los obstáculos y fijar con la persona objetivos realistas.</p>

<h2>¿Qué hacer si un cliente te cuenta un problema de salud?</h2>
<p>Desde 2015, el cribado del American College of Sports Medicine (ACSM) se basa en tres factores: la actividad actual, los signos o una enfermedad cardiovascular, metabólica o renal conocida, y la intensidad buscada. Esa actualización respondía a un exceso: demasiadas derivaciones innecesarias al médico, que pueden desanimar a la gente a moverse. La OMS considera además que, sin contraindicación, un visto bueno médico previo no suele ser necesario para una actividad ligera o moderada que no vaya más allá de caminar a paso ligero.</p>
<p>La HAS da la pauta cuando hay dudas:</p>
<ul>
<li><strong>Una respuesta positiva en el cuestionario:</strong> se recomienda una consulta médica antes de empezar.</li>
<li><strong>Signos que hacen pensar en una enfermedad:</strong> la persona deja en suspenso cualquier actividad, sea cual sea la intensidad, y consulta a su médico.</li>
<li><strong>45 años o más, sin ejercicio intenso regular y con un objetivo cercano al esfuerzo máximo:</strong> se aconseja una consulta médica.</li>
</ul>
<p>En los tres casos, no interpretas nada. Repites lo que has oído, explicas que la decisión corresponde a un médico, anotas la fecha y aplazas la parte de movimiento. Si un cliente tiene un dolor en el pecho o se desmaya delante de ti, llama al 112: es el número de emergencias en toda España y la llamada es gratuita desde fijos y móviles. El diagnóstico es cosa del médico, así que una frase como «seguro que es la tensión» no tiene sitio en una valoración.</p>

<h2>¿Cómo cerrar una valoración inicial?</h2>
<p>Resume en tres frases lo que has entendido, lo que has medido y lo que propones. Después da un objetivo con fecha, el ritmo de las sesiones y la fecha de la próxima revisión. Pon por escrito las condiciones y el precio antes de cualquier compromiso.</p>
<p>No prometas un resultado en cifras, porque no puedes garantizarlo ni demostrarlo. Di qué vas a medir y cuándo. En España no hay una ley estatal que regule el trabajo de entrenador personal: lo decide cada comunidad autónoma. En Cataluña o Madrid, por ejemplo, la ley exige una titulación o cualificación concreta, un seguro de responsabilidad civil si trabajas por tu cuenta y un trámite antes de empezar (la inscripción en el registro oficial de profesionales del deporte en Cataluña, una comunicación previa en Madrid); si trabajas en otra comunidad, revisa su ley del deporte. Esa misma tarde, pasa lo esencial a la <a href="/coachs/fiche-client-coach-sportif.html">ficha de cliente</a>, mientras tienes frescas las palabras exactas del cliente.</p>

<h2>Puntos clave</h2>
<ul>
<li>Envía el cuestionario antes de la sesión y haz que escuchar sea la parte más larga.</li>
<li>Ante la menor señal de salud, aplaza el movimiento y deriva al médico, sin interpretar.</li>
<li>Termina con un objetivo con fecha y unas condiciones por escrito, sin prometer resultados.</li>
</ul>
""",
        "faq": [
            {"q": "¿Qué se hace en una valoración inicial con un entrenador personal?", "a": "El entrenador escucha el objetivo y el historial deportivo, repasa el cuestionario de salud, hace dos o tres tests sencillos si nada lo impide y después propone un plan. Esta reunión valora la condición física. No sustituye una consulta médica."},
            {"q": "¿Cuánto dura una valoración inicial?", "a": "No he encontrado ninguna recomendación que fije la duración. Una hora es un formato práctico: un tercio para escuchar, un tercio para el movimiento y el resto para el marco, la seguridad y los siguientes pasos. Adáptala al cliente y a los tests que tengas previstos."},
            {"q": "¿Qué preguntar a un cliente en la primera sesión?", "a": "Qué le trae ahora, cómo sabrá que ha funcionado, qué ha probado ya, cuánto tiempo tiene de verdad, qué le gusta y qué no quiere hacer. Añade el cuestionario de salud y deriva al cliente a un médico en cuanto una respuesta lo pida."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (en francés).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Teixeira PJ, Carraça EV, Markland D, et al. Exercise, physical activity, and self-determination theory: a systematic review. <em>Int J Behav Nutr Phys Act</em>. 2012.", "u": "https://doi.org/10.1186/1479-5868-9-78"},
            {"t": "administracion.gob.es. Servicios prestados a través de números de urgencia nacionales (112). 2026.", "u": "https://administracion.gob.es/tu-espacio-europeo/derechos-obligaciones/ciudadanos/asistencia-sanitaria/numeros-urgencia"},
            {"t": "Ley 39/2022, de 30 de diciembre, del Deporte, disposición final sexta. BOE, texto consolidado.", "u": "https://www.boe.es/eli/es/l/2022/12/30/39/con"},
            {"t": "Ley 3/2008, de 23 de abril, del ejercicio de las profesiones del deporte (Cataluña), artículos 4, 8 y 11. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2008-9292"},
            {"t": "Ley 6/2016, de 24 de noviembre, por la que se ordena el ejercicio de las profesiones del deporte en la Comunidad de Madrid, artículos 10, 13, 16, 22 y 24. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2017-3069"},
        ],
    },
    {
        "fr": "questionnaire-sante-avant-le-sport-client",
        "slug": "cuestionario-salud-antes-del-ejercicio",
        "title": "Cuestionario de salud antes del ejercicio: qué preguntar a un cliente",
        "seo_title": "Cuestionario de salud antes del ejercicio: qué preguntar",
        "description": "Cuestionario de salud antes del ejercicio: qué puede preguntar un entrenador personal, cómo funcionan los derechos del PAR-Q+ y qué hacer si el cliente dice sí.",
        "body": """
<p>La respuesta corta: un <strong>cuestionario de salud antes del ejercicio</strong> pregunta por la actividad actual, las enfermedades conocidas, los síntomas nuevos y la intensidad buscada. Que estés obligado a usarlo depende de las normas que se apliquen a tu actividad, pero la herramienta es útil en cualquier caso. La Alta Autoridad de Salud de Francia (HAS) recomienda un cuestionario autoadministrado a toda persona que quiera empezar o aumentar una actividad de intensidad al menos moderada, e indica que un profesional del ejercicio puede proponerlo. Si un cliente responde que sí, no interpretas: lo derivas a un médico antes de empezar.</p>

<h2>¿Necesita un entrenador personal un cuestionario de salud o un certificado médico?</h2>
<p>Depende de las normas que se apliquen a tu actividad. En España no hay una ley estatal que regule el trabajo de entrenador personal: lo decide cada comunidad autónoma, y en Madrid, por ejemplo, la ley exige una titulación concreta y, si trabajas por tu cuenta, un seguro de responsabilidad civil. Revisa la ley del deporte de la tuya. Aunque ninguna norma te lo exija, normalmente puedes incluir un cuestionario o un certificado médico como condición en tu contrato con el cliente.</p>

<h2>PAR-Q+ o cuestionario propio: ¿cuál usar?</h2>
<div class="tablewrap"><table>
<caption>Fuente: HAS 2022 y condiciones de uso del PAR-Q+, consultadas el 31 de octubre de 2026.</caption>
<thead><tr><th>Opción</th><th>Uso</th><th>Qué saber</th></tr></thead>
<tbody>
<tr><td>PAR-Q+</td><td>Cribado antes de la actividad, de 15 a 69 años</td><td>7 preguntas, texto protegido</td></tr>
<tr><td>Tu propio cuestionario</td><td>Lo que cambia tu sesión</td><td>Redáctalo tú, sin copiar el PAR-Q+</td></tr>
</tbody>
</table></div>
<p>El PAR-Q+ pide prudencia. Sus condiciones exigen un permiso previo por escrito para modificarlo o integrarlo en una app, una web, un software o una encuesta online. Citar la fuente no equivale a tener permiso. Las versiones oficiales sin modificar son hoy gratuitas para ciertos usos individuales, clínicos, educativos y de investigación no comercial. Las condiciones no mencionan a los entrenadores, aunque la web ofrece recursos para profesionales del ejercicio, y el uso comercial puede tener un coste. Ante la duda, escribe al titular de los derechos.</p>
<p>Lo más sencillo: invita al cliente a rellenarlo él mismo en la web oficial, eparmedx.com. Encontrar el texto reproducido en otro sitio no te da permiso para copiarlo en tu formulario.</p>

<h2>¿Qué preguntas debe incluir un cuestionario de salud?</h2>
<p>Para tu propio cuestionario, parte de la lógica del American College of Sports Medicine (ACSM), que se resume en tres factores, y añade lo que sirva a tu sesión:</p>
<ul>
<li><strong>La actividad actual.</strong> Cuántas sesiones por semana, de qué duración, a qué intensidad.</li>
<li><strong>Lo que ya se sabe.</strong> Una enfermedad cardiovascular, metabólica o renal diagnosticada. Basta con sí o no.</li>
<li><strong>Lo nuevo.</strong> Una señal inusual, en reposo o durante el esfuerzo.</li>
<li><strong>La intensidad buscada.</strong> Lo que el cliente quiere hacer, y a qué nivel.</li>
<li><strong>Lo que limita el movimiento.</strong> Una molestia, una operación reciente, un embarazo: todo lo que te obliga a adaptar un ejercicio.</li>
</ul>
<p>Pasa cada pregunta por el mismo filtro: ¿qué cambias en tu sesión si la respuesta es sí? Si no cambia nada, quítala.</p>
<p>La HAS añade dos referencias de edad. A partir de 45 años, sin actividad intensa regular y con un objetivo cercano al esfuerzo máximo, se aconseja una consulta médica. A partir de 70 años, se recomienda para una actividad de intensidad al menos alta.</p>

<h2>¿Qué hacer si un cliente responde que sí?</h2>
<p>La HAS es clara. Una respuesta positiva: se recomienda una consulta médica antes de empezar. Signos o síntomas que hacen pensar en una enfermedad: la persona deja la actividad en suspenso y consulta a su médico. Todo negativo: puede ser más activa, con las precauciones habituales.</p>
<p>Tu papel termina ahí. No juzgas la gravedad ni tranquilizas. Anotas la fecha, esperas a que el cliente te confirme la opinión médica recibida y sus posibles límites, y después adaptas. Repite el cuestionario cada vez que cambie la situación.</p>

<h2>¿Cómo tratar las respuestas del cuestionario?</h2>
<p>Las respuestas a un cuestionario de salud son datos de salud. En España están especialmente protegidas: además del RGPD se aplica la Ley Orgánica 3/2018 (LOPDGDD), la autoridad de control es la Agencia Española de Protección de Datos (AEPD) y un menor solo puede dar su consentimiento por sí mismo a partir de los 14 años. En la UE, tratar datos de salud está prohibido en principio, salvo excepciones; la primera es el consentimiento explícito de tu cliente para uno o varios fines concretos, que puede retirar en cualquier momento, con la misma facilidad con que lo dio. Pídelo separado de tus condiciones generales, después de explicarle qué recoges y para qué. Queda un punto abierto: el consentimiento solo vale si la persona puede negarse de verdad, así que rechazar a un cliente que deja el cuestionario en blanco no es una cuestión resuelta. Guarda las respuestas en el apartado de salud de tu <a href="/coachs/fiche-client-coach-sportif.html">ficha de cliente</a>.</p>
<p>Esta guía es solo informativa y no sustituye el consejo de un médico ni de un abogado.</p>

<h2>Puntos clave</h2>
<ul>
<li>Que el cuestionario sea obligatorio depende de las normas que se apliquen a tu actividad, pero la HAS recomienda uno antes de empezar.</li>
<li>El PAR-Q+ no se puede copiar en un formulario sin permiso por escrito.</li>
<li>Cuando un cliente responde que sí, no interpretas: lo derivas a un médico antes de empezar.</li>
</ul>
""",
        "faq": [
            {"q": "¿Es obligatorio el PAR-Q+?", "a": "Depende de las normas que se apliquen a tu actividad; en España no hay una ley estatal sobre la profesión: lo decide cada comunidad autónoma. La Alta Autoridad de Salud de Francia (HAS) recomienda un cuestionario de este tipo antes de empezar o de aumentar una actividad de intensidad al menos moderada. Las condiciones del PAR-Q+ prohíben modificarlo o integrarlo en una herramienta online sin permiso por escrito."},
            {"q": "¿Puede un entrenador personal pedir un certificado médico?", "a": "Sí, normalmente puedes ponerlo como condición en tu contrato con el cliente. Que una norma te lo exija depende de las reglas que se apliquen a tu actividad. Si las respuestas de un cliente piden una consulta médica, espera a esa opinión antes de empezar."},
            {"q": "¿Qué hacer si un cliente responde que sí en el cuestionario de salud?", "a": "No interpretes la respuesta ni le quites importancia. Se recomienda una consulta médica antes de empezar, y un cliente con signos o síntomas que hagan pensar en una enfermedad deja la actividad en suspenso y consulta a su médico. Anota la fecha y adapta cuando el cliente te confirme la opinión médica y sus posibles límites."},
        ],
        "sources": [
            {"t": "HAS. Consultation et prescription médicale d'activité physique à des fins de santé chez l'adulte. Guide. 2022 (en francés).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2018-10/guide_aps_vf.pdf"},
            {"t": "Riebe D, Franklin BA, Thompson PD, et al. Updating ACSM's Recommendations for Exercise Preparticipation Health Screening. <em>Med Sci Sports Exerc</em>. 2015.", "u": "https://doi.org/10.1249/MSS.0000000000000664"},
            {"t": "PAR-Q+ Collaboration. Terms and Conditions. 2026.", "u": "https://eparmedx.com/terms-and-conditions/"},
            {"t": "Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo (Reglamento general de protección de datos), artículos 4, 7 y 9. 2016.", "u": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"},
            {"t": "Agencia Española de Protección de Datos. ¿Qué son los datos sensibles? Preguntas frecuentes.", "u": "https://www.aepd.es/preguntas-frecuentes/0-conceptos-basicos/FAQ-0004-que-son-los-datos-sensibles"},
            {"t": "Ley 39/2022, de 30 de diciembre, del Deporte, disposición final sexta. BOE, texto consolidado.", "u": "https://www.boe.es/eli/es/l/2022/12/30/39/con"},
            {"t": "Ley 6/2016, de 24 de noviembre, por la que se ordena el ejercicio de las profesiones del deporte en la Comunidad de Madrid, artículos 10, 16 y 24. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2017-3069"},
        ],
    },
    {
        "fr": "tests-physiques-nouveau-client",
        "slug": "tests-fisicos-cliente-nuevo",
        "title": "Tests físicos para un cliente nuevo: ¿cuáles elegir?",
        "description": "Tests físicos para un cliente nuevo: cuáles elegir según su perfil, cómo hacerlos de forma fiable, cómo leer los resultados y qué pensar del test de Ruffier.",
        "body": """
<p>La respuesta corta: no he encontrado ninguna batería oficial de tests. Entre los <strong>tests físicos para un cliente nuevo</strong>, elige tres o cuatro ligados a su objetivo: uno de resistencia, uno de tren inferior, uno de tren superior y uno de equilibrio si su perfil lo pide. Sirven para comparar al cliente consigo mismo. No hacen ningún diagnóstico.</p>

<h2>¿Qué tests físicos elegir para cada cliente?</h2>
<p>La Alta Autoridad de Salud de Francia (HAS) detalla los tests de campo más habituales y recuerda que ningún test mide por sí solo la fuerza o la flexibilidad de todo el cuerpo. La tabla combina sus referencias con algunos estudios.</p>
<div class="tablewrap"><table>
<caption>Fuente: HAS 2022; Holland 2014; Jones 1999; Penry 2011.</caption>
<thead><tr><th>Capacidad</th><th>Test</th><th>Perfil</th><th>Qué saber</th></tr></thead>
<tbody>
<tr><td>Resistencia</td><td>Marcha de 6 minutos</td><td>Principiante, persona mayor, vuelta al ejercicio</td><td>Validación clínica, no deportiva</td></tr>
<tr><td>Resistencia</td><td>Carrera de 12 minutos (test de Cooper)</td><td>Adulto joven que ya entrena</td><td>Esfuerzo intenso, toma con cautela la estimación del VO2 máx</td></tr>
<tr><td>Piernas</td><td>Levantarse de la silla durante 30 segundos</td><td>Persona mayor, principiante</td><td>Silla sin reposabrazos, sin usar las manos. Validado a partir de 60 años</td></tr>
<tr><td>Tren superior</td><td>Flexiones sin parar</td><td>Adulto sin molestias en el hombro</td><td>Mezcla fuerza y resistencia</td></tr>
<tr><td>Fuerza</td><td>Test de 10 a 15 RM</td><td>Principiante, persona mayor, vuelta al ejercicio</td><td>Específico de cada ejercicio</td></tr>
<tr><td>Flexibilidad</td><td>Flexión de tronco sentado (sit and reach)</td><td>Cliente sin dolor de espalda</td><td>Sobre todo los isquiotibiales</td></tr>
<tr><td>Equilibrio</td><td>Apoyo sobre una pierna con los ojos cerrados</td><td>Persona mayor</td><td>Tres intentos, el mejor tiempo. Quédate a su lado, cerca de un apoyo</td></tr>
</tbody>
</table></div>
<p>Dos ejemplos de selección. Para una persona sedentaria de 55 años que vuelve al ejercicio: marcha de 6 minutos, levantarse de la silla y apoyo sobre una pierna. Para alguien activo de 30 años que busca fuerza: carrera de 12 minutos, flexiones y un 8 RM en dos ejercicios que domine, repartidos en dos sesiones.</p>
<p>Antes de cualquier test, relee el <a href="/coachs/questionnaire-sante-avant-le-sport-client.html">cuestionario de salud</a>. Si pide una consulta médica, el test espera.</p>

<h2>¿Cómo hacer los tests físicos sin falsear los resultados?</h2>
<p>Un test solo vale si puedes repetirlo de forma idéntica. La norma técnica de la European Respiratory Society y la American Thoracic Society (ERS/ATS; Holland, 2014) considera que las pruebas de marcha son válidas, fiables y sensibles al cambio en la enfermedad respiratoria crónica, y subraya lo sensibles que son a pequeñas diferencias de método. Recomienda dos intentos de la marcha de 6 minutos, separados por al menos 30 minutos, para fijar una referencia estable.</p>
<ul>
<li><strong>Mismas condiciones.</strong> Mismo lugar, mismo recorrido, misma hora del día, mismo calzado, misma silla. La HAS describe la marcha de 6 minutos alrededor de dos conos separados 30 m. La norma ERS/ATS pide una superficie plana y al menos 30 m: en un recorrido más corto, olvídate de los valores de referencia.</li>
<li><strong>Mismas palabras.</strong> Escribe tus instrucciones y léelas en voz alta. Para la marcha, la norma prevé una frase fija cada minuto, y nada más. Si el cliente se para, el cronómetro sigue corriendo.</li>
<li><strong>Misma preparación.</strong> Para la marcha de 6 minutos, nada de calentamiento ni de esfuerzo intenso en las 2 horas previas, según esa norma. Para los demás tests, mantén el mismo calentamiento.</li>
<li><strong>Un registro escrito.</strong> Anota las condiciones junto al resultado, o acabarás comparando dos cosas distintas.</li>
</ul>
<p>Si el cliente refiere dolor, mareo, una falta de aire inusual o calambres, o si se tambalea o palidece, detén el test y derívalo a un médico. Ante un dolor en el pecho o un desmayo, haz que se siente o se tumbe y llama al 112: es el número de emergencias en toda España y la llamada es gratuita desde fijos y móviles.</p>

<h2>¿Puede un cliente nuevo hacer un test máximo?</h2>
<p>No en la primera sesión, salvo que sea un cliente entrenado que ya conozca el test. La HAS describe el 1RM como un indicador fiable de la fuerza, y los tests de 4 RM u 8 RM como una estimación fiable. Considera más seguros los tests de 10 a 15 RM para las personas mayores, desentrenadas o con una enfermedad crónica. Incluso con 4 u 8 repeticiones, espera a que la técnica esté limpia. La carrera de 12 minutos ya exige un esfuerzo sostenido, así que resérvala para un cliente acostumbrado a la intensidad.</p>
<p>No confundas estos tests con una prueba de esfuerzo clínica, que se hace con control del electrocardiograma y de la tensión arterial, en un entorno clínico.</p>

<h2>¿Es fiable el test de Ruffier?</h2>
<p>Sigue siendo un indicador sencillo, poco preciso para estimar la condición cardiorrespiratoria. En un estudio con 81 adultos sanos (Sartor, 2016), el índice de Ruffier-Dickson tuvo una correlación de -0,40 con la condición física medida y explicó el 15 % de la variabilidad. No aparece en la tabla de tests de la HAS. Si tu cliente insiste, compara sus resultados entre sí y no calcules un VO2 máx a partir de ellos.</p>

<h2>¿Cómo leer los resultados y cuándo repetir los tests?</h2>
<p>Compara al cliente consigo mismo: eso es una <a href="/methode/ligne-de-base.html">línea base</a>. Los valores de referencia describen a otras poblaciones. Para la marcha de 6 minutos, Enright (1998) encontró una mediana de 576 m en hombres y 494 m en mujeres, en 290 adultos sanos de 40 a 80 años, y las ecuaciones explican en torno al 40 % de la varianza. Para la carrera de 12 minutos, Penry (2011) informa de una buena fiabilidad en adultos jóvenes, pero pide cautela al estimar un VO2 máx a partir de ella.</p>
<p>Una diferencia con un valor de referencia no te permite concluir nada sobre la salud del cliente. Si un resultado te sorprende, derívalo a un médico sin comentarlo. El test de levantarse de la silla, por su parte, se validó en 76 adultos de más de 60 años (Jones, 1999): sus valores no sirven para un cliente de 30.</p>
<p>No he encontrado ninguna frecuencia oficial para repetir los tests. Lo más lógico es repetirlos al final de un bloque del <a href="/coachs/creer-programme-personnalise-client.html">plan de entrenamiento</a>, en las mismas condiciones, y enseñar la evolución en el <a href="/coachs/bilan-mensuel-client-coaching.html">informe mensual de progreso</a>.</p>

<h2>Puntos clave</h2>
<ul>
<li>Tres o cuatro tests ligados al objetivo bastan, elegidos según el perfil.</li>
<li>Usa siempre el mismo protocolo, anota las condiciones y compara al cliente consigo mismo.</li>
<li>Un test no hace ningún diagnóstico: ante la menor señal de alarma, para y deriva al médico.</li>
</ul>
""",
        "faq": [
            {"q": "¿Qué test físico debe hacer un principiante?", "a": "La marcha de 6 minutos para la resistencia, levantarse de la silla durante 30 segundos para las piernas y, si hace falta, un test de 10 a 15 RM. Son tests fáciles de dosificar. Relee siempre el cuestionario de salud antes de empezar."},
            {"q": "¿Es fiable el test de Ruffier?", "a": "Es un indicador sencillo, poco preciso para estimar la condición cardiorrespiratoria. En un estudio con 81 adultos sanos, explicó el 15 % de la variabilidad. No aparece en la tabla de tests de la Alta Autoridad de Salud de Francia (HAS)."},
            {"q": "¿Cada cuánto hay que repetir los tests a un cliente?", "a": "No he encontrado ninguna frecuencia oficial. Lo más lógico es repetirlos al final de un bloque de entrenamiento, en las mismas condiciones, para comparar al cliente consigo mismo."},
        ],
        "sources": [
            {"t": "HAS. Guide des connaissances sur l'activité physique et la sédentarité. 2022 (en francés).", "u": "https://www.has-sante.fr/upload/docs/application/pdf/2022-08/guide_connaissance_ap_sedentarite_vf.pdf"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Enright PL, Sherrill DL. Reference equations for the six-minute walk in healthy adults. <em>Am J Respir Crit Care Med</em>. 1998.", "u": "https://doi.org/10.1164/ajrccm.158.5.9710086"},
            {"t": "Jones CJ, Rikli RE, Beam WC. A 30-s chair-stand test as a measure of lower body strength in community-residing older adults. <em>Res Q Exerc Sport</em>. 1999.", "u": "https://doi.org/10.1080/02701367.1999.10608028"},
            {"t": "Penry JT, Wilcox AR, Yun J. Validity and reliability analysis of Cooper's 12-minute run and the multistage shuttle run in healthy adults. <em>J Strength Cond Res</em>. 2011.", "u": "https://doi.org/10.1519/JSC.0b013e3181cc2423"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "administracion.gob.es. Servicios prestados a través de números de urgencia nacionales (112). 2026.", "u": "https://administracion.gob.es/tu-espacio-europeo/derechos-obligaciones/ciudadanos/asistencia-sanitaria/numeros-urgencia"},
        ],
    },
    {
        "fr": "creer-programme-personnalise-client",
        "slug": "plan-entrenamiento-personalizado-cliente",
        "title": "Cómo hacer un plan de entrenamiento personalizado: el método",
        "description": "Cómo hacer un plan de entrenamiento personalizado para un cliente: de la valoración inicial a la progresión, con las referencias de la OMS y del ACSM.",
        "body": """
<p>La respuesta corta: un <strong>plan de entrenamiento personalizado</strong> parte de la valoración del cliente, nunca de una plantilla. Empieza por su objetivo, su tiempo disponible real y su nivel. Fija el volumen y la intensidad, elige un reparto de sesiones que vaya a mantener, escribe una regla de progresión y ajusta según lo que te cuente. El posicionamiento del American College of Sports Medicine (ACSM) publicado en 2026 muestra que pocas variables cambian de verdad los resultados, así que céntrate en esas.</p>

<h2>¿Qué necesitas saber antes de hacer un plan de entrenamiento?</h2>
<p>Cinco datos lo deciden casi todo. Salen de la <a href="/coachs/bilan-forme-premier-rendez-vous.html">valoración inicial</a> y de los <a href="/coachs/tests-physiques-nouveau-client.html">tests físicos</a>:</p>
<ul>
<li><strong>El objetivo</strong>, con las palabras del cliente y una fecha.</li>
<li><strong>El tiempo disponible real:</strong> el número de sesiones que mantendrá en una semana complicada.</li>
<li><strong>El nivel:</strong> lo que hace hoy y lo que ha hecho antes.</li>
<li><strong>El lugar y el material.</strong></li>
<li><strong>Los límites:</strong> molestias que comenta, una consulta médica pendiente o límites fijados por un médico.</li>
</ul>
<p>Si hay una consulta médica pendiente, el plan también espera. Si el médico ha fijado límites, aplícalos tal cual, sin reinterpretarlos.</p>

<h2>¿Cómo fijar el volumen y la intensidad?</h2>
<p>Dos referencias bastan para situarte: la OMS para la salud y el ACSM para el entrenamiento de fuerza, con 137 revisiones sistemáticas y más de 30.000 participantes, todos adultos sanos.</p>
<div class="tablewrap"><table>
<caption>Fuente: OMS 2020; ACSM 2026; Schoenfeld 2017. Adultos sanos.</caption>
<thead><tr><th>Objetivo</th><th>Referencia</th><th>Fuente</th></tr></thead>
<tbody>
<tr><td>Salud, vuelta al ejercicio</td><td>De 150 a 300 min de actividad moderada por semana, o de 75 a 150 min de actividad vigorosa, más trabajo de fuerza de todos los grandes grupos musculares 2 o más días</td><td>OMS</td></tr>
<tr><td>Personas mayores</td><td>Dentro de ese volumen, actividad variada centrada en el equilibrio y la fuerza, 3 o más días por semana</td><td>OMS</td></tr>
<tr><td>Fuerza</td><td>80 % del 1RM o más, de 2 a 3 series, 2 o más sesiones por semana</td><td>ACSM</td></tr>
<tr><td>Hipertrofia</td><td>10 o más series por semana y grupo muscular. Más volumen, más ganancia (15 estudios)</td><td>ACSM, Schoenfeld</td></tr>
<tr><td>Potencia</td><td>Del 30 al 70 % del 1RM, fase concéntrica rápida</td><td>ACSM</td></tr>
</tbody>
</table></div>
<p>Estas cifras describen el destino, mucho más allá de la primera semana. La OMS aconseja a quien esté lejos de ellas empezar poco a poco y aumentar después la frecuencia, la intensidad y la duración. Comparado con no entrenar, el trabajo de fuerza ya mejora la fuerza, el tamaño muscular y el equilibrio. Para un principiante, basta con un primer plan sencillo.</p>
<p>Otros ajustes importan menos de lo que se cree. Según el ACSM, entrenar hasta el fallo muscular o cambiar el tipo de material no cambió los resultados de forma constante. Un cliente sin gimnasio puede seguir un plan de verdad, siempre que la carga o las repeticiones puedan subir.</p>

<h2>¿Cómo repartir las sesiones en la semana?</h2>
<p>Elige según el calendario del cliente. Un metaanálisis de 14 estudios y 392 personas (Ramos-Campo, 2024) no encontró diferencias significativas de fuerza ni de masa muscular entre el entrenamiento de cuerpo completo y la rutina dividida cuando el volumen es igual. Los autores concluyen que la elección puede seguir las preferencias.</p>
<p>Aquí tienes una lógica de ejemplo, para ajustar:</p>
<ul>
<li><strong>2 sesiones:</strong> cuerpo completo cada vez.</li>
<li><strong>3 sesiones:</strong> cuerpo completo, o una rotación de tren superior y tren inferior.</li>
<li><strong>4 sesiones o más:</strong> una rutina dividida se vuelve posible, si el cliente las mantiene de verdad.</li>
</ul>
<p>Piensa en la semana que falla: si se cae una sesión, una rutina dividida deja atrás un grupo muscular y una de cuerpo completo no. Para un objetivo de fuerza, pon el ejercicio prioritario al principio de la sesión, como señala el ACSM.</p>

<h2>¿Cómo hacer progresar un plan de entrenamiento?</h2>
<p>Escribe la regla en el plan, para que el cliente sepa qué activa el siguiente paso. Ejemplo: cuando todas las series lleguen a 12 repeticiones limpias, sube la carga y las repeticiones vuelven a 8.</p>
<p>Tienes varias palancas. Un ensayo con personas entrenadas (Plotkin, 2022, 43 al inicio, 38 al final) muestra que añadir repeticiones o añadir carga da adaptaciones comparables en 8 semanas, con una ligera ventaja de la carga para la fuerza máxima. Eso ayuda en casa, cuando la carga disponible llega a su tope. El estudio es corto y solo trata cuádriceps y gemelos.</p>
<p>Cambia una variable cada vez, para saber qué produjo qué. Según el ACSM, la periodización no cambió los resultados de forma constante: reserva los planes complejos para un cliente avanzado y repasa <a href="/articles/periodisation-entrainement-bases.html">las bases de la periodización</a> si lo necesitas.</p>

<h2>¿Cuándo ajustar el plan y dónde termina tu papel?</h2>
<p>Después de cada sesión, recoge el esfuerzo percibido, las molestias y lo que se ha saltado. Si el cliente falla dos veces seguidas el mismo tipo de sesión, cambia el plan antes de hablar de motivación.</p>
<p>Tres límites no se mueven:</p>
<ul>
<li><strong>La salud.</strong> Según la OMS, quien desarrolla síntomas nuevos al aumentar su actividad debe consultar a un profesional sanitario. Paras, derivas y no interpretas.</li>
<li><strong>La nutrición.</strong> Puedes dar pautas generales. Cuanto más personal es el consejo, mayor es el riesgo, sobre todo si hay una enfermedad de por medio.</li>
<li><strong>El marco legal.</strong> En España no hay una ley estatal que regule el trabajo de entrenador personal: lo decide cada comunidad autónoma, y en Navarra o el País Vasco, por ejemplo, la ley exige una titulación concreta y, si trabajas por tu cuenta, un seguro de responsabilidad civil; si trabajas en otra comunidad, revisa su ley del deporte. Si entrenas online, esas dos leyes también se aplican cuando tienes allí tu sede o domicilio, y exigen que las webs y apps con planes de entrenamiento indiquen quién los elabora y con qué cualificación.</li>
</ul>

<h2>Puntos clave</h2>
<ul>
<li>El plan sale de la valoración: objetivo, tiempo real, nivel, material y límites.</li>
<li>Fija pocas variables, con una regla de progresión por escrito y un reparto de sesiones que el cliente vaya a mantener.</li>
<li>Síntomas nuevos, nutrición y normas de tu comunidad autónoma: estos límites van antes que el plan.</li>
</ul>
""",
        "faq": [
            {"q": "¿Cómo hacer un plan de fuerza personalizado para un cliente?", "a": "Parte de la valoración: objetivo, tiempo disponible real, nivel, material y límites. Después fija el volumen y la intensidad según el objetivo, elige un reparto de sesiones que vaya a mantener, escribe una regla de progresión y ajusta según lo que te cuente."},
            {"q": "¿Cuántas sesiones por semana debe tener un plan de entrenamiento?", "a": "La OMS recomienda trabajar la fuerza de todos los grandes grupos musculares 2 o más días por semana, y el ACSM, 2 o más sesiones para ganar fuerza. Para un principiante, dos sesiones de cuerpo completo son un buen comienzo. El número correcto es el que el cliente mantiene en una semana complicada."},
            {"q": "¿Puede un entrenador personal incluir una dieta en el plan?", "a": "Puedes dar pautas generales, sin presentarte como dietista-nutricionista. La frontera con el consejo individual no es nítida: cuanto más personal es el consejo, mayor es el riesgo, sobre todo si hay una enfermedad. En ese caso, deriva al cliente a un médico o a un dietista-nutricionista."},
        ],
        "sources": [
            {"t": "Currier BS, D'Souza AC, Singh MAF, et al. American College of Sports Medicine Position Stand. Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. <em>Med Sci Sports Exerc</em>. 2026.", "u": "https://doi.org/10.1249/MSS.0000000000003897"},
            {"t": "Schoenfeld BJ, Ogborn D, Krieger JW. Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis. <em>J Sports Sci</em>. 2017.", "u": "https://doi.org/10.1080/02640414.2016.1210197"},
            {"t": "Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>Br J Sports Med</em>. 2020.", "u": "https://doi.org/10.1136/bjsports-2020-102955"},
            {"t": "Ramos-Campo DJ, Benito-Peinado PJ, Andreu-Caravaca L, et al. Efficacy of Split Versus Full-Body Resistance Training on Strength and Muscle Growth: A Systematic Review With Meta-Analysis. <em>J Strength Cond Res</em>. 2024.", "u": "https://doi.org/10.1519/JSC.0000000000004774"},
            {"t": "Plotkin D, Coleman M, Van Every D, et al. Progressive overload without progressing load? The effects of load or repetition progression on muscular adaptations. <em>PeerJ</em>. 2022.", "u": "https://doi.org/10.7717/peerj.14142"},
            {"t": "Ley 39/2022, de 30 de diciembre, del Deporte, disposición final sexta. BOE, texto consolidado.", "u": "https://www.boe.es/eli/es/l/2022/12/30/39/con"},
            {"t": "Ley Foral 18/2019, de 4 de abril, sobre acceso y ejercicio de las profesiones del deporte en Navarra, artículos 1, 7, 15 y 22. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2019-6778"},
            {"t": "Ley 8/2022, de 30 de junio, sobre acceso y ejercicio de profesiones de la actividad física y del deporte en la Comunidad Autónoma del País Vasco, artículos 2, 8, 15 y 18. BOE.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2022-14085"},
        ],
    },
    {
        "fr": "fideliser-clients-coaching-sportif",
        "slug": "fidelizar-clientes-entrenador-personal",
        "title": "Por qué se van tus clientes: cómo fidelizar como entrenador personal",
        "seo_title": "Fidelizar clientes como entrenador personal: por qué se van",
        "description": "Fidelizar clientes como entrenador personal: por qué se van, qué muestran de verdad los estudios sobre el abandono y cómo calcular tu tasa de retención real.",
        "body": """
<p>La respuesta corta: para <strong>fidelizar clientes como entrenador personal</strong>, empieza por medir quién se va y por qué, porque ninguna estadística lo hará por ti. No he encontrado ninguna tasa de abandono propia de los entrenadores independientes. La investigación respalda sobre todo tres palancas sencillas: un objetivo por escrito, un progreso registrado y un seguimiento regular. El resto está en tu propia lista de clientes.</p>

<h2>¿Cuántos clientes abandonan de verdad?</h2>
<p>La única cifra sólida que he conservado viene de un solo gimnasio de Río de Janeiro. Sperandei y sus colegas siguieron a 5.240 socios: el 63 % lo había dejado antes del tercer mes y menos del 4 % superó los doce meses de actividad continua. El estudio, publicado en 2016, trata un único gimnasio, se basa en sus datos de socios y se hizo en un entorno sin supervisión, como dice su título. Así que no vale para todos los gimnasios ni para un cliente que entrena con un entrenador personal. Desconfía de los porcentajes de abandono que circulan sin referencia.</p>
<p>Tu cifra real se calcula en diez minutos. Toma tus clientes activos al inicio de un trimestre y cuenta cuántos siguen al final, sin sumar los nuevos. Ejemplo de cálculo: 12 clientes el 1 de enero y 9 todavía activos el 31 de marzo, es decir, 9 ÷ 12 = 75 % de retención en tres meses. Con tan pocos clientes, cada baja pesa más de 8 puntos. Lee esta tasa sobre el año y fíjate sobre todo en los motivos.</p>

<h2>¿Por qué se van los clientes de un entrenador personal?</h2>
<p>Ninguno de los estudios citados aquí responde a eso para el cliente de un entrenador independiente. Tu mejor fuente siguen siendo tus antiguos clientes. Esta clasificación de trabajo, sin valor estadístico, te ayuda a ordenar cada baja:</p>
<ul>
<li><strong>Baja prevista:</strong> el objetivo se ha cumplido, o el cliente ya sabe entrenar solo. Es un éxito, y quizá una futura recomendación.</li>
<li><strong>Baja forzada:</strong> una mudanza, el presupuesto, un nuevo horario de trabajo, un nacimiento, la salud. A veces puedes ofrecer un formato más ligero o a distancia.</li>
<li><strong>Baja evitable:</strong> un progreso que no se ve, sesiones que parecen todas iguales, un objetivo que nunca se revisa, un horario que dejó de encajar, una relación que se ha apagado.</li>
</ul>
<p>Haz tres preguntas a cada cliente que se va: qué te hizo decidirte, qué te habría hecho quedarte, qué le dirías a alguien que se plantea empezar. Apunta las respuestas palabra por palabra. «Ya no me lo puedo permitir» también puede querer decir «ya no veo qué saco de esto». Si el mismo motivo aparece varias veces en un año, has encontrado tu prioridad número uno.</p>

<h2>¿Qué hace que un cliente se quede a largo plazo?</h2>
<p>Los trabajos que he seleccionado no tratan el entrenamiento personal individual con un profesional independiente, pero marcan una dirección.</p>
<ul>
<li><strong>Registra el progreso.</strong> El metaanálisis de Harkin y sus colegas (2016, 138 ensayos, 19.951 personas) encuentra un efecto medio de 0,40 sobre el logro de objetivos, mayor cuando el resultado se registra o se comparte. No se limita al ejercicio.</li>
<li><strong>Ve más allá del autorregistro.</strong> En 122 evaluaciones y 44.747 personas, Michie y sus colegas (2009) muestran que las intervenciones que lo combinan con otra técnica de la teoría del control alcanzan un efecto de 0,42, frente a 0,26 en las demás.</li>
<li><strong>Cuida el contexto.</strong> La síntesis de 55 revisiones de Collado-Mateo (2021) cita, entre otros factores, la supervisión, la retroalimentación, el seguimiento del progreso, los objetivos, el apoyo social y el disfrute. Trata de pacientes con enfermedades crónicas y de personas mayores, no de todos los clientes que ve un entrenador.</li>
</ul>
<p>En la práctica: el cliente registra, tú respondes y revisas el objetivo con él. Un <a href="/coachs/bilan-mensuel-client-coaching.html">informe mensual de progreso de una página</a> basta para marcar ese ritmo.</p>

<h2>¿Cuándo intervenir antes de que un cliente se vaya?</h2>
<p>No esperes a que el cliente anuncie que se va. Cuatro momentos piden actuar:</p>
<ul>
<li><strong>Las primeras semanas.</strong> En el gimnasio de Río, el abandono llegaba pronto, y <a href="/articles/combien-de-temps-pour-prendre-une-habitude.html">crear un hábito lleva tiempo</a>. Prevé una revisión rápida hacia la tercera semana: qué funciona y qué no.</li>
<li><strong>El final de un bono.</strong> Habla de lo que viene después dos o tres sesiones antes de la última, con el informe en la mano. <a href="/coachs/packs-abonnement-seance-coach-sportif.html">La fórmula que ofreces</a> también influye en ese momento.</li>
<li><strong>Objetivo cumplido.</strong> Fija el siguiente con el cliente, o prepara una salida limpia con lo que necesita para seguir solo.</li>
<li><strong>Ausencias repetidas.</strong> Aplica <a href="/coachs/seance-annulee-regles-coach.html">tu política de cancelación</a> y después pregúntale qué ha cambiado en su semana.</li>
</ul>
<p>No cuentes con el contrato para retener a nadie. La ley de consumidores prohíbe imponer duraciones excesivas y considera abusiva la renovación automática si no deja al cliente una posibilidad real de decir que no quiere renovar; tu contrato debe explicar cómo darse de baja y, si pactas una permanencia, la penalización por irse antes debe ser proporcional a los días que falten. Para enviar publicidad por email u otro medio electrónico a un particular necesitas su autorización previa y expresa, salvo que exista una relación contractual previa: entonces puedes escribirle sobre servicios tuyos parecidos a los que contrató, siempre que le hayas dado la opción de negarse al recoger sus datos y se la des, de forma sencilla y gratuita, en cada mensaje. Antes de escribir a un antiguo cliente, comprueba que cumples esas condiciones.</p>

<h2>Puntos clave</h2>
<ul>
<li>Ninguna tasa general de abandono describe tu negocio: calcula tu retención con tus propios clientes y anota cada motivo de baja.</li>
<li>Objetivo por escrito, progreso registrado, seguimiento regular: son las palancas con más respaldo, aunque los estudios no traten a entrenadores independientes.</li>
<li>Actúa antes de la baja: primeras semanas, final de un bono, objetivo cumplido, ausencias repetidas.</li>
</ul>
""",
        "faq": [
            {"q": "¿Cómo fidelizar a los clientes como entrenador personal?", "a": "Fija un objetivo por escrito, registra el progreso, haz revisiones periódicas y habla de lo que viene después antes de que termine el bono. Pregunta también a cada cliente que se va qué le habría hecho quedarse: tus propios motivos de baja te enseñarán más que una estadística general."},
            {"q": "¿Cuál es la tasa de abandono en el gimnasio?", "a": "No he encontrado ninguna cifra global fiable. En un gimnasio de Río de Janeiro estudiado con 5.240 socios, el 63 % lo había dejado antes del tercer mes. Ese resultado viene de un solo gimnasio sin supervisión y no vale para todos los gimnasios ni para un cliente que entrena con un entrenador personal."},
            {"q": "¿Cómo se calcula la tasa de retención de clientes?", "a": "Toma tus clientes activos al inicio de un trimestre y cuenta cuántos siguen al final, sin sumar los nuevos. Por ejemplo, 12 clientes el 1 de enero y 9 todavía activos el 31 de marzo dan 9 ÷ 12 = 75 % en tres meses. Con pocos clientes, lee la tasa sobre el año."},
        ],
        "sources": [
            {"t": "Sperandei S, Vieira MC, Reis AC. Adherence to physical activity in an unsupervised setting: Explanatory variables for high attrition rates among fitness center members. <em>J Sci Med Sport</em>. 2016.", "u": "https://doi.org/10.1016/j.jsams.2015.12.522"},
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Michie S, Abraham C, Whittington C, McAteer J, Gupta S. Effective techniques in healthy eating and physical activity interventions: a meta-regression. <em>Health Psychol</em>. 2009.", "u": "https://doi.org/10.1037/a0016136"},
            {"t": "Collado-Mateo D, Lavín-Pérez AM, Peñacoba C, et al. Key Factors Associated with Adherence to Physical Exercise in Patients with Chronic Diseases and Older Adults: An Umbrella Review. <em>Int J Environ Res Public Health</em>. 2021.", "u": "https://doi.org/10.3390/ijerph18042023"},
            {"t": "Real Decreto Legislativo 1/2007, texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, artículos 62, 85 y 87. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555"},
            {"t": "Ley 34/2002, de 11 de julio, de servicios de la sociedad de la información y de comercio electrónico, artículos 21 y 22. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758"},
        ],
    },
    {
        "fr": "bilan-mensuel-client-coaching",
        "slug": "informe-mensual-progreso-cliente",
        "title": "Informe mensual de progreso del cliente: qué enseñarle",
        "description": "Informe mensual de progreso para entrenadores personales: qué medidas enseñar al cliente, cómo compararlas, cómo hacer la revisión y cómo tratar sus datos.",
        "body": """
<p>La respuesta corta: un <strong>informe mensual de progreso</strong> cabe en una página y responde a cuatro preguntas: cómo va el objetivo, qué se ha hecho, qué ha cambiado y qué cambias el mes que viene. Enseña de tres a cinco medidas, siempre comparadas con el propio cliente, y termina con una decisión por escrito. El ritmo mensual es una elección práctica que los estudios citados aquí no fijan.</p>

<h2>¿Por qué hacer una revisión del progreso cada mes?</h2>
<p>De una sesión a otra, al cliente le cuesta ver su progreso. El informe lo hace visible. El metaanálisis de Harkin y sus colegas (2016, 138 ensayos, 19.951 personas) muestra que seguir el progreso ayuda a alcanzar los objetivos, con un efecto mayor cuando el resultado se registra o se comparte. No se limita al ejercicio, pero un informe cumple las dos condiciones: queda por escrito y el cliente lo comparte contigo.</p>
<p>También te ayuda a tomar una decisión en lugar de repetir el mismo plan, y te da un apoyo para <a href="/coachs/fideliser-clients-coaching-sportif.html">fidelizar a un cliente a largo plazo</a>. Un mes ya te da material sobre asistencia y cargas. Un test de campo puede esperar dos o tres meses.</p>

<h2>¿Qué debe incluir un informe mensual de progreso?</h2>
<p>Elige según el objetivo del cliente. Esta tabla cubre la mayoría de los casos:</p>
<div class="tablewrap"><table>
<caption>Fuente: tabla de trabajo de esta guía, para adaptar a cada cliente.</caption>
<thead><tr><th>Medida</th><th>Qué enseñas</th><th>Precaución</th></tr></thead>
<tbody>
<tr><td>Asistencia</td><td>Sesiones hechas sobre sesiones previstas</td><td>Separa las ausencias inevitables de las demás</td></tr>
<tr><td>Carga</td><td>Esfuerzo percibido multiplicado por la duración, semana a semana</td><td>Compara con el propio cliente, nunca con otra persona</td></tr>
<tr><td>Rendimiento</td><td>Dos o tres ejercicios de referencia: carga, repeticiones, tiempo</td><td>Mantén el mismo ejercicio y las mismas instrucciones</td></tr>
<tr><td>Test de campo</td><td>Un solo test, si sirve al objetivo</td><td>Mismas condiciones cada vez</td></tr>
<tr><td>Sensaciones</td><td>Energía, sueño, disfrute, puntuados del 1 al 5</td><td>Guían la conversación y no diagnostican nada</td></tr>
<tr><td>Peso, perímetros</td><td>Solo si es su objetivo y está de acuerdo</td><td>Nunca la única medida del éxito</td></tr>
</tbody>
</table></div>
<p>Para la carga, el método más sencillo sigue siendo el RPE de la sesión: una puntuación del esfuerzo multiplicada por la duración. Foster y sus colegas lo evaluaron en 2001 frente a un método basado en la frecuencia cardiaca y lo encontraron válido para esfuerzos variados. La elección de los tests está en nuestra guía sobre <a href="/coachs/tests-physiques-nouveau-client.html">tests físicos para un cliente nuevo</a>.</p>

<h2>¿Cómo comparar los resultados con rigor?</h2>
<p>La única comparación útil enfrenta al cliente consigo mismo, en igualdad de condiciones: mismo ejercicio, mismas instrucciones, misma hora del día, mismo calentamiento. Ese rigor importa. Para la marcha de 6 minutos, la norma europea y estadounidense de 2014 señala que los resultados son sensibles a pequeñas diferencias de método y recomienda dos intentos. Este test se validó en la enfermedad respiratoria crónica: con un cliente sano, solo sirve para compararlo consigo mismo.</p>
<p>Desconfía también de los tests que prometen demasiado. En el estudio de Sartor y sus colegas (2016, 81 adultos sanos), el índice de Ruffier-Dickson solo explica el 15 % de la variabilidad de la condición cardiorrespiratoria. Úsalo como un simple indicador y no calcules un VO2 máx a partir de él. Lee cualquier diferencia a lo largo de varios meses: una sola bajada puede venir de una semana cargada, un viaje o un resfriado.</p>

<h2>¿Cómo hacer la revisión mensual con el cliente?</h2>
<p>Bastan de quince a veinte minutos, durante una sesión o por videollamada. Un desarrollo posible:</p>
<ol>
<li>Empieza preguntando cómo ha vivido el mes, antes de enseñar una sola cifra.</li>
<li>Enseña lo que ha mejorado, con la cifra de partida al lado.</li>
<li>Presenta lo que se ha estancado como hechos: «6 sesiones de 8», sin comentarios sobre la fuerza de voluntad.</li>
<li>Busca la causa con el cliente: horarios, sueño, un plan demasiado ambicioso, un objetivo desfasado.</li>
<li>Decide de uno a tres cambios y escribe el objetivo del mes siguiente.</li>
</ol>
<p>Trata igual un mes malo. Si el cliente no puede mantener tres sesiones por semana, adapta el plan a su semana real. No prometas ningún resultado para el mes siguiente. Si menciona un síntoma nuevo, una enfermedad o un trastorno de la conducta alimentaria, no interpretas: lo derivas a un médico o a un dietista-nutricionista.</p>

<h2>¿Qué hacer con los datos del informe?</h2>
<p>Un informe suele contener datos sensibles. En España, además del RGPD, se aplica la Ley Orgánica 3/2018 de Protección de Datos (LOPDGDD), y la autoridad de control es la Agencia Española de Protección de Datos (AEPD). Los datos de salud de tus clientes son datos especialmente protegidos, y un menor solo puede dar su consentimiento por sí mismo a partir de los 14 años. Los antecedentes médicos, las enfermedades y los tratamientos son datos de salud por naturaleza, y el peso también puede llegar a serlo, sobre todo combinado con los pasos o las calorías. Pide un consentimiento explícito, separado de tus condiciones generales, y guarda estos documentos en un espacio protegido.</p>
<p>El informe queda entre tu cliente y tú. Compártelo con un médico, un fisioterapeuta, otro entrenador o un familiar solo con su acuerdo. Lo más sencillo: dáselo y que lo comparta él si quiere. Para publicar una foto de antes y después en la que se le reconozca, necesitas su consentimiento expreso para ese uso, y puede retirarlo cuando quiera: aceptar que le hagas fotos no basta. La ley no exige que sea por escrito, pero pídelo así, indicando el soporte, el fin y la duración, porque te sirve de prueba. Si es menor y no tiene madurez suficiente, lo da por escrito su representante legal, que debe comunicarlo antes al Ministerio Fiscal.</p>

<h2>Puntos clave</h2>
<ul>
<li>Una página, de tres a cinco medidas y una decisión por escrito: el informe existe para cambiar algo el mes siguiente.</li>
<li>Compara al cliente consigo mismo, en igualdad de condiciones, y lee las diferencias a lo largo de varios meses.</li>
<li>Los datos del informe son del cliente: consentimiento explícito, espacio protegido y nada de compartirlos sin su acuerdo.</li>
</ul>
""",
        "faq": [
            {"q": "¿Qué debe incluir un informe mensual de progreso de un cliente?", "a": "El objetivo de partida, la asistencia, dos o tres medidas de rendimiento, cómo se siente el cliente y los cambios decididos para el mes siguiente. Basta una página. Compara cada cifra con el propio cliente, nunca con una media ni con otro cliente."},
            {"q": "¿Hay que pesar al cliente en cada revisión?", "a": "Solo si el peso corresponde a su objetivo y está de acuerdo. Esa cifra nunca debería ser la única medida del éxito, y puede contar como dato de salud. Si el cliente menciona un trastorno de la conducta alimentaria o una enfermedad, derívalo a un médico o a un dietista-nutricionista."},
            {"q": "¿Puede un entrenador personal enviar el informe de un cliente a su médico o a su fisioterapeuta?", "a": "Solo con el acuerdo del cliente. Lo más sencillo es darle el informe para que lo transmita él mismo. Sin ese acuerdo, no se lo envíes a nadie, ni siquiera a un profesional sanitario."},
        ],
        "sources": [
            {"t": "Harkin B, Webb TL, Chang BP, et al. Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. <em>Psychol Bull</em>. 2016.", "u": "https://doi.org/10.1037/bul0000025"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Holland AE, Spruit MA, Troosters T, et al. An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease. <em>Eur Respir J</em>. 2014.", "u": "https://doi.org/10.1183/09031936.00150314"},
            {"t": "Sartor F, Bonato M, Papini G, et al. A 45-Second Self-Test for Cardiorespiratory Fitness: Heart Rate-Based Estimation in Healthy Individuals. <em>PLoS One</em>. 2016.", "u": "https://doi.org/10.1371/journal.pone.0168154"},
            {"t": "Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo (Reglamento general de protección de datos), artículos 4 y 9 y considerando 35. 2016.", "u": "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679"},
            {"t": "Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"},
            {"t": "Ley Orgánica 1/1982, de 5 de mayo, de protección civil del derecho al honor, a la intimidad personal y familiar y a la propia imagen, artículos 2, 3 y 7. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196"},
        ],
    },
    {
        "fr": "lire-etat-de-forme-client",
        "slug": "estado-forma-cliente-antes-sesion",
        "title": "Sueño, fatiga y carga: cómo valorar el estado de forma de un cliente",
        "seo_title": "Estado de forma del cliente: cómo leerlo antes de la sesión",
        "description": "Cómo valorar el estado de forma de un cliente: qué preguntar antes de la sesión, qué cambia una mala noche, cómo medir la carga y qué valen el reloj y la VFC.",
        "body": """
<p>La respuesta corta: para valorar el <strong>estado de forma de un cliente</strong>, hazle tres preguntas antes del calentamiento, compara las respuestas con lo que es normal en él y ajusta la sesión cuando varias señales apuntan en la misma dirección. Ningún indicador basta por sí solo: ni el sueño, ni la variabilidad de la frecuencia cardiaca (VFC), ni la puntuación de un reloj inteligente. Estas medidas te ayudan a dosificar un esfuerzo. No hacen ningún diagnóstico.</p>

<h2>¿Qué preguntar a un cliente antes de la sesión?</h2>
<p>Bastan dos minutos. Mantén las mismas preguntas y la misma escala del 1 al 5:</p>
<ul>
<li>¿Cómo has dormido en comparación con lo habitual?</li>
<li>¿Cuánta energía tienes hoy, contando el estrés?</li>
<li>¿Tienes algún dolor o alguna molestia nueva?</li>
</ul>
<p>La revisión de Saw y sus colegas (2016, 56 estudios) muestra que las medidas subjetivas y las objetivas coinciden poco, y que las subjetivas reflejan mejor la carga de entrenamiento. Trata de deportistas, así que aplícala con cautela. Anota cada respuesta, porque solo la diferencia con su normalidad te dice algo. Un 2 de un cliente que siempre responde 4 cuenta más que un 2 de uno que suele responder 2.</p>

<h2>¿Hay que cambiar la sesión si el cliente ha dormido mal?</h2>
<p>No necesariamente. El metaanálisis de Craven y sus colegas (2022, 69 publicaciones, 959 participantes, el 89 % hombres) encuentra un rendimiento un 7,56 % menor de media tras 6 horas de sueño o menos, con una heterogeneidad muy alta entre estudios. Dos matices ayudan en la práctica:</p>
<ul>
<li><strong>El tipo de noche.</strong> Los efectos solo fueron constantes tras una noche en blanco o un madrugón, no tras acostarse tarde. La bajada llegó entonces a alrededor de un 0,4 % por hora despierto antes del ejercicio.</li>
<li><strong>La hora de la sesión.</strong> Los esfuerzos de tarde y de noche se vieron afectados; los de la mañana, muy poco.</li>
</ul>
<p>Un cliente que se levantó a las 5 de la mañana y viene a las 7 de la tarde no está en la misma situación que uno que se acostó tarde y viene a las 8 de la mañana. Aun así, estas medias no predicen su sesión: mira cómo responde al calentamiento antes de cambiar nada.</p>

<h2>¿Cómo medir la carga de entrenamiento sin material?</h2>
<p>Pide al cliente que puntúe su esfuerzo de 0 a 10 al terminar la sesión y multiplica esa nota por la duración: es el RPE de la sesión. Ejemplo de cálculo: 60 minutos puntuados con un 7 dan 420 unidades. Foster y sus colegas lo evaluaron en 2001 frente a un método basado en la frecuencia cardiaca y lo encontraron válido para esfuerzos variados. Suma las sesiones, incluido el ejercicio que hace sin ti, y compara las semanas entre sí.</p>
<p>Esta puntuación describe lo que el cliente sintió. Tus cargas, series y distancias describen lo que hizo. Para el mismo trabajo, un esfuerzo percibido que sube durante varias sesiones merece una pregunta. Deja de lado, eso sí, la ratio de carga aguda:crónica para prevenir lesiones: Impellizzeri y sus colegas concluyeron en 2020 que no hay pruebas que respalden ese uso.</p>

<h2>¿Son fiables los relojes inteligentes y la VFC?</h2>
<p>Léelos como tendencias, con límites conocidos.</p>
<ul>
<li><strong>Sueño.</strong> En el estudio de Chinoy y sus colegas (2021), siete dispositivos de consumo de la época, llevados puestos o colocados cerca de la cama y comparados con la polisomnografía en 34 adultos jóvenes sanos, detectaron bien el sueño (sensibilidad de al menos 0,93) y peor la vigilia (especificidad de 0,18 a 0,54). Las fases del sueño fueron irregulares, y las noches alteradas se midieron peor. Ignora la cifra de «sueño profundo» de una sola noche.</li>
<li><strong>Variabilidad de la frecuencia cardiaca.</strong> Según el metaanálisis de Bellenger y sus colegas (2016, 27 estudios), sube en reposo cuando la adaptación es positiva y cambia poco con la sobrecarga funcional (overreaching). Un valor bajo no demuestra un sobreentrenamiento, y un valor normal no lo descarta. Estos estudios tratan de deportistas de resistencia, lejos del cliente medio.</li>
<li><strong>Medición.</strong> La <a href="/methode/variabilite-cardiaque.html">variabilidad de la frecuencia cardiaca</a> depende del sensor, de cómo se lleva el reloj, de los latidos irregulares o de un medicamento que ralentiza el corazón. No puedes compararla de un dispositivo a otro.</li>
<li><strong>Punto de referencia.</strong> Solo la <a href="/methode/ligne-de-base.html">línea base</a> del propio cliente, construida durante varias semanas, tiene sentido. Muestra si se aleja de sus hábitos, sin decir si esos hábitos son buenos, y una deriva lenta puede pasarle desapercibida.</li>
<li><strong>Puntuaciones de recuperación.</strong> Resumen estas señales, con sus límites incluidos. Una puntuación baja no prohíbe nada, y una alta no autoriza nada.</li>
</ul>
<p>Estos datos son del cliente. Te los enseña si quiere, con su consentimiento explícito, y no se los pasas a nadie sin él. Nunca hagas depender la sesión de que los comparta. En España, los datos de salud de tus clientes son datos especialmente protegidos: además del RGPD se aplica la Ley Orgánica 3/2018 (LOPDGDD), y la autoridad de control es la Agencia Española de Protección de Datos (AEPD).</p>

<h2>¿Cuándo ajustar la sesión y cuándo derivar al médico?</h2>
<p>Busca la convergencia: vigilas cada señal por separado y actúas cuando coinciden varias.</p>
<div class="tablewrap"><table>
<caption>Fuente: referencias prudentes de esta guía, sin valor diagnóstico.</caption>
<thead><tr><th>Lo que observas</th><th>Decisión posible</th></tr></thead>
<tbody>
<tr><td>Noche corta, energía correcta, buen calentamiento</td><td>Sesión prevista</td></tr>
<tr><td>Noche corta y poca energía, sesión de tarde o de noche</td><td>Menos volumen, ninguna carga máxima</td></tr>
<tr><td>Esfuerzo percibido que sube durante varias sesiones</td><td>Semana más ligera, busca la causa con el cliente</td></tr>
<tr><td>Dolor que cambia el movimiento</td><td>Quita el ejercicio, consulta médica si persiste</td></tr>
<tr><td>Fatiga inusual que dura pese a una carga más ligera</td><td>Deriva al médico</td></tr>
<tr><td>Mareo, dolor en el pecho, falta de aire anormal, palpitaciones</td><td>Para de inmediato, que lo vea un médico y, en caso de urgencia, llama al 112, gratuito desde fijos y móviles en toda España</td></tr>
</tbody>
</table></div>
<p>No tienes que poner nombre a lo que pasa. «Sobreentrenamiento» y «carencia» son conclusiones médicas. Describe lo que observas, sugiere una consulta y lleva las tendencias a tu <a href="/coachs/bilan-mensuel-client-coaching.html">informe mensual de progreso</a>.</p>

<h2>Puntos clave</h2>
<ul>
<li>Tres preguntas puntuadas en cada sesión ya te dan lo esencial: la diferencia con lo que es normal en el cliente.</li>
<li>Sueño, carga, reloj y variabilidad de la frecuencia cardiaca se leen juntos y como tendencias. Ninguno basta solo.</li>
<li>Ajustas la sesión y no diagnosticas: un síntoma nuevo o una fatiga que dura son cosa del médico.</li>
</ul>
""",
        "faq": [
            {"q": "¿Cómo saber si un cliente está demasiado cansado para entrenar?", "a": "Pregúntale cómo ha dormido, cuánta energía tiene y si tiene algún dolor nuevo, y luego mira cómo responde al calentamiento. Si bajan varias señales, aligera la sesión. Si la fatiga dura o va acompañada de síntomas, derívalo a un médico."},
            {"q": "¿Hay que cancelar una sesión después de dormir mal?", "a": "No necesariamente. Una noche corta baja el rendimiento de media, sobre todo por la tarde o por la noche y tras un madrugón, pero la respuesta varía de una persona a otra. Mantén la sesión si el cliente responde bien al calentamiento y, si no, reduce el volumen o la intensidad."},
            {"q": "¿Una VFC baja significa sobreentrenamiento?", "a": "No. Los resultados son contradictorios y, según un metaanálisis de 2016 en deportistas de resistencia, la VFC en reposo cambia poco con la sobrecarga funcional. Una sola bajada puede venir de una mala noche o de una medición menos limpia: lee la tendencia, junto con cómo se siente el cliente."},
        ],
        "sources": [
            {"t": "Saw AE, Main LC, Gastin PB. Monitoring the athlete training response: subjective self-reported measures trump commonly used objective measures: a systematic review. <em>Br J Sports Med</em>. 2016.", "u": "https://doi.org/10.1136/bjsports-2015-094758"},
            {"t": "Craven J, McCartney D, Desbrow B, et al. Effects of Acute Sleep Loss on Physical Performance: A Systematic and Meta-Analytical Review. <em>Sports Med</em>. 2022.", "u": "https://doi.org/10.1007/s40279-022-01706-y"},
            {"t": "Foster C, Florhaug JA, Franklin J, et al. A new approach to monitoring exercise training. <em>J Strength Cond Res</em>. 2001.", "u": "https://pubmed.ncbi.nlm.nih.gov/11708692/"},
            {"t": "Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. <em>Int J Sports Physiol Perform</em>. 2020.", "u": "https://doi.org/10.1123/ijspp.2019-0864"},
            {"t": "Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. <em>Sleep</em>. 2021.", "u": "https://doi.org/10.1093/sleep/zsaa291"},
            {"t": "Bellenger CR, Fuller JT, Thomson RL, et al. Monitoring Athletic Training Status Through Autonomic Heart Rate Regulation: A Systematic Review and Meta-Analysis. <em>Sports Med</em>. 2016.", "u": "https://doi.org/10.1007/s40279-016-0484-2"},
            {"t": "Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. BOE, texto consolidado.", "u": "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"},
            {"t": "administracion.gob.es. Servicios prestados a través de números de urgencia nacionales (112). 2026.", "u": "https://administracion.gob.es/tu-espacio-europeo/derechos-obligaciones/ciudadanos/asistencia-sanitaria/numeros-urgencia"},
        ],
    },
]
