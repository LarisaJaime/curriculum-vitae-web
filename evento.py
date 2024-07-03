import streamlit as st
from datetime import datetime, timedelta
import time

def main():
    st.title('¡Invitación al Casamiento de Belén y Maximiliano!')
    st.image('./image/484f7219c122ff3d5b7ffd6e3095d299.jpg', use_column_width=True)  # Puedes ajustar la ruta de la imagen

    # Definir la fecha del casamiento
    fecha_casamiento = datetime(2024, 10, 26, 19, 0, 0)  # Fecha y hora del casamiento

    # Mostrar la invitación y el contador de cuenta regresiva
    st.write("""
             Nos casamos, estamos muy contentos y emocionados de que compartas con nosotros este gran momento.
             """)
    with st.empty():
        while True:
            ahora = datetime.now()
            if ahora > fecha_casamiento:
                st.write("""
                    Estimados amigos y familiares,

                    ¡Hoy es el gran día! Estamos emocionados de compartir con ustedes uno de los momentos más especiales de nuestras vidas: el casamiento de Belén y Maximiliano.

                    Gracias por ser parte de este día inolvidable.

                    Con cariño,
                    Belén y Maximiliano
                """)
                break

            tiempo_restante = fecha_casamiento - ahora
            days = tiempo_restante.days
            hours, remainder = divmod(tiempo_restante.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            st.write("""
                **Faltan:** {} días, {} horas, {} minutos y {} segundos para el casamiento.
            """.format(days, hours, minutes, seconds))

            time.sleep(1)

if __name__ == '__main__':
    main()
