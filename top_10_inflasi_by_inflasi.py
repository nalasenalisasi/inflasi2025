import pandas as pd

file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter for Commodities (Flag=3)
commodities_df = df[df['Flag'] == 3].copy()

# List to store top 10 for each month
all_top_10 = []

months = sorted(commodities_df['Bulan'].unique())

for month in months:
    # Filter by month
    month_df = commodities_df[commodities_df['Bulan'] == month]
    
    # Sort by Inflasi MtM descending
    top_10 = month_df.sort_values(by='Inflasi MtM', ascending=False).head(10)
    
    # Add Rank column
    top_10 = top_10.copy()
    top_10['Rank'] = range(1, 11)
    
    # Select relevant columns
    cols = ['Bulan', 'Rank', 'Nama Komoditas', 'Inflasi MtM', 'Andil MtM']
    top_10_filtered = top_10[cols]
    
    all_top_10.append(top_10_filtered)

# Combine all months
final_df = pd.concat(all_top_10, ignore_index=True)

# Save to Excel
output_file = 'top_10_komoditas_by_inflasi_mtm_2025.xlsx'
final_df.to_excel(output_file, index=False)

print(f"File berhasil disimpan: {output_file}")
print("\nPreview Data (Bulan 1):")
print(final_df[final_df['Bulan'] == 1])
