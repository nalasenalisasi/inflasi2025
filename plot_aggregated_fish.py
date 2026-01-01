import pandas as pd
import matplotlib.pyplot as plt
import math

# Load data
file_path = 'inflasi 2025.xlsx'
df = pd.read_excel(file_path)

# Filter for Commodities (Flag=3)
df_com = df[df['Flag'] == 3].copy()
df_com['Nama Komoditas'] = df_com['Nama Komoditas'].str.upper()

# Filter for commodities starting with "IKAN"
fish_df = df_com[df_com['Nama Komoditas'].str.startswith('IKAN')]

# Get list of unique fish names
fish_names = sorted(fish_df['Nama Komoditas'].unique())
fish_names = [name.title() for name in fish_names] # Title case for better look

# Aggregate Andil MtM by Month
monthly_andil = fish_df.groupby('Bulan')['Andil MtM'].sum().reset_index()

# Plot
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(12, 10)) # Increased height for the list

# Adjust layout to make room for text at bottom
plt.subplots_adjust(bottom=0.35)

# Plot line
plt.plot(monthly_andil['Bulan'], monthly_andil['Andil MtM'], 
         marker='o', linestyle='-', linewidth=2.5, color='#1f77b4', label='Total Andil Ikan')

# Add labels (2 decimal places)
for x, y in zip(monthly_andil['Bulan'], monthly_andil['Andil MtM']):
    plt.annotate(
        f"{y:.2f}", 
        (x, y), 
        textcoords="offset points", 
        xytext=(0, 10), 
        ha='center',
        fontsize=10,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#dddddd", alpha=0.8)
    )

plt.title('Tren Total Andil Inflasi MtM Kelompok Ikan (2025)', fontsize=16, pad=20)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Total Andil Inflasi MtM (%)', fontsize=12)
plt.xticks(range(1, 13))
plt.grid(True, linestyle='--', alpha=0.7)

# Create formatted list text (3 columns)
num_columns = 3
num_items = len(fish_names)
rows = math.ceil(num_items / num_columns)

list_text = "Komoditas yang digabungkan:\n"
column_width = 35 # Characters

# Construct the string row by row
formatted_lines = []
for r in range(rows):
    line_parts = []
    for c in range(num_columns):
        idx = r + c * rows
        if idx < num_items:
            item = f"- {fish_names[idx]}"
            line_parts.append(f"{item:<{column_width}}")
    formatted_lines.append("".join(line_parts))

final_text = list_text + "\n".join(formatted_lines)

# Add text box at the bottom
plt.figtext(0.5, 0.02, final_text, ha="center", fontsize=9, family='monospace',
            bbox={"facecolor":"#f0f0f0", "alpha":0.5, "pad":10}, va="bottom")

# Save
output_file = 'tren_andil_mtm_kelompok_ikan.png'
plt.savefig(output_file, dpi=300)
print(f"Grafik berhasil disimpan: {output_file}")
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(12, 10))
plt.subplots_adjust(bottom=0.35)
elec_df = df_com[df_com['Nama Komoditas'].str.startswith('TARIF LISTRIK')]
elec_names = sorted(elec_df['Nama Komoditas'].unique())
elec_names = [name.title() for name in elec_names]
monthly_elec = elec_df.groupby('Bulan')['Andil MtM'].sum().reset_index()
plt.plot(monthly_elec['Bulan'], monthly_elec['Andil MtM'], marker='o', linestyle='-', linewidth=2.5, color='#ff7f0e', label='Tarif Listrik')
for x, y in zip(monthly_elec['Bulan'], monthly_elec['Andil MtM']):
    plt.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#dddddd", alpha=0.8))
plt.title('Tren Andil Inflasi MtM Tarif Listrik (2025)', fontsize=16, pad=20)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Total Andil Inflasi MtM (%)', fontsize=12)
plt.xticks(range(1, 13))
plt.grid(True, linestyle='--', alpha=0.7)
num_columns = 3
num_items = len(elec_names)
rows = math.ceil(num_items / num_columns)
list_text = "Komoditas yang digabungkan:\n"
column_width = 35
formatted_lines = []
for r in range(rows):
    line_parts = []
    for c in range(num_columns):
        idx = r + c * rows
        if idx < num_items:
            item = f"- {elec_names[idx]}"
            line_parts.append(f"{item:<{column_width}}")
    formatted_lines.append("".join(line_parts))
final_text = list_text + "\n".join(formatted_lines)
plt.figtext(0.5, 0.02, final_text, ha="center", fontsize=9, family='monospace', bbox={"facecolor":"#f0f0f0", "alpha":0.5, "pad":10}, va="bottom")
output_file = 'tren_andil_mtm_tarif_listrik.png'
plt.savefig(output_file, dpi=300)
print(f"Grafik berhasil disimpan: {output_file}")
