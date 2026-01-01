import pandas as pd

file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter commodities
commodities = df[df['Flag'] == 3]['Nama Komoditas'].unique()
commodities = [str(c).upper() for c in commodities]

targets = [
    "BERAS", "DAGING AYAM RAS", "IKAN BANDENG", "IKAN KEMBUNG", 
    "TELUR AYAM RAS", "MINYAK GORENG", "TOMAT", "CABAI MERAH", 
    "CABAI RAWIT", "BAWANG MERAH", "BAWANG PUTIH", "TAHU", 
    "TEMPE", "GULA PASIR", "EMAS PERHIASAN"
]

print("Matching Commodities found:")
for target in targets:
    matches = [c for c in commodities if target in c]
    print(f"{target} -> {matches}")
