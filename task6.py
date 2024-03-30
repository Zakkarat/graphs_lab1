import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
years_of_experience = np.random.rand(50) * 30
bonus_size = np.random.rand(50) * 4000 + 1000

plt.figure(figsize=(10, 6))
plt.scatter(years_of_experience, bonus_size, color='blue')
plt.title('Залежність розміру надбавки від трудового стажу')
plt.xlabel('Трудовий стаж (роки)')
plt.ylabel('Розмір надбавки')

plt.tight_layout()
plt.show()