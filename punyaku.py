#Library 
import streamlit as st

#Write
st.write ('Welcome')
st.subheader('ini adalah aplikasi untuk mengalikan bilangan bulat')

#input bilangan pertama 
number1 = st.number_input('masukan bilangan pertama')
st.write(f'bilangan pertama adalah {number1}')

#input bilangan kedua
number2 = st.number_input('masukan bilangan kedua')
st.write(f'bilangan kedua adalah {number2}')

if st.button('Hitung'):
        st.write(f'Hasil kali antara {number1} dan {number2} adalah {number1*number2}')
else:
    st.write('Silahkan pencet tombol hitung :)')