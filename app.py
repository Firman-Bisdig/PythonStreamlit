import streamlit as st
import numpy as np
import pandas as pd
import requests

# 1 Element Text di Streamlit
st.title("SELAMAT DATANG DI APLIKASI STREAMLIT")
st.header("Aplikasi Presentasi Data dengan Streamlit")
st.subheader("Mempelajari Data Science dan Machine Learning secara Praktis")
st.caption("Belajar menjadi lebih mudah dan menyenangkan!")
st.code("print('Halo, teman-teman! Selamat belajar Streamlit!')")
st.text("Ini adalah contoh teks biasa untuk memperkaya tampilan aplikasi.")
st.latex(r'''\int e^x \,dx = e^x + C''')
st.markdown("""
Selamat datang di aplikasi presentasi data ini!  
Di sini, Anda bisa mempelajari konsep dasar **Data Science** dan **Machine Learning** dengan cara yang interaktif dan sederhana.  
Gunakan menu dan fungsi yang tersedia untuk menjelajahi dan memahami data secara menyenangkan.
""")

# 2 Menampilkan DataFrame di Streamlit
data = {
    "Nama": ["Man", "Naufal", "Sifa", "Nadya", "Farel"],
    "Umur": [19, 18, 20, 25, 27],
    "Kota": ["Pangkep", "Kolaka", "Sudiang", "Gowa", "Bulukumba"],
    "Pekerjaan": ["Data Scientist", "Analyst", "Engineer", "Researcher", "Consultant"]
} 

df = pd.DataFrame(data)
st.write(df)
st.divider()

# 3 Menampilkan Data Menggunakan API
st.subheader("Data Pengguna dari API Publik")
API_URL = "https://jsonplaceholder.typicode.com/users"
response = requests.get(API_URL)
try:
    if response.status_code == 200:
        users = response.json()
        user_data = []
        for user in users:
            user_data.append({
                "ID": user["id"],
                "Nama": user["name"],
                "Username": user["username"],
                "Email": user["email"],
                "Kota": user["address"]["city"],
                "Telepon": user["phone"],
                "Website": user["website"],
                "Perusahaan": user["company"]["name"]
            })
        df = pd.DataFrame(user_data)
        st.dataframe(df)
    else:
        st.error(f"Gagal mengambil data dari API: Status code {response.status_code}")
except requests.exceptions.RequestException as e:
     st.error(f"Error koneksi API: {e}")

# 4 Menampilkan DataFrame Menggunakan EXCEL/PDF upload file
st.subheader("Upload File")
uploaded_file = st.file_uploader("Pilih file Excel/PDF (.xlsx/.pdf)", type=["xlsx", "xls", "csv", "pdf"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("Data dari File Excel/PDF")
        st.dataframe(df)
        if 'Umur' in df.columns:
            st.markdown("**Statistik Umur**")
            st.write(df["Umur"].describe())
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
else:
    st.info("Silakan unggah file Excel/PDF untuk menampilkan data.")

# 5 Menampilkan Data from NP
st.subheader("Data dari NP")
np_data = np.random.randint(10, 50, size=(5, 3))
st.write("Data NumPy array:")
st.write(np_data)

# 6 Metric di Streamlit
st.subheader("Menampilkan Metric Penting dari Model ML")
st.caption("Situs ringkasan performa dan statistik pembelajaran ML.")
col1, col2, col3 = st.columns(3)
col1.metric(label="Akurasi Model", value="92.5%", delta="+1.2%")
col2.metric(label="Loss Training", value="0.15", delta="-0.03")
col3.metric(label="Waktu Pelatihan", value="45 menit", delta="-5 menit")

# 7 Menampilkan Grafik
st.title("Line Chart: Progres Pembelajaran Machine Learning dengan 3 Metrik")
# Contoh data untuk 3 metrik selama 10 epoch
data = {
    "epoch": list(range(1, 11)),
    "Training Accuracy": [0.60, 0.68, 0.75, 0.80, 0.82, 0.85, 0.87, 0.89, 0.91, 0.93],
    "Validation Accuracy": [0.58, 0.65, 0.70, 0.74, 0.78, 0.80, 0.82, 0.83, 0.85, 0.86],
    "Training Loss": [0.9, 0.75, 0.6, 0.5, 0.4, 0.35, 0.3, 0.25, 0.22, 0.2]
}
df = pd.DataFrame(data)
df = df.set_index("epoch")
st.line_chart(df)
st.bar_chart(data)
st.area_chart(data)

# 8 Input Formulir
st.title("Formulir Data Pengguna")

with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_foto = st.file_uploader("Upload Foto")
    foto_kamera = st.camera_input("Ambil Foto dari Kamera")
    rating = st.slider("Rating Kepuasan", 1, 10)

    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data atas nama **{nama}** berhasil dikirim! 🎉")
    
    # Menampilkan data tambahan jika ingin
    st.write("### Data Dikirim:")
    st.write(f"- Alamat: {alamat}")
    st.write(f"- Usia: {usia} tahun")
    st.write(f"- Tanggal Lahir: {tanggal_lahir}")
    st.write(f"- Waktu Janjian: {waktu_janji}")
    st.write(f"- Jenis Kelamin: {jenis_kelamin}")
    st.write(f"- Hobi: {', '.join(hobi)}")
    st.write(f"- Warna Favorit: {warna_favorit}")
    st.write(f"- Rating Kepuasan: {rating}/10")
    
    if file_foto:
        st.image(file_foto, caption="Foto yang Diupload")
    elif foto_kamera:
        st.image(foto_kamera, caption="Foto dari Kamera")

# 9 contoh mini input ke2
st.title("Jualan Thrift - Input Pesanan")
st.header("Pilih Barang Thrift dan Jumlahnya")
# Thrift items with prices
thrift_items = {
    "Kaos Vintage": 50000,
    "Jaket Denim": 150000,
    "Sepatu Kets": 120000,
    "Tas Selempang": 75000,
    "Kacamata Retro": 60000,
    "Jam Tangan Klasik": 85000
}
order = {}
for item, price in thrift_items.items():
    qty = st.number_input(f"{item} (Rp {price:,}) - Jumlah", min_value=0, max_value=10, value=0, step=1, key=item)
    if qty > 0:
        order[item] = {"qty": qty, "price": price, "total": qty * price}
if order:
    st.subheader("Ringkasan Pesanan Thrift")
    total_price = 0
    for item, details in order.items():
        st.write(f"{item} x {details['qty']} = Rp {details['total']:,}")
        total_price += details['total']
    st.markdown(f"**Total Harga: Rp {total_price:,}**")
    if st.button("Submit Pesanan Thrift"):
        st.success("Pesanan thrift Anda telah diterima! Terima kasih sudah belanja.")
else:
    st.info("Silakan pilih barang thrift dan jumlahnya.")

# 10 Menampilkan Video
st.subheader("Menampilkan Video")
# Menampilkan video dari file lokal
st.video('c:\\Users\LENOVO\Videos\promosi.mp4')
# Menampilkan video dari URL (misalnya YouTube)
st.video('https://youtu.be/oejoowV-cek?si=gmSZtzjykN1emakh')


# 11 menggunakan sidebar
# Sidebar content about Machine Learning website
st.sidebar.title("Tentang Web Machine Learning")
st.sidebar.write("""
Selamat datang di website kami yang membahas **Machine Learning** secara lengkap.  
Di sini Anda dapat menemukan berbagai artikel, tutorial,  
dan proyek menarik tentang Data Science dan Machine Learning.
**Menu Navigasi:**
""")
choice = st.sidebar.radio(
    "Pilih topik yang ingin Anda jelajahi:",
    ("Pengantar ML", "Algoritma ML", "Proyek ML", "Sumber Belajar")
)
if choice == "Pengantar ML":
    st.sidebar.info("Mengenal dasar-dasar Machine Learning dan konsep pentingnya.")
elif choice == "Algoritma ML":
    st.sidebar.info("Jelajahi berbagai algoritma populer seperti regresi, klasifikasi, dan clustering.")
elif choice == "Proyek ML":
    st.sidebar.info("Lihat contoh proyek nyata yang menggunakan teknik Machine Learning.")
else:
    st.sidebar.info("Daftar sumber belajar dan referensi terbaik untuk memperdalam ilmu ML.")
