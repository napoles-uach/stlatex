import streamlit as st

st.title("Editor LaTeX en Streamlit usando MathJax")

# Área de texto para escribir el código LaTeX
st.subheader("Escribe tu código LaTeX aquí:")
latex_code = st.text_area(
    "Código LaTeX",
    value=r"""
\documentclass{article}
\begin{document}
Hola, este es un ejemplo de documento en \LaTeX renderizado con MathJax.
\end{document}
""",
    height=300,
)

# HTML con MathJax para renderizar el contenido LaTeX
mathjax_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" async
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js">
    </script>
</head>
<body>
    <h1>Vista previa renderizada</h1>
    <p>A continuación se muestra el contenido renderizado desde LaTeX:</p>
    <div id="output">
        \\[
        {latex_code}
        \\]
    </div>
</body>
</html>
"""

# Mostrar el HTML con MathJax en Streamlit
st.components.v1.html(mathjax_html, height=500, scrolling=True)
