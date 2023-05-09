import streamlit as st
nama= st.text_input('Masukan Nama Bahan kimia')
st.write(f'Nama Bahan Kimia yang Anda Gunakan Adalah {nama}')

ppm1= st.text_input('Masukan Ambang Batas Bahan Kimia yang Anda Gunakan Sesuai dengan NAB-TLV-TWA (ppm)')
st.write(f'Ambang Batas dari Bahan Kimia yang Anda Gunakan Adalah {nama}')

st.caption('Durasi Jam Bekerja')
durasi1 = st.number_input ('Masukkan durasi kerja/hari (jam)')
st.caption('Waktu paparan pertama')
ppm2 = st.number_input ('Masukkan konsentrasi senyawa yang terhirup pertama (ppm)')
durasi2 = st.number_input ('Masukkan durasi terpapar pertama (jam)')
st.caption('Waktu paparan kedua')
ppm3 = st.number_input ('Masukkan konsentrasi senyawa yang terhirup kedua (ppm)')
durasi3 = st.number_input ('Masukkan durasi terpapar kedua (jam)')
st.caption('Waktu paparan ketiga')
ppm4 = st.number_input ('Masukkan konsentrasi senyawa yang terhirup ketiga (ppm)')
durasi4 = st.number_input ('Masukkan durasi terpapar ketiga (jam)')
if st.button ('Konsentrasi senyawa yang terhirup/jam bekerja adalah'):
    konsentrasi = ((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
    st.success(f'{konsentrasi}ppm')
if st.button ('Konsentrasi senyawa yang terhirup selama satu hari berkerja adalah'):
    deteksi = (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
    st.success(f'{deteksi}ppm')
if st.button("hasil deteksi"):
    hasil =  (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
    if hasil >= ppm1:
        st.write("Tidak aman😩")
    elif hasil <=ppm1:
        st.write("aman😍")