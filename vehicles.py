import streamlit as st 
import pandas as pd
import plotly.express as px

st.header('Anuncio de coches en venta')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botón
        
        if hist_button:
            
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)