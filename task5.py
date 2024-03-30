import matplotlib.pyplot as plt
import numpy as np

activities = ['Breaks', 'Cleaning', 'Inventory Management', 'With Clients', 'Other Tasks']
time_allocation = [20.0, 20.0, 30.0, 15.0, 15.0]  # Percentages

colors = ['gold', 'lightcoral', 'lightgreen', 'lightblue', 'violet']

plt.figure(figsize=(8, 6))
plt.pie(time_allocation, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Time Allocation of a Store Seller During Workday')

plt.tight_layout()
plt.show()