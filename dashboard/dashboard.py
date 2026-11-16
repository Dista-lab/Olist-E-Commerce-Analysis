
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    data_path = Path(__file__).resolve().parent / "main_data.csv"
    df = pd.read_csv(data_path)
    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )
    return df


main_df = load_data()

# =========================
# TITLE
# =========================
st.title("📊 E-Commerce Public Dataset Dashboard")

st.markdown(
    """
    Dashboard interaktif untuk menganalisis:
    - kontribusi revenue berdasarkan kategori produk,
    - tren revenue bulanan,
    - hubungan keterlambatan pengiriman dengan review pelanggan.
    """
)

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("🔎 Filter")

min_date = main_df["order_purchase_timestamp"].min().date()
max_date = main_df["order_purchase_timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Pastikan user memilih dua tanggal
if len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1)

    filtered_df = main_df[
        (main_df["order_purchase_timestamp"] >= start_date)
        & (main_df["order_purchase_timestamp"] < end_date)
    ]

else:
    filtered_df = main_df.copy()


# =========================
# KPI
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"BRL {filtered_df['price'].sum():,.2f}"
    )

with col2:
    st.metric(
        "Total Pesanan",
        f"{filtered_df['order_id'].nunique():,}"
    )

with col3:
    st.metric(
        "Total Produk Terjual",
        f"{len(filtered_df):,}"
    )


st.divider()


# =========================
# PERTANYAAN 1
# =========================
st.header(
    "1️⃣ Kategori Produk dengan Revenue Tertinggi"
)

revenue_per_category = (
    filtered_df
    .groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

col1, col2 = st.columns(2)

# ---- Bar chart ----
with col1:

    fig1, ax1 = plt.subplots(figsize=(8, 6))

    ax1.barh(
        revenue_per_category.index[::-1],
        revenue_per_category.values[::-1]
    )

    ax1.set_xlabel("Total Revenue (BRL)")
    ax1.set_ylabel("Kategori Produk")
    ax1.set_title("10 Kategori dengan Revenue Tertinggi")

    plt.tight_layout()

    st.pyplot(fig1)


# ---- Monthly revenue ----
with col2:

    monthly_revenue = (
        filtered_df
        .set_index("order_purchase_timestamp")
        .resample("ME")["price"]
        .sum()
    )

    fig2, ax2 = plt.subplots(figsize=(8, 6))

    ax2.plot(
        monthly_revenue.index,
        monthly_revenue.values,
        marker="o"
    )

    ax2.set_title("Tren Revenue Bulanan")
    ax2.set_xlabel("Bulan")
    ax2.set_ylabel("Revenue (BRL)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)


# =========================
# PERTANYAAN 2
# =========================
st.divider()

st.header(
    "2️⃣ Keterlambatan Pengiriman vs Review Score"
)

review_data = (
    filtered_df
    .dropna(subset=["review_score", "is_late"])
    .drop_duplicates(subset=["order_id"])
)

if len(review_data) > 0:

    avg_review = (
        review_data
        .groupby("is_late")["review_score"]
        .mean()
    )

    labels = [
        "Tepat Waktu" if not value else "Terlambat"
        for value in avg_review.index
    ]

    fig3, ax3 = plt.subplots(figsize=(7, 5))

    bars = ax3.bar(
        labels,
        avg_review.values
    )

    ax3.set_ylim(0, 5)
    ax3.set_ylabel("Rata-rata Review Score")
    ax3.set_title(
        "Rata-rata Review Score berdasarkan Ketepatan Pengiriman"
    )

    for bar in bars:

        height = bar.get_height()

        ax3.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            f"{height:.2f}",
            ha="center"
        )

    plt.tight_layout()

    st.pyplot(fig3)

else:

    st.warning(
        "Tidak ada data review pada rentang tanggal yang dipilih."
    )


# =========================
# DATA PREVIEW
# =========================
st.divider()

with st.expander("📄 Lihat Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


# =========================
# FOOTER
# =========================
st.caption(
    "Dibuat untuk submission akhir "
    "Belajar Fundamental Analisis Data - Dicoding"
)
