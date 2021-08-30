from ecg_gudb_database import GUDb
from hrv import HRV
import matplotlib.pyplot as plt


#get subject data
sitting_class = GUDb(0, 'sitting')
math_class = GUDb(0, 'maths')

rr_sitting_example = sitting_class.anno_cs
hrv_class = HRV(sitting_class.fs)
hr_sitting_array = hrv_class.HR(rr_sitting_example)

#rr_example
print(rr_sitting_example)

#hr_plot
fig = plt.figure()
ax = plt.subplot(211)
ax.set_title("Subject #0's HR, Sitting")
plt.plot(hr_sitting_array, 'b')
plt.ylabel("heartrate/Hz")


rr_math_example =  math_class.anno_cs
hr_math_array = hrv_class.HR(rr_math_example)
ax = plt.subplot(212)
ax.set_title("Subject #0's HR, Doing math")
plt.plot(hr_math_array, 'r')
plt.xlabel("t/seconds")
plt.ylabel("heartrate/Hz")
plt.show()