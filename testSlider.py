import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider, Button, TextBox

time = 0.00055
frequency = 100
intensity = 100
frequency1 = 200
intensity1 = 100


#plt.ion()
fig,axs = plt.subplots(nrows=1, ncols=2)
plt.subplots_adjust(bottom=0.25)
x = np.arange(0,time*636,time)
y1 = (np.cos(x*3.14*2*frequency))*intensity
y2 = (np.cos(x*3.14*2*frequency1))*intensity1

#fig.tight_layout() 
d, = axs[0].plot(x, y1)
axs[0].set_title('Period 1')
d1, = axs[1].plot(x, y2, 'tab:orange')
axs[1].set_title('Period 2')

ax_slide = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_slide1 = plt.axes([0.2, 0.05, 0.65, 0.03])
s_factor = Slider(ax_slide, 'frequency1', 0, 500, valinit=100, valstep=50)
s_factor1 = Slider(ax_slide1, 'frequency2', 0, 500, valinit=200, valstep=50)

def update(val):
    newFreq = s_factor.val
    newFreq1 = s_factor1.val
    y1 = (np.cos(x*3.14*2*newFreq))*intensity
    y2 = (np.cos(x*3.14*2*newFreq1))*intensity1
    d.set_ydata(y1)
    d1.set_ydata(y2)
    #redrawing the figure
    fig.canvas.draw()


#Label x and y plots
axs[1].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[0].set(xlabel='Time', ylabel='Intensity(A.I.)')

for ax in axs.flat:
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which='both')
s_factor.on_changed(update)
s_factor1.on_changed(update)

plt.show()