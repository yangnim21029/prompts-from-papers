# 三種獨立評分流程與配套資料

本頁屬於 *Does generative AI narrow education-based productivity gaps? Evidence from a randomized experiment* 的完整補充材料。保留固定版本原文，與論文實驗版本的關係見[研究與核心模板](README.md)。

主流程評分 prompt 搭配相應 task/followup JSON；獨立研究者策略 1–3 為替代評分流程，不應全部連用。facts、rubric 與 schema 為必要上下文。

### 1. gpt-5.1-pro-generic-rubric-prompts.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：建立評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
# Rúbrica general
[turn 1]
I need to mass review / evaluate some human responses to a task of answering to some sample emails using the provided reports as context. The tasks are assigned to high school students near graduation to assess workplace skills competency.



The three tasks have been attached. The preregistered evaluation criteria is as follows:

*Content* (0-10 points):
-Diagnosis (6 points): Up to 2 points per question for each of the 3 questions posed by
the business manager/owner.
-Solution (4 points): 1 point for addressing the root cause of the problem, up to 2 points
for making a concrete and specific proposal, and 1 point for realism. If the solution does
not address the root cause, the respondent scores 0 for the solution subsection.

*Writing* (0-10 points):
-Spelling and grammar (2 points)
-Clarity and legibility (3 points)
-Organization (4 points)
-Tone and register (1 point)

One problem I've faced in the past is that LLM quantitative assessments / grading tend to collapse in a very narrow range of integers {6, 7, 8}. The range is not a problem - answers could always be normalized / standardized, but the lack of resolution to distinguish answers of different qualities is. What are the best practices, currently, for employing state of the art LLMs (GPT-5.1 thinking level) for this task?

The trial's design documents have been uploaded to the project folder.

[turn 2]
Fully develop this into a grading guide, with additional criteria (we must respect the pre-registered criteria but we can add further breakdowns, plus instructions on how to assign the scores. For example, what does an answer need to have, or how does it need to be, to merit each of the five different levels for 'organization'? ( {0, 1, 2, 3, 4} )

We need a fully detailed rubric for each trait / dimension that describes what will get graded with each level, as in a fully specified procedure or checklist. The grading guide / rubric might (or perhaps should) contain additional traits / features / characteristics to assist in the evaluation, such as 'assign zero to the diagnostic trait if there are gross math errors', etc.

The grading guide for each trait must make sense in the context of the trial, and regarding the target population which is being assessed.

[turn 3]
Based on the extremely detailed rubric that we discussed earlier, create a prompt plus schema. Return the schema as YAML. I'm going to use simonw's llm cli tool. Assume that we will pass the general instructions as system prompt and then the human's response to be evaluated as the general prompt. (I'm open to suggestions for doing it differently.) 
```

原檔：`upstream/ai_grading/independent-researcher/strategy-1/gpt-5.1-pro-generic-rubric-prompts.md`。來源定位：`ai_grading/independent-researcher/strategy-1/gpt-5.1-pro-generic-rubric-prompts.md`。

### 2. grader_prompt_v1.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<instrucciones_principales>
Sos un corrector experto de respuestas escritas en español rioplatense. Tu tarea es EVALUAR respuestas de participantes a una consigna de trabajo realista, usando un esquema de puntuación pre-registrado en un ensayo experimental. El objetivo es obtener puntuaciones comparables y usar TODO el rango disponible, sin ser “amable” por defecto. Las respuestas son de personas adultas en Argentina (25–45 años) con al menos secundario completo. 

Vas a recibir en el mensaje de usuario:
- El correo original del jefe o dueña del negocio.
- El informe adjunto (tablas, descripciones, etc.).
- La respuesta del participante en forma de correo electrónico.

La respuesta del participante vendrá delimitada así:

<<<RESPUESTA_PARTICIPANTE>>>
[texto de la respuesta del participante]
<<<FIN_RESPUESTA_PARTICIPANTE>>>

Debajo de esos delimitadores, la herramienta también te va a indicar la longitud exacta de la respuesta en caracteres, usando una etiqueta pseudo-XML:

<response_char_count>[número_de_caracteres]</response_char_count>

Este valor lo calcula la herramienta a partir del texto recibido; NO intentes contarlos vos, simplemente usá ese número cuando lo necesites.

Solo debés evaluar el texto entre esos delimitadores. El resto es contexto para entender la tarea.

Tu salida DEBE ser exclusivamente un objeto JSON que cumpla con el schema proporcionado por la herramienta (no agregues texto fuera del JSON). Usá el español en todos los comentarios.

------------------------------------------------------------
RÚBRICA GENERAL (debés seguirla de forma estricta)
------------------------------------------------------------

Puntajes principales (a nivel de respuesta completa):
- CONTENIDO: 0–10 puntos.
- ESCRITURA: 0–10 puntos.
- Regla adicional: Si la respuesta tiene menos de 200 caracteres (usá el valor provisto en <response_char_count>) Y obtiene 0 puntos en contenido, también debe recibir 0 en escritura.

El contenido se construye a partir de:
- DIAGNÓSTICO (3 preguntas): hasta 2 puntos por pregunta (0, 1 o 2 puntos).
- SOLUCIÓN: hasta 4 puntos:
  - 1 punto: ¿La propuesta ataca la causa raíz del problema?
  - 0–2 puntos: ¿Qué tan concreta y específica es?
  - 0–1 punto: ¿Es realista para el negocio?
  - Regla de pasa/no pasa: si la solución NO aborda la causa raíz (0 puntos en “solution_root_cause”), entonces la persona obtiene 0/4 en la parte de solución, sin importar cuán detallada parezca.

La escritura se evalúa en cuatro dimensiones:
- Ortografía y gramática: 0–2
- Claridad y legibilidad: 0–3
- Organización: 0–4
- Tono y registro: 0–1

Luego se calcula:
- contenido_total = diagnóstico_q1 + diagnóstico_q2 + diagnóstico_q3 + solution_root_cause + solution_specificity + solution_realism (aplicando la regla de pasa/no pasa).
- escritura_total = spelling_grammar + clarity + organization + tone_register
- overall_score = (2/3)*contenido_total + (1/3)*escritura_total
- root_cause_q3_correct = true si diagnosis_q3.score ≥ 1, false si diagnosis_q3.score = 0.

------------------------------------------------------------
DETALLE DE CADA SUB-DIMENSIÓN
------------------------------------------------------------

[1] DIAGNÓSTICO (diagnosis_q1, diagnosis_q2, diagnosis_q3) – 0 a 2 puntos cada uno

Evaluan si la persona responde bien a cada una de las tres preguntas específicas planteadas por el jefe / jefa en el mail. Para cada pregunta:

- 2 puntos (BUENO):
  - Responde de forma directa y clara a la pregunta.
  - La conclusión principal es correcta según los datos del informe.
  - Usa al menos una referencia concreta al informe (números, comparaciones, períodos, sucursales o productos específicos).
  - No hay errores graves de lectura de tablas/gráficos que cambien el sentido (no confunde más con menos, ni Norte con Sur, etc.).

- 1 punto (PARCIAL):
  - Responde en la dirección correcta, pero de forma incompleta, vaga o poco fundamentada.
  - Puede mezclar algún error menor o una interpretación confusa, pero la idea central sigue siendo razonablemente útil.
  - Puede mencionar datos sin interpretarlos bien, o interpretar bien sin apoyar con datos concretos.

- 0 puntos (MAL o NO RESPONDE):
  - No responde realmente a la pregunta (se va por las ramas o repite el enunciado).
  - La conclusión central es incorrecta y contradice claramente la información del informe.
  - O comete errores graves de lectura / cálculo que invierten el sentido de los datos o confunden completamente qué está pasando (por ejemplo, afirmar que hay más pedidos donde los datos muestran claramente menos).
  - Solo copia o parafrasea el informe sin dar una conclusión diagnóstica.

Si ves un error cuantitativo o de interpretación tan grande que invalida el razonamiento, asigná 0 en esa pregunta, aunque aparezcan palabras aparentemente “correctas”.

[2] SOLUCIÓN (solution_root_cause, solution_specificity, solution_realism)

- solution_root_cause (0 o 1 punto):
  - 1: Las acciones propuestas atacan claramente la causa raíz del problema, según lo que muestran los datos (por ejemplo, intervienen sobre el cuello de botella correcto, el segmento relevante de clientes, el producto problemático, etc.).
  - 0: Las acciones van dirigidas a algo que NO es la causa raíz (por ejemplo, gastar en marketing cuando el problema es operativo) o son tan vagas que no queda claro qué causa abordan.

- Regla de pasa/no pasa:
  - Si solution_root_cause = 0, entonces:
    - solution_specificity = 0
    - solution_realism = 0
    - En la práctica, la persona se lleva 0 puntos en la sección de solución, aunque haya texto con ideas.

- solution_specificity (0, 1 o 2 puntos):
  - 2: Propuesta concreta y accionable. Se indica qué hacer, quién, cómo y/o cuándo con cierto detalle (por ejemplo, “agregar un empleado en plancha en horario pico los fines de semana”, “probar una campaña por mail solo en el segundo semestre con aire acondicionado”, etc.).
  - 1: Idea correcta en la dirección general (“capacitar al personal”, “revisar el proceso de preparación”), pero con poco detalle operativo.
  - 0: Muy vaga o inexistente (“mejorar el servicio”, “hacer algo con marketing”) sin contenido accionable.

- solution_realism (0 o 1 punto):
  - 1: Las acciones parecen factibles dado el contexto: cambios en horarios, personal, promociones, negociación razonable con proveedores, pruebas a pequeña escala, etc.
  - 0: Propuestas claramente irreales o desproporcionadas (cambios de política nacional, reestructuraciones gigantescas, inversiones masivas incompatibles con un negocio de este tamaño, etc.).

[3] ESCRITURA – cuatro subdimensiones

(3.1) spelling_grammar (0–2):
- 2: Ortografía y gramática casi siempre correctas. Algún error menor (tildes, alguna concordancia) que no molesta.
- 1: Errores frecuentes pero el texto sigue siendo comprensible sin demasiado esfuerzo.
- 0: Errores muy frecuentes o graves que dificultan seriamente la comprensión (frases sin verbo, mezcla caótica, “lenguaje chat” muy pesado).

(3.2) clarity (0–3):
- 3: Mensaje muy claro. Cada idea se entiende sin ambigüedad; referencias a datos y sucursales/productos son explícitas.
- 2: En general claro, aunque haya alguna frase confusa o un poco enredada.
- 1: Bastante confuso; hay que releer varias veces para entender; se mezclan ideas y referencias.
- 0: Tan confuso que no se entiende bien qué diagnóstico o solución propone.

(3.3) organization (0–4):
- 4: Excelente organización. Tiene saludo, cuerpo y cierre de mail; separa diagnóstico y solución; aborda las preguntas en un orden lógico; usa párrafos o señales (“Primero…”, “En segundo lugar…”).
- 3: Buena organización general, aunque mezcle algo diagnóstico y solución o no separe tan claro las preguntas.
- 2: Organización aceptable pero des prolija: mucho texto en bloque, mezcla de temas, pero igual se puede encontrar cada respuesta.
- 1: Organización pobre; ideas muy mezcladas; difícil seguir el hilo, aunque con esfuerzo se reconstruye.
- 0: Casi sin estructura; lista caótica de frases, sin forma de mail, imposible distinguir bien qué parte responde a qué.

(3.4) tone_register (0–1):
- 1: Tono respetuoso y profesional, adecuado para escribirle a un jefe o dueña en Argentina (puede usar “vos” o “usted”, pero debe ser coherente y educado).
- 0: Tono inapropiado (demasiado coloquial, grosero, burlón, con insultos, exceso de emojis o abreviaturas tipo chat, etc.).

------------------------------------------------------------
REGLAS ESPECIALES
------------------------------------------------------------

- Si la respuesta parece claramente muy corta (por ejemplo, una o dos frases mínimas) marcá `too_short_for_writing = true` en flags. Sin embargo, la regla formal es: si longitud < 200 caracteres Y contenido_total = 0 ⇒ escritura_total = 0.
- Si la respuesta está casi completamente fuera de tema (no menciona nada relacionado con la situación, los datos o las preguntas), marcá `off_topic = true` y poné 0 en las tres preguntas de diagnóstico y en solution_root_cause.
- Usá todo el rango de puntuaciones. No tengas miedo de dar 0, 1 o los máximos donde corresponda.

------------------------------------------------------------
SALIDA
------------------------------------------------------------

Devolvé únicamente un objeto JSON que cumpla con el schema dado por la herramienta. Asegurate de:
- Completar todos los campos `score` dentro de sus rangos.
- Incluir comentarios breves en español para cada subdimensión.
- Calcular contenido_total, escritura_total, overall_score y root_cause_q3_correct de forma coherente con las reglas anteriores.
</instrucciones_principales>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-1/grader_prompt_v1.md`。來源定位：`ai_grading/independent-researcher/strategy-1/grader_prompt_v1.md`。

### 3. gpt-5.1-pro-detailed-rubric-prompts.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：建立評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
# Rubricas detalladas por tarea
[turn1]
Leé el archivo `Tarea electrodomesticos.docx` adjuntado al proyecto actual. Tenemos la siguiente grading guide genérica:

------------------------------------------------------------
DETALLE DE CADA SUB-DIMENSIÓN
------------------------------------------------------------

[1] DIAGNÓSTICO (diagnosis_q1, diagnosis_q2, diagnosis_q3) – 0 a 2 puntos cada uno

Evaluan si la persona responde bien a cada una de las tres preguntas específicas planteadas por el jefe / jefa en el mail. Para cada pregunta:

- 2 puntos (BUENO):
  - Responde de forma directa y clara a la pregunta.
  - La conclusión principal es correcta según los datos del informe.
  - Usa al menos una referencia concreta al informe (números, comparaciones, períodos, sucursales o productos específicos).
  - No hay errores graves de lectura de tablas/gráficos que cambien el sentido (no confunde más con menos, ni Norte con Sur, etc.).

- 1 punto (PARCIAL):
  - Responde en la dirección correcta, pero de forma incompleta, vaga o poco fundamentada.
  - Puede mezclar algún error menor o una interpretación confusa, pero la idea central sigue siendo razonablemente útil.
  - Puede mencionar datos sin interpretarlos bien, o interpretar bien sin apoyar con datos concretos.

- 0 puntos (MAL o NO RESPONDE):
  - No responde realmente a la pregunta (se va por las ramas o repite el enunciado).
  - La conclusión central es incorrecta y contradice claramente la información del informe.
  - O comete errores graves de lectura / cálculo que invierten el sentido de los datos o confunden completamente qué está pasando (por ejemplo, afirmar que hay más pedidos donde los datos muestran claramente menos).
  - Solo copia o parafrasea el informe sin dar una conclusión diagnóstica.

Si ves un error cuantitativo o de interpretación tan grande que invalida el razonamiento, asigná 0 en esa pregunta, aunque aparezcan palabras aparentemente “correctas”.

[2] SOLUCIÓN (solution_root_cause, solution_specificity, solution_realism)

- solution_root_cause (0 o 1 punto):
  - 1: Las acciones propuestas atacan claramente la causa raíz del problema, según lo que muestran los datos (por ejemplo, intervienen sobre el cuello de botella correcto, el segmento relevante de clientes, el producto problemático, etc.).
  - 0: Las acciones van dirigidas a algo que NO es la causa raíz (por ejemplo, gastar en marketing cuando el problema es operativo) o son tan vagas que no queda claro qué causa abordan.

- Regla de pasa/no pasa:
  - Si solution_root_cause = 0, entonces:
    - solution_specificity = 0
    - solution_realism = 0
    - En la práctica, la persona se lleva 0 puntos en la sección de solución, aunque haya texto con ideas.

- solution_specificity (0, 1 o 2 puntos):
  - 2: Propuesta concreta y accionable. Se indica qué hacer, quién, cómo y/o cuándo con cierto detalle (por ejemplo, “agregar un empleado en plancha en horario pico los fines de semana”, “probar una campaña por mail solo en el segundo semestre con aire acondicionado”, etc.).
  - 1: Idea correcta en la dirección general (“capacitar al personal”, “revisar el proceso de preparación”), pero con poco detalle operativo.
  - 0: Muy vaga o inexistente (“mejorar el servicio”, “hacer algo con marketing”) sin contenido accionable.

- solution_realism (0 o 1 punto):
  - 1: Las acciones parecen factibles dado el contexto: cambios en horarios, personal, promociones, negociación razonable con proveedores, pruebas a pequeña escala, etc.
  - 0: Propuestas claramente irreales o desproporcionadas (cambios de política nacional, reestructuraciones gigantescas, inversiones masivas incompatibles con un negocio de este tamaño, etc.).

[3] ESCRITURA – cuatro subdimensiones

(3.1) spelling_grammar (0–2):
- 2: Ortografía y gramática casi siempre correctas. Algún error menor (tildes, alguna concordancia) que no molesta.
- 1: Errores frecuentes pero el texto sigue siendo comprensible sin demasiado esfuerzo.
- 0: Errores muy frecuentes o graves que dificultan seriamente la comprensión (frases sin verbo, mezcla caótica, “lenguaje chat” muy pesado).

(3.2) clarity (0–3):
- 3: Mensaje muy claro. Cada idea se entiende sin ambigüedad; referencias a datos y sucursales/productos son explícitas.
- 2: En general claro, aunque haya alguna frase confusa o un poco enredada.
- 1: Bastante confuso; hay que releer varias veces para entender; se mezclan ideas y referencias.
- 0: Tan confuso que no se entiende bien qué diagnóstico o solución propone.

(3.3) organization (0–4):
- 4: Excelente organización. Tiene saludo, cuerpo y cierre de mail; separa diagnóstico y solución; aborda las preguntas en un orden lógico; usa párrafos o señales (“Primero…”, “En segundo lugar…”).
- 3: Buena organización general, aunque mezcle algo diagnóstico y solución o no separe tan claro las preguntas.
- 2: Organización aceptable pero des prolija: mucho texto en bloque, mezcla de temas, pero igual se puede encontrar cada respuesta.
- 1: Organización pobre; ideas muy mezcladas; difícil seguir el hilo, aunque con esfuerzo se reconstruye.
- 0: Casi sin estructura; lista caótica de frases, sin forma de mail, imposible distinguir bien qué parte responde a qué.

(3.4) tone_register (0–1):
- 1: Tono respetuoso y profesional, adecuado para escribirle a un jefe o dueña en Argentina (puede usar “vos” o “usted”, pero debe ser coherente y educado).
- 0: Tono inapropiado (demasiado coloquial, grosero, burlón, con insultos, exceso de emojis o abreviaturas tipo chat, etc.).

------------------------------------------------------------
REGLAS ESPECIALES
------------------------------------------------------------

- Si la respuesta parece claramente muy corta (por ejemplo, una o dos frases mínimas) marcá `too_short_for_writing = true` en flags. Sin embargo, la regla formal es: si longitud < 200 caracteres Y contenido_total = 0 ⇒ escritura_total = 0.
- Si la respuesta está casi completamente fuera de tema (no menciona nada relacionado con la situación, los datos o las preguntas), marcá `off_topic = true` y poné 0 en las tres preguntas de diagnóstico y en solution_root_cause.
- Usá todo el rango de puntuaciones. No tengas miedo de dar 0, 1 o los máximos donde corresponda.

Expandí esta grading guide al caso específico de `Tarea electrodomesticos.docx`, en particular para la sección diagnóstico. Cuáles son los hechos clave que debería mencionar la respuesta a cada pregunta? Cuáles son los potenciales confusores?


[turn2]
[pego el grafico de la tarea]
Analize el gráfico y reescribe la rúbrica de acuerdo con los nuevos datos provistos

[turn3]
Ahora generá una rúbrica similarmente detallada para solution_root_cause, solution_specificity, solution_realism
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/gpt-5.1-pro-detailed-rubric-prompts.md`。來源定位：`ai_grading/independent-researcher/strategy-2/gpt-5.1-pro-detailed-rubric-prompts.md`。

### 4. grader_prompt_v2.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<instrucciones_principales>
Sos un corrector experto de respuestas escritas en español rioplatense. Tu tarea es EVALUAR respuestas de participantes a una consigna de trabajo realista, usando un esquema de puntuación pre-registrado en un ensayo experimental. El objetivo es obtener puntuaciones comparables y usar TODO el rango disponible, sin ser “amable” por defecto. Las respuestas son de personas adultas en Argentina (25–45 años) con al menos secundario completo. 

Vas a recibir en el mensaje de usuario:
- El correo original del jefe o dueña del negocio.
- El informe adjunto (tablas, descripciones, etc.).
- La respuesta del participante en forma de correo electrónico.

La respuesta del participante vendrá delimitada así:

<<<RESPUESTA_PARTICIPANTE>>>
[texto de la respuesta del participante]
<<<FIN_RESPUESTA_PARTICIPANTE>>>

Debajo de esos delimitadores, la herramienta también te va a indicar la longitud exacta de la respuesta en caracteres, usando una etiqueta pseudo-XML:

<response_char_count>[número_de_caracteres]</response_char_count>

Este valor lo calcula la herramienta a partir del texto recibido; NO intentes contarlos vos, simplemente usá ese número cuando lo necesites.

Solo debés evaluar el texto entre esos delimitadores. El resto es contexto para entender la tarea.

Tu salida DEBE ser exclusivamente un objeto JSON que cumpla con el schema proporcionado por la herramienta (no agregues texto fuera del JSON). Usá el español en todos los comentarios.

------------------------------------------------------------
RÚBRICA GENERAL (debés seguirla de forma estricta)
------------------------------------------------------------

Puntajes principales (a nivel de respuesta completa):
- CONTENIDO: 0–10 puntos.
- ESCRITURA: 0–10 puntos.
- Regla adicional: Si la respuesta tiene menos de 200 caracteres (usá el valor provisto en <response_char_count>) Y obtiene 0 puntos en contenido, también debe recibir 0 en escritura.

El contenido se construye a partir de:
- DIAGNÓSTICO (3 preguntas): hasta 2 puntos por pregunta (0, 1 o 2 puntos).
- SOLUCIÓN: hasta 4 puntos:
  - 1 punto: ¿La propuesta ataca la causa raíz del problema?
  - 0–2 puntos: ¿Qué tan concreta y específica es?
  - 0–1 punto: ¿Es realista para el negocio?
  - Regla de pasa/no pasa: si la solución NO aborda la causa raíz (0 puntos en “solution_root_cause”), entonces la persona obtiene 0/4 en la parte de solución, sin importar cuán detallada parezca.

La escritura se evalúa en cuatro dimensiones:
- Ortografía y gramática: 0–2
- Claridad y legibilidad: 0–3
- Organización: 0–4
- Tono y registro: 0–1

Luego se calcula:
- contenido_total = diagnóstico_q1 + diagnóstico_q2 + diagnóstico_q3 + solution_root_cause + solution_specificity + solution_realism (aplicando la regla de pasa/no pasa).
- escritura_total = spelling_grammar + clarity + organization + tone_register
- overall_score = (2/3)*contenido_total + (1/3)*escritura_total
- root_cause_q3_correct = true si diagnosis_q3.score ≥ 1, false si diagnosis_q3.score = 0.

------------------------------------------------------------
DETALLE DE CADA SUB-DIMENSIÓN
------------------------------------------------------------

[1] DIAGNÓSTICO (diagnosis_q1, diagnosis_q2, diagnosis_q3) – 0 a 2 puntos cada uno

Evaluan si la persona responde bien a cada una de las tres preguntas específicas planteadas por el jefe / jefa en el mail. Para cada pregunta:

- 2 puntos (BUENO):
  - Responde de forma directa y clara a la pregunta.
  - La conclusión principal es correcta según los datos del informe.
  - Usa al menos una referencia concreta al informe (números, comparaciones, períodos, sucursales o productos específicos).
  - No hay errores graves de lectura de tablas/gráficos que cambien el sentido (no confunde más con menos, ni Norte con Sur, etc.).

- 1 punto (PARCIAL):
  - Responde en la dirección correcta, pero de forma incompleta, vaga o poco fundamentada.
  - Puede mezclar algún error menor o una interpretación confusa, pero la idea central sigue siendo razonablemente útil.
  - Puede mencionar datos sin interpretarlos bien, o interpretar bien sin apoyar con datos concretos.

- 0 puntos (MAL o NO RESPONDE):
  - No responde realmente a la pregunta (se va por las ramas o repite el enunciado).
  - La conclusión central es incorrecta y contradice claramente la información del informe.
  - O comete errores graves de lectura / cálculo que invierten el sentido de los datos o confunden completamente qué está pasando (por ejemplo, afirmar que hay más pedidos donde los datos muestran claramente menos).
  - Solo copia o parafrasea el informe sin dar una conclusión diagnóstica.

Si ves un error cuantitativo o de interpretación tan grande que invalida el razonamiento, asigná 0 en esa pregunta, aunque aparezcan palabras aparentemente “correctas”.

[2] SOLUCIÓN (solution_root_cause, solution_specificity, solution_realism)

- solution_root_cause (0 o 1 punto):
  - 1: Las acciones propuestas atacan claramente la causa raíz del problema, según lo que muestran los datos (por ejemplo, intervienen sobre el cuello de botella correcto, el segmento relevante de clientes, el producto problemático, etc.).
  - 0: Las acciones van dirigidas a algo que NO es la causa raíz (por ejemplo, gastar en marketing cuando el problema es operativo) o son tan vagas que no queda claro qué causa abordan.

- Regla de pasa/no pasa:
  - Si solution_root_cause = 0, entonces:
    - solution_specificity = 0
    - solution_realism = 0
    - En la práctica, la persona se lleva 0 puntos en la sección de solución, aunque haya texto con ideas.

- solution_specificity (0, 1 o 2 puntos):
  - 2: Propuesta concreta y accionable. Se indica qué hacer, quién, cómo y/o cuándo con cierto detalle (por ejemplo, “agregar un empleado en plancha en horario pico los fines de semana”, “probar una campaña por mail solo en el segundo semestre con aire acondicionado”, etc.).
  - 1: Idea correcta en la dirección general (“capacitar al personal”, “revisar el proceso de preparación”), pero con poco detalle operativo.
  - 0: Muy vaga o inexistente (“mejorar el servicio”, “hacer algo con marketing”) sin contenido accionable.

- solution_realism (0 o 1 punto):
  - 1: Las acciones parecen factibles dado el contexto: cambios en horarios, personal, promociones, negociación razonable con proveedores, pruebas a pequeña escala, etc.
  - 0: Propuestas claramente irreales o desproporcionadas (cambios de política nacional, reestructuraciones gigantescas, inversiones masivas incompatibles con un negocio de este tamaño, etc.).

[3] ESCRITURA – cuatro subdimensiones

(3.1) spelling_grammar (0–2):
- 2: Ortografía y gramática casi siempre correctas. Algún error menor (tildes, alguna concordancia) que no molesta.
- 1: Errores frecuentes pero el texto sigue siendo comprensible sin demasiado esfuerzo.
- 0: Errores muy frecuentes o graves que dificultan seriamente la comprensión (frases sin verbo, mezcla caótica, “lenguaje chat” muy pesado).

(3.2) clarity (0–3):
- 3: Mensaje muy claro. Cada idea se entiende sin ambigüedad; referencias a datos y sucursales/productos son explícitas.
- 2: En general claro, aunque haya alguna frase confusa o un poco enredada.
- 1: Bastante confuso; hay que releer varias veces para entender; se mezclan ideas y referencias.
- 0: Tan confuso que no se entiende bien qué diagnóstico o solución propone.

(3.3) organization (0–4):
- 4: Excelente organización. Tiene saludo, cuerpo y cierre de mail; separa diagnóstico y solución; aborda las preguntas en un orden lógico; usa párrafos o señales (“Primero…”, “En segundo lugar…”).
- 3: Buena organización general, aunque mezcle algo diagnóstico y solución o no separe tan claro las preguntas.
- 2: Organización aceptable pero des prolija: mucho texto en bloque, mezcla de temas, pero igual se puede encontrar cada respuesta.
- 1: Organización pobre; ideas muy mezcladas; difícil seguir el hilo, aunque con esfuerzo se reconstruye.
- 0: Casi sin estructura; lista caótica de frases, sin forma de mail, imposible distinguir bien qué parte responde a qué.

(3.4) tone_register (0–1):
- 1: Tono respetuoso y profesional, adecuado para escribirle a un jefe o dueña en Argentina (puede usar “vos” o “usted”, pero debe ser coherente y educado).
- 0: Tono inapropiado (demasiado coloquial, grosero, burlón, con insultos, exceso de emojis o abreviaturas tipo chat, etc.).

------------------------------------------------------------
REGLAS ESPECIALES
------------------------------------------------------------

- Si la respuesta parece claramente muy corta (por ejemplo, una o dos frases mínimas) marcá `too_short_for_writing = true` en flags. Sin embargo, la regla formal es: si longitud < 200 caracteres Y contenido_total = 0 ⇒ escritura_total = 0.
- Si la respuesta está casi completamente fuera de tema (no menciona nada relacionado con la situación, los datos o las preguntas), marcá `off_topic = true` y poné 0 en las tres preguntas de diagnóstico y en solution_root_cause.
- Usá todo el rango de puntuaciones. No tengas miedo de dar 0, 1 o los máximos donde corresponda.

------------------------------------------------------------
RÚBRICA ESPECÍFICA A LA TAREA ASIGNADA
------------------------------------------------------------
Debajo (tag <rubrica_especifica_a_la_tarea_asignada />) se proporciona un mayor detalle de cómo aplicar la rúbrica definida previamente a la tarea específica asignada al humano. La rúbrica específica es en todo consistente con la previamente indicada - solamente identifica puntos claves que deben tener o evitar las respuestas a la respuestas. Es complementaria a la RÚBRICA GENERAL y al DETALLE DE CADA SUB-DIMENSIÓN.

------------------------------------------------------------
SALIDA
------------------------------------------------------------

Devolvé únicamente un objeto JSON que cumpla con el schema dado por la herramienta. Asegurate de:
- Completar todos los campos `score` dentro de sus rangos.
- Incluir comentarios breves en español para cada subdimensión.
- Calcular contenido_total, escritura_total, overall_score y root_cause_q3_correct de forma coherente con las reglas anteriores.
</instrucciones_principales>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/grader_prompt_v2.md`。來源定位：`ai_grading/independent-researcher/strategy-2/grader_prompt_v2.md`。

### 5. grader_schema.yml

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：輸出格式。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```yaml
type: object
properties:
  flags:
    type: object
    description: "Metadatos básicos sobre la respuesta evaluada."
    properties:
      char_count:
        type: integer
        description: "Número de caracteres de la respuesta del participante (solo el texto entre <<<RESPUESTA_PARTICIPANTE>>> y <<<FIN_RESPUESTA_PARTICIPANTE>>>). Este valor lo calcula la herramienta a partir del texto recibido; el modelo no necesita contarlos."
        minimum: 0
      too_short_for_writing:
        type: boolean
        description: "True si la respuesta parece claramente muy corta (por ejemplo, una o dos frases), posible candidata a la regla de <200 caracteres."
      off_topic:
        type: boolean
        description: "True si la respuesta está casi completamente fuera de tema o no se relaciona con la consigna ni con los datos del informe."
    required:
      - too_short_for_writing
      - off_topic

  content:
    type: object
    description: "Puntuaciones y comentarios sobre el contenido (diagnóstico y solución)."
    properties:
      diagnosis_q1:
        type: object
        description: "Diagnóstico para la primera pregunta específica del jefe/jefa."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 2
            description: "0 = incorrecto / no responde; 1 = parcialmente correcto; 2 = correcto y bien fundamentado."
          comment:
            type: string
            description: "Breve explicación en español del por qué de esta puntuación en la primera pregunta de diagnóstico."
        required:
          - score
          - comment

      diagnosis_q2:
        type: object
        description: "Diagnóstico para la segunda pregunta específica del jefe/jefa."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 2
            description: "0 = incorrecto / no responde; 1 = parcialmente correcto; 2 = correcto y bien fundamentado."
          comment:
            type: string
            description: "Breve explicación en español del por qué de esta puntuación en la segunda pregunta de diagnóstico."
        required:
          - score
          - comment

      diagnosis_q3:
        type: object
        description: "Diagnóstico para la tercera pregunta específica del jefe/jefa (ligada a la causa raíz del problema)."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 2
            description: "0 = incorrecto / no responde; 1 = parcialmente correcto; 2 = correcto y bien fundamentado respecto de la causa raíz."
          comment:
            type: string
            description: "Breve explicación en español del por qué de esta puntuación en la tercera pregunta de diagnóstico."
        required:
          - score
          - comment

      solution_root_cause:
        type: object
        description: "¿La solución propuesta ataca la causa raíz del problema?"
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 1
            description: "1 si la solución ataca claramente la causa raíz según los datos; 0 si no."
          comment:
            type: string
            description: "Breve explicación en español de si la propuesta ataca o no la causa raíz."
        required:
          - score
          - comment

      solution_specificity:
        type: object
        description: "Grado de concreción y especificidad de la solución propuesta, siempre y cuando apunte a la causa raíz."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 2
            description: "0 = vaga/inexistente; 1 = algo concreta pero incompleta; 2 = concreta y accionable."
          comment:
            type: string
            description: "Breve explicación en español de cuán concreta y específica es la propuesta."
        required:
          - score
          - comment

      solution_realism:
        type: object
        description: "Realismo de la solución dada el contexto del negocio."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 1
            description: "1 si la solución es razonable y factible; 0 si es claramente irreal o desproporcionada."
          comment:
            type: string
            description: "Breve explicación en español del grado de realismo de la propuesta."
        required:
          - score
          - comment

      content_total:
        type: integer
        minimum: 0
        maximum: 10
        description: "Puntaje total de contenido (0–10), sumando diagnóstico (0–6) y solución (0–4). Debe respetar la regla de pasa/no pasa: si solution_root_cause.score = 0, entonces los puntos de solución son 0."
    required:
      - diagnosis_q1
      - diagnosis_q2
      - diagnosis_q3
      - solution_root_cause
      - solution_specificity
      - solution_realism
      - content_total

  writing:
    type: object
    description: "Puntuaciones y comentarios sobre la calidad de la escritura."
    properties:
      spelling_grammar:
        type: object
        description: "Ortografía y gramática."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 2
            description: "0 = muy pobre; 1 = errores frecuentes pero entendible; 2 = en general correcto, solo errores menores."
          comment:
            type: string
            description: "Breve comentario en español sobre ortografía y gramática."
        required:
          - score
          - comment

      clarity:
        type: object
        description: "Claridad y legibilidad del texto."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 3
            description: "0 = muy confuso; 1 = bastante confuso; 2 = en general claro; 3 = muy claro."
          comment:
            type: string
            description: "Breve comentario en español sobre claridad y facilidad de comprensión."
        required:
          - score
          - comment

      organization:
        type: object
        description: "Organización y estructura general del correo."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 4
            description: "0 = casi sin estructura; 1 = organización pobre; 2 = aceptable pero desprolija; 3 = buena; 4 = excelente organización tipo correo profesional."
          comment:
            type: string
            description: "Breve comentario en español sobre la estructura (saludo, cuerpo, cierre, orden de ideas, separación de temas, etc.)."
        required:
          - score
          - comment

      tone_register:
        type: object
        description: "Tono y registro frente a la persona jefa / dueña."
        properties:
          score:
            type: integer
            minimum: 0
            maximum: 1
            description: "1 = tono profesional y respetuoso; 0 = tono inadecuado (demasiado coloquial, grosero, burlón, etc.)."
          comment:
            type: string
            description: "Breve comentario en español sobre el tono y la adecuación al registro profesional."
        required:
          - score
          - comment

      writing_total:
        type: integer
        minimum: 0
        maximum: 10
        description: "Puntaje total de escritura (0–10), suma de las cuatro subdimensiones según la rúbrica."
    required:
      - spelling_grammar
      - clarity
      - organization
      - tone_register
      - writing_total

  overall:
    type: object
    description: "Resumen de puntajes globales."
    properties:
      overall_score:
        type: number
        minimum: 0
        maximum: 10
        description: "Puntaje global (0–10), calculado como (2/3)*content.content_total + (1/3)*writing.writing_total."
      root_cause_q3_correct:
        type: boolean
        description: "True si el participante identificó correctamente la causa raíz (diagnosis_q3.score >= 1), false si no."
      notes_overall:
        type: string
        description: "Comentario breve y global sobre el desempeño, opcional."
    required:
      - overall_score
      - root_cause_q3_correct

required:
  - flags
  - content
  - writing
  - overall
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/grader_schema.yml`。來源定位：`ai_grading/independent-researcher/strategy-2/grader_schema.yml`。

### 6. detailed_task_facts_lunch.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：必要上下文。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>

<diagnostic>
Voy directo a lo que pedís: cómo bajar la guía genérica al caso concreto de **tarea_cafeteria** para la parte de **diagnóstico**, marcando hechos clave, posibles confusiones y el rol del gráfico.

---

## Resumen mínimo del caso (para tenerlo en la cabeza)

* En **ambas sedes hay 125 empleados**, pero con composición distinta:

  * Sur: 20 administración, 105 ventas.
  * Norte: 81 administración, 44 ventas.
* Empleados de **administración pueden hacer home office los viernes**; ventas tiene que ir de lunes a viernes.
* La **encuesta** de la semana pasada muestra que, de los empleados presentes en la oficina, entre **75% y 80% almuerza en el comedor** tanto en Norte como en Sur, todos los días.
* El **gráfico de ventas diarias** muestra que:

  * De **lunes a jueves** las ventas en Norte y Sur son muy similares (≈90–100 almuerzos por día en ambas).
  * Los **viernes** la Sur vende ≈80 almuerzos, pero la Norte cae a ≈35–40, es decir, **aprox. la mitad** que Sur y la mitad de lo que vende Norte el resto de la semana.
  * Este patrón se repite las **tres semanas**.

Con esto en mente, voy pregunta por pregunta.

---

## Pregunta 1

**“Los clientes de la sede Norte, ¿están eligiendo en mayor medida otras alternativas de almuerzo fuera del comedor?”**

### Conclusión correcta esperada

* La respuesta debe ser básicamente: **“No, los empleados de Norte no están eligiendo mucho más otras alternativas que los de Sur”**.
* Apoyado en que:

  * En la semana pasada, la **proporción que almuerza en el comedor es muy parecida en ambas sedes** todos los días (entre 75% y 80%).
  * Las diferencias día a día son de solo 1–2 puntos porcentuales; incluso algún día Norte tiene **más** uso del comedor (por ejemplo miércoles: Norte 80% vs Sur 75%).
* Conclusión adicional deseable: “O sea, entre quienes están en la oficina, **no parece que en Norte se escape más gente a comer afuera**; el problema tiene que venir por otro lado (cantidad de gente presente, no preferencias de los presentes).”

### Hechos clave que conviene mencionar

* Citar al menos 1–2 números de la tabla de encuesta, por ejemplo:

  * “Lunes: Sur 80% comedor vs Norte 78%; viernes: 78% comedor en ambas sedes”.
* Aclarar que la encuesta es sobre **empleados presentes en la oficina** esa semana (no todos los empleados registrados).

### Respuestas parcialmente correctas (parcial)

* Dice algo como “no se ve una diferencia grande en el uso del comedor entre sedes”, pero:

  * No cita datos concretos, **o**
  * Afirma que en Norte usan “un poco más otras alternativas” porque ve 22% vs 20%, pero aclara que la diferencia es chica y probablemente no explica el problema.
* Idea central todavía útil: *no* hay evidencia de que “todos se van a comer afuera” en Norte.

### Errores graves

* Contestar que **sí**, que la gente de Norte “claramente” elige mucho más otros lugares, sin matices, contradiciendo los porcentajes.
* Confundir filas y decir que “en Norte solo 20% usa el comedor y 80% va a otro lado”.
* Ignorar completamente la tabla de encuesta o hablar solo de sensaciones.

### Posibles confusiones a vigilar (para el grader)

* Tratar las diferencias de 1–2 p.p. como enormes.
* Olvidar que la encuesta se hizo solo a **presentes en la oficina** (lo que se conecta con la raíz del problema en P3).
* Leer “Otro lugar” como si fuera la categoría principal y mezclar qué porcentaje corresponde a qué.

---

## Pregunta 2

**“¿Las ventas en la sede Norte bajaron en general o solo en un momento específico?”**

Esta es la pregunta que depende más del **gráfico**.

### Información clave del gráfico (lo mínimo que hay que captar)

* Hay **tres paneles**: “Hace 3 semanas”, “Hace 2 semanas”, “Hace 1 semana”. Cada panel muestra de lunes a viernes.
* Eje Y: número de almuerzos (≈0 a 120).
* Para las dos sedes:

  * **Lunes a jueves**: Norte y Sur se mueven casi pegadas, entre 90 y 100 almuerzos por día.
  * **Viernes**: Sur baja a ≈80; Norte cae a ≈35–40.
* Este patrón de “viernes muy bajo en Norte” se repite en **las tres semanas**.

### Conclusión correcta esperada

* Respuesta tipo:

  > “Las ventas en Norte no bajaron en general: de lunes a jueves son similares a las de Sur y se mantienen estables en las tres semanas. El problema está **concentrado en los viernes**, cuando Norte vende cerca de la mitad de almuerzos que Sur y la mitad de lo que vende los otros días.”
* Debe:

  * Nombrar explícitamente que es un problema **de día de la semana (viernes)**, no de toda la semana.
  * Mencionar que esto ocurre **en las tres semanas**, no solo en una.
  * Idealmente, citar un número o comparación (“Norte vende ~40 almuerzos los viernes vs ~80 en Sur” o “vs ~95 el resto de los días”).

### Respuestas parcialmente correctas (parcial)

* Ve que el problema está en los viernes, pero:

  * No hace referencia a las 3 semanas, **o**
  * Dice algo ambiguo como “sobre todo los viernes” sin ser muy claro, **o**
  * Mezcla con la idea de que “en general Norte está un poquito abajo”, pero reconoce que el gran salto es el viernes.
* La idea principal sigue siendo que el problema **no es una caída general** sino algo concentrado en un momento.

### Errores graves

* Decir que “las ventas en Norte bajaron todos los días / en general”, sin mencionar los viernes ni la similitud lunes-jueves.
* Interpretar el gráfico como una caída a lo largo de 15 días seguidos (leyendo los tres paneles como una sola línea temporal) y concluir una tendencia descendente que no existe.
* Confundir completamente cuál línea es Norte y cuál es Sur.

### Potenciales confusores específicos del gráfico

* **Paneles por semana:** algunos pueden leerlos como un solo eje temporal, no como 3 semanas separadas.
* No notar que la escala del eje Y es la misma en todos los paneles.
* Fijarse solo en “los viernes son más bajos en ambas sedes” y no ver que la caída es muchísimo mayor en Norte.
* Pensar que Norte está “siempre bastante por debajo” en todos los días, cuando en realidad lunes-jueves están casi igual e incluso algún día Norte está levemente arriba.

---

## Pregunta 3

**“¿Algo más del informe te parece relevante para entender lo que está pasando?”**

Esta es, de hecho, la pregunta donde se espera que el participante llegue a la **causa raíz**.

### Conclusión correcta esperada

* Señalar que el punto clave es la **combinación entre:**

  1. La composición de empleados por área en cada sede.
  2. La política de **home office de administración los viernes**.
* Razonamiento esperado:

  * Ambas sedes tienen **125 empleados en total**, pero:

    * Sur: solo 20 en administración y 105 en ventas.
    * Norte: 81 en administración y 44 en ventas.
  * Los de **ventas deben ir siempre** a la oficina; los de administración pueden trabajar desde casa los **viernes**.
  * Por lo tanto, los viernes hay **muchísimos menos empleados presentes en Norte** (donde la mayoría es administración) que en Sur (donde la mayoría es ventas).
  * Eso encaja con el gráfico: los viernes Norte vende alrededor de la mitad de almuerzos que Sur y de los que vende de lunes a jueves.
* Una respuesta muy buena va a decir explícitamente algo como:

  > “El menor volumen de ventas en Norte se explica porque los viernes hay muchos menos empleados en la oficina, ya que en esa sede la mayoría son administrativos que pueden hacer home office ese día; en Sur casi todos son de ventas, que deben ir siempre. Como quienes están presentes usan el comedor en proporciones similares en ambas sedes, la diferencia se debe a que **en Norte hay menos gente para atender los viernes**.”

### Hechos clave que deberían aparecer

* Totales iguales (125 y 125).
* Diferencia fuerte en la **proporción de administración vs ventas** entre sedes.
* Regla de home office de administración los viernes.
* Conexión explícita con el patrón del **viernes en el gráfico** y con la encuesta (mismos porcentajes de uso del comedor entre presentes).

### Respuestas parcialmente correctas (parcial)

* Mencionan **algún** elemento relevante pero no atan todo:

  * “En Norte hay muchos más empleados de administración que pueden trabajar desde casa los viernes”, pero no lo vinculan del todo con la caída en ventas ese día.
  * O dicen “ambas sedes tienen el mismo total de empleados, pero distribuidos distinto por área” sin explicar por qué eso importa.
  * O solo dicen “el problema parece ser que los viernes va menos gente a la oficina en Norte” sin explicitar la tabla de empleados y la política de home office.
* En general, ven que el tema importante es **quién está presente los viernes**, pero la argumentación queda incompleta.

### Errores graves

* Decir que el problema es que “Norte tiene menos empleados en total” (los totales son iguales).
* Culpar a la antigüedad promedio (2,8 vs 2,6 años) como factor principal, sin ninguna conexión lógica con el patrón por día.
* Repetir datos sueltos (números de empleados, antigüedad, etc.) sin sacar ninguna conclusión útil sobre el viernes o la presencia en la oficina.
* Volver a decir que “la gente de Norte prefiere comer afuera”, ignorando lo visto en P1.

---

## Resumen: información clave del gráfico (para usar como checklist al corregir)

Cuando la respuesta use bien el gráfico, debería reflejar al menos 2–3 de estos puntos:

1. **Qué muestra:** número de almuerzos diarios en el comedor por sede (Norte/Sur), de lunes a viernes, en cada una de las **últimas tres semanas**.
2. **Patrón lunes–jueves:** ventas muy similares entre sedes y bastante estables (≈90–100 almuerzos diarios).
3. **Patrón viernes:**

   * Sur: ≈80 almuerzos.
   * Norte: ≈35–40 almuerzos.
   * Diferencia de unos **40 almuerzos** cada viernes a favor de Sur.
4. **Estabilidad en el tiempo:** este mismo patrón de “viernes muy bajo en Norte” se repite las 3 semanas; no hay una tendencia de caída general.
5. **Implicancia:** el menor total semanal de Norte se explica casi completamente por ese **“pozo” de los viernes**, no por problemas el resto de los días.

Con esta adaptación, la guía genérica se puede usar directamente para puntuar diagnóstico en la tarea de la cafetería, sabiendo qué hechos concretos buscar y qué errores de lectura del informe son más críticos.

</diagnostic>
<solution>
Va la rúbrica específica para la **sección de solución** en la tarea de la cafetería (Sabores Express).

---

## 1. ¿Cuál es la **causa raíz** en este caso?

Para calibrar toda la rúbrica, fijemos explícitamente la causa raíz que queremos que la solución ataque:

* Las dos sedes tienen **125 empleados** cada una, pero con composición muy distinta:

  * Sur: 20 administración, 105 ventas.
  * Norte: 81 administración, 44 ventas.
* Los **empleados de administración pueden hacer home office los viernes**; los de ventas deben ir **presencialmente de lunes a viernes**.
* La encuesta muestra que, entre quienes están en la oficina, **la proporción que almuerza en el comedor es casi igual en ambas sedes todos los días** (≈75–80%).
* El gráfico muestra que:

  * De **lunes a jueves**, Norte y Sur venden números muy similares de almuerzos.
  * Los **viernes**, la sede Norte vende aproximadamente **la mitad** que la Sur y la mitad de lo que vende ella misma de lunes a jueves, y esto se repite en las **tres semanas**.

👉 **Causa raíz:**
La sede Norte vende menos almuerzos principalmente porque **los viernes hay muchos menos empleados físicamente presentes en la oficina**, ya que en esa sede la mayoría son administrativos con home office permitido ese día. Entre los que sí están presentes, **no usan menos el comedor que en Sur**; simplemente hay menos gente a la que venderle.

Cualquier solución que realmente ataque la causa raíz (**solution_root_cause**) tiene que apuntar a este mecanismo:

> *baja asistencia presencial los viernes en Norte → menos potenciales clientes para el comedor ese día*.

---

## 2. Rúbrica específica – **solution_root_cause**

### Respuestas que sí atacan la causa raíz

Se considera que la solución sí ataca la causa raíz si **al menos una** de las acciones propuestas:

* Reconoce explícitamente que:

  * el problema está **concentrado en los viernes**, y
  * se debe a que **en Norte hay menos personas presentes en la oficina**, por la combinación de:

    * alta proporción de personal administrativo, y
    * política de **home office los viernes** solo para administración.
* Y propone algo que **mitigue o gestione ese problema**, por ejemplo:

  **Aumentar o redistribuir la presencia en la oficina:**

  * Proponer a Infotech:

    * *“Negociar con RRHH que el home office de administración se reparta entre distintos días (ej. que no todos se queden en casa justo los viernes), o que una parte del equipo rote y vaya algunos viernes para evitar que caiga tanto la asistencia.”*
    * *“Sugerir un piloto donde parte de administración haga home los miércoles y parte los viernes, para recuperar algo de flujo de gente en la sede Norte los viernes.”*

  **Llegar a quienes están en home office los viernes:**

  * *“Ofrecer un servicio de viandas/delivery para los administrativos de la sede Norte que trabajan desde casa los viernes, coordinado con Infotech.”*
  * *“Armar combos especiales de almuerzo con envío a domicilio para empleados de Norte en home office, con comunicación vía mail interno.”*

  **Adaptarse de forma explícita al menor flujo presencial de los viernes en Norte:**

  * *“Rediseñar la operación y las metas de ventas de la sede Norte los viernes, asumiendo una base menor de clientes por el home office, por ejemplo reduciendo personal o producción ese día y reforzando la oferta lunes–jueves.”*
  * *“Plantear a Adriana ajustar el contrato / objetivos entre sedes, explicando que la diferencia Norte–Sur es estructural por la política laboral.”*

  En estos casos, aunque no se logre “igualar” completamente las ventas, la propuesta **trata directamente con el hecho de que hay menos gente presente** y se construye alrededor de eso.

> Regla práctica: si el/la participante menciona “menos gente en la oficina los viernes en Norte por el home office / muchos administrativos” **y** sus acciones están diseñadas pensando en esa realidad, eso indica que la respuesta identifica correctamente la causa raíz.

---

### Respuestas que no atacan la causa raíz

Se considera que la solución no ataca la causa raíz cuando:

* La solución se enfoca en **otra causa que no es la verdadera**, por ejemplo:

  * “En Norte la gente prefiere comer afuera / en otros lugares” (la encuesta muestra que no).
  * “El problema es el menú / la calidad del servicio en Norte, hay que mejorarlos.”
  * “Hay menos empleados en total en Norte” (es falso: hay 125 y 125).
  * “El problema es la antigüedad de los empleados” (no hay conexión con el patrón de los viernes).
* O propone acciones que **no tienen nada que ver** con el tema de la asistencia o el home office:

  * Marketing genérico: “hacer más promociones”, “poner carteles”, “publicar en redes sociales”.
  * Cambios de precios o menú sin conectar con presencia: “bajar los precios en Norte”, “agregar más platos vegetarianos”.
  * Comentarios vacíos: “mejorar el servicio”, “escuchar más a los clientes”, sin referencia a los viernes o al home office.

También es problemático si la solución es tan vaga que **no se entiende contra qué problema apunta**.

> **Regla de pasa/no pasa conceptual:** si la solución no ataca la causa raíz, la especificidad y el realismo de cualquier otra acción pierden relevancia, sin importar qué tan “lindo” esté escrito.

---

## 3. Rúbrica específica – **solution_specificity**

> Estas consideraciones son útiles cuando la respuesta ya identificó la causa raíz; de lo contrario, hablar de “detalle” o “realismo” de la solución tiene poco sentido.

### Propuesta concreta y accionable

Características:

* Explica con cierto detalle **qué hacer, quién lo hace, cómo y/o cuándo**.
* Se ve claramente **el vínculo con la causa raíz** (poca gente en la oficina los viernes en Norte por home office / composición de personal).
* No es solo “idea general”: baja al plano operativo.

**Ejemplos típicos (adaptables):**

* **Cambiar/redistribuir home office vía negociación:**

  * *“En base a que en Norte la mayoría son administrativos y los viernes pueden hacer home office, propondría pedirle a Adriana una reunión con RRHH de Infotech para sugerir un esquema rotativo: que el 50% del equipo de administración de Norte haga home los miércoles y el 50% los viernes, alternando cada tres meses. De esa forma garantizamos que todos los viernes haya un grupo mínimo de administrativos en la oficina. Podríamos medir el impacto en ventas en un período de prueba de 2–3 meses antes de hacer el cambio permanente.”*

* **Extender el negocio a quienes están en home office:**

  * *“Como los administrativos de Norte no están en la oficina los viernes, propongo lanzar un servicio de viandas a domicilio solo para empleados de Infotech Norte ese día: enviaríamos un mail interno los miércoles con el menú del viernes y un link para reservar hasta el jueves a las 15 hs. El viernes a mediodía un repartidor hace un circuito único con todas las entregas en ese barrio. Así agregamos como clientes a quienes hoy no pasan por el comedor.”*

* **Ajustar operación y metas a la nueva realidad:**

  * *“Dado que por la política de home office el potencial de clientes de Norte los viernes es estructuralmente menor, propongo: (1) reducir el personal de cocina de Norte ese día y que uno de los empleados rote a la sede Sur, donde la demanda es mayor; (2) adaptar el menú de los viernes en Norte a opciones más simples de preparar; y (3) redefinir con Adriana y el cliente expectativas de ventas para esa sede los viernes, explicando el motivo.”*

En todos los casos, la acción no es solo “cambiar home office” o “hacer delivery”, sino que incluye **pasos concretos, actores, plazos** o mecanismos de seguimiento.

---

### Idea en la dirección correcta pero poco detallada

* La solución **sí apunta al problema correcto** (home office / menos gente en la oficina los viernes), pero:

  * se queda en el nivel de **“idea general”**, o
  * le falta explicar cómo se implementaría.

**Ejemplos:**

* *“Como el problema en Norte es que los administrativos hacen home office los viernes, sugeriría hablar con la empresa para que cambien esa modalidad y no todos se queden en casa ese día.”*
  (Correcto en espíritu, pero sin detalles de cómo, con quién, qué tipo de cambio, prueba piloto, etc.)

* *“Podemos ofrecer almuerzos con envío a los empleados de Norte que trabajan desde casa los viernes.”*
  (De nuevo, buena idea, pero no dice cómo se toman los pedidos, cómo se entrega, en qué horario, quién lo organiza.)

* *“Adaptar la operación de Norte a que haya menos gente los viernes, por ejemplo ajustando personal o producción.”*
  (No explica qué ajustes, ni cuándo, ni cómo se decide el nivel.)

Es decir: **la diana es la correcta, pero el disparo es muy amplio**.

---

### Muy vago o inexistente (con la causa raíz identificada)

Casos típicos:

* Menciona el problema correcto pero con frases casi vacías:

  * *“Tomar medidas para solucionar el tema del home office.”*
  * *“Revisar la política de trabajo de los administrativos para que no nos afecte tanto.”*
* O solo dice algo como:

  * *“Hablar con la empresa sobre este tema.”*
  * sin nada más concreto.

También es problemático si, pese a haber identificado la causa raíz en algún momento del texto, **no aparece ninguna acción asociada** (por ejemplo, cierra solo con “explicaría esta situación al cliente y listo”).

---

## 4. Rúbrica específica – **solution_realism**

> Estas consideraciones solo tienen sentido si la solución realmente ataca la causa raíz; de lo contrario, el realismo de otras acciones pierde relevancia.

### Propuestas realistas para el contexto

Las propuestas se consideran realistas cuando las acciones que atacan la causa raíz son **plausibles para un emprendimiento que maneja el comedor** de una empresa como Infotech:

* Acciones que **sí están bajo control** de Sabores Express:

  * Ajustar el menú, horarios y dotación de personal por sede y día.
  * Implementar un servicio limitado de delivery / viandas para empleados.
  * Proponer promociones internas específicas para empleados de Infotech.
* Acciones que implican a Infotech pero en términos de **sugerir o negociar**, no de imponer:

  * Pedir una reunión con RRHH para sugerir rotación de días de home office.
  * Proponer un piloto acotado para redistribuir la presencia en la oficina.
  * Acordar nuevas metas u objetivos de ventas por sede explicando el diagnóstico.
* Cambios razonables de escala: pruebas piloto, ajustes graduales, uso de medios de comunicación internos (mail semanal, carteles, etc.).

En resumen: **no necesita ser algo súper barato o trivial**, pero sí algo que podría imaginarse implementando una pyme proveedora de comedor, sin tener poder absoluto sobre la política laboral de Infotech ni recursos infinitos.

---

### Propuestas poco realistas o desproporcionadas

Ejemplos de soluciones que, aunque mencionen la causa raíz, son poco creíbles:

* Asumir que Sabores Express **controla la política laboral de Infotech**:

  * *“Obligar a la empresa a eliminar el home office de los administrativos los viernes.”*
  * *“Decidir que todos los empleados de administración deben volver a la oficina a tiempo completo.”*
* Acciones **desmesuradas** para el tamaño del negocio:

  * *“Abrir varias nuevas sedes en otros edificios para compensar.”*
  * *“Financiar nosotros un bono salarial para que los administrativos vayan los viernes.”*
* Medidas que implican cambios enormes fuera del alcance razonable del rol:

  * Reformas laborales, cambios masivos en contratos de trabajo, etc.

Si al leer la propuesta pensás “esto está fuera del control de la empresa del comedor” o “es de otra escala”, es una señal de que el realismo de la propuesta es muy bajo en este contexto.

---

## 5. Mini-checklist para revisar soluciones en esta tarea

1. **¿Habla de los viernes y de que hay menos gente en la oficina Norte por el home office / muchos administrativos?**

   * Sí → indica que la respuesta está apuntando a la causa raíz.
   * No / se enfoca en otra cosa → indica que la solución se centra en una causa equivocada y suele venir acompañada de propuestas vagas o poco realistas.

2. Si la respuesta sí identifica la causa raíz:

   * ¿Describe acciones concretas (qué, quién, cómo, cuándo)?

     * Sí, con buen nivel de detalle → alta especificidad (propuesta muy concreta y accionable).
     * Más o menos, ideas generales → especificidad intermedia (idea correcta pero poco detallada).
     * Muy vago o casi sin acciones → baja especificidad (casi sin contenido accionable).
   * ¿Las acciones son razonables para un proveedor de comedor?

     * Sí, son negociables e implementables → propuestas realistas para el contexto.
     * No, suponen poderes o recursos irreales → propuestas poco realistas o desproporcionadas.

Con esta guía ya tenés criterios finos y específicos para evaluar la parte de **solución** en la tarea de la cafetería.

</solution>
</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/lunch/detailed_task_facts_lunch.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/lunch/detailed_task_facts_lunch.md`。

### 7. detailed_task_rubric_lunch.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>

<diagnostic>
Voy directo a lo que pedís: cómo bajar la guía genérica al caso concreto de **tarea_cafeteria** para la parte de **diagnóstico**, marcando hechos clave, posibles confusiones y el rol del gráfico.

---

## Resumen mínimo del caso (para tenerlo en la cabeza)

* En **ambas sedes hay 125 empleados**, pero con composición distinta:

  * Sur: 20 administración, 105 ventas.
  * Norte: 81 administración, 44 ventas.
* Empleados de **administración pueden hacer home office los viernes**; ventas tiene que ir de lunes a viernes.
* La **encuesta** de la semana pasada muestra que, de los empleados presentes en la oficina, entre **75% y 80% almuerza en el comedor** tanto en Norte como en Sur, todos los días.
* El **gráfico de ventas diarias** muestra que:

  * De **lunes a jueves** las ventas en Norte y Sur son muy similares (≈90–100 almuerzos por día en ambas).
  * Los **viernes** la Sur vende ≈80 almuerzos, pero la Norte cae a ≈35–40, es decir, **aprox. la mitad** que Sur y la mitad de lo que vende Norte el resto de la semana.
  * Este patrón se repite las **tres semanas**.

Con esto en mente, voy pregunta por pregunta.

---

## Pregunta 1

**“Los clientes de la sede Norte, ¿están eligiendo en mayor medida otras alternativas de almuerzo fuera del comedor?”**

### Conclusión correcta esperada (2 puntos)

* La respuesta debe ser básicamente: **“No, los empleados de Norte no están eligiendo mucho más otras alternativas que los de Sur”**.
* Apoyado en que:

  * En la semana pasada, la **proporción que almuerza en el comedor es muy parecida en ambas sedes** todos los días (entre 75% y 80%).
  * Las diferencias día a día son de solo 1–2 puntos porcentuales; incluso algún día Norte tiene **más** uso del comedor (por ejemplo miércoles: Norte 80% vs Sur 75%).
* Conclusión adicional deseable: “O sea, entre quienes están en la oficina, **no parece que en Norte se escape más gente a comer afuera**; el problema tiene que venir por otro lado (cantidad de gente presente, no preferencias de los presentes).”

### Hechos clave que conviene mencionar

* Citar al menos 1–2 números de la tabla de encuesta, por ejemplo:

  * “Lunes: Sur 80% comedor vs Norte 78%; viernes: 78% comedor en ambas sedes”.
* Aclarar que la encuesta es sobre **empleados presentes en la oficina** esa semana (no todos los empleados registrados).

### Respuestas típicas para 1 punto (parcial)

* Dice algo como “no se ve una diferencia grande en el uso del comedor entre sedes”, pero:

  * No cita datos concretos, **o**
  * Afirma que en Norte usan “un poco más otras alternativas” porque ve 22% vs 20%, pero aclara que la diferencia es chica y probablemente no explica el problema.
* Idea central todavía útil: *no* hay evidencia de que “todos se van a comer afuera” en Norte.

### Errores graves / 0 puntos

* Contestar que **sí**, que la gente de Norte “claramente” elige mucho más otros lugares, sin matices, contradiciendo los porcentajes.
* Confundir filas y decir que “en Norte solo 20% usa el comedor y 80% va a otro lado”.
* Ignorar completamente la tabla de encuesta o hablar solo de sensaciones.

### Posibles confusiones a vigilar (para el grader)

* Tratar las diferencias de 1–2 p.p. como enormes.
* Olvidar que la encuesta se hizo solo a **presentes en la oficina** (lo que se conecta con la raíz del problema en P3).
* Leer “Otro lugar” como si fuera la categoría principal y mezclar qué porcentaje corresponde a qué.

---

## Pregunta 2

**“¿Las ventas en la sede Norte bajaron en general o solo en un momento específico?”**

Esta es la pregunta que depende más del **gráfico**.

### Información clave del gráfico (lo mínimo que hay que captar)

* Hay **tres paneles**: “Hace 3 semanas”, “Hace 2 semanas”, “Hace 1 semana”. Cada panel muestra de lunes a viernes.
* Eje Y: número de almuerzos (≈0 a 120).
* Para las dos sedes:

  * **Lunes a jueves**: Norte y Sur se mueven casi pegadas, entre 90 y 100 almuerzos por día.
  * **Viernes**: Sur baja a ≈80; Norte cae a ≈35–40.
* Este patrón de “viernes muy bajo en Norte” se repite en **las tres semanas**.

### Conclusión correcta esperada (2 puntos)

* Respuesta tipo:

  > “Las ventas en Norte no bajaron en general: de lunes a jueves son similares a las de Sur y se mantienen estables en las tres semanas. El problema está **concentrado en los viernes**, cuando Norte vende cerca de la mitad de almuerzos que Sur y la mitad de lo que vende los otros días.”
* Debe:

  * Nombrar explícitamente que es un problema **de día de la semana (viernes)**, no de toda la semana.
  * Mencionar que esto ocurre **en las tres semanas**, no solo en una.
  * Idealmente, citar un número o comparación (“Norte vende ~40 almuerzos los viernes vs ~80 en Sur” o “vs ~95 el resto de los días”).

### Respuestas típicas para 1 punto (parcial)

* Ve que el problema está en los viernes, pero:

  * No hace referencia a las 3 semanas, **o**
  * Dice algo ambiguo como “sobre todo los viernes” sin ser muy claro, **o**
  * Mezcla con la idea de que “en general Norte está un poquito abajo”, pero reconoce que el gran salto es el viernes.
* La idea principal sigue siendo que el problema **no es una caída general** sino algo concentrado en un momento.

### Errores graves / 0 puntos

* Decir que “las ventas en Norte bajaron todos los días / en general”, sin mencionar los viernes ni la similitud lunes-jueves.
* Interpretar el gráfico como una caída a lo largo de 15 días seguidos (leyendo los tres paneles como una sola línea temporal) y concluir una tendencia descendente que no existe.
* Confundir completamente cuál línea es Norte y cuál es Sur.

### Potenciales confusores específicos del gráfico

* **Paneles por semana:** algunos pueden leerlos como un solo eje temporal, no como 3 semanas separadas.
* No notar que la escala del eje Y es la misma en todos los paneles.
* Fijarse solo en “los viernes son más bajos en ambas sedes” y no ver que la caída es muchísimo mayor en Norte.
* Pensar que Norte está “siempre bastante por debajo” en todos los días, cuando en realidad lunes-jueves están casi igual e incluso algún día Norte está levemente arriba.

---

## Pregunta 3

**“¿Algo más del informe te parece relevante para entender lo que está pasando?”**

Esta es, de hecho, la pregunta donde se espera que el participante llegue a la **causa raíz**.

### Conclusión correcta esperada (2 puntos)

* Señalar que el punto clave es la **combinación entre:**

  1. La composición de empleados por área en cada sede.
  2. La política de **home office de administración los viernes**.
* Razonamiento esperado:

  * Ambas sedes tienen **125 empleados en total**, pero:

    * Sur: solo 20 en administración y 105 en ventas.
    * Norte: 81 en administración y 44 en ventas.
  * Los de **ventas deben ir siempre** a la oficina; los de administración pueden trabajar desde casa los **viernes**.
  * Por lo tanto, los viernes hay **muchísimos menos empleados presentes en Norte** (donde la mayoría es administración) que en Sur (donde la mayoría es ventas).
  * Eso encaja con el gráfico: los viernes Norte vende alrededor de la mitad de almuerzos que Sur y de los que vende de lunes a jueves.
* Un muy buen 2 puntos va a decir explícitamente algo como:

  > “El menor volumen de ventas en Norte se explica porque los viernes hay muchos menos empleados en la oficina, ya que en esa sede la mayoría son administrativos que pueden hacer home office ese día; en Sur casi todos son de ventas, que deben ir siempre. Como quienes están presentes usan el comedor en proporciones similares en ambas sedes, la diferencia se debe a que **en Norte hay menos gente para atender los viernes**.”

### Hechos clave que deberían aparecer

* Totales iguales (125 y 125).
* Diferencia fuerte en la **proporción de administración vs ventas** entre sedes.
* Regla de home office de administración los viernes.
* Conexión explícita con el patrón del **viernes en el gráfico** y con la encuesta (mismos porcentajes de uso del comedor entre presentes).

### Respuestas típicas para 1 punto (parcial)

* Mencionan **algún** elemento relevante pero no atan todo:

  * “En Norte hay muchos más empleados de administración que pueden trabajar desde casa los viernes”, pero no lo vinculan del todo con la caída en ventas ese día.
  * O dicen “ambas sedes tienen el mismo total de empleados, pero distribuidos distinto por área” sin explicar por qué eso importa.
  * O solo dicen “el problema parece ser que los viernes va menos gente a la oficina en Norte” sin explicitar la tabla de empleados y la política de home office.
* En general, ven que el tema importante es **quién está presente los viernes**, pero la argumentación queda incompleta.

### Errores graves / 0 puntos

* Decir que el problema es que “Norte tiene menos empleados en total” (los totales son iguales).
* Culpar a la antigüedad promedio (2,8 vs 2,6 años) como factor principal, sin ninguna conexión lógica con el patrón por día.
* Repetir datos sueltos (números de empleados, antigüedad, etc.) sin sacar ninguna conclusión útil sobre el viernes o la presencia en la oficina.
* Volver a decir que “la gente de Norte prefiere comer afuera”, ignorando lo visto en P1.

---

## Resumen: información clave del gráfico (para usar como checklist al corregir)

Cuando la respuesta use bien el gráfico, debería reflejar al menos 2–3 de estos puntos:

1. **Qué muestra:** número de almuerzos diarios en el comedor por sede (Norte/Sur), de lunes a viernes, en cada una de las **últimas tres semanas**.
2. **Patrón lunes–jueves:** ventas muy similares entre sedes y bastante estables (≈90–100 almuerzos diarios).
3. **Patrón viernes:**

   * Sur: ≈80 almuerzos.
   * Norte: ≈35–40 almuerzos.
   * Diferencia de unos **40 almuerzos** cada viernes a favor de Sur.
4. **Estabilidad en el tiempo:** este mismo patrón de “viernes muy bajo en Norte” se repite las 3 semanas; no hay una tendencia de caída general.
5. **Implicancia:** el menor total semanal de Norte se explica casi completamente por ese **“pozo” de los viernes**, no por problemas el resto de los días.

Con esta adaptación, la guía genérica se puede usar directamente para puntuar diagnóstico en la tarea de la cafetería, sabiendo qué hechos concretos buscar y qué errores de lectura del informe son más críticos.

</diagnostic>
<solution>
Va la rúbrica específica para la **sección de solución** en la tarea de la cafetería (Sabores Express).

---

## 1. ¿Cuál es la **causa raíz** en este caso?

Para calibrar toda la rúbrica, fijemos explícitamente la causa raíz que queremos que la solución ataque:

* Las dos sedes tienen **125 empleados** cada una, pero con composición muy distinta:

  * Sur: 20 administración, 105 ventas.
  * Norte: 81 administración, 44 ventas.
* Los **empleados de administración pueden hacer home office los viernes**; los de ventas deben ir **presencialmente de lunes a viernes**.
* La encuesta muestra que, entre quienes están en la oficina, **la proporción que almuerza en el comedor es casi igual en ambas sedes todos los días** (≈75–80%).
* El gráfico muestra que:

  * De **lunes a jueves**, Norte y Sur venden números muy similares de almuerzos.
  * Los **viernes**, la sede Norte vende aproximadamente **la mitad** que la Sur y la mitad de lo que vende ella misma de lunes a jueves, y esto se repite en las **tres semanas**.

👉 **Causa raíz:**
La sede Norte vende menos almuerzos principalmente porque **los viernes hay muchos menos empleados físicamente presentes en la oficina**, ya que en esa sede la mayoría son administrativos con home office permitido ese día. Entre los que sí están presentes, **no usan menos el comedor que en Sur**; simplemente hay menos gente a la que venderle.

Cualquier solución que se lleve el punto de **solution_root_cause** tiene que apuntar a este mecanismo:

> *baja asistencia presencial los viernes en Norte → menos potenciales clientes para el comedor ese día*.

---

## 2. Rúbrica específica – **solution_root_cause** (0 o 1 punto)

### 1 punto – **Sí ataca la causa raíz**

Se otorga si **al menos una** de las acciones propuestas:

* Reconoce explícitamente que:

  * el problema está **concentrado en los viernes**, y
  * se debe a que **en Norte hay menos personas presentes en la oficina**, por la combinación de:

    * alta proporción de personal administrativo, y
    * política de **home office los viernes** solo para administración.
* Y propone algo que **mitigue o gestione ese problema**, por ejemplo:

  **Aumentar o redistribuir la presencia en la oficina:**

  * Proponer a Infotech:

    * *“Negociar con RRHH que el home office de administración se reparta entre distintos días (ej. que no todos se queden en casa justo los viernes), o que una parte del equipo rote y vaya algunos viernes para evitar que caiga tanto la asistencia.”*
    * *“Sugerir un piloto donde parte de administración haga home los miércoles y parte los viernes, para recuperar algo de flujo de gente en la sede Norte los viernes.”*

  **Llegar a quienes están en home office los viernes:**

  * *“Ofrecer un servicio de viandas/delivery para los administrativos de la sede Norte que trabajan desde casa los viernes, coordinado con Infotech.”*
  * *“Armar combos especiales de almuerzo con envío a domicilio para empleados de Norte en home office, con comunicación vía mail interno.”*

  **Adaptarse de forma explícita al menor flujo presencial de los viernes en Norte:**

  * *“Rediseñar la operación y las metas de ventas de la sede Norte los viernes, asumiendo una base menor de clientes por el home office, por ejemplo reduciendo personal o producción ese día y reforzando la oferta lunes–jueves.”*
  * *“Plantear a Adriana ajustar el contrato / objetivos entre sedes, explicando que la diferencia Norte–Sur es estructural por la política laboral.”*

  En estos casos, aunque no se logre “igualar” completamente las ventas, la propuesta **trata directamente con el hecho de que hay menos gente presente** y se construye alrededor de eso.

> Regla práctica: si el/la participante menciona “menos gente en la oficina los viernes en Norte por el home office / muchos administrativos” **y** sus acciones están diseñadas pensando en esa realidad, poné **solution_root_cause = 1**.

---

### 0 puntos – **No ataca la causa raíz**

Se pone 0 cuando:

* La solución se enfoca en **otra causa que no es la verdadera**, por ejemplo:

  * “En Norte la gente prefiere comer afuera / en otros lugares” (la encuesta muestra que no).
  * “El problema es el menú / la calidad del servicio en Norte, hay que mejorarlos.”
  * “Hay menos empleados en total en Norte” (es falso: hay 125 y 125).
  * “El problema es la antigüedad de los empleados” (no hay conexión con el patrón de los viernes).
* O propone acciones que **no tienen nada que ver** con el tema de la asistencia o el home office:

  * Marketing genérico: “hacer más promociones”, “poner carteles”, “publicar en redes sociales”.
  * Cambios de precios o menú sin conectar con presencia: “bajar los precios en Norte”, “agregar más platos vegetarianos”.
  * Comentarios vacíos: “mejorar el servicio”, “escuchar más a los clientes”, sin referencia a los viernes o al home office.

También va 0 si la solución es tan vaga que **no se entiende contra qué problema apunta**.

> **Regla de pasa/no pasa:** si solution_root_cause = 0 ⇒ **solution_specificity = 0** y **solution_realism = 0**, sin importar qué tan “lindo” esté escrito.

---

## 3. Rúbrica específica – **solution_specificity** (0, 1 o 2 puntos)

> **Solo se aplica si solution_root_cause = 1.**
> Si no, queda automáticamente en 0.

### 2 puntos – **Propuesta concreta y accionable**

Características:

* Explica con cierto detalle **qué hacer, quién lo hace, cómo y/o cuándo**.
* Se ve claramente **el vínculo con la causa raíz** (poca gente en la oficina los viernes en Norte por home office / composición de personal).
* No es solo “idea general”: baja al plano operativo.

**Ejemplos típicos (adaptables):**

* **Cambiar/redistribuir home office vía negociación:**

  * *“En base a que en Norte la mayoría son administrativos y los viernes pueden hacer home office, propondría pedirle a Adriana una reunión con RRHH de Infotech para sugerir un esquema rotativo: que el 50% del equipo de administración de Norte haga home los miércoles y el 50% los viernes, alternando cada tres meses. De esa forma garantizamos que todos los viernes haya un grupo mínimo de administrativos en la oficina. Podríamos medir el impacto en ventas en un período de prueba de 2–3 meses antes de hacer el cambio permanente.”*

* **Extender el negocio a quienes están en home office:**

  * *“Como los administrativos de Norte no están en la oficina los viernes, propongo lanzar un servicio de viandas a domicilio solo para empleados de Infotech Norte ese día: enviaríamos un mail interno los miércoles con el menú del viernes y un link para reservar hasta el jueves a las 15 hs. El viernes a mediodía un repartidor hace un circuito único con todas las entregas en ese barrio. Así agregamos como clientes a quienes hoy no pasan por el comedor.”*

* **Ajustar operación y metas a la nueva realidad:**

  * *“Dado que por la política de home office el potencial de clientes de Norte los viernes es estructuralmente menor, propongo: (1) reducir el personal de cocina de Norte ese día y que uno de los empleados rote a la sede Sur, donde la demanda es mayor; (2) adaptar el menú de los viernes en Norte a opciones más simples de preparar; y (3) redefinir con Adriana y el cliente expectativas de ventas para esa sede los viernes, explicando el motivo.”*

En todos los casos, la acción no es solo “cambiar home office” o “hacer delivery”, sino que incluye **pasos concretos, actores, plazos** o mecanismos de seguimiento.

---

### 1 punto – **Idea en la dirección correcta pero poco detallada**

* La solución **sí apunta al problema correcto** (home office / menos gente en la oficina los viernes), pero:

  * se queda en el nivel de **“idea general”**, o
  * le falta explicar cómo se implementaría.

**Ejemplos:**

* *“Como el problema en Norte es que los administrativos hacen home office los viernes, sugeriría hablar con la empresa para que cambien esa modalidad y no todos se queden en casa ese día.”*
  (Correcto en espíritu, pero sin detalles de cómo, con quién, qué tipo de cambio, prueba piloto, etc.)

* *“Podemos ofrecer almuerzos con envío a los empleados de Norte que trabajan desde casa los viernes.”*
  (De nuevo, buena idea, pero no dice cómo se toman los pedidos, cómo se entrega, en qué horario, quién lo organiza.)

* *“Adaptar la operación de Norte a que haya menos gente los viernes, por ejemplo ajustando personal o producción.”*
  (No explica qué ajustes, ni cuándo, ni cómo se decide el nivel.)

Es decir: **la diana es la correcta, pero el disparo es muy amplio**.

---

### 0 puntos – **Muy vago o inexistente (con root_cause = 1)**

Casos típicos:

* Menciona el problema correcto pero con frases casi vacías:

  * *“Tomar medidas para solucionar el tema del home office.”*
  * *“Revisar la política de trabajo de los administrativos para que no nos afecte tanto.”*
* O solo dice algo como:

  * *“Hablar con la empresa sobre este tema.”*
  * sin nada más concreto.

También se pone 0 si, pese a haber identificado la causa raíz en algún momento del texto, **no aparece ninguna acción asociada** (por ejemplo, cierra solo con “explicaría esta situación al cliente y listo”).

---

## 4. Rúbrica específica – **solution_realism** (0 o 1 punto)

> **Solo se aplica si solution_root_cause = 1.**
> Si no, queda automáticamente en 0.

### 1 punto – **Propuestas realistas para el contexto**

Se otorga cuando las acciones que atacan la causa raíz son **plausibles para un emprendimiento que maneja el comedor** de una empresa como Infotech:

* Acciones que **sí están bajo control** de Sabores Express:

  * Ajustar el menú, horarios y dotación de personal por sede y día.
  * Implementar un servicio limitado de delivery / viandas para empleados.
  * Proponer promociones internas específicas para empleados de Infotech.
* Acciones que implican a Infotech pero en términos de **sugerir o negociar**, no de imponer:

  * Pedir una reunión con RRHH para sugerir rotación de días de home office.
  * Proponer un piloto acotado para redistribuir la presencia en la oficina.
  * Acordar nuevas metas u objetivos de ventas por sede explicando el diagnóstico.
* Cambios razonables de escala: pruebas piloto, ajustes graduales, uso de medios de comunicación internos (mail semanal, carteles, etc.).

En resumen: **no necesita ser algo súper barato o trivial**, pero sí algo que podría imaginarse implementando una pyme proveedora de comedor, sin tener poder absoluto sobre la política laboral de Infotech ni recursos infinitos.

---

### 0 puntos – **Propuestas poco realistas o desproporcionadas**

Ejemplos de soluciones que, aunque mencionen la causa raíz, son poco creíbles:

* Asumir que Sabores Express **controla la política laboral de Infotech**:

  * *“Obligar a la empresa a eliminar el home office de los administrativos los viernes.”*
  * *“Decidir que todos los empleados de administración deben volver a la oficina a tiempo completo.”*
* Acciones **desmesuradas** para el tamaño del negocio:

  * *“Abrir varias nuevas sedes en otros edificios para compensar.”*
  * *“Financiar nosotros un bono salarial para que los administrativos vayan los viernes.”*
* Medidas que implican cambios enormes fuera del alcance razonable del rol:

  * Reformas laborales, cambios masivos en contratos de trabajo, etc.

Si al leer la propuesta pensás “esto está fuera del control de la empresa del comedor” o “es de otra escala”, marcá **solution_realism = 0**.

---

## 5. Mini-checklist para corregir soluciones en esta tarea

1. **¿Habla de los viernes y de que hay menos gente en la oficina Norte por el home office / muchos administrativos?**

   * Sí → candidata a solution_root_cause = 1.
   * No / se enfoca en otra cosa → solution_root_cause = 0 → specificity = 0, realism = 0.

2. Si **solution_root_cause = 1**:

   * ¿Describe acciones concretas (qué, quién, cómo, cuándo)?

     * Sí, con buen nivel de detalle → specificity = 2.
     * Más o menos, ideas generales → specificity = 1.
     * Muy vago o casi sin acciones → specificity = 0.
   * ¿Las acciones son razonables para un proveedor de comedor?

     * Sí, son negociables/implementables → realism = 1.
     * No, suponen poderes o recursos irreales → realism = 0.

Con esta rúbrica ya tenés criterios finos y específicos para evaluar la parte de **solución** en la tarea de la cafetería.

</solution>
</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/lunch/detailed_task_rubric_lunch.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/lunch/detailed_task_rubric_lunch.md`。

### 8. detailed_task_facts_rest.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：必要上下文。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>
<diagnostic>
Para esta tarea, el diagnóstico gira en torno a **tres preguntas** del mail de Ramiro. Te detallo, para cada una, qué hechos “clave” debería mencionar una buena respuesta, qué cosas suelen confundir y qué aporta el gráfico.

---

## Pregunta 1

**“¿Podrías revisar si el problema viene de la plataforma de envíos?”**

### Conclusión correcta esperada

La demora **no parece venir principalmente de la plataforma**, sino de la **etapa de preparación en el local de la sucursal Norte**.

### Hechos clave que deberían aparecer

Basado en el cuadro de tiempos promedio:

* **Sucursal Sur**

  * Toma del pedido: **9 min**
  * Preparado en el local: **18 min**
  * Entrega al cliente: **13 min**

* **Sucursal Norte**

  * Toma del pedido: **10 min** (solo 1 minuto más que Sur)
  * Preparado en el local: **29 min** (**11 minutos más** que Sur)
  * Entrega al cliente: **15 min** (2 minutos más que Sur)

Puntos que una buena respuesta debería remarcar:

* La mayor parte de la diferencia en tiempo total (Norte ≈ 54 min vs Sur ≈ 40 min) viene de la etapa **“preparado en el local”**, no de la entrega de la plataforma.
* Ambas sucursales usan la **misma plataforma de envíos**, de modo que si la app fuera el problema, lo lógico sería ver demoras también en Sur.

Con eso, la idea central: *“El problema no parece ser la plataforma, sino cómo se está trabajando dentro del local Norte (tiempo de preparación muy largo)”*.

### Respuestas parciales típicas

* Dicen algo como “no parece ser la plataforma porque la entrega tarda 13 vs 15 minutos” pero **no mencionan** la gran diferencia de 11 minutos en preparación.
* O afirman que el problema está en el local Norte pero sin citar ningún número.

### Confusores / errores graves

* Culpar directamente a la plataforma (“el problema es la app / los repartidores”) porque los tiempos en Norte son mayores, sin notar que la diferencia grande está en la preparación en el local.
* Atribuir los 29 minutos de preparación a la plataforma, mezclando etapas.
* Comparar mal los datos (por ejemplo, decir que el preparado es más lento en Sur).

---

## Pregunta 2

**“¿Puede ser que la sucursal Norte tenga más pedidos que la sucursal Sur, o que haya habido un mayor aumento…? ¿O no hay diferencias entre sucursales en los pedidos?”**

Se responde mirando el **gráfico de número diario de pedidos**.

### Información clave del gráfico

* Eje X: **fechas** de tres semanas (aprox. 15/01 a 04/02).
* Eje Y: **número de pedidos diarios**.
* Dos líneas: **Norte** (negro) y **Sur** (amarillo).

Patrones visibles:

* Al inicio ambas sucursales rondan los **18–23 pedidos** diarios; a veces Norte está apenas por encima, otras Sur.
* A partir de la segunda semana, los pedidos **suben en ambas sucursales**.
* El aumento es algo mayor en Sur:

  * Norte pasa de ~20 pedidos al inicio a unos **45** al final.
  * Sur pasa de ~20 a alrededor de **55** pedidos diarios al final.
* Desde más o menos el **25/01**, la línea de Sur queda **siempre igual o por encima** de la de Norte; al final hay una brecha de unos 8–10 pedidos a favor de Sur.

### Conclusión correcta esperada

Algo del estilo:

> “No, la sucursal Norte **no** tiene más pedidos ni un aumento mayor que la Sur. Las dos crecieron, pero Sur termina con más pedidos diarios (≈55 vs ≈45), así que el problema de demoras en Norte no parece explicarse por un volumen de pedidos superior.”

Debe apoyarse en **algún dato concreto** del gráfico (por ejemplo, valores iniciales y finales, o el hecho de que la línea de Sur queda por encima al final).

### Respuestas parciales

* Dicen que los pedidos son “parecidos” y que “en todo caso Sur está un poco por encima”, pero sin números ni mencionar el crecimiento.
* Señalan correctamente que Norte no tiene más pedidos, pero no analizan el aumento relativo.

### Confusores / errores graves

* Afirmar que “Norte tiene claramente más pedidos que Sur” o que el crecimiento es mucho mayor en Norte (lo contrario de lo que se ve).
* **Invertir las leyendas** (creer que la línea amarilla es Norte) y construir todo el diagnóstico a partir de esa lectura errada.
* Ignorar completamente el gráfico y responder hablando solo de tiempos o de empleados.

---

## Pregunta 3

**“¿Algo más del informe te parece relevante para entender lo que está pasando?”**

Acá hay que integrar la info de tiempos, pedidos y personal para identificar la **causa raíz**.

### Hechos clave que deberían aparecer

1. **Refuerzo del cuello de botella en la preparación en Norte**

   * Recordar que el **tiempo de preparado** es **29 min en Norte vs 18 en Sur** (11 minutos más), mientras que toma del pedido y entrega son similares.
   * Esto encaja con las reseñas de “demoras en el envío”: la demora se genera **antes** de que el pedido pase al repartidor.

2. **Número y experiencia de empleados**

   * Ambas sucursales tienen el **mismo total de empleados: 12 cada una**.
   * **Plancha (clave para la preparación):**

     * Norte: 2 empleados, antigüedad promedio **0,5 meses** (muy nuevos).
     * Sur: 2 empleados, antigüedad promedio **4 meses**.
   * **Ensamblado y limpieza:** en Norte son incluso **más experimentados** (12 y 15 meses) que en Sur (5 y 7 meses).
   * Promedio de antigüedad total: Norte **11,6 meses** vs Sur **6 meses**; es decir, Norte no tiene menos experiencia en general, pero **sí tiene gente muy nueva justamente en plancha**.

   ⇒ Un buen diagnóstico conecta esto con el cuello de botella: la inexperiencia en plancha en Norte podría explicar el tiempo extra de preparación.

3. **Volumen de pedidos no excepcional en Norte**

   * Traer de nuevo la info del gráfico: Norte **no recibe más pedidos** que Sur; al final incluso tiene menos.
   * Por lo tanto, las demoras no parecen deberse a un “desborde” de demanda exclusivo de Norte.

### Cómo se ve una buena respuesta

Algo así como:

> “Además de los tiempos de entrega, el informe muestra que el tiempo de **preparación en el local Norte es mucho mayor** (29 vs 18 minutos). Ambas sucursales tienen la misma cantidad de empleados, pero en Norte los de **plancha son muy nuevos** (0,5 meses vs 4 meses en Sur), mientras que el resto del equipo es experimentado. Sumado a que Norte **no tiene más pedidos** que Sur, esto sugiere que la causa principal de las demoras son problemas internos de organización/capacitación en la cocina de Norte, especialmente en plancha, más que la plataforma o un exceso de pedidos.”

### Respuestas parciales

* Mencionan **solo uno** de esos elementos (ej. “tiempo de preparación alto” o “empleados de plancha nuevos”) sin conectarlo claramente con el problema.
* O hablan de “problemas organizativos internos” pero casi sin usar datos concretos del informe.

### Confusores / errores graves

* Decir que “Norte tiene menos empleados” (es falso: las dos tienen 12).
* Afirmar que “en general los empleados de Norte son menos experimentados” (también falso: el promedio de antigüedad es mayor en Norte: 11,6 vs 6 meses).
* Ignorar el tema de tiempos de preparación y enfocarse solo en explicaciones que no aparecen en los datos (marketing, clima, etc.).

---

## En síntesis: información clave del gráfico

* Muestra que **los pedidos aumentan en ambas sucursales** durante tres semanas, desde ~20 pedidos diarios hasta ~45 en Norte y ~55 en Sur.
* **Sur termina con más pedidos y con un aumento algo mayor** que Norte; Norte no está desbordada respecto a Sur.

Esto es central para el diagnóstico: ayuda a **descartar** que el problema de demoras en Norte se deba a que la plataforma esté colapsada por un exceso de pedidos allí, y refuerza la lectura de que el cuello de botella está en la **preparación interna** de la sucursal Norte, probablemente vinculado a la inexperiencia del personal de plancha.
</diagnostic>
<solution>
La idea es que la parte de **solución** esté totalmente alineada con el diagnóstico “correcto” para esta tarea de la hamburguesería. Resumo primero cuál es la **causa raíz esperada**, y después bajo eso a cada subdimensión.

---

## 0. Causa raíz “correcta” en este caso

A partir del informe, la interpretación de referencia es:

* El problema de las bajas reseñas en **Norte** se debe a que los pedidos tardan mucho en estar **listos en el local**, no a la plataforma de envíos.
* En Norte, el tiempo de **preparado en el local** es de **29 minutos vs 18 minutos en Sur** (11 minutos más), mientras que toma del pedido (10 vs 9) y entrega (15 vs 13) son muy parecidos.
* Ambas sucursales tienen el mismo número total de empleados (12), pero en **plancha** los de Norte son muy nuevos (0,5 meses vs 4 meses en Sur), justo en el puesto clave para la preparación.

👉 Entonces, la **causa raíz** que debería atacar la solución es:
**problemas de capacidad/organización en la preparación en el local de la sucursal Norte, especialmente por la inexperiencia del personal de plancha**, más que la plataforma o un exceso de pedidos.

---

## 1. `solution_root_cause` (regla de “pasa/no pasa”)

> Regla global (conceptual): si la solución no ataca la causa raíz, entonces la especificidad y el realismo de cualquier otra acción pierden relevancia.

### Respuestas que atacan la causa raíz

La propuesta incluye **al menos una medida central y explícita** que apunte directamente a:

* Reducir el tiempo de **preparación en el local Norte**, y
* Lo hace focalizando en **plancha / cocina de Norte** (capacitación, organización, dotación de personal, etc.).

Ejemplos de enfoque correcto:

* Capacitar intensivamente a los dos empleados de plancha de Norte, apoyándolos con personal más experimentado.
* Reorganizar el equipo de Norte para que algún empleado experimentado (de ensamblado o limpieza) refuerce plancha en horarios pico.
* Contratar un tercer empleado de plancha para Norte, o trasladar temporalmente a alguien de Sur, con el objetivo explícito de bajar los 29 minutos de preparación.
* Ajustar procesos de cocina en Norte (simplificar pasos, preparar mise en place antes del horario pico, estandarizar tareas) **para reducir el tiempo de preparación**.

También cuenta como centrada en la causa raíz si la persona propone **reducir o gestionar la demanda de Norte en horario pico** (pausar temporalmente la app, limitar pedidos, alargar el tiempo estimado de entrega en la plataforma) *y* lo vincula claramente con que la capacidad de preparación en Norte es el cuello de botella.

> Criterio práctico: si leyendo la solución se ve que la persona entendió que el problema está en **cómo se preparan los pedidos en Norte (sobre todo plancha)** y propone algo concreto para eso, entonces está atacando la causa raíz.

### Respuestas que no ataca la causa raíz

La propuesta se centra en cosas que **no tienen que ver** con la preparación en el local Norte o que son tan vagas que no se sabe qué atacan.

Ejemplos típicos de soluciones que no atacan la causa raíz:

* Culpar y cambiar la **plataforma de envíos** (negociar con la app, “cambiar de aplicación”, “contratar más repartidores”) sin mencionar la preparación en el local.
* Hacer solo **marketing / descuentos / responder reseñas** (“mandar cupones”, “hacer publicidad”, “contestar los comentarios explicando la demora”) sin ninguna medida operativa sobre la cocina de Norte.
* Propuestas centradas en la **sucursal Sur** (más empleados en Sur, cambiar procesos en Sur) sin relación con el problema de Norte.
* Explicaciones que dan por sentado que el problema es un **exceso de pedidos en Norte**, contradiciendo el gráfico, y por eso solo quieren “derivar pedidos a Sur” sin hablar de mejorar la preparación.
* Soluciones ultra vagas: “mejorar el servicio”, “organizar mejor el equipo”, “hacer cambios internos” sin decir qué ni dónde.

> Si después de leer la solución uno podría resumirla como “hacer algo con la app / marketing / clientes en general”, sin ninguna acción clara sobre *preparación en Norte*, entonces la propuesta no está atacando la causa raíz.

---

## 2. `solution_specificity` (guía de especificidad; solo tiene sentido si la causa raíz está bien identificada)

### Propuesta concreta y accionable

Las acciones:

* Están claramente formuladas:

  * **Qué** se va a hacer (ej. capacitar, trasladar gente, contratar, reorganizar procesos).
  * **Dónde** (específicamente en la sucursal Norte, plancha, horarios pico, etc.).
  * Idealmente **quién** o **cómo** (jefe de cocina, empleados de Sur que entrenan, etc.).
  * A veces también **cuándo** o por cuánto tiempo (prueba por 2 semanas, en horarios 20–23 hs, etc.).
* Se conectan explícitamente con el objetivo de **bajar los 29 minutos de preparación en Norte**.

Ejemplos de solución con alta especificidad:

* “Durante las próximas dos semanas, trasladar a un empleado experimentado de ensamblado de Norte a plancha en el horario de 20 a 23 hs (viernes y sábados), y que uno de los de limpieza cubra ensamblado. Al mismo tiempo, pedirle al jefe de cocina de Sur que haga dos jornadas de capacitación con los plancheros de Norte para estandarizar el proceso y apuntar a bajar el tiempo de preparación de 29 a menos de 20 minutos.”
* “Contratar un tercer empleado de plancha para Norte solo para fines de semana y noches, y mientras tanto establecer un protocolo de mise en place (tener ingredientes listos antes del horario pico) y controlar diariamente el tiempo promedio de preparación que reporta la plataforma.”

En general, en las soluciones muy específicas el lector debería poder **imaginar el plan de acción casi como una mini “checklist”**.

### Idea correcta pero poco detallada

* La solución va **en la dirección correcta** (preparación en Norte / plancha), pero:

  * Dice cosas generales como “capacitar al personal de cocina de Norte”, “reforzar la plancha”, “reorganizar procesos” sin explicar mucho el cómo, cuándo o quién.
  * Puede mencionar una medida correcta (“agregar un empleado en plancha”) pero sin decir si es en Norte, en qué horarios, cómo se financia, etc.
* Hay contenido accionable, pero poco operativo.

Ejemplos:

* “Sugiero capacitar a los empleados de plancha de la sucursal Norte y reorganizar la cocina para que los pedidos salgan más rápido.”
* “Agregaría una persona en la plancha de Norte para los horarios pico y revisaría los procesos de preparación.”

Se entiende la intención, pero al llevarlo a la práctica un gerente real necesitaría muchos detalles adicionales.

### Propuesta vaga o inexistente

Incluso cuando la causa raíz está bien identificada (es decir, hay alguna referencia a la cocina de Norte), la especificidad es prácticamente nula si:

* La solución se reduce a frases casi vacías:

  * “Tomar medidas para mejorar los tiempos.”
  * “Reorganizar el local.”
  * “Hacer cambios internos para optimizar el servicio.”
* O si solo repite el diagnóstico (“el problema es que en Norte tardan más en preparar”) sin ninguna acción concreta.
* O si lo único concreto es algo que en realidad no se puede ejecutar (“que todos trabajen más rápido”) sin explicar cómo.

---

## 3. `solution_realism` (guía de realismo; solo tiene sentido si la causa raíz está bien identificada)

### Acciones razonablemente factibles para un negocio de este tamaño

Se considera realista cuando:

* Las propuestas encajan con un **local de hamburguesas con dos sucursales**, sin requerir inversiones masivas ni decisiones fuera de su control.
* Ejemplos de acciones realistas:

  * Capacitación interna o cruzada entre sucursales.
  * Reasignar tareas entre empleados de Norte (que alguien con experiencia pase a plancha, etc.).
  * Contratar **1 empleado adicional** en plancha o ampliar horarios de alguno, sobre todo en horario pico.
  * Ajustar turnos, poner más personal de plancha en fines de semana.
  * Probar por un tiempo limitado **reducir la cantidad de pedidos** aceptados en Norte en horario pico o aumentar el tiempo estimado de entrega en la app (medida de gestión de la demanda, no estructuralmente imposible).
  * Ofrecer pequeños gestos comerciales (algún descuento puntual o extra en casos de demora) siempre que no sea la única medida.

Es decir, cambios que uno podría imaginar efectivamente implementados por un gerente de este tipo de negocio.

### Propuestas claramente irreales o desproporcionadas

Aunque ataquen la causa raíz, se considera que la solución **no es realista** si:

* Implica decisiones o inversiones desproporcionadas para el tamaño del negocio:

  * “Abrir una planta central de producción para abastecer las sucursales.”
  * “Desarrollar una plataforma propia de envíos con flota de repartidores propia a nivel nacional.”
  * “Reformar completamente el local Norte (obra grande, mudanza de sucursal, etc.) solo por las demoras recientes.”
* Propone cambios que no dependen del negocio:

  * “Cambiar las regulaciones de delivery en la ciudad.”
  * “Obligar a la plataforma a contratar el doble de repartidores” sin ninguna negociación plausible.
* Va contra el sentido común empresarial:

  * “Cerrar definitivamente la sucursal Norte” como solución principal a un problema de demoras de unas semanas.
  * “Ofrecer todos los envíos gratis de por vida” sin ningún análisis de costos.
* Mezcla un número irreal de medidas muy costosas a la vez, sin ningún criterio de prueba o gradualidad.

> Regla práctica: si leyendo la propuesta pensarías “esto sería lindo en un mundo ideal, pero ningún dueño razonable de una hamburguesería mediana podría hacerlo así”, eso indica que el realismo de la solución es muy bajo.

---

Con esta guía:

* La dimensión de causa raíz te dice si la persona entendió *qué* hay que atacar (preparación en Norte / plancha).
* La especificidad describe cuán claro y operable es el *plan de acción*.
* El realismo verifica que ese plan sea compatible con un negocio real de dos sucursales, sin pedirle cosas imposibles o desproporcionadas.

</solution>

</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/rest/detailed_task_facts_rest.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/rest/detailed_task_facts_rest.md`。

### 9. detailed_task_rubric_rest.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>
<diagnostic>
Para esta tarea, el diagnóstico gira en torno a **tres preguntas** del mail de Ramiro. Te detallo, para cada una, qué hechos “clave” debería mencionar una buena respuesta, qué cosas suelen confundir y qué aporta el gráfico.

---

## Pregunta 1

**“¿Podrías revisar si el problema viene de la plataforma de envíos?”**

### Conclusión correcta esperada

La demora **no parece venir principalmente de la plataforma**, sino de la **etapa de preparación en el local de la sucursal Norte**.

### Hechos clave que deberían aparecer (para 2 puntos)

Basado en el cuadro de tiempos promedio:

* **Sucursal Sur**

  * Toma del pedido: **9 min**
  * Preparado en el local: **18 min**
  * Entrega al cliente: **13 min**

* **Sucursal Norte**

  * Toma del pedido: **10 min** (solo 1 minuto más que Sur)
  * Preparado en el local: **29 min** (**11 minutos más** que Sur)
  * Entrega al cliente: **15 min** (2 minutos más que Sur)

Puntos que una buena respuesta debería remarcar:

* La mayor parte de la diferencia en tiempo total (Norte ≈ 54 min vs Sur ≈ 40 min) viene de la etapa **“preparado en el local”**, no de la entrega de la plataforma.
* Ambas sucursales usan la **misma plataforma de envíos**, de modo que si la app fuera el problema, lo lógico sería ver demoras también en Sur.

Con eso, la idea central: *“El problema no parece ser la plataforma, sino cómo se está trabajando dentro del local Norte (tiempo de preparación muy largo)”*.

### Respuestas parciales típicas (1 punto)

* Dicen algo como “no parece ser la plataforma porque la entrega tarda 13 vs 15 minutos” pero **no mencionan** la gran diferencia de 11 minutos en preparación.
* O afirman que el problema está en el local Norte pero sin citar ningún número.

### Confusores / errores graves (0 puntos)

* Culpar directamente a la plataforma (“el problema es la app / los repartidores”) porque los tiempos en Norte son mayores, sin notar que la diferencia grande está en la preparación en el local.
* Atribuir los 29 minutos de preparación a la plataforma, mezclando etapas.
* Comparar mal los datos (por ejemplo, decir que el preparado es más lento en Sur).

---

## Pregunta 2

**“¿Puede ser que la sucursal Norte tenga más pedidos que la sucursal Sur, o que haya habido un mayor aumento…? ¿O no hay diferencias entre sucursales en los pedidos?”**

Se responde mirando el **gráfico de número diario de pedidos**.

### Información clave del gráfico

* Eje X: **fechas** de tres semanas (aprox. 15/01 a 04/02).
* Eje Y: **número de pedidos diarios**.
* Dos líneas: **Norte** (negro) y **Sur** (amarillo).

Patrones visibles:

* Al inicio ambas sucursales rondan los **18–23 pedidos** diarios; a veces Norte está apenas por encima, otras Sur.
* A partir de la segunda semana, los pedidos **suben en ambas sucursales**.
* El aumento es algo mayor en Sur:

  * Norte pasa de ~20 pedidos al inicio a unos **45** al final.
  * Sur pasa de ~20 a alrededor de **55** pedidos diarios al final.
* Desde más o menos el **25/01**, la línea de Sur queda **siempre igual o por encima** de la de Norte; al final hay una brecha de unos 8–10 pedidos a favor de Sur.

### Conclusión correcta esperada (2 puntos)

Algo del estilo:

> “No, la sucursal Norte **no** tiene más pedidos ni un aumento mayor que la Sur. Las dos crecieron, pero Sur termina con más pedidos diarios (≈55 vs ≈45), así que el problema de demoras en Norte no parece explicarse por un volumen de pedidos superior.”

Debe apoyarse en **algún dato concreto** del gráfico (por ejemplo, valores iniciales y finales, o el hecho de que la línea de Sur queda por encima al final).

### Respuestas parciales (1 punto)

* Dicen que los pedidos son “parecidos” y que “en todo caso Sur está un poco por encima”, pero sin números ni mencionar el crecimiento.
* Señalan correctamente que Norte no tiene más pedidos, pero no analizan el aumento relativo.

### Confusores / errores graves (0 puntos)

* Afirmar que “Norte tiene claramente más pedidos que Sur” o que el crecimiento es mucho mayor en Norte (lo contrario de lo que se ve).
* **Invertir las leyendas** (creer que la línea amarilla es Norte) y construir todo el diagnóstico a partir de esa lectura errada.
* Ignorar completamente el gráfico y responder hablando solo de tiempos o de empleados.

---

## Pregunta 3

**“¿Algo más del informe te parece relevante para entender lo que está pasando?”**

Acá hay que integrar la info de tiempos, pedidos y personal para identificar la **causa raíz**.

### Hechos clave que deberían aparecer (para 2 puntos)

1. **Refuerzo del cuello de botella en la preparación en Norte**

   * Recordar que el **tiempo de preparado** es **29 min en Norte vs 18 en Sur** (11 minutos más), mientras que toma del pedido y entrega son similares.
   * Esto encaja con las reseñas de “demoras en el envío”: la demora se genera **antes** de que el pedido pase al repartidor.

2. **Número y experiencia de empleados**

   * Ambas sucursales tienen el **mismo total de empleados: 12 cada una**.
   * **Plancha (clave para la preparación):**

     * Norte: 2 empleados, antigüedad promedio **0,5 meses** (muy nuevos).
     * Sur: 2 empleados, antigüedad promedio **4 meses**.
   * **Ensamblado y limpieza:** en Norte son incluso **más experimentados** (12 y 15 meses) que en Sur (5 y 7 meses).
   * Promedio de antigüedad total: Norte **11,6 meses** vs Sur **6 meses**; es decir, Norte no tiene menos experiencia en general, pero **sí tiene gente muy nueva justamente en plancha**.

   ⇒ Un buen diagnóstico conecta esto con el cuello de botella: la inexperiencia en plancha en Norte podría explicar el tiempo extra de preparación.

3. **Volumen de pedidos no excepcional en Norte**

   * Traer de nuevo la info del gráfico: Norte **no recibe más pedidos** que Sur; al final incluso tiene menos.
   * Por lo tanto, las demoras no parecen deberse a un “desborde” de demanda exclusivo de Norte.

### Cómo se ve una buena respuesta (2 puntos)

Algo así como:

> “Además de los tiempos de entrega, el informe muestra que el tiempo de **preparación en el local Norte es mucho mayor** (29 vs 18 minutos). Ambas sucursales tienen la misma cantidad de empleados, pero en Norte los de **plancha son muy nuevos** (0,5 meses vs 4 meses en Sur), mientras que el resto del equipo es experimentado. Sumado a que Norte **no tiene más pedidos** que Sur, esto sugiere que la causa principal de las demoras son problemas internos de organización/capacitación en la cocina de Norte, especialmente en plancha, más que la plataforma o un exceso de pedidos.”

### Respuestas parciales (1 punto)

* Mencionan **solo uno** de esos elementos (ej. “tiempo de preparación alto” o “empleados de plancha nuevos”) sin conectarlo claramente con el problema.
* O hablan de “problemas organizativos internos” pero casi sin usar datos concretos del informe.

### Confusores / errores graves (0 puntos)

* Decir que “Norte tiene menos empleados” (es falso: las dos tienen 12).
* Afirmar que “en general los empleados de Norte son menos experimentados” (también falso: el promedio de antigüedad es mayor en Norte: 11,6 vs 6 meses).
* Ignorar el tema de tiempos de preparación y enfocarse solo en explicaciones que no aparecen en los datos (marketing, clima, etc.).

---

## En síntesis: información clave del gráfico

* Muestra que **los pedidos aumentan en ambas sucursales** durante tres semanas, desde ~20 pedidos diarios hasta ~45 en Norte y ~55 en Sur.
* **Sur termina con más pedidos y con un aumento algo mayor** que Norte; Norte no está desbordada respecto a Sur.

Esto es central para el diagnóstico: ayuda a **descartar** que el problema de demoras en Norte se deba a que la plataforma esté colapsada por un exceso de pedidos allí, y refuerza la lectura de que el cuello de botella está en la **preparación interna** de la sucursal Norte, probablemente vinculado a la inexperiencia del personal de plancha.
</diagnostic>
<solution>
La idea es que la parte de **solución** esté totalmente alineada con el diagnóstico “correcto” para esta tarea de la hamburguesería. Resumo primero cuál es la **causa raíz esperada**, y después bajo eso a cada subdimensión.

---

## 0. Causa raíz “correcta” en este caso

A partir del informe, la interpretación de referencia es:

* El problema de las bajas reseñas en **Norte** se debe a que los pedidos tardan mucho en estar **listos en el local**, no a la plataforma de envíos.
* En Norte, el tiempo de **preparado en el local** es de **29 minutos vs 18 minutos en Sur** (11 minutos más), mientras que toma del pedido (10 vs 9) y entrega (15 vs 13) son muy parecidos.
* Ambas sucursales tienen el mismo número total de empleados (12), pero en **plancha** los de Norte son muy nuevos (0,5 meses vs 4 meses en Sur), justo en el puesto clave para la preparación.

👉 Entonces, la **causa raíz** que debería atacar la solución es:
**problemas de capacidad/organización en la preparación en el local de la sucursal Norte, especialmente por la inexperiencia del personal de plancha**, más que la plataforma o un exceso de pedidos.

---

## 1. `solution_root_cause` (0–1 punto, con regla de “pasa/no pasa”)

> Regla global: si `solution_root_cause = 0` ⇒ `solution_specificity = 0` y `solution_realism = 0`.

### 1 punto (la solución ataca la causa raíz)

La propuesta incluye **al menos una medida central y explícita** que apunte directamente a:

* Reducir el tiempo de **preparación en el local Norte**, y
* Lo hace focalizando en **plancha / cocina de Norte** (capacitación, organización, dotación de personal, etc.).

Ejemplos de enfoque correcto:

* Capacitar intensivamente a los dos empleados de plancha de Norte, apoyándolos con personal más experimentado.
* Reorganizar el equipo de Norte para que algún empleado experimentado (de ensamblado o limpieza) refuerce plancha en horarios pico.
* Contratar un tercer empleado de plancha para Norte, o trasladar temporalmente a alguien de Sur, con el objetivo explícito de bajar los 29 minutos de preparación.
* Ajustar procesos de cocina en Norte (simplificar pasos, preparar mise en place antes del horario pico, estandarizar tareas) **para reducir el tiempo de preparación**.

También cuenta como “root cause = 1” si la persona propone **reducir o gestionar la demanda de Norte en horario pico** (pausar temporalmente la app, limitar pedidos, alargar el tiempo estimado de entrega en la plataforma) *y* lo vincula claramente con que la capacidad de preparación en Norte es el cuello de botella.

> Criterio práctico: si leyendo la solución se ve que la persona entendió que el problema está en **cómo se preparan los pedidos en Norte (sobre todo plancha)** y propone algo concreto para eso, poné 1 en root_cause.

### 0 puntos (no ataca la causa raíz)

La propuesta se centra en cosas que **no tienen que ver** con la preparación en el local Norte o que son tan vagas que no se sabe qué atacan.

Ejemplos típicos de soluciones con `root_cause = 0`:

* Culpar y cambiar la **plataforma de envíos** (negociar con la app, “cambiar de aplicación”, “contratar más repartidores”) sin mencionar la preparación en el local.
* Hacer solo **marketing / descuentos / responder reseñas** (“mandar cupones”, “hacer publicidad”, “contestar los comentarios explicando la demora”) sin ninguna medida operativa sobre la cocina de Norte.
* Propuestas centradas en la **sucursal Sur** (más empleados en Sur, cambiar procesos en Sur) sin relación con el problema de Norte.
* Explicaciones que dan por sentado que el problema es un **exceso de pedidos en Norte**, contradiciendo el gráfico, y por eso solo quieren “derivar pedidos a Sur” sin hablar de mejorar la preparación.
* Soluciones ultra vagas: “mejorar el servicio”, “organizar mejor el equipo”, “hacer cambios internos” sin decir qué ni dónde.

> Si después de leer la solución uno podría resumirla como “hacer algo con la app / marketing / clientes en general”, sin ninguna acción clara sobre *preparación en Norte*, entonces va `root_cause = 0`.

---

## 2. `solution_specificity` (0–2 puntos, **solo si root_cause = 1**)

### 2 puntos – Propuesta concreta y accionable

Las acciones:

* Están claramente formuladas:

  * **Qué** se va a hacer (ej. capacitar, trasladar gente, contratar, reorganizar procesos).
  * **Dónde** (específicamente en la sucursal Norte, plancha, horarios pico, etc.).
  * Idealmente **quién** o **cómo** (jefe de cocina, empleados de Sur que entrenan, etc.).
  * A veces también **cuándo** o por cuánto tiempo (prueba por 2 semanas, en horarios 20–23 hs, etc.).
* Se conectan explícitamente con el objetivo de **bajar los 29 minutos de preparación en Norte**.

Ejemplos de solución con 2 puntos en especificidad:

* “Durante las próximas dos semanas, trasladar a un empleado experimentado de ensamblado de Norte a plancha en el horario de 20 a 23 hs (viernes y sábados), y que uno de los de limpieza cubra ensamblado. Al mismo tiempo, pedirle al jefe de cocina de Sur que haga dos jornadas de capacitación con los plancheros de Norte para estandarizar el proceso y apuntar a bajar el tiempo de preparación de 29 a menos de 20 minutos.”
* “Contratar un tercer empleado de plancha para Norte solo para fines de semana y noches, y mientras tanto establecer un protocolo de mise en place (tener ingredientes listos antes del horario pico) y controlar diariamente el tiempo promedio de preparación que reporta la plataforma.”

En general, para 2 puntos el lector debería poder **imaginar el plan de acción casi como una mini “checklist”**.

### 1 punto – Idea correcta pero poco detallada

* La solución va **en la dirección correcta** (preparación en Norte / plancha), pero:

  * Dice cosas generales como “capacitar al personal de cocina de Norte”, “reforzar la plancha”, “reorganizar procesos” sin explicar mucho el cómo, cuándo o quién.
  * Puede mencionar una medida correcta (“agregar un empleado en plancha”) pero sin decir si es en Norte, en qué horarios, cómo se financia, etc.
* Hay contenido accionable, pero poco operativo.

Ejemplos:

* “Sugiero capacitar a los empleados de plancha de la sucursal Norte y reorganizar la cocina para que los pedidos salgan más rápido.”
* “Agregaría una persona en la plancha de Norte para los horarios pico y revisaría los procesos de preparación.”

Se entiende la intención, pero al llevarlo a la práctica un gerente real necesitaría muchos detalles adicionales.

### 0 puntos – Propuesta vaga o inexistente

Incluso con `root_cause = 1` (es decir, con alguna referencia a la cocina de Norte), `solution_specificity = 0` si:

* La solución se reduce a frases casi vacías:

  * “Tomar medidas para mejorar los tiempos.”
  * “Reorganizar el local.”
  * “Hacer cambios internos para optimizar el servicio.”
* O si solo repite el diagnóstico (“el problema es que en Norte tardan más en preparar”) sin ninguna acción concreta.
* O si lo único concreto es algo que en realidad no se puede ejecutar (“que todos trabajen más rápido”) sin explicar cómo.

---

## 3. `solution_realism` (0–1 punto, **solo si root_cause = 1**)

### 1 punto – Acciones razonablemente factibles para un negocio de este tamaño

Se considera realista cuando:

* Las propuestas encajan con un **local de hamburguesas con dos sucursales**, sin requerir inversiones masivas ni decisiones fuera de su control.
* Ejemplos de acciones realistas:

  * Capacitación interna o cruzada entre sucursales.
  * Reasignar tareas entre empleados de Norte (que alguien con experiencia pase a plancha, etc.).
  * Contratar **1 empleado adicional** en plancha o ampliar horarios de alguno, sobre todo en horario pico.
  * Ajustar turnos, poner más personal de plancha en fines de semana.
  * Probar por un tiempo limitado **reducir la cantidad de pedidos** aceptados en Norte en horario pico o aumentar el tiempo estimado de entrega en la app (medida de gestión de la demanda, no estructuralmente imposible).
  * Ofrecer pequeños gestos comerciales (algún descuento puntual o extra en casos de demora) siempre que no sea la única medida.

Es decir, cambios que uno podría imaginar efectivamente implementados por un gerente de este tipo de negocio.

### 0 puntos – Propuestas claramente irreales o desproporcionadas

Aunque ataquen la causa raíz, se considera que la solución **no es realista** si:

* Implica decisiones o inversiones desproporcionadas para el tamaño del negocio:

  * “Abrir una planta central de producción para abastecer las sucursales.”
  * “Desarrollar una plataforma propia de envíos con flota de repartidores propia a nivel nacional.”
  * “Reformar completamente el local Norte (obra grande, mudanza de sucursal, etc.) solo por las demoras recientes.”
* Propone cambios que no dependen del negocio:

  * “Cambiar las regulaciones de delivery en la ciudad.”
  * “Obligar a la plataforma a contratar el doble de repartidores” sin ninguna negociación plausible.
* Va contra el sentido común empresarial:

  * “Cerrar definitivamente la sucursal Norte” como solución principal a un problema de demoras de unas semanas.
  * “Ofrecer todos los envíos gratis de por vida” sin ningún análisis de costos.
* Mezcla un número irreal de medidas muy costosas a la vez, sin ningún criterio de prueba o gradualidad.

> Regla práctica: si leyendo la propuesta pensarías “esto sería lindo en un mundo ideal, pero ningún dueño razonable de una hamburguesería mediana podría hacerlo así”, poné `solution_realism = 0`.

---

Con esta rúbrica:

* **root_cause** te dice si la persona entendió *qué* hay que atacar (preparación en Norte / plancha).
* **specificity** mide cuán claro y operable es el *plan de acción*.
* **realism** verifica que ese plan sea compatible con un negocio real de dos sucursales, sin pedirle cosas imposibles o desproporcionadas.

</solution>

</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/rest/detailed_task_rubric_rest.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/rest/detailed_task_rubric_rest.md`。

### 10. detailed_task_facts_sales.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：必要上下文。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>
<diagnostic>

# DIAGNÓSTICO
## diagnosis_q1 – Aires acondicionados en 2024

**Pregunta:** “Para entender si este problema es específico a estos dos productos, ¿te fijarías si en 2024 las ventas de aires acondicionados fueron diferentes a lo normal?”

### Respuestas claramente correctas

La respuesta debe dejar claro que **los aires acondicionados NO muestran un problema nuevo en 2024**:

* Dice explícitamente que **el patrón 2024 de aires es muy similar al de 2023**:

  * ventas altas en verano (ene‑feb y fin de año) y
  * ventas muy bajas en invierno (jun‑jul, alrededor de 40–60 unidades en ambos años).
* Puede mencionar ejemplos: “enero y diciembre rondan las 170–180 unidades, julio cae cerca de 40, igual que el año anterior”.
* Conecta con la pregunta: concluye que **el problema de “estacionalidad rara” parece específico de estufas (y en parte ventiladores), no de aires**.

### Respuestas parcialmente correctas

La idea central es correcta pero pobremente desarrollada:

* Señala que *“los aires siguen vendiéndose más en verano que en invierno”* o *“no se ve un cambio grande en 2024”*, pero:

  * no compara explícitamente 2023 vs 2024, o
  * no menciona meses concretos / rangos de valores, o
  * no cierra con la idea de que el problema es específico de estufas/ventiladores.

### Errores graves / confusores

* Afirma que **los aires también pierden estacionalidad en 2024** o que **tienen una caída/generalización del problema**, cuando el gráfico muestra un patrón muy parecido al de 2023.
* Confunde series: describe el comportamiento de estufas o ventiladores como si fueran aires (por ejemplo, hablar de ventas alrededor de 350–450 unidades como si fueran del aire).
* Ignora el gráfico y responde algo genérico (clima, dólar, etc.) sin decir nada concreto sobre la serie de aires.
* Se queda sólo en copiar el gráfico (“la línea sube y baja”) sin una conclusión sobre si 2024 es normal o no.

---

## diagnosis_q2 – ¿Trabas a la importación?

*(Esta parte no cambia con el nuevo gráfico; depende de la tabla de pedidas/entregadas.)*

**Pregunta:** “Mi asistente mencionó que el año pasado hubo trabas a la importación de ciertos productos electrónicos. ¿Te fijarías si esto podría tener algo que ver?”

### Respuestas claramente correctas

* Usa la **tabla de pedidos y entregas por semestre** y dice algo equivalente a:

  * Para **aires acondicionados** en 2024 hay cierta diferencia entre unidades pedidas y entregadas (se entregan algo menos de las pedidas), lo que sugiere alguna restricción.
  * Para **estufas y ventiladores** las unidades entregadas son prácticamente iguales a las pedidas en todos los semestres 2023–2024.
* Concluye claro que **las trabas a la importación no explican el problema central** (la estacionalidad rara de estufas y ventiladores), porque para esos productos **el proveedor está entregando todo lo que se pide**.
* Puede agregar que los niveles de entrega de estufas y ventiladores en 2024 son muy similares a 2023.

### Respuestas parcialmente correctas

* Llega a la idea general de que **las trabas a la importación no parecen ser la causa principal del problema**, pero:

  * lo argumenta de forma muy general (ej. “se entrega casi todo lo que se pide”) sin detallar por producto, o
  * sólo menciona aires pero igualmente descarta importaciones como causa del problema de estufas/ventiladores.

### Errores graves / confusores

* Dice que **las trabas a la importación explican el problema de estufas y/o ventiladores**, cuando la tabla muestra que se entrega todo lo pedido para esos productos.
* Confunde “pedidas” con “vendidas” o interpreta mal los datos (por ejemplo, ver menos unidades pedidas en un semestre y atribuirlo al importador).
* No responde realmente a la pregunta (no habla de la tabla ni de importaciones).

---

## diagnosis_q3 – ¿Algo más relevante? (causa raíz)

**Pregunta:** “¿Algo más del informe te parece relevante para entender lo que está pasando?”

La idea de fondo sigue siendo: **el cambio en la estrategia de mailings trimestrales es la causa raíz más plausible** del cambio en el patrón de ventas de estufas y ventiladores.

### Respuestas claramente correctas

Para una respuesta claramente correcta, debería:

1. **Usar la información de mailings** (punto 3 del informe) para comparar 2023 vs 2024:

   * 2023:

     * Ventiladores: se promocionan en **Ene–Mar** y **Oct–Dic**.
     * Estufas: se promocionan en **Abr–Jun** y **Jul–Sep** (pleno invierno).
   * 2024:

     * Estufas: sólo aparecen en **Ene–Mar** (desaparecen de los mails justo en los meses fríos).
     * Ventiladores: sólo se promocionan en **Abr–Jun**; **no se los menciona en Oct–Dic 2024**, a diferencia de 2023, y en su lugar se publicita un **caloventor**.
2. **Vincular eso con el gráfico de ventas:**

   * Estufas: en 2023 tienen un gran pico invernal (jun–jul), mientras que en 2024 las ventas se mantienen casi planas todo el año, sin ese pico ⇒ **coincide con que dejaron de promocionarse en invierno**.
   * Ventiladores: en 2023 vuelven a subir fuerte hacia fin de año (dic) y en 2024 no hay ese rebote ⇒ **coincide con que en 2024 se dejan de promocionar antes del verano**.
3. **Conclusión clara:** el cambio en cómo y cuándo se incluyen estufas y ventiladores en los mails parece **explicar la pérdida (total o parcial) de estacionalidad en 2024**; el problema está del lado de marketing/demanda, no de stock/importaciones.

Se puede considerar igualmente correcta tanto una versión que diga “desapareció la estacionalidad” como una que matice: “en 2024 la estacionalidad es mucho menos marcada (estufas casi planas, ventiladores sin pico de fin de año)”.

### Respuestas parcialmente correctas

Menciona la dirección correcta pero de manera incompleta:

* Nota que **cambió la estrategia de mailings** entre 2023 y 2024 (por ejemplo, que se dejaron de promocionar estufas en invierno o ventiladores antes del verano) y que eso “puede explicar” parte del problema, **pero**:

  * no describe bien cómo cambió para ambos productos, o
  * no conecta explícitamente con el patrón del gráfico, o
  * sólo habla en general de “marketing/publicidad” sin usar mucho los datos concretos de los trimestres.

También entra como respuesta parcialmente correcta si:

* Usa bien la tabla de importaciones para descartar esa causa **y sugiere** que el problema debe venir de la forma de promocionar los productos, pero sin entrar en detalle sobre los trimestres.

### Errores graves / confusores

* Ignora por completo la información de mailings y se limita a repetir cosas del gráfico o de importaciones sin ofrecer una causa nueva.
* Asegura que la estrategia de mails **no cambió** o que es “igual” en 2023 y 2024, cuando la tabla muestra diferencias claras (estufas desaparecen del invierno 2024; ventiladores desaparecen del fin de año 2024).
* Confunde productos (por ejemplo, decir que la estufa portátil se siguió promocionando en invierno 2024 o que los ventiladores están en el mail de Oct–Dic 2024).
* Atribuye la causa principal a factores no mencionados en el informe (competencia, clima, tipo de cambio) sin apoyarse en los datos dados.


</diagnostic>
<solution>

# SOLUCIÓN

## 1. solution_root_cause (regla de “pasa/no pasa”)

### ¿Cuál es la causa raíz en esta tarea?

Según los datos:

* **Aires acondicionados**: 2024 se ve “normal”, con fuerte estacionalidad verano–invierno similar a 2023.
* **Estufas**: en 2023 tienen un pico invernal muy marcado; en 2024 se mantienen casi planas durante todo el año.
* **Ventiladores**: en 2023 se ve un patrón claramente veraniego; en 2024 la estacionalidad es mucho menos clara.
* El proveedor **entrega prácticamente todo lo pedido** de estufas y ventiladores en 2023 y 2024.
* Lo que **sí cambia fuerte** en 2024 es la **estrategia de mailings** trimestrales:

  * 2023: se promocionan estufas en los trimestres fríos y ventiladores en los cálidos.
  * 2024: estufas desaparecen de los mails en invierno; ventiladores ya no se promocionan antes del verano y se prioriza un producto sustituto (caloventor).

**Causa raíz “correcta”**: el problema está en **cómo y cuándo se promocionan estufas y ventiladores (marketing, en particular los mails estacionales)**, no en importaciones ni en un problema general de la categoría.

### Respuestas que sí atacan la causa raíz

Considerá que en la parte de solución la propuesta **apunta claramente a corregir esa falla de promoción estacional de estufas y ventiladores** cuando propone cosas como:

* “Volver a incluir **estufas** en los mails de **Abr–Jun y Jul–Sep** y **ventiladores** en los de **Ene–Mar y Oct–Dic**.”
* “Reordenar el calendario de campañas para que **estufas y ventiladores sean protagonistas en los meses de frío/calor**.”
* “Diseñar campañas específicas (descuentos, combos, destacados en web y mails) para estufas en invierno y ventiladores en verano.”
* “Dejar de canibalizar estufas con el caloventor en Oct–Dic y darle más visibilidad a ventiladores y aires en esa época.”

No hace falta que mencione la palabra “causa raíz”, pero **la acción principal** tiene que ser: *cambiar la estrategia de marketing / mailings para estufas y ventiladores en las temporadas adecuadas*, coherente con lo que detectó en el diagnóstico.

También puede incluir otras ideas accesorias (revisar precios, stock, UX de la web), siempre que **la pieza central** sea arreglar la promoción estacional de esos productos.

### Respuestas que no atacan la causa raíz

La solución **no se enfoca en ese problema de marketing estacional**. Ejemplos:

* Centra toda la solución en **importaciones/stock**:

  * “Negociar con el importador para que nos entregue más estufas y ventiladores.”
  * “Buscar nuevos proveedores para evitar las trabas a la importación.”
* Propone soluciones **operativas o de producto** sin relación con la evidencia:

  * “Mejorar el tiempo de entrega / logística”, “abrir locales físicos”, “ampliar la variedad de productos”, etc.
* Propone **marketing genérico** sin conectar con la estacionalidad ni con estufas/ventiladores:

  * “Invertir más en publicidad”, “hacer más campañas en redes” sin mencionar que hay que **volver a promocionar específicamente estufas en invierno y ventiladores en verano**.
* La respuesta es tan vaga que no se entiende qué causa del problema está atacando.

Ante la duda: si un corrector tuviera que responder “¿esta propuesta arreglaría el problema que vemos en el gráfico y en los mails?”, y la respuesta honesta es “probablemente no” o “no se sabe”, entonces la solución no está atacando la causa raíz.

---

## 2. solution_specificity (guía de especificidad; solo tiene sentido si la causa raíz está bien identificada)

> Estas consideraciones son útiles cuando la propuesta ya apunta a la causa raíz; de lo contrario, hablar de “detalle” o “realismo” de la solución tiene poco sentido.

Acá se describe **cuán concreta y accionable** es la propuesta para corregir la estrategia de promoción.

### Propuesta concreta y accionable

La respuesta describe **acciones específicas** sobre el marketing estacional de estufas y ventiladores, con cierto nivel de detalle de **qué, cómo, cuándo y/o quién**. Por ejemplo:

* Define **productos y momentos**:

  * “En el próximo mail de **Abr–Jun** destacar estufas con un banner principal y un 10% de descuento.”
  * “En **Jul–Sep** repetir estufas y sumar combos ‘estufa + caloventor’.”
  * “En **Ene–Mar y Oct–Dic** incluir ventiladores en la primera sección del mail y en la home de la web.”
* Describe **canales y formato**:

  * “Actualizar las plantillas de newsletter para que siempre haya una sección fija de ‘climatización’ donde alternemos estufas y ventiladores según la temporada.”
  * “Crear campañas específicas de remarketing para clientes que compraron en años previos productos de calefacción o ventilación.”
* Incluye **implementación mínima**:

  * “Definir el calendario de campañas del año antes de fin de mes.”
  * “Responsable: equipo de marketing/CRM; usar datos históricos de ventas para fijar las semanas de envío.”
  * “Medir resultados comparando las ventas de estufas/ventiladores con el mismo trimestre del año anterior.”

En resumen: si alguien de la empresa pudiera leer la solución y **saber qué tareas concretas tiene que hacer la semana que viene**, estamos frente a una propuesta muy específica y accionable.

### Idea correcta pero poco detallada

La propuesta va en la dirección adecuada (corregir la promoción estacional de estufas y ventiladores) pero queda en un nivel más general. Ejemplos:

* “Hay que **volver a promocionar estufas en invierno y ventiladores en verano** en los mails.”
* “Reforzar las campañas de marketing para estos productos en los meses donde deberían venderse más.”
* “Asegurarnos de que en cada newsletter haya al menos un producto de calefacción en los meses fríos y uno de ventilación en los meses calurosos.”

No dice **qué descuentos**, ni **qué formato de mail**, ni **qué trimestres concretos**, ni quién lo hace o cuándo. Se entiende la idea, pero habría que trabajarla bastante para implementarla.

### Nada específico (cuando la causa raíz está bien identificada)

La especificidad es muy baja cuando:

* La solución es extremadamente vaga:

  * “Mejorar el marketing de estufas y ventiladores.”
  * “Hacer más promociones” sin nada más.
* O se limita a frases tipo “hay que hacer un plan de marketing” sin ningún ejemplo o indicación concreta de qué cambiar en mails/calendario/campañas.

De nuevo: si el texto no te permite listar ni una tarea accionable clara, la propuesta carece de contenido específico.

---

## 3. solution_realism (guía de realismo; solo tiene sentido si la causa raíz está bien identificada)

Evalúa si, para un negocio online de electrodomésticos como el del caso, las acciones propuestas parecen **factibles y razonables**, sin requerir cambios desproporcionados.

### Propuestas realistas

Se consideran realistas las estrategias que implican cosas como:

* Cambiar el **contenido y calendario de los mails** (qué productos se incluyen en cada trimestre).
* Ajustar la **prioridad de estufas/ventiladores en los newsletters y en la web**.
* Ofrecer **descuentos moderados**, combos, envío gratis en ciertos períodos para estos productos.
* Reorientar parte del **presupuesto de marketing digital** hacia campañas específicas para estufas y ventiladores.
* Hacer una **prueba piloto** en el próximo trimestre y luego escalar si funciona.

En general, todo lo que suene a decisiones normales de un área de marketing/ventas de un e‑commerce mediano entra como realista.

### Claramente irreal / desproporcionado

Las propuestas, aun cuando apunten a la causa correcta, se vuelven **exageradas o poco creíbles** para este contexto cuando, por ejemplo:

* Propuestas que dependen de **cambios macro o regulatorios**:

  * “Presionar al gobierno para que elimine las trabas a la importación.” (además estaría mal en root_cause).
* Inversiones gigantes o fuera de escala:

  * “Lanzar una campaña masiva en TV nacional todo el año para estos productos” sin ninguna mención a limitaciones de presupuesto.
  * “Abrir varias cadenas de locales físicos especializados sólo en estufas y ventiladores.”
* Medidas que implican **reestructuraciones enormes** del negocio para un problema puntual:

  * “Cambiar todo el modelo de negocio hacia venta mayorista internacional”, etc.

Si el lector razonable piensa “esto nunca lo haría esta empresa para este problema concreto”, eso indica que el realismo de la solución es muy bajo.

---
Recordatorio conceptual de la **regla dura**:

> Si la solución no ataca la causa raíz, la especificidad y el realismo de cualquier otra acción pierden relevancia, por más “linda” que parezca la propuesta.

---
</solution>
</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/sales/detailed_task_facts_sales.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/sales/detailed_task_facts_sales.md`。

### 11. detailed_task_rubric_sales.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
<rubrica_especifica_a_la_tarea_asignada>
<diagnostic>

# DIAGNÓSTICO
## diagnosis_q1 – Aires acondicionados en 2024

**Pregunta:** “Para entender si este problema es específico a estos dos productos, ¿te fijarías si en 2024 las ventas de aires acondicionados fueron diferentes a lo normal?”

### 2 puntos

La respuesta debe dejar claro que **los aires acondicionados NO muestran un problema nuevo en 2024**:

* Dice explícitamente que **el patrón 2024 de aires es muy similar al de 2023**:

  * ventas altas en verano (ene‑feb y fin de año) y
  * ventas muy bajas en invierno (jun‑jul, alrededor de 40–60 unidades en ambos años).
* Puede mencionar ejemplos: “enero y diciembre rondan las 170–180 unidades, julio cae cerca de 40, igual que el año anterior”.
* Conecta con la pregunta: concluye que **el problema de “estacionalidad rara” parece específico de estufas (y en parte ventiladores), no de aires**.

### 1 punto

La idea central es correcta pero pobremente desarrollada:

* Señala que *“los aires siguen vendiéndose más en verano que en invierno”* o *“no se ve un cambio grande en 2024”*, pero:

  * no compara explícitamente 2023 vs 2024, o
  * no menciona meses concretos / rangos de valores, o
  * no cierra con la idea de que el problema es específico de estufas/ventiladores.

### 0 puntos (errores graves / confusores)

* Afirma que **los aires también pierden estacionalidad en 2024** o que **tienen una caída/generalización del problema**, cuando el gráfico muestra un patrón muy parecido al de 2023.
* Confunde series: describe el comportamiento de estufas o ventiladores como si fueran aires (por ejemplo, hablar de ventas alrededor de 350–450 unidades como si fueran del aire).
* Ignora el gráfico y responde algo genérico (clima, dólar, etc.) sin decir nada concreto sobre la serie de aires.
* Se queda sólo en copiar el gráfico (“la línea sube y baja”) sin una conclusión sobre si 2024 es normal o no.

---

## diagnosis_q2 – ¿Trabas a la importación?

*(Esta parte no cambia con el nuevo gráfico; depende de la tabla de pedidas/entregadas.)*

**Pregunta:** “Mi asistente mencionó que el año pasado hubo trabas a la importación de ciertos productos electrónicos. ¿Te fijarías si esto podría tener algo que ver?”

### 2 puntos

* Usa la **tabla de pedidos y entregas por semestre** y dice algo equivalente a:

  * Para **aires acondicionados** en 2024 hay cierta diferencia entre unidades pedidas y entregadas (se entregan algo menos de las pedidas), lo que sugiere alguna restricción.
  * Para **estufas y ventiladores** las unidades entregadas son prácticamente iguales a las pedidas en todos los semestres 2023–2024.
* Concluye claro que **las trabas a la importación no explican el problema central** (la estacionalidad rara de estufas y ventiladores), porque para esos productos **el proveedor está entregando todo lo que se pide**.
* Puede agregar que los niveles de entrega de estufas y ventiladores en 2024 son muy similares a 2023.

### 1 punto

* Llega a la idea general de que **las trabas a la importación no parecen ser la causa principal del problema**, pero:

  * lo argumenta de forma muy general (ej. “se entrega casi todo lo que se pide”) sin detallar por producto, o
  * sólo menciona aires pero igualmente descarta importaciones como causa del problema de estufas/ventiladores.

### 0 puntos

* Dice que **las trabas a la importación explican el problema de estufas y/o ventiladores**, cuando la tabla muestra que se entrega todo lo pedido para esos productos.
* Confunde “pedidas” con “vendidas” o interpreta mal los datos (por ejemplo, ver menos unidades pedidas en un semestre y atribuirlo al importador).
* No responde realmente a la pregunta (no habla de la tabla ni de importaciones).

---

## diagnosis_q3 – ¿Algo más relevante? (causa raíz)

**Pregunta:** “¿Algo más del informe te parece relevante para entender lo que está pasando?”

La idea de fondo sigue siendo: **el cambio en la estrategia de mailings trimestrales es la causa raíz más plausible** del cambio en el patrón de ventas de estufas y ventiladores.

### 2 puntos

Para 2 puntos la respuesta debería:

1. **Usar la información de mailings** (punto 3 del informe) para comparar 2023 vs 2024:

   * 2023:

     * Ventiladores: se promocionan en **Ene–Mar** y **Oct–Dic**.
     * Estufas: se promocionan en **Abr–Jun** y **Jul–Sep** (pleno invierno).
   * 2024:

     * Estufas: sólo aparecen en **Ene–Mar** (desaparecen de los mails justo en los meses fríos).
     * Ventiladores: sólo se promocionan en **Abr–Jun**; **no se los menciona en Oct–Dic 2024**, a diferencia de 2023, y en su lugar se publicita un **caloventor**.
2. **Vincular eso con el gráfico de ventas:**

   * Estufas: en 2023 tienen un gran pico invernal (jun–jul), mientras que en 2024 las ventas se mantienen casi planas todo el año, sin ese pico ⇒ **coincide con que dejaron de promocionarse en invierno**.
   * Ventiladores: en 2023 vuelven a subir fuerte hacia fin de año (dic) y en 2024 no hay ese rebote ⇒ **coincide con que en 2024 se dejan de promocionar antes del verano**.
3. **Conclusión clara:** el cambio en cómo y cuándo se incluyen estufas y ventiladores en los mails parece **explicar la pérdida (total o parcial) de estacionalidad en 2024**; el problema está del lado de marketing/demanda, no de stock/importaciones.

Se puede aceptar como 2 puntos tanto una versión que diga “desapareció la estacionalidad” como una que matice: “en 2024 la estacionalidad es mucho menos marcada (estufas casi planas, ventiladores sin pico de fin de año)”.

### 1 punto

Menciona la dirección correcta pero de manera incompleta:

* Nota que **cambió la estrategia de mailings** entre 2023 y 2024 (por ejemplo, que se dejaron de promocionar estufas en invierno o ventiladores antes del verano) y que eso “puede explicar” parte del problema, **pero**:

  * no describe bien cómo cambió para ambos productos, o
  * no conecta explícitamente con el patrón del gráfico, o
  * sólo habla en general de “marketing/publicidad” sin usar mucho los datos concretos de los trimestres.

También puede ser 1 punto si:

* Usa bien la tabla de importaciones para descartar esa causa **y sugiere** que el problema debe venir de la forma de promocionar los productos, pero sin entrar en detalle sobre los trimestres.

### 0 puntos

* Ignora por completo la información de mailings y se limita a repetir cosas del gráfico o de importaciones sin ofrecer una causa nueva.
* Asegura que la estrategia de mails **no cambió** o que es “igual” en 2023 y 2024, cuando la tabla muestra diferencias claras (estufas desaparecen del invierno 2024; ventiladores desaparecen del fin de año 2024).
* Confunde productos (por ejemplo, decir que la estufa portátil se siguió promocionando en invierno 2024 o que los ventiladores están en el mail de Oct–Dic 2024).
* Atribuye la causa principal a factores no mencionados en el informe (competencia, clima, tipo de cambio) sin apoyarse en los datos dados.


</diagnostic>
<solution>

# SOLUCIÓN

## 1. solution_root_cause (0–1 punto)

### ¿Cuál es la causa raíz en esta tarea?

Según los datos:

* **Aires acondicionados**: 2024 se ve “normal”, con fuerte estacionalidad verano–invierno similar a 2023.
* **Estufas**: en 2023 tienen un pico invernal muy marcado; en 2024 se mantienen casi planas durante todo el año.
* **Ventiladores**: en 2023 se ve un patrón claramente veraniego; en 2024 la estacionalidad es mucho menos clara.
* El proveedor **entrega prácticamente todo lo pedido** de estufas y ventiladores en 2023 y 2024.
* Lo que **sí cambia fuerte** en 2024 es la **estrategia de mailings** trimestrales:

  * 2023: se promocionan estufas en los trimestres fríos y ventiladores en los cálidos.
  * 2024: estufas desaparecen de los mails en invierno; ventiladores ya no se promocionan antes del verano y se prioriza un producto sustituto (caloventor).

**Causa raíz “correcta”**: el problema está en **cómo y cuándo se promocionan estufas y ventiladores (marketing, en particular los mails estacionales)**, no en importaciones ni en un problema general de la categoría.

### 1 punto – Sí ataca la causa raíz

Dar 1 si, en la parte de solución, la propuesta **apunta claramente a corregir esa falla de promoción estacional de estufas y ventiladores**. Por ejemplo, que proponga cosas como:

* “Volver a incluir **estufas** en los mails de **Abr–Jun y Jul–Sep** y **ventiladores** en los de **Ene–Mar y Oct–Dic**.”
* “Reordenar el calendario de campañas para que **estufas y ventiladores sean protagonistas en los meses de frío/calor**.”
* “Diseñar campañas específicas (descuentos, combos, destacados en web y mails) para estufas en invierno y ventiladores en verano.”
* “Dejar de canibalizar estufas con el caloventor en Oct–Dic y darle más visibilidad a ventiladores y aires en esa época.”

No hace falta que mencione la palabra “causa raíz”, pero **la acción principal** tiene que ser: *cambiar la estrategia de marketing / mailings para estufas y ventiladores en las temporadas adecuadas*, coherente con lo que detectó en el diagnóstico.

Se puede aceptar 1 punto aunque incluya otras ideas accesorias (revisar precios, stock, UX de la web), siempre que **la pieza central** sea arreglar la promoción estacional de esos productos.

### 0 puntos – No ataca la causa raíz

Poner 0 si la solución **no se enfoca en ese problema de marketing estacional**. Ejemplos:

* Centra toda la solución en **importaciones/stock**:

  * “Negociar con el importador para que nos entregue más estufas y ventiladores.”
  * “Buscar nuevos proveedores para evitar las trabas a la importación.”
* Propone soluciones **operativas o de producto** sin relación con la evidencia:

  * “Mejorar el tiempo de entrega / logística”, “abrir locales físicos”, “ampliar la variedad de productos”, etc.
* Propone **marketing genérico** sin conectar con la estacionalidad ni con estufas/ventiladores:

  * “Invertir más en publicidad”, “hacer más campañas en redes” sin mencionar que hay que **volver a promocionar específicamente estufas en invierno y ventiladores en verano**.
* La respuesta es tan vaga que no se entiende qué causa del problema está atacando.

Ante la duda: si un corrector tuviera que responder “¿esta propuesta arreglaría el problema que vemos en el gráfico y en los mails?”, y la respuesta honesta es “probablemente no” o “no se sabe”, entonces `solution_root_cause = 0`.

---

## 2. solution_specificity (0–2 puntos)

> **Solo se aplica si `solution_root_cause = 1`.**
> Si root_cause=0, acá va automáticamente 0.

Acá evaluás **cuán concreta y accionable** es la propuesta para corregir la estrategia de promoción.

### 2 puntos – Propuesta concreta y accionable

La respuesta describe **acciones específicas** sobre el marketing estacional de estufas y ventiladores, con cierto nivel de detalle de **qué, cómo, cuándo y/o quién**. Por ejemplo:

* Define **productos y momentos**:

  * “En el próximo mail de **Abr–Jun** destacar estufas con un banner principal y un 10% de descuento.”
  * “En **Jul–Sep** repetir estufas y sumar combos ‘estufa + caloventor’.”
  * “En **Ene–Mar y Oct–Dic** incluir ventiladores en la primera sección del mail y en la home de la web.”
* Describe **canales y formato**:

  * “Actualizar las plantillas de newsletter para que siempre haya una sección fija de ‘climatización’ donde alternemos estufas y ventiladores según la temporada.”
  * “Crear campañas específicas de remarketing para clientes que compraron en años previos productos de calefacción o ventilación.”
* Incluye **implementación mínima**:

  * “Definir el calendario de campañas del año antes de fin de mes.”
  * “Responsable: equipo de marketing/CRM; usar datos históricos de ventas para fijar las semanas de envío.”
  * “Medir resultados comparando las ventas de estufas/ventiladores con el mismo trimestre del año anterior.”

En resumen: si alguien de la empresa pudiera leer la solución y **saber qué tareas concretas tiene que hacer la semana que viene**, es un 2.

### 1 punto – Idea correcta pero poco detallada

La propuesta va en la dirección adecuada (corregir la promoción estacional de estufas y ventiladores) pero queda en un nivel más general. Ejemplos:

* “Hay que **volver a promocionar estufas en invierno y ventiladores en verano** en los mails.”
* “Reforzar las campañas de marketing para estos productos en los meses donde deberían venderse más.”
* “Asegurarnos de que en cada newsletter haya al menos un producto de calefacción en los meses fríos y uno de ventilación en los meses calurosos.”

No dice **qué descuentos**, ni **qué formato de mail**, ni **qué trimestres concretos**, ni quién lo hace o cuándo. Se entiende la idea, pero habría que trabajarla bastante para implementarla.

### 0 puntos – Nada específico (si root_cause=1)

Dar 0 en specificity (manteniendo root_cause=1) cuando:

* La solución es extremadamente vaga:

  * “Mejorar el marketing de estufas y ventiladores.”
  * “Hacer más promociones” sin nada más.
* O se limita a frases tipo “hay que hacer un plan de marketing” sin ningún ejemplo o indicación concreta de qué cambiar en mails/calendario/campañas.

De nuevo: si el texto no te permite listar ni una tarea accionable clara, es un 0.

---

## 3. solution_realism (0–1 punto)

> También **solo se aplica si `solution_root_cause = 1`**.
> Si root_cause=0 ⇒ realism=0.

Evalúa si, para un negocio online de electrodomésticos como el del caso, las acciones propuestas parecen **factibles y razonables**, sin requerir cambios desproporcionados.

### 1 punto – Realista

Dar 1 si la estrategia propuesta implica cosas como:

* Cambiar el **contenido y calendario de los mails** (qué productos se incluyen en cada trimestre).
* Ajustar la **prioridad de estufas/ventiladores en los newsletters y en la web**.
* Ofrecer **descuentos moderados**, combos, envío gratis en ciertos períodos para estos productos.
* Reorientar parte del **presupuesto de marketing digital** hacia campañas específicas para estufas y ventiladores.
* Hacer una **prueba piloto** en el próximo trimestre y luego escalar si funciona.

En general, todo lo que suene a decisiones normales de un área de marketing/ventas de un e‑commerce mediano entra como realista.

### 0 puntos – Claramente irreal / desproporcionado

Poner 0 si, aun cuando la acción apunte a la causa correcta, la forma de implementarla es **exagerada o poco creíble** para este contexto. Ejemplos:

* Propuestas que dependen de **cambios macro o regulatorios**:

  * “Presionar al gobierno para que elimine las trabas a la importación.” (además estaría mal en root_cause).
* Inversiones gigantes o fuera de escala:

  * “Lanzar una campaña masiva en TV nacional todo el año para estos productos” sin ninguna mención a limitaciones de presupuesto.
  * “Abrir varias cadenas de locales físicos especializados sólo en estufas y ventiladores.”
* Medidas que implican **reestructuraciones enormes** del negocio para un problema puntual:

  * “Cambiar todo el modelo de negocio hacia venta mayorista internacional”, etc.

Si el lector razonable piensa “esto nunca lo haría esta empresa para este problema concreto”, entonces realism=0.

---
Recordatorio de la **regla dura**:

> Si `solution_root_cause = 0` ⇒ `solution_specificity = 0` y `solution_realism = 0`.
> Aunque la persona escriba cosas “lindas”, si no ataca la causa raíz no suma nada en la sección solución.

---
</solution>
</rubrica_especifica_a_la_tarea_asignada>
```

原檔：`upstream/ai_grading/independent-researcher/strategy-2/task-materials/sales/detailed_task_rubric_sales.md`。來源定位：`ai_grading/independent-researcher/strategy-2/task-materials/sales/detailed_task_rubric_sales.md`。

### 12. elo_prompt.md

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```text
Sos un corrector experto de respuestas escritas en español rioplatense. Tu tarea es COMPARAR varias respuestas al MISMO ejercicio y ordenarlas de mejor a peor desempeño, según la rúbrica pre-registrada del experimento.

IMPORTANTE:
- No vas a asignar puntajes numéricos.
- Solo vas a producir un ORDEN ESTRICTO (sin empates) de los IDs de las respuestas.
- Ese orden debe reflejar, lo mejor posible, el resultado final que obtendrías si aplicaras cuidadosamente la rúbrica pre-registrada (contenido y escritura) a cada respuesta.

------------------------------------------------------------
CONTEXTO Y FORMATO DE ENTRADA
------------------------------------------------------------

En el mensaje de usuario vas a recibir:

1) La consigna de la tarea (correo del jefe/jefa + descripción del negocio).
2) El informe adjunto (tablas, descripciones, etc.).
3) Un grupo de ~12 respuestas de participantes, en pseudo-XML, con este formato:

<ANSWERS>
  <ANSWER id="RESP-123">
    [texto completo de la respuesta del participante 123]
  </ANSWER>
  <ANSWER id="RESP-456">
    [texto completo de la respuesta del participante 456]
  </ANSWER>
  ...
</ANSWERS>

- Cada etiqueta <ANSWER> tiene un atributo id que identifica de manera única a la respuesta (puede parecerse a un UUID, pero no importa su formato).
- No modifiques los IDs ni inventes otros nuevos.
- Todas las respuestas corresponden a la MISMA tarea; solo difieren en el texto del participante.

------------------------------------------------------------
CRITERIO DE EVALUACIÓN (basado en la rúbrica pre-registrada)
------------------------------------------------------------

El experimento define una rúbrica con dos dimensiones principales:

1. CONTENIDO (0–10 puntos conceptuales):
   - DIAGNÓSTICO (6 puntos): hasta 2 puntos por cada una de las 3 preguntas del jefe/jefa.
   - SOLUCIÓN (4 puntos):
     - 1 punto: aborda la causa raíz del problema.
     - 0–2 puntos: propuesta concreta y específica.
     - 0–1 punto: realismo.
     - Regla de pasa/no pasa: si la solución NO aborda la causa raíz, la persona obtiene 0 en la sección de solución, sin importar cuán detallada parezca.

2. ESCRITURA (0–10 puntos conceptuales):
   - Ortografía y gramática (2)
   - Claridad y legibilidad (3)
   - Organización (4)
   - Tono y registro (1)

El resultado principal del experimento es:
- Puntaje global = (2/3) * contenido + (1/3) * escritura.
- Además se construye un indicador binario “identificó la causa raíz” si tiene al menos 1 punto en la tercera pregunta de diagnóstico.

Tu tarea en esta etapa de ranking es:

> Imaginar qué puntaje global (0–10) obtendría cada respuesta si aplicaras en detalle esa rúbrica, donde el contenido tiene más peso que la escritura (2/3 vs 1/3), y dentro del contenido el diagnóstico y la solución se ponderan según el esquema anterior. NO calcules ni devuelvas los puntajes, pero usalos mentalmente para COMPARAR RESPUESTAS.

En otras palabras, debés ordenar las respuestas de mejor a peor desempeño EN TÉRMINOS DEL PUNTAJE GLOBAL IMPLÍCITO que recibirían bajo la rúbrica pre-registrada.

Guía práctica para comparar:

- Priorizá primero el CONTENIDO:
  - Qué tan bien responden las 3 preguntas específicas del jefe/jefa usando el informe.
  - Si identifican la causa raíz correcta y si la solución realmente la ataca.
  - Qué tan concreta y realista es la propuesta de solución.
- Luego, entre respuestas similares en contenido, usá la ESCRITURA como desempate:
  - Ortografía/gramática.
  - Claridad y facilidad de lectura.
  - Organización del mail (saludo, cuerpo, cierre; orden de ideas).
  - Tono respetuoso y profesional.

También considerá que el experimento penaliza fuertemente respuestas muy cortas: si una respuesta es brevísima y casi no desarrolla diagnóstico ni solución, debería quedar muy abajo en el ranking, incluso si la escritura es prolija.

------------------------------------------------------------
INSTRUCCIONES PARA EL ORDENAMIENTO
------------------------------------------------------------

1. Leé todas las respuestas del grupo, prestando atención a:
   - Qué tan bien responden a las tres preguntas diagnósticas usando los datos del informe.
   - Qué tan buena es la propuesta de solución, especialmente si ataca la causa raíz.
   - Qué tan clara, ordenada y profesional es la escritura.

2. Construí un orden total de los IDs de respuesta:
   - El PRIMER elemento del ranking es la mejor respuesta del grupo según la rúbrica.
   - El ÚLTIMO elemento del ranking es la peor respuesta del grupo.
   - NO SE PERMITEN EMPATES. Aunque dos respuestas parezcan muy similares, rompé el empate usando pequeños detalles (uso de datos, claridad, organización, tono, etc.).

3. Revisá:
   - Que cada ID que aparece en <ANSWER id="..."> esté incluido EXACTAMENTE UNA VEZ en el arreglo de ranking.
   - Que no falte ningún ID y que no haya duplicados.

------------------------------------------------------------
SALIDA (MUY IMPORTANTE)
------------------------------------------------------------

Debés devolver **EXCLUSIVAMENTE** un objeto JSON que cumpla con el schema que te pasa la herramienta. NO agregues explicaciones fuera del JSON.

Campos esperados:

- "criterion": Un string que identifique el criterio de ranking utilizado. Por defecto usá "overall" para indicar que ordenaste según el puntaje global implícito (2/3 contenido, 1/3 escritura).
- "ranking": Arreglo de IDs de respuesta, de mejor a peor.
- "rationales": Objeto opcional con comentarios breves, donde cada clave es un ID de respuesta y el valor es una breve explicación en español del por qué esa respuesta queda aproximadamente en esa zona del ranking (puede ser más detallado para las mejores y peores).

Ejemplo conceptual (NO lo copies literalmente, solo es para ilustrar la forma):

{
  "criterion": "overall",
  "ranking": ["RESP-123", "RESP-456", "RESP-789"],
  "rationales": {
    "RESP-123": "Muy buen diagnóstico, solución concreta que ataca la causa raíz, escritura clara.",
    "RESP-456": "Diagnóstico correcto pero solución algo vaga; escritura razonable.",
    "RESP-789": "No responde bien a las preguntas y casi no propone solución; varias partes confusas."
  }
}

Recordá: el objetivo es un ORDEN ESTRICTO DE IDs, bien razonado según la rúbrica pre-registrada, para usar luego en un sistema de ranking estadístico (Elo / Bradley–Terry). No generes puntajes numéricos.
```

原檔：`upstream/ai_grading/independent-researcher/strategy-3/elo_prompt.md`。來源定位：`ai_grading/independent-researcher/strategy-3/elo_prompt.md`。

### 13. elo_schema.yml

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：輸出格式。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```yaml
type: object
description: >
  Ranking de varias respuestas a la misma tarea, ordenadas de mejor a peor
  según la rúbrica pre-registrada (contenido y escritura) y el criterio indicado.
properties:
  criterion:
    type: string
    description: >
      Criterio utilizado para el ranking (por ejemplo: "overall", "content", "writing").
      Por defecto se espera "overall", es decir, el puntaje global implícito
      basado en 2/3 contenido y 1/3 escritura según la rúbrica del experimento.
  ranking:
    type: array
    description: >
      Lista de IDs de respuestas, ordenadas de MEJOR a PEOR según el criterio.
      Debe incluir exactamente una vez cada id presente en las etiquetas <ANSWER id="...">
      del pseudo-XML de entrada. No se permiten empates.
    items:
      type: string
  rationales:
    type: object
    description: >
      Comentarios breves y opcionales que justifican el orden. Cada clave debe ser
      un ID de respuesta (exactamente igual al atributo id en el pseudo-XML) y
      el valor un texto breve en español con una explicación de por qué esa respuesta
      se ubica aproximadamente en esa posición del ranking.
    additionalProperties:
      type: string

required:
  - criterion
  - ranking
```

原檔：`upstream/ai_grading/independent-researcher/strategy-3/elo_schema.yml`。來源定位：`ai_grading/independent-researcher/strategy-3/elo_schema.yml`。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/abs/2608.04198v1) · [官方程式固定版本](https://github.com/ramirogalvez/ai-skill-gap-experiment-data/tree/c144fe68de350b810ac275bd6d6df8219db47fc0) · [逐檔來源與授權](../../sources.json)
