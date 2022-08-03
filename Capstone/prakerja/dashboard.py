from multiprocessing.sharedctypes import Value
from xml.dom import ValidationErr
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import lorem

# import data
pendidikan = pd.read_csv('cleaned_pendidikan.csv', index_col = 0)
populasi = pd.read_csv('cleaned_populasi.csv', index_col = 0)
usia = pd.read_csv('cleaned_usia.csv', index_col = 0)
prakerja = pd.read_csv('cleaned_prakerja.csv', index_col =0)

# page config
# st.set_page_config(layout='wide')

# sidebar
st.sidebar.header('Populasi Penduduk Indonesia')
col1,col2 = st.sidebar.columns(2)
with col1:
    tahun_awal = int(st.number_input('Masukkan Tahun Awal', min_value = 1800, max_value= 2099, value = 1800) - 1800)
with col2:
    tahun_akhir = int(st.number_input('Masukkan Tahun Akhir', min_value = 1801, max_value= 2100, value = 2000) - 1800)
st.sidebar.header('Distribusi Pengangguran')
slider = st.sidebar.slider('Pilih Tahun', min_value = 2014, max_value = 2022, value = 2014)

# center title 
st.markdown('''<h1 style='text-align: center; color: black;'>
Pengaruh Program Kartu Prakerja Terhadap Angka Pengangguran di Indonesia
</h1>''', unsafe_allow_html=True)

st.markdown('''<h3 style='text-align: center; color: black;'>
\n Dipublikasi pada 4 Agustus 2022 
\n By : Haoking Suryanatmaja
</h3>''', unsafe_allow_html=True)

st.markdown('''<div style="text-align: justify;">
Saat ini, pekerjaan merupakan hal yang langka karena persaingan yang ketat. Selain itu, populasi penduduk yang terus meningkat yang 
tidak diimbangi dengan pertumbuhan lapangan pekerjaan menyebabkan sekelompok masyarakat tidak memiliki pekerjaan atau disebut 
sebagai pengangguran. Oleh karena hal tersebut, lapangan pekerjaan perlu diperbanyak dan keahlian dari masyarakat perlu ditingkatkan
agar dapat bersaing dan mengurangi angka pengangguran.
</div>''', unsafe_allow_html=True)
st.write('')

# thumbnail
st.image('prakerja.png', caption = 'Ilustrasi Kartu Prakerja')

st.markdown('''<div style="text-align: justify;">
Salah satu tindakan yang dilakukan oleh pemerintah adalah program kartu prakerja. Dengan program ini, masyarakat diharapkan dapat
meningkatkan wawasan dan pengetahuan serta mendapatkan keahlian sebagai tenaga kerja yang terampil agar dapat bersaing ataupun 
berwirausaha dan membuka lapangan pekerjaan.
</div>''', unsafe_allow_html=True)
st.markdown('')

# populasi indonesia
st.header('Populasi Penduduk Indonesia')
st.markdown('''<div style="text-align: justify;">
Berdasarkan data populasi yang diperoleh dari gapminder.org sejak tahun 2018, peningkatan penduduk Indonesia cukup signifikan.
Pada tahun 2020, penduduk Indonesia mencapai sekitar 274 jiwa dan jumlah ini akan terus bertambah. Pada tahun 2060-2070 populasi
Indonesia diprediksi akan mencapai puncak yaitu sekitar 330 juta jiwa.
</div>''', unsafe_allow_html=True)
st.markdown('')

fig = plt.figure(figsize=(10, 6))
plt.title("Populasi Penduduk Indonesia Tahun 1800-2100", y=1.02, fontsize=18)
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk')
sns.lineplot(x="tahun", y = 'jumlah', data = populasi.iloc[tahun_awal:tahun_akhir,:])
plt.ticklabel_format(style='plain', axis='y')
st.pyplot(fig)

st.markdown('''<div style="text-align: justify;">
Hal ini tentu saja cukup mengkhawatirkan jika tidak ada perubahan yang terjadi terutama dari segi pekerjaan. Jumlah masyarakat
yang terus bertambah ini perlu diimbangi dengan kualitas diri dari masing-masing individu agar dapat bersaing dan berkreatifitas 
dalam berwirausaha.
</div>''', unsafe_allow_html=True)
st.markdown('')

st.header('Distribusi Pengangguran Berdasarkan Kategori')
st.markdown('''<div style="text-align: justify;">
Berdasarkan data yang diperoleh dari Badan Pusat Statistik, pengangguran dapat dilihat dari dua kategori yaitu usia dan pendidikan
terakhir yang ditempuh hingga tamat.
</div>''', unsafe_allow_html=True)
st.markdown('')

# pengangguran vs usia
st.subheader('Usia')
st.markdown('''<div style="text-align: justify;">
Usia yang dikategorikan mulai dari umur 15 tahun hingga 60 tahun dengan interval sebesar 4 tahun.
</div>''', unsafe_allow_html=True)
st.markdown('')

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    x = 'jumlah_pengangguran',
    y = 'kelompok_usia', 
    data = usia[usia['tahun'] == slider]
)
plt.title("Distribusi Pengangguran Berdasarkan Usia", y=1.02, fontsize=18)
plt.xlabel('Jumlah Pengangguran')
plt.ylabel('Usia')
plt.ticklabel_format(style='plain', axis='x')
st.pyplot(fig)

st.markdown('''<div style="text-align: justify;">
Sejak tahun 2014 hingga 2022 kategori usia yang mendominasi menjadi pengangguran adalah pada rentang 20-24 tahun. Pada tahun 2014
hingga 2018 rentang 15-19 tahun menempati posisi kedua dan rentang 25-29 tahun pada posisi ketiga. Namun, sejak tahun 2018 rentang
25-29 tahun mendominasi posisi kedua. Tenaga kerja yang pada awalnya pada usia muda berpindah ke rentang usia yang lebih tua. Hal ini
menunjukkan tidak ada perubahan signifikan yang terjadi terhadap pengangguran.
</div>''', unsafe_allow_html=True)
st.markdown('')

# pengangguran vs pendidikan
st.subheader('Pendidikan')
st.markdown('''<div style="text-align: justify;">
Jumlah pengangguran juga dapat dilihat dari kategori pendidikan yaitu kategori belum bersekolah, lulusan SD, SMP, SMU/SMK, akademi, 
maupun universitas.
</div>''', unsafe_allow_html=True)
st.markdown('')

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    x = 'jumlah_pengangguran',
    y = 'kelompok_pendidikan', 
    data = pendidikan[pendidikan['tahun'] == slider]
)
plt.title("Distribusi Pengangguran Berdasarkan Pendidikan Terakhir", y=1.02, fontsize=18)
plt.xlabel('Jumlah Pengangguran')
plt.ylabel('Pendidikan')
plt.ticklabel_format(style='plain', axis='x')
st.pyplot(fig)

st.markdown('''<div style="text-align: justify;">
Sejak tahun 2014-2022, kategori pendidikan tertinggi SMU merupakan kategori yang memiliki jumlah pengangguran paling banyak. Selain itu,
pengangguran juga didominasi dari kategori SD, SLTP, dan SMK. 
</div>''', unsafe_allow_html=True)
st.markdown('')

# prakerja
st.header('Prakerja')
st.markdown('''<div style="text-align: justify;">
Jumlah pengangguran meningkat drastis pada tahun 2020-2021, hal ini dikarenakan dampak dari pandemi COVID-19 yang menyebabkan
berbagai sektor lumpuh yang akhirnya berdampak kepada tenaga kerja. Memasuki tahun 2022, jumlah pengangguran sudah mulai berkurang
</div>''', unsafe_allow_html=True)
st.markdown('')

col1,col2 = st.columns(2)
with col1:
    fig = plt.figure(figsize=(10, 5))
    plt.title("Jumlah Pengangguran Tahun 2014-2022", y=1.02, fontsize=18)
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Pengangguran')
    sns.lineplot(x="tahun", y = 'jumlah_pengangguran', data = usia.groupby('tahun').sum())
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig)
with col2:
    fig = plt.figure(figsize=(10, 5))
    plt.title("Penerima Kartu Prakerja", y=1.02, fontsize=18)
    plt.xlabel('gelombang')
    plt.ylabel('Penerima')
    sns.lineplot(x="gelombang", y = 'penerima', data = prakerja)
    plt.ticklabel_format(style='plain', axis='y')
    st.pyplot(fig)

st.markdown('''<div style="text-align: justify;">
Sejak bulan April tahun 2020, pemerintah sudah melaksanakan program kartu prakerja secara digital, mulai dari pendaftaran,
pelatihan, hingga insentif yang dapat digunakan sebagai modal usaha juga diberikan secara digital. Kartu Prakerja terbukti memberikan 
manfaat yang sangat positif, dibuktikan dengan hasil survei oleh prakerja.go.id.
</div>''', unsafe_allow_html=True)
st.markdown('')

st.markdown('''<div style="text-align: justify;">
Dari 11 juta penerima manfaat program Kartu Prakerja,
diperoleh data survei dibawah ini. Sebanyak 90% belum pernah mengikuti pelatihan apapun sebelum mendapatkan kartu prakerja. 
Menggunakan insentif Kartu Prakerja untuk modal usaha sebesar 42,4%. Sebanyak 25,6% sekarang terjun jadi wirausaha, karena 
telah mendapatkan bekal pengetahuan dari mengikuti pelatihan. 34,6% yang semula menganggur kini sudah mendapatkan pekerjaan 
dengan menyertakan sertifikat pelatihan. Namun masih ada 39,85% yang masih belum mendapatkan pekerjaan.
</div>''', unsafe_allow_html=True)

st.header('Insight')
st.markdown('''
- Populasi penduduk akan terus bertambah sehingga perlu dilakukan peningkatan kualitas dari masyarakat agar dapat bersaing dengan  tenaga kerja luar ataupun memulai wirausaha sehingga dapat membuka lapangan pekerjaan
- Kategori pengangguran yang dominan masih dalam usia produktif dan memiliki dasar pengetahuan sehingga bisa dilakukan pelatihan  untuk meningkatkan wawasan dan daya saing
- Program kartu prakerja merupakan salah satu tindakan yang tepat dilakukan pemerintah dalam menangani pengangguran dengan menyediakan  fasilitas bagi tenaga kerja, namun belum dapat menurunkan angka pengangguran secara signifikan
''', unsafe_allow_html=True)

st.caption('Sumber data: gapminder.org, bps.go.id, kompas.com, prakerja.go.id')