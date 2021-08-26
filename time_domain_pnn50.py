import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import scipy.stats as stats
from hrv import HRV
from ecg_gudb_database import GUDb
import sys

maths_true = []
sitting_true = []

total_subjects = 25
subject = []

do_normalise = True

# calculate all subjects' pNN50 and store in list
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
        maths_true.append(hrv_class.pNN50(
            maths_true_rr))

        sitting_true_rr = sitting_class.anno_cs
        sitting_true.append(hrv_class.pNN50(
            sitting_true_rr))


subject = np.array(subject)
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(subject+(0*width), sitting_true, width)
rects2 = ax.bar(subject+(1*width), maths_true, width)

ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
ax.set_ylabel('pNN50')
ax.set_xlabel('Subject #')
ax.set_title('pNN50 Results for sitting and maths test')
ax.set_xticks(subject + width)
ax.set_xticklabels(subject)
ax.legend((rects1[0], rects2[0]), ('sitting', 'math'))

# calculate all subjects' avg and std
avg_maths_true = np.average(maths_true)
sd_maths_true = np.std(maths_true)

avg_sitting_true = np.average(sitting_true)
sd_sitting_true = np.std(sitting_true)

print(avg_sitting_true)
print(sd_sitting_true)
print(avg_maths_true)
print(sd_maths_true)

fig = plt.figure()

plt.bar(['sitting', 'math'],
        [avg_sitting_true, avg_maths_true],
        yerr=[sd_sitting_true, sd_maths_true],
        align='center', alpha=0.5, ecolor='black', capsize=10)
plt.title("Average and stardard value of pNN50 Results, Math vs sitting")
plt.ylabel('pNN50')

# calculate p value
t, p = stats.ttest_rel(maths_true, sitting_true)
print("Math vs sitting: p=", p)


plt.show()
