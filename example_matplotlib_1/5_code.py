import matplotlib.pyplot as plt

# Data
weeks = ['0-4 weeks', '5-8 weeks', '9-12 weeks', '13-16 weeks', '17-20 weeks', '21-26 weeks']
n_values = [194, 65, 44, 31, 24, 7]

# Plot
fig, ax = plt.subplots()
bars = ax.bar(weeks, n_values)

# Add text annotations
for bar, n in zip(bars, n_values):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{n}', ha='center', va='bottom')

# rotate x labels 20 degrees
plt.xticks(rotation=20)

# Labels and title
ax.set_xlabel('Weeks')
ax.set_ylabel('Number of episodes mastitis / women\n breastfeeding - weeks * 1000')

# Show plot on the screen
plt.show()
