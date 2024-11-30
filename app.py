import streamlit as st

# Título de la aplicación
st.title("Editor LaTeX en Streamlit usando latex.js")

# Campo de texto para el código LaTeX
st.subheader("Escribe tu código LaTeX aquí:")
latex_code = st.text_area(
    label="Código LaTeX",
    value=r"""
\documentclass{article}
\begin{document}
Hola, este es un ejemplo de documento en LaTeX renderizado con latex.js.
\end{document}
""",
    height=300,
)

# HTML para latex.js y el contenedor de la vista previa
latex_js_html = f"""
<script src="https://cdn.jsdelivr.net/npm/latex.js@0.12.0/dist/latex.min.js"></script>
<div id="output"></div>
<script>
    function renderLatex() {{
        const latexCode = `{latex_code}`;
        const htmlOutput = latexjs.parse(latexCode).htmlDocument();
        document.getElementById("output").innerHTML = htmlOutput.body.innerHTML;
    }}
    renderLatex();
</script>
"""

# Mostrar el resultado renderizado
st.subheader("Vista previa renderizada:")
st.components.v1.html(latex_js_html, height=500)
