import matplotlib.pyplot as plt
import numpy as np

new_percentages = [15, 20, 30, 20, 10, 5]

plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups, new_percentages, color='skyblue')

plt.title('Плинність кадрів за віковими групами', fontsize=14)
plt.xlabel('Вікова група', fontsize=12)
plt.ylabel('Плинність кадрів (%)', fontsize=12)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1), ha='center', va='bottom')

plt.tight_layout()
plt.show()