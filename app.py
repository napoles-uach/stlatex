import streamlit as st

st.title("Editor LaTeX en Streamlit usando MathJax")

# Instrucciones para el usuario
st.write(
    "Este editor utiliza MathJax para renderizar LaTeX. Por favor, ingresa fragmentos de código LaTeX sin usar entornos de documento completos."
)

# Área de texto para que el usuario escriba LaTeX
latex_code = st.text_area(
    "Código LaTeX",
    value=r"""
\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
""",
    height=200,
)

# HTML con MathJax para renderizar
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
    <div>
        \\[
        {latex_code}
        \\]
    </div>
</body>
</html>
"""

# Mostrar el contenido renderizado en la app de Streamlit
st.components.v1.html(mathjax_html, height=300, scrolling=True)
