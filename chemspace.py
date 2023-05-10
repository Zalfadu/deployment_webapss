import streamlit as st

#Memunculkan tampilan samping
st.sidebar.title('Menu')
with st.sidebar:
        option = st.radio('Pilih salah satu:',['INTRO','KALKON','KANGEN','DEBARAN','CLOSING'])
#Memunculkan halaman awal
if option == "INTRO": 
    st.markdown("<h1 style='text-align: center; color: blue;'>CHEMISTRY SPACE🌌</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Website khusus perhitungan untuk bidang Analisis Kimia dan terapannya</h4>", unsafe_allow_html=True)
    st.image("https://i.pinimg.com/originals/6d/32/d9/6d32d95c7f04f8870a4980bd538bc3e4.gif")
    #Memunculkan 3 menu 
    col1, col2, col3 = st.columns(3)
    with col1:
       st.header("KALKON")
       st.markdown(
        """
        KALKON merupakan singkatan Kalkulator Konsentrasi, dimana menu ini dapat membantu menghitung konsentrasi hasil standarisasi bahan baku sekunder dan penetapan kadar analit dalam sampel dengan metode TITRIMETRI
    """
    )


    with col2:
       st.header("KANGEN")
       st.markdown(
        """
        KANGEN merupakan singkatan Kalkulator Pengenceran, menu ini dapat membantu menghitung volume dan konsentrasi sebelum maupun sesudah proses pengenceran
    """
    )


    with col3:
       st.header("DEBARAN")
       st.markdown(
        """
        DEBARAN merupakan singkatan Deteksi Bahaya Paparan  bahan kimia yang berbahaya, dimana menu ini dapat mendeteksi tingkat aman bekerja dengan berbagai bahan kimia sesuai dengan Nilai Batas Ambang (TLV-TWA dan TLV-C). Selain itu dapat juga menghitung seberapa besar konsentrasi bahan kimia yang terpapar oleh pekerja selama satu hari bekerja
    """
    )
#Memunculkan judul 1
if option == "KALKON":
    st.header(':red[Welcome to KALKON!] 🤭')
    st.subheader('Kalkulator Konsentrasi')
    #Input slide
    progress_text = "Operation in progress. Please wait."
#Perhitungan judul 1
    #Khusus titrimetri
    st.write(":blue[*Perhitungan Konsentrasi Titran Khusus Titrimetri*]")
    #Input volume khusus titrimetri
    number1 = st.number_input('Masukkan Volume Titran (mL)')
    st.write(f'Volume Titran adalah {number1}')
    #Input bobot sampel
    number2 = st.number_input('Masukkan Bobot Sampel (mg) atau (kg)')
    st.write(f'Bobot Sampel adalah {number2}')
    #Input fp
    number3 = st.number_input('Masukkan Faktor Pengencer')
    st.write(f'Faktor Pengencer adalah {number3}')
    #Input Berat Ekivalen
    number4 = st.number_input('Masukkan Berat Ekivalen (mg/mgrek) atau Masukan Berat Molekul (mg/mmol)')
    st.write(f'Berat Ekivalen adalah {number4}')
    if st.button('Hitung Normalitas'):
        Normalitas = number2/(number1*number3*number4)
        st.success(f'Normalitas adalah {Normalitas}N')
    if st.button('Hitung Molaritas'):
        Molaritas = number2/(number1*number3*number4)
        st.success(f'Molaritas adalah {Molaritas}M')
    else:
        st.write('Silahkan tekan tombol hitung😊')       
    #Khusus Kadar b/v atau b/b
    st.write(':blue[*Perhitungan Konsentrasi Kadar Sampel %(b/b), %(b/v), atau ppm Khusus Titrimetri*]')
    #Input Normalitas Titran
    number15 =  st.number_input(
        'Normalitas (mgrek/ml) atau Masukan Molaritas (mmol/ml) dari Titran',
         step=1e-6,
        format="%.4f")
    st.write(f'Normalitas atau Molaritas adalah {number15}')
    #Input volume titran
    number16 = st.number_input('Volume Titran (mL)')
    st.write(f'Volume Titran adalah {number16}')
    #Input Volume titrat
    number17 =  st.number_input('Volume titrat/sampel (mL) atau (L)')
    st.write(f'Volume titrat/sampel adalah {number17}')
    #Input bobot sampel
    number18 = st.number_input('Berat sampel (mg) atau (kg)')
    st.write(f'Berat sampel adalam {number18}')
    #Input Berat Ekivalen
    number19 = st.number_input('Berat Ekivalen (mg/mgrek) atau Masukan Berat Molekul (mg/mmol)')
    st.write(f'Berat Ekivalen adalah {number19}')
    #Input 10
    number20 = 1/1000
    #Input fp
    number21 = st.number_input('Faktor Pengencer')
    st.write(f'Faktor Pengencer adalah {number21}')
    #Input Persen 
    number22 = 100 
    if st.button('Hitung Kadar % (b/v)'):
        Kadar = number15*number16*number19*number20*number22/number17
        st.success(f'Kadar sebesar {Kadar}%(b/v)')
    if st.button('Hitung Kadar % (b/b)'):
        Kadar = number15*number16*number19*number20*number22/number18
        st.success(f'Kadar sebesar {Kadar}%(b/b)')   
    if st.button('Hitung PPM'):
        ppm = number15*number16*number19/number17
        st.success(f'ppm sebesar {ppm}ppm')
    else:
        st.write('Silahkan tekan tombol hitung😊')
#Memunculkan judul 2        
if option == "KANGEN":
    #Write
    st.header(':orange[This is KANGEN!]🥰')
    st.subheader('Kalkulator Pengenceran')
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
        st.write ('Silahkan tekan tombol hitung 😊')
#Memunculkan judul 3
if option == "DEBARAN": 
    #Write
    st.header(':green[Deteksi Bahaya Paparan Bahan Kimia]🧪')
    st.subheader('Mendeteksi tingkat aman ketika bekerja dengan bahan kimia berbahaya')
    #Input slide
    progress_text = "Operation in progress. Please wait."
    #Input nama bahan kimia
    nama= st.text_input('Masukan bahan kimia yang digunakan')
    st.write(f'Nama bahan kimia yang anda gunakan adalah {nama}')
    #Input durasi kerja/hari 
    durasi1 = st.number_input ('Masukkan durasi kerja/hari (jam)')
    #Input NAB-TLV-TWA senyawa
    ppm1 = st.number_input ('Masukkan batas ambang berdasarkan NAB-TLV-TWA (ppm)')
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
        st.success(f'Konsentrasi senyawa {nama} yang terhirup adalah {konsentrasi}ppm')
    if st.button ('Konsentrasi senyawa yang terhirup selama satu hari berkerja adalah'):
        deteksi = (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
        st.success(f'Konsentrasi senyawa {nama} yang terhirup selama satu hari bekerja adalah {deteksi}ppm')
    if st.button("Hasil deteksi"):
        hasil =  (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
        if hasil >= ppm1:
           st.write("TIDAK AMAN😩")
        elif hasil <=ppm1:
           st.write("AMAN😍")
#Memunculkan judul 4
if option == "CLOSING": 
    st.markdown("<h1 style='text-align: center; color: blue;'>About The Programmer👩‍💻</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Oleh Kelompok 7</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Dwi Herawati (2219066)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Ghina Salma (2219075)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Tiara Purnama Putri (2219176)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Uray Tya Keshia Maharani (2219177)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Zalfa Dhiya Ulhaq (2219186)</h5>", unsafe_allow_html=True)
   

