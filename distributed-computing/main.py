import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Зчитування даних
df = pd.read_csv('results.csv')

# Побудова зведеної таблиці: строки — OMP потоки, стовпці — MPI процеси
pivot = df.pivot(index='OpenMP Threads', columns='MPI Procs', values='Time (sec)')

# Стиль оформлення
sns.set_theme(style="whitegrid")

# Побудова графіку
plt.figure(figsize=(9, 6))
ax = sns.heatmap(
    pivot,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'label': 'Execution Time (sec)'}
)

# Підписи та оформлення
plt.title("Execution Time Heatmap", fontsize=14, fontweight='bold')
plt.xlabel("MPI Processes", fontsize=12)
plt.ylabel("OpenMP Threads", fontsize=12)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()

plt.show()
