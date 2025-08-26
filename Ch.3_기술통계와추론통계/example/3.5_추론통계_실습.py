import random
import matplotlib.pyplot as plt

sample_size = 31
sample_count = 1000

x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / sample_size) for _ in range(sample_count)]

# 히스토그램 그리기
plt.hist(x_values, bins=30, edgecolor='black')
plt.title('Central Limit Theorem Simulation')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()