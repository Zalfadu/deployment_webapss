import streamlit as st

#Memunculkan tampilan samping
st.sidebar.title('Menu')
with st.sidebar:
        option = st.radio('Pilih salah satu:',['INTRO','Kalkulator Khusus Konsentrasi','DEBARAN','CLOSING'])
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

   
#Memunculkan judul 2 
if option == "Kalkulator Khusus Konsentrasi":
    tab1, tab2, tab3 = st.tabs(["MATERI", "KALKON", "KANGEN"])

    with tab1:
        st.header("MATERI")
        st.subheader("Menu ini membantu menghitung konsentrasi hasil standarisasi, penetapan kadar, dan hasil pengenceran😁")
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>TITRIMETRI</h6>", unsafe_allow_html=True)
        st.write("Titrimetri (titrasi) adalah suatu metode analisis kimia kuantitatif dalam laboratorium dengan mereaksikan suatu zat atau sampel dengan larutan standar yang sudah baku atau diketahui konsentrasinya secara teliti")
        st.write("Melalui metode titrimetri dapat dihitung konsentrasi suatu zat dengan standarisasi (dalam kalkulator ini dengan satuan Normal & Molar), selain itu dapat dihitung kadar analit dalam suatu sampel (dalam kalkulator ini dengan satuan %(b/v),%(b/b),dan ppm)")
        st.image("https://i.pinimg.com/564x/d2/66/14/d266147674e2776cc7d4bc53281aa715.jpg")
        
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>KADAR (%b/v)</h6>", unsafe_allow_html=True)
        st.write('Kadar %(b/v) adalah persentase kadar yang menyatakan jumlah gram zat terlarut dalam setiap 100 mL larutan')
        
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>KADAR (%b/b)</h6>", unsafe_allow_html=True)
        st.write('Kadar %(b/b) adalah persentase kadar yang menyatakan jumlah gram zat terlarut dalam setiap 100 g larutan')
        
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>PART PER MILLION (ppm)</h6>", unsafe_allow_html=True)
        st.write("Part per million adalah jumlah satu bagian zat terlarut (1 mg) dalam satu juta bagian zat pelarut (1 L)")
        
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>NORMALITAS</h6>", unsafe_allow_html=True)
        st.write('Normalitas adalah ukuran konsentrasi dengan berat setara dalam gram per liter larutan, dimana berat setara itu sendiri didefinisikan sebagai ukuran kapasitas reaktif dari suatu molekul yang terlarut dalam larutan')
        st.write("Rumus Normalitas")
        st.latex(r'''
    N = \left(\frac{mg}{mL.BE.Fp}\right)
    ''')
        
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>MOLARITAS</h6>", unsafe_allow_html=True)
        st.write("Molaritas didefinisikan sebagai satuan konsentrasi larutan yang menyatakan jumlah mol zat terlarut dalam satu liter larutan")
        st.write("Rumus Molaritas")
        st.latex(r'''
    M = \left(\frac{mg}{mL.BM.Fp}\right)
    ''')
        
        
        st.markdown("<h6 style='text-align: center; color: black;'>PENGENCERAN</h6>", unsafe_allow_html=True)
        st.write('Pengenceran adalah suatu prosedur dengan tujuan untuk menurunkan konsentrasi suatu zat atau membuat suatu zat menjadi lebih encer dengan penambahan suatu zat pelarut')
        st.write("Rumus Pengenceran")
        st.latex(r'''
    Konsentrasi 1.Volume 1 = Konsentrasi 2.Volume 2
    ''')
        
        
    with tab2:
        st.header("KALKON")
        #Memunculkan judul 1
        st.header(':red[Welcome to KALKON!] 🤭')
        st.subheader('Kalkulator Konsentrasi')
        #Input slide
        progress_text = "Operation in progress. Please wait."
        #Perhitungan judul 1
        #Khusus titrimetri
        st.write(":blue[*Perhitungan Konsentrasi Titran Khusus Titrimetri*]")
        #Input volume khusus titrimetri
        number1 = st.number_input('Masukkan Volume Titran (mL)',format="%.2f")
        st.write(f'Volume Titran adalah {number1}')
        #Input bobot sampel
        number2 = st.number_input('Masukkan Bobot Sampel (mg) atau (kg)',format="%.4f")
        st.write(f'Bobot Sampel adalah {number2}')
        #Input fp
        number3 = st.number_input('Masukkan Faktor Pengencer',format="%.2f")
        st.write(f'Faktor Pengencer adalah {number3}')
        #Input Berat Ekivalen
        number4 = st.number_input('Masukkan Berat Ekivalen (mg/mgrek) atau Masukan Berat Molekul (mg/mmol)',format="%.2f")
        st.write(f'Berat Ekivalen adalah {number4}')
        if st.button('Hitung Normalitas'):
            Normalitas = number2/(number1*number3*number4)
            st.success(f'Normalitas adalah {Normalitas:.4f}N')
        if st.button('Hitung Molaritas'):
            Molaritas = number2/(number1*number3*number4)
            st.success(f'Molaritas adalah {Molaritas:.4f}M')
        else:
            st.write('Silahkan tekan tombol hitung😊')       
        #Khusus Kadar b/v atau b/b
        st.write(':blue[*Perhitungan Konsentrasi Kadar Sampel %(b/b), %(b/v), atau ppm Khusus Titrimetri*]')
        #Input Normalitas Titran
        number15 =  st.number_input('Normalitas (mgrek/ml) atau Masukan Molaritas (mmol/ml) dari Titran',format="%.4f")
        st.write(f'Normalitas atau Molaritas adalah {number15}')
        #Input volume titran
        number16 = st.number_input('Volume Titran (mL)',format="%.2f")
        st.write(f'Volume Titran adalah {number16}')
        #Input Volume titrat
        number17 =  st.number_input('Volume titrat/sampel (mL) atau (L)',format="%.2f")
        st.write(f'Volume titrat/sampel adalah {number17}')
        #Input bobot sampel
        number18 = st.number_input('Berat sampel (mg) atau (kg)',format="%.4f")
        st.write(f'Berat sampel adalam {number18}')
        #Input Berat Ekivalen
        number19 = st.number_input('Berat Ekivalen (mg/mgrek) atau Masukan Berat Molekul (mg/mmol)')
        st.write(f'Berat Ekivalen adalah {number19}')
        #Input 10
        number20 = 1/1000
        #Input fp
        number21 = st.number_input('Faktor Pengencer',)
        st.write(f'Faktor Pengencer adalah {number21}')
        #Input Persen 
        number22 = 100 
        if st.button('Hitung Kadar % (b/v)',):
            Kadar = number15*number16*number19*number20*number22/number17
            st.success(f'Kadar sebesar {Kadar:.2f}%(b/v)')
        if st.button('Hitung Kadar % (b/b)',):
            Kadar = number15*number16*number19*number20*number22/number18
            st.success(f'Kadar sebesar {Kadar:.2f}%(b/b)')   
        if st.button('Hitung PPM'):
            ppm = number15*number16*number19/number17
            st.success(f'ppm sebesar {ppm:.4f}ppm')
        else:
            st.write('Silahkan tekan tombol hitung😊')

    with tab3:
        st.header("KANGEN")
        #Write
        st.header(':orange[This is KANGEN!]🥰')
        st.subheader('Kalkulator Pengenceran')
        #Input slide
        progress_text = "Operation in progress. Please wait."
        #Input Konsentrasi
        number1 = st.number_input ('Masukkan Konsentrasi Sebelum Pengenceran',format="%.2f")
        number2 = st.number_input ('Masukkan Konsentrasi Sesudah Pengenceran',format="%.2f")
        #Input Volume
        number3 = st.number_input ('Masukkan Volume Sebelum Pengenceran (mL)',format="%.2f")
        number4 = st.number_input ('Masukkan Volume Sesudah Pengenceran (mL)',format="%.2f")
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
    tab4, tab5, tab6 = st.tabs(["MATERI","CEK NILAI AMBANG BATAS","DEBARAN"])

    with tab4:
        st.header("MATERI")
        st.markdown("<h6 style='text-align: center; color: black;'>APA ITU NILAI AMBANG BATAS?</h6>", unsafe_allow_html=True)
        st.write("Nilai Ambang Batas (NAB)/Threshold Limit Value adalah suatu standar faktor bahaya di tempat kerja sebagai kadar/intensitas rata-rata tertimbang waktu (Time Weighted Average) yang dapat diterima tenaga kerja tanpa mengakibatkan resiko penyakit atau gangguan kesehatan, dalam pekerjaan sehari-hari dengan waktu tidak melebihi 8 jam sehari atau 40 jam seminggu. (Permenakertrans  No.13/MEN/X/2011) tentang NAB Faktor fisika & Faktor Kimia di tempat kerja).")
        st.write("Di Indonesia, NAB zat kimia di udara tempat kerja yang mengacu pada SNI 19-0232-2005. Standar ini terdapat 3 jenis NAB :")
        st.markdown(
        """
1.	NAB rata-rata tertimbang waktu zat kimia di udara tempat kerja, dimana terdapat tenaga kerja yang dapat terpapar zat kimia sehari-hari selama tidak lebih dari 8 jam/hari atau 40 jam/minggu.

2.	NAB kadar tertinggi yang diperkenankan, yaitu kadar zat kimia di udara tempat kerja yang tidak boleh dilampaui meskipun dalam waktu sekejap


3.	NAB paparan singkat yang diperkenankan, yaitu kadar zat kimia di udara tempat kerja yang tidak boleh dilampaui agar tenaga kerja yang terpapar pada periode singkat (>15 menit), masih dalam kategori aman, tanpa mengakibatkan iritasi, kerusakan jaringan tubuh dan terbius.


        """
        )
        st.markdown("<h6 style='text-align: center; color: black;'>ACGIH (American Conference of Governmental Industrial Hygienists) dan TLVs (Threshold Limit Values)</h6>", unsafe_allow_html=True)
        st.write("TLV didalam ACGIH didefinisikan sebagai konsentrasi bahan kimia di udara tempat bekerja yang memberi gambaran kondisi pekerja yang dapat terpapar berulang kali pada keseluruhan waktu kerja dalam kehidupannya, tanpa menimbulkan efek kesehatan yang merugikan. TLV disusun untuk melindungi pekerja dewasa normal dan sehat. Terdapat 3 kategori TLV pada TLV-ACGIH ini, yaitu:")
        st.markdown(
        """
1.	TLV-TWA (Thershold Limit Value-Time Weighted Average), Konsentrasi rata-rata tertimbang waktu untuk 8 jam kerja atau 40 jam perminggu tanpa adanya efek kesehatan yang merugikan.

2.	TLV-STEL (Thershold Limit Value- Short Term Exposure Limit), Nilai ambang batas untuk paparan selama 15 menit yang tidak boleh dilampau pada setiap waktu selama hari kerja, meskipun 8 jam TWA mendekati (TLV-TWA) Maksimum terjadinya STEL adalah 4 kali dalam sehari & Terdapat jangka waktu 60 menit diantaranya, meskipun konsentrasinya tidak melebihi TLV-TWA, maka konsentrasi STEL tidak boleh melebihi 5 kali nilai TLV-TWAnya.

3.	TLV – Ceiling ((Thershold Limit Value-Ceiling), Konsentrasi tertinggi yang tidak diperkenankan tercapai pada setiap bagian paparan kerja.

        """
        )

    

       
    with tab5:
        st.header("CEK NILAI AMBANG BATAS")
        st.write("Pilih bahan kimia yang Anda gunakan untuk mengetahui nilai ambang batasnya")
        #Input slide
        progress_text = "Operation in progress. Please wait."
        option = st.selectbox('Masukan Nama Bahan Kimia',('Ammonia','Hydrogen Sulfide','Carbon Monoxide','Carbon Dioxide','Cyanide','Mercury','Acetone','Benzene','Etanol','Toluene','Sulfuric Acid','Methylphosphonofluoridate (Sarin)','Vinyl Chloride','Perchloroethylene (PCA)','Chloride Acid'))
        
        if option == 'Ammonia':
            title = st.write('Nilai ambang batas Ammonia berdasarkan TLV-TWA atau TLV-C adalah 25 ppm')
          
        if option == 'Hydrogen Sulfide':
            title = st.write('Nilai ambang batas Hydrogen Sulfide berdasarkan TLV-TWA atau TLV-C adalah 10 ppm')
         
        if option == 'Carbon Monoxide':
            title = st.write('Nilai ambang batas Carbon Monoxide berdasarkan TLV-TWA atau TLV-C adalah 35 ppm')
          
        if option == 'Carbon Dioxide':
            title = st.write('Nilai ambang batas Carbon Dioxide berdasarkan TLV-TWA atau TLV-C adalah 5000 ppm')
         
        if option == 'Cyanide':
            title = st.write('Nilai ambang batas Cyanide berdasarkan TLV-TWA atau TLV-C adalah 10 ppm')
              
        if option == 'Mercury':
            title = st.write('Nilai ambang batas Mercury berdasarkan TLV-TWA atau TLV-C adalah 0,000025 ppm')
              
        if option == 'Acetone':
            title = st.write('Nilai ambang batas Acetone berdasarkan TLV-TWA atau TLV-C adalah 250 ppm')
               
        if option == 'Benzene':
            title = st.write('Nilai ambang batas Benzene berdasarkan TLV-TWA atau TLV-C adalah 0,5 ppm')
            
        if option == 'Etanol':
            title = st.write('Nilai ambang batas Etanol berdasarkan TLV-TWA atau TLV-C adalah 1000 ppm')
             
        if option == 'Toluene':
            title = st.write('Nilai ambang batas Toluene berdasarkan TLV-TWA atau TLV-C adalah 20 ppm')
             
        if option == 'Sulfuric Acid':
            title = st.write('Nilai ambang batas Sulfuric Acid berdasarkan TLV-TWA atau TLV-C adalah 0,0002 ppm')
              
        if option == 'Methylphosphonofluoridate (Sarin)':
            title = st.write('Nilai ambang batas Methylphosphonofluoridate (Sarin) berdasarkan TLV-TWA atau TLV-C adalah 0,00000008 ppm')
               
        if option == 'Vinyl Chloride':
            title = st.write('Nilai ambang batas Vinyl Chloride berdasarkan TLV-TWA atau TLV-C adalah 1 ppm')
                
        if option == 'Perchloroethylene (PCA)':
            title = st.write('Nilai ambang batas Perchloroethylene (PCA) berdasarkan TLV-TWA atau TLV-C adalah 25 ppm')
              
        if option == 'Chloride Acid':
            title = st.write('Nilai ambang batas Chloride Acid berdasarkan TLV-TWA atau TLV-C adalah 2 ppm')
        st.write('Jika bahan kimia yang Anda gunakan tidak tersedia, silakan cek di link berikut : https://www.acgih.org/data-hub/')
        
    with tab6:
        st.header("DEBARAN")
        #Write
        st.header(':green[Deteksi Bahaya Paparan Bahan Kimia]🧪')
        st.write('Mendeteksi tingkat aman ketika bekerja dengan bahan kimia berbahaya')
        
        
        ppm1 = st.number_input ('Masukkan batas ambang berdasarkan NAB-TLV-TWA (ppm)',format="%.10f")
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
            st.success(f'Konsentrasi senyawa {option} yang terhirup adalah {konsentrasi:.4f}ppm')
        if st.button ('Konsentrasi senyawa yang terhirup selama satu hari berkerja adalah'):
            deteksi = (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
            st.success(f'Konsentrasi senyawa {option} yang terhirup selama satu hari bekerja adalah {deteksi} ppm')
        if st.button("Hasil deteksi"):
            hasil =  (durasi2 + durasi3 + durasi4)/durasi1*((ppm2*durasi2) + (ppm3*durasi3) + (ppm4*durasi4))/(durasi2 + durasi3 + durasi4)
            if hasil >=option:
               st.write("TIDAK AMAN😩")
            elif hasil <=option:
               st.write("AMAN😍")

#Memunculkan judul 4
if option == "CLOSING": 
    st.markdown("<h1 style='text-align: center; color: blue;'>Our Background😁</h1>", unsafe_allow_html=True)
    st.write("Website ini adalah tugas project mata kuliah Logika & Pemograman Komputer di Politeknik AKA Bogor, dimana pada tugas ini para mahasiswa membuat website yang berhubungan dengan bidang ilmu Analisis Kimia dan Terapannya sehingga dapat mempermudah aktivitas pembelajaran berbagai mata kuliah yang terkait")
    st.markdown("<h1 style='text-align: center; color: blue;'>Our Hope🤗</h1>", unsafe_allow_html=True)
    st.write('Seperti namanya yaitu CHEMISTRY SPACE kami berharap website ini dapat menjadi tempat berkembangnya penerapan bidang ilmu Analisis Kimia, baik sebagai kalkulator perhitungan atau bahkan aplikasi yang dapat membawa kemajuan bagi ilmu pengetahuan')
    st.markdown("<h1 style='text-align: center; color: blue;'>About The Programmer👩‍💻</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: black;'>Oleh Kelompok 7</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Dwi Herawati (2219066)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Ghina Salma (2219075)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Tiara Purnama Putri (2219176)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Uray Tya Keshia Maharani (2219177)</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Zalfa Dhiya Ulhaq (2219186)</h5>", unsafe_allow_html=True)
   
     
        

  
    
    
    
    
    
    
    