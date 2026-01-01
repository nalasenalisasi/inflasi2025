import pandas as pd

file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

print("Unique Flags:", df['Flag'].unique())

# Check sample rows for each flag
for flag in df['Flag'].unique():
    print(f"\n--- Flag {flag} Sample ---")
    print(df[df['Flag'] == flag][['Nama Komoditas', 'Inflasi MtM', 'Andil MtM']].head())
