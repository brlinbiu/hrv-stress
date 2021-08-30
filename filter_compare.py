import numpy as np
import matplotlib.pyplot as plt
from hrv import HRV
from ecgdetectors import Detectors
from scipy.fftpack import fft, ifft
import scipy.stats as stats
import sys
from ecg_gudb_database import GUDb
# choose one of subjects
sitting_class = GUDb(1, 'sitting')

# spectrum before fft filtering
xf = sitting_class.t
xf_n = xf[range(int(len(xf)/2))]
# spectrum after fft filtering
yf = abs(fft(sitting_class.cs_V2_V1))/len(xf)
yf_n = yf[range(int(len(xf)/2))]


# plot
fig = plt.figure()
ax = plt.subplot(211)
ax.set_title("Subject 1's power after fft trans before filtering")
plt.ylabel("power")
plt.plot(xf_n, yf_n, 'r')
plt.ylim(0, 0.0002)


sitting_class.filter_data()
yf = abs(fft(sitting_class.cs_V2_V1_filt))/len(xf)
yf_n = yf[range(int(len(xf)/2))]
ax = plt.subplot(212)
ax.set_title("Subject 1's power after fft trans after filtering")
plt.xlabel("Sampling point")
plt.ylabel("power")
plt.plot(xf_n, yf_n, 'b')
plt.ylim(0, 0.0002)
plt.show()