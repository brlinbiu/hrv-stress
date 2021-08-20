#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pathlib
from hrv import HRV
from ecgdetectors import Detectors
import scipy.stats as stats
import sys
from ecg_gudb_database import GUDb


# for plotting max hflf ratio
hflfmax = 10

maths_true_hf = []
sitting_true_hf = []

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
        maths_true_hf.append(hrv_class.fAnalysis(maths_true_rr))

        sitting_true_rr = sitting_class.anno_cs
        sitting_true_hf.append(hrv_class.fAnalysis(sitting_true_rr))

subject = np.array(subject)
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.bar(subject+(0*width), sitting_true_hf, width)
rects2 = ax.bar(subject+(1*width), maths_true_hf, width)

ax.set_ylabel('LF/HF ratio')
ax.set_xlabel('Subject #')
ax.set_title('LF/HF ratio sitting vs maths test')
ax.set_xticks(subject + width)
ax.set_xticklabels(subject)
ax.legend((rects1[0], rects2[0]), ('sitting', 'math'))

plt.figure()

avg_sitting_true_hf = np.average(sitting_true_hf)
sd_sitting_true_hf = np.std(sitting_true_hf)

avg_maths_true_hf = np.average(maths_true_hf)
sd_maths_true_hf = np.std(maths_true_hf)


print(avg_sitting_true_hf)
print(sd_sitting_true_hf)
print(avg_maths_true_hf)
print(sd_maths_true_hf)

plt.bar(['sitting', 'math'], [avg_sitting_true_hf, avg_maths_true_hf], yerr=[
        sd_sitting_true_hf, sd_maths_true_hf], align='center', alpha=0.5, ecolor='black', capsize=10)
plt.ylim([0, hflfmax])
ax.set_ylabel('LF/HF ratio')
plt.title("Sitting vs math")

t, p = stats.ttest_ind(sitting_true_hf, maths_true_hf, equal_var=False)
print("T-test between sitting and math test: p=", p)


plt.show()