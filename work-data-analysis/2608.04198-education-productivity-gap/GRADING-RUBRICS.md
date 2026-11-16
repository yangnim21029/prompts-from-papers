# 主要評分流程的六份 JSON 量表

本頁屬於 *Does generative AI narrow education-based productivity gaps? Evidence from a randomized experiment* 的完整補充材料。保留固定版本原文，與論文實驗版本的關係見[研究與核心模板](README.md)。

主流程評分 prompt 搭配相應 task/followup JSON；獨立研究者策略 1–3 為替代評分流程，不應全部連用。facts、rubric 與 schema 為必要上下文。

### 1. lunch_fup_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{
  "follow_up_question": [
    {
      "question": "¿Me contarías brevemente por qué es que estamos vendiendo menos almuerzos en la sede Norte?",
      "correct_answer": "Sí. La sede Norte tiene una mayor proporción de empleados del área de administración, mientras que la sede Sur tiene una mayor proporción del área de ventas. Los empleados de administración tienen permitido trabajar desde su casa los viernes, mientras que los de ventas deben asistir presencialmente de lunes a viernes. La explicación más probable para la diferencia de ventas entre sedes los días viernes es que la sede Norte tiene más empleados de administración, y estos se quedan trabajando desde su casa los viernes."
    }
  ],
  "content_rubric": [
    {
      "score": 0,
      "description": "La respuesta es incorrecta: no identifica el mecanismo causal correcto que genera el problema, y/o introduce explicaciones irrelevantes o equivocadas.",
      "example1": "Sí, las diferencias en las ventas entre ambas sedes probablemente se deban a la composición del personal. Es probable que los empleados de administración, que tienen mayor presencia en la sede Norte, perciban ingresos más bajos que los empleados de ventas, lo que podría explicar el menor nivel de ventas en esa sede.",
      "explanation1": "No identifica el mecanismo correcto: no menciona el home office ni que el problema ocurre los viernes, e introduce causas que no están en el caso.",
      "example2": "La diferencia parece deberse a cómo está organizada la plantilla y a las distintas formas de asistencia al trabajo, no a un problema del servicio de almuerzos.",
      "explanation2": "No identifica el mecanismo específico: no menciona el home office ni que el problema ocurre los viernes.",
      "example3": "Las ventas más bajas parecen deberse a que la gente viene menos y a posibles problemas del menú, como precios o variedad.",
      "explanation3": "No identifica el mecanismo correcto, o lo menciona de forma muy superficial, e introduce causas que no aparecen en el caso; tampoco menciona que el problema ocurre los viernes."
    },
    {
      "score": 1,
      "description": "La respuesta es correcta pero incompleta: menciona parte de la idea central que subyace al problema, pero no desarrolla el mecanismo causal relevante de manera clara o deja elementos esenciales sin explicar.",
      "example1": "Sí, la sede Norte tiene empleados que trabajan desde casa por eso vende menos.",
      "explanation1": "Menciona que en la sede Norte hay más home office, pero no aclara que esto ocurre específicamente los viernes.",
      "example2": "Los datos de la encuesta de preferencias no son del todo claros porque los viernes varios empleados de administración de la sede Norte trabajan desde casa, así que habría que revisar mejor cuántas personas estuvieron presentes antes de sacar conclusiones.",
      "explanation2": "Menciona el home office de los viernes, pero no lo señala explícitamente como la causa de la menor venta de almuerzos.",
      "example3": "Por lo que estuve viendo, los viernes suele haber menos gente en la oficina y eso puede estar afectando las ventas, así que quizá convenga pensar en algunas acciones para estimular la demanda ese día.",
      "explanation3": "Menciona que los viernes hay menos presencialidad, pero no identifica que esto se debe a la mayor proporción de empleados de administración en la sede Norte ni explica claramente que ese es el mecanismo causal de la menor venta de almuerzos."
    },
    {
      "score": 2,
      "description": "La respuesta es correcta y completa: identifica claramente la idea central que subyace al problema y explica de manera precisa el mecanismo causal relevante, conectando todos los elementos necesarios para justificar la conclusión.",
      "example1": "Sí, la sede Norte vende menos que la sede Sur los viernes porque, en comparación con la sede Sur, tiene más empleados de administración que tienen permitido trabajar desde casa ese día.",
      "explanation1": "Identifica correctamente que la sede Norte tiene más empleados de administración que hacen home office los viernes, explicando así la caída de ventas ese día.",
      "example2": "La diferencia se da los viernes porque la sede Norte tiene más empleados de administración que trabajan desde casa ese día, mientras que en la sede Sur la mayoría va presencialmente.",
      "explanation2": "Identifica correctamente que la sede Norte tiene más empleados de administración que hacen home office los viernes, lo que explica la menor venta de almuerzos ese día."
    }
  ]
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/followup/lunch_fup_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/followup/lunch_fup_guides.json`。

### 2. rest_fup_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{
  "follow_up_question": [
    {
      "question": "¿Me contarías brevemente por qué es que la sede Norte está recibiendo malos puntajes en la plataforma de envíos?",
      "correct_answer": "Sí. El problema es que en la sucursal Norte, los empleados de plancha tienen menor antigüedad. Esto sugiere que la mayoría del personal en plancha de Norte es nuevo y probablemente aún no está familiarizado con los procesos, lo que podría explicar las demoras en la preparación."
    }
  ],
  "content_rubric": [
    {
      "score": 0,
      "description": "La respuesta es incorrecta: no identifica el mecanismo causal correcto que genera el problema, y/o introduce explicaciones irrelevantes o equivocadas.",
      "example1": "Sí, la sucursal Norte presenta una mayor cantidad de empleados en el área de ensamblado. Esto podría estar entorpeciendo la producción y retrasando la preparación de los pedidos.",
      "explanation1": "No identifica el mecanismo causal central detrás del problema (la menor antigüedad en plancha) y propone una causa que no aparece en el caso.",
      "example2": "Por lo que estuve revisando, el problema parece venir del sector de atención al cliente. Es posible que quienes reciben los pedidos estén cometiendo errores o tardando demasiado, y eso impacta negativamente en los puntajes.",
      "explanation2": "No identifica el área correcta ni el mecanismo relevante; atribuye el problema a un sector que no aparece en el caso.",
      "example3": "Buen día, requerimos aumentar la experiencia del personal y la cantidad de repartidores.",
      "explanation3": "No identifica el mecanismo correcto y agrega causas irrelevantes, como la necesidad de más repartidores, que no aparecen en el caso."
    },
    {
      "score": 1,
      "description": "La respuesta es correcta pero incompleta: menciona parte de la idea central que subyace al problema, pero no desarrolla el mecanismo causal relevante de manera clara o deja elementos esenciales sin explicar.",
      "example1": "El problema está en que la sucursal Norte tiene empleados menos experimentados.",
      "explanation1": "Reconoce que el personal del Norte tiene menos experiencia, pero no especifica que esto ocurre en el área de plancha ni explica cómo esa falta de antigüedad genera los malos puntajes.",
      "example2": "En la sede Norte el personal de plancha es bastante nuevo y todavía no tiene suficiente práctica, por eso probablemente están teniendo dificultades en el rol.",
      "explanation2": "Menciona la falta de experiencia en plancha, pero no explica cómo eso genera demoras ni cómo esas demoras producen los malos puntajes.",
      "example3": "Hola Ramiro, en la zona de plancha el equipo todavía es bastante inexperto, y creo que ese es el problema.",
      "explanation3": "Menciona que el personal de plancha carece de experiencia, pero no explica cómo esa falta de práctica genera demoras ni cómo esas demoras derivan en los malos puntajes."
    },
    {
      "score": 2,
      "description": "La respuesta es correcta y completa: identifica claramente la idea central que subyace al problema y explica de manera precisa el mecanismo causal relevante, conectando todos los elementos necesarios para justificar la conclusión.",
      "note": "Se aceptan formulaciones equivalentes a 'baja antigüedad' como 'son muy nuevos', 'les falta experiencia', 'no tienen práctica' u otros sinónimos, siempre que se identifique correctamente el área relevante (plancha) y se explique que la falta de experiencia causa demoras en la preparación, lo cual genera los malos puntajes.",
      "example1": "Los empleados en plancha de la sucursal Norte presentan poca antigüedad. Esta falta de experiencia es lo que, probablemente, explica que la sucursal Norte presente tiempos de preparado mayores en promedio y, por lo tanto, malos puntajes en la plataforma de envíos.",
      "explanation1": "Identifica la falta de antigüedad específicamente en plancha y explica claramente cómo esto produce tiempos de preparado mayores y malos puntajes.",
      "example2": "Por lo que estuve analizando, el inconveniente surge en el proceso de preparación de los pedidos: el personal de plancha tiene poca experiencia y eso provoca retrasos, lo que termina afectando el desempeño general de la sucursal.",
      "explanation2": "Identifica correctamente que el problema está en plancha y explica que la falta de experiencia del personal genera retrasos en la preparación, articulando el mecanismo causal que deriva en el bajo desempeño de la sucursal."
    }
  ]
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/followup/rest_fup_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/followup/rest_fup_guides.json`。

### 3. sales_fup_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{
  "follow_up_question": [
    {
      "question": "¿Me contarías brevemente por qué es que no estamos vendiendo más estufas en invierno y ventiladores portátiles en verano?",
      "correct_answer": "Sí. En 2024, durante los meses donde cada producto tiene mayor demanda, las estufas y los ventiladores no fueron incluidos en los envíos publicitarios. Esto probablemente hizo que los clientes no recibieran recordatorios u ofertas de estos productos en el momento de mayor necesidad, llevando a menores ventas en los meses donde uno esperaría que las ventas fuesen mayores."
    }
  ],
  "content_rubric": [
    {
      "score": 0,
      "description": "La respuesta es incorrecta: no identifica el mecanismo causal correcto que genera el problema, y/o introduce explicaciones irrelevantes o equivocadas.",
      "example1": "Sí, la falta de estacionalidad en las ventas de los ventiladores podría explicarse por una modificación en las preferencias de los consumidores que, por las condiciones macroeconómicas, ahora eligen los aires acondicionados.",
      "explanation1": "No identifica el problema real, ya que atribuye las bajas ventas a un cambio en preferencias o aires acondicionados, causas que no aparecen en el caso, e ignora completamente el rol de la publicidad estacional.",
      "example2": "Las bajas ventas probablemente se explican por las limitaciones para ingresar productos importados al país, lo que redujo la disponibilidad y afectó la demanda.",
      "explanation2": "Atribuye el problema a restricciones de importación equivocadamente e ignora el rol de la publicidad estacional.",
      "example3": "Las ventas bajaron porque no estamos haciendo suficiente publicidad en general; habría que aumentar la cantidad de anuncios.",
      "explanation3": "Atribuye el problema a una falta de publicidad en términos generales, pero no identifica que el error concreto fue no incluir estufas y ventiladores en los envíos publicitarios durante los meses de mayor demanda."
    },
    {
      "score": 1,
      "description": "La respuesta es correcta pero incompleta: menciona parte de la idea central que subyace al problema, pero no desarrolla el mecanismo causal relevante de manera clara o deja elementos esenciales sin explicar.",
      "example1": "Sí, el problema pareciera ser la estrategia de marketing.",
      "explanation1": "Identifica que el problema está vinculado al marketing, pero no explica que el error específico fue no incluir estufas y ventiladores en los envíos publicitarios durante los meses de mayor demanda.",
      "example2": "Por lo que estuve viendo, el problema parece venir de cómo se estuvieron promocionando los productos, porque la comunicación no estuvo bien alineada con las temporadas.",
      "explanation2": "Reconoce que el problema está relacionado con la promoción y la estacionalidad, pero no especifica que el error concreto fue no incluir estufas y ventiladores en los envíos publicitarios durante los meses de mayor demanda ni explica el mecanismo causal completo.",
      "example3": "El problema parece estar en el calendario de publicidad: las promociones no se enviaron en las fechas adecuadas y eso hizo que los productos no se comunicaran en la temporada correcta.",
      "explanation3": "Menciona que la publicidad no estuvo alineada con la temporada, pero no identifica que el error específico fue no incluir estufas y ventiladores en los envíos publicitarios durante los meses de mayor demanda ni desarrolla el mecanismo causal completo."
    },
    {
      "score": 2,
      "description": "La respuesta es correcta y completa: identifica claramente la idea central que subyace al problema y explica de manera precisa el mecanismo causal relevante, conectando todos los elementos necesarios para justificar la conclusión.",
      "example1": "Sí, el problema radica en el diseño de nuestra estrategia de marketing. Mientras que en 2023 logramos que la publicidad acompañara adecuadamente el patrón estacional, en 2024 esto no ocurrió, lo que nos impidió aprovechar los picos de demanda de los ventiladores, en verano, y de las estufas, en invierno.",
      "explanation1": "Identifica correctamente que la publicidad no acompañó la estacionalidad en 2024 y explica cómo ese desajuste provocó la caída en ventas de los productos que dependen fuertemente de la demanda estacional.",
      "example2": "El inconveniente se debe a que en 2024 la publicidad no acompañó la estacionalidad: las estufas no fueron incluidas en las campañas de invierno y los ventiladores no aparecieron en las campañas de verano, lo que hizo que los clientes no recibieran los recordatorios adecuados en los meses de mayor demanda.",
      "explanation2": "Explica de manera precisa que la publicidad no incluyó estufas en invierno ni ventiladores en verano, identificando el error estacional y el mecanismo causal que llevó a la caída en ventas."
    }
  ]
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/followup/sales_fup_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/followup/sales_fup_guides.json`。

### 4. lunch_task_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{ 
  "task_context": {
    "description": "Trabajás en la gestión de “Sabores Express”, un emprendimiento contratado para manejar el comedor en las sedes Norte y Sur de Infotech, una importante empresa. Ayer recibiste el siguiente correo electrónico de tu jefa:",
    "email_from_boss": "De: Adriana González <agonzalez@gmail.com>\nAsunto: problema con ventas en la sede Norte\nHola, ¿cómo estás?\nTe escribo porque estuve mirando las ventas de las últimas semanas y no logro entender qué está pasando en nuestro comedor de la sede Norte. A pesar de que Infotech tiene casi el mismo número de empleados en ambas sedes, vendemos menos almuerzos en la sede Norte que en la Sur. ¿Me ayudás a entender lo que está pasando?\nAdjunto un informe que preparó mi equipo para ayudarnos a entender mejor la situación. A partir de los datos de este informe, me gustaría que me compartas tu mirada sobre los siguientes puntos:\nLos clientes de la sede Norte, ¿están eligiendo en mayor medida otras alternativas de almuerzo fuera del comedor?\n¿Las ventas en la sede Norte bajaron en general o solo en un momento específico?\n¿Algo más del informe te parece relevante para entender lo que está pasando?\nPor favor fundamentá bien tus respuestas, ya que planeo compartir este diagnóstico con otros miembros del equipo.\nPor último, según tu análisis, ¿qué sugerirías que hagamos para solucionar este problema?\nSaludos,\nAdriana",
    "informe_adjunto":{
      "resumen": "Resumen del problema: A pesar de que Infotech tiene casi el mismo número de empleados en ambas sedes, se venden menos almuerzos en la sede Norte que en la Sur.",
      "grafico": "1) Número diario de almuerzos vendidos en el comedor de cada sede durante las últimas tres semanas:\nhttps://i.imgur.com/ptacA4I.png",
      "tabla1": "2) Durante la semana pasada se realizó una encuesta a los empleados de Infotech presentes en la oficina. Se les preguntó de dónde obtuvieron su almuerzo ese día. Los resultados son los siguientes:\n\\n\\n\\begin{tabular}{|l|*{5}{P{3cm}|}}\\n\\hline\\n\\textbf{Site} & \\textbf{Lunes} & \\textbf{Martes} & \\textbf{Miércoles} & \\textbf{Jueves} & \\textbf{Viernes} \\\\\\n\\hline\\n\\textbf{Sur} &\\n\\makecell[l]{Comedor: 80\\%\\\\Otro lugar: 20\\%} &\\n\\makecell[l]{Comedor: 76\\%\\\\Otro lugar: 24\\%} &\\n\\makecell[l]{Comedor: 75\\%\\\\Otro lugar: 25\\%} &\\n\\makecell[l]{Comedor: 80\\%\\\\Otro lugar: 20\\%} &\\n\\makecell[l]{Comedor: 78\\%\\\\Otro lugar: 22\\%} \\\\\\n\\hline\\n\\textbf{Norte} &\\n\\makecell[l]{Comedor: 78\\%\\\\Otro lugar: 22\\%} &\\n\\makecell[l]{Comedor: 75\\%\\\\Otro lugar: 25\\%} &\\n\\makecell[l]{Comedor: 80\\%\\\\Otro lugar: 20\\%} &\\n\\makecell[l]{Comedor: 79\\%\\\\Otro lugar: 21\\%} &\\n\\makecell[l]{Comedor: 78\\%\\\\Otro lugar: 22\\%} \\\\\\n\\hline\\n\\end{tabular}",
      "tabla2": "3) Infotech cuenta con empleados en 2 áreas distintas: administración y ventas. Los empleados de administración pueden trabajar desde casa los viernes, mientras que los de ventas deben asistir presencialmente de lunes a viernes. La tabla muestra las características de los empleados de cada sede según el área de trabajo:\\n\\n\\begin{tabular}{l cccc}\\n\\toprule\\n& \\multicolumn{2}{c}{\\textbf{Sede Sur}} & \\multicolumn{2}{c}{\\textbf{Sede Norte}} \\\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\\n\\textbf{Área de trabajo} & \\textbf{\\makecell{Número de \\\\ Empleados}} & \\textbf{\\makecell{Antigüedad promedio \\\\ (en años)}} & \\textbf{\\makecell{Número de \\\\ Empleados}} & \\textbf{\\makecell{Antigüedad promedio \\\\ (en años)}} \\\\\\n\\midrule\\nAdministración & 20 & 2.0 & 81 & 3.0 \\\\\\nVentas & 105 & 3.0 & 44 & 2.0 \\\\\\n\\midrule\\n\\textbf{Total} & \\textbf{125} & \\textbf{2.8} & \\textbf{125} & \\textbf{2.6} \\\\\\n\\bottomrule\\n\\end{tabular}"},
    "consigna": "Escribí a continuación un correo con la respuesta a Adriana:\nPara: Adriana González\nAsunto: Re: problema con ventas en la sede Norte"
  },
  "content": {
    "diagnosis": {
      "max_points": 6,
      "questions": {
        "A1": {
          "prompt": "Los clientes de la sede Norte, ¿están eligiendo en mayor medida otras alternativas de almuerzo fuera del comedor?",
          "correct_answer": "No. Se puede ver en la tabla del informe que el % de empleados de Infotech que eligen el comedor (vs. otro lugar) es similar en la Sede Norte que en la sede Sur. Las ventas no están cayendo porque los clientes estén eligiendo en mayor medida otras alternativas fuera del comedor.",
          "note": "Para recibir puntaje en este punto **debe mencionar** explícitamente que las proporciones de empleados que almuerzan en el comedor (versus otro lugar) son similares entre las dos sedes. Frases genéricas como 'no hay diferencias entre sucursales' o 'los resultados son parecidos' deben calificarse con 0 puntos, ya que no especifican a qué tipo de diferencia se refieren. La respuesta debe aludir claramente a la comparación de proporciones entre sedes, y si además menciona que esta similitud se mantiene a lo largo de la semana, mejor. No hace falta que se proporcionen ejemplos numéricos para obtener 2 puntos en este criterio, pero sí debe hacerse referencia explícita a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente",
              "example": "Sí, en la sede Norte hay un mayor porcentaje de empleados que decide no almorzar en el comedor.",
              "explanation": "La afirmación es incorrecta según los datos del informe: no hay un mayor porcentaje de empleados de la sede Norte eligiendo alternativas externas. Además, la respuesta no menciona la comparación de proporciones entre sedes, requisito indispensable para recibir puntaje en este criterio."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial",
              "example": "No, en la sede Norte no parecen estar eligiendo otras alternativas con más frecuencia.",
              "explanation": "La respuesta va en la dirección correcta, pero es demasiado general: no menciona las proporciones de empleados que almuerzan en el comedor en cada sede, ni hace referencia explícita a los datos de la tabla. No cumple con el requisito central del criterio, aunque tampoco afirma algo incorrecto, por lo que merece 1 punto."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente",
              "example": "No, como se muestra en la tabla provista en el informe, el porcentaje de empleados que elige el comedor en la sede Norte es muy similar al porcentaje de empleados que elige el comedor en la sede Sur.",
              "explanation": "La respuesta hace referencia explícita a la comparación de proporciones entre sedes —el requisito clave del criterio— y además menciona que esta información surge de los datos de la tabla del informe. No aporta números, pero no es necesario para obtener el puntaje máximo. La justificación es clara y adecuada."
            }
          }
        },
        "A2": {
          "prompt": "¿Las ventas en la sede Norte bajaron en general o solo en un momento específico?",
          "correct_answer": "Como se ve en el gráfico, las ventas en la sede Norte únicamente son menores los días viernes. No hay diferencias entre las ventas de las dos sedes en los demás días de la semana.",
          "note": "Aludir a la causa real del problema no alcanza para recibir un punto en este inciso. Expresiones como 'constantes y parejos', 'similares', 'sin diferencias', 'igual el resto de los días' o equivalentes, deben considerarse como que el participante está diciendo que las ventas son iguales el resto de los días. No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente",
              "example": "Las ventas en la sede Norte no mostraron una baja puntual, sino que han sido constantemente más bajas que las de la sede Sur durante las tres semanas analizadas.",
              "explanation": "La afirmación contradice directamente los datos del gráfico: las ventas no son constantemente más bajas en la sede Norte, sino solo los días viernes. Además, la respuesta no distingue entre días ni identifica el patrón específico que exige la consigna. Por lo tanto, no responde correctamente al punto evaluado."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial.",
              "example": "La sede Norte vende menos los días viernes",
              "explanation": "La respuesta identifica correctamente el día en que la sede Norte vende menos, pero es demasiado breve y no desarrolla la comparación con el resto de los días de la semana. No hace referencia explícita al patrón general del gráfico ni explica que fuera de los viernes las ventas son similares entre sedes. Por eso es correcta pero superficial."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente",
              "example": "En la información adjuntada puede observarse que, en todas las semanas, la sede Norte presenta menos ventas que la sede Sur los viernes. El resto de los días las ventas en ambas sedes son prácticamente iguales.",
              "explanation": "La respuesta describe con claridad el patrón del gráfico: identifica el día específico de menor desempeño (viernes) y aclara que fuera de ese día las ventas son similares. Menciona explícitamente la comparación entre sedes y se apoya en los datos del informe, cumpliendo plenamente con los requisitos para obtener 2 puntos."
            }
          }
        },
        "A3": {
          "prompt": "¿Algo más del informe te parece relevante para entender lo que está pasando?",
          "correct_answer": "Sí. La sede Norte tiene una mayor proporción de empleados del área de Administración (81 sobre 125), mientras que la sede Sur tiene una mayor proporción del área de ventas (105 sobre 125). Los empleados de administración tienen permitido trabajar desde su casa los viernes, mientras que los de ventas deben asistir presencialmente de lunes a viernes. La explicación más probable para la diferencia de ventas entre sedes los días viernes es que la sede Norte tiene más empleados de administración, y estos se quedan trabajando desde su casa los viernes.",
          "note": "No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente.",
              "example": "Sí, las diferencias en las ventas entre ambas sedes probablemente se deban a la composición del personal. Es probable que los empleados de administración, que tienen mayor presencia en la sede Norte, perciban ingresos más bajos que los empleados de ventas, lo que podría explicar el menor nivel de ventas en esa sede.",
              "explanation": "La respuesta menciona diferencias en la composición del personal, pero introduce una explicación inexistente en el informe (“ingresos más bajos”) que no está respaldada por los datos. Además, no identifica el mecanismo correcto: que los empleados administrativos trabajan desde su casa los viernes. Esto constituye una interpretación incorrecta del informe, por lo que la respuesta debe recibir 0 puntos."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial.",
              "example": "Sí, la sede Norte vende menos que la sede Sur los viernes porque tiene más empleados que trabajan desde casa ese día.",
              "explanation": "La respuesta señala el mecanismo correcto (más empleados trabajando desde casa los viernes), pero lo hace de forma muy general y sin referencia explícita a los datos del informe. No menciona la proporción de empleados administrativos ni alude a la diferencia en la composición del personal entre sedes, por lo que queda incompleta y merece solo 1 punto."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente.",
              "example": "Sí, la tabla que muestra la composición de trabajadores en ambas sedes indica que la sede Norte tiene una mayor proporción de empleados administrativos. Como en ambas sedes este grupo puede trabajar desde casa los días viernes, esta diferencia en la composición podría explicar por qué las ventas de los viernes son más bajas en la sede Norte.",
              "explanation": "La respuesta menciona de manera explícita la diferencia en la composición del personal entre sedes, se basa directamente en los datos de la tabla y describe correctamente el mecanismo: los empleados administrativos pueden trabajar desde casa los viernes, reduciendo la cantidad de clientes potenciales en la sede Norte. La explicación es clara, precisa y fundamentada en la información del informe, cumpliendo plenamente con el criterio para 2 puntos."
            }
          }
        }
      }
    },
    "solution": {
      "max_points": 4,
      "prompt": "Las propuestas del participante pueden incluir una o varias acciones para solucionar el problema. Cada acción debe evaluarse de manera individual según los criterios B1, B2 y B3, sin elegir una 'mejor' acción dentro de la grilla. El objetivo de esta sección es definir cómo puntuar cada acción concreta en función de si aborda la causa del problema, cuán específica es y cuán realista resulta.",
      "problem_to_solve":"Las ventas son menores en la sede Norte porque cuentan con una mayor proporción de trabajadores que pueden trabajar desde su casa los viernes.",
      "criteria": {
        "B1": {
          "description": "Para cada acción propuesta, ¿la solución propuesta lidia directamente con la causa del problema?",
          "note": "Para recibir 1 punto en este criterio, el participante debe proponer una solución que aborde explícitamente la causa del problema identificada en A3 (la menor asistencia de empleados los viernes en la sede Norte). Si en A3 reconoció claramente esa causa y en B1 presenta una propuesta coherente con ella, aunque no la mencione de forma explícita, puede recibir 1 punto. Si no identificó la causa en A3 ni en B1, o propone soluciones genéricas sin relación con la asistencia (por ejemplo, mejorar la comida, la atención o la publicidad), debe recibir 0 puntos.",
          "note2": "No debe asignarse puntaje en este criterio si el participante solo identifica correctamente la causa del problema en A3 (que la sede Norte tiene más empleados administrativos que trabajan desde casa los viernes), pero no propone una solución explícita para resolverlo en B1. Reconocer la causa no equivale a ofrecer una medida correctiva. La propuesta debe indicar de manera clara qué acción se tomaría para compensar la menor asistencia o mitigar su efecto en las ventas (por ejemplo, ofrecer promociones los viernes o ajustar la producción los viernes). No se debe otorgar puntaje en B1 por diagnóstico correcto en A3, ni por alusiones generales a la causa del problema en B1.",
          "note3": "Toda propuesta basada en promociones, menús del día, descuentos, beneficios o 'special days' debe recibir automáticamente 0 puntos si no apunta específicamente a (a) aumentar las ventas de los viernes —el día afectado por el teletrabajo— o (b) aumentar explícitamente las ventas de lunes a jueves para compensar la caída de los viernes. Propuestas promocionales que no especifican uno de estos dos objetivos no abordan la causa del problema.",
          "scores": {
            "0": {
              "label": "No",
              "example1": "Podríamos implementar una encuesta que le pregunte a los empleados de la sede Norte qué es lo que no les gusta de la comida del comedor.",
              "explanation1": "La propuesta no está relacionada con la causa del problema: la menor asistencia los viernes debido a que muchos empleados administrativos trabajan desde su casa. En lugar de proponer una acción para compensar o mitigar esa menor asistencia, la sugerencia se enfoca en la comida, lo cual es irrelevante para el mecanismo real. Por eso no lidia con la causa del problema y debe recibir 0 puntos.",
              "example2": "Propongo ofrecer menús especiales y descuentos para incrementar las ventas.",
              "explanation2": "La propuesta no aborda la causa del problema. Sugiere ofrecer menús especiales y descuentos, pero no especifica que estas acciones deban aplicarse los viernes —el día afectado por la menor asistencia— ni que busquen compensar esa caída aumentando las ventas de lunes a jueves. Al no orientar las promociones hacia el mecanismo que genera la baja en ventas (el teletrabajo de los empleados administrativos los viernes), la solución no responde al problema real y debe recibir 0 puntos."
            },
            "1": {
              "label": "Sí",
              "example1": "Podríamos ofrecer promociones los viernes en la sede Norte para incentivar a quienes suelen almorzar en otro lugar a elegir el comedor ese día. De este modo, podríamos compensar la caída en ventas que se produce cuando los empleados administrativos trabajan desde casa.",
              "explanation1": "La propuesta se vincula de manera directa con la causa del problema: la menor asistencia en la sede Norte los viernes por el teletrabajo del personal administrativo. La solución plantea una acción concreta —promociones específicas los viernes— orientada a compensar esa baja de clientes. Aborda explícitamente el mecanismo que genera la caída en ventas.",
              "example2": "Podríamos ofrecer promociones de lunes a jueves en la sede Norte para incentivar a quienes suelen almorzar en otro lugar a elegir el comedor durante la semana. De este modo, podríamos compensar la caída en ventas que se produce cuando los empleados administrativos trabajan desde casa los viernes.",
              "explanation2": "La propuesta se vincula de manera directa con la causa del problema: la menor asistencia en la sede Norte los viernes por el teletrabajo del personal administrativo. La solución plantea una acción concreta —promociones específicas de lunes a jueves- orientada a compensar esa baja de clientes los viernes."

            }
          }
        },
        "B2": {
          "description": "Para cada acción propuesta, ¿es una acción concreta/específica?",
          "note": "Este criterio evalúa el grado de concreción y detalle de la propuesta. Es decir, cuán claramente se entiende qué acción se propone. Para obtener 2 puntos, la propuesta debe describir una acción definida, y dejar claro qué se haría y con qué objetivo. Si se mencionan varias opciones sin desarrollo, si las acciones son vagas (por ejemplo, 'hablar con Infotech o ver la manera de ofrecer delivery'), corresponde 1 punto o menos.",
          "scores": {
            "0": {
              "label": "Propuesta demasiado general o abstracta: no se entiende bien qué acción concreta se propone.",
              "example": "Sugiero modificar la oferta el viernes, u ofrecer alternativas para los que hacen home office",
              "explanation": "La propuesta es vaga y no define ninguna acción concreta. “Modificar la oferta” y “ofrecer alternativas” son expresiones amplias que no permiten entender qué se haría exactamente ni cómo se implementaría. Tampoco especifica qué tipo de modificaciones se realizarían ni cómo se relacionan con el problema identificado, por lo que recibe 0 puntos."
            },
            "1": {
              "label": "Propuesta con cierta especificidad, pero sin suficiente detalle operativo o contextual.",
              "example1": "Evaluar ofrecer promociones los viernes.",
              "explanation1": "La propuesta apunta en la dirección correcta (promociones los viernes), pero se formula de manera muy preliminar: “evaluar ofrecer” no constituye una medida concreta y no se aclara qué tipo de promoción, a quién estaría dirigida o qué se busca lograr. Tiene algo de especificidad, pero es insuficiente para comprender la acción de forma operativa, por lo que obtiene 1 punto.",
              "example2": "Deberíamos modificar el menú los viernes y ofrecer promoeciones el día de home office.",
              "explanation2": "La propuesta se orienta hacia el mecanismo adecuado —intervenir específicamente los viernes, día afectado por el home office— pero sigue siendo demasiado general. Decir 'modificar el menú' y 'ofrecer promociones' no aclara qué cambios concretos se harían, qué tipo de promociones se aplicarían, ni cómo estas acciones contribuirían a mitigar la caída en ventas. Aunque muestra cierta dirección correcta, carece del nivel de detalle operativo necesario para definirla como una acción concreta, por lo que corresponde asignar 1 punto."
            },
            "2": {
              "label": "Propuesta clara y específica: se entiende qué acción se propone y cómo podría implementarse en términos generales. No es necesario que la propuesta incluya plazos, métricas o formatos de implementación, pero sí debe describir de forma directa una medida concreta.",
              "example": "Ofrecer promociones en la sede Norte los días de menor asistencia para incentivar el consumo en el comedor.",
              "explanation": "La propuesta es directa y fácilmente implementable: especifica qué se haría (ofrecer promociones), dónde (sede Norte) y con qué objetivo (incentivar el consumo los días de baja asistencia). No necesita detallar plazos o formatos para ser considerada clara y concreta. Describe una acción definida y coherente con el contexto, por lo que merece 2 puntos."
            }
          }
        },
        "B3": {
          "description": "Para cada acción propuesta, ¿es una acción realista?",
          "note": "Para recibir 1 punto en este criterio, la propuesta debe ser factible dentro del rol y las posibilidades reales de gestión del emprendimiento Sabores Express. No deben considerarse realistas las soluciones que impliquen modificar políticas laborales de Infotech (como eliminar o alterar los días de home office, cambiar las reglas de asistencia del personal administrativo o de ventas, o reasignar empleados entre sedes). Estas decisiones exceden el ámbito de acción del emprendimiento. Solo deben considerarse realistas las medidas que la empresa de catering podría implementar directamente, como ajustar la producción, ofrecer promociones, modificar el menú o diseñar alternativas para los empleados en home office.",
          "scores": {
            "0": {
              "label": "No",
              "example": "Podríamos eliminar la posibilidad de que los empleados de administración trabajen desde casa los viernes.",
              "explanation": "Esta propuesta no es realista porque implica modificar una política laboral de Infotech —la empresa empleadora del personal— y no del emprendimiento Sabores Express. El emprendimiento no tiene autoridad para cambiar las reglas de home office, asistencia o modalidades de trabajo del personal administrativo. La medida excede completamente su ámbito de acción y por lo tanto debe recibir 0 puntos."
            },
            "1": {
              "label": "Sí",
              "example": "Ofrecer promociones los viernes en la sede Norte. Esto compensaría la menor demanda provocada por la menor cantidad de empleados esos días en esa sede.",
              "explanation": "La propuesta es realista porque se limita a acciones que la empresa de catering puede implementar directamente: diseñar promociones y ajustar su oferta comercial. No pretende modificar políticas laborales ni alterar decisiones institucionales de Infotech. Por lo tanto, corresponde asignar 1 punto."
            }
          }
        }
      }
    },
    "total_max_points": 10
  },
  "writing": {
    "total_max_points": 10,
    "criteria": {
      "1": {
        "name": "Ortografía y gramática",
        "description": "Se evalúa la corrección ortográfica y gramatical del texto, incluyendo el uso adecuado de tildes, signos de puntuación, concordancia verbal y nominal, y mayúsculas. Se valora especialmente la redacción clara, fluida y cuidada, con frases bien estructuradas y sin errores que afecten la calidad o el tono profesional del mensaje.",
        "note": "No se considera error el uso de solo signos de cierre (¿? / ¡!)",
        "scores": {
          "0": {
            "label": "Errores graves o numerosos: el texto presenta múltiples errores ortográficos o gramaticales (tildes, concordancia, puntuación o mayúsculas) que se repiten a lo largo del texto. Estos errores afectan la claridad o dan una impresión de descuido, incluso si el texto se entiende en general.",
            "example1": "viendo q las ventas bajaron en ese tiempo vamos a seguir mirando el tema puede ser q ese dia no gusto la comida o q habia menos gente en la empresa igual voy a seguir viendo gracias.",
            "explanation1": "El texto presenta múltiples errores graves: ausencia sistemática de mayúsculas iniciales, uso de abreviaturas informales (“q”), omisión de tildes (“día”, “había”), problemas de puntuación (frase larga sin comas ni puntos), y falta de estructura sintáctica. Estos errores afectan tanto la claridad como el tono profesional del mensaje, por lo que corresponde asignar 0 puntos.",
            "example2": "Hola Adriana Buenas..viendo los datos de las dos sucursales,zona norte tiene mas empleados en oficina q hacen home office y eso baja las ventas xq no van al comedor,en cambio zona sur estan todos presencial toda la semana por eso venden mas esos dias..",
            "explanation2": "El texto presenta errores repetidos de tildes (“más”, “están”), uso de abreviaturas informales (“q”, “xq”), puntuación incorrecta (coma mal colocada, exceso de puntos, ausencia de espacios), problemas de concordancia y mayúsculas incorrectas (“zona norte”, “zona sur”). La acumulación de errores y el registro muy poco formal justifican asignar 0 puntos."
          },
          "1": {
            "label": "Algunos errores o descuidos menores, pero perceptibles: se observan varios errores dispersos (tildes omitidas, puntuación inadecuada, uso impreciso de conectores o ligeras fallas de concordancia). No impiden la comprensión, pero restan fluidez o profesionalismo al texto.",
            "example1": "Estimada Adriana,\nPor lo que veo en los datos la mayoria de los empleados de la sede Norte trabaja remoto los viernes, por eso bajan las ventas ese dia. En la sede Sur la gente asiste toda la semana y las ventas se mantienen. Segun el informe no parece que esten eligiendo otros lugares para almorzar.",
            "explanation1": "El texto es comprensible, pero presenta varios errores menores: tildes omitidas (“mayoría”, “día”, “según”, “estén”), algunos problemas de puntuación (falta una coma tras “los datos”), y una redacción algo plana. Estos errores no impiden entender el mensaje, pero afectan la prolijidad y el nivel profesional del texto. Por eso recibe 1 punto.",
            "example2": "Hola por lo que veo en la sede norte hay mas empleados de ventas que en la sur y eso puede explicar porque ahí bajaron las ventas los viernes ya q varios hacen home office esos dias",
            "explanation2": "El texto contiene errores frecuentes de tildes (“más”, “por qué”, “días”), falta de puntuación (la frase es demasiado larga y sin cortes), y uso de abreviaturas informales (“q”). Aunque el mensaje es comprensible, el nivel de corrección es insuficiente para una redacción profesional. Corresponde asignar 1 punto."
          },
          "2": {
            "label": "Redacción impecable o casi impecable: el texto está cuidadosamente escrito, sin errores ortográficos ni gramaticales perceptibles. La puntuación es precisa, las oraciones están bien estructuradas y el registro es fluido y natural. A lo sumo puede haber un error aislado que no afecta en absoluto la calidad del texto.",
            "example1": "Buenas tardes, Adriana. Según los datos, la baja en ventas los viernes se explica por el trabajo remoto del personal administrativo de la sede Norte. En la sede Sur la asistencia es completa, por lo que las ventas se mantienen estables.",
            "explanation1": "El texto está correctamente escrito: uso adecuado de tildes, puntuación precisa, frases claras y bien estructuradas. El registro es profesional y fluido. No presenta errores perceptibles, por lo que corresponde asignar 2 puntos.",
            "example2": "Hola Adriana,\nRevisando los datos, observé que la baja en ventas ocurre principalmente los viernes, cuando gran parte del personal administrativo de la sede Norte trabaja remoto. De lunes a jueves las ventas son similares a la sede Sur.\nPropongo ajustar la producción de almuerzos los viernes y ofrecer menús promocionales o viandas para quienes hacen home office.\nQuedo a disposición para conversar las opciones.\nSaludos,",
            "explanation2": "El texto es claro, está correctamente puntuado y no presenta errores ortográficos ni gramaticales. La redacción fluye de forma natural, con oraciones bien construidas y coherentes. El tono es profesional y adecuado al contexto. Es un ejemplo típico de 2 puntos."
          }
        }
      },
      "2": {
        "name": "Claridad y legibilidad",
        "description": "Se evalúa la claridad, precisión y fluidez del texto, **dentro del contexto del mail del jefe y de la consigna**. Las ideas deben expresarse de manera directa, ordenada y sin ambigüedades, y deben permitir que el jefe comprenda la respuesta a partir de la información del informe. Se valoran las oraciones bien construidas, la coherencia entre frases y la ausencia de repeticiones o redundancias. El texto se entiende fácilmente y transmite las ideas con naturalidad y economía de palabras.  Un texto es poco claro no solo cuando está mal escrito, sino también cuando, aunque sea breve o gramaticalmente correcto, **no desarrolla las ideas necesarias para responder lo que pide el jefe**, o resulta tan general que el jefe no entendería el mensaje.",
        "note": "La repetición de ideas **debe penalizarse**. Los textos que no desarrollan las ideas mínimamente necesarias para que el jefe entienda la respuesta **en el contexto de su mail** también deben penalizarse. Un texto puede estar bien escrito a nivel lingüístico pero ser confuso o inútil si no permite comprender la respuesta requerida.",
        "scores": {
          "0": {
            "label": "Texto confuso o desorganizado: el texto resulta difícil de comprender por errores de construcción o frases inconexas. Presenta repeticiones de ideas innecesarias o ambigüedades que impiden seguir el hilo argumental con claridad.",
            "example1": "Hola Adriana, lo que pasó fue que se tardó más en entregar los almuerzos, en la sede sur, porque había menos personal, y también algunos empleados nuevos, que no conocían bien el proceso, y eso hizo que se acumularan los pedidos, y eso fue alterando todo.",
            "explanation1": "El texto presenta baja claridad por varias razones: frases encadenadas sin estructura, falta de puntuación adecuada, repeticiones (“y eso”), ambigüedad sobre qué sede tiene el problema, y un desarrollo desordenado que mezcla causas sin jerarquía ni coherencia. Esto impide seguir el hilo argumental con fluidez.",
            "example2": "Al analizar las ventas parece que bajaron en un momento pero no todo el tiempo, lo cual puede estar relacionado con distintas cosas que se dieron ese día y que al mismo tiempo hicieron que el resultado no fuera tan claro como se esperaba, porque si bien hubo menos gente también se ofreció otro menú y eso cambió la percepción general de los empleados, lo que nos lleva a pensar que hay que seguir observando.",
            "explanation2": "La oración es excesivamente larga, con ideas encadenadas sin pausas ni estructura clara. Hay múltiples hipótesis superpuestas y ambigüedad en la secuencia de eventos. El resultado es un texto difícil de seguir, sin claridad ni economía de palabras.",
            "example3": "Bajaron las ventas. Saludos,",
            "explanation3": "Aunque está escrito de manera clara y sin errores, **no dice nada útil para el jefe**: no desarrolla la idea, no usa datos del informe y no responde ninguna de las preguntas. Por tanto, debe recibir 0 puntos."
          },
          "1": {
            "label": "Claridad limitada: se identifican varias frases confusas, mal estructuradas o redundantes. La lectura requiere esfuerzo y el mensaje no fluye naturalmente. Las ideas aparecen sin una secuencia lógica o con expresiones poco precisas.",
            "example1": "Estimada Adriana, buenos días luego de revisar los informes note que las ventas en la sede norte bajaron en las últimas semanas pero al mismo tiempo aumentaron un poco en la sur, quizás sería bueno revisar mejor a que se debe esa diferencia y ver si coincide con los días de trabajo remoto, cuando tenga más datos te los envío, saludos.",
            "explanation1": "El texto expresa una idea general, pero presenta problemas de claridad: ausencia de puntuación adecuada, mezcla de ideas en una sola oración larga, uso impreciso de conectores (“pero al mismo tiempo”, “quizás”), y falta de una estructura interna que ordene los argumentos. El mensaje se entiende, pero requiere esfuerzo del lector.",
            "example2": "Hola Adriana, revisando los datos veo que las ventas bajaron más en la sede Norte que en la Sur, sobre todo los viernes. Puede deberse a que esos días hay menos empleados o a que el menú no resulta atractivo, aunque no estoy segura de cuál de las dos cosas pesa más. También noté que las semanas con menos asistencia coinciden con los días en que hubo cambios en la comida.\nPor otro lado, al mirar otra vez los resultados me da la impresión de que la baja sigue siendo más fuerte los viernes, justo cuando hay menos gente. Eso refuerza la idea de que el problema podría ser tanto por la comida como por la cantidad de empleados, o incluso por ambas cosas al mismo tiempo. Tal vez habría que revisar mejor qué pasa esos días para entender bien por qué bajan las ventas.",
            "explanation2": "El texto contiene repeticiones (“viernes”, “menos empleados”, “menos gente”), hipótesis contradictorias o no priorizadas, y exceso de información poco organizada. Aunque tiene contenido, la secuencia de ideas es poco clara y obliga a releer para comprender el mensaje.",
            "example3": "Hola Adriana, bajaron un poco las ventas pero habría que ver más cosas. Saludos,",
            "explanation3": "Responde algo, pero de forma superficial y sin desarrollar. No quedaría claro para el jefe cuál es el diagnóstico o cuáles son las posibles soluciones."
          },
          "2": {
            "label": "Claridad aceptable pero mejorable: el texto se comprende en general, aunque contiene algunas oraciones extensas, o formulaciones poco naturales que interrumpen la fluidez. Puede haber alguna repetición de ideas. Requiere algo de esfuerzo para seguir el hilo.",
            "example1": "De mi mayor consideración:\nHabiendo revisado la información sobre la baja en ventas de almuerzos en la sede Norte, considero que podría deberse al trabajo remoto del personal administrativo los días viernes, lo cual explicaría la diferencia con la sede Sur, aunque sería necesario analizar también otros factores para tener una visión más completa.\nPor lo expuesto, entiendo que la modalidad laboral es un elemento relevante en la disminución observada.\nSaludos cordiales,",
            "explanation1": "El texto es comprensible y mantiene cierta coherencia, pero presenta oraciones largas, formulaciones formales poco naturales. Aunque se entiende, la fluidez es limitada y las ideas no están del todo optimizadas.",
            "example2": "Buenas tardes Adriana: con respecto al informe, las ventas bajaron un poco en la sede Norte, no tanto en comparación con la Sur, y podría deberse a que los empleados llevan su propia comida porque no se informa con tiempo el menú. Por ese motivo considero importante planificar opciones semanales para evitar esa diferencia.",
            "explanation2": "El mensaje es claro en términos generales, pero las oraciones son extensas."
          },
          "3": {
            "label": "Claridad y legibilidad destacadas: el texto es muy claro y fluido. Las oraciones están bien construidas, no hay ambigüedades, o repetición de ideas. Se lee con naturalidad.",
            "example1": "Hola Adriana, espero que estés bien.\nGracias por la información enviada, me resultó muy útil para entender la situación.\nPor lo que pude observar, la baja en las ventas ocurre principalmente los viernes, cuando la mayoría del personal administrativo trabaja desde casa. Como posible solución, propongo alternar los días de trabajo remoto para que una parte del equipo asista los viernes y así equilibrar el consumo.\nSaludos,\nMariana",
            "explanation1": "El texto es muy claro, con ideas ordenadas y bien conectadas. Cada oración cumple una función específica y no hay repeticiones ni ambigüedades. La lectura es fluida y natural, y la información se presenta de manera precisa.",
            "example2": "Hola Adriana, espero que estés bien.\nRevisando los datos, noté que la proporción de empleados que almuerzan en el comedor es similar en ambas sedes, por lo que el problema no parece estar en una menor preferencia por el servicio. En cambio, la diferencia se explica porque en la sede Norte hay más personal administrativo que trabaja remoto los viernes, lo que reduce la cantidad de almuerzos servidos ese día.\nSaludos,",
            "explanation2": "El texto está muy bien estructurado, desarrolla las ideas con precisión y mantiene un hilo argumental claro. No hay redundancias y la exposición es directa y comprensible. La claridad y la legibilidad son excelentes."
          }
        }
      },
      "3": {
        "name": "Organización del texto",
        "description": "Se evalúa la estructura y el orden interno del texto. Debe seguir una secuencia lógica que incluya:\n1. una introducción que enmarque el mensaje o un saludo (por ejemplo, 'Hola XX, cómo estás?' o una breve referencia al mail del jefe),\nEjemplo de referencia al mail del jefe: “Revisé los datos que me enviaste y encontré lo siguiente:”\n2. un desarrollo en el que se respondan las preguntas planteadas,\n3. una sección con propuestas o sugerencias para resolver el problema, y\n4. un cierre que retome las ideas principales o una despedida.\nEjemplos de cierre o saludo:\n1.“Estoy a disposición para discutir cómo implementar las mejoras.”\n2.'Saludos,'\nTambién se valora la organización interna dentro de cada sección: el uso adecuado de párrafos, la coherencia en la secuencia de ideas y la ausencia de saltos temáticos.",
        "note": "Tanto un saludo como una referencia al mail del jefe cuentan como introducción, y tanto una despedida como un cierre que retome la ideas principales o que diga 'Quedo a disposición' cuentan como cierre.",
        "scores": {
          "0": {
            "label": "Texto desorganizado o sin estructura reconocible: no se distinguen las secciones principales o las ideas aparecen mezcladas y repetidas. Falta orden tanto en la estructura general como dentro de los párrafos.",
            "example": "Al mirar las ventas pienso que puede tener que ver con los gustos de la gente, porque en la zona norte hay más empleados y también ganan mejor, entonces quizás prefieren comer afuera o pedir otra cosa. Igual en la semana las ventas son parecidas, pero los viernes bajan mucho, puede ser por eso o porque hay menos empleados. También habría que ver si los precios influyen, porque si se subieron puede que eso afecte, aunque no estoy seguro. Capaz se podría cambiar el menú o reducir el personal para equilibrar los costos y así mejorar las ventas, ya que todo está bastante caro últimamente y eso también puede influir",
            "explanation": "El texto carece totalmente de estructura: no hay una introducción clara, no se responde en un bloque separado a las preguntas del informe, ni hay una sección de propuestas ni un cierre. Las ideas aparecen mezcladas (gustos, precios, asistencia, menú, costos) sin orden temático y en una única secuencia desordenada. No existen párrafos diferenciados ni una progresión lógica. Esto impide reconocer secciones y constituye una organización deficiente."
          },
          "1": {
            "label": "Estructura débil o confusa: se percibe cierta intención de organización, pero faltan secciones o están mal delimitadas. Dentro de cada parte hay mezcla de ideas o saltos que dificultan la lectura. Los párrafos no agrupan bien las ideas.",
            "example": "Buenas tardes Adriana: con respecto al informe que me enviaste, noté que las ventas bajaron un poco en la sede Norte, sobre todo los lunes y martes, posiblemente porque los empleados no conocen el menú con anticipación y prefieren traer su comida, por eso pienso que sería útil planificar el menú semanalmente para evitar esa situación.",
            "explanation": "El texto intenta tener una estructura —abre con un saludo y ofrece un comentario final—, pero las secciones están mal delimitadas: mezcla diagnóstico y propuesta en la misma frase, no separa ideas en párrafos y no sigue la secuencia introductoria–análisis–propuesta–cierre. La lectura es posible, pero el orden es insuficiente y confuso, lo que justifica el puntaje intermedio-bajo."
          },
          "2": {
            "label": "Organización parcial o irregular: el texto incluye la mayoría de las secciones, pero el orden o la articulación entre ellas es poco clara. Algunas partes están bien organizadas, mientras que otras presentan saltos. Los párrafos son comprensibles pero desbalanceados.",
            "example": "Buenas tardes Adriana,\nRevisando los datos del informe, noto que la diferencia en las ventas entre ambas sedes podría deberse a varios factores combinados. En la sede Norte los viernes se vende menos, lo que coincide con el día en que la mayoría del personal administrativo trabaja desde casa, pero también podría influir el tipo de menú, ya que cuando cambia la oferta las ventas tienden a mejorar. En ese sentido, no parecería que los empleados estén eligiendo otras opciones fuera del comedor, ya que el porcentaje que almuerza allí es muy similar al de la sede Sur.\nAdemás, observé que la sede Norte tiene más personal administrativo y menos de ventas, lo que reduce la cantidad de personas que asisten toda la semana. Quizás sería útil revisar si las promociones o los platos especiales se están comunicando igual en ambas sedes, o si los días de menor asistencia podrían compensarse con opciones más atractivas.\nSaludos,",
            "explanation": "El texto contiene la mayoría de las secciones esperadas (introducción, desarrollo, propuestas y cierre), pero la articulación es desigual. El diagnóstico combina demasiadas ideas en párrafos largos y con saltos temáticos. Las propuestas aparecen mezcladas con las explicaciones previas, lo que debilita la separación entre secciones. Aunque se reconoce un esfuerzo de estructura, no es completamente clara ni equilibrada."
          },
          "3": {
            "label": "Organización clara y coherente: el texto sigue la secuencia esperada (introducción, respuestas, propuestas, cierre) y las ideas dentro de cada sección están bien agrupadas. Hay un uso adecuado de párrafos, aunque las transiciones o la progresión de ideas podrían ser más fluidas.",
            "example": "Hola Adriana, ¿cómo estás?\nMuchas gracias por los datos enviados, me resultaron muy útiles para analizar la situación.\n Por lo que pude ver, las ventas bajan principalmente los viernes, mientras que el resto de la semana se mantienen estables. No parece que los empleados estén eligiendo otros lugares para almorzar, ya que los porcentajes de uso del comedor son muy similares entre sedes.\nLa diferencia se explica porque los viernes la mayoría del personal administrativo de la sede Norte trabaja desde casa. Como posible solución, podríamos alternar los días de home office o implementar promociones especiales ese día para incentivar el consumo.\nSaludos,",
            "explanation": "El texto sigue correctamente la secuencia esperada: introducción clara, diagnóstico ordenado y en párrafos separados, propuestas coherentes y un cierre. Las ideas dentro de cada sección están bien agrupadas y no hay repeticiones o mezclas graves. La única razón por la que no alcanza 4 puntos es que la falta de separación entre diagnóstico y las propuestas."
          },
          "4": {
            "label": "Organización excelente: el texto presenta una estructura completa y equilibrada: cada sección cumple su función, las ideas dentro de cada una están ordenadas, y las transiciones entre párrafos son naturales. La organización general y la interna contribuyen a una lectura fluida y lógica.",
            "example": "Hola Adriana, ¿cómo estás?\nEstuve revisando el informe y te comparto mi análisis.\nQué pasa en la sede Norte\nLos datos muestran que la proporción de empleados que almuerzan en el comedor es similar en ambas sedes, por lo que no parece que el problema sea una menor preferencia por el servicio. La diferencia principal está en la asistencia: en la sede Norte hay más empleados de administración que trabajan desde casa los viernes, lo que reduce el número de almuerzos vendidos esos días. En la sede Sur, en cambio, la mayoría pertenece al área de ventas y asiste toda la semana, manteniendo estable el nivel de consumo.\nQué podemos hacer\nAjustar la cantidad de almuerzos preparados los viernes en la sede Norte.\nImplementar un menú especial o promociones para quienes asisten ese día.\nComunicar con anticipación las opciones semanales, para incentivar la reserva de almuerzos.\nEn resumen, la baja de ventas en la sede Norte se explica por la menor presencia del personal administrativo los viernes. Si ajustamos la oferta y reforzamos la comunicación, podríamos equilibrar las ventas entre ambas sedes.\nDecime si estás de acuerdo y diseñamos un plan para testear estas propuestas en las próximas semanas.\nSaludos,",
            "explanation": "El texto presenta una estructura ejemplar: introducción clara, diagnóstico organizado en un bloque propio con ideas secuenciadas, propuestas separadas y presentadas en formato ordenado (viñetas), un cierre que retoma ideas y abre camino a próximos pasos. Las transiciones son naturales y cada sección cumple su función. La organización facilita una lectura fluida y lógica, por lo que corresponde la máxima puntuación."
          }
        }
      },
      "4": {
        "name": "Registro adecuado",
        "description": "Se evalúa si el tono del mail es apropiado para el contexto laboral y coherente con el tono del mail del jefe. El tono no debe ser excesivamente informal, debe ser cortes y profesional.\nEl criterio penaliza automáticamente (0 puntos) los casos en los que:\n1.El texto esté completamente escrito en mayúsculas (por considerarse una forma inapropiada o agresiva de comunicación).\n2. El texto incluya rastros evidentes de generación automática o placeholders propios de un asistente virtual, como firmas incompletas del tipo “[tu nombre]”, o texto no reemplazado.",
        "note1": "En este criterio no se evalúa la presencia o la falta de saludo y despedida",
        "note2": "Mencionar explícitamente que se utilizó una herramienta de IA para elaborar el diagnóstico **no se penaliza**",
        "scores": {
          "0": {
            "label": "El tono del mail es demasiado informal, coloquial o poco cortés en relación con el tono del mail del jefe. También se asigna 0 puntos si el texto está completamente en mayúsculas, si deja evidencia explícita de interacción con ChatGPT u otra IA, o si el texto no presenta un tono profesional acorde al mail del jefe.",
            "example1": "Buenas,\nSegún el informe que me mandaste creo que el problema está en la asistencia de los empleados los viernes, por eso hay menos ventas esos días. también puede influir que a fin de mes muchos gastan menos y eso baja las compras en el comedor.\nAbrazo,",
            "explanation1": "El tono es excesivamente informal para un intercambio laboral: usa saludos coloquiales (“Buenas”, “Abrazo”). No mantiene la formalidad esperable en el contexto definido por el mail del jefe.",
            "example2": "Hola Adriana, ¿cómo estás?\nSegún el informe que me mandaste creo que el problema está en la asistencia de los empleados los viernes, por eso hay menos ventas esos días. también puede influir que a fin de mes muchos gastan menos y eso baja las compras en el comedor.\nSaludos,\n[Tu nombre]",
            "explanation2": "Incluye un placeholder típico de un asistente virtual ('[tu nombre]'), lo cual activa la penalización automática.",
            "example3": "HOLA ADRIANA, COMO ESTA?\nLE ESCRIBO PARA DECIRLE QUE SEGUN LOS DATOS NO HAY GRANDES DIFERENCIAS ENTRE LAS SEDES. IGUAL TENDRIA QUE MANDARME MAS INFORMACION PARA ENTENDER BIEN.\nSALUDOS CORDIALES,",
            "explanation3": "El texto está completamente en mayúsculas, lo cual se considera un tono inadecuado o agresivo en comunicación escrita. Esto activa automáticamente el puntaje 0, independientemente del contenido."          
          },
          "1": {
            "label": "Registro adecuado: el tono es respetuoso y coherente acorde con el tono del mail del jefe. El texto mantiene un registro profesional y apropiado para el contexto laboral.",
            "example": "Hola Adriana, ¿cómo estás?\nSegún el informe que me mandaste creo que el problema está en la asistencia de los empleados los viernes, por eso hay menos ventas esos días. también puede influir que a fin de mes muchos gastan menos y eso baja las compras en el comedor.\nSaludos cordiales,",
            "explanation": "El tono es respetuoso, profesional y consistente con el estilo del mail del jefe. No hay expresiones coloquiales, excesivamente informales ni agresivas. Se mantiene un registro adecuado para un intercambio laboral, con cortesía y neutralidad apropiadas. No hay mayúsculas inapropiadas ni rastros de interacción con IA. Por lo tanto, corresponde la puntuación completa."
          }
        }
      }
    }
  }
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/task/lunch_task_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/task/lunch_task_guides.json`。

### 5. rest_task_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{ 
  "task_context": {
    "description": "Trabajás en la gestión de un local de delivery de hamburguesas premium que cuenta con dos sucursales (Norte y Sur). Cada sucursal tiene sus propios empleados, que venden hamburguesas únicamente a través de una plataforma de envíos (al estilo de PedidosYa). Ayer recibiste el siguiente correo electrónico de tu jefe:",
    "email_from_boss": "De: Ramiro González <rgonzalez@gmail.com>\nAsunto: problema con reseñas online\nHola, ¿cómo estás?\nTe escribo porque me puse a revisar las opiniones online de nuestras sucursales, y estoy un poco preocupado por la sucursal Norte: en las últimas semanas estuvimos recibiendo bajas puntuaciones debido a demoras excesivas en el envío. ¿Podrías ayudarme a entender lo que está pasando?\nAdjunto un informe que preparó mi asistente para ayudarnos a entender mejor la situación. A partir de los datos de este informe, me gustaría que me compartas tu mirada sobre los siguientes puntos:\n¿Podrías revisar si el problema viene de la plataforma de envíos?\n¿Puede ser que la sucursal Norte tenga más pedidos que la sucursal Sur, o que haya habido un mayor aumento en el número de pedidos en esta sucursal? ¿O no hay diferencias entre sucursales en los pedidos?\n¿Algo más del informe te parece relevante para entender lo que está pasando?\nPor favor fundamentá bien tus respuestas, ya que planeo compartir este diagnóstico con otros miembros del equipo.\nPor último, según tu análisis, ¿qué sugerirías que hagamos para solucionar este problema?\nSaludos,\nRamiro",
    "informe_adjunto":{
      "resumen": "Resumen del problema: En las últimas semanas la sucursal Norte estuvo recibiendo bajas puntuaciones debido a demoras excesivas en el envío.",
      "grafico": "1) Número diario de pedidos en las últimas tres semanas en las sucursales Norte y Sur:\nhttps://i.imgur.com/Hy1Buun.png",
      "tabla1": "2) Información sobre los tiempos de preparación y entrega para cada una de las sucursales en las últimas dos semanas (proporcionada por la plataforma de envíos):\nSucursal Sur\nTiempo promedio de toma del pedido: 9 minutos\nTiempo promedio de preparado en el local: 18 minutos\nTiempo promedio de entrega (desde entrega al repartidor hasta entrega al cliente): 13 minutos\n Sucursal Norte\n Tiempo promedio de toma del pedido: 10 minutos\nTiempo promedio de preparado en el local: 29 minutos\nTiempo promedio de entrega (desde entrega al repartidor hasta entrega al cliente): 15 minutos",
      "tabla2": "3) Número de empleados y su antigüedad promedio en cada una de las sucursales:\\n\\n\\begin{tabular}{l cccc}\\n\\toprule\\n& \\multicolumn{2}{c}{\\textbf{Sucursal Norte}} & \\multicolumn{2}{c}{\\textbf{Sucursal Sur}} \\\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\\n& \\textbf{\\makecell{Número de \\\\ empleados}} & \\textbf{\\makecell{Antigüedad promedio \\\\ (en meses)}} & \\textbf{\\makecell{Número de \\\\ empleados}} & \\textbf{\\makecell{Antigüedad promedio \\\\ (en meses)}} \\\\\\n\\midrule\\nEmpleados en plancha & 2 & 0.5 & 2 & 4.0 \\\\\\nEmpleados en ensamblado & 4 & 12.0 & 3 & 5.0 \\\\\\nEmpleados de limpieza & 6 & 15.0 & 7 & 7.0 \\\\\\n\\midrule\\n\\textbf{Total} & \\textbf{12} & \\textbf{11.6} & \\textbf{12} & \\textbf{6.0} \\\\\\n\\bottomrule\\n\\end{tabular}"},
    "consigna": "Escribí a continuación un correo con la respuesta a Ramiro:\nPara: Ramiro González\nAsunto: Re: problema con reseñas online"
  },
  "content": {
    "diagnosis": {
      "max_points": 6,
      "questions": {
        "A1": {
          "prompt": "¿Podrías revisar si el problema viene de la plataforma de envíos?",
          "correct_answer": "Como puede verse en el informe, el tiempo promedio de toma de pedido y el tiempo promedio de entrega son casi iguales en ambas sucursales, por lo que el mal desempeño de la sucursal Norte no puede ser por un problema de la plataforma de pedidos. También se puede ver que el tiempo promedio de preparado en el local es mucho más alto en la sucursal Norte, lo que indica que el problema viene de demoras internas en la sucursal Norte.",
          "note": "**Debe mencionar** a la plataforma de envíos para recibir puntos en esta pregunta. En caso contrario debe recibir 0 puntos en esta pregunta. Aludir a la causa real del problema no alcanza para recibir un punto en este inciso. No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente. No menciona a la plataforma de envíos.",
              "example": "La sucursal Norte presenta menor tiempo promedio de preparado en el local, por lo tanto, el problema parece ser de la plataforma de envíos.",
              "explanation": "La respuesta no menciona correctamente la plataforma de envíos ni usa los datos del informe. Además, interpreta mal la evidencia: el tiempo de preparación es mayor en Norte, no menor. Esto demuestra que no responde a la pregunta y no identifica la causa real del problema."
            },
            "1": {
              "label": "Menciona la respuesta correcta y a la plataforma de envíos, pero de manera superficial.",
              "example": "Sí, la información provista sugiere que el problema no proviene de la plataforma de envíos.",
              "explanation": "Menciona la plataforma de envíos y la conclusión correcta, pero de manera superficial. No utiliza datos concretos del informe (tiempos de toma o de entrega) ni explica por qué la plataforma queda descartada como causa del problema."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada y a la plataforma de envíos, y justifica adecuadamente.",
              "example": "Sí, como puede observarse en la información adjunta, los tiempos promedio de toma y entrega del pedido son prácticamente iguales en ambas sedes. La única diferencia radica en el tiempo promedio de preparado del pedido que es superior en la sucursal Norte. Esto indica que el problema no proviene de un mal funcionamiento de la plataforma de envíos.",
              "explanation": "Usa correctamente los datos del informe para descartar la plataforma: compara los tiempos de toma y entrega entre sucursales y señala que la diferencia aparece únicamente en el tiempo de preparación en el local. La respuesta es clara, específica y basada en evidencia, lo que justifica adecuadamente la conclusión."
            }
          }
        },
        "A2": {
          "prompt": "¿Puede ser que la sucursal Norte tenga más pedidos que la sucursal Sur, o que haya habido un mayor aumento en el número de pedidos en esta sucursal? ¿O no hay diferencias entre sucursales en los pedidos?",
          "correct_answer": "Como puede verse en el gráfico, ambas sucursales tienen un número similar de pedidos. Si bien en los últimos días aumentó la cantidad de pedidos, este aumento fue similar en ambas sucursales (y el aumento hasta fue un poco menor en la Norte). Por lo tanto, esto no puede ser un causante del mal desempeño de esa sucursal.",
          "note": "**Debe mencionar** la evolución de las ventas de ambas sedes. Aludir a la causa real del problema no alcanza para recibir un punto en este inciso. Decir que los pedidos bajaron en cualquiera de las dos sucursales es incorrecto e implica una asignación de 0 puntos en este criterio. No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente",
              "example": "Sí, el gráfico muestra que hasta la semana del 21 de enero los pedidos eran muy similares en ambas sucursales. Sin embargo, a partir de esa semana se observa un aumento en los pedidos en ambas, siendo dicho incremento más marcado en la sucursal Norte.",
              "explanation": "La respuesta interpreta incorrectamente los datos: afirma que el aumento es más marcado en la sucursal Norte, lo cual contradice el gráfico. Esto implica una lectura errónea de la evidencia y lleva a una conclusión equivocada sobre el origen del problema. Por eso recibe 0 puntos."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial",
              "example": "No, por lo que se puede ver en el gráfico la cantidad de pedidos en la sucursal Norte es menor.",
              "explanation": "Menciona la conclusión correcta —que los pedidos no explican el problema— pero de forma superficial y sin describir la evolución en ambas sucursales. Además, la afirmación sobre que “Norte tiene menos pedidos” es incompleta y poco precisa respecto a los datos reales."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente",
              "example": "No, por lo que se puede ver en el gráfico adjuntado, la cantidad de pedidos es muy similar en ambas sucursales hasta la semana del 21 de enero. Luego de ello comienza un aumento de los pedidos que es más pronunciado en la sucursal Sur. Si bien existe una diferencia en el número de pedidos entre ambas sedes, esta beneficia a la sucursal Norte.",
              "explanation": "La respuesta describe detalladamente la evolución de los pedidos en ambas sucursales, usa la información del gráfico de forma precisa y explica por qué los pedidos no pueden justificar el mal desempeño de Norte. Menciona tanto el nivel como el aumento de los pedidos, cumpliendo plenamente con los requisitos del criterio."
            }
          }
        },
        "A3": {
          "prompt": "¿Algo más del informe te parece relevante para entender lo que está pasando?",
          "correct_answer": "Sí. Como puede verse en la tabla, la principal diferencia entre empleados de ambas sedes que podría estar explicando el mal funcionamiento de la sede Norte es que en la sucursal Norte, los empleados de plancha tienen menor antigüedad (0.5 meses en promedio, vs. 4 en la sucursal Sur). Esto sugiere que la mayoría del personal en plancha de Norte es nuevo y probablemente aún no está familiarizado con los procesos, lo que podría explicar las demoras en la preparación.",
          "note": "No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente.",
              "example": "Sí, las diferencias en las ventas entre ambas sedes probablemente se deban a la composición del personal. Es probable que los empleados de la sucursal Norte, perciban ingresos más bajos que los empleados de la sucursal Sur, lo que podría explicar el menor nivel de desempeño en la sucursal Norte.",
              "explanation": "La respuesta no utiliza la información relevante del informe: introduce hipótesis ajenas al problema y no se refiere a la antigüedad del personal de plancha."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial.",
              "example": "Los empleados de la sucursal Norte se encuentran menos capacitados que los empleados de la sucursal Sur.",
              "explanation": "Menciona la idea central —que el personal de la sucursal Norte tiene menos experiencia— pero de manera superficial y sin apoyarse explícitamente en los datos del informe. No hace referencia a la diferencia de antigüedad en plancha, que es el punto clave."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente.",
              "example": "La tabla de la composición de la planta de trabajadores de cada sucursal muestra que los empleados en plancha de la sucursal Norte presentan mucha menos antigüedad que los empleados en plancha de la sucursal Sur. Mientras que en la primera la antigüedad promedio de estos trabajadores es de 0.5 meses, en la segunda es de 4 meses. Esta falta de experiencia es lo que, probablemente, explica que la sucursal Norte presente tiempos de preparado mayores en promedio.",
              "explanation": "Usa de manera precisa los datos del informe: identifica que la diferencia crucial está en la antigüedad del personal de plancha, compara ambos valores y vincula esa información con los tiempos de preparado más altos en la sucursal Norte. Es una respuesta completa, clara y bien fundamentada."
            }
          }
        }
      }
    },
    "solution": {
      "max_points": 4,
      "prompt": "Las propuestas del participante pueden incluir una o varias acciones para solucionar el problema. Cada acción debe evaluarse de manera individual según los criterios B1, B2 y B3, sin elegir una 'mejor' acción dentro de la grilla. El objetivo de esta sección es definir cómo puntuar cada acción concreta en función de si aborda la causa del problema, cuán específica es y cuán realista resulta.",
      "problem_to_solve": "La sucursal Norte tarda más que la sucursal Sur en entregar los pedidos porque sus empleados en plancha presentan una menor antigüedad y, por lo tanto, tienen menos experiencia",
      "criteria": {
        "B1": {
          "description": "Para cada acción propuesta, ¿la solución propuesta lidia directamente con la causa del problema?",
          "note": "Para recibir 1 punto en este criterio, el participante debe proponer una solución que aborde explícitamente la causa del problema identificada en A3 (la menor antigüedad y falta de experiencia del personal de plancha en la sucursal Norte). Si en A3 reconoció claramente esa causa y en B1 presenta una propuesta coherente con ella, aunque no la mencione de forma explícita, puede recibir 1 punto. Si no identificó la falta de experiencia en A3 ni en B1, o propone medidas genéricas sin relación con ese diagnóstico (por ejemplo, reorganizar turnos, mejorar la plataforma o aumentar el personal sin aludir a capacitación o aprendizaje), debe recibir 0 puntos.",
          "note2": "No debe asignarse puntaje en este criterio si el participante solo identifica correctamente la causa del problema en A3 (que los empleados en plancha de la sucursal Norte tienen menos antigüedad), pero no propone una solución explícita para resolverlo en B1. Reconocer la causa no equivale a ofrecer una medida correctiva. La propuesta debe indicar de manera clara qué acción concreta se tomaría para abordar esa falta de experiencia o mejorar el desempeño del personal. No se debe otorgar puntaje en B1 por diagnóstico correcto en A3, ni por alusiones generales a la causa del problema en B1.",
          "scores": {
            "0": {
              "label": "No",
              "example": "Deberíamos reducir la cantidad de empleados en ensamblado de la sucursal Norte, ya que el exceso de éstos está entorpeciendo la producción.",
              "explanation": "La propuesta no aborda la causa del problema: no menciona la falta de experiencia del personal de plancha ni propone una acción relacionada con su desempeño. En cambio, introduce un nuevo diagnóstico no respaldado por el informe (un supuesto “exceso” de personal en ensamblado). Por lo tanto, no lidia directamente con la causa real del problema."
            },
            "1": {
              "label": "Sí",
              "example": "Deberíamos capacitar a los empleados de la sucursal Norte para compensar su falta de experiencia.",
              "explanation": "La solución propuesta aborda explícitamente la causa del problema: la falta de experiencia del personal de plancha."
            }
          }
        },
        "B2": {
          "description": "Para cada acción propuesta, ¿es una acción concreta/específica?",
          "note": "Este criterio evalúa el grado de concreción y detalle de la propuesta. Es decir, cuán claramente se entiende qué acción se propone. Para obtener 2 puntos, la propuesta debe describir una acción definida, aplicable al contexto del local, y dejar claro qué se haría y con qué objetivo. Si se mencionan varias opciones sin desarrollo, si las acciones son vagas (por ejemplo, 'capacitar', 'hablar con el equipo', 'mejorar la organización'), corresponde 1 punto o menos.",
          "scores": {
            "0": {
              "label": "Propuesta demasiado general o abstracta: no se entiende bien qué acción concreta se propone.",
              "example": "Hablar con los empleados en plancha para ver qué está pasando.",
              "explanation": "La propuesta es demasiado vaga: no especifica qué se haría, cómo se abordaría el problema ni qué tipo de acción concreta se implementaría. No describe un plan operativo y no permite inferir una solución aplicable dentro del local."
            },
            "1": {
              "label": "Propuesta con cierta especificidad, pero sin suficiente detalle operativo o contextual.",
              "example": "Capacitar a los empleados en plancha de la sucursal Norte. Se mencionan acciones posibles pero sin explicar cómo se implementarían.",
              "explanation": "La propuesta avanza hacia la solución correcta —capacitarlos— pero sigue siendo general y sin detalles. No aclara qué tipo de capacitación, quién la dará, ni de qué forma ayudaría a reducir los tiempos de preparación. La especificidad es insuficiente para alcanzar el puntaje máximo."
            },
            "2": {
              "label": "Propuesta clara y específica dentro del contexto de la empresa: se entiende qué acción se propone y cómo podría implementarse en términos generales. No es necesario que la propuesta incluya plazos, métricas o formatos de implementación, pero sí debe describir de forma directa una medida concreta.",
              "example": "Organizar una capacitación práctica en la sucursal Norte, guiada por el encargado de plancha de la sucursal Sur, para que los nuevos empleados aprendan los procedimientos y reduzcan los tiempos de preparación.",
              "explanation": "La propuesta es clara y específica: indica qué se hará (capacitación práctica), quién la llevará a cabo (el encargado de plancha de Sur) y con qué objetivo (reducir los tiempos de preparación). Es realista, aplicable y suficientemente detallada para entender la acción sin ambigüedades."
            }
          }
        },
        "B3": {
          "description": "Para cada acción propuesta, ¿es una acción realista?",
          "note": "Debe considerarse realista una propuesta en la que el participante sugiera reemplazar a empleados con poca experiencia por otros más experimentados, siempre que esto implique un recambio de personal y no una duplicación de puestos. En cambio, no debe considerarse realista una solución que consista simplemente en contratar empleados experimentados adicionales. En síntesis: 'despedir y reemplazar' puede ser realista, pero 'sumar más empleados' no.",
          "scores": {
            "0": {
              "label": "No",
              "example1": "Podríamos trasladar temporalmente a todos los empleados de plancha más experimentados de la sucursal Sur a la sucursal Norte.",
              "explanation1": "No es realista porque implicaría desarmar completamente la operación de plancha de la sucursal Sur, dejando a esa sede sin personal clave. Genera un problema mayor en la otra sucursal y no es una medida operativamente viable.",
              "example2": "Podríamos contratar más empleados experimentados",
              "explanation2": "No es realista según los criterios del ejercicio: esta propuesta implica sumar personal adicional, lo cual no resuelve el problema de experiencia del equipo actual y contradice la regla explícita del criterio (no se considera realista contratar más empleados experimentados adicionales). La solución no aborda el problema estructural del equipo de plancha existente."
            },
            "1": {
              "label": "Sí",
              "example": "Podríamos trasladar temporalmente a un empleado de plancha de la sucursal Sur a la sucursal Norte para que capacite a los empleados de plancha de la sucursal Norte.",
              "explanation": "Es una propuesta realista porque plantea una medida factible: trasladar temporalmente a un solo empleado experimentado sin afectar de manera crítica la operación de la sucursal Sur. No implica duplicar personal, y está alineada con la necesidad de mejorar la experiencia del equipo de plancha de Norte."
            }
          }
        }
      }
    },
    "total_max_points": 10
  },
  "writing": {
    "total_max_points": 10,
    "criteria": {
      "1": {
        "name": "Ortografía y gramática",
        "description": "Se evalúa la corrección ortográfica y gramatical del texto, incluyendo el uso adecuado de tildes, signos de puntuación, concordancia verbal y nominal, y mayúsculas. Se valora especialmente la redacción clara, fluida y cuidada, con frases bien estructuradas y sin errores que afecten la calidad o el tono profesional del mensaje.",
        "note": "No se considera error el uso de solo signos de cierre (¿? / ¡!)",
        "scores": {
          "0": {
            "label": "Errores graves o numerosos: el texto presenta múltiples errores ortográficos o gramaticales (tildes, concordancia, puntuación o mayúsculas) que se repiten a lo largo del texto. Estos errores afectan la claridad o dan una impresión de descuido, incluso si el texto se entiende en general.",
            "example1": "hola Ramiro, revice los informes que me enviaste. No hay problema con la plataforma de envios y la Sucursal Norte tampoco tiene mas pedidos que la Sur. Identifique que los empleados de pplancha son nuevos y demoran mucho. Una figura presente como supervisor puede mejorar la efectivdad del local, sin duda esto hara que se eleven las vtas, saludos.",
            "explanation1": "Presenta múltiples errores graves de ortografía (revice, envios, mas, Identifique, pplancha, efectivdad, hara, vtas), problemas de mayúsculas y fallas de concordancia. Los errores son frecuentes y afectan al tono profesional del texto.",
            "example2": "buenos dias ramiro te escrivo por que estube revisando los informes y me pareseria que el problema esta en la falta de compromiso de los empleados de la sucursal norte ya que no estan cumpliendo con los tiempos de entrega como deberian por eso pienso que lo mejor seria aser una reunion para ablar con ellos y ver si se puede mejorar el rendiminto general.",
            "explanation2": "Incluye numerosos errores ortográficos sistemáticos (dias, escrivo, estube, pareseria, estan, deberian, aser, ablar, rendiminto), además de falta de mayúsculas, ausencia de puntuación y oraciones excesivamente largas. Estos errores dificultan la lectura y evidencian descuido."
          },
          "1": {
            "label": "Algunos errores o descuidos menores, pero perceptibles: se observan varios errores dispersos (tildes omitidas, puntuación inadecuada, uso impreciso de conectores o ligeras fallas de concordancia). No impiden la comprensión, pero restan fluidez o profesionalismo al texto.",
            "example1": "buen día luis,\nsegún los datos que revisé, las ventas de la sede norte bajaron un poco en julio pero se mantuvieron estables el resto del año. puede ser que los empleados eligieran comer afuera esos días o que el menú no fuera tan variado. sería bueno revisar eso para los próximos meses.\nsaludos",
            "explanation1": "Contiene varios errores menores: falta de mayúsculas en nombres propios y al inicio de oraciones, y puntuación mejorable. Aunque es comprensible, la redacción pierde prolijidad y no alcanza un registro profesional impecable.",
            "example2": "los empleados de la sucursal norte tienen poca experiencia en plancha y eso genera demoras. tambien podria ser que no esten bien organizados, porque hay varios con experiencia pero no aprovechan el tiempo. no parece haber un encargado que los controle ni que marque el ritmo de trabajo.",
            "explanation2": "El texto omite tildes (tambien, esten), no usa mayúsculas al inicio de frases y presenta alguna repetición conceptual. Los errores no impiden la comprensión, pero reducen la fluidez y el nivel profesional del mensaje."
          },
          "2": {
            "label": "Redacción impecable o casi impecable: el texto está cuidadosamente escrito, sin errores ortográficos ni gramaticales perceptibles. La puntuación es precisa, las oraciones están bien estructuradas y el registro es fluido y natural. A lo sumo puede haber un error aislado que no afecta en absoluto la calidad del texto.",
            "example1": "Buen día Ramiro, ¿cómo estás?\nMirando los datos, me di cuenta de que los tiempos de entrega son parecidos en ambas sucursales, pero en la Norte la preparación demora más. Es probable que eso se deba a la menor experiencia del personal en plancha y ensamblado.\nSería útil reforzar la capacitación y, si se puede, enviar apoyo temporal desde la Sur para equilibrar los tiempos.\nSaludos,",
            "explanation1": "No presenta errores ortográficos ni gramaticales. Las oraciones están bien puntuadas, la redacción es fluida y el registro es profesional. Es un ejemplo de escritura clara y cuidada.",
            "example2": "¿Qué tal Ramiro?\nCon respecto al problema que mencionás, los empleados en plancha trabajan hace muy poco tiempo en el local, pero con un poco de entrenamiento estarán a la par de los empleados del local Sur. Habría que conversar con ellos para alentarlos a mejorar en ese aspecto y así lograr mejores calificaciones.\nEspero que mi aporte sea útil.\nSaludos cordiales!",
            "explanation2": "El texto está correctamente escrito, con buena estructura, sin errores evidentes y con un tono adecuado. La puntuación es clara y el mensaje fluye de manera natural. Puede haber ligeras variaciones estilísticas, pero no afectan la calidad general."
          }
        }
      },
      "2": {
        "name": "Claridad y legibilidad",
        "description": "Se evalúa la claridad, precisión y fluidez del texto, **dentro del contexto del mail del jefe y de la consigna**. Las ideas deben expresarse de manera directa, ordenada y sin ambigüedades, y deben permitir que el jefe comprenda la respuesta a partir de la información del informe. Se valoran las oraciones bien construidas, la coherencia entre frases y la ausencia de repeticiones o redundancias. El texto se entiende fácilmente y transmite las ideas con naturalidad y economía de palabras.  Un texto es poco claro no solo cuando está mal escrito, sino también cuando, aunque sea breve o gramaticalmente correcto, **no desarrolla las ideas necesarias para responder lo que pide el jefe**, o resulta tan general que el jefe no entendería el mensaje.",
        "note": "La repetición de ideas **debe penalizarse**. Los textos que no desarrollan las ideas mínimamente necesarias para que el jefe entienda la respuesta **en el contexto de su mail** también deben penalizarse. Un texto puede estar bien escrito a nivel lingüístico pero ser confuso o inútil si no permite comprender la respuesta requerida.",
        "scores": {
          "0": {
            "label": "Texto confuso o desorganizado: el texto resulta difícil de comprender por errores de construcción o frases inconexas. Presenta repeticiones de ideas innecesarias o ambigüedades que impiden seguir el hilo argumental con claridad.",
            "example1": "Hola Ramiro lo que pasó fue que las ventas bajaron porque no se vendió tanto como antes y también porque se tardó en entregar los pedidos y los clientes se quejaron por eso y después ya no quisieron comprar más y capaz también porque no había stock pero no estoy seguro igual creo que eso influyó bastante.",
            "explanation1": "El texto es confuso, con una oración extremadamente larga, ideas mezcladas sin orden y afirmaciones poco precisas. Hay repeticiones (“ventas bajaron”, “no quisieron comprar más”) y contradicciones con el informe (no hay problemas de stock). La falta de estructura dificulta seguir el mensaje.",
            "example2": "Hola Ramiro, estuve revisando lo de la sucursal norte y me parece que el problema principal está en los tiempos de preparación, porque si los pedidos tardan más en salir, los clientes se cansan de esperar y eso termina afectando las ventas.\nAdemás, creo que el problema puede venir por los tiempos, ya que cuando los pedidos se demoran los clientes no quieren esperar tanto, y al final eso hace que bajen las ventas porque los pedidos no salen a tiempo.",
            "explanation2": "Hay repetición explícita de ideas (“problema en los tiempos”, “cuando se demoran los clientes se cansan”, “bajan las ventas porque no salen a tiempo”), lo que genera redundancia. La frase es circular y no aporta información nueva. Esto afecta la claridad y rompe la fluidez de lectura.",
            "example3": "Tienen menos antigüedad. Saludos,",
            "explanation3": "Aunque está escrito de manera clara y sin errores, **no dice nada útil para el jefe**: no desarrolla la idea, no usa datos del informe y no responde ninguna de las preguntas. Por tanto, debe recibir 0 puntos."          
          },
          "1": {
            "label": "Claridad limitada: se identifican varias frases confusas, mal estructuradas o redundantes. La lectura requiere esfuerzo y el mensaje no fluye naturalmente. Las ideas aparecen sin una secuencia lógica o con expresiones poco precisas.",
            "example1": "Estimado, revisando los datos que me enviaste noto que la sucursal norte presenta demoras importantes en el armado de los pedidos, esto puede deberse a una falta de organización en la cocina ya que si bien hay más personal que en la sur los tiempos son mayores, lo cual no debería pasar, de todas maneras voy a hablar con los encargados para ver si hay algún inconveniente en el proceso o si es un tema de coordinación entre los empleados.",
            "explanation1": "El texto tiene oraciones demasiado largas, mezcla diagnóstico con hipótesis sin orden, y presenta saltos argumentales. La estructura interna es confusa y la lectura exige esfuerzo. Aunque se entiende la idea central, la redacción es poco clara.",
            "example2": "Según lo que pude observar, el inconveniente parece estar en la sucursal norte porque los pedidos se demoran más que en la sur, y eso hace que los clientes esperen demasiado y dejen de comprar, también puede ser que los empleados estén algo desmotivados o cansados por la cantidad de trabajo, ya que hace varios meses que no se hacen cambios en los turnos ni mejoras en las condiciones, lo cual podría estar afectando el rendimiento general y provocando que los tiempos sean más largos de lo habitual.",
            "explanation2": "Presenta oraciones extensas y contiene ideas agregadas sin una secuencia clara. Hay afirmaciones imprecisas y no apoyadas en el informe (“desmotivados”, “condiciones laborales”). La falta de foco afecta la claridad general.",
            "example3": "Hola Ramiro, parece ser un problema en los tiempos de preparación, pero me tendría que fijar bien. Saludos,",
            "explanation3": "Responde algo, pero de forma superficial y sin desarrollar. No quedaría claro para el jefe cuál es el diagnóstico o cuáles son las posibles soluciones."
          },
          "2": {
            "label": "Claridad aceptable pero mejorable: el texto se comprende en general, aunque contiene algunas oraciones extensas, o formulaciones poco naturales que interrumpen la fluidez. Puede haber alguna repetición de ideas. Requiere algo de esfuerzo para seguir el hilo.",
            "example1": "Estimado, luego de revisar los indicadores, observo que la sucursal Norte presenta demoras en el tiempo de preparación, posiblemente vinculadas a una menor coordinación entre los sectores, sería conveniente evaluar una redistribución de tareas o realizar rotaciones internas para equilibrar la carga laboral entre plancha y ensamblado. También podríamos implementar un esquema de incentivos para reforzar la productividad, aunque antes sería necesario analizar si las demoras se deben a la falta de experiencia o a cuestiones de organización interna.\nEn general, el problema no parece provenir de la plataforma de envíos, sino del funcionamiento operativo dentro del local, lo cual podría resolverse con ajustes menores en la asignación de personal y una comunicación más fluida entre los equipos.",
            "explanation1": "El texto es comprensible, pero tiene oraciones largas y transiciones poco naturales. Hay cierta repetición (redistribución de tareas / organización interna) y mezcla de propuestas con diagnóstico. La claridad es buena, pero no sobresaliente.",
            "example2": "Buenos días, Ramiro:\nRevisando los datos del último informe noto que la sucursal norte tiene un tiempo promedio de preparación considerablemente mayor que la sur, y aunque la diferencia no parece muy grande cuando se observa día por día, al analizar la tendencia semanal se evidencia un aumento constante que podría estar generando demoras acumuladas en la entrega y afectando la satisfacción de los clientes, sobre todo en los horarios pico donde el volumen de pedidos es más alto.\nCreo que sería útil evaluar si este retraso está relacionado con la falta de experiencia del personal o con una mala distribución de tareas dentro del local, y en función de eso definir si conviene capacitar al equipo actual o sumar refuerzos en los turnos de mayor demanda.\nSaludos",
            "explanation2": "La redacción es clara, pero hay oraciones demasiado largas y densas que dificultan la lectura. La idea principal se entiende, pero requiere más esfuerzo del necesario, por lo que no alcanza el nivel máximo de fluidez."
          },
          "3": {
            "label": "Claridad y legibilidad destacadas: el texto es muy claro y fluido. Las oraciones están bien construidas, no hay ambigüedades, o repetición de ideas. Se lee con naturalidad.",
            "example1": "Buenas tardes, Ramiro:\nQuería disculparme por los inconvenientes en los tiempos de entrega registrados durante los últimos días. Luego de revisar el proceso, detectamos que el retraso proviene de la adaptación del nuevo empleado en el área de ensamblado. Estamos acompañando su capacitación para que alcance el ritmo del resto del equipo y confiamos en que los tiempos se normalicen en breve.\nSaludos cordiales",
            "explanation1": "La redacción es clara, directa y sin repeticiones. Las ideas están bien ordenadas y cada frase aporta información nueva. El texto fluye de manera natural y es fácil de leer.",
            "example2": "Ramiro:\nEl tiempo promedio de preparación en la sucursal Norte es de 29 minutos, frente a 18 en la Sur. Esa diferencia de 11 minutos explica las demoras percibidas por los clientes, ya que el tiempo de entrega es prácticamente igual en ambas.\nEl problema parece estar en la organización interna del local, no en la plataforma de envíos. Sugiero capacitar al personal de plancha y revisar la distribución de tareas para equilibrar los tiempos entre sucursales.\nSaludos,",
            "explanation2": "El texto es muy claro y ordenado: explica el problema con precisión, evita redundancias y presenta las ideas de forma secuencial y fluida. No hay ambigüedades ni repeticiones. La lectura es natural y profesional."
          }
        }
      },
      "3": {
        "name": "Organización del texto",
        "description": "Se evalúa la estructura y el orden interno del texto. Debe seguir una secuencia lógica que incluya:\n1. una introducción que enmarque el mensaje o un saludo (por ejemplo, 'Hola XX, cómo estás?' o una breve referencia al mail del jefe),\nEjemplo de referencia al mail del jefe: “Revisé los datos que me enviaste y encontré lo siguiente:”\n2. un desarrollo en el que se respondan las preguntas planteadas,\n3. una sección con propuestas o sugerencias para resolver el problema, y\n4. un cierre que retome las ideas principales o una despedida.\nEjemplos de cierre o saludo:\n1.“Estoy a disposición para discutir cómo implementar las mejoras.”\n2.'Saludos,'\nTambién se valora la organización interna dentro de cada sección: el uso adecuado de párrafos, la coherencia en la secuencia de ideas y la ausencia de saltos temáticos.",
        "note": "Tanto un saludo como una referencia al mail del jefe cuentan como introducción, y tanto una despedida como un cierre que retome la ideas principales o que diga 'Quedo a disposición' cuentan como cierre.",
        "scores": {
          "0": {
            "label": "Texto desorganizado o sin estructura reconocible: no se distinguen las secciones principales o las ideas aparecen mezcladas y repetidas. Falta orden tanto en la estructura general como dentro de los párrafos.",
            "example": "estuve viendo los datos y me parece que algo anda mal con los tiempos, porque hay empleados que trabajan más y otros menos, aunque eso también depende de si viven cerca o si tienen más experiencia, igual habría que ver si no es por los turnos o por cómo se reparten las tareas, porque capaz no todos hacen lo mismo, y si encima hay menos personal los días de más pedidos, eso también influye, por eso no sé si conviene cambiar los horarios o revisar las planillas.",
            "explanation": "No hay estructura reconocible. El texto mezcla diagnósticos, hipótesis, suposiciones y soluciones en una sola oración larguísima. No existe introducción, desarrollo ni cierre; tampoco se distinguen párrafos. Las ideas aparecen desordenadas y repetidas, lo que impide seguir un hilo lógico."
          },
          "1": {
            "label": "Estructura débil o confusa: se percibe cierta intención de organización, pero faltan secciones o están mal delimitadas. Dentro de cada parte hay mezcla de ideas o saltos que dificultan la lectura. Los párrafos no agrupan bien las ideas.",
            "example": "Hola, estuve mirando los datos y vi que la sucursal Sur entrega más rápido que la Norte, puede ser por cómo se organizan los turnos o por la cantidad de personal, habría que revisar eso porque quizás no se están distribuyendo bien las tareas.",
            "explanation": "El texto muestra una intención mínima de organización (introducción + diagnóstico parcial), pero está incompleto: no tiene propuestas claras ni cierre. Además, dentro del único párrafo hay saltos temáticos y mezcla de causas sin orden, lo que dificulta la lectura."
          },
          "2": {
            "label": "Organización parcial o irregular: el texto incluye la mayoría de las secciones, pero el orden o la articulación entre ellas es poco clara. Algunas partes están bien organizadas, mientras que otras presentan saltos. Los párrafos son comprensibles pero desbalanceados.",
            "example": "Ramiro, buenas tardes.\nTe comento lo que encontré en la información que me enviaste.\nPor lo que veo los retrasos se concentran sobre todo en el turno tarde. Recomiendo:\nReasignar parte del personal del turno mañana para equilibrar la carga. Revisar si la demora se debe a un cuello de botella en empaquetado.\nImplementar un control diario de tiempos hasta normalizar la operación.\nSaludos,",
            "explanation": "Incluye introducción y propuestas, pero el orden interno es irregular. Las ideas aparecen parcialmente organizadas, pero hay saltos entre diagnóstico y propuestas dentro del mismo bloque. La estructura está presente, pero es débil o incompleta."
          },
          "3": {
            "label": "Organización clara y coherente: el texto sigue la secuencia esperada (introducción, respuestas, propuestas, cierre) y las ideas dentro de cada sección están bien agrupadas. Hay un uso adecuado de párrafos, aunque las transiciones o la progresión de ideas podrían ser más fluidas.",
            "example": "Estimado Ramiro,\nRevisé los reportes de la última semana y detecté que la mayor parte de las demoras proviene del tiempo de preparación en el local. En la sucursal Norte, el promedio es de 28 minutos, frente a 17 en la Sur.\nEl tiempo de entrega por parte de los repartidores es similar entre ambas sucursales, por lo que el problema no parece estar en la plataforma de envíos. Tampoco se observa una diferencia importante en el volumen de pedidos.\nUna posible explicación es la falta de experiencia del personal de plancha, ya que varios empleados se incorporaron recientemente. Esto podría estar generando un cuello de botella en la etapa de preparación.\nSería conveniente reforzar la capacitación y acompañar a los nuevos empleados hasta que se estabilice el rendimiento.\nSaludos,",
            "explanation": "El texto sigue la estructura general esperada: presenta un saludo inicial, desarrolla un diagnóstico ordenado (comparando tiempos de preparación, entrega y volumen de pedidos), propone una medida concreta y cierra de manera adecuada. Las ideas están agrupadas por tema y el hilo lógico se comprende sin dificultad. Sin embargo, dentro del segundo bloque aparece cierta mezcla de contenidos —se habla en un mismo párrafo de plataforma, pedidos y antigüedad del personal— lo que podría separarse en dos párrafos para mejorar la claridad. Aun así, la organización global es coherente y cumple con la secuencia introducción → diagnóstico → propuesta → cierre."
          },
          "4": {
            "label": "Organización excelente: el texto presenta una estructura completa y equilibrada: cada sección cumple su función, las ideas dentro de cada una están ordenadas, y las transiciones entre párrafos son naturales. La organización general y la interna contribuyen a una lectura fluida y lógica.",
            "example": "Estimados,\nEstuve revisando los datos que me enviaron sobre las recientes demoras en la sucursal Norte y preparé un breve análisis con las principales conclusiones y propuestas de mejora.\nLas demoras registradas se explican principalmente por el tiempo de preparación en el local, que promedia 28 minutos frente a 17 en la sucursal Sur. El tiempo de entrega por parte de los repartidores es muy similar entre ambas sucursales, por lo que el problema no parece estar en la plataforma de envíos. Tampoco se detectan diferencias relevantes en el volumen de pedidos.\nLa causa más probable está en la menor experiencia del personal de plancha: varios empleados se incorporaron recientemente, lo que podría estar afectando la eficiencia y generando un cuello de botella en la preparación.\nRecomiendo implementar un plan de capacitación y acompañamiento para el nuevo personal, así como un monitoreo semanal de los tiempos de preparación para verificar las mejoras. Con estas medidas, deberíamos poder reducir las demoras y recuperar los niveles de servicio habituales.\nQuedo a disposición para coordinar los próximos pasos o ampliar el análisis si lo consideran necesario.\nSaludos cordiales,",
            "explanation": "Presenta una estructura completa y equilibrada: introducción contextualizada, análisis ordenado y secuencial, propuestas claras y un cierre formal. Cada párrafo cumple una función clara y las ideas están agrupadas temáticamente. Las transiciones son naturales y la lectura es fluida. Es un ejemplo de organización impecable."
          }
        }
      },
      "4": {
        "name": "Registro adecuado",
        "description": "Se evalúa si el tono del mail es apropiado para el contexto laboral y coherente con el tono del mail del jefe. El tono no debe ser excesivamente informal, debe ser cortes y profesional.\nEl criterio penaliza automáticamente (0 puntos) los casos en los que:\n1.El texto esté completamente escrito en mayúsculas (por considerarse una forma inapropiada o agresiva de comunicación).\n2. El texto incluya rastros evidentes de generación automática o placeholders propios de un asistente virtual, como firmas incompletas del tipo “[tu nombre]”, o texto no reemplazado.",
        "note1": "En este criterio no se evalúa la presencia o la falta de saludo y despedida",
        "note2": "Mencionar explícitamente que se utilizó una herramienta de IA para elaborar el diagnóstico **no se penaliza**",
        "scores": {
          "0": {
            "label": "El tono del mail es demasiado informal, coloquial o poco cortés en relación con el tono del mail del jefe. También se asigna 0 puntos si el texto está completamente en mayúsculas, si deja evidencia explícita de interacción con ChatGPT u otra IA, o si el texto no presenta un tono profesional acorde al mail del jefe.",
            "example1": "Buenas,\nEstuve mirando los datos y vi que la sucursal Sur entrega más rápido que la Norte, puede ser por cómo se organizan los turnos o por la cantidad de personal, habría que revisar eso porque quizás no se están distribuyendo bien las tareas.\nAbrazo,",
            "explanation1": "El tono es excesivamente informal para un intercambio laboral: usa saludos coloquiales (“Buenas”, “Abrazo”). No mantiene la formalidad esperable en el contexto definido por el mail del jefe.",
            "example2": "Hola Ramiro, ¿cómo estás?\nEstuve mirando los datos y vi que la sucursal Sur entrega más rápido que la Norte, puede ser por cómo se organizan los turnos o por la cantidad de personal, habría que revisar eso porque quizás no se están distribuyendo bien las tareas.\nSaludos cordiales,\n[Tu nombre]",
            "explanation2": "Incluye un placeholder típico de un asistente virtual ('[tu nombre]'), lo cual activa la penalización automática.",
            "example3": "HOLA RAMIRO, ¿CÓMO ESTÁS?\nESTUVE MIRANDO LOS DATOS Y VI QUE LA SUCURSAL SUR ENTREGA MÁS RÁPIDO QUE LA NORTE, PUEDE SER POR CÓMO SE ORGANIZAN LOS TURNOS O POR LA CANTIDAD DE PERSONAL, HABRÍA QUE REVISAR ESO PORQUE QUIZÁS NO SE ESTÁN DISTRIBUYENDO BIEN LAS TAREAS.\nSALUDOS CORDIALES,",
            "explanation3": "El texto está completamente en mayúsculas, lo cual se considera un tono inadecuado o agresivo en comunicación escrita. Esto activa automáticamente el puntaje 0, independientemente del contenido."          
          },
          "1": {
            "label": "Registro adecuado: el tono es respetuoso y coherente acorde con el tono del mail del jefe. El texto mantiene un registro profesional y apropiado para el contexto laboral.",
            "example": "Hola Ramiro, ¿cómo estás?\nEstuve mirando los datos y vi que la sucursal Sur entrega más rápido que la Norte, puede ser por cómo se organizan los turnos o por la cantidad de personal, habría que revisar eso porque quizás no se están distribuyendo bien las tareas.\nSaludos cordiales,",
            "explanation": "El tono es respetuoso, profesional y consistente con el mail del jefe. Aunque el estilo es sencillo e informal en algunos lugares, se mantiene dentro de un registro cortés y adecuado para el contexto laboral, sin señales de IA ni marcas impropias."
          }
        }
      }
    }
  }
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/task/rest_task_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/task/rest_task_guides.json`。

### 6. sales_task_guides.json

需要提供：依原檔 placeholders 提供受試者答案、task、rubric 或對話紀錄。

用途：評分規準。原文範圍：完整作者原檔，西班牙文／英文保持原樣；GPL-3.0。

```json
{ 
  "task_context": {
    "description": "Trabajás en un negocio en Argentina de venta online de electrodomésticos importados. En enero de 2025, el dueño del negocio te envía el siguiente correo electrónico:",
    "email_from_boss": "De: Luis González <lgonzalez@gmail.com>\nAsunto: problema con ventas de estufas y ventiladores\nBuen día,\nEspero que estés bien. Te escribo porque estuve revisando las ventas de nuestros productos y noté algo raro con las estufas y ventiladores portátiles. Históricamente, nuestras ventas de ventiladores aumentan en verano y las de estufas en invierno. Sin embargo, en 2024 esto no ocurrió. ¿Podrías ayudarme a entender lo que está pasando?\nAdjunto un informe que preparó mi asistente para ayudarnos a entender mejor la situación. A partir de los datos de este informe, me gustaría que me compartas tu mirada sobre los siguientes puntos:\nPara entender si este problema es específico a estos dos productos, ¿te fijarías si en 2024 las ventas de aires acondicionados fueron diferentes a lo normal?\nMi asistente mencionó que el año pasado hubo trabas a la importación de ciertos productos electrónicos. ¿Te fijarías si esto podría tener algo que ver?\n¿Algo más del informe te parece relevante para entender lo que está pasando?\nPor favor fundamentá bien tus respuestas, ya que planeo compartir este diagnóstico con otros miembros del equipo.\nPor último, según tu análisis, ¿qué sugerirías que hagamos para solucionar este problema?\nQuedo atento a tu respuesta.\nSaludos,\nLuis",
    "informe_adjunto":{
      "resumen": "Resumen del problema: Históricamente, nuestras ventas de ventiladores aumentan en verano y las de estufas en invierno. Sin embargo, en 2024 esto no ocurrió.",
      "grafico": "1) Evolución de las ventas de aires acondicionados, estufas y ventiladores portátiles durante los últimos dos años:\nhttps://i.imgur.com/3yY4hC8.png",
      "tabla1": "2) La tabla a continuación indica, para cada producto, el número de unidades pedidas al importador y entregadas por el mismo para cada semestre en 2023 y 2024.\\n\\n\\begin{tabular}{l cc cc cc}\\n\\toprule\\n& \\multicolumn{2}{c}{\\textbf{Aires acondicionados}} & \\multicolumn{2}{c}{\\textbf{Estufas portátiles}} & \\multicolumn{2}{c}{\\textbf{Ventiladores portátiles}} \\\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\\n\\textbf{Período} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{pedidas}} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{entregadas}} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{pedidas}} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{entregadas}} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{pedidas}} &\\n\\makecell[c]{\\textbf{Unidades}\\\\\\textbf{entregadas}} \\\\\\n\\midrule\\nEne-Jun 2023 & 742 & 741 & 2,172 & 2,172 & 2,145 & 2,145 \\\\\\nJul-Dic 2023 & 494 & 494 & 2,125 & 2,127 & 2,175 & 2,175 \\\\\\nEne-Jun 2024 & 687 & 644 & 2,182 & 2,183 & 2,130 & 2,131 \\\\\\nJul-Dic 2024 & 688 & 619 & 2,125 & 2,126 & 2,150 & 2,150 \\\\\\n\\bottomrule\\n\\end{tabular}",
      "tabla2": "3) Cada trimestre enviamos un correo electrónico a nuestra base de clientes publicitando ciertos productos. A continuación, se indica qué productos fueron incluidos en este correo en los últimos dos años:\nMar 2023: Ventilador portátil, televisor, aire acondicionado.\nAbr - Jun 2023: Heladera, lavarropas, microondas, estufa portátil.\nJul - Sep 2023: Estufa portátil, caloventor, lavavajillas.\nOct - Dic 2023: Computadora, televisor, aire acondicionado, ventilador portátil.\nEne - Mar 2024: Pava eléctrica, aire acondicionado, estufa portátil.\nAbr - Jun 2024: Televisor, computadora, ventilador portátil, microondas.\nJul - Sep 2024: Lavavajillas, lavarropas, horno eléctrico.\nOct - Dic 2024: Aire acondicionado, televisor, caloventor."},
    "consigna": "Escribí a continuación un correo con la respuesta a Luis:\nPara: Luis González\nAsunto: Re: problema con ventas de estufas y ventiladores."
  },
  "content": {
    "diagnosis": {
      "max_points": 6,
      "questions": {
        "A1": {
          "prompt": "Para entender si este problema es específico a estos dos productos, ¿te fijarías si en 2024 las ventas de aires acondicionados fueron diferentes a lo normal?",
          "correct_answer": "Como puede verse en el gráfico, en 2024, las ventas de aire acondicionado siguieron el mismo patrón estacional que 2023. En particular, las ventas fueron mayores en los meses de verano, y menores en los meses de invierno. Por lo tanto, el problema es específico a estos dos productos (ventiladores portátiles y estufas portátiles).",
          "note": "Debe mencionar la evolución de las ventas de los aires acondicionados para recibir puntos en esta pregunta. En caso contrario debe recibir 0 puntos en esta pregunta. Aludir a la causa real del problema no alcanza para recibir un punto en este inciso. No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente.",
              "example": "La venta de aires acondicionados siguió un patrón estacional en 2023, pero se mantuvo constante en 2024.",
              "explanation": "No responde correctamente porque afirma un patrón inexistente en los datos: inventa que 2024 fue “constante” y no reconoce que la estacionalidad se mantiene. Además, no establece si el problema es específico a los otros productos."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial.",
              "example": "La venta de aires acondicionados en 2023 no fue diferente a la de 2024.",
              "explanation": "Menciona la idea central —que 2024 no difiere de 2023— pero de forma superficial. No describe el patrón estacional ni hace referencia explícita a los datos provistos."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente.",
              "example": "De acuerdo al gráfico provisto en el informe, tanto en 2023 como en 2024 la venta de aires acondicionados siguió un patrón estacional, aumentando en verano y cayendo en invierno.",
              "explanation": "Responde de forma completa porque describe correctamente la evolución de las ventas en ambos años, utiliza explícitamente la información del gráfico y explica el patrón estacional. La justificación es precisa y se basa en los datos provistos."
            }
          }
        },
        "A2": {
          "prompt": "Mi asistente mencionó que el año pasado hubo trabas a la importación de ciertos productos electrónicos. ¿Te fijarías si esto podría tener algo que ver?",
          "correct_answer": "Como puede verse en las tablas, no hubo faltantes en la entrega de ventiladores portátiles o estufas portátiles el año pasado. Las unidades entregadas fueron iguales o mayores que las unidades pedidas. Por lo tanto, las trabas a la importación no son una explicación para el problema que se observa.",
          "note": "Debe mencionar pedidos, entregas, stock de producto o aspectos similares para que su puntaje en esta pregunta no sea 0. Aludir a la causa real del problema no alcanza para recibir un punto en este inciso. Si responde que la causa del problema son las importaciones debe recibir 0 puntos en este inciso. No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente",
              "example": "Sí, las trabas a las importaciones impidieron que tengamos suficiente stock para enfrentar los períodos con picos de demanda.",
              "explanation": "Responde incorrectamente porque afirma que hubo problemas de stock cuando los datos muestran lo contrario. No usa información del informe y atribuye el problema a las importaciones, lo cual contradice la evidencia."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial",
              "example": "En 2023 y 2024 no tuvimos problemas con las unidades pedidas y entregadas de estufas y ventiladores portátiles.",
              "explanation": "Menciona la idea central —que no hubo problemas entre pedidos y entregas— pero de modo superficial. No utiliza detalles del informe ni explica por qué esto descarta las trabas a la importación como causa del problema."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente",
              "example": "No parece haber habido grandes trabas a la importación: la cantidad de productos pedidos y entregados se mantuvo prácticamente igual a lo largo de los distintos períodos. Salvo en algunos momentos puntuales en el caso de los aires acondicionados, las unidades entregadas fueron siempre iguales o superiores a las unidades solicitadas.",
              "explanation": "Responde de manera completa porque usa información detallada de las tablas, compara pedidos y entregas y explica por qué esto descarta faltantes. Justifica correctamente la conclusión incorporando los datos del informe."
            }
          }
        },
        "A3": {
          "prompt": "¿Algo más del informe te parece relevante para entender lo que está pasando?",
          "correct_answer": "Sí. Como puede verse en el informe, los ventiladores portátiles fueron promocionados en los meses de mayor demanda en 2023 (ene-mar y oct-dic), mientras que en 2024 fueron promocionados sólo en abril-junio. Análogamente, las estufas portátiles fueron promocionadas en los meses de mayor demanda en 2023 (abr-sep), mientras que en 2024 sólo fueron promocionadas en enero-marzo. Es decir, en 2024, durante los meses donde cada producto tiene mayor demanda, estos productos no fueron incluidos en los envíos publicitarios. Esto probablemente hizo que los clientes no recibieran recordatorios u ofertas de estos productos en el momento de mayor necesidad, llevando a menores ventas en los meses donde uno esperaría que las ventas fuesen mayores.",
          "note": "No hace falta que se proporcionen ejemplos numéricos para que la respuesta esté completa (2 puntos), pero si debe hacerse referencia a los datos proporcionados.",
          "scores": {
            "0": {
              "label": "No responde correctamente.",
              "example": "Sí, la falta de estacionalidad en las ventas de los ventiladores podría explicarse por una modificación en las preferencias de los consumidores que, por las condiciones macroeconómicas, ahora eligen los aires acondicionados.",
              "explanation": "Responde incorrectamente porque propone una hipótesis no respaldada por el informe y no utiliza ningún dato provisto. Además, desvía la explicación hacia cambios en preferencias sin considerar la información relevante de marketing disponible en el informe."
            },
            "1": {
              "label": "Menciona la respuesta correcta, pero de manera superficial.",
              "example": "Sí, el problema pareciera ser la estrategia de marketing.",
              "explanation": "Identifica el área relevante, pero de manera superficial. No se apoya en los datos del informe ni explica qué aspecto concreto de la estrategia publicitaria cambió entre años o cómo eso afecta las ventas."
            },
            "2": {
              "label": "Menciona la respuesta correcta de manera detallada, y justifica adecuadamente.",
              "example": "Sí, los datos adjuntos sugieren que el problema radica en el diseño de nuestra estrategia de marketing. Mientras que en 2023 logramos que la publicidad acompañara adecuadamente el patrón estacional de las ventas, en 2024 esto no ocurrió, lo que nos impidió aprovechar los picos de demanda de ventiladores y estufas.",
              "explanation": "Responde completamente porque utiliza la evidencia del informe para comparar la estrategia de marketing entre años, identifica el desajuste con los picos estacionales y explica claramente por qué esto afecta las ventas. Justifica la conclusión con datos del informe."
            }
          }
        }
      }
    },
    "solution": {
      "max_points": 4,
      "prompt": "Las propuestas del participante pueden incluir una o varias acciones para solucionar el problema. Cada acción debe evaluarse de manera individual según los criterios B1, B2 y B3, sin elegir una 'mejor' acción dentro de la grilla. El objetivo de esta sección es definir cómo puntuar cada acción concreta en función de si aborda la causa del problema, cuán específica es y cuán realista resulta.",
      "problem_to_solve": "En 2024 las ventas de estufas y ventiladores no siguen un patrón estacional",
      "criteria": {
        "B1": {
          "description": "Para cada acción propuesta, ¿la solución propuesta lidia directamente con la causa del problema?",
          "note": "Para recibir 1 punto en este criterio, el participante debe mencionar explícitamente que la publicidad debe ajustarse a la estacionalidad o, en su defecto, haber identificado claramente ese problema en A3. Si en A3 reconoció la falta de estacionalidad y en B1 alude a la publicidad de forma coherente con ese diagnóstico, puede recibir 1 punto. Si no lo mencionó en A3 ni en B1, o solo indica de manera genérica que se debe publicitar más, debe recibir 0 puntos.",
          "note2": "No debe asignarse puntaje en este criterio si el participante solo identifica correctamente la causa del problema en A3 (la falta de estacionalidad en las publicidades de estufas y ventiladores), pero no propone una solución explícita para resolverlo en B1. Reconocer la causa no equivale a ofrecer una medida correctiva. La propuesta debe indicar de manera clara qué acción concreta se tomaría para abordar esa falta de estacinoalidad en las publicidades. No se debe otorgar puntaje en B1 por diagnóstico correcto en A3, ni por alusiones generales a la causa del problema en B1.",
          "note3": "Si la propuesta consiste únicamente en aplicar descuentos, promociones, ofertas estacionales o bajar precios —sin ajustar explícitamente la estacionalidad de la publicidad— debe recibir 0 puntos. Estas acciones no abordan la causa del problema identificada en la consigna.",
          "scores": {
            "0": {
              "label": "No",
              "example1": "Deberíamos dejar de vender los ventiladores, está claro que los consumidores prefieren los aires acondicionados.",
              "explanation1": "No responde correctamente porque propone una acción que no aborda la causa del problema. Ignora la evidencia del informe y no hace ninguna referencia a la estacionalidad ni al rol de la publicidad, por lo que no sugiere una solución vinculada al diagnóstico correcto.",
              "example2": "Podríamos ofrecer descuentos en la compra de ventiladores en verano y descuentos en la compra de calefactores en invierno.",
              "explanation2": "No responde correctamente porque propone una acción que no aborda la causa del problema -la falta de estacionalidad en las publicidades de los ventiladores y de las estufas-."
            },
            "1": {
              "label": "Sí",
              "example": "Deberíamos repensar la estrategia de marketing para que sea consistente con los patrones de demanda que maximizan nuestras ventas. Podríamos, por ejemplo, replicar lo que hicimos 2023. Bajo este esquema las ventas de los ventiladores y de las estufas mostraron el patrón estacional.",
              "explanation": "Responde correctamente porque propone explícitamente ajustar la publicidad para que acompañe los momentos de mayor demanda. Conecta la solución con el diagnóstico basado en la estacionalidad y plantea una acción concreta consistente con los datos del informe."
            }
          }
        },
        "B2": {
          "description": "Para cada acción propuesta, ¿es una acción concreta/específica?",
          "note": "Este criterio evalúa el grado de concreción y detalle de la propuesta. Es decir, cuán claramente se entiende qué acción se propone. Para obtener 2 puntos, la propuesta debe describir una acción definida, aplicable al contexto del local, y dejar claro qué se haría y con qué objetivo. **Es condición necesaria para recibir 2 puntos que la propuesta especifique explícitamente en qué época del año deben promocionarse las estufas y los ventiladores (por ejemplo, estufas en invierno y ventiladores en verano).** Si se mencionan varias opciones sin desarrollo, si las acciones son vagas (por ejemplo, 'repensar la estrategia de marketing', 'mejorar la publicidad' o 'adecuar la periodicidad'), corresponde 1 punto o menos.",
          "scores": {
            "0": {
              "label": "Propuesta demasiado general o abstracta: no se entiende bien qué acción concreta se propone.",
              "example1": "Repensar la estrategia de marketing.",
              "explanation1": "La propuesta es demasiado vaga: no especifica qué aspecto de la estrategia cambiar, ni qué acción concreta se realizaría. No permite entender cómo se implementaría la solución.",
              "example2": "Los correos electrónicos deberían ser completamente estacionales.",
              "explanation2": "La propuesta es demasiado general: no aclara qué cambios concretos se realizarían en la práctica. No indica qué productos se promocionarían, en qué momentos, ni cómo se ajustaría el calendario de envíos, por lo que no permite entender la acción específica que se propone."
            },
            "1": {
              "label": "Propuesta con cierta especificidad, pero sin suficiente detalle operativo o contextual.",
              "example1": "Adecuar la periodicidad de las publicidades.",
              "explanation1": "La propuesta es general y sin detalles operativos. Indica una dirección de acción, pero no explica cómo se haría ni a qué cambios concretos se refiere.",
              "example2": "Tendríamos que mantener las campañas de cada producto en su temporada correspondiente.",
              "explanation2": "La propuesta es general y sin detalles operativos. No menciona a los ventiladores ni a las estufas, ni cuando debe promocionarse cada uno de estos productos.",
              "example3": "Los correos deben enviarse al inicio de la temporada de uso, no una vez que ya terminó.",
              "explanation3": "La propuesta es general y sin detalles operativos. No menciona a los ventiladores ni a las estufas, ni cuando debe promocionarse cada uno de estos productos."

            },
            "2": {
              "label": "Propuesta clara y específica dentro del contexto de la empresa: se entiende qué acción se propone y cómo podría implementarse en términos generales. No es necesario que la propuesta incluya plazos, métricas o formatos de implementación.",
              "example": "Modificar el calendario de campañas para que las estufas se promocionen en los meses de invierno, y los ventiladores en los meses de verano, aprovechando los picos estacionales de demanda.",
              "explanation": "La propuesta es clara y aplicable al contexto: detalla qué acción específica se haría (ajustar el calendario de campañas) y con qué objetivo (aprovechar la estacionalidad). Se entiende exactamente cómo implementarla de manera general."
            }
          }
        },
        "B3": {
          "description": "Para cada acción propuesta, ¿es una acción realista?",
          "scores": {
            "0": {
              "label": "No",
              "example": "Podríamos rediseñar por completo los ventiladores y estufas portátiles para que ambos productos sean útiles durante todo el año: por ejemplo, que funcionen como ventilador en verano y como estufa en invierno.",
              "explanation": "No es realista porque implica rediseñar los productos desde cero, algo costoso, técnicamente complejo y fuera del alcance de una respuesta operativa. No se ajusta al contexto del negocio ni a las capacidades esperables para resolver el problema identificado."
            },
            "1": {
              "label": "Sí",
              "example": "Modificar la estrategia de marketing para que los ventiladores sean promocionados en verano y las estufas en invierno.",
              "explanation": "Es una propuesta realista porque se trata de un ajuste organizacional factible, de bajo costo y alineado con las operaciones habituales del negocio. Puede implementarse sin cambios estructurales ni tecnológicos"
            }
          }
        }
      }
    },
    "total_max_points": 10
  },
  "writing": {
    "total_max_points": 10,
    "criteria": {
      "1": {
        "name": "Ortografía y gramática",
        "description": "Se evalúa la corrección ortográfica y gramatical del texto, incluyendo el uso adecuado de tildes, signos de puntuación, concordancia verbal y nominal, y mayúsculas. Se valora especialmente la redacción clara, fluida y cuidada, con frases bien estructuradas y sin errores que afecten la calidad o el tono profesional del mensaje.",
        "note": "No se considera error el uso de solo signos de cierre (¿? / ¡!)",
        "scores": {
          "0": {
            "label": "Errores graves o numerosos: el texto presenta múltiples errores ortográficos o gramaticales (tildes, concordancia, puntuación o mayúsculas) que se repiten a lo largo del texto. Estos errores afectan la claridad o dan una impresión de descuido, incluso si el texto se entiende en general.",
            "example1": "hola buenas tarde, estube mirando los datos y el balence no da igual por que los aire no enfrian bien y los ventiladore usa mucha corriente directa eso genera gasto alto, tendria que ver si hay sucidio en la luz o no.",
            "explanation1": "Presenta múltiples errores ortográficos (“estube”, “balence”, “aire”, “ventiladore”, “sucidio”), fallas de concordancia y omisión de mayúsculas. Los errores afectan la claridad y muestran descuido sostenido en la escritura.",
            "example2": "Buenos dias estimado, segun el analisis que pude ver los dato no coinciden con el informe, el restraso en las entregas y la variacion climitica puede haber afectado las ventas de los aires acondicionados. Seria bueno revizar el perido donde surgio el inconveniente para tener un analisis mas sertero.",
            "explanation2": "Tiene numerosos errores ortográficos recurrentes (“dias”, “segun”, “dato”, “restraso”, “climitica”, “revizar”, “perido”, “sertero”), además de problemas de concordancia. La acumulación de errores afecta la calidad general del texto"
          },
          "1": {
            "label": "Algunos errores o descuidos menores, pero perceptibles: se observan varios errores dispersos (tildes omitidas, puntuación inadecuada, uso impreciso de conectores o ligeras fallas de concordancia). No impiden la comprensión, pero restan fluidez o profesionalismo al texto.",
            "example1": "buen día luis,\nsegún los datos que revisé, las ventas de la sede norte bajaron un poco en julio pero se mantuvieron estables el resto del año. puede ser que los empleados eligieran comer afuera esos días o que el menú no fuera tan variado. sería bueno revisar eso para los próximos meses.\nsaludos",
            "explanation1": "Presenta varios descuidos menores: faltan mayúsculas en nombres propios y al inicio de frases, y hay ligeros problemas de puntuación. Aunque se entiende bien, la redacción pierde formalidad y prolijidad",
            "example2": "Buenos dias Luis,\nRevisando los datos del informe veo que las ventas de estufas y ventiladores se mantuvieron bastante estables durante todo el año, sin grandes variaciones. En comparacion con 2023, las estufas vendieron mas en invierno y los ventiladores en verano, pero en 2024 esa diferencia casi no se nota.\nNo parece haber problemas con las importaciones, aunque la publicidad pudo haber sido escasa. Seria bueno revisar si los clientes recibieron la informacion a tiempo y si las campañas fueron iguales en todas las regiones.\nSaludos cordiales.",
            "explanation2": "El texto tiene varias tildes omitidas (“dias”, “comparacion”, “mas”, “informacion”, “Seria”), y la puntuación podría ser más cuidada. Los errores no impiden la comprensión, pero restan profesionalismo."
          },
          "2": {
            "label": "Redacción impecable o casi impecable: el texto está cuidadosamente escrito, sin errores ortográficos ni gramaticales perceptibles. La puntuación es precisa, las oraciones están bien estructuradas y el registro es fluido y natural. A lo sumo puede haber un error aislado que no afecta en absoluto la calidad del texto.",
            "example1": "Buenas tardes, Adriana. Según los datos, la baja en ventas los viernes se explica por el trabajo remoto del personal administrativo de la sede Norte. En la sede Sur la asistencia es completa, por lo que las ventas se mantienen estables.",
            "explanation1": "No presenta errores ortográficos ni gramaticales. Las frases están bien construidas, con puntuación clara y registro adecuado. La redacción es fluida y profesional.",
            "example2": "Hola Adriana,\nRevisando los datos, observé que la baja en ventas ocurre principalmente los viernes, cuando gran parte del personal administrativo de la sede Norte trabaja remoto. De lunes a jueves las ventas son similares a la sede Sur.\nPropongo ajustar la producción de almuerzos los viernes y ofrecer menús promocionales o viandas para quienes hacen home office.\nQuedo a disposición para conversar las opciones.\nSaludos,",
            "explanation2": "El texto está muy bien escrito: sin errores de ortografía, con estructuras claras y puntuación correcta. El registro es natural, profesional y coherente en todo el mensaje."
          }
        }
      },
      "2": {
        "name": "Claridad y legibilidad",
        "description": "Se evalúa la claridad, precisión y fluidez del texto, **dentro del contexto del mail del jefe y de la consigna**. Las ideas deben expresarse de manera directa, ordenada y sin ambigüedades, y deben permitir que el jefe comprenda la respuesta a partir de la información del informe. Se valoran las oraciones bien construidas, la coherencia entre frases y la ausencia de repeticiones o redundancias. El texto se entiende fácilmente y transmite las ideas con naturalidad y economía de palabras.  Un texto es poco claro no solo cuando está mal escrito, sino también cuando, aunque sea breve o gramaticalmente correcto, **no desarrolla las ideas necesarias para responder lo que pide el jefe**, o resulta tan general que el jefe no entendería el mensaje.",
        "note": "La repetición de ideas **debe penalizarse**. Los textos que no desarrollan las ideas mínimamente necesarias para que el jefe entienda la respuesta **en el contexto de su mail** también deben penalizarse. Un texto puede estar bien escrito a nivel lingüístico pero ser confuso o inútil si no permite comprender la respuesta requerida.",
        "scores": {
          "0": {
            "label": "Texto confuso o desorganizado: el texto resulta difícil de comprender por errores de construcción o frases inconexas. Presenta repeticiones de ideas innecesarias o ambigüedades que impiden seguir el hilo argumental con claridad.",
            "example1": "La gente compra cuando le conviene…si no tiene plata busca lo más barato y si suben los precios deja de comprar porque no le alcanza y capaz espera alguna oferta o descuento y después se olvida del producto por eso bajan las ventas…no es tan dificil de ver.",
            "explanation1": "El texto es confuso y desordenado: mezcla ideas sin conectores claros, y presenta frases encadenadas sin estructura. Esto dificulta seguir el argumento.",
            "example2": "puede ser que sea por el tema de las importasiones o porque los precios cambiaron pero si la venta subio en otro momento tal ves sea porque la gente aprovecho las ofertas o porque no habia stock igual con la situacion del pais es dificil saber bien que paso pero seguro algo influyo.",
            "explanation2": "La frase es larga y caótica, con varias ideas juntas sin orden lógico. Hay repeticiones, ambigüedades y problemas que afectan seriamente la legibilidad. No se entiende claramente el mensaje.",
            "example3": "Es un problema de marketing. Saludos,",
            "explanation3": "Aunque está escrito de manera clara y sin errores, **no dice nada útil para el jefe**: no desarrolla la idea, no usa datos del informe y no responde ninguna de las preguntas. Por tanto, debe recibir 0 puntos."
          },
          "1": {
            "label": "Claridad limitada: se identifican varias frases confusas, mal estructuradas o redundantes. La lectura requiere esfuerzo y el mensaje no fluye naturalmente. Las ideas aparecen sin una secuencia lógica o con expresiones poco precisas.",
            "example1": "Buenas tardes Luis,\nEl motivo de la baja en las ventas puede ser que los clientes ya compraron el año pasado aires frío calor, por lo que al tener un producto que sirve para todo el año no necesitan volver a gastar en estufas o ventiladores. Esto hace que el mercado se reduzca y que tengamos que pensar otras opciones, que puede ser también revisar las importaciones para ver si hay faltantes, porque si no hay stock tampoco se puede vender, y además ver si conviene traer más aires para el verano.",
            "explanation1": "Contiene frases largas, ideas mezcladas y explicaciones redundantes. El orden es poco claro y el texto no fluye naturalmente. Requiere esfuerzo del lector para seguir el argumento.",
            "example2": "Hola, para solucionar el problema habría que bajar un poco el precio de las estufas y ventiladores, así se venden más. Igual creo que el aire acondicionado se vende mejor porque tiene frío y calor, por eso la gente lo elige más.",
            "explanation2": "Las ideas están poco conectadas y aparecen sin un hilo claro. Hay falta de precisión y razonamientos incompletos. La lectura no es fluida.",
            "example3": "Hola Luis, parece ser un problema en la estacionalidad del marketing, pero necesito más información. Saludos,",
            "explanation3": "Responde algo, pero de forma superficial y sin desarrollar. No quedaría claro para el jefe cuál es el diagnóstico o cuáles son las posibles soluciones."
          },
          "2": {
            "label": "Claridad aceptable pero mejorable: el texto se comprende en general, aunque contiene algunas oraciones extensas, o formulaciones poco naturales que interrumpen la fluidez. Puede haber alguna repetición de ideas. Requiere algo de esfuerzo para seguir el hilo.",
            "example1": "Hola Luis,\nEstuve revisando el informe con los gráficos de ventas y noté que el descenso en la sede Norte se concentra principalmente los viernes, el resto de la semana las ventas se mantienen estables, puede ser que el trabajo remoto de los empleados administrativos esté afectando la concurrencia al comedor esos días.\nTambién influye que el menú se repite seguido, lo que puede desmotivar a algunos empleados a almorzar en la empresa. De todas formas, no parece ser el principal motivo.\nSería útil revisar la cantidad de personal presente los viernes y ajustar la oferta o las promociones para equilibrar las ventas entre sedes.\nSaludos,",
            "explanation1": "El texto es claro en general, pero tiene oraciones largas y algunas formulaciones que interrumpen la fluidez. Hay momentos en que el hilo se vuelve menos directo. Aun así, se entiende sin dificultad.",
            "example2": "En relación con la consulta que me enviaste, analicé los datos del informe y observo que las ventas de aires acondicionados en 2024 se mantuvieron bastante similares a las de 2023.\nA partir de la tabla de unidades pedidas y entregadas, se nota que en ventiladores y estufas hubo una leve diferencia a favor de los productos entregados, mientras que en aires acondicionados la cantidad recibida fue algo menor, especialmente en el segundo semestre.\nConsidero que esta menor disponibilidad puede haber afectado las ventas, más que una caída en la demanda, como sugerencia, propondría equilibrar los pedidos de los tres productos para evitar faltantes en los próximos períodos.",
            "explanation2": "Es comprensible, pero contiene oraciones extensas y algunas transiciones poco naturales. El flujo no es impecable y requiere algo de esfuerzo para seguir el razonamiento."
          },
          "3": {
            "label": "Claridad y legibilidad destacadas: el texto es muy claro y fluido. Las oraciones están bien construidas, no hay ambigüedades, o repetición de ideas. Se lee con naturalidad.",
            "example1": "Hola Luis,\nEstuve revisando el informe y noté que las ventas de aires acondicionados se mantuvieron estables en 2024, mientras que las de estufas y ventiladores bajaron respecto de 2023.\nNo parece haber problemas de importación, pero sí un cambio en las campañas: se publicitaron productos fuera de temporada.\nSugiero volver a ajustar las promociones al clima —ventiladores en verano y estufas en invierno— para recuperar las ventas.\nSaludos,",
            "explanation1": "El texto es claro, directo y bien secuenciado. No hay redundancias ni ambigüedades. Las ideas fluyen naturalmente y la organización es muy buena.",
            "example2": "Hola Luis,\nEn 2024 las ventas de aires acondicionados mantuvieron el mismo patrón que en 2023: suben en verano y bajan en invierno, sin cambios significativos. Tampoco se observan efectos por trabas a la importación.\nEl problema parece estar en las campañas: este año no se promocionaron ventiladores en verano ni estufas en invierno, lo que explica la pérdida de los picos estacionales.\nSugiero volver a alinear las promociones con las temporadas para recuperar las ventas en esos productos.\nSaludos,",
            "explanation2": "La redacción es muy clara y fácil de leer. Cada idea está expresada con precisión y en orden lógico. No hay repeticiones ni ambigüedades. La claridad y la economía de palabras son sobresalientes."
          }
        }
      },
      "3": {
        "name": "Organización del texto",
        "description": "Se evalúa la estructura y el orden interno del texto. Debe seguir una secuencia lógica que incluya:\n1. una introducción que enmarque el mensaje o un saludo (por ejemplo, 'Hola XX, cómo estás?' o una breve referencia al mail del jefe),\nEjemplo de referencia al mail del jefe: “Revisé los datos que me enviaste y encontré lo siguiente:”\n2. un desarrollo en el que se respondan las preguntas planteadas,\n3. una sección con propuestas o sugerencias para resolver el problema, y\n4. un cierre que retome las ideas principales o una despedida.\nEjemplos de cierre o saludo:\n1.“Estoy a disposición para discutir cómo implementar las mejoras.”\n2.'Saludos,'\nTambién se valora la organización interna dentro de cada sección: el uso adecuado de párrafos, la coherencia en la secuencia de ideas y la ausencia de saltos temáticos.",
        "note": "Tanto un saludo como una referencia al mail del jefe cuentan como introducción, y tanto una despedida como un cierre que retome la ideas principales o que diga 'Quedo a disposición' cuentan como cierre.",
        "scores": {
          "0": {
            "label": "Texto desorganizado o sin estructura reconocible: no se distinguen las secciones principales o las ideas aparecen mezcladas y repetidas. Falta orden tanto en la estructura general como dentro de los párrafos.",
            "example": "lo que habría que hacer es poner descuentos o algo así porque la gente no compra como antes, está todo muy caro y la situación económica no ayuda, además los otros negocios también hacen promociones y hay que competir, aunque igual depende del tipo de producto porque algunos no se venden ni con oferta, pero habría que intentar con algo para ver si suben las ventas porque la cosa está difícil y uno no se puede quedar quieto.",
            "explanation": "El texto no presenta una estructura reconocible: no hay introducción, desarrollo ni cierre. Las ideas aparecen mezcladas en un único bloque, sin orden ni párrafos, y con saltos temáticos que dificultan seguir el hilo."
          },
          "1": {
            "label": "Estructura débil o confusa: se percibe cierta intención de organización, pero faltan secciones o están mal delimitadas. Dentro de cada parte hay mezcla de ideas o saltos que dificultan la lectura. Los párrafos no agrupan bien las ideas.",
            "example": "Hola buenas tardes Luis, estuve viendo los datos y me parece que las ventas bajaron un poco, puede ser por el tema de las promociones o de la financiación, porque últimamente los bancos no están ofreciendo muchas cuotas y eso complica a los clientes. Capaz habría que revisar eso o ver si se pueden hacer descuentos para incrementar las ventas.",
            "explanation": "Hay un saludo, pero no se distinguen las secciones principales. Todo está en un solo párrafo largo con ideas mezcladas entre diagnóstico y propuestas. La organización interna es débil y no sigue una secuencia clara."
          },
          "2": {
            "label": "Organización parcial o irregular: el texto incluye la mayoría de las secciones, pero el orden o la articulación entre ellas es poco clara. Algunas partes están bien organizadas, mientras que otras presentan saltos. Los párrafos son comprensibles pero desbalanceados.",
            "example": "Estimado,\nEstuve revisando los datos y noté que las ventas de aires acondicionados se mantuvieron estables, sin diferencias respecto al año anterior. En cambio, en estufas y ventiladores sí hubo una caída, aunque no parece deberse a problemas con el importador. Considero que puede estar relacionada con la falta de promoción en los meses correspondientes y con una mayor competencia en el rubro.\nSería conveniente reforzar la comunicación de estos productos en los períodos estacionales y revisar si las campañas se están enviando en los momentos adecuados.\nSin más, lo saludo atentamente.",
            "explanation": "Incluye introducción, desarrollo, propuestas y cierre, pero el orden no es del todo claro y algunas ideas aparecen mezcladas. La organización dentro de los párrafos es desigual: algunas partes están bien agrupadas y otras tienen saltos o cambios súbitos de foco."
          },
          "3": {
            "label": "Organización clara y coherente: el texto sigue la secuencia esperada (introducción, respuestas, propuestas, cierre) y las ideas dentro de cada sección están bien agrupadas. Hay un uso adecuado de párrafos, aunque las transiciones o la progresión de ideas podrían ser más fluidas.",
            "example": "Buen día Luis,\nEstuve revisando los datos y noto que en 2024 las ventas de estufas y ventiladores perdieron el comportamiento estacional habitual. No parece que haya sido por problemas de importación, ya que los aires acondicionados mantuvieron un nivel de ventas normal.\nCreo que el principal factor puede ser la falta de campañas o promociones en los meses correspondientes. Sería importante retomar las estrategias de marketing estacional, promocionando ventiladores y aires acondicionados en verano, y estufas en invierno. También podría ser útil medir cómo reaccionan las ventas después de estos ajustes y evaluar otros canales como redes sociales o promociones en tienda.\nQuedo a disposición para avanzar con estas ideas.\nSaludos,",
            "explanation": "El texto sigue una estructura general adecuada (saludo, diagnóstico, propuestas, cierre) y las ideas están bien agrupadas. Sin embargo, el diagnóstico y las propuestas aparecen mezclados dentro del mismo párrafo, lo que interrumpe la separación clara entre secciones requerida para una organización excelente."
          },
          "4": {
            "label": "Organización excelente: el texto presenta una estructura completa y equilibrada: cada sección cumple su función, las ideas dentro de cada una están ordenadas, y las transiciones entre párrafos son naturales. La organización general y la interna contribuyen a una lectura fluida y lógica.",
            "example": "Hola Luis, ¿cómo estás?\nEstuve revisando los datos y en 2024 las ventas de aires acondicionados mantuvieron el mismo comportamiento estacional que en 2023: aumentaron en verano y bajaron en invierno.\nEn cuanto a las importaciones, no se observó un impacto significativo en las ventas ni en la disponibilidad de los productos.\nEl principal cambio parece estar en la promoción. Este año no hubo campañas específicas de ventiladores en verano ni de estufas en invierno, lo que puede explicar la falta de picos estacionales. En cambio, los aires acondicionados sí se promocionaron en los momentos clave.\nMi recomendación es retomar las campañas estacionales para recuperar los niveles habituales de venta. Con una comunicación adecuada y en los momentos justos, deberíamos poder restablecer el patrón de ventas esperado.\nQuedo atento a tus comentarios.\nSaludos,",
            "explanation": "La estructura es completa: introducción clara, diagnóstico, propuestas y cierre adecuado. Los párrafos están perfectamente organizados y las transiciones son naturales, lo que permite una lectura fluida y lógica."
          }
        }
      },
      "4": {
        "name": "Registro adecuado",
        "description": "Se evalúa si el tono del mail es apropiado para el contexto laboral y coherente con el tono del mail del jefe. El tono no debe ser excesivamente informal, debe ser cortes y profesional.\nEl criterio penaliza automáticamente (0 puntos) los casos en los que:\n1.El texto esté completamente escrito en mayúsculas (por considerarse una forma inapropiada o agresiva de comunicación).\n2. El texto incluya rastros evidentes de generación automática o placeholders propios de un asistente virtual, como firmas incompletas del tipo “[tu nombre]”, o texto no reemplazado.",
        "note1": "En este criterio no se evalúa la presencia o la falta de saludo y despedida",
        "note2": "Mencionar explícitamente que se utilizó una herramienta de IA para elaborar el diagnóstico **no se penaliza**",
        "scores": {
          "0": {
            "label": "El tono del mail es demasiado informal, coloquial o poco cortés en relación con el tono del mail del jefe. También se asigna 0 puntos si el texto está completamente en mayúsculas, si deja evidencia explícita de interacción con ChatGPT u otra IA, o si el texto no presenta un tono profesional acorde al mail del jefe.",
            "example1": "Buenas,\nSegún el informe que me mandaste creo que el problema está en la falta de estacional en las campañas de publicidad de las estufas y ventiladores. También puede influir que los aires acondicionados tiran frío y calor, y que este último año hubo crisis económica en Argentina.\nAbrazo,",
            "explanation1": "El tono es excesivamente informal para un intercambio laboral: usa saludos coloquiales (“Buenas”, “Abrazo”). No mantiene la formalidad esperable en el contexto definido por el mail del jefe.",
            "example2": "Hola Luis, ¿cómo estás?\nSegún el informe que me mandaste creo que el problema está en la falta de estacional en las campañas de publicidad de las estufas y ventiladores. También puede influir que los aires acondicionados tiran frío y calor, y que este último año hubo crisis económica en Argentina.\nSaludos,\n[Tu nombre]",
            "explanation2": "Incluye un placeholder típico de un asistente virtual ('[tu nombre]'), lo cual activa la penalización automática.",
            "example3": "HOLA LUIS, ¿CÓMO ESTÁS?\nSEGÚN EL INFORME QUE ME MANDASTE CREO QUE EL PROBLEMA ESTÁ EN LA FALTA DE ESTACIONAL EN LAS CAMPAÑAS DE PUBLICIDAD DE LAS ESTUFAS Y VENTILADORES. TAMBIÉN PUEDE INFLUIR QUE LOS AIRES ACONDICIONADOS TIRAN FRÍO Y CALOR, Y QUE ESTE ÚLTIMO AÑO HUBO CRISIS ECONÓMICA EN ARGENTINA.\nSALUDOS CORDIALES,",
            "explanation3": "El texto está completamente en mayúsculas, lo cual se considera un tono inadecuado o agresivo en comunicación escrita. Esto activa automáticamente el puntaje 0, independientemente del contenido."          
          },
          "1": {
            "label": "Registro adecuado: el tono es respetuoso y coherente acorde con el tono del mail del jefe. El texto mantiene un registro profesional y apropiado para el contexto laboral.",
            "example": "Hola Luis, ¿cómo estás?\nSegún el informe que me mandaste creo que el problema está en la falta de estacional en las campañas de publicidad de las estufas y ventiladores. También puede influir que los aires acondicionados tiran frío y calor, y que este último año hubo crisis económica en Argentina.\nSaludos cordiales,",
            "explanation": "El tono es respetuoso, profesional y consistente con el mail del jefe. Aunque el estilo es sencillo e informal en algunos lugares, se mantiene dentro de un registro cortés y adecuado para el contexto laboral, sin señales de IA ni marcas impropias."
          }
        }
      }
    }
  }
}
```

原檔：`upstream/ai_grading/main-pipeline/rubrics/task/sales_task_guides.json`。來源定位：`ai_grading/main-pipeline/rubrics/task/sales_task_guides.json`。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/abs/2608.04198v1) · [官方程式固定版本](https://github.com/ramirogalvez/ai-skill-gap-experiment-data/tree/c144fe68de350b810ac275bd6d6df8219db47fc0) · [逐檔來源與授權](../../sources.json)
