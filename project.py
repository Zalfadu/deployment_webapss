import streamlit as st

#Write
st.header("Perhitungan Volume Teoritis Titrasi")
st.caption('Hanya dapat digunakan untuk standarisasi saja')
st.write('Oleh Kelompok 7')
st.write('Dwi Herawati             (2219066)')
st.write('Ghina Salma              (2219176)')
st.write('Tiara Purnama Putri      (2219176)')
st.write('Uray Tya Keshia Maharani (2219184)')
st.write('Zalfa Dhiya Ulhaq        (2219186)')

#Input normalitas
number1 = st.number_input('Masukan Normalitas Larutan (N)')
st.write(f'Normalitas Larutan adalah {number1}')

#Input bobot sampel
number2 = st.number_input('Masukan Bobot Sampel (mg)')
st.write(f'Bobot Sampel adalah {number2}')

#Input fp
number3 = st.number_input('Masukan Faktor Pengencer')
st.write(f'Faktor Pengencer adalah {number3}')

#Input Berat Ekivalen
number4 = st.number_input('Masukan Berat Ekivalen (mg/mgrek)')
st.write(f'Berat Ekivalen adalah {number4}')

if st.button('Hitung Volume Teoritis'):
        Volume_teoritis = number2/(number1*number3*number4)
        st.success(f'Volume Teoritis adalah {Volume_teoritis}mL')
else:
    st.write('Silahkan pencet tombol hitung :)')