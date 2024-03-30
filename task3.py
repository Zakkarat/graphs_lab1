import matplotlib.pyplot as plt
import numpy as np

prices = [28, 26, 27, 29, 26]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(grades, prices, color='salmon')
ax1.set_xlabel('Gasoline Grade')
ax1.set_ylabel('Price per Liter (UAH)', color='black')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.plot(grades, quality_ratings, color='blue', marker='o', linestyle='-')
ax2.set_ylabel('Quality Rating (out of 10)', color='blue')
ax2.tick_params(axis='y', colors='blue')

plt.title('Comparison of Gasoline Prices and Quality Ratings')

plt.tight_layout()
plt.show()
