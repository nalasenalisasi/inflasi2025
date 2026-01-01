import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Grafik Bulanan Inflasi 2025", layout="centered")

@st.cache_data
def load_data_from_candidates():
    base = Path(__file__).parent
    candidates = [
        base / "inflasi 2025.xlsx",
        base / "inflasi2025.xlsx",
        base.parent / "inflasi 2025.xlsx",
        base.parent / "inflasi2025.xlsx",
    ]
    for p in candidates:
        if p.exists():
            return pd.read_excel(str(p), engine="openpyxl")
    raise FileNotFoundError("Excel file not found in expected locations")

month_map = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}

uploaded = st.sidebar.file_uploader("Upload Excel", type=["xlsx"])
if uploaded:
    df = pd.read_excel(uploaded, engine="openpyxl")
else:
    try:
        df = load_data_from_candidates()
    except FileNotFoundError:
        st.error("File 'inflasi 2025.xlsx' tidak ditemukan. Upload file melalui sidebar atau letakkan di root atau folder src.")
        st.stop()

st.title("Grafik Bulanan Inflasi 2025")

dataset_choice = st.sidebar.selectbox("Pilih Dataset", ["Headline", "Komoditas"])

if dataset_choice == "Headline":
    d = df[df["Flag"] == 0].copy().sort_values("Bulan")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(d["Bulan"], d["Inflasi MtM"], marker="o", linestyle="-", color="#1f77b4", linewidth=2)
    for x, y in zip(d["Bulan"], d["Inflasi MtM"]):
        ax.annotate(f"{y:.2f}%", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9, fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.8))
    ax.set_title("Inflasi MtM Tahun 2025")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Inflasi MtM (%)")
    ax.set_xticks(d["Bulan"].tolist())
    ax.grid(True, linestyle="--", alpha=0.7)
    st.pyplot(fig)
else:
    dkom = df[df["Flag"] == 3].copy()
    commodities = sorted(dkom["Nama Komoditas"].dropna().unique().tolist())
    query = st.sidebar.text_input("Cari Komoditas", "")
    filtered = [c for c in commodities if query.lower() in c.lower()] or commodities
    selected_commodity = st.sidebar.selectbox("Pilih Komoditas", filtered)
    metric_choice = st.sidebar.selectbox("Jenis Nilai", ["Inflasi MtM", "Andil MtM"])
    d = dkom[dkom["Nama Komoditas"] == selected_commodity].sort_values("Bulan")
    fig, ax = plt.subplots(figsize=(10, 6))
    color = "#d62728" if metric_choice == "Inflasi MtM" else "#2ca02c"
    ax.plot(d["Bulan"], d[metric_choice], marker="o", linestyle="-", color=color, linewidth=2)
    for x, y in zip(d["Bulan"], d[metric_choice]):
        ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#dddddd", alpha=0.8))
    ax.set_title(f"Tren {metric_choice} - {selected_commodity} (2025)")
    ax.set_xlabel("Bulan")
    ax.set_ylabel(f"{metric_choice} (%)")
    ax.set_xticks(sorted(d["Bulan"].unique().tolist()))
    ax.grid(True, linestyle="--", alpha=0.7)
    st.pyplot(fig)

