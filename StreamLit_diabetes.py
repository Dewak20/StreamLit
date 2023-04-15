import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))

#Judul WEB
st.title('Data Mining Prediksi Diabetes')
st.subheader(':blue[_by Krishnadana_]:sunglasses:')


#Form input data (Harus sama dengInsulinan nama coloumn pada data)

# Membuat Input menjadi 2 Colomn
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Masukkan nilai Pregnansi')

with col1:
    Glucose = st.text_input('Masukkan nilai Glukosa')

with col1:
    BloodPressure = st.text_input('Masukkan nilai Tekanan darah')

with col1:
    SkinThickness = st.text_input('Masukkan nilai Ketebalan kulit')

with col2:
    Insulin = st.text_input('Masukkan nilai Ketebalan Insulin')

with col2:
    BMI = st.text_input('Masukkan nilai BMI')

with col2:
    DiabetesPedigreeFunction = st.text_input('Masukkan nilai Indikator riwayat diabetes ')

with col2:
    Age =  st.text_input('Masukkan Umur')


# Code untuk prediksi

diabetes_diagnosis = ''

# Membuat button prediksi

if st.button('Test Prediksi Diabetes'):
    diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                                               Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if(diabetes_prediction[0]==1):
        diabetes_diagnosis = "Pasien terkena Diabetes"
    else:
        diabetes_diagnosis = "Pasien tidak terkena Diabetes"
    st.success(diabetes_diagnosis)
    
    
    