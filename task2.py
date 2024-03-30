import matplotlib.pyplot as plt
import numpy as np

average_salary = 12794.35
std_dev = average_salary / 3
num_employees = 1000

np.random.seed(0)
salaries = np.random.normal(loc=average_salary, scale=std_dev, size=num_employees)

plt.figure(figsize=(10, 6))
plt.hist(salaries, bins=30, color='skyblue', edgecolor='black')

plt.axvline(average_salary, color='red', linestyle='dashed', linewidth=2)
plt.text(average_salary+200, 5, f'Середня: {average_salary} грн', color='red')

plt.title('Розподіл Зарплат Співробітників')
plt.xlabel('Зарплата (гривні)')
plt.ylabel('Кількість Співробітників')

plt.tight_layout()
plt.show()
