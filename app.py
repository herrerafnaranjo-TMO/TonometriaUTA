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
# Centrado de Imagen de Anatomía
c1, c2, c3 = st.columns([1, 2, 1]) # Crea tres espacios, el del medio es el doble de ancho
with c2:
    st.image("img/dinamicaha.png", caption="Figura 1. Dinámica del humor acuoso.", use_container_width=True)

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
    
   # Control de tamaño para el Endpoint de Goldmann
c_m1, c_m2, c_m3 = st.columns([1.5, 1, 1.5]) 
with c_m2:
    st.image("img/mirassemicirculos.jpg", caption="Figura 2. Endpoint ideal (GAT).", use_container_width=True)

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

# Centrado de galería de errores
ce1, ce2, ce3 = st.columns([0.5, 3, 0.5]) # Columna central mucho más ancha para ver detalles
with ce2:
    st.image("img/errorestonometria.png", caption="Figura 3. Atlas de errores técnicos frecuentes.", use_container_width=True)


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

# --- SIMULADOR DE PIO CORREGIDA (IOP CORRECTION SIMULATOR) ---
st.markdown("---")
st.header("🔢 Simulador de Corrección de PIO según CCT")

# 1. Validación de Inputs (Data Integrity & Range Validation)
col_in1, col_in2 = st.columns(2)
with col_in1:
    pio_medida = st.number_input(
        "PIO Medida (mmHg):", 
        min_value=2.0, max_value=70.0, value=15.0, step=1.0,
        help="Presión obtenida por tonometría de aplanación (GAT)."
    )
with col_in2:
    cct_paciente = st.number_input(
        "Paquimetría Central (µm):", 
        min_value=300, max_value=850, value=540, step=5,
        help="Espesor corneal central medido por paquimetría ultrasónica u óptica."
    )

# 2. Lógica de Alertas de Seguridad (Clinical Red Flags)
if pio_medida > 30:
    st.error("⚠️ **Alerta:** Presión muy elevada. Sospechar Glaucoma de ángulo cerrado o error de calibración.")
elif pio_medida < 8:
    st.warning("⚠️ **Alerta:** Hipotonía ocular. Revisar posible filtración o desprendimiento ciliar.")

if cct_paciente < 450 or cct_paciente > 620:
    st.info("💡 **Nota:** Esta córnea tiene un espesor atípico. El factor de corrección tiene mayor margen de error.")

# 3. Cálculo de la PIO Corregida (Ehlers/Dresdner Approximation)
factor_corr = ((cct_paciente - 545) / 10) * 0.7
pio_corregida = pio_medida - factor_corr

# 4. Despliegue de Resultados e Interpretación Didáctica
st.subheader(f"Estimación de PIO Corregida: {pio_corregida:.1f} mmHg")

if cct_paciente < 545:
    st.info(f"💡 **Interpretación:** La córnea es delgada. La PIO real es probablemente **MAYOR** que la medida (se sumaron {abs(factor_corr):.1f} mmHg).")
elif cct_paciente > 545:
    st.info(f"💡 **Interpretación:** La córnea es gruesa. La PIO real es probablemente **MENOR** que la medida (se restaron {abs(factor_corr):.1f} mmHg).")
else:
    st.success("✅ Córnea con espesor promedio. No se requiere ajuste teórico.")

# 5. Nota Docente de Rigor (Evidence-Based Practice Disclaimer)
st.warning("""
**Nota Docente:** La 'PIO Corregida' es solo una estimación teórica. 
En la clínica, no se debe ajustar la presión solo por paquimetría; 
se debe evaluar integralmente el nervio óptico y el campo visual. 
*(Referencia: OHTS Guidelines)*.
""")


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

# --- SECCIÓN DE REFERENCIAS BIBLIOGRÁFICAS (REFERENCES) ---
st.markdown("---") # Línea divisoria para separar del simulador

with st.expander("📚 Ver Referencias Bibliográficas (59 fuentes)"):
    st.markdown("### Bibliografía y Evidencia Científica")
    st.write("La siguiente lista contiene la evidencia que sustenta los algoritmos y conceptos de esta plataforma:")
    
    referencias = [
        "1.	Brubaker RF. Clinical measurements of aqueous dynamics: implications for addressing glaucoma. In: Civan MM, ed. The Eye's Aqueous Humor, From Secretion to Glaucoma. New York, NY: Academic Press; 1998:234-284."
        "2.	Tamm ER, Lutjen-Drecoll E. Ciliary body. Microscopy research and technique. Apr 1 1996;33(5):390-439."
        "3.	Weinreb R, Brandt JD, Garway-Heath DF, Medeiros FA. Intraocular Pressure. World Glaucoma Association Consensus Series. The Hague, The Netherlands: Kugler Publications; 2007."
        "4.	Tripathi RC. Mechanism of the aqueous outflow across the trabecular wall of Schlemm's canal. Exp Eye Res. Jan 1971;11(1):116-121."
        "5.	Alm A, Nilsson SF. Uveoscleral outflow--a review. Exp Eye Res. Apr 2009;88(4):760-768."
        "6.	Toris CB, Yablonski ME, Wang YL, Camras CB. Aqueous humor dynamics in the aging human eye. Am J Ophthalmol. Apr 1999;127(4):407-412."
        "7.	Nemesure B, Honkanen R, Hennis A, Wu SY, Leske MC, Barbados Eye Studies G. Incident open-angle glaucoma and intraocular pressure. Ophthalmology. Oct 2007;114(10):1810-1815."
        "8.	Leydhecker W, Akiyama K, Neumann HG. [Intraocular pressure in normal human eyes]. Klinische Monatsblatter fur Augenheilkunde und fur augenarztliche Fortbildung. 1958;133(5):662-670."
        "9.	Chan MP, Grossi CM, Khawaja AP, et al. Associations with Intraocular Pressure in a Large Cohort: Results from the UK Biobank. Ophthalmology. Apr 2016;123(4):771-782."
        "10.	Gillespie BW, Musch DC, Guire KE, et al. The collaborative initial glaucoma treatment study: baseline visual field and test-retest variability. Invest Ophthalmol Vis Sci. Jun 2003;44(6):2613-2620."
        "11.	Nouri-Mahdavi K, Hoffman D, Coleman AL, et al. Predictive factors for glaucomatous visual field progression in the Advanced Glaucoma Intervention Study. Ophthalmology. Sep 2004;111(9):1627-1635."
        "12.	Gordon MO, Beiser JA, Brandt JD, et al. The Ocular Hypertension Treatment Study: baseline factors that predict the onset of primary open-angle glaucoma. Arch Ophthalmol. Jun 2002;120(6):714-720; discussion 829-730."
        "13.	Drance SM. The Collaborative Normal-Tension Glaucoma Study and some of its lessons. Can J Ophthalmol. Feb 1999;34(1):1-6."
        "14.	Duggal P, Klein AP, Lee KE, Klein R, Klein BE, Bailey-Wilson JE. Identification of novel genetic loci for intraocular pressure: a genomewide scan of the Beaver Dam Eye Study. Arch Ophthalmol. Jan 2007;125(1):74-79."
        "15.	Ortiz GJ, Cook DJ, Yablonski ME, Masonson H, Harmon G. Effect of cold air on aqueous humor dynamics in humans. Invest Ophthalmol Vis Sci. Jan 1988;29(1):138-140."
        "16.	Mehra KS, Roy PN, Khare BB. Tobacco smoking and glaucoma. Ann Ophthalmol. Apr 1976;8(4):462-464."
        "17.	Rafuse PE, Mills DW, Hooper PL, Chang TS, Wolf R. Effects of Valsalva's manoeuvre on intraocular pressure. Can J Ophthalmol. Apr 1994;29(2):73-76."
        "18.	Iester M, Mermoud A, Achache F, Roy S. New Tonopen XL: comparison with the Goldmann tonometer. Eye. Feb 2001;15(Pt 1):52-58."
        "19.	Kim NR, Kim CY, Kim H, Seong GJ, Lee ES. Comparison of goldmann applanation tonometer, noncontact tonometer, and TonoPen XL for intraocular pressure measurement in different types of glaucomatous, ocular hypertensive, and normal eyes. Current eye research. Apr 2011;36(4):295-300."
        "20.	Estrovich IE, Shen C, Chu Y, et al. Schiotz tonometry accurately measures intraocular pressure in Boston type 1 keratoprosthesis eyes. Cornea. Jun 2015;34(6):682-685."
        "21.	Lin CC, Chen A, Jeng BH, Porco TC, Ou Y, Han Y. Scleral intraocular pressure measurement in cadaver eyes pre- and postkeratoprosthesis implantation. Investigative ophthalmology & visual science. Apr 2014;55(4):2244-2250."
        "22.	Cook JA, Botello AP, Elders A, et al. Systematic review of the agreement of tonometers with Goldmann applanation tonometry. Ophthalmology. Aug 2012;119(8):1552-1557."
        "23.	Okafor KC, Brandt JD. Measuring intraocular pressure. Current opinion in ophthalmology. Mar 2015;26(2):103-109."
        "24.	Gaasterland D, Tanishima T, Kuwabara T. Axoplasmic flow during chronic experimental glaucoma. 1. Light and electron microscopic studies of the monkey optic nervehead during development of glaucomatous cupping. Invest Ophthalmol Vis Sci. Sep 1978;17(9):838-846."
        "25.	Quigley HA, Addicks EM. Chronic experimental glaucoma in primates. II. Effect of extended intraocular pressure elevation on optic nerve head and axonal transport. Invest Ophthalmol Vis Sci. Feb 1980;19(2):137-152."
        "26.	Cartwright MJ, Anderson DR. Correlation of asymmetric damage with asymmetric intraocular pressure in normal-tension glaucoma (low-tension glaucoma). Arch Ophthalmol. Jul 1988;106(7):898-900."
        "27.	Crichton A, Drance SM, Douglas GR, Schulzer M. Unequal intraocular pressure and its relation to asymmetric visual field defects in low-tension glaucoma. Ophthalmology. Sep 1989;96(9):1312-1314."
        "28.	Hollows FC, Graham PA. Intra-ocular pressure, glaucoma, and glaucoma suspects in a defined population. Br J Ophthalmol. Oct 1966;50(10):570-586."
        "29.	Bengtsson B. The prevalence of glaucoma. Br J Ophthalmol. Jan 1981;65(1):46-49."
        "30.	Leske MC, Connell AM, Wu SY, Hyman LG, Schachat AP. Risk factors for open-angle glaucoma. The Barbados Eye Study. Arch Ophthalmol. Jul 1995;113(7):918-924."
        "31.	Shiose Y, Kitazawa Y, Tsukahara S, et al. Epidemiology of glaucoma in Japan--a nationwide glaucoma survey. Jpn J Ophthalmol. 1991;35(2):133-155."
        "32.	Coleman A, Pasquale L, Girkin C, Bourne RR, Iwase A. Epidemiology of intraocular pressure. In: Weinreb R, Brandt JD, Garway-Heath DF, Medeiros FA, eds. Intraocular Pressure. Amsterdam: Kugler Publications; 2007:79-101."
        "33.	Torres RJ, Jones E, Edmunds B, Becker T, Cioffi GA, Mansberger SL. Central corneal thickness in Northwestern American Indians/Alaskan Natives and comparison with White and African-American persons. Am J Ophthalmol. Nov 2008;146(5):747-751."
        "34.	Sommer A, Tielsch JM, Katz J, et al. Relationship between intraocular pressure and primary open angle glaucoma among white and black Americans. The Baltimore Eye Survey. Arch Ophthalmol. 1991;109(8):1090-1095."
        "35.	Kohlhaas M, Boehm AG, Spoerl E, Pursten A, Grein HJ, Pillunat LE. Effect of central corneal thickness, corneal curvature, and axial length on applanation tonometry. Arch Ophthalmol. Apr 2006;124(4):471-476."
        "36.	Shih CY, Graff Zivin JS, Trokel SL, Tsai JC. Clinical significance of central corneal thickness in the management glaucoma. Arch Ophthalmol. Sep 2004;122(9):1270-1275."
        "37.	Wilson LB, Quinn GE, Ying GS, et al. The relation of axial length and intraocular pressure fluctuations in human eyes. Invest Ophthalmol Vis Sci. May 2006;47(5):1778-1784."
        "38.	Kass MA, Heuer DK, Higginbotham EJ, et al. The Ocular Hypertension Treatment Study: a randomized trial determines that topical ocular hypotensive medication delays or prevents the onset of primary open-angle glaucoma. Arch Ophthalmol. Jun 2002;120(6):701-713; discussion 829-730."
        "39.	Coffey M, Reidy A, Wormald R, Xian WX, Wright L, Courtney P. Prevalence of glaucoma in the west of Ireland. Br J Ophthalmol. Jan 1993;77(1):17-21."
        "40.	Kahn HA, Milton RC. Revised Framingham eye study prevalence of glaucoma and diabetic retinopathy. Am J Epidemiol. Jun 1980;111(6):769-776."
        "41.	Klein BE, Klein R, Sponsel WE, et al. Prevalence of glaucoma. The Beaver Dam Eye Study. Ophthalmology. Oct 1992;99(10):1499-1504."
        "42.	Tielsch JM, Sommer A, Katz J, Royall RM, Quigley HA, Javitt J. Racial variations in the prevalence of primary open-angle glaucoma. The Baltimore Eye Survey. Jama. 1991;266(3):369-374."
        "43.	Tielsch J, Katz J, Singh K. Population-based evaluation of glaucoma screening: The Baltimore Eye Survey. Am J Epidemiology. 1991;134:1102-1110."
        "44.	Sultan MB, Mansberger SL, Lee PP. Understanding the importance of IOP variables in glaucoma: a systematic review. Surv Ophthalmol. Nov-Dec 2009;54(6):643-662."
        "45.	Jonas JB, Budde WM, Stroux A, Oberacher-Velten IM, Junemann A. Diurnal intraocular pressure profiles and progression of chronic open-angle glaucoma. Eye. Apr 7 2006."
        "46.	Bengtsson B, Heijl A. Diurnal IOP fluctuation: not an independent risk factor for glaucomatous visual field loss in high-risk ocular hypertension. Graefes Arch. Clin. Exp. Ophthalmol. Jun 2005;243(6):513-518."
        "47.	Barkana Y, Anis S, Liebmann J, Tello C, Ritch R. Clinical utility of intraocular pressure monitoring outside of normal office hours in patients with glaucoma. Arch Ophthalmol. Jun 2006;124(6):793-797."
        "48.	Wax MB, Camras CB, Fiscella RG, Girkin C, Singh K, Weinreb RN. Emerging perspectives in glaucoma: optimizing 24-hour control of intraocular pressure. Am. J. Ophthalmol. Jun 2002;133 Suppl:S1-10."
        "49.	Bergea B, Bodin L, Svedbergh B. Impact of intraocular pressure regulation on visual fields in open-angle glaucoma. Ophthalmology. 1999;106(5):997-1004; discussion 1004-1005."
        "50.	Asrani S, Zeimer R, Wilensky J, Gieser D, Vitale S, Lindenmuth K. Large diurnal fluctuations in intraocular pressure are an independent risk factor in patients with glaucoma. J Glaucoma. Apr 2000;9(2):134-142."
        "51.	Leske MC, Heijl A, Hussein M, Bengtsson B, Hyman L, Komaroff E. Factors for glaucoma progression and the effect of treatment: the early manifest glaucoma trial. Arch Ophthalmol. 2003;121(1):48-56."
        "52.	AGIS:7. The advanced glaucoma intervention study (AGIS): 7. The relationship between control of intraocular pressure and visual field deterioration. The AGIS Investigators. Am. J. Ophthalmol. 2000;130(4):429-440."
        "53.	CNTGS. The effectiveness of intraocular pressure reduction in the treatment of normal-tension glaucoma. Collaborative Normal-Tension Glaucoma Study Group. Am. J. Ophthalmol. 1998;126(4):498-505."
        "54.	CNTGS. Comparison of glaucomatous progression between untreated patients with normal-tension glaucoma and patients with therapeutically reduced intraocular pressures. Collaborative Normal-Tension Glaucoma Study Group. Am. J. Ophthalmol. 1998;126(4):487-497."
        "55.	Realini T, Weinreb RN, Wisniewski SR. Diurnal intraocular pressure patterns are not repeatable in the short term in healthy individuals. Ophthalmology. Sep 2010;117(9):1700-1704."
        "56.	Bengtsson B, Leske MC, Hyman L, Heijl A. Fluctuation of intraocular pressure and glaucoma progression in the early manifest glaucoma trial. Ophthalmology. Feb 2007;114(2):205-209."
        "57.	Medeiros FA, Weinreb RN, Zangwill LM, et al. Long-term intraocular pressure fluctuations and risk of conversion from ocular hypertension to glaucoma. Ophthalmology. Jun 2008;115(6):934-940."
        "58.	Liu JH, Zhang X, Kripke DF, Weinreb RN. Twenty-four-hour intraocular pressure pattern associated with early glaucomatous changes. Invest Ophthalmol Vis Sci. Apr 2003;44(4):1586-1590."
        "59.	Caprioli J, Coleman AL. Intraocular pressure fluctuation a risk factor for visual field progression at low intraocular pressures in the advanced glaucoma intervention study. Ophthalmology. Jul 2008;115(7):1123-1129 e1123."
    ]
    
    for ref in referencias:
        st.markdown(f"- {ref}")
