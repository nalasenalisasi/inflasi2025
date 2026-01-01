import pandas as pd
import matplotlib.pyplot as plt

# Set style for better visuals
plt.style.use('seaborn-v0_8-whitegrid')

file_path = 'inflasi 2025.xlsx'
try:
    df = pd.read_excel(file_path)

    # Filter flag=0
    filtered_df = df[df['Flag'] == 0].copy()

    # Sort by Month (Bulan) just in case
    filtered_df = filtered_df.sort_values('Bulan')

    # Data for plotting
    months = filtered_df['Bulan']
    inflation_mtm = filtered_df['Inflasi MtM']

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(months, inflation_mtm, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='Inflasi MtM')

    # Add labels with background to avoid overlapping the line
    for x, y in zip(months, inflation_mtm):
        plt.annotate(
            f'{y:.2f}%', 
            (x, y), 
            textcoords="offset points", 
            xytext=(0, 10), 
            ha='center',
            fontsize=9,
            fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.8)
        )

    # Customize the chart
    plt.title('Inflasi MtM Tahun 2025', fontsize=14, pad=20)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Inflasi MtM (%)', fontsize=12)
    plt.xticks(months)  # Ensure all months are shown
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    output_file = 'inflasi_mtm_2025.png'
    plt.savefig(output_file, dpi=300)
    print(f"Grafik berhasil disimpan sebagai {output_file}")
    
    # Show plot (optional, might not work in all envs but good to have)
    # plt.show()

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
