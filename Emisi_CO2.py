import pickle
import streamlit as st

# Function to set the Blue Light theme
def set_blue_light_theme():
    """
    Sets the Streamlit theme to Blue Light.
    """
    # Set primary color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e15462ye0 {
            background-color: #f5f7ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set secondary color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e5i1odf0 {
            background-color: #c0cbe1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set text color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e1hbx90p0 {
            color: #2c3e50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Load the pre-trained model using pickle
model = pickle.load(open('Emisi.sav', 'rb'))

# Set Blue Light theme
set_blue_light_theme()

# Title of the application
st.title('Emisi_CO2 Prediction')

# Description of the machine learning model
deskripsi_model = """
### Deskripsi Model Machine Learning

Alasan project ini dilakukan tidak jauh dikarenakan polusi udara yang semakin meningkat di beberapa kota di indonesia.
Hal tersebut dapat diliat dari beberapa sumber data dan artikel salah satunya adalah article berikut https://www.metrojambi.com/lifestyle/13802320/ini-10-kota-di-indonesia-dengan-polusi-udara-tinggi-bagaimana-dengan-surabaya
yang dimana memberikan informasi bahwa polusi udara semakin meningkat di beberapa kota besar di indoensia. Oleh karena itu, project ini dilakukan.
Agar memberikan manfaat untuk masyarakat untuk mengetahui kendaraan yang mereka gunakan memiliki emisi yang tinggi atau rendah sehingga dapat meminimalisir terjadinya emisi.
Dengan batas aman 150, meskipun sebenarnya batas aman Emisi CO2 di indonesia 120 g/km dan di luar negeri 100 g/km. Hal ini dipertimbangkan karena masih banyak kendaaraan  di indonesia berada di luar batas aman  atau berstatus berbahaya.
Model ini menggunakan Linear Regression dengan akurasi 90%.
"""
# Display the description of the machine learning model
st.markdown(deskripsi_model)

# Feature inputs for prediction
feature1 = st.number_input("Masukkan Ukuran Mesin (L) (0.0 - 10)", value=0.0)
feature2 = st.number_input("Masukkan Jumlah Silinder (2-16)", value=0)
feature3 = st.number_input("Masukkan Konsumsi Bahan Bakar di Kota (L/100 km) (1-35)", value=0.0)
feature4 = st.number_input("Masukkan Konsumsi Bahan Bakar di Jalan Raya (L/100 km) (1-35)", value=0.0)
feature5 = st.number_input("Masukkan Konsumsi Bahan Bakar Gabungan (L/100 km) 1-35", value=0.0)
feature6 = st.number_input("Masukkan Konsumsi Bahan Bakar Gabungan (mpg) (11-70)", value=0)

if st.button('Predict'):
    # Perform prediction using the loaded model
    hasil_prediksi = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6]])
    st.write('Predicted Emisi_CO2(g/km):', hasil_prediksi[0])

# Function to classify "Safe" or "Dangerous"
def klasifikasi_emisi(hasil_prediksi):
    if hasil_prediksi is not None and hasil_prediksi > 150:
        return "Berbahaya"
    else:
        return "Aman"

# Use the function to determine emission status if hasil_prediksi is defined
if 'hasil_prediksi' in locals():
    status_emisi = klasifikasi_emisi(hasil_prediksi)
    st.write("Status Emisi:", status_emisi)
