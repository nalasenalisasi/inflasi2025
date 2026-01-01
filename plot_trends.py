import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Load data
file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter for Commodities (Flag=3)
df_com = df[df['Flag'] == 3].copy()
df_com['Nama Komoditas'] = df_com['Nama Komoditas'].str.upper()

# Target commodities mapping (User Input -> Dataset Name)
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

# Filter dataset
selected_commodities = list(target_map.values())
filtered_df = df_com[df_com['Nama Komoditas'].isin(selected_commodities)]

# Setup Plot
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(14, 8))

# Create color map
colors = cm.tab20(np.linspace(0, 1, len(selected_commodities)))

# Plot each commodity
for (name, group), color in zip(filtered_df.groupby('Nama Komoditas'), colors):
    # Sort by month
    group = group.sort_values('Bulan')
    
    # Get user-friendly name if possible (reverse lookup or just use display name)
    display_name = name
    for k, v in target_map.items():
        if v == name:
            display_name = k
            break
            
    plt.plot(group['Bulan'], group['Andil MtM'], marker='o', label=display_name, linewidth=2, markersize=6, color=color)

# Customize
plt.title('Tren Andil Inflasi MtM Komoditas Pangan Strategis & Emas (2025)', fontsize=16, pad=20)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Andil Inflasi MtM (%)', fontsize=12)
plt.xticks(range(1, 13))
plt.grid(True, linestyle='--', alpha=0.5)

# Legend outside
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, title='Komoditas')

plt.tight_layout()

# Save
output_file = 'tren_andil_mtm_komoditas.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Grafik berhasil disimpan: {output_file}")
