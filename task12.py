import matplotlib.pyplot as plt
import numpy as np

students = ['Студент 3', 'Студент 7', 'Студент 4', 'Студент 8', 'Студент 1',
            'Студент 2', 'Студент 5', 'Студент 6']
performance = [45, 50, 55, 60, 65, 70, 85, 90]

colors = ['skyblue'] * 6 + ['orange'] * 2

plt.figure(figsize=(10, 6))
bars = plt.barh(students, performance, color=colors)

plt.title('Успішність студентів у серпні', fontsize=14)

plt.annotate('Обігнали інших',
             xy=(performance[-1], students[-1]),
             xytext=(performance[-1]+5, students[-1]),
             arrowprops=dict(facecolor='black', shrink=0.05),
             ha='center', va='center')

plt.xlabel('Успішність', fontsize=12)
plt.tight_layout()
plt.show()