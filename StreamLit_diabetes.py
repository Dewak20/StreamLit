import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('Diabetes_model.sav'))

#Judul WEB
st.title('Data Mining Prediksi Diabetes')