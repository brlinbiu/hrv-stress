import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean
import scipy.stats as stats
from hrv import HRV
from ecg_gudb_database import GUDb
import sys

maths_true = []
sitting_true = []

sitting_class = GUDb(12, 'sitting')
sitting_class.filter_data()
maths_class = GUDb(12, 'maths')
maths_class.filter_data()

if sitting_class.anno_cs_exists and maths_class.anno_cs_exists:
    hrv_class = HRV(sitting_class.fs)

    sitting_true_rr = sitting_class.anno_cs
    hr_array = hrv_class.HR(sitting_true_rr)

pd_math = pd.DataFrame(hr_array, columns=["Real-time HR"])
print(pd_math)
print(stats.shapiro(hr_array))


fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(2, 1, 1)  # subplot 1
ax1.scatter(pd_math.index, pd_math.values)
plt.xlabel("Sampling time")
plt.ylabel("Heart Rate")
plt.title("Scatter plot of real-time heart rate for the Sitting group of Subject #12")
plt.grid()

ax2 = fig.add_subplot(2, 1, 2)  # subplot 2
pd_math.hist(bins=30, alpha=0.5, ax=ax2,)
pd_math.plot(kind='kde', secondary_y=True, ax=ax2)
plt.xlabel("Heart Rate")
plt.ylabel("Count")
plt.title("Histogram plot of real-time heart rate for the Sitting group of Subject #12")
plt.grid()
plt.show()