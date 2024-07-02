import streamlit as st

# Título de la aplicación
st.title('Currículum Profesional')

# Información Personal
st.header('Información Personal')
nombre = st.text_input('Nombre completo', 'Juan Pérez')
profesion = st.text_input('Profesión', 'Desarrollador de Software')
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
