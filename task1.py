import matplotlib.pyplot as plt
import numpy as np

provided_data_values = [9850, 9780, 9580, 9310, 9100, 8850, 8620, 8300, 8420]

interpolated_years = np.linspace(2024, 2032, len(provided_data_values))

plt.figure(figsize=(10, 5))
plt.plot(interpolated_years, provided_data_values, '-o', color='red')

plt.title("Кількість навчальних закладів", fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Кількість', fontsize=12)

plt.xticks(years)

plt.xlim(2023, 2033)
plt.ylim(8200, 10000)

plt.grid(True)

plt.show()