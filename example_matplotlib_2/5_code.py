from matplotlib import pyplot as plt
import pandas as pd

# Load PET data from a TSV file
tsv_file = '4_data/PET.tsv'
data = pd.read_csv(tsv_file, delimiter='\t')
x = data["Strain"]
y = data["Stress(MPA)"]
# plot with dot line style
plt.plot(x, y, label="PET", linestyle='dotted', color="black")

# Load PET after washing data from a TSV file
tsv_file = '4_data/PET after washing.tsv'
data = pd.read_csv(tsv_file, delimiter='\t')
x = data["Strain"]
y = data["Stress(MPA)"]
plt.plot(x, y, label="PET after washing", color="red")

# add legend
plt.legend()

# Add labels and title
plt.xlabel('Strain (%)')
plt.ylabel('Stress (MPA)')
plt.title('Stress-strain curve of PET and PET after washing')

plt.show()
