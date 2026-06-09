import streamlit as st

st.set_page_config(
    page_title="Asistente del Dashboard Financiero",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Asistente del Dashboard Financiero")
st.write("Este asistente ayuda a interpretar la información publicada en el dashboard financiero.")

st.info(
    "Esta es una versión de prueba sin IA generativa. "
    "Funciona con respuestas guiadas y no genera costo por consulta."
)

respuestas = {
    "presupuesto": "El presupuesto asignado corresponde al monto autorizado para una escuela, región, programa o fondo durante el periodo fiscal seleccionado.",
    "asignado": "El presupuesto asignado es el monto autorizado para ejecutar durante el periodo fiscal.",
    "ejecución": "La ejecución presupuestaria indica qué porcentaje del presupuesto asignado ya fue utilizado, comprometido o ejecutado.",
    "ejecutado": "El presupuesto ejecutado representa los recursos que ya fueron utilizados o comprometidos según la información disponible.",
    "ingresos": "Los ingresos representan los recursos registrados para una escuela, región o programa dentro del dashboard.",
    "escuela": "Para identificar la escuela con mayores ingresos, revisa la tabla o visual denominado 'Top escuelas por ingresos' dentro del dashboard.",
    "región": "Para analizar la información por región, utiliza el filtro de Región ubicado en la parte superior del dashboard.",
    "fondos": "Los fondos permiten diferenciar el origen de los recursos, por ejemplo fondos estatales, federales o especiales.",
    "federal": "Los fondos federales corresponden a recursos provenientes de asignaciones federales.",
    "estatal": "Los fondos estatales corresponden a recursos asignados desde el presupuesto estatal.",
    "filtro": "Los filtros permiten ajustar la información visible por año fiscal, trimestre, región, tipo de fondo u otra categoría disponible."
}

preguntas_sugeridas = [
    "¿Qué significa presupuesto asignado?",
    "¿Cómo interpreto la ejecución presupuestaria?",
    "¿Qué son los ingresos?",
    "¿Cómo filtro por región?",
    "¿Qué escuela tiene mayores ingresos?"
]

if "historial" not in st.session_state:
    st.session_state.historial = [
        {
            "rol": "assistant",
            "contenido": "¡Hola! Soy el asistente del dashboard financiero. Puedes hacerme preguntas sobre presupuesto, ejecución, ingresos, escuelas, regiones o fondos."
        }
    ]

st.markdown("### Preguntas sugeridas")

cols = st.columns(2)
for i, pregunta_sugerida in enumerate(preguntas_sugeridas):
    with cols[i % 2]:
        if st.button(pregunta_sugerida):
            st.session_state.pregunta_actual = pregunta_sugerida

for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["rol"]):
        st.write(mensaje["contenido"])

pregunta = st.chat_input("Escribe tu pregunta aquí...")

if "pregunta_actual" in st.session_state:
    pregunta = st.session_state.pregunta_actual
    del st.session_state.pregunta_actual

if pregunta:
    st.session_state.historial.append({"rol": "user", "contenido": pregunta})

    respuesta = (
        "Por ahora no tengo esa respuesta configurada. "
        "Puedes consultar las páginas de presupuesto, ingresos, ejecución, escuelas o regiones en el dashboard."
    )

    for clave, texto in respuestas.items():
        if clave.lower() in pregunta.lower():
            respuesta = texto
            break

    st.session_state.historial.append({"rol": "assistant", "contenido": respuesta})
    st.rerun()