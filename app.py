import streamlit as st

st.title("Editor LaTeX en Streamlit usando latex.js")

# Área de texto para que el usuario escriba el código LaTeX
st.subheader("Escribe tu código LaTeX:")
latex_code = st.text_area(
    "Código LaTeX",
    value=r"""
\documentclass{article}
\begin{document}
Hola, este es un ejemplo de documento en LaTeX renderizado con latex.js.
\end{document}
""",
    height=300,
)

# HTML para renderizar el código con latex.js
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/latex.js@0.12.0/dist/latex.min.js"></script>
</head>
<body>
    <div id="output"></div>
    <script>
        const latexCode = `{latex_code}`;
        const htmlOutput = latexjs.parse(latexCode).htmlDocument();
        document.getElementById("output").innerHTML = htmlOutput.body.innerHTML;
    </script>
</body>
</html>
"""

# Mostrar la vista previa renderizada como un iframe
st.subheader("Vista previa renderizada:")
st.components.v1.html(html_template, height=500, scrolling=True)
