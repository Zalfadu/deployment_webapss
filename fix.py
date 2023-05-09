import streamlit as st
st.sidebar.title('Menu')
with st.sidebar:
        option = st.radio('Pilih salah satu:',['Pendahuluan','KALKON','KANGEN','Deteksi Bahaya Paparan Bahan Kimia'])
if option == "Pendahuluan": 
    st.image("https://i.pinimg.com/originals/6d/32/d9/6d32d95c7f04f8870a4980bd538bc3e4.gif")
    st.header(':blue[Website Perhitungan Konsentrasi dan Deteksi Bahaya Paparan Bahan Kimia Oleh Kelompok 7]')
    st.write("Dwi Herawati (2219066)")
    st.write("Ghina Salma (2219075)")
    st.write("Tiara Purnama Putri (2219176)")
    st.write("Uray Tya Keshia Maharani (2219177)")
    st.write("Zalfa Dhiya Ulhaq (2219186)")

if option == "KALKON":
    st.header(':red[Welcome to KALKON!] 🤭')
    st.subheader('KALkulator KONsentrasi')
    #Input slide
    progress_text = "Operation in progress. Please wait."
    #Input volume
    number1 = st.number_input('Masukan Volume Titran (mL)')
    st.write(f'Volume Titran adalah {number1}')
    #Input bobot sampel
    number2 = st.number_input('Masukan Bobot Sampel (mg) atau (kg)')
    st.write(f'Bobot Sampel adalah {number2}')
    #Input fp
    number3 = st.number_input('Masukan Faktor Pengencer')
    st.write(f'Faktor Pengencer adalah {number3}')
    #Input Berat Ekivalen
    number4 = st.number_input('Masukan Berat Ekivalen (mg/mgrek) atau Masukan Berat Molekul (mg/mmol)')
    st.write(f'Berat Ekivalen adalah {number4}')
    #Input Normalitas 
    number5 =  st.number_input('Masukan Normalitas (mgrek/ml) atau Masukan Molaritas (mmol/ml)')
    st.write(f'Normalitas atau Molaritas adalah {number4}')
    #Input Volume titrat
    number6 =  st.number_input('Volume titrat (mL)')
    st.write(f'Volume titrat adalah {number6}')
    #Input 10
    number7 = 1/1000
    #Input Persen 
    number8 = 100 
    if st.button('Hitung Normalitas'):
        Normalitas = number2/(number1*number3*number4)
        st.success(f'Normalitas adalah {Normalitas}N')
    if st.button('Hitung Molaritas'):
        Molaritas = number2/(number1*number3*number4)
        st.success(f'Molaritas adalah {Molaritas}M')
    if st.button('Hitung Kadar'):
        Kadar = number1*number3*number4*number5*number7*number8/number6
        st.success(f'Kadar adalah {Kadar}%')
    if st.button('Hitung PPM'):
        PPM = number1*number3*number4*number5/number2
        st.success(f'PPM adalah {PPM}PPM')
    else:
        st.write('Silahkan pencet tombol hitung :)')
        
if option == "KANGEN":
    #Write
    st.header(':orange[This is KANGEN!]🥰')
    st.subheader('KAlkulator peNGENceran')
    #Input slide
    progress_text = "Operation in progress. Please wait."
    #Input Konsentrasi
    number1 = st.number_input ('Masukkan Konsentrasi Sebelum Pengenceran')
    number2 = st.number_input ('Masukkan Konsentrasi Sesudah Pengenceran')
    #Input Volume
    number3 = st.number_input ('Masukkan Volume Sebelum Pengenceran (mL)')
    number4 = st.number_input ('Masukkan Volume Sesudah Pengenceran (mL)')
    if st.button ('Konsentrasi yang dicari adalah'):
        Konsentrasi = (number2*number4)/number3
        Konsentrasi = (number1*number3)/number4
        st.success(f'Konsentrasinya sebesar {Konsentrasi}')
    if st.button ('Volume yang dicari adalah') :
        Volume = (number2*number4)/number1
        Volume = (number1*number3)/number2
        st.success(f'Volumenya sebesar {Volume}')
    else :
        st.write ('Silahkan tekan tombol hitung :)')

if option == "Deteksi Bahaya Paparan Bahan Kimia": 
    #Write
    st.header(':green[Deteksi Bahaya Paparan Bahan Kimia]🧪')
    st.subheader('Mendeteksi tingkat aman ketika bekerja dengan bahan kimia berbahaya')
    #Input slide
    progress_text = "Operation in progress. Please wait."
    #Input durasi kerja/hari 
    durasi1 = st.number_input ('Masukkan durasi kerja/hari (jam)')
    #Input NAB-TLV-TWA senyawa
    ppm1 = st.number_input ('Masukkan batas ambang berdasarkan NAB-TLV-TWA (ppm)')
    #Input bahan kimia
    option = st.selectbox('Dengan Bahan Kimia Apa Anda Bekerja?',
    ('Hidrogen Sulfida', 'Amonia', 'Asam Sulfat'))
    st.write('You selected:', option)
    #Input durasi paparan 
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

  
 
