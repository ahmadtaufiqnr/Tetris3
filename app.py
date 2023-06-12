import streamlit as st
import datetime
from lorem_text import lorem
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

st.set_page_config(
    page_title='Analisis Data Saham ASII (Astra Internasional)',
    layout='wide'
)
df=pd.read_csv("C:/Users/atauf/Downloads/ASII.csv")

df_normal=pd.read_csv("D:\TETRIS 3\PYTHON\Session # 5 - Bulding Interactive Dashboard with Python (1) - Python Streamlit\Belajar_Streamlit\datanormalized.csv")


# st.write("Hello world!")
# "Hello"
st.title("Analisis Data Saham ASII (Astra Internasional)")
st.header("Apa itu Saham???")

"Saham adalah instrumen keuangan yang mewakili kepemilikan sebagian dari suatu perusahaan. Ketika Anda membeli saham, Anda secara efektif membeli bagian kecil dari perusahaan tersebut."
"Investasi saham dapat dilakukan oleh individu atau institusi dengan harapan mendapatkan keuntungan dari kenaikan harga saham atau dividen yang dibayarkan oleh perusahaan."
"Faktor yang mempengaruhi saham:"
"1. Kinerja Keuangan Perusahaan: Kinerja keuangan perusahaan, termasuk pendapatan, laba bersih, pertumbuhan penjualan, dan marjin keuntungan, dapat mempengaruhi harga saham. Jika kinerja keuangan perusahaan lebih baik dari harapan, harga saham cenderung naik, sementara kinerja yang buruk dapat menyebabkan penurunan harga saham."
"2. Prospek Pertumbuhan: Prospek pertumbuhan perusahaan dan industri secara keseluruhan dapat mempengaruhi harga saham. Jika sebuah perusahaan memiliki prospek pertumbuhan yang positif, seperti meluncurkan produk baru atau memperluas pasar, hal itu dapat menyebabkan kenaikan harga saham. Sebaliknya, jika prospek pertumbuhan terlihat suram, harga saham bisa turun."
"3. Kondisi Ekonomi Makro: Kondisi ekonomi makro, seperti tingkat suku bunga, inflasi, pertumbuhan ekonomi, dan kebijakan moneter, dapat berdampak signifikan pada harga saham secara keseluruhan. Misalnya, kondisi ekonomi yang kuat dan suku bunga rendah cenderung mendukung kenaikan harga saham, sedangkan resesi atau kebijakan moneter yang ketat dapat menyebabkan penurunan harga saham."
"4. Sentimen Pasar: Sentimen investor dan persepsi pasar terhadap saham atau pasar secara keseluruhan juga dapat mempengaruhi harga saham. Sentimen positif, seperti optimisme dan keyakinan investor, dapat mendorong kenaikan harga saham, sementara sentimen negatif, seperti kekhawatiran atau kepanikan, dapat menyebabkan penurunan harga saham."
"5. Berita dan Peristiwa: Berita dan peristiwa penting yang terkait dengan perusahaan atau industri, seperti laporan keuangan, peluncuran produk, perubahan manajemen, merger atau akuisisi, perubahan regulasi, atau peristiwa global penting, dapat mempengaruhi harga saham. Berita positif atau peristiwa yang dianggap menguntungkan bisa meningkatkan harga saham, sementara berita negatif atau peristiwa yang tidak diharapkan bisa menekan harga saham."

"Maka dari itu, untuk mengetahui kondisi saham dari suatu perusahaan diperlukan adanya analisis dari harga saham tiap waktunya agar investor dapat memilih waktu yang tepat untuk melakukan investasi saham ke perusahaan tersebut."
"Berikut contoh analisis saham ASII (Astra Internasional),"
st.caption(
    "data diperoleh dari https://www.kaggle.com/datasets/muamkh/ihsgstockdata "
    )
# df
"Data ASII merupakan data harian dimulai tanggal 16 April 2001 sampai 06 Januari 2023."
# df_normal
st.image('std close.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

"Dapat dilihat tren saham ASII untuk tiap tahun berbeda-beda sehingga harus dikaji lebih lanjut untuk meyakinkan investor dalam membeli saham."

"Untuk meyakinkan investor dalam membeli saham, berikut adalah prediksi yang diperoleh dengan menggunakan Gaussian Process dari data saham ASII."
st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.caption(
    "dengan MSE yang diperoleh sebesar 0.0710244182897843"
)

"Dari hasil prediksi, dapat diketahui bahwa tren dari harga saham aktual dengan prediksi tidak berbeda cukup jauh."
"Saat tren saham pada data aktual naik, tren prediksi juga naik. Begitupula saat tren data aktual turun, tren predikti turun."
"Meskipun masih ada kenaikan atau penurunan yang berbeda dari data aktual dengan data prediksi, hasil prediksi masih dapat digunakan sebagai acuan investor dalam membeli saham."