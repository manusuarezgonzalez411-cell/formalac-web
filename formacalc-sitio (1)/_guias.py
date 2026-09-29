# -*- coding: utf-8 -*-
# Contenido editorial largo que se inserta en cada calculadora (antes de las FAQ)

G = {}

G["imc"] = """
          <h2>Tabla de categorías de la OMS (adultos)</h2>
          <table class="data-table">
            <tr><th>IMC (kg/m²)</th><th>Categoría</th></tr>
            <tr><td>Menos de 18,5</td><td>Bajo peso</td></tr>
            <tr><td>18,5 – 24,9</td><td>Peso normal</td></tr>
            <tr><td>25,0 – 29,9</td><td>Sobrepeso</td></tr>
            <tr><td>30,0 – 34,9</td><td>Obesidad grado I</td></tr>
            <tr><td>35,0 – 39,9</td><td>Obesidad grado II</td></tr>
            <tr><td>40 o más</td><td>Obesidad grado III</td></tr>
          </table>

          <h2>Ejemplo resuelto paso a paso</h2>
          <p>Una persona que pesa 70 kg y mide 175 cm (1,75 m). Primero se eleva la altura al cuadrado:
          1,75 × 1,75 = 3,0625. Después se divide el peso entre ese valor: 70 / 3,0625 = <strong>22,9</strong>.
          Cae dentro del rango de peso normal.</p>
          <p>También puedes hacer el cálculo al revés para saber qué rango de peso corresponde a tu altura.
          Con 1,75 m, un IMC entre 18,5 y 24,9 equivale a pesos de aproximadamente 56,7 a 76,3 kg
          (multiplicando 18,5 y 24,9 por 3,0625).</p>

          <h2>Cómo interpretar tu resultado con sentido común</h2>
          <p>Un IMC es un dato de partida, no un diagnóstico. Estar en la parte alta o baja de un rango no
          implica un problema por sí mismo, y estar dentro del rango "normal" no garantiza buena salud si hay
          mala alimentación, sedentarismo o mucha grasa abdominal. Algunas ideas para darle contexto:</p>
          <ul>
            <li><strong>Mira la tendencia, no un día suelto.</strong> Lo relevante es si tu peso sube o baja de
            forma sostenida durante meses, no una lectura aislada de la báscula.</li>
            <li><strong>Añade el perímetro de cintura.</strong> Un índice cintura-altura (cintura dividida entre
            altura, en la misma unidad) por debajo de 0,5 se usa a menudo como referencia orientativa de menor
            riesgo cardiometabólico.</li>
            <li><strong>Considera tu composición.</strong> Si entrenas fuerza y tienes bastante masa muscular,
            el IMC puede sobrestimar tu grasa. En ese caso mira también el
            <a href="grasa-corporal.html">porcentaje de grasa corporal</a>.</li>
          </ul>

          <h2>Errores frecuentes al calcular el IMC</h2>
          <ul>
            <li>Pesarse con ropa o después de comer mucho: pésate por la mañana, tras ir al baño y sin ropa
            gruesa para tener una referencia comparable.</li>
            <li>Introducir la altura en pies o pulgadas en un campo pensado para centímetros.</li>
            <li>Aplicar estos rangos a niños y adolescentes: en menores se usan percentiles por edad y sexo, no
            las categorías de adultos.</li>
            <li>Tomar el resultado como un objetivo estético en lugar de un indicador de salud general.</li>
          </ul>
"""

G["calorias"] = """
          <h2>La fórmula que usamos: Mifflin-St Jeor</h2>
          <p>Para estimar el metabolismo basal (BMR) usamos la ecuación de Mifflin-St Jeor, publicada en 1990
          y una de las más validadas para población adulta general:</p>
          <ul>
            <li><strong>Hombres:</strong> BMR = 10 × peso (kg) + 6,25 × altura (cm) − 5 × edad + 5</li>
            <li><strong>Mujeres:</strong> BMR = 10 × peso (kg) + 6,25 × altura (cm) − 5 × edad − 161</li>
          </ul>
          <p>Ese BMR se multiplica por un factor de actividad (1,2 sedentario, 1,375 ligero, 1,55 moderado,
          1,725 alto y 1,9 muy alto) para obtener tus calorías de mantenimiento.</p>

          <h2>Dos ejemplos resueltos</h2>
          <p><strong>Hombre, 30 años, 80 kg, 180 cm, actividad moderada.</strong> BMR = 800 + 1.125 − 150 + 5 =
          1.780 kcal. Con factor 1,55, el mantenimiento es de unas <strong>2.759 kcal/día</strong>. Para perder
          peso a ritmo moderado rondaría las 2.260 kcal; para ganar, unas 3.060 kcal.</p>
          <p><strong>Mujer, 28 años, 62 kg, 165 cm, actividad ligera.</strong> BMR = 620 + 1.031 − 140 − 161 ≈
          1.350 kcal. Con factor 1,375, el mantenimiento es de unas <strong>1.857 kcal/día</strong>.</p>

          <h2>Cómo pasar de la estimación a tu cifra real</h2>
          <p>Ninguna ecuación conoce tu genética, tu masa muscular ni cuánto te mueves fuera del gimnasio. El
          método más fiable es usar la cifra como punto de partida y comprobarla:</p>
          <ol>
            <li>Come alrededor de esa cantidad durante 2-3 semanas, registrando lo que comes de forma honesta.</li>
            <li>Pésate en las mismas condiciones (por ejemplo, por la mañana) varias veces por semana y calcula
            la media semanal.</li>
            <li>Si el peso medio se mantiene estable, esa es tu ingesta de mantenimiento. Si sube o baja más de
            lo esperado, ajusta en pasos de 100-150 kcal.</li>
          </ol>

          <h2>Qué significa cada objetivo</h2>
          <p>Para perder peso se resta un déficit; para ganar, se suma un pequeño superávit. Los superávits
          moderados (unas 250-300 kcal) suelen ser suficientes para ganar músculo con poca grasa añadida si se
          entrena fuerza con regularidad. Los déficits muy grandes son más difíciles de sostener y aumentan el
          riesgo de perder masa muscular; en la <a href="deficit-calorico.html">calculadora de déficit</a>
          puedes elegir el ritmo con más detalle.</p>

          <h2>Cuándo estas cifras no son una guía adecuada</h2>
          <p>No están pensadas para menores de edad, embarazo, lactancia, personas con enfermedades
          metabólicas o renales, ni para quien tenga antecedentes de trastornos de la conducta alimentaria. En
          esos casos, las necesidades deben valorarse con un profesional sanitario.</p>
"""

G["proteina"] = """
          <h2>Rangos de referencia por objetivo</h2>
          <table class="data-table">
            <tr><th>Situación</th><th>Referencia orientativa (g por kg de peso)</th></tr>
            <tr><td>Adulto sedentario sano (evitar carencias)</td><td>0,8</td></tr>
            <tr><td>Persona activa, entrenamiento recreativo</td><td>1,2 – 1,6</td></tr>
            <tr><td>Ganar o mantener masa muscular</td><td>1,4 – 2,0</td></tr>
            <tr><td>Déficit calórico con entrenamiento de fuerza</td><td>1,8 – 2,2</td></tr>
          </table>
          <p>La posición del International Society of Sports Nutrition (2017) sitúa el rango para construir y
          mantener masa muscular en 1,4-2,0 g/kg. Un metaanálisis de 2018 (Morton y cols.) encontró que el
          beneficio adicional sobre la masa muscular se estabilizaba en torno a 1,6 g/kg en la mayoría de
          personas, con un margen superior hasta unos 2,2 g/kg. Por eso las cifras que da la calculadora son
          puntos de partida razonables, no umbrales exactos.</p>

          <h2>Ejemplo resuelto</h2>
          <p>Una persona de 75 kg que entrena fuerza para ganar músculo. Con 1,8 g/kg necesita unos
          <strong>135 g de proteína al día</strong>. Repartidos en cuatro comidas, son unos 34 g por comida, una
          cantidad fácil de alcanzar con una ración normal de una fuente proteica.</p>

          <h2>Cuánta proteína aportan algunos alimentos (aprox. cada 100 g)</h2>
          <table class="data-table">
            <tr><th>Alimento</th><th>Proteína aproximada</th></tr>
            <tr><td>Pechuga de pollo cocinada</td><td>30 – 32 g</td></tr>
            <tr><td>Atún al natural (lata, escurrido)</td><td>24 – 26 g</td></tr>
            <tr><td>Ternera magra cocinada</td><td>26 – 28 g</td></tr>
            <tr><td>Salmón cocinado</td><td>20 – 24 g</td></tr>
            <tr><td>Yogur griego natural</td><td>8 – 10 g</td></tr>
            <tr><td>Lentejas cocidas</td><td>8 – 9 g</td></tr>
            <tr><td>Huevo entero (1 unidad grande ≈ 50 g)</td><td>6 – 7 g por huevo</td></tr>
          </table>
          <p>Son valores orientativos: varían con la marca, la cocción y el corte. Consulta la etiqueta o una
          base de datos de composición de alimentos si necesitas precisión.</p>

          <h2>Consejos prácticos</h2>
          <ul>
            <li>Incluye una fuente de proteína en cada comida en lugar de concentrarla en la cena.</li>
            <li>Si sigues una dieta vegetariana o vegana, combina legumbres, cereales, frutos secos, tofu o
            tempeh y ajusta al alza el objetivo un poco para compensar la menor digestibilidad de algunas
            fuentes vegetales.</li>
            <li>Los suplementos (proteína en polvo) son una comodidad, no una necesidad: úsalos solo si te
            ayudan a llegar a tu cifra.</li>
            <li>Personas con enfermedad renal, o con dudas sobre su función renal, deben consultar con su
            médico antes de aumentar la proteína de forma importante.</li>
          </ul>
"""

G["gasto-calorico"] = """
          <h2>De qué se compone tu gasto energético</h2>
          <table class="data-table">
            <tr><th>Componente</th><th>Qué es</th><th>Peso aproximado en el total</th></tr>
            <tr><td>BMR</td><td>Energía en reposo para mantener funciones vitales</td><td>60 – 70 %</td></tr>
            <tr><td>Efecto térmico de los alimentos</td><td>Energía que cuesta digerir y absorber la comida</td><td>≈ 10 %</td></tr>
            <tr><td>NEAT</td><td>Movimiento diario que no es ejercicio planificado</td><td>Muy variable (15 – 30 %)</td></tr>
            <tr><td>Ejercicio planificado</td><td>Entrenamientos y deporte</td><td>5 – 15 %</td></tr>
          </table>
          <p>Son proporciones aproximadas y cambian mucho de una persona a otra: quien tiene un trabajo de pie
          y camina mucho puede gastar cientos de calorías más por NEAT que quien trabaja sentado, aunque ambos
          entrenen lo mismo.</p>

          <h2>Cómo elegir tu nivel de actividad sin engañarte</h2>
          <ul>
            <li><strong>Sedentario (×1,2):</strong> trabajo sentado y poco o ningún ejercicio.</li>
            <li><strong>Ligero (×1,375):</strong> ejercicio suave 1-3 días por semana o trabajo con algo de
            movimiento.</li>
            <li><strong>Moderado (×1,55):</strong> entrenamientos 3-5 días por semana.</li>
            <li><strong>Alto (×1,725):</strong> entrenamiento intenso 6-7 días por semana.</li>
            <li><strong>Muy alto (×1,9):</strong> trabajo físico exigente combinado con entrenamiento diario o
            doble sesión.</li>
          </ul>
          <p>Un error habitual es elegir un nivel demasiado alto porque se entrena "casi todos los días". Si
          dudas entre dos niveles, empieza por el inferior y ajusta con datos reales.</p>

          <h2>Ejemplo resuelto</h2>
          <p>Un hombre de 35 años, 78 kg y 178 cm: BMR = 780 + 1.112,5 − 175 + 5 ≈ 1.723 kcal. Su TDEE sería
          de unas 2.068 kcal si es sedentario (×1,2), 2.369 kcal con actividad ligera (×1,375) y
          2.671 kcal con actividad moderada (×1,55). La diferencia entre elegir un nivel u otro es de
          más de 600 kcal al día, por eso conviene ser honesto al seleccionar.</p>

          <h2>Por qué tu reloj o tu máquina de cardio pueden exagerar</h2>
          <p>Los dispositivos que estiman las calorías quemadas en una sesión suelen sobrestimarlas. Si usas
          esa cifra para "comer más" después de entrenar, es fácil anular el déficit sin darte cuenta. Es más
          fiable basar tu gasto en la fórmula y en la evolución real de tu peso.</p>
"""

G["1rm"] = """
          <h2>Fórmulas habituales para estimar el 1RM</h2>
          <p>Esta calculadora usa la fórmula de Epley: <strong>1RM = peso × (1 + repeticiones / 30)</strong>.
          Existen otras, como la de Brzycki: <strong>1RM = peso × 36 / (37 − repeticiones)</strong>. Con series
          cortas dan resultados muy parecidos; con series largas se separan.</p>
          <table class="data-table">
            <tr><th>Ejemplo: 80 kg × 5 reps</th><th>Resultado</th></tr>
            <tr><td>Epley: 80 × (1 + 5/30)</td><td>93,3 kg</td></tr>
            <tr><td>Brzycki: 80 × 36 / 32</td><td>90,0 kg</td></tr>
          </table>
          <p>La diferencia de unos 3 kg muestra que el 1RM estimado es una referencia, no un dato exacto.
          Lo importante es usar siempre la misma fórmula para comparar tu progreso en el tiempo.</p>

          <h2>Relación aproximada entre porcentaje y repeticiones</h2>
          <table class="data-table">
            <tr><th>% del 1RM</th><th>Repeticiones posibles (aprox.)</th><th>Uso habitual</th></tr>
            <tr><td>95 %</td><td>2</td><td>Fuerza máxima</td></tr>
            <tr><td>90 %</td><td>4</td><td>Fuerza</td></tr>
            <tr><td>85 %</td><td>6</td><td>Fuerza / hipertrofia</td></tr>
            <tr><td>80 %</td><td>8</td><td>Hipertrofia</td></tr>
            <tr><td>75 %</td><td>10</td><td>Hipertrofia</td></tr>
            <tr><td>70 %</td><td>12</td><td>Hipertrofia / resistencia</td></tr>
            <tr><td>65 %</td><td>15</td><td>Resistencia muscular</td></tr>
          </table>
          <p>Estas equivalencias varían según la persona y el ejercicio: en movimientos que implican mucha
          masa muscular, como la sentadilla o el peso muerto, muchas personas hacen menos repeticiones al mismo
          porcentaje que en ejercicios más pequeños.</p>

          <h2>Cómo hacer la serie de estimación con seguridad</h2>
          <ul>
            <li>Calienta de forma progresiva con series de aproximación antes de tu serie de trabajo.</li>
            <li>Elige un peso con el que puedas hacer entre 3 y 8 repeticiones con técnica correcta; las series
            más cortas dan estimaciones más fiables.</li>
            <li>Detente antes del fallo técnico. La estimación no requiere llegar al límite absoluto.</li>
            <li>Usa barras de seguridad o un compañero en ejercicios como press banca o sentadilla.</li>
          </ul>

          <h2>Cómo usar el resultado</h2>
          <p>Con tu 1RM estimado puedes fijar cargas: por ejemplo, para hipertrofia trabajar series de 8-12
          repeticiones en torno al 70-80 %. Recalcula cada 4-8 semanas, o cuando notes que las cargas se
          vuelven demasiado fáciles o difíciles. Si quieres ver cómo encaja en una programación, prueba el
          <a href="rutinas.html">generador de rutinas</a>.</p>
"""

G["grasa-corporal"] = """
          <h2>Cómo tomar las medidas correctamente</h2>
          <ul>
            <li><strong>Cuello:</strong> justo debajo de la laringe, con la cinta ligeramente inclinada hacia
            abajo por delante, sin apretar.</li>
            <li><strong>Cintura (hombres):</strong> a la altura del ombligo, tras exhalar con normalidad y sin
            meter la tripa.</li>
            <li><strong>Cintura (mujeres):</strong> en la zona más estrecha del abdomen, habitualmente por
            encima del ombligo.</li>
            <li><strong>Cadera (mujeres):</strong> en la zona más ancha de los glúteos.</li>
            <li>Mide dos o tres veces y usa la media. Hazlo siempre a la misma hora, preferiblemente por la
            mañana y en ayunas.</li>
          </ul>

          <h2>Ejemplo resuelto</h2>
          <p>Hombre de 175 cm, con 38 cm de cuello y 85 cm de cintura. La diferencia cintura − cuello es de
          47 cm. Aplicando la fórmula de la Marina se obtiene un porcentaje de grasa de aproximadamente
          <strong>17 %</strong>, que se sitúa en la categoría de "en forma" de la tabla siguiente.</p>

          <h2>Categorías orientativas (American Council on Exercise)</h2>
          <table class="data-table">
            <tr><th>Categoría</th><th>Hombres</th><th>Mujeres</th></tr>
            <tr><td>Grasa esencial</td><td>2 – 5 %</td><td>10 – 13 %</td></tr>
            <tr><td>Atletas</td><td>6 – 13 %</td><td>14 – 20 %</td></tr>
            <tr><td>En forma</td><td>14 – 17 %</td><td>21 – 24 %</td></tr>
            <tr><td>Aceptable</td><td>18 – 24 %</td><td>25 – 31 %</td></tr>
            <tr><td>Obesidad</td><td>25 % o más</td><td>32 % o más</td></tr>
          </table>
          <p>Ojo: mantenerse en el rango de "grasa esencial" no es un objetivo saludable, es el mínimo necesario
          para las funciones básicas del cuerpo.</p>

          <h2>Qué margen de error tiene</h2>
          <p>Los métodos de circunferencias, como el de la Marina de EE. UU. (Hodgdon y Beckett, 1984),
          comparten un error de unos pocos puntos porcentuales frente a técnicas de laboratorio como la
          absorciometría DEXA. Se ve afectado por la distribución de grasa de cada persona y por la precisión de
          la medición. Por eso es más útil para seguir cambios a lo largo del tiempo, midiendo siempre del mismo
          modo, que para conocer un porcentaje exacto.</p>

          <h2>Cuándo no es una buena herramienta</h2>
          <p>No es adecuada para menores, embarazadas ni personas con edemas o retención de líquidos marcada.
          Tampoco conviene obsesionarse con perseguir cifras muy bajas: la salud hormonal, el rendimiento y el
          estado de ánimo pueden verse afectados si se baja demasiado el porcentaje de grasa.</p>
"""

G["deficit-calorico"] = """
          <h2>Déficit diario según el ritmo de pérdida</h2>
          <table class="data-table">
            <tr><th>Ritmo</th><th>Déficit diario aproximado</th><th>Para quién suele encajar</th></tr>
            <tr><td>0,25 kg/semana</td><td>275 kcal</td><td>Poco margen de grasa, entrenamiento exigente</td></tr>
            <tr><td>0,5 kg/semana</td><td>550 kcal</td><td>Punto de partida razonable para muchas personas</td></tr>
            <tr><td>0,75 kg/semana</td><td>825 kcal</td><td>Más grasa que perder; requiere vigilar proteína y energía</td></tr>
            <tr><td>1 kg/semana</td><td>1.100 kcal</td><td>Solo en periodos cortos y con supervisión</td></tr>
          </table>
          <p>El cálculo parte de la equivalencia aproximada de 7.700 kcal por kilo de grasa. Es una
          simplificación útil, pero el cuerpo se adapta: al perder peso, el gasto baja un poco, así que el ritmo
          real tiende a frenarse con el tiempo.</p>

          <h2>Ejemplo resuelto</h2>
          <p>Si tu TDEE es de 2.400 kcal y eliges 0,5 kg por semana, el déficit diario es
          (0,5 × 7.700) / 7 = 550 kcal, así que tu objetivo sería de unas <strong>1.850 kcal al día</strong>.
          Como referencia práctica, muchas personas se sienten mejor con déficits de entre el 10 y el 25 % de su
          gasto: el ejemplo equivale a un 23 %.</p>

          <h2>Cómo proteger tu masa muscular mientras pierdes grasa</h2>
          <ul>
            <li>Mantén el entrenamiento de fuerza: es la señal principal para conservar músculo.</li>
            <li>Sube la proteína hacia la parte alta del rango (consulta la
            <a href="proteina.html">calculadora de proteína</a>).</li>
            <li>Evita déficits excesivos, que aumentan el riesgo de pérdida muscular y de fatiga.</li>
            <li>Cuida el sueño: dormir poco empeora el apetito, la recuperación y el rendimiento.</li>
          </ul>

          <h2>Cuándo detener o replantear un déficit</h2>
          <p>Si aparecen fatiga persistente, mal descanso, mareos, pérdida del ciclo menstrual, frío constante,
          irritabilidad marcada o una preocupación obsesiva por la comida, conviene subir las calorías y hablar
          con un profesional sanitario. Un déficit no debe usarse en embarazo, lactancia, en menores de edad ni
          con antecedentes de trastornos de la conducta alimentaria sin supervisión profesional.</p>

          <h2>Cómo saber si funciona</h2>
          <p>Pésate varias veces por semana y observa la media semanal. Es normal que el peso fluctúe uno o dos
          kilos por líquidos, sal, ciclo menstrual o digestión. Evalúa el progreso cada 2-3 semanas y solo
          entonces ajusta las calorías, en pasos pequeños.</p>
"""

G["rutinas"] = """
          <h2>Qué estructura elegir según tus días disponibles</h2>
          <table class="data-table">
            <tr><th>Días</th><th>Esquema</th><th>Ventaja principal</th></tr>
            <tr><td>3</td><td>Cuerpo completo (A/B/C)</td><td>Cada músculo se trabaja 3 veces por semana con margen de recuperación</td></tr>
            <tr><td>4</td><td>Torso / pierna (2 + 2)</td><td>Buen equilibrio entre volumen y recuperación</td></tr>
            <tr><td>5</td><td>Empuje / tirón / pierna + torso y pierna</td><td>Más volumen por sesión sin excesivo tiempo</td></tr>
            <tr><td>6</td><td>Empuje / tirón / pierna dos veces</td><td>Frecuencia 2 por grupo muscular, requiere buena recuperación</td></tr>
          </table>

          <h2>Volumen, frecuencia e intensidad: qué dice la evidencia</h2>
          <ul>
            <li><strong>Frecuencia:</strong> un metaanálisis (Schoenfeld y cols., 2016) sugiere que entrenar cada
            grupo muscular al menos dos veces por semana es algo mejor para hipertrofia que una sola vez, con el
            volumen igualado.</li>
            <li><strong>Volumen:</strong> a nivel semanal, cifras de unas 10 series o más por grupo muscular se
            asocian con mayores ganancias que volúmenes más bajos (Schoenfeld y cols., 2017). Los principiantes
            progresan con volúmenes menores.</li>
            <li><strong>Cercanía al fallo:</strong> terminar las series con 1-3 repeticiones en reserva suele ser
            una buena estrategia para progresar sin acumular fatiga excesiva.</li>
          </ul>

          <h2>Ejemplo de sesión "Tren superior A" (hipertrofia, nivel intermedio)</h2>
          <table class="data-table">
            <tr><th>Ejercicio</th><th>Series × repeticiones</th></tr>
            <tr><td>Press banca con barra o mancuernas</td><td>4 × 6-10</td></tr>
            <tr><td>Remo con barra o en máquina</td><td>4 × 8-10</td></tr>
            <tr><td>Press militar sentado</td><td>3 × 8-12</td></tr>
            <tr><td>Dominadas o jalón al pecho</td><td>3 × 8-12</td></tr>
            <tr><td>Elevaciones laterales</td><td>3 × 12-15</td></tr>
            <tr><td>Curl de bíceps y extensión de tríceps</td><td>2 × 10-15 cada uno</td></tr>
          </table>

          <h2>Cómo progresar semana a semana</h2>
          <p>Un método sencillo es la doble progresión: elige un rango de repeticiones (por ejemplo, 8-12) y
          usa el mismo peso hasta que consigas el máximo del rango en todas las series; entonces sube la carga
          un poco y vuelve a empezar desde la parte baja del rango. Registra tus entrenamientos para saber qué
          hiciste la semana anterior.</p>

          <h2>Calentamiento, descanso y descargas</h2>
          <ul>
            <li>Empieza cada sesión con 5-10 minutos de movilidad y series de aproximación en el primer ejercicio.</li>
            <li>Descansa entre 2 y 3 minutos en ejercicios pesados y 60-90 segundos en los de aislamiento.</li>
            <li>Cada 6-8 semanas, considera una semana más ligera (descarga) si notas fatiga acumulada.</li>
            <li>Duerme entre 7 y 9 horas: es cuando se consolida gran parte de la recuperación.</li>
          </ul>

          <h2>Importante</h2>
          <p>Esta herramienta propone una estructura general, no una prescripción personalizada. Si tienes
          lesiones, dolor, una condición médica o mucha experiencia previa, conviene que un entrenador
          cualificado adapte la programación. Usa la <a href="1rm.html">calculadora de 1RM</a> para elegir
          cargas iniciales.</p>
"""

G["plan-comidas"] = """
          <h2>Cómo se convierten los porcentajes en gramos</h2>
          <p>Las calorías por gramo son aproximadamente: <strong>proteína 4 kcal, carbohidratos 4 kcal y
          grasas 9 kcal</strong>. Para pasar un porcentaje a gramos se multiplica primero por las calorías totales
          y luego se divide entre las kcal por gramo del nutriente.</p>

          <h2>Ejemplo resuelto: 2.200 kcal con reparto 30 / 40 / 30</h2>
          <table class="data-table">
            <tr><th>Macronutriente</th><th>Cálculo</th><th>Gramos al día</th></tr>
            <tr><td>Proteína (30 %)</td><td>2.200 × 0,30 / 4</td><td>165 g</td></tr>
            <tr><td>Carbohidratos (40 %)</td><td>2.200 × 0,40 / 4</td><td>220 g</td></tr>
            <tr><td>Grasas (30 %)</td><td>2.200 × 0,30 / 9</td><td>73 g</td></tr>
          </table>
          <p>Repartido en cuatro comidas, cada una tendría unas 550 kcal, con aproximadamente 41 g de proteína,
          55 g de carbohidratos y 18 g de grasa.</p>

          <h2>Rangos de referencia generales</h2>
          <p>Las guías dietéticas de las Academias Nacionales de EE. UU. sitúan los rangos aceptables de
          distribución de macronutrientes en adultos en 10-35 % de las calorías como proteína, 45-65 % como
          carbohidratos y 20-35 % como grasas. Los repartos de esta calculadora se mueven en torno a esos
          márgenes; la opción "bajo en carbohidratos" (50 % de grasas) queda fuera del rango habitual y es mejor
          valorarla con un profesional si tienes alguna condición de salud.</p>

          <h2>Cómo montar tus comidas sin obsesionarte</h2>
          <ul>
            <li>Empieza por la proteína: una ración de carne, pescado, huevos, lácteos, legumbres o tofu por comida.</li>
            <li>Añade una fuente de carbohidratos (arroz, patata, pan integral, pasta, fruta, legumbres) según lo
            que necesite tu gasto y tu entrenamiento.</li>
            <li>Suma verduras en abundancia por la fibra y los micronutrientes: aportan pocas calorías y mucha
            saciedad.</li>
            <li>Ajusta las grasas (aceite de oliva, frutos secos, aguacate, pescado azul) al final para cuadrar
            calorías.</li>
          </ul>

          <h2>Límites de este planificador</h2>
          <p>Reparte los macros a partes iguales entre comidas, lo que es cómodo pero no obligatorio. Tampoco
          tiene en cuenta alergias, intolerancias ni condiciones médicas. Si necesitas un plan personalizado, un
          dietista-nutricionista colegiado puede diseñarlo a tu medida. Para calcular tu punto de partida, usa
          la <a href="calorias.html">calculadora de calorías</a> y la <a href="proteina.html">de proteína</a>.</p>
"""
