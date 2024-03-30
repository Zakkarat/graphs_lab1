import matplotlib.pyplot as plt
import numpy as np

dates = ['2023-03', '2023-05', '2023-07', '2023-09', '2023-11', '2024-01']
profitability = [102, 100, 90, 80, 70, 55]

plt.figure(figsize=(10, 6))
plt.plot(dates, profitability, marker='o', color='blue', linestyle='-')

plt.title('Прибутковість акцій компанії протягом 2023 року', fontsize=14)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Прибутковість', fontsize=12)

plt.grid(True)
plt.tight_layout()
plt.show()