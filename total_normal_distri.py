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

total_subjects = 25
subject = []

for i in range(total_subjects):
    print(i)
    sitting_class = GUDb(i, 'sitting')
    sitting_class.filter_data()
    maths_class = GUDb(i, 'maths')
    maths_class.filter_data()

    if sitting_class.anno_cs_exists and maths_class.anno_cs_exists:
        subject.append(i)

        hrv_class = HRV(sitting_class.fs)

        maths_true_rr = maths_class.anno_cs
        hr_array = hrv_class.HR(maths_true_rr)
        hr_avg = mean(hr_array)
        maths_true.append(hr_avg)

        # sitting_true_rr = sitting_class.anno_cs
        # hr_array = hrv_class.HR(sitting_true_rr)
        # hr_avg = mean(hr_array)
        # sitting_true.append(hr_avg)

print(maths_true)
print(stats.shapiro(maths_true))

# pd_sitting = pd.DataFrame(sitting_true, columns=["Real-time HR"])
pd_math = pd.DataFrame(maths_true, columns=["Real-time HR"])

# fig = plt.figure(figsize=(10, 6))
# ax1 = fig.add_subplot(2, 1, 1)  # subplot 1
# ax1.scatter(pd_sitting.index, pd_sitting.values)
# plt.grid()

# ax2 = fig.add_subplot(2, 1, 2)  # subplot 2
# pd_sitting.hist(bins=30, alpha=0.5, ax=ax2,)
# pd_sitting.plot(kind='kde', secondary_y=True, ax=ax2)
# plt.grid()
# plt.show()

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(2, 1, 1)  # subplot 1
ax1.scatter(pd_math.index, pd_math.values)
plt.grid()

ax2 = fig.add_subplot(2, 1, 2)  # subplot 2
pd_math.hist(bins=30, alpha=0.5, ax=ax2,)
pd_math.plot(kind='kde', secondary_y=True, ax=ax2)
plt.grid()
plt.show()