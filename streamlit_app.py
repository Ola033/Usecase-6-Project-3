import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 


st.write('Hello World') 

st.markdown(
    """
    <style>
    .reportview-container {
        background: #ffebee;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Welcome to My Streamlit App")

st.write("This is a simple app created using Streamlit. You can interact with it and see some cool features!")
  


data = pd.DataFrame({
    'Cars': ['Car A', 'Car B', 'Car C'],
    'Values': [10, 20, 15],
     'Info': ['Fast and sleek', 'Family friendly', 'Compact and efficient']

})




fig = px.bar(data, x='Cars', y='Values', 
              hover_name='Cars',
              hover_data={'Values': True, 'Info': True}, 
              title='Car Comparison',
              color='Cars')


st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

st.subheader("Choose Your Favorite Car")

car_options = ['Car A', 'Car B', 'Car C']
selected_car = st.selectbox("Select a car:", car_options)

st.write(f"You selected: {selected_car}")


