import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider, Button, TextBox
#UI -Time, Intensity, Frequ, Integral Correction
#Slider - Frequency, Half Life
time = 0.00055
frequency = 100
intensity = 100
frequency1 = 200
intensity1 = 100
frequency2 = 400
intensity2 = 125
frequency3 = 700
intensity3 = 100
hl1 = 0.14
hl2 = 0.07
hl3 = 0.035
hl4 = 0.0175
frequ = 1.5 

#Set value - Future: additional phase value
phase = 1.57 

cor = 0.087 
scale = 0.08 
shift = 1 
cor1 = 0.07
scale1 = 0.05 
shift1 = 0.1 

#plt.ion()
fig, axs = plt.subplots(nrows=5, ncols=2)
x = np.arange(0,time*636,time)
y1 = (np.cos(x*3.14*2*frequency))*intensity
y2 = (np.cos(x*3.14*2*frequency1))*intensity1
y3 = (np.cos(x*3.14*2*frequency2))*intensity2
y4 = (np.cos(x*3.14*2*frequency3))*intensity3
y5 = y1*2.718**(-x/hl1)+y2*2.718**(-x/hl2)+y3*2.718**(-x/hl3)+y4*2.718**(-x/hl4)
y6 = y1*2.718**(-x/hl1)
freq = np.arange(0,frequ*4800,frequ)
freqRad = freq/(2*3.1415927)
y8=np.array([])
y9=np.array([])
y10=np.array([])
y12 = np.array([])
tot=0
for b in freq:
    y7=y5*np.cos(b*x)*time
    for v in y7:
        tot = tot + v
    y8=np.append(y8, [tot])
    tot=0 
for b in freq:
    y7=y5*np.sin(b*x)*time
    for v in y7:
        tot = tot + v
    y9=np.append(y9, [tot])
    tot=0
for b in freq:
    y7=y5*np.sin(b*x+phase)*time
    for v in y7:
        tot = tot + v
    y10=np.append(y10, [tot])
    tot=0
last = 0
for b in y8:
    calc = b +last -cor
    last=calc
    y12=np.append(y12, [calc])
y13 = (y12/np.max(y8))*scale
y14 = y13+shift
y11=np.sqrt(y8**2+y10**2)
y15 = np.array([])
for b in y11:
    calc = b +last -cor1
    last=calc
    y15=np.append(y15, [calc])
y16 = (y15/np.max(y11))*scale1
y17 = y16+shift1
f = open("absorption.txt", "w")
t = open("frequecy.txt", "w")
v = open("phased.txt", "w")
p = open("integral.txt", "w")
for y in y8:
    f.write(str(y))
    f.write('\n')
f.close()   
for y in freq:
    t.write(str(y))
    t.write('\n')
t.close()   
for y in y10:
    v.write(str(y))
    v.write('\n')
v.close() 
for y in y12:
    p.write(str(y))
    p.write('\n')
p.close()   

fig.tight_layout() 
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Period 1')
axs[0, 1].plot(x, y2, 'tab:orange')
axs[0, 1].set_title('Period 2')
axs[1, 0].plot(x, y3, 'tab:green')
axs[1, 0].set_title('Period 3')
axs[1, 1].plot(x, y4, 'tab:red')
axs[1, 1].set_title('Period 4')
axs[2, 1].plot(x, y5, 'tab:blue')
axs[2, 1].set_title('Combined FID')
axs[2, 0].plot(x, y6, 'tab:purple')
axs[2, 0].set_title('FID period 1')
axs[3, 0].plot(freqRad, y8, 'tab:blue')
axs[3, 0].set_title('Absorption Spectrum')
axs[3, 1].plot(freqRad, y9, 'tab:blue')
axs[3, 0].plot(freqRad, y14, 'tab:orange')
axs[3, 1].set_title('Dispersion Spectrum')
axs[4, 0].plot(freqRad, y10, 'tab:orange')
axs[4, 0].set_title('Phased Dispersion')
axs[4, 1].plot(freqRad, y11, 'tab:orange')
axs[4, 1].plot(freqRad, y17, 'tab:red')
axs[4, 1].set_title('Combined Phase Absorption and Dispersion')

#Label x and y plots
axs[4,1].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[4,0].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[3,0].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.I.)')
axs[3,1].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[2,0].set(xlabel='Time', ylabel='Relative Intensity(A.I.)')
axs[2,1].set(xlabel='Time', ylabel='Relative Intensity(A.I.)')
axs[1,1].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[1,0].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[0,1].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[0,0].set(xlabel='Time', ylabel='Intensity(A.I.)')

for ax in axs.flat:
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which='both')
plt.show()