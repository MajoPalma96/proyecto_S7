#importar las librerias
import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv("vehicles_us.csv") # leer los datos

st.title("Datos de anuncios de venta de autos")
st.header("Histograma de precios")
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma de precios para el conjunto de datos de anuncios de venta de autos')
            
            # crear un histograma
            fig = px.histogram(car_data, x="price")
            fig.update_layout({"yaxis_title": "Frecuencia"})

            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

st.header("Gráfico de dispersión entre precio y cuentakilómetros")
#sct_button = st.button('Construir gráfico de dispersión') # crear un botón
#Con checkbox:
sct_check= st.checkbox('Construir gráfico de dispersión')
if sct_check: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un gráfico de dispersión entre entre precio y cuentakilómetros de los anuncios de venta de autos')
            
            # crear un histograma
            fig2 = px.scatter(car_data, x="odometer", y="price", color="type",opacity=0.7)
            
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig2, use_container_width=True)