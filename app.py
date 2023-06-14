import streamlit as st
import datetime
from lorem_text import lorem
import pandas as pd
import numpy as np
import datetime as dt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot

st.set_page_config(
    page_title='Analisis Persaingan Harga Saham ASII, UNTR, AUTO, AALI, dan ASGR',
    layout='wide'
)

#SIDEBAR
with st.sidebar:
    st.title('**Capstone Project**')
    st.subheader('Data Analytics Fast Track Program - TETRIS Batch III - The CEO Project')
    # your_name=st.text_input("enter name")
    # with st.expander('lorem ipsum'):
    #     st.write(lorem.paragraphs(1))
    st.markdown(
        """
        Keterangan :

        **1. Open (Harga pembukaan)**
        > adalah harga perdagangan pertama suatu saham pada awal sesi perdagangan.

        **2. Low (Harga terendah)**\n
        > adalah harga terendah yang dicapai oleh suatu saham selama periode waktu tertentu, seperti hari perdagangan, minggu, bulan, atau tahun.

        **3. High (Harga tertinggi)**\n
        > adalah harga tertinggi yang dicapai oleh suatu saham selama periode waktu tertentu.

        **4. Close (Harga penutupan)**\n
        > adalah harga perdagangan terakhir suatu saham pada akhir sesi perdagangan.

        **5. Volume (Volume perdagangan)**\n
        > adalah jumlah saham yang diperdagangkan selama periode waktu tertentu. Hal ini mencerminkan seberapa aktifnya suatu saham diperdagangkan.

        **Sumber Data**
        > https://www.kaggle.com/datasets/muamkh/ihsgstockdata
        
        """
    )

df=pd.read_csv("ASII.csv")
df = df.rename(columns={'timestamp': 'date'})
df1=df.set_index('date')
df2=pd.read_csv("datanormalized.csv")
df_norm_untr=pd.read_csv("datanormalized_UNTR.csv")
df_norm_auto=pd.read_csv("datanormalized_AUTO.csv")
df_norm_aali=pd.read_csv("datanormalized_AALI.csv")
df_norm_asgr=pd.read_csv("datanormalized_ASGR.csv")


st.title("Analisis Persaingan Harga Saham ASII, UNTR, AUTO, AALI, dan ASGR")
st.write("**Ahmad Taufiq Nur Rahman** | ataufiqnr799@gmail.com | www.linkedin.com/in/ahmadtaufiqnr ")
"---"

col1, col2=st.columns((2,3))
with col1:
    st.header("Apa itu Saham?",anchor="SAHAM")
    st.markdown(
    """
    Saham adalah instrumen keuangan yang mewakili kepemilikan sebagian dari suatu perusahaan. Ketika seseorang membeli saham maka secara efektif orang tersebut membeli bagian kecil dari perusahaan.
    Investasi saham dapat dilakukan oleh individu atau institusi dengan harapan mendapatkan keuntungan dari kenaikan harga saham atau dividen yang dibayarkan oleh perusahaan.
    
    ---
    """
    )
    st.subheader("Faktor yang Mempengaruhi Harga Saham")

with col2:
    st.image('gambar1.jpg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# st.subheader(
#     """
#         "Faktor yang Mempengaruhi Harga Saham"
#         **Helo** _there_, 'how are you'?
#     > Quickly
#     - This
#     - is
    
#     """
# )
"Maka dari itu, untuk mengetahui kondisi saham dari suatu perusahaan diperlukan adanya analisis dari harga saham tiap waktunya agar investor dapat memilih waktu yang tepat untuk melakukan investasi saham ke perusahaan tersebut."
"Berikut analisis harga saham ASII (Astra International Tbk.), UNTR (United Tractors Tbk.), AUTO (Astra Otoparts Tbk.), AALI (Astra Agro Lestari Tbk.), dan ASGR (Astra Graphia Tbk.)."
st.caption(
    "data diperoleh dari https://www.kaggle.com/datasets/muamkh/ihsgstockdata "
    )
# df
"Data harian harga saham dimulai tanggal 16 April 2001 sampai 06 Januari 2023."

# st.dataframe(df1)
# st.dataframe(df2)

data_ly=df2.groupby('Year').last().reset_index()
data1_ly=df_norm_untr.groupby('Year').last().reset_index()
data2_ly=df_norm_auto.groupby('Year').last().reset_index()
data3_ly=df_norm_aali.groupby('Year').last().reset_index()
data4_ly=df_norm_asgr.groupby('Year').last().reset_index()

# # Histogram Sum Close per Tahun
# df_hist_sum = pd.concat([data_ly.assign(dataset='ASII Close'), data1_ly.assign(dataset='UNTR Close'),
#                 data2_ly.assign(dataset='AUTO Close'), data3_ly.assign(dataset='AALI Close'),
#                 data4_ly.assign(dataset='ASGR Close')])

# fig = px.bar(df_hist_sum, x='Year', y='volume', color='dataset',
#             title="Sum Close Trend Saham per Tahun ",
#             labels={'year': 'Year', 'volume': 'Volume', 'dataset': 'Saham'})

# st.plotly_chart(fig, use_container_width=True)

st.subheader("Return Saham per Tahun")

CURR_YEAR=st.select_slider(
    "Pilih tahun",
    [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002]
)
PREV_YEAR=CURR_YEAR-1

ket, mx_open, mx_low, mx_high, mx_close = st.columns(5)
with ket:
    st.markdown("<h3 style='font-size: 30px; color: blue;'>ASII</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 20px; color: orange;'>Astra International Tbk.</h3>", unsafe_allow_html=True)
with mx_open:
    curr_open = data_ly.loc[data_ly['Year']==CURR_YEAR, 'open'].values[0]
    prev_open = data_ly.loc[data_ly['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct=100.0*(curr_open-prev_open)/prev_open
    st.metric('open', value=curr_open, delta=f'{open_diff_pct:.2f}%')
with mx_low:
    curr_low = data_ly.loc[data_ly['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data_ly.loc[data_ly['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data_ly.loc[data_ly['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data_ly.loc[data_ly['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data_ly.loc[data_ly['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data_ly.loc[data_ly['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')

ket, mx_open, mx_low, mx_high, mx_close = st.columns(5)
with ket:
    st.markdown("<h3 style='font-size: 30px; color: blue;'>UNTR</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 20px; color: orange;'>United Tractors Tbk.</h3>", unsafe_allow_html=True)
with mx_open:
    curr_open1 = data1_ly.loc[data1_ly['Year']==CURR_YEAR, 'open'].values[0]
    prev_open1 = data1_ly.loc[data1_ly['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct1=100.0*(curr_open1-prev_open1)/prev_open1
    st.metric('open', value=curr_open1, delta=f'{open_diff_pct1:.2f}%')
with mx_low:
    curr_low = data1_ly.loc[data1_ly['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data1_ly.loc[data1_ly['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data1_ly.loc[data1_ly['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data1_ly.loc[data1_ly['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data1_ly.loc[data1_ly['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data1_ly.loc[data1_ly['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')

ket, mx_open, mx_low, mx_high, mx_close = st.columns(5)
with ket:
    st.markdown("<h3 style='font-size: 30px; color: blue;'>AUTO</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 20px; color: orange;'>Astra Otoparts Tbk.</h3>", unsafe_allow_html=True)
with mx_open:
    curr_open = data2_ly.loc[data2_ly['Year']==CURR_YEAR, 'open'].values[0]
    prev_open = data2_ly.loc[data2_ly['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct=100.0*(curr_open-prev_open)/prev_open
    st.metric('open', value=curr_open, delta=f'{open_diff_pct:.2f}%')
with mx_low:
    curr_low = data2_ly.loc[data2_ly['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data2_ly.loc[data2_ly['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data2_ly.loc[data2_ly['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data2_ly.loc[data2_ly['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data2_ly.loc[data2_ly['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data2_ly.loc[data2_ly['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')

ket, mx_open, mx_low, mx_high, mx_close = st.columns(5)
with ket:
    st.markdown("<h3 style='font-size: 30px; color: blue;'>AALI</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 20px; color: orange;'>Astra Agro Lestari Tbk.</h3>", unsafe_allow_html=True)
with mx_open:
    curr_open = data3_ly.loc[data3_ly['Year']==CURR_YEAR, 'open'].values[0]
    prev_open = data3_ly.loc[data3_ly['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct=100.0*(curr_open-prev_open)/prev_open
    st.metric('open', value=curr_open, delta=f'{open_diff_pct:.2f}%')
with mx_low:
    curr_low = data3_ly.loc[data3_ly['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data3_ly.loc[data3_ly['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data3_ly.loc[data3_ly['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data3_ly.loc[data3_ly['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data3_ly.loc[data3_ly['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data3_ly.loc[data3_ly['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')

ket, mx_open, mx_low, mx_high, mx_close = st.columns(5)
with ket:
    st.markdown("<h3 style='font-size: 30px; color: blue;'>ASGR</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 20px; color: orange;'>Astra Graphia Tbk.</h3>", unsafe_allow_html=True)
with mx_open:
    curr_open = data4_ly.loc[data4_ly['Year']==CURR_YEAR, 'open'].values[0]
    prev_open = data4_ly.loc[data4_ly['Year']==PREV_YEAR, 'open'].values[0]
    open_diff_pct=100.0*(curr_open-prev_open)/prev_open
    st.metric('open', value=curr_open, delta=f'{open_diff_pct:.2f}%')
with mx_low:
    curr_low = data4_ly.loc[data4_ly['Year']==CURR_YEAR, 'low'].values[0]
    prev_low = data4_ly.loc[data4_ly['Year']==PREV_YEAR, 'low'].values[0]
    low_diff_pct=100.0*(curr_low-prev_low)/prev_low
    st.metric('low', value=curr_low, delta=f'{low_diff_pct:.2f}%')
with mx_high:
    curr_high = data4_ly.loc[data4_ly['Year']==CURR_YEAR, 'high'].values[0]
    prev_high = data4_ly.loc[data4_ly['Year']==PREV_YEAR, 'high'].values[0]
    high_diff_pct=100.0*(curr_high-prev_high)/prev_high
    st.metric('high', value=curr_high, delta=f'{high_diff_pct:.2f}%')
with mx_close:
    curr_close = data4_ly.loc[data4_ly['Year']==CURR_YEAR, 'close'].values[0]
    prev_close = data4_ly.loc[data4_ly['Year']==PREV_YEAR, 'close'].values[0]
    close_diff_pct=100.0*(curr_close-prev_close)/prev_close
    st.metric('close', value=curr_close, delta=f'{close_diff_pct:.2f}%')
st.caption("Keterangan : JANGAN LUPA DIISI")

st.header("Harga Setiap Saham")
st.caption("Harga Saham mulai Januari 2019 sampai Januari 2023")

tab1,tab2,tab3,tab4,tab5=st.tabs(['ASII','UNTR','AUTO','AALI','ASGR'])
with tab1:
    col1,col2=st.columns((3,1))
    with col1:
        # STOCK CANDLESTICK
        # ASII
        df_asii=pd.read_csv("ASII.csv")
        df_asii['timestamp'] = pd.to_datetime(df_asii['timestamp'])
        df_asii['year'] = df_asii['timestamp'].dt.year
        df_asii['month'] = df_asii['timestamp'].dt.month
        df_asii['day'] = df_asii['timestamp'].dt.day
        df_asii['SMA_10'] = df_asii.close.rolling(10, min_periods=1).mean()
        df_asii['SMA_30'] = df_asii.close.rolling(30, min_periods=1).mean()
        df_asii1=df_asii
        df_asii = df_asii.loc[(df_asii['timestamp'].dt.year >= 2019) & (df_asii['timestamp'].dt.year <= 2023)]
        fig = go.Figure(data=[
            go.Scatter(x=df_asii['timestamp'],
                    y=df_asii['SMA_10'],
                    mode='lines',
                    name='SMA10'),
            go.Scatter(x=df_asii['timestamp'],
                    y=df_asii['SMA_30'],
                    mode='lines',
                    name='SMA30'),
            go.Candlestick(x=df_asii['timestamp'],
                        open=df_asii['open'],
                        high=df_asii['high'],
                        low=df_asii['low'],
                        close=df_asii['close'],
                        name='Candlestick')
        ])
        fig.update_layout(title="ASII stock price",
                        xaxis_title='Date',
                        yaxis_title='Price')
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write(lorem.paragraphs(1))
with tab2:
    col1,col2=st.columns((3,1))
    with col1:
        #UNTR
        df_untr=pd.read_csv("UNTR.csv")
        df_untr['timestamp'] = pd.to_datetime(df_untr['timestamp'])
        df_untr['year'] = df_untr['timestamp'].dt.year
        df_untr['month'] = df_untr['timestamp'].dt.month
        df_untr['day'] = df_untr['timestamp'].dt.day
        df_untr['SMA_10'] = df_untr.close.rolling(10, min_periods=1).mean()
        df_untr['SMA_30'] = df_untr.close.rolling(30, min_periods=1).mean()
        df_untr1=df_untr
        df_untr = df_untr.loc[(df_untr['timestamp'].dt.year >= 2019) & (df_untr['timestamp'].dt.year <= 2023)]

        fig = go.Figure(data=[
            go.Scatter(x=df_untr['timestamp'],
                    y=df_untr['SMA_10'],
                    mode='lines',
                    name='SMA10'),
            go.Scatter(x=df_untr['timestamp'],
                    y=df_untr['SMA_30'],
                    mode='lines',
                    name='SMA30'),
            go.Candlestick(x=df_untr['timestamp'],
                        open=df_untr['open'],
                        high=df_untr['high'],
                        low=df_untr['low'],
                        close=df_untr['close'],
                        name='Candlestick')
        ])
        fig.update_layout(title="UNTR stock price",
                        xaxis_title='Date',
                        yaxis_title='Price')
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write(lorem.paragraphs(1))

with tab3:
    col1,col2=st.columns((3,1))
    with col1:
        #AUTO
        df_auto=pd.read_csv("AUTO.csv")
        df_auto['timestamp'] = pd.to_datetime(df_auto['timestamp'])
        df_auto['year'] = df_auto['timestamp'].dt.year
        df_auto['month'] = df_auto['timestamp'].dt.month
        df_auto['day'] = df_auto['timestamp'].dt.day
        df_auto['SMA_10'] = df_auto.close.rolling(10, min_periods=1).mean()
        df_auto['SMA_30'] = df_auto.close.rolling(30, min_periods=1).mean()
        df_auto1=df_auto
        df_auto = df_auto.loc[(df_auto['timestamp'].dt.year >= 2019) & (df_auto['timestamp'].dt.year <= 2023)]

        fig = go.Figure(data=[
            go.Scatter(x=df_auto['timestamp'],
                    y=df_auto['SMA_10'],
                    mode='lines',
                    name='SMA10'),
            go.Scatter(x=df_auto['timestamp'],
                    y=df_auto['SMA_30'],
                    mode='lines',
                    name='SMA30'),
            go.Candlestick(x=df_auto['timestamp'],
                        open=df_auto['open'],
                        high=df_auto['high'],
                        low=df_auto['low'],
                        close=df_auto['close'],
                        name='Candlestick')
        ])
        fig.update_layout(title="AUTO stock price",
                        xaxis_title='Date',
                        yaxis_title='Price')
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write(lorem.paragraphs(1))

with tab4:
    col1,col2=st.columns((3,1))
    with col1:
        #AALI
        df_aali=pd.read_csv("AALI.csv")
        df_aali['timestamp'] = pd.to_datetime(df_aali['timestamp'])
        df_aali['year'] = df_aali['timestamp'].dt.year
        df_aali['month'] = df_aali['timestamp'].dt.month
        df_aali['day'] = df_aali['timestamp'].dt.day
        df_aali['SMA_10'] = df_aali.close.rolling(10, min_periods=1).mean()
        df_aali['SMA_30'] = df_aali.close.rolling(30, min_periods=1).mean()
        df_aali1=df_aali
        df_aali = df_aali.loc[(df_aali['timestamp'].dt.year >= 2019) & (df_aali['timestamp'].dt.year <= 2023)]

        fig = go.Figure(data=[
            go.Scatter(x=df_aali['timestamp'],
                    y=df_aali['SMA_10'],
                    mode='lines',
                    name='SMA10'),
            go.Scatter(x=df_aali['timestamp'],
                    y=df_aali['SMA_30'],
                    mode='lines',
                    name='SMA30'),
            go.Candlestick(x=df_aali['timestamp'],
                        open=df_aali['open'],
                        high=df_aali['high'],
                        low=df_aali['low'],
                        close=df_aali['close'],
                        name='Candlestick')
        ])
        fig.update_layout(title="AALI stock price",
                        xaxis_title='Date',
                        yaxis_title='Price')
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write(lorem.paragraphs(1))

with tab5:
    col1,col2=st.columns((3,1))
    with col1:
        #ASGR
        df_asgr=pd.read_csv("ASGR.csv")
        df_asgr['timestamp'] = pd.to_datetime(df_asgr['timestamp'])
        df_asgr['year'] = df_asgr['timestamp'].dt.year
        df_asgr['month'] = df_asgr['timestamp'].dt.month
        df_asgr['day'] = df_asgr['timestamp'].dt.day
        df_asgr['SMA_10'] = df_asgr.close.rolling(10, min_periods=1).mean()
        df_asgr['SMA_30'] = df_asgr.close.rolling(30, min_periods=1).mean()
        df_asgr1=df_asgr
        df_asgr = df_asgr.loc[(df_asgr['timestamp'].dt.year >= 2019) & (df_asgr['timestamp'].dt.year <= 2023)]

        fig = go.Figure(data=[
            go.Scatter(x=df_asgr['timestamp'],
                    y=df_asgr['SMA_10'],
                    mode='lines',
                    name='SMA10'),
            go.Scatter(x=df_asgr['timestamp'],
                    y=df_asgr['SMA_30'],
                    mode='lines',
                    name='SMA30'),
            go.Candlestick(x=df_asgr['timestamp'],
                        open=df_asgr['open'],
                        high=df_asgr['high'],
                        low=df_asgr['low'],
                        close=df_asgr['close'],
                        name='Candlestick')
        ])
        fig.update_layout(title="ASGR stock price",
                        xaxis_title='Date',
                        yaxis_title='Price')
        st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write(lorem.paragraphs(1))

data_mean=pd.pivot_table(
    data=df_asii1,
    index='year',
    aggfunc={
        'volume':'mean',
    }
).reset_index()

data1_mean=pd.pivot_table(
    data=df_untr1,
    index='year',
    aggfunc={
        'volume':'mean',
    }
).reset_index()

data2_mean=pd.pivot_table(
    data=df_auto1,
    index='year',
    aggfunc={
        'volume':'mean',
    }
).reset_index()

data3_mean=pd.pivot_table(
    data=df_aali1,
    index='year',
    aggfunc={
        'volume':'mean',
    }
).reset_index()

data4_mean=pd.pivot_table(
    data=df_asgr1,
    index='year',
    aggfunc={
        'volume':'mean',
    }
).reset_index()

# HISTOGRAM    
col1, col2 = st.columns((1,3))
with col1:
    # Histogram Rataan Vol Saham per Tahun
    st.write(lorem.paragraphs(1))
with col2:
    # Histogram Rataan Vol Saham per Tahun
    df_hist_sum = pd.concat([data_mean.assign(dataset='ASII'), data1_mean.assign(dataset='UNTR'),
                    data2_mean.assign(dataset='AUTO'), data3_mean.assign(dataset='AALI'),
                    data4_mean.assign(dataset='ASGR')])
    fig = px.bar(df_hist_sum, x='year', y='volume', color='dataset',
                title="Rataan Volume Saham per Tahun ",
                labels={'year': 'Year', 'volume': 'Volume', 'dataset': 'Saham'})
    st.plotly_chart(fig, use_container_width=True)


st.header("Close trend")

#MULTISELECT CLOSE TRENDS
multitahun = st.multiselect(
    "Pilih tahun",
    [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002],
    default=[2022, 2021]
)
#CLOSE TRENDS ASII
filtered_df = df2[df2['Year'].isin(multitahun)]
close_line = alt.Chart(filtered_df).mark_line().encode(
    alt.X('Day:T', title='Days'),
    alt.Y('Normalized Close:Q', title='Normalized Close', aggregate='sum'),
    alt.Color('Year:N', title='Year')
).properties(
    title=f"Close Trend Saham ASII {', '.join(map(str, multitahun))}"
)
st.altair_chart(close_line, use_container_width=True)

row1, row2 = st.columns(2)
with row1:
    #CLOSE TRENDS UNTR
    filtered_df = df_norm_untr[df_norm_untr['Year'].isin(multitahun)]
    close_line = alt.Chart(filtered_df).mark_line().encode(
    alt.X('Day:T', title='Days'),
    alt.Y('Normalized Close:Q', title='Normalized Close', aggregate='sum'),
    alt.Color('Year:N', title='Year')
    ).properties(
    title=f"Close Trend Saham UNTR {', '.join(map(str, multitahun))}"
    )
    st.altair_chart(close_line, use_container_width=True)
with row2:
    #CLOSE TRENDS AUTO
    filtered_df = df_norm_auto[df_norm_auto['Year'].isin(multitahun)]
    close_line = alt.Chart(filtered_df).mark_line().encode(
        alt.X('Day:T', title='Days'),
        alt.Y('Normalized Close:Q', title='Normalized Close', aggregate='sum'),
        alt.Color('Year:N', title='Year')
    ).properties(
        title=f"Close Trend Saham AUTO {', '.join(map(str, multitahun))}"
    )
    st.altair_chart(close_line, use_container_width=True)
row1, row2 = st.columns(2)
with row1:
    #CLOSE TRENDS AALI
    filtered_df = df_norm_aali[df_norm_aali['Year'].isin(multitahun)]
    close_line = alt.Chart(filtered_df).mark_line().encode(
        alt.X('Day:T', title='Days'),
        alt.Y('Normalized Close:Q', title='Normalized Close', aggregate='sum'),
        alt.Color('Year:N', title='Year')
    ).properties(
        title=f"Close Trend Saham AALI {', '.join(map(str, multitahun))}"
    )
    st.altair_chart(close_line, use_container_width=True)
with row2:
    #CLOSE TRENDS AALI
    filtered_df = df_norm_asgr[df_norm_asgr['Year'].isin(multitahun)]
    close_line = alt.Chart(filtered_df).mark_line().encode(
        alt.X('Day:T', title='Days'),
        alt.Y('Normalized Close:Q', title='Normalized Close', aggregate='sum'),
        alt.Color('Year:N', title='Year')
    ).properties(
        title=f"Close Trend Saham ASGR {', '.join(map(str, multitahun))}"
    )
    st.altair_chart(close_line, use_container_width=True)

#gambar tiap tahun
# st.image('std close.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

"Dapat dilihat tren saham ASII untuk tiap tahun berbeda-beda sehingga harus dikaji lebih lanjut untuk meyakinkan investor dalam membeli saham."

"Untuk meyakinkan investor dalam membeli saham, berikut adalah prediksi yang diperoleh dengan menggunakan Gaussian Process dari data saham ASII untuk tahun 2022."


st.header("Prediksi Close Trend Saham")

#PREDICTION ASII
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
    'ASII Observation': Y22,
    'ASII Prediction': Ypredict22,
    'gpr22': gpr22
}
dfp1 = pd.DataFrame(data)

#Selang Kepercayaan 95%
df_conf = pd.DataFrame()
df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
df_conf.index = X22

fig = px.line(dfp1, x="X22", y=["ASII Observation","ASII Prediction"],
              color_discrete_sequence=["blue", "orange"],
              title="Prediksi Harga Saham ASII"
              )
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
fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["ASII Observation"], mode='lines', name='Observation', line=dict(color='blue'),showlegend=False))
fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["ASII Prediction"], mode='lines', name='Prediction', line=dict(color='orange'),showlegend=False))
fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                  hovermode='x unified')
st.plotly_chart(fig,use_container_width=True)

# st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.caption(
    "dengan MSE yang diperoleh sebesar 0.0710244182897843"
)
row1, row2 = st.columns(2)
with row1:
    #PREDICTION UNTR
    dfp=pd.read_csv("datapred_UNTR.csv")
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
        'UNTR Observation': Y22,
        'UNTR Prediction': Ypredict22,
        'gpr22': gpr22
    }
    dfp1 = pd.DataFrame(data)

    #Selang Kepercayaan 95%
    df_conf = pd.DataFrame()
    df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
    df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
    df_conf.index = X22

    fig = px.line(dfp1, x="X22", y=["UNTR Observation","UNTR Prediction"],
                color_discrete_sequence=["blue", "orange"],
                title="Prediksi Harga Saham UNTR"
                )
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
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["UNTR Observation"], mode='lines', name='Observation', line=dict(color='blue'),showlegend=False))
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["UNTR Prediction"], mode='lines', name='Prediction', line=dict(color='orange'),showlegend=False))
    fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                    hovermode='x unified')
    st.plotly_chart(fig,use_container_width=True)

    # st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(
        "dengan MSE yang diperoleh sebesar 1.107250719335884"
    )
with row2:
    #PREDICTION AUTO
    dfp=pd.read_csv("datapred_AUTO.csv")
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
        'AUTO Observation': Y22,
        'AUTO Prediction': Ypredict22,
        'gpr22': gpr22
    }
    dfp1 = pd.DataFrame(data)

    #Selang Kepercayaan 95%
    df_conf = pd.DataFrame()
    df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
    df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
    df_conf.index = X22

    fig = px.line(dfp1, x="X22", y=["AUTO Observation","AUTO Prediction"],
                color_discrete_sequence=["blue", "orange"],
                title="Prediksi Harga Saham AUTO"
                )
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
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["AUTO Observation"], mode='lines', name='Observation', line=dict(color='blue'),showlegend=False))
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["AUTO Prediction"], mode='lines', name='Prediction', line=dict(color='orange'),showlegend=False))
    fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                    hovermode='x unified')
    st.plotly_chart(fig,use_container_width=True)

    # st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(
        "dengan MSE yang diperoleh sebesar 0.04528807735627166"
    )

row1, row2 = st.columns(2)
with row1:
    #PREDICTION AALI
    dfp=pd.read_csv("datapred_AALI.csv")
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
        'AALI Observation': Y22,
        'AALI Prediction': Ypredict22,
        'gpr22': gpr22
    }
    dfp1 = pd.DataFrame(data)

    #Selang Kepercayaan 95%
    df_conf = pd.DataFrame()
    df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
    df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
    df_conf.index = X22

    fig = px.line(dfp1, x="X22", y=["AALI Observation","AALI Prediction"],
                color_discrete_sequence=["blue", "orange"],
                title="Prediksi Harga Saham AALI"
                )
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
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["AALI Observation"], mode='lines', name='Observation', line=dict(color='blue'),showlegend=False))
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["AALI Prediction"], mode='lines', name='Prediction', line=dict(color='orange'),showlegend=False))
    fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                    hovermode='x unified')
    st.plotly_chart(fig,use_container_width=True)

    # st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(
        "dengan MSE yang diperoleh sebesar 0.0304560674749706"
    )
with row2:
    #PREDICTION ASGR
    dfp=pd.read_csv("datapred_ASGR.csv")
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
        'ASGR Observation': Y22,
        'ASGR Prediction': Ypredict22,
        'gpr22': gpr22
    }
    dfp1 = pd.DataFrame(data)

    #Selang Kepercayaan 95%
    df_conf = pd.DataFrame()
    df_conf['Lower'] = Ypredict22 - 1.96 * gpr22
    df_conf['Upper'] = Ypredict22 + 1.96 * gpr22
    df_conf.index = X22

    fig = px.line(dfp1, x="X22", y=["ASGR Observation","ASGR Prediction"],
                color_discrete_sequence=["blue", "orange"],
                title="Prediksi Harga Saham ASGR"
                )
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
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["ASGR Observation"], mode='lines', name='Observation', line=dict(color='blue'),showlegend=False))
    fig.add_trace(go.Scatter(x=dfp1["X22"], y=dfp1["ASGR Prediction"], mode='lines', name='Prediction', line=dict(color='orange'),showlegend=False))
    fig.update_layout(showlegend=True, legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                    hovermode='x unified')
    st.plotly_chart(fig,use_container_width=True)

    # st.image('close predict.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(
        "dengan MSE yang diperoleh sebesar 0.02906138352811595"
    )

"Dari hasil prediksi, dapat diketahui bahwa tren dari harga saham aktual dengan prediksi tidak berbeda cukup jauh."
"Saat tren saham pada data aktual naik, tren prediksi juga naik. Begitupula saat tren data aktual turun, tren predikti turun."
"Meskipun masih ada kenaikan atau penurunan yang berbeda dari data aktual dengan data prediksi, hasil prediksi masih dapat digunakan sebagai acuan investor dalam membeli saham."