import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Modeli yükleme
model_path = 'eniyi.joblib'
model = joblib.load(model_path)

# Başlık ve açıklama
st.title("Otel Fiyat Tahmin Uygulaması")
st.write("Bu uygulama, otel özelliklerine dayalı olarak fiyat tahmini yapar. En iyi model kullanılarak geliştirilmiştir.")

# Kullanıcı giriş alanları
st.sidebar.header("Otel Özelliklerini Giriniz")
otel_yildizi = st.sidebar.selectbox("Otel Yıldızı", options=[1, 2, 3, 4, 5])
sehir = st.sidebar.selectbox("Şehir", options=['Istanbul', 'Antalya', 'Ankara', 'Izmir', 'Bodrum'])
oda_sayisi = st.sidebar.slider("Oda Sayısı", min_value=1, max_value=100, value=10)
denize_yakinlik = st.sidebar.slider("Denize Yakınlık (km)", min_value=0.1, max_value=5.0, value=1.0)
mevsim = st.sidebar.selectbox("Mevsim", options=['Yaz', 'Kış', 'Bahar', 'Sonbahar'])
ortalama_puan = st.sidebar.slider("Ortalama Puan", min_value=1.0, max_value=10.0, value=5.0)

# Kullanıcı girişlerini veri çerçevesine dönüştürme
data = pd.DataFrame({
    'otel_yildizi': [otel_yildizi],
    'sehir': [sehir],
    'oda_sayisi': [oda_sayisi],
    'denize_yakinlik': [denize_yakinlik],
    'mevsim': [mevsim],
    'ortalama_puan': [ortalama_puan]
})

# Tahmin butonu
if st.button("Tahmini Görüntüle"):
    # Tahmin işlemi
    prediction = model.predict(data)[0]
    st.subheader(f"Tahmini Otel Fiyatı: {prediction:.2f} TL")

