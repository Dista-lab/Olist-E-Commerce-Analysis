
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Lokasi file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Membaca dataset
main_data = pd.read_csv(os.path.join(BASE_DIR, "main_data.csv"))
segment_data = pd.read_csv(os.path.join(BASE_DIR, "segment_data.csv"))
monthly_sales = pd.read_csv(os.path.join(BASE_DIR, "monthly_sales.csv"))
category_sales = pd.read_csv(os.path.join(BASE_DIR, "category_sales.csv"))

# Judul dashboard
st.title("🛒 Olist E-Commerce Analytics Dashboard")
st.markdown("Dashboard analisis penjualan dan segmentasi pelanggan Olist")

st.divider()

# Filter tanggal
if "order_purchase_timestamp" in main_data.columns:
    main_data["order_purchase_timestamp"] = pd.to_datetime(
        main_data["order_purchase_timestamp"]
    )

    min_date = main_data["order_purchase_timestamp"].min().date()
    max_date = main_data["order_purchase_timestamp"].max().date()

    date_range = st.date_input(
        "Pilih rentang tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        filtered_data = main_data[
            (main_data["order_purchase_timestamp"].dt.date >= date_range[0]) &
            (main_data["order_purchase_timestamp"].dt.date <= date_range[1])
        ]
    else:
        filtered_data = main_data.copy()
else:
    filtered_data = main_data.copy()

# KPI
st.subheader("Ringkasan Penjualan")

col1, col2, col3 = st.columns(3)

with col1:
    total_orders = (
        filtered_data["order_id"].nunique()
        if "order_id" in filtered_data.columns else 0
    )
    st.metric("Total Orders", f"{total_orders:,}")

with col2:
    total_customers = (
        filtered_data["customer_unique_id"].nunique()
        if "customer_unique_id" in filtered_data.columns else 0
    )
    st.metric("Total Customers", f"{total_customers:,}")

with col3:
    total_revenue = (
        filtered_data["total_sales"].sum()
        if "total_sales" in filtered_data.columns else 0
    )
    st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")

st.divider()

# Tren penjualan bulanan
st.subheader("Tren Penjualan Bulanan")

if {"month", "total_sales"}.issubset(monthly_sales.columns):
    fig = px.line(
        monthly_sales,
        x="month",
        y="total_sales",
        markers=True,
        title="Monthly Revenue"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Kolom month atau total_sales tidak ditemukan.")

st.divider()

# Segmentasi pelanggan
st.subheader("Segmentasi Pelanggan (RFM)")

if {"segment", "customer_count"}.issubset(segment_data.columns):
    fig = px.bar(
        segment_data,
        x="segment",
        y="customer_count",
        color="segment",
        title="Jumlah Pelanggan per Segmen"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Kolom segment atau customer_count tidak ditemukan.")

st.divider()

# Penjualan berdasarkan kategori
st.subheader("Penjualan Berdasarkan Kategori Produk")

if {"product_category_name_english", "total_sales"}.issubset(category_sales.columns):
    fig = px.bar(
        category_sales.sort_values("total_sales", ascending=False).head(10),
        x="total_sales",
        y="product_category_name_english",
        orientation="h",
        title="Top 10 Product Categories"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Kolom kategori atau total_sales tidak ditemukan.")
