import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))

st.title('USA HOUSING PREDICTION')
st.sidebar.header('Housing Data')
image = Image.open('houses.png')
st.image(image, '')

def user_dataset():
    Income=st.sidebar.number_input('Income')
    House_Age=st.sidebar.number_input('House Age',2,30)
    Number_of_rooms=st.sidebar.number_input('Number of Rooms',2,15)
    Number_of_Bedrooms=st.sidebar.slider('Number of Bedrooms',1,10)
    Area_Population=st.sidebar.number_input('Area Population')
    
    
    
    user_data_report={
        'Avg. Area Income':Income, 
        'Avg. Area House Age':House_Age,
        'Avg. Area Number of Rooms':Number_of_rooms,
       'Avg. Area Number of Bedrooms':Number_of_Bedrooms, 
       'Area Population':Area_Population
    }
    
    data=pd.DataFrame(user_data_report,index=[0])
    return data

user_data = user_dataset()
st.header('Housing Data')
st.write(user_data)

Price = model.predict(user_data)
st.subheader('Price of House')
st.subheader('$'+str(np.round(Price[0], 2)))