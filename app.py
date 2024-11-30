import streamlit as st

st.title("Depuración de Renderizado LaTeX con latex.js")

# HTML para verificar si latex.js funciona
html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/latex.js@0.12.0/dist/latex.min.js"></script>
</head>
<body>
    <h1>Verificación de latex.js</h1>
    <p>Si latex.js funciona, deberías ver un ejemplo de LaTeX renderizado a continuación:</p>
    <div id="output"></div>
    <script>
        try {
            // Ejemplo fijo de LaTeX para probar
            const exampleLatex = `
            \\documentclass{article}
            \\begin{document}
            Este es un documento de prueba en \\LaTeX.
            \\end{document}
            `;
            const htmlOutput = latexjs.parse(exampleLatex).htmlDocument();
            document.getElementById("output").innerHTML = htmlOutput.body.innerHTML;
        } catch (e) {
            document.getElementById("output").innerHTML = "<p>Error al cargar latex.js: " + e.message + "</p>";
        }
    </script>
</body>
</html>
"""

# Mostrar el HTML en Streamlit
st.components.v1.html(html_template, height=500, scrolling=True)

