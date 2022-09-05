import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import data
pendidikan = pd.read_csv('cleaned_pendidikan.csv', index_col = 0)
populasi = pd.read_csv('cleaned_populasi.csv', index_col = 0)
usia = pd.read_csv('cleaned_usia.csv', index_col = 0)
prakerja = pd.read_csv('cleaned_prakerja.csv', index_col =0)

# page config
# st.set_page_config(layout='wide')

# sidebar distribusi
# st.sidebar.header('Distribusi Pengangguran')
# slider = st.sidebar.slider('Pilih Tahun', min_value = 2014, max_value = 2022, value = 2014)

# judul 
st.markdown('''<h1 style='text-align: center; color: black;'>
Pengaruh Program Kartu Prakerja Terhadap Angka Pengangguran di Indonesia
</h1>''', unsafe_allow_html=True)

# penulis
st.markdown('''<h3 style='text-align: center; color: black;'>
\n Dipublikasi pada 4 Agustus 2022 
\n By : Haoking Suryanatmaja
</h3>''', unsafe_allow_html=True)

# pendahuluan 1
st.markdown('''<div style="text-align: justify;">
Saat ini, pekerjaan merupakan hal yang langka karena persaingan yang ketat. Selain itu, populasi penduduk yang terus meningkat yang 
tidak diimbangi dengan pertumbuhan lapangan pekerjaan menyebabkan sekelompok masyarakat tidak memiliki pekerjaan atau disebut 
sebagai pengangguran. Oleh karena hal tersebut, lapangan pekerjaan perlu diperbanyak dan keahlian dari masyarakat perlu ditingkatkan
agar dapat bersaing dan mengurangi angka pengangguran.
</div>''', unsafe_allow_html=True)
st.write('')

# thumbnail
st.image('prakerja.png', caption = 'Ilustrasi Kartu Prakerja')

# pendahuluan 2 
st.markdown('''<div style="text-align: justify;">
Salah satu tindakan yang dilakukan oleh pemerintah adalah program kartu prakerja. Dengan program ini, masyarakat diharapkan dapat
meningkatkan wawasan dan pengetahuan serta mendapatkan keahlian sebagai tenaga kerja yang terampil agar dapat bersaing ataupun 
berwirausaha dan membuka lapangan pekerjaan.
</div>''', unsafe_allow_html=True)
st.markdown('')

# populasi indonesia 1
st.header('Populasi Penduduk Indonesia')
st.markdown('''<div style="text-align: justify;">
Berdasarkan data populasi yang diperoleh dari gapminder.org sejak tahun 1800, peningkatan penduduk Indonesia cukup signifikan.
Pada tahun 2020, penduduk Indonesia mencapai sekitar 274 jiwa dan jumlah ini akan terus bertambah. Pada tahun 2060-2070 populasi
Indonesia diprediksi akan mencapai puncak yaitu sekitar 330 juta jiwa.
</div>''', unsafe_allow_html=True)
st.markdown('')

# grafik populasi tahun 1800-2100
col1,col2 = st.columns(2)
with col1:
    tahun_awal = st.number_input(
            'Masukkan Tahun Awal', 
            min_value = 1800, 
            max_value= 2099, 
            value = 1800
            ) 
    tahun_awal = int(tahun_awal - 1800)
with col2:
    tahun_akhir = st.number_input(
        'Masukkan Tahun Akhir',
        min_value = 1801,
        max_value= 2100,
        value = 2000
        )
    tahun_akhir = int(tahun_akhir - 1800)

fig = plt.figure(figsize=(10, 6))
sns.lineplot(
    x="tahun",
    y = 'jumlah',
    data = populasi.iloc[tahun_awal:tahun_akhir,:]
    )
plt.title("Populasi Penduduk Indonesia Tahun 1800-2100", y=1.02, fontsize=18)
plt.xlabel('Tahun',fontweight='bold')
plt.ylabel('Jumlah Penduduk', fontweight='bold')
plt.ticklabel_format(style='plain', axis='y')
st.pyplot(fig)
st.caption('Sumber: gapminder.org')

# populasi indonesia 2
st.markdown('''<div style="text-align: justify;">
Hal ini tentu saja cukup mengkhawatirkan jika tidak ada perubahan yang terjadi terutama dari segi pekerjaan. Jumlah masyarakat
yang terus bertambah ini perlu diimbangi dengan kualitas diri dari masing-masing individu agar dapat bersaing dan berkreatifitas 
dalam berwirausaha.
</div>''', unsafe_allow_html=True)
st.markdown('')

# distribusi 1
st.header('Distribusi Pengangguran Berdasarkan Kategori')
st.markdown('''<div style="text-align: justify;">
Berdasarkan data yang diperoleh dari Badan Pusat Statistik, pengangguran dapat dilihat dari dua kategori yaitu usia dan pendidikan
terakhir yang ditempuh hingga tamat.
</div>''', unsafe_allow_html=True)
st.markdown('')

# distribusi usia
st.subheader('Usia')
st.markdown('''<div style="text-align: justify;">
Usia yang dikategorikan mulai dari umur 15 tahun hingga 60 tahun dengan interval sebesar 4 tahun.
</div>''', unsafe_allow_html=True)
st.markdown('')

# grafik distribusi usia tahun 2014-2022
slider_usia = st.slider(
    'Pilih tahun untuk melihat distribusi kelompok usia pengangguran per tahun', 
    min_value = 2014, max_value = 2022, value = 2014
    )
fig = plt.figure(figsize=(10, 5))
sns.barplot(
    x = 'jumlah_pengangguran',
    y = 'kelompok_usia', 
    data = usia[usia['tahun'] == slider_usia]
)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Distribusi Pengangguran Berdasarkan Usia", y=1.02, fontsize=18)
plt.xlabel('Jumlah Pengangguran', fontweight='bold')
plt.ylabel('Usia', fontweight='bold')
st.pyplot(fig)
st.caption('Sumber: Badan Pusat Statistik')

# new grafik usia

# distribusi usia 2
# st.markdown('''<div style="text-align: justify;">
# Sejak tahun 2014 hingga 2022 kategori usia yang mendominasi menjadi pengangguran adalah pada <b>rentang usia 20-24 tahun.</b> 
# Pada tahun 2014 hingga 2018 rentang usia 15-19 tahun menempati posisi kedua dan rentang 25-29 tahun pada posisi ketiga. 
# Namun, sejak tahun 2018 rentang usia 25-29 tahun mendominasi posisi kedua. Tenaga kerja yang pada awalnya pada usia muda 
# berpindah ke rentang usia yang lebih tua. Hal ini menunjukkan sejak tahun 2018 <b>tidak ada perubahan signifikan</b>     yang terjadi 
# terhadap pengangguran.
# </div>''', unsafe_allow_html=True)
# st.markdown('')

# disribusi pendidikan 1
st.subheader('Pendidikan')
st.markdown('''<div style="text-align: justify;">
Jumlah pengangguran juga dapat dilihat dari kategori pendidikan yaitu kategori belum bersekolah, lulusan SD, SMP, SMU/SMK, akademi, 
maupun universitas.
</div>''', unsafe_allow_html=True)
st.markdown('')

# grafik distribusi pendidikan tahun 2014-2022
slider_pendidikan = st.slider('Pilih Tahun', min_value = 2014, max_value = 2022, value = 2014)
fig = plt.figure(figsize=(10, 5))
sns.barplot(
    x = 'jumlah_pengangguran',
    y = 'kelompok_pendidikan', 
    data = pendidikan[pendidikan['tahun'] == slider_pendidikan]
)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Distribusi Pengangguran Berdasarkan Pendidikan Terakhir", y=1.02, fontsize=18)
plt.xlabel('Jumlah Pengangguran', fontweight='bold')
plt.ylabel('Pendidikan', fontweight='bold')
st.pyplot(fig)
st.caption('Sumber: Badan Pusat Statistik')

# distribusi pendidikan 2 
# st.markdown('''<div style="text-align: justify;">
# Sejak tahun 2014-2022, <b>kategori pendidikan tertinggi SMU</b> merupakan kategori yang memiliki jumlah pengangguran paling banyak.
# Selain itu, pengangguran juga didominasi dari <b>kategori SD, SLTP, dan SMK.</b>
# </div>''', unsafe_allow_html=True)
# st.markdown('')

# prakerja 1
st.header('Prakerja')
st.markdown('''<div style="text-align: justify;">
Jumlah pengangguran <b>meningkat drastis</b> pada tahun 2020-2021, hal ini dikarenakan dampak dari pandemi COVID-19 yang menyebabkan
berbagai sektor lumpuh yang akhirnya berdampak kepada tenaga kerja. Memasuki tahun 2022, jumlah pengangguran sudah mulai berkurang
</div>''', unsafe_allow_html=True)
st.markdown('')

# grafik jumlah pengangguran
fig = plt.figure(figsize=(10, 5))
sns.lineplot(x="tahun", y = 'jumlah_pengangguran', data = usia.groupby('tahun').sum())
plt.ticklabel_format(style='plain', axis='y')
plt.title("Jumlah Pengangguran Tahun 2014-2022", y=1.02, fontsize=18)
plt.xlabel('Tahun', fontweight='bold')
plt.ylabel('Jumlah Pengangguran', fontweight='bold')
st.pyplot(fig)
st.caption('Sumber: Badan Pusat Statistik')

# prakerja 2
st.markdown('''<div style="text-align: justify;">
Sejak bulan April tahun 2020, pemerintah sudah melaksanakan program kartu prakerja secara digital, mulai dari pendaftaran,
pelatihan, hingga insentif yang dapat digunakan sebagai modal usaha juga diberikan secara digital. Dampak yang dihasilkan sudah
dapat terlihat pada tahun 2021 dan 2022 karena <b>terbukti memberikan manfaat yang sangat positif</b> berdasarkan data yang 
diperoleh dari hasil prakerja.go.id.
</div>''', unsafe_allow_html=True)
st.markdown('')

st.header("Penerima Kartu Prakerja")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Jumlah Gelombang', 20)
with col2:
    st.metric('Rata-rata Penerima', 542636)
with col3:
    st.metric('Total Penerima Kartu Prakerja', 11938001)

# prakerja 3
# st.markdown('''<div style="text-align: justify;">
# Dari 11 juta penerima manfaat program Kartu Prakerja, diperoleh data survei dibawah ini.
# Sebanyak <b>25,6%</b> terjun menjadi wirausahawan, karena 
# telah mendapatkan bekal pengetahuan dari mengikuti pelatihan. <b>Sejumlah 34,6%</b> yang semula menganggur kini sudah mendapatkan 
# pekerjaan dengan menyertakan sertifikat pelatihan. Namun, <b>masih ada 39,85%</b> yang masih belum mendapatkan pekerjaan.
# </div>''', unsafe_allow_html=True)

# pie chart
labels = ['Wirausaha', 'Bekerja', 'Belum Bekerja']
sizes = [25.6, 34.6, 39.8]
explode = (0, 0, 0.1) 

fig1, ax1 = plt.subplots(figsize=(5,2))
ax1.pie(sizes, explode=explode, labels=labels, radius=1, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)
st.caption('Sumber: prakerja.go.id')

# Prakerja 4
# st.markdown('''<div style="text-align: justify;">
# </div>''', unsafe_allow_html=True)

# insight 
st.header('Insight')
st.markdown('''
- Populasi penduduk akan terus bertambah sehingga perlu dilakukan peningkatan kualitas dari masyarakat agar dapat bersaing ataupun memulai wirausaha sehingga dapat membuka lapangan pekerjaan
- Pada tahun 2021, kategori pengangguran yang dominan masih dalam usia muda (20-24 tahun) dan memiliki dasar pengetahuan dan potensi (SMU) sehingga pemerintah perlu memfokuskan program kartu prakerja ke golongan tersebut 
- Hal ini merupakan salah satu tindakan yang tepat dilakukan pemerintah dalam menangani pengangguran dengan menyediakan fasilitas bagi pengangguran yang terdampak
- Prakerja belum dapat menurunkan angka pengangguran secara signifikan, hal ini dapat ditingkatkan dengan memperbesar kuota penerima kartu prakerja
''', unsafe_allow_html=True)
