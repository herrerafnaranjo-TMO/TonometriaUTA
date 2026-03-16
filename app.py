import streamlit as st
import pandas as pd  # <--- ESTA LÍNEA ES LA QUE FALTA O FUE SOBREESCRITA
import numpy as np

# --- INYECCIÓN DE ESTILO CUSTOM (CSS) ---
st.markdown("""
    <style>
    /* Cambiar el fondo de la página */
    .stApp {
        background-color: #f0f2f6;
    }
    /* Estilo para los Títulos (Headers) */
    h1, h2, h3 {
        color: #0e1117;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Resaltar los Metrics */
    [data-testid="stMetricValue"] {
        color: #1f77b4;
        font-weight: bold;
    }
    /* Personalizar los cuadros de Info/Warning */
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Configuración con Academic Rigor
st.set_page_config(page_title="EBCD-SS: Tonometry & Glaucoma", layout="wide")

# Esto define la paleta de colores académica
st.markdown("""
    <style>
    :root {
        --primary-color: #003366; /* Azul Marino Académico */
        --background-color: #ffffff;
        --secondary-background-color: #e6e9ef;
        --text-color: #262730;
        --font: "sans serif";
    }
    </style>
""", unsafe_allow_html=True)


# --- SECCIÓN 1: INTRODUCCIÓN Y FUNDAMENTOS ---
st.title("🔬 Presión Intraocular y Tonometría en el Glaucoma")
st.markdown(f"**Fundamentos del Glacucoma** | Universidad de Tarapacá: Tecnología Médica en Oftalmología y Optometría")

# Texto de Introducción depurado
st.markdown("""
### Introducción
La **Presión Intraocular (PIO)** es un factor fundamental en la salud ocular y tiene una relación crítica con el **Glaucoma**. 
En esta plataforma se abordan conceptos básicos de la dinámica del humor acuoso, la fisiología de la PIO, tecnologías de medición 
y la relevancia clínica de la tonometría en la práctica del Tecnólogo Médico.

La PIO no debe ser un valor considerado de forma aislada; es una variable dinámica que depende de **factores biomecánicos y fisiológicos**.
""")

# Perla Clínica con Rigor Académico
st.warning("""
**💡 PERLA CLÍNICA:** La PIO es el único factor de riesgo modificable con evidencia sólida (Estudios multicéntricos **EGPS**, **UKGTS** y **OHTS**) 
para detener o ralentizar la progresión del daño glaucomatoso.
""")

# Glosario de Pregrado (Interactivo)
with st.expander("📖 Glosario de Términos"):
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.write("**Presión intraocular (PIO):** Valor expresado en mmHg que corresponde a la tensión que ejerce el contenido del interior del ojo hacia las paredes del globo ocular.")
        st.write("**Tonometría:** Procedimiento clínico que estima de forma indirecta la PIO.")
        st.write("**Humor acuoso:** Fluido incoloro que circula por la cámara anterior y mantiene el metabolismo de estructuras cercanas.")
    with col_g2:
        st.write("**Factor de riesgo:** Atributo que aumenta la probabilidad de desarrollar una patología o su progresión. Pueden ser modificables o no.")
        st.write("**Estudio multicéntrico:** Investigación realizada simultáneamente en diversas instituciones sobre intervenciones terapéuticas o diagnósticas.")


# --- MÓDULO 1: CONCEPTOS BÁSICOS DE PRESIÓN INTRAOCULAR ---
st.header("1. Conceptos Básicos de Presión Intraocular")

st.markdown("""
La PIO es la presión del fluido dentro del globo ocular y depende de tres factores fundamentales de la biomecánica y fisiología:
""")

# --- 1. PRODUCCIÓN ---
with st.expander("1. Producción de Humor Acuoso", expanded=True):
        st.write("**Tasa de formación:** 1.3 a 3.0 µl/min.")
        st.write("**Origen:** Crestas de los procesos ciliares (*Pars Plicata*) en el cuerpo ciliar [Ref 2].")
        st.info("""
        **Aspectos relevantes:**
        * **Ritmo circadiano:** La producción es el doble por la mañana que durante el sueño.
        * **Factores que disminuyen la producción:** Diabetes mellitus, distrofia miotónica y envejecimiento.
        * **Factores que no influyen en la producción:** PEX, Dispersión pigmentaria, GPAA e Hipertensión ocular [Ref 3].
        """)
        st.info("💡 ¡No se confunda, algunos conceptos se aprenderán pronto!")

# --- 2. SALIDA (Estructurado en Expander) ---
with st.expander("2. Salida del Humor Acuoso", expanded=False):
    st.write("Tasa normal: **0.1 a 0.4 µl/min/mmHg**. Se divide en dos rutas críticas:")

    tab_trab, tab_uveo = st.tabs(["Vía Trabecular (Convencional)", "Vía Uveoescleral (No Convencional)"])

    with tab_trab:
        st.markdown("### Sistema Trabecular (70% - 95%)")
        st.write("**Ruta:** Malla trabecular → Porción yuxtacanalicular → Canal de Schlemm → Canales colectores → Venas epiesclerales.")
        st.warning("**Punto Crítico:** La porción yuxtacanalicular genera la mayor resistencia al flujo [Ref 3, 4].")
        st.error("📉 Reducida en: GPAA, PEX, Dispersión pigmentaria e Hipertensión ocular.")
        
        # Inserción de la observación técnica
        st.info("""
        **Nota Técnica:** Valores menores a 0.1 µl/min/mmHg son patológicos. 
        En PIO muy alta, la facilidad de salida (C) suele estar colapsada, impidiendo la compensación del globo ocular.
        """)

    with tab_uveo:
        st.markdown("### Sistema Uveoescleral")
        st.write("**Ruta:** Raíz del iris → Espacios intersticiales del músculo ciliar → Espacio supracoroideo [Ref 5].")
        st.info("""
        **Dinámica Temporal:** Con el envejecimiento, esta vía se reduce, aumentando la dependencia del sistema trabecular.
        * **Uveítis:** Flujo aumentado (por cambios en el músculo ciliar).
        * **Hipertensión Ocular:** Flujo reducido.
        """)

# --- 3. PRESIÓN VENOSA ---
with st.expander("3. Presión Venosa Epiescleral"):
    st.write("**Valor normal:** 8 a 10 mmHg.")
    st.write("**Determinantes:** Posición corporal, temperatura, inhalación de O2 y drogas vasoactivas [Ref 3].")
    st.caption("Nota: Su medida precisa es difícil en la práctica clínica diaria.")

# --- SIMULADOR INTERACTIVO DE GOLDMANN ---
st.subheader("🎮 Simulador de Dinámica de Fluidos (Goldmann)")
st.markdown("""
Selecciona una condición clínica para observar cómo cambian las variables de la ecuación: 
$P_o = (F / C) + P_e$
""")

# Selector de escenario clínico
escenario = st.selectbox("Seleccione Escenario Clínico:", 
                         ["Ojo Sano", "Glaucoma de Ángulo Abierto", "Hipertensión Ocular", 
                          "Diabetes Mellitus", "Uveítis Anterior", "Envejecimiento (Adulto Mayor)"])

# Lógica de parámetros según escenario (Valores aproximados para fines pedagógicos)
# F (Tasa formación), C (Facilidad salida), Pe (Presión venosa)
if escenario == "Ojo Sano":
    f, c, pe = 2.5, 0.25, 9.0
    desc = "Equilibrio fisiológico normal."
elif escenario == "Glaucoma de Ángulo Abierto":
    f, c, pe = 2.5, 0.08, 9.5
    desc = "Resistencia crítica en la malla yuxtacanalicular. C muy bajo."
elif escenario == "Hipertensión Ocular":
    f, c, pe = 2.8, 0.12, 10.0
    desc = "Facilidad de salida reducida, pero aún compensada parcialmente."
elif escenario == "Diabetes Mellitus":
    f, c, pe = 1.8, 0.22, 9.0
    desc = "La tasa de formación (F) disminuye en pacientes diabéticos."
elif escenario == "Uveítis Anterior":
    f, c, pe = 2.0, 0.15, 8.0 
    desc = "PIO suele ser baja por hiposecreción ciliar y aumento de vía uveoescleral."
elif escenario == "Envejecimiento (Adulto Mayor)":
    f, c, pe = 2.0, 0.20, 9.0
    desc = "Reducción fisiológica de la formación (F) y de la vía uveoescleral."

# Sliders interactivos pre-cargados con el escenario
st.markdown(f"**Análisis de Escenario:** {desc}")
col_sim1, col_sim2 = st.columns([1, 1])

with col_sim1:
    f_val = st.slider("F (Tasa de Formación µl/min)", 1.0, 4.0, f, 0.1)
    c_val = st.slider("C (Facilidad de Salida µl/min/mmHg)", 0.01, 0.5, c, 0.01)
    pe_val = st.slider("Pe (Presión Venosa mmHg)", 5.0, 15.0, pe, 0.5)

# Cálculo de la PIO resultante
pio_res = (f_val / c_val) + pe_val

with col_sim2:
    st.metric("PIO Resultante (Po)", f"{pio_res:.1f} mmHg", 
              delta=f"{pio_res - 15.7:.1f} vs Media", delta_color="inverse")
    
    # Visualización de la Resistencia (Inverso de C)
    resistencia = 1 / c_val
    st.write(f"**Resistencia al flujo:** {resistencia:.2f} mmHg/(µl/min)")
    st.progress(min(resistencia / 50, 1.0)) # Barra de resistencia
    st.caption("Resistencia en la porción yuxtacanalicular")

# Mensaje Constructivista Tajante
if c_val < 0.1:
    st.error("⚠️ ALERTA: La facilidad de salida (C) es patológica. El riesgo de daño axonal aumenta exponencialmente.")



# --- MÓDULO 2: DEFINICIÓN Y DETERMINANTES DE LA PIO ---
st.header("2. Definición y Determinantes de la PIO")

# --- PIO NORMAL Y RELACIÓN CON GLAUCOMA ---
col_norm1, col_norm2 = st.columns([1.5, 1])

with col_norm1:
    st.subheader("El Concepto de PIO Normal")
    st.markdown("""
    Se define como la presión presente en individuos sanos, sin evidencia de daño estructural (excavación del nervio óptico) 
    ni funcional (pérdida de campo visual).
    
    * **Promedio poblacional:** Aproximadamente **15.7 mmHg** (± 2.5) [Ref 7-9].
    * **Distribución:** Sigue una curva de Gauss con un sesgo (*skewness*) hacia las presiones más altas.
    """)
    
    st.info("""
    **Rigor Académico:** La PIO **no forma parte de la definición de glaucoma**, pero es el único factor de riesgo 
    causal sobre el cual podemos intervenir para demorar el daño axonal [Ref 10-13].
    """)

with col_norm2:
    # Espacio para gráfico de distribución (Simulado con métricas)
    st.write("**Distribución Estadística**")
    st.metric("Media Poblacional", "15.7 mmHg")
    st.metric("Límite Superior Sugerido", "21.0 mmHg", delta="+2 Desviaciones Estándar")

# --- FACTORES DETERMINANTES ---
st.subheader("Factores Determinantes")

with st.expander("Ver determinantes Genéticos, Ambientales y Físicos"):
    f_gen, f_amb, f_fis = st.columns(3)
    
    with f_gen:
        st.markdown("**Genéticos**")
        st.write("Existen múltiples loci en cromosomas relacionados con la PIO [Ref 14].")
        
    with f_amb:
        st.markdown("**Químicos y Ambientales**")
        st.success("⬇️ Bajan: Aire frío, LSD, Ketamina [Ref 15].")
        st.error("⬆️ Elevan: Tabaco, Heroína, Succinilcolina [Ref 16].")
        
    with f_fis:
        st.markdown("**Físicos**")
        st.write("Elevan la PIO: Maniobra de Valsalva, instrumentos de viento, inclinación del cuerpo.")
        st.write("Mecanismo: Probablemente por aumento de la presión venosa epiescleral [Ref 17].")

# --- SUB-MÓDULO: HEMODINÁMICA Y RIESGO EPIDEMIOLÓGICO ---
st.divider()
st.subheader("🩺 Hemodinámica: Presión de Perfusión Ocular Media (PPOM)")

st.markdown("""
La PPOM evalúa el equilibrio entre la presión arterial y la PIO. Aunque el coeficiente **2/3** es una estimación general para compensar la resistencia vascular y gravedad, es el estándar en estudios como el **Barbados Eye Study**.
""")

# --- CALCULADORA DE RIESGO VASCULAR ---
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1: pas = st.number_input("Sistólica (PAS)", 70, 200, 120)
    with c2: pad = st.number_input("Diastólica (PAD)", 40, 130, 80)
    with c3: pio_ppom = st.number_input("PIO Actual (mmHg)", 5, 60, 16)

# Cálculos
pam = pad + (1/3 * (pas - pad))
ppom = (2/3 * pam) - pio_ppom

# Mostrar Resultados con Código de Colores Epidemiológico
if ppom < 45:
    color_ppom = "inverse" 
    status = "🔴 RIESGO ALTO"
    obs = "Fuerte asociación con progresión glaucomatosa (Barbados Eye Study)."
    # Renderizado explícito de la observación
    st.metric("Resultado PPOM", f"{ppom:.1f} mmHg", delta=status, delta_color=color_ppom)
    st.error(f"**Observación:** {obs}") 

elif 45 <= ppom <= 55:
    color_ppom = "normal" 
    status = "🟡 RIESGO MODERADO"
    obs = "Requiere monitoreo si existen otros factores de riesgo o daño estructural."
    st.metric("Resultado PPOM", f"{ppom:.1f} mmHg", delta=status, delta_color=color_ppom)
    st.warning(f"**Observación:** {obs}")

else:
    color_ppom = "normal" 
    status = "🟢 RIESGO BAJO"
    obs = "Perfil hemodinámico estable según modelos actuales."
    st.metric("Resultado PPOM", f"{ppom:.1f} mmHg", delta=status, delta_color=color_ppom)
    st.success(f"**Observación:** {obs}")

# --- CRÍTICA METODOLÓGICA (CONSTRUCTIVISMO) ---
with st.expander("Análisis de Exactitud Científica y Limitaciones"):
    st.markdown(f"""
    **¿Por qué el factor 2/3 no es una constante universal?**
    1. **Variabilidad Individual:** Estudios Doppler muestran que la presión en la arteria oftálmica varía entre el **60% y 75%** de la PAM sistémica.
    2. **Falla de Autorregulación:** La fórmula asume una autorregulación perfecta, la cual suele estar dañada en pacientes con **Diabetes** o **Glaucoma**.
    3. **Sesgo Poblacional:** Un valor de 50 mmHg puede ser suficiente para un ojo sano, pero insuficiente en un paciente con microangiopatía.
    
    **Punto Crítico:** Valores de PPOM < 48 mmHg pueden aumentar hasta **6.6 veces** el riesgo de glaucoma de ángulo abierto.
    """)



# --- MÓDULO 3: TONOMETRÍA E INSTRUMENTACIÓN ---
st.header("3. Tonometría: Instrumentación y Errores Sistemáticos")

# 1. Teoría de la Aplanación (Imbert-Fick)
with st.expander("Física de la Medición: Principio de Imbert-Fick", expanded=True):
    st.markdown("""
    El tonómetro de Goldmann se basa en la ley de Imbert-Fick, que para una esfera seca de pared delgada establece:""")  
    st.latex(r"W = P_t \times A")
    
    st.markdown("""Sin embargo, el ojo humano es húmedo y posee rigidez estructural. La **Fórmula Modificada** es:
    """)
    st.latex(r"W + S = P_t \times A + B")
    st.markdown("""
    * **W:** Fuerza aplicada por el tonómetro.
    * **S:** Tensión superficial del menisco lagrimal.
    * **B:** Fuerza requerida para vencer la rigidez corneal (*Bending force*).
    
    **Rigor Técnico:** Con un diámetro de aplanación de **3.06 mm**, las fuerzas **S** y **B** se cancelan mutuamente, permitiendo que la fuerza aplicada sea una lectura directa de la PIO.
    """)

# --- SIMULADOR DE ERRORES GAT REFINADO ---
st.subheader("Simulador de Errores en Tonometría de Goldmann (GAT)")

col_err1, col_err2 = st.columns(2)

with col_err1:
    st.markdown("**Variables Procedimentales:**")
    fluo = st.radio("Menisco de Fluoresceína:", ["Normal", "Exceso", "Insuficiente"], key="f_err")
    align = st.checkbox("Semicírculos desiguales verticalmente", key="a_err")
    astig = st.selectbox("Astigmatismo Corneal (>3.00 D):", ["Ninguno", "A favor de la regla", "En contra de la regla"], key="ast_err")

with col_err2:
    st.markdown("**Impacto en el Razonamiento Clínico:**")
    
    # Inicializamos el balance de error
    errores = []
    efecto_final = 0 # 0: Neutro, >0: Sobreestima, <0: Subestima

    if fluo == "Exceso":
        errores.append("⬆️ Exceso de Fluoresceína (Sobreestima)")
        efecto_final += 1
    elif fluo == "Insuficiente":
        errores.append("⬇️ Déficit de Fluoresceína (Subestima)")
        efecto_final -= 1
        
    if align:
        errores.append("⬆️ Mala alineación vertical (Sobreestima)")
        efecto_final += 1
        
    if astig == "A favor de la regla":
        errores.append("⬆️ Astigmatismo a favor (Sobreestima)")
        efecto_final += 1
    elif astig == "En contra de la regla":
        errores.append("⬇️ Astigmatismo en contra (Subestima)")
        efecto_final -= 1

    # Mostramos la lista de errores detectados
    for e in errores:
        st.write(e)

    # Diagnóstico Final Tajante
    st.divider()
    if efecto_final > 0:
        st.error(f"**EFECTO NETO: SOBREESTIMACIÓN.** El valor de PIO medido es artificialmente alto. Confianza del dato: BAJA.")
    elif efecto_final < 0:
        st.error(f"**EFECTO NETO: SUBESTIMACIÓN.** ¡Peligro! Podrías estar omitiendo un glaucoma. Confianza del dato: BAJA.")
    else:
        if not errores:
            st.success("Técnica Correcta: El valor es confiable.")
        else:
            st.warning("**EFECTO INDETERMINADO.** Los errores se compensan entre sí, pero la técnica es deficiente. Repetir medición.")



# 3. Comparativa de Tecnologías
st.subheader("Selección de Tecnología Según Contexto Clínico")

devices_data = {
    "Córnea Normal / Cooperador": ["Goldmann (GAT) / Perkins", "Gold Standard. Requiere anestesia y fluoresceína."],
    "Niño o No Cooperador": ["Rebote (iCare)", "No requiere anestesia. Ideal para screening pediátrico [Ref 22]."],
    "Córnea Irregular / Edema": ["Tono-Pen", "Transductor de 1 mm. Mejor para superficies no uniformes [Ref 18]."],
    "Queratoprótesis de Boston": ["Schiotz (Limbar)", "Indentación. Útil cuando la córnea central es inaccesible [Ref 20]."],
    "Córnea Anormal / Cicatriz": ["Pneumotonómetro", "Punta de silicón de 5 mm. Menos sensible a irregularidades [Ref 21]."],
    "Alteración Biomecánica": ["ORA / Contorno Dinámico", "Miden histéresis o acoplamiento hidrostático. Menos afectados por CCT."]
}

case_type = st.selectbox("Situación Clínica del Paciente:", list(devices_data.keys()))

st.success(f"**Dispositivo Recomendado:** {devices_data[case_type][0]}")
st.write(f"**Justificación:** {devices_data[case_type][1]}")

# 4. Tabla Maestra de Referencia
with st.expander("Tabla Maestra de Instrumentación"):
    df_tech = pd.DataFrame({
        "Dispositivo": ["No Contacto (Aire)", "ORA", "Sensores Continuos"],
        "Características": ["Sin riesgo de contagio", "Mide histéresis corneal", "Lentes de contacto (Triggerfish)"],
        "Acuerdo con GAT": ["66% dentro de 2 mmHg", "Aporta factor de corrección", "Requiere más estudios de exactitud"]
    })
    st.table(df_tech)

# --- MÓDULO 4: CCT, BIOMECÁNICA Y RIESGO (Análisis Estructural) ---
st.header("El Factor Corneal en la Tonometría")
st.subheader("Central Corneal Thickness (CCT)")
st.write("""
      El espesor corneal es la fuente de error sistemático más documentada. Partiendo de un valor medio de 520 µm: 
      * **Córneas gruesas:** Sobreestiman la PIO.
      * **Córneas delgadas:** Subestiman la PIO.
      * **Curvatura:** Córneas planas subestiman la PIO [Ref 35].
      """)
st.info("**OHTS Evidence:** Un CCT delgado es un factor de riesgo independiente para la conversión a Glaucoma [Ref 12].")



# --- MÓDULO 4: EPIDEMIOLOGÍA Y VALOR PREDICTIVO ---
st.header("4. Epidemiología y Estadística Clínica")

with st.expander("Causalidad: ¿La PIO causa Glaucoma?", expanded=True):
    st.markdown("""
    La relación causa-efecto está respaldada por:
    * **Modelos Experimentales:** Elevaciones inducidas provocan excavación papilar típica [Ref 24, 25].
    * **Evidencia Clínica:** Glaucoma unilateral post-cierre angular agudo y correlación directa en asimetría de daño [Ref 26, 27].
    """)

# Factores Epidemiológicos
st.subheader("Determinantes Epidemiológicos")
col_epi1, col_epi2, col_epi3 = st.columns(3)

with col_epi1:
    st.markdown("**Edad**")
    st.caption("Resultados controvertidos. Varía según la población (ej. descenso en Japón) [Ref 30-32].")

with col_epi2:
    st.markdown("**Raza**")
    st.caption("Mayor prevalencia en Hispanos y Africanos, pero no es un marcador útil para diferenciar niveles de PIO [Ref 32-34].")

with col_epi3:
    st.markdown("**Oculometría**")
    st.caption("La miopía es un factor leve. El largo axial no correlaciona con la PIO medida por manometría [Ref 35].")

# La Paradoja del Tamizaje (Screening)
st.divider()
st.subheader("Análisis del Valor Predictivo (Corte 21 mmHg)")
col_val1, col_val2 = st.columns(2)

with col_val1:
    st.metric("Falsos Positivos (OHT)", "Elevado")
    st.write("Sujetos con PIO > 21 mmHg que **nunca** desarrollan daño glaucomatoso [Ref 12, 38].")

with col_val2:
    st.metric("Falsos Negativos (GNT)", "30% - 90%")
    st.error("**Rigor Académico:** La gran mayoría de los pacientes con glaucoma tienen PIO normal al momento del diagnóstico [Ref 29, 39-42].")

# --- MÓDULO 5: FLUCTUACIÓN Y VARIACIONES ---
st.header("5. Variaciones y Fluctuación de la PIO")

with st.expander("Glosario de Variación Temporal"):
    st.markdown("""
    * **Fluctuación a corto plazo:** Cambios en ≤ 24 horas.
    * **Fluctuación a largo plazo:** Cambios entre visitas diferentes [Ref 49].
    * **Pico (Peak):** Valor máximo registrado.
    * **Valle:** Valor mínimo registrado.
    """)

# Significado Clínico y Controversia
st.subheader("Importancia de la Dinámica Temporal")
st.info("""
**Controversia en Progresión:** Mientras algunos estudios (EMGT) no hallan asociación clara [Ref 56, 57], otros sugieren que la fluctuación es un factor de riesgo independiente, especialmente en presiones bajas [Ref 50, 58, 59].
""")

# Simulación de Curva Diurna
st.markdown("### Visualización de la Curva de Tensión Diurna")
horas = ["08:00", "11:00", "14:00", "17:00", "20:00", "23:00", "02:00", "05:00"]
pio_valores = [18, 16, 15, 17, 19, 21, 24, 22] # Ejemplo de pico nocturno

df_curva = pd.DataFrame({"Hora": horas, "PIO (mmHg)": pio_valores})
st.line_chart(df_curva.set_index("Hora"))

st.warning("""
**Dificultad Estadística:** Es complejo determinar si el daño se debe a la variabilidad per se o simplemente a que una mayor fluctuación aumenta la probabilidad de alcanzar picos hipertensivos peligrosos.
""")
