import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv("4_plotting_data.csv")

avg_total_bill = tips["total_bill"].mean()
avg_tip = tips["tip"].mean()

plt.scatter(tips["total_bill"], tips["tip"])
plt.axhline(avg_tip, color='red', linestyle='--', label='avg tip')
plt.axvline(avg_total_bill, color='blue', linestyle='--', label='avg total_bill')

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()
plt.savefig("2_visualisation_image.png", dpi=300)
plt.show()
