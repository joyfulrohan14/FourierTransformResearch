#Read Fourier Data from text file

#2820 Hz - starting point multiplied by 2*pi
#imports
import matplotlib.pyplot as plt  # the graphing library con: limited UI components
import numpy as np  # libary to operate arrays
import math
from matplotlib.widgets import Slider, Button, TextBox

#code starts
fileName = input("Please enter file name with data (format point number, number): ")
acquTime = input("Enter the time (s) that it took to acquire your data: ")
fid = []
with open(fileName, "r") as fp:
    line = fp.readline()
    while line:
        x = line.split(", ")
        fid.append(x[1])
        line = fp.readline()
        line = fp.readline()

# for x in fid:
#     print (x)
print(len(fid))
# print (lineNum)


time = float(float(acquTime)/len(fid))
# fig, axs = plt.subplots(nrows=1, ncols=2)
# plt.subplots_adjust(bottom=0.25)
x = np.arange(0, float(acquTime), time) 
frequ = 1.5
freq = np.arange(0, frequ*len(fid), frequ)
freqRad = freq/(2*3.1415927)
# yaxis.set_visible(False)
# set_yticklabels([])
plt.plot(freqRad, fid)
plt.margins(2, 2)
# axs[0, 0].set_title('FID')
# for ax in axs.flat:
#     ax.axhline(y=0, color='k')
#     ax.axvline(x=0, color='k')
#     ax.grid(True, which='both')
plt.show()
