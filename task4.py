import matplotlib.pyplot as plt
import numpy as np

turnover_rates = [5.2, 4.8, 5.0, 5.1, 4.9, 5.3]

plt.figure(figsize=(10, 6))
plt.bar(departments, turnover_rates, color='lightblue')

plt.title('Turnover Rates in September Across Six Departments')
plt.xlabel('Department')
plt.ylabel('Turnover Rate (%)')

plt.ylim(4.5, 5.6)

plt.tight_layout()
plt.show()