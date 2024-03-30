import matplotlib.pyplot as plt
import numpy as np

sectors = ['Логістика', 'Маркетинг', 'Дослідження та розробка', 'Управління', 'Бухгалтерія']
percentages = [45.0, 20.0, 15.0, 10.0, 10.0]

plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(percentages, labels=sectors, autopct='%1.1f%%', startangle=140, colors=['#0a7d33']*5)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

plt.title('Розподіл фондів за сферами діяльності', fontsize=14)

plt.tight_layout()
plt.show()