import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
salaries = np.random.normal(loc=50000, scale=15000, size=100)
incomes = salaries + np.random.normal(loc=20000, scale=5000, size=salaries.shape)

plt.figure(figsize=(10, 6))
plt.scatter(salaries, incomes, alpha=0.6)

plt.title('Зв\'язок між доходами та зарплатою', fontsize=14)
plt.xlabel('Зарплата', fontsize=12)
plt.ylabel('Дохід', fontsize=12)

plt.xlim(10000, 80000)
plt.ylim(30000, 110000)

plt.grid(True)
plt.tight_layout()
plt.show()