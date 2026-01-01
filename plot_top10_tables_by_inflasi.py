import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

# Create output directory
output_dir = 'tabel_top10_inflasi_images'
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Load data
file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter for Commodities (Flag=3)
commodities_df = df[df['Flag'] == 3].copy()

# Month name mapping
month_map = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
    5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
    9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}

months = sorted(commodities_df['Bulan'].unique())

for month in months:
    # Filter and sort by Inflasi MtM
    month_df = commodities_df[commodities_df['Bulan'] == month]
    top_10 = month_df.sort_values(by='Inflasi MtM', ascending=False).head(10)
    
    # Prepare data for table
    table_data = []
    for i, (_, row) in enumerate(top_10.iterrows(), 1):
        table_data.append([
            str(i),
            row['Nama Komoditas'],
            f"{row['Inflasi MtM']:.2f}",
            f"{row['Andil MtM']:.2f}"
        ])

    columns = ['Rank', 'Komoditas', 'Inflasi MtM (%)', 'Andil MtM (%)']

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Add title
    month_name = month_map.get(month, str(month))
    plt.title(f'10 Komoditas dengan Inflasi MtM Tertinggi\nBulan {month_name} 2025', 
              fontsize=16, pad=20, fontweight='bold', color='#333333')

    # Create table
    table = ax.table(cellText=table_data, colLabels=columns, loc='center', cellLoc='center')
    
    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8) # Stretch height

    # Color styling
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#a83232') # Reddish for Inflation focus
            cell.set_text_props(color='white', weight='bold')
        elif row % 2 == 0:
            cell.set_facecolor('#f2f2f2')
        
        cell.set_edgecolor('#dddddd')
        cell.set_linewidth(1)
        
        # Align 'Komoditas' column to left
        if col == 1 and row != 0:
            cell.set_text_props(ha='left')
            cell.set_width(0.4)
        else:
            cell.set_width(0.15)
            if col == 1: cell.set_width(0.4)

    # Save
    output_file = os.path.join(output_dir, f'top10_by_inflasi_{month}_{month_name}.png')
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {output_file}")

print("Selesai membuat semua gambar tabel (basis Inflasi MtM).")
