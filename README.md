# E-Commerce Public Dataset Analysis

## Deskripsi Proyek

Proyek ini merupakan analisis data terhadap **E-Commerce Public Dataset** dari Olist, sebuah dataset transaksi e-commerce di Brasil. Analisis dilakukan untuk memperoleh insight mengenai performa penjualan, kategori produk, perilaku pelanggan, serta pengalaman pelanggan terhadap layanan pengiriman.

Proyek ini mencakup tahapan Data Wrangling, Exploratory Data Analysis (EDA), Visualization & Explanatory Analysis, serta analisis lanjutan menggunakan metode RFM (Recency, Frequency, Monetary). Hasil analisis disajikan melalui notebook Jupyter dan dashboard interaktif menggunakan Streamlit.

## Dataset

Dataset yang digunakan adalah E-Commerce Public Dataset dari Olist.

Sumber dataset:
- [E-Commerce Public Dataset – Dicoding](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view?usp=sharing)
- [Olist Brazilian E-Commerce Dataset – Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Pertanyaan Bisnis

Analisis ini berfokus pada beberapa pertanyaan bisnis terkait performa penjualan dan pengalaman pelanggan. Pertanyaan bisnis dan batasan periode analisis dijelaskan lebih lanjut pada notebook `notebook.ipynb`.

## Struktur Direktori

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   ├── main_data.csv
│   ├── monthly_sales.csv
│   ├── category_sales.csv
│   ├── rfm_data.csv
│   └── segment_data.csv
│
├── data/
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── products_dataset.csv
│   ├── sellers_dataset.csv
│   └── product_category_name_translation.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Instalasi dan Persiapan

1. Pastikan Python sudah terinstal.
2. Clone atau unduh repository proyek ini.
3. Buka terminal pada direktori proyek.
4. Buat dan aktifkan virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

5. Instal seluruh library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## Menjalankan Notebook

Buka file `notebook.ipynb` menggunakan Jupyter Notebook atau Visual Studio Code.

Pastikan kernel Python yang digunakan sudah sesuai dengan environment proyek, kemudian jalankan seluruh cell secara berurutan.

## Menjalankan Dashboard

Masuk ke direktori utama proyek dan jalankan perintah:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka melalui browser pada alamat lokal yang diberikan oleh Streamlit, biasanya:

```text
http://localhost:8501
```

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Dashboard

Dashboard interaktif digunakan untuk menyajikan hasil analisis, meliputi:
- Ringkasan performa penjualan.
- Kategori produk dengan revenue tertinggi.
- Tren revenue bulanan.
- Hubungan keterlambatan pengiriman dengan review pelanggan.
- Informasi hasil analisis pelanggan.