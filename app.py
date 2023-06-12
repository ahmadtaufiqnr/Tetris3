import streamlit as st
import datetime
from lorem_text import lorem
import pandas as pd
import numpy as np
import datetime as dt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title='Analisis Data Saham ASII (Astra International Tbk)',
    layout='wide'
)
df=pd.read_csv("ASII.csv")
df = df.rename(columns={'timestamp': 'date'})
df1=df.set_index('date')
df2=pd.read_csv("datanormalized.csv")
# df2

# CURR_YEAR=max(df2['Year'])

data=pd.pivot_table(
    data=df2,
    index='Year',
    aggfunc={
        'open':'sum',
        'low':'sum',
        'high':'sum',
        'close':'sum'
    }
).reset_index()
# st.dataframe(data)

# df_normal=pd.read_csv("D:\TETRIS 3\PYTHON\Session # 5 - Bulding Interactive Dashboard with Python (1) - Python Streamlit\Belajar_Streamlit\datanormalized.csv")

# st.write("Hello world!")
# "Hello"

st.title("Analisis Data Saham ASII (Astra International Tbk)")
st.header("Apa itu Saham???")

"Saham adalah instrumen keuangan yang mewakili kepemilikan sebagian dari suatu perusahaan. Ketika seseorang membeli saham maka secara efektif orang tersebut membeli bagian kecil dari perusahaan."
"Investasi saham dapat dilakukan oleh individu atau institusi dengan harapan mendapatkan keuntungan dari kenaikan harga saham atau dividen yang dibayarkan oleh perusahaan."

st.header(
    "Faktor yang Mempengaruhi Harga Saham"
)

"1. Kinerja Keuangan Perusahaan: Kinerja keuangan perusahaan, termasuk pendapatan, laba bersih, pertumbuhan penjualan, dan marjin keuntungan, dapat mempengaruhi harga saham. Jika kinerja keuangan perusahaan lebih baik dari harapan, harga saham cenderung naik, sementara kinerja yang buruk dapat menyebabkan penurunan harga saham."
"2. Prospek Pertumbuhan: Prospek pertumbuhan perusahaan dan industri secara keseluruhan dapat mempengaruhi harga saham. Jika sebuah perusahaan memiliki prospek pertumbuhan yang positif, seperti meluncurkan produk baru atau memperluas pasar, hal itu dapat menyebabkan kenaikan harga saham. Sebaliknya, jika prospek pertumbuhan terlihat suram, harga saham bisa turun."
"3. Kondisi Ekonomi Makro: Kondisi ekonomi makro, seperti tingkat suku bunga, inflasi, pertumbuhan ekonomi, dan kebijakan moneter, dapat berdampak signifikan pada harga saham secara keseluruhan. Misalnya, kondisi ekonomi yang kuat dan suku bunga rendah cenderung mendukung kenaikan harga saham, sedangkan resesi atau kebijakan moneter yang ketat dapat menyebabkan penurunan harga saham."
"4. Sentimen Pasar: Sentimen investor dan persepsi pasar terhadap saham atau pasar secara keseluruhan juga dapat mempengaruhi harga saham. Sentimen positif, seperti optimisme dan keyakinan investor, dapat mendorong kenaikan harga saham, sementara sentimen negatif, seperti kekhawatiran atau kepanikan, dapat menyebabkan penurunan harga saham."
"5. Berita dan Peristiwa: Berita dan peristiwa penting yang terkait dengan perusahaan atau industri, seperti laporan keuangan, peluncuran produk, perubahan manajemen, merger atau akuisisi, perubahan regulasi, atau peristiwa global penting, dapat mempengaruhi harga saham. Berita positif atau peristiwa yang dianggap menguntungkan bisa meningkatkan harga saham, sementara berita negatif atau peristiwa yang tidak diharapkan bisa menekan harga saham."

"Maka dari itu, untuk mengetahui kondisi saham dari suatu perusahaan diperlukan adanya analisis dari harga saham tiap waktunya agar investor dapat memilih waktu yang tepat untuk melakukan investasi saham ke perusahaan tersebut."
"Berikut contoh analisis saham ASII (Astra International Tbk),"
st.caption(
    "data diperoleh dari https://www.kaggle.com/datasets/muamkh/ihsgstockdata "
    )
# df
"Data harian harga saham ASII dimulai tanggal 16 April 2001 sampai 06 Januari 2023."

# st.dataframe(df1)
# st.dataframe(df2)
CURR_YEAR=st.select_slider(
    "Pilih tahun",
    [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001]
)
PREV_YEAR=CURR_YEAR-1

mx_open, mx_low, mx_high, mx_close = st.columns(4)
with mx_open:
    curr_open = data.loc[data['Year']==CURR_YEAR, 'open'].values[0]
    prev_open = data.loc[data['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct=100.0*(curr_open-prev_open)/prev_open
    st.metric('open', value=curr_open, delta=f'{open_diff_pct:.2f}%')
with mx_low:
    curr_low = data.loc[data['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data.loc[data['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data.loc[data['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data.loc[data['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data.loc[data['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data.loc[data['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')

st.header("Close trend")
# PilihTahun=st.radio(
#     "Pilih tahun",
#     [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001]
# )
close_line = alt.Chart(df2[df2['Year']==CURR_YEAR],
                       title=alt.Title(f"Close Trend Saham ASII "+str(CURR_YEAR))
                       ).mark_line().encode(
    alt.X('Day', title='Date'),
    alt.Y('Normalized Close', title='Normalized Close', aggregate='sum')
)
st.altair_chart(close_line,use_container_width=True)

#TAMBAHIN OPEN, LOW, HIGH NORMALIZED

#gambar tiap tahun
# st.image('std close.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

"Dapat dilihat tren saham ASII untuk tiap tahun berbeda-beda sehingga harus dikaji lebih lanjut untuk meyakinkan investor dalam membeli saham."

"Untuk meyakinkan investor dalam membeli saham, berikut adalah prediksi yang diperoleh dengan menggunakan Gaussian Process dari data saham ASII untuk tahun 2022."


dfp=pd.read_csv("datapred.csv")
YY=dfp['Normalized Close']
XX=dfp['Day']
df_gpr_mean=dfp['gpr_mean']
df_gpr_std=dfp['gpr_std']

X22=XX[0:259]
Y22=YY[0:259]
Ypredict22=df_gpr_mean[0:259]
gpr22=df_gpr_std[0:259]

data = {
    'X22': X22,
    'Y22': Y22,
    'Ypredict22': Ypredict22,
    'gpr22': gpr22
}
dfp1 = pd.DataFrame(data)

#Selang Kepercayaan 95%
df_conf = pd.DataFrame()
df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
df_conf.index = X22


fig = px.line(dfp1, x="X22", y=["Y22","Ypredict22"])
fig.update_layout(showlegend=False)
fig.add_trace(go.Scatter(
    x=df_conf.index,
    y=df_conf['Upper'],
    mode='lines',
    showlegend=False,
    line=dict(color='rgba(0,0,0,0)')
))
fig.add_trace(go.Scatter(
    x=df_conf.index,
    y=df_conf['Lower'],
    mode='lines',
    name='95% confidence',
    fill='tonexty',
    line=dict(color='#95FFFF')
))
fig.update_layout(
    xaxis_title="Days",
    yaxis_title="Normalized Close",
    showlegend=False
)
# Menambahkan fill between
fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["Y22"], mode='lines', name='Observation', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["Ypredict22"], mode='lines', name='Prediction', line=dict(color='orange')))
fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                  hovermode='x unified')
st.plotly_chart(fig,use_container_width=True)

# st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.caption(
    "dengan MSE yang diperoleh sebesar 0.0710244182897843"
)

"Dari hasil prediksi, dapat diketahui bahwa tren dari harga saham aktual dengan prediksi tidak berbeda cukup jauh."
"Saat tren saham pada data aktual naik, tren prediksi juga naik. Begitupula saat tren data aktual turun, tren predikti turun."
"Meskipun masih ada kenaikan atau penurunan yang berbeda dari data aktual dengan data prediksi, hasil prediksi masih dapat digunakan sebagai acuan investor dalam membeli saham."