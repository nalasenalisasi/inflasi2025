import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Output directory
output_dir = 'grafik_komoditas'
os.makedirs(output_dir, exist_ok=True)

# Load data
file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter for Commodities (Flag=3)
df_com = df[df['Flag'] == 3].copy()
df_com['Nama Komoditas'] = df_com['Nama Komoditas'].str.upper()

# Target commodities mapping
target_map = {
    "BERAS": "BERAS",
    "DAGING AYAM RAS": "DAGING AYAM RAS",
    "IKAN BANDENG": "IKAN BANDENG/IKAN BOLU",
    "IKAN KEMBUNG": "IKAN KEMBUNG/IKAN GEMBUNG/ IKAN BANYAR/IKAN GEMBOLO/ IKAN ASO-ASO",
    "TELUR AYAM RAS": "TELUR AYAM RAS",
    "MINYAK GORENG": "MINYAK GORENG",
    "TOMAT": "TOMAT",
    "CABAI MERAH": "CABAI MERAH",
    "CABAI RAWIT": "CABAI RAWIT",
    "BAWANG MERAH": "BAWANG MERAH",
    "BAWANG PUTIH": "BAWANG PUTIH",
    "TAHU MENTAH": "TAHU MENTAH",
    "TEMPE": "TEMPE",
    "GULA PASIR": "GULA PASIR",
    "EMAS PERHIASAN": "EMAS PERHIASAN"
}

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

for display_name, db_name in target_map.items():
    # Filter data for specific commodity
    data = df_com[df_com['Nama Komoditas'] == db_name].sort_values('Bulan')
    
    if data.empty:
        print(f"Warning: No data found for {display_name}")
        continue

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data['Bulan'], data['Andil MtM'], marker='o', linestyle='-', linewidth=2, color='#1f77b4')
    
    # Add value labels
    for x, y in zip(data['Bulan'], data['Andil MtM']):
        label = f"{y:.2f}"
        plt.annotate(
            label,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#dddddd", alpha=0.8)
        )

    plt.title(f'Tren Andil Inflasi MtM - {display_name} (2025)', fontsize=14, pad=15)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Andil Inflasi MtM (%)', fontsize=12)
    plt.xticks(range(1, 13))
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Sanitize filename
    safe_name = re.sub(r'[^\w\s-]', '', display_name).strip().lower().replace(' ', '_')
    output_file = os.path.join(output_dir, f'{safe_name}.png')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()
    
    print(f"Grafik disimpan: {output_file}")

print("\nSelesai membuat semua grafik individu.")
