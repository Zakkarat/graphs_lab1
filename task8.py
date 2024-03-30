import matplotlib.pyplot as plt
import numpy as np

regions = ['Північний', 'Південний', 'Східний', 'Західний', 'Центральний']
population_growth_rates = [12.5, 14.8, 13.2, 15.4, 11.7]
colors = ['blue', 'green', 'orange', 'red', 'black']

plt.figure(figsize=(10, 6))
bars = plt.bar(regions, population_growth_rates, color=colors)

plt.title('Народжуваність за регіонами', fontsize=14)
plt.xlabel('Регіон', fontsize=12)
plt.ylabel('Народжуваність на 1 000 населення', fontsize=12)

for bar, color in zip(bars, colors):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom', color=color, weight='bold')

plt.tight_layout()
plt.show()