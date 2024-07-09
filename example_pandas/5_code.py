from matplotlib import pyplot as plt
import pandas as pd

# Load PET data from a TSV file
tsv_file = '4_data/PET.tsv'
data = pd.read_csv(tsv_file, delimiter='\t')
data.plot(x="Strain", y="Stress(MPA)", label="PET", linestyle='dotted', color="black")

# Load PET after washing data from a TSV file
tsv_file = '4_data/PET after washing.tsv'
data2 = pd.read_csv(tsv_file, delimiter='\t')
data2.plot(x="Strain", y="Stress(MPA)", label="PET after washing", color="red")

# add legend
plt.legend()

# Add labels and title
plt.xlabel('Strain (%)')
plt.ylabel('Stress (MPA)')
plt.title('Stress-strain curve of PET and PET after washing')

plt.show()
