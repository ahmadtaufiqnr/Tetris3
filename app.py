import streamlit as st
import datetime
from lorem_text import lorem

st.set_page_config(
    page_title='COBA',
    layout='wide'
)

st.write("Hello world!")

"Hello"
st.title("Judul")
st.header("Header")
st.caption("HAHAHAHA")
st.code('''
import pandas as pd
import sreamlit as st
#streamlit run app.py
''')
st.latex("ax^2+bx+c=0")

#WIDGET input tombol
tombol=st.button("Tekan ini")
tombol

saya_setuju=st.checkbox("Centang jika setuju")
if saya_setuju:
    st.write("Anda setuju")
else:
    st.write("Belajar")

#radiobutton
buah_fav=st.radio(
    "Pilihan",
    ['Apel','Anggur','Jeruk','Mangga']
)
buah_fav

makanan=st.selectbox(
    "Pilihan",
    ['Nasgor','Mie','dkk']
)
makanan

#multiselect
minum=st.multiselect(
    "Pilihan",
    ['apa','siapa']
)

Ukuran=st.select_slider(
    "Ukuran",
    ['SS','S','M']
)
Ukuran

params = st.slider(
    "insert alpha val",
    min_value=0.0,
    max_value=1.0,
    step=0.1,
    value=0.5
)
params

with st.sidebar:
    st.title('Titanic')
    your_name=st.text_input("enter name")

    with st.expander('lorem ipsum'):
        st.write(lorem.paragraphs(1))

tab1,tab2,tab3=st.tabs(['Tab1','Tab2','Tab3'])

with tab1:
    st.write(lorem.paragraphs(1))