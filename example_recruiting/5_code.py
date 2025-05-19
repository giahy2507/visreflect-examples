import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv("tips.csv")

avg_total_bill = tips["total_bill"].mean()
avg_tip = tips["tip"].mean()
sns.relplot(data=tips, x="total_bill", y="tip")
plt.axhline(avg_tip, color='red', linestyle='--', label='avg tip')
plt.axvline(avg_total_bill, color='blue', linestyle='--', label='avg total_bill')

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()
plt.savefig("2_visualisation_image.png", dpi=300)
plt.show()
