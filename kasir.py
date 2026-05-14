import streamlit as st




st.set_page_config(page_title="TOKO PANAGAN ORDER", layout="centered")

st.title("🛒 TOKO PANAGAN ORDER")

# Daftar harga
daftar_harga = {
    "Beras": 15000,
    "Gula": 16000,
    "Minyak": 18000,
    "Telur": 25000,
    "Mie Instan": 3500
}

# Session state buat nyimpen keranjang
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# Bagian pilih barang
st.subheader("Pilih Barang")
col1, col2 = st.columns([2, 1])

with col1:
    barang = st.selectbox("Pilih barang", list(daftar_harga.keys()))

with col2:
    jumlah = st.number_input("Jumlah", min_value=1, value=1, step=1)

if st.button("Tambah ke Keranjang"):
    harga = daftar_harga[barang]
    subtotal = harga * jumlah
    st.session_state.keranjang.append({
        "Barang": barang,
        "Harga": harga,
        "Jumlah": jumlah,
        "Subtotal": subtotal
    })
    st.success(f"{jumlah}x {barang} ditambahkan!")

# Tampilkan keranjang
st.subheader("Keranjang Belanja")
if st.session_state.keranjang:
    st.dataframe(st.session_state.keranjang, use_container_width=True)

    total_belanja = sum(item["Subtotal"] for item in st.session_state.keranjang)

    if total_belanja >= 100000:
        diskon = total_belanja * 0.1
        total_bayar = total_belanja - diskon
        st.info(f"Diskon 10%: Rp {int(diskon):,}")
    else:
        diskon = 0
        total_bayar = total_belanja

    st.markdown("---")
    st.metric("Subtotal", f"Rp {total_belanja:,}")
    st.metric("TOTAL BAYAR", f"Rp {int(total_bayar):,}")

    if st.button("Reset Keranjang"):
        st.session_state.keranjang = []
        st.rerun()
else:
    st.info("Keranjang masih kosong")

st.caption("Terima kasih sudah belanja!")

import streamlit as st
import urllib.parse

st.markdown("---")
st.subheader("Hubungi Kami")

no_wa = "6282118115124"  # Ganti dengan nomor WA kamu. Pakai 62, tanpa + dan 0 di depan
link_toko = "https://tokopanagan-fx5fvveg2krek97hfvl6os.streamlit.app"

# Pesan otomatis pas pelanggan klik
pesan = f"Halo, saya mau pesan dari TOKO PANAGAN ORDER. Ini link toko: {link_toko}"
pesan_encoded = urllib.parse.quote(pesan)
link_wa = f"https://wa.me/{no_wa}?text={pesan_encoded}"

col1, col2 = st.columns(2)

with col1:
    st.link_button("📱 Pesan via WhatsApp", link_wa)

with col2:
    st.link_button("🔗 Copy Link Toko", link_toko)

st.caption("Alamat: Jl. Contoh No. 123, Kota Kamu")
st.caption("Jam buka: 08:00 - 21:00")




import streamlit as st



st.markdown("---")
st.subheader("Bagikan Toko Ini")

link_toko = "https://tokopanagan-fx5fvveg2krek97hfvl6os.streamlit.app"

col1, col2 = st.columns(2)

with col1:
    st.link_button("📱 Share Link", link_toko)

with col2:
    st.code(link_toko, language="text")