import streamlit as st

# Título de la aplicación
st.title('Currículum Profesional')

st.image('./image/484f7219c122ff3d5b7ffd6e3095d299.jpg', use_column_width=True)  # Puedes ajustar la ruta de la imagen

# Información Personal
st.header('Información Personal')
# Estilo CSS para simular un cuadro de entrada
estilo_cuadro = """
    <style>
        .cuadro {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f0f0f0;
        }
    </style>
"""
# Mostrar el nombre como texto encuadrado
st.markdown(estilo_cuadro, unsafe_allow_html=True)

st.write("Nombre completo")
st.markdown('<div class="cuadro"> Larisa Natalia Jaime</div>', unsafe_allow_html=True)
st.write("Profesión")
profesion = ('Desarrollador de Software')
st.markdown(f'<div class="cuadro"> {profesion}</div>', unsafe_allow_html=True)
email = st.text_input('Correo electrónico', 'juan.perez@example.com')
telefono = st.text_input('Teléfono', '+123456789')
ubicacion = st.text_input('Ubicación', 'Ciudad, País')

# Experiencia Laboral
st.header('Experiencia Laboral')

# Experiencia 1
with st.expander("Desarrollador Web Senior @ Empresa A (2018 - Presente)"):
    st.write("""
    - Descripción breve de las responsabilidades y logros en este puesto.
    - Puedes agregar más detalles y puntos clave aquí.
    """)

# Experiencia 2
with st.expander("Analista de Datos @ Empresa B (2015 - 2018)"):
    st.write("""
    - Descripción breve de las responsabilidades y logros en este puesto.
    """)

# Educación
st.header('Educación')

# Educación 1
with st.expander("Licenciatura en Ingeniería Informática @ Universidad XYZ (2011 - 2015)"):
    st.write("""
    - Descripción breve de tu área de estudio y logros académicos.
    """)

# Educación 2
with st.expander("Curso en Desarrollo Web Full Stack @ Escuela ABC (2016)"):
    st.write("""
    - Descripción breve del curso y habilidades adquiridas.
    """)

# Habilidades
st.header('Habilidades')
st.write("""
- Python, JavaScript, SQL
- Desarrollo web (HTML, CSS, Flask, Django)
- Análisis de datos (Pandas, Matplotlib)
- Gestión de bases de datos (MySQL, PostgreSQL)
""")

# Proyectos
st.header('Proyectos Destacados')
st.write("""
- Puedes listar aquí algunos proyectos destacados con enlaces o descripciones breves.
- Este es un buen lugar para mostrar tu experiencia práctica y aplicar las habilidades mencionadas.
""")

# Contacto
st.header('Contacto')
st.write(f'Correo electrónico: {email}')
st.write(f'Teléfono: {telefono}')
st.write(f'Ubicación: {ubicacion}')
