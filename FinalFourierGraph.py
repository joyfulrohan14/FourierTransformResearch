import matplotlib.pyplot as plt  # the graphing library con: limited UI components
import numpy as np  # libary to operate arrays
import math
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons

# UI -Time, Intensity, Frequ, Integral Correction, phase
# Slider - Frequency, Half Life , Aquition Time

# User input acquition, second number is FID acquition time divided by number of points to get time incremenets
# Grab the file

# alternate apodization functions


acquTime = 636  # at/time = number points
time = 0.00055  # time increments

# inntenisty and frequency variables for the four wave functions
frequency = 100
intensity = 100
frequency1 = 200
intensity1 = 100
frequency2 = 400
intensity2 = 125
frequency3 = 700
intensity3 = 100

# the half lifes
hl1 = 0.14
hl2 = 0.07
hl3 = 0.035
hl4 = 0.0175

# frequency increments
frequ = 1.5

# apodization variable
# Apodization: 1-exponential 2-sine 3-sinesquared 4- shifted sine 5 shifted sinesquared
apo = 0
sapo = 0
s2apo = 0
ssapo = 0
ss2apo = 0

# these next six varaibles are there to manipulate the integral
phase = 1.57
cor = 0.087
scale = 0.08
shift = 1
cor1 = 0.07
scale1 = 0.05
shift1 = 0.1


# set up the figure and add a margin at the bottom for the UI components
fig, axes = plt.subplots()
plt.subplots_adjust(bottom=0.50)

# turn off graph lines
plt.axis('off')

# this section is where all the sliders and UI components are defined
axcolor = 'lightgoldenrodyellow'
resetax = plt.axes([0.9, 0.05, 0.08, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

ax_slide = plt.axes([0.2, 0.19, 0.65, 0.03])
s_factor = Slider(ax_slide, 'frequency1 (Hz)', 1, 900, valinit=100, valstep=50)

ax_slide1 = plt.axes([0.2, 0.16, 0.65, 0.03])
s_factor1 = Slider(ax_slide1, 'frequency2 (Hz)',
                   1, 900, valinit=200, valstep=50)

ax_slide2 = plt.axes([0.2, 0.13, 0.65, 0.03])
s_factor2 = Slider(ax_slide2, 'frequency3 (Hz)',
                   1, 900, valinit=400, valstep=50)

ax_slide3 = plt.axes([0.2, 0.1, 0.65, 0.03])
s_factor3 = Slider(ax_slide3, 'frequency4 (Hz)',
                   1, 900, valinit=700, valstep=50)

ax_slide4 = plt.axes([0.2, 0.32, 0.65, 0.03])
s_factor4 = Slider(ax_slide4, 'intensity1 (A.I.)',
                   0, 500, valinit=100, valstep=50)

ax_slide5 = plt.axes([0.2, 0.29, 0.65, 0.03])
s_factor5 = Slider(ax_slide5, 'intensity2 (A.I.)',
                   0, 500, valinit=200, valstep=50)

ax_slide6 = plt.axes([0.2, 0.26, 0.65, 0.03])
s_factor6 = Slider(ax_slide6, 'intensity3 (A.I.)',
                   0, 500, valinit=100, valstep=50)

ax_slide7 = plt.axes([0.2, 0.23, 0.65, 0.03])
s_factor7 = Slider(ax_slide7, 'intenisty4 (A.I.)',
                   0, 500, valinit=100, valstep=50)

axbox = plt.axes([0.2, 0.06, 0.65, 0.03])
text_box = TextBox(axbox, 'Time (s)', initial=0.00055)

ax_slide8 = plt.axes([0.2, 0.69, 0.65, 0.03])
s_factor8 = Slider(ax_slide8, 'T2 1 (s)', 0, 1, valinit=0.14, valstep=0.001)

ax_slide9 = plt.axes([0.2, 0.66, 0.65, 0.03])
s_factor9 = Slider(ax_slide9, 'T2 2 (s)', 0, 1, valinit=0.07, valstep=0.001)

ax_slide10 = plt.axes([0.2, 0.63, 0.65, 0.03])
s_factor10 = Slider(ax_slide10, 'T2 3 (s)', 0, 1, valinit=0.035, valstep=0.001)

ax_slide11 = plt.axes([0.2, 0.60, 0.65, 0.03])
s_factor11 = Slider(ax_slide11, 'T2 4 (s)', 0, 1,
                    valinit=0.0175, valstep=0.001)

ax_slide12 = plt.axes([0.2, 0.55, 0.65, 0.03])
s_factor12 = Slider(ax_slide12, 'Acquition Time', 300,
                    1000, valinit=636, valstep=50)

rax = plt.axes([0, 0.39, 0.25, 0.15], facecolor=axcolor)
radio2 = RadioButtons(rax, ('none','exponential','sine', 'sine-squared'))

axbox9 = plt.axes([0.6, 0.48, 0.20, 0.05])
text_box9 = TextBox(axbox9, 'Exponential Apodization', initial=0)

axbox10 = plt.axes([0.6, 0.42, 0.20, 0.05])
text_box10 = TextBox(axbox10, 'Shift Value Apodization', initial=0)

axbox1 = plt.axes([0.4, 0.73, 0.20, 0.03])
text_box1 = TextBox(axbox1, 'Phase', initial=1.57)

axbox2 = plt.axes([0.4, 0.76, 0.2, 0.03])
text_box2 = TextBox(axbox2, 'Frequency Step', initial=1.5)

axbox3 = plt.axes([0.4, 0.80, 0.2, 0.03])
text_box3 = TextBox(axbox3, 'Corection Absorption ', initial=0.087)

axbox4 = plt.axes([0.4, 0.83, 0.2, 0.03])
text_box4 = TextBox(axbox4, 'Scale Absorption', initial=0.08)

axbox5 = plt.axes([0.4, 0.86, 0.2, 0.03])
text_box5 = TextBox(axbox5, 'Shift Absorption', initial=1)

axbox6 = plt.axes([0.4, 0.91, 0.2, 0.03])
text_box6 = TextBox(axbox6, 'Corection Combined Phase ', initial=0.07)

axbox7 = plt.axes([0.4, 0.94, 0.2, 0.03])
text_box7 = TextBox(axbox7, 'Scale Combined Phase', initial=0.05)

axbox8 = plt.axes([0.4, 0.97, 0.2, 0.03])
text_box8 = TextBox(axbox8, 'Shift Combined Phase', initial=0.1)


# Makes the second figure and makes 10 seperate smaller graphs
fig, axs = plt.subplots(nrows=5, ncols=2)
plt.subplots_adjust(bottom=0.25)
x = np.arange(0, time*acquTime, time)

# sets the apodization variable to 0, but need this for the divide by 0 error thrown
if (apo != 0):
    e = np.arange(0, apo*acquTime, apo)

else:
    e = 1

# These y variables are arrays with all the points needed to plot the graphs
y1 = (np.cos(x*3.14*2*frequency))*intensity  # Period 1
y2 = (np.cos(x*3.14*2*frequency1))*intensity1  # Period 2
y3 = (np.cos(x*3.14*2*frequency2))*intensity2  # Period 3
y4 = (np.cos(x*3.14*2*frequency3))*intensity3  # Period 4
y5 = (y1*2.718**(-x/hl1)+y2*2.718**(-x/hl2)+y3*2.718 **
      (-x/hl3)+y4*2.718**(-x/hl4))*(2.718**e)  # Combined FID
y6 = y1*2.718**(-x/hl1)  # Fid for Period 1
freq = np.arange(0, frequ*4800, frequ)  # x values for next set of functions
freqRad = freq/(2*3.1415927)  # x values divided by 2 pi to make the period

# set the empty arrays for the next graphs
y8 = np.array([])
y9 = np.array([])
y10 = np.array([])
y12 = np.array([])
y19 = np.array([])

# counter for the total sum
tot = 0
# Absorption Spectrum, Dispersion Spectrum, and combined Calculations
for b in freq:
    y7 = y5*np.cos(b*x)*time
    for v in y7:
        tot = tot + v
    y8 = np.append(y8, [tot])
    tot = 0
for b in freq:
    y7 = y5*np.sin(b*x)*time
    for v in y7:
        tot = tot + v
    y9 = np.append(y9, [tot])
    tot = 0
for b in freq:
    y7 = y5*np.sin(b*x+phase)*time
    for v in y7:
        tot = tot + v
    y10 = np.append(y10, [tot])
    tot = 0
for b in freq:
    y7 = y5*np.sin(b*x)*time
    for v in y7:
        tot = tot + v
    y19 = np.append(y19, [tot])
    tot = 0
last = 0
for b in y8:
    calc = b + last - cor
    last = calc
    y12 = np.append(y12, [calc])
y13 = (y12/np.max(y8))*scale
y14 = y13+shift
y11 = np.sqrt(y8**2+y19**2)
y18 = np.sqrt(y8**2+y10**2)
y15 = np.array([])
for b in y11:
    calc = b + last - cor1
    last = calc
    y15 = np.append(y15, [calc])
y16 = (y15/np.max(y11))*scale1
y17 = y16+shift1

# Write the y values to a text document as labeled below
# f = open("absorption.txt", "w")
# t = open("frequecy.txt", "w")
# v = open("phased.txt", "w")
# p = open("integral.txt", "w")
# for y in y8:
#     f.write(str(y))
#     f.write('\n')
# f.close()
# for y in freq:
#     t.write(str(y))
#     t.write('\n')
# t.close()
# for y in y10:
#     v.write(str(y))
#     v.write('\n')
# v.close()
# for y in y12:
#     p.write(str(y))
#     p.write('\n')
# p.close()

# Take the x and y values found above and plot them on the figure
fig.tight_layout()
d, = axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Period 1')
d1, = axs[0, 1].plot(x, y2, 'tab:orange')
axs[1, 0].set_title('Period 2')
d2, = axs[1, 0].plot(x, y3, 'tab:blue')
axs[1, 0].set_title('Period 3')
d3, = axs[1, 1].plot(x, y4, 'tab:red')
axs[1, 1].set_title('Period 4')
d4, = axs[2, 1].plot(x, y5, 'tab:blue')
axs[2, 1].set_title('Combined FID')
d5, = axs[2, 0].plot(x, y6, 'tab:purple')
axs[2, 0].set_title('FID period 1')
d6, = axs[3, 0].plot(freqRad, y8, 'tab:blue')
axs[3, 0].set_title('Absorption Spectrum')
d7, = axs[3, 1].plot(freqRad, y9, 'tab:blue')
d8, = axs[3, 0].plot(freqRad, y14, 'tab:orange')
axs[3, 1].set_title('Dispersion Spectrum')
d9, = axs[4, 0].plot(freqRad, y11, 'tab:orange')
axs[4, 0].set_title('Combined Absorption and Dispersion')
d10, = axs[4, 1].plot(freqRad, y18, 'tab:orange')
d11, = axs[4, 1].plot(freqRad, y17, 'tab:red')
axs[4, 1].set_title('Combined Phase Absorption and Dispersion')
axs[4, 1].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[4, 0].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[3, 0].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.I.)')
axs[3, 1].set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
axs[2, 0].set(xlabel='Time', ylabel='Relative Intensity(A.I.)')
axs[2, 1].set(xlabel='Time', ylabel='Relative Intensity(A.I.)')
axs[1, 1].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[1, 0].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[0, 1].set(xlabel='Time', ylabel='Intensity(A.I.)')
axs[0, 0].set(xlabel='Time', ylabel='Intensity(A.I.)')
for ax in axs.flat:
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which='both')

# This function resets all the values on the UI page to their original values as well as sets the graphs back to their original state


def reset(event):
    s_factor.reset()
    s_factor1.reset()
    s_factor2.reset()
    s_factor3.reset()
    s_factor4.reset()
    s_factor5.reset()
    s_factor6.reset()
    s_factor7.reset()
    s_factor8.reset()
    s_factor9.reset()
    s_factor10.reset()
    s_factor11.reset()
    s_factor12.reset()
    text_box.set_val(0.00055)
    text_box1.set_val(1.57)
    text_box2.set_val(1.5)
    text_box3.set_val(0.087)
    text_box4.set_val(0.08)
    text_box5.set_val(1)
    text_box6.set_val(0.07)
    text_box7.set_val(0.05)
    text_box8.set_val(0.1)
    text_box9.set_val(0)
    text_box10.set_val(0)


# THis function redos everything from above as soon as a user changes any of the UI components


def update(val):
    newFreq = s_factor.val
    newFreq1 = s_factor1.val
    newFreq2 = s_factor2.val
    newFreq3 = s_factor3.val
    inten = s_factor4.val
    inten1 = s_factor5.val
    inten2 = s_factor6.val
    inten3 = s_factor7.val
    hl1 = s_factor8.val
    hl2 = s_factor9.val
    hl3 = s_factor10.val
    hl4 = s_factor11.val
    acquTime = s_factor12.val
    time = float(text_box.text)
    frequ = float(text_box2.text)
    phase = float(text_box1.text)
    cor = float(text_box3.text)
    scale = float(text_box4.text)
    shift = float(text_box5.text)
    cor1 = float(text_box6.text)
    scale1 = float(text_box7.text)
    shift1 = float(text_box8.text)
    apo = float(text_box9.text)
    sapo = float(text_box10.text)
    keyword=radio2.value_selected
    if (keyword=='none'):
        e=1
        text_box10.set_val(0)
    elif(keyword=='exponential'):
        f = np.arange(0, apo*acquTime, apo)
        e = 2.718**f
    # elif (keyword=='sine-unshifted'):
    #     f=np.arange(0, acquTime, 1)
    #     e=np.sin((3.14159*f)/acquTime)
    #     for x in e:
    #         print(x)
    # elif(keyword=='sine-squared unshifted'):
    #     f=np.arange(0, acquTime, 1)
    #     e = (np.sin((3.14159*f)/acquTime))**2
    elif(keyword=='sine'):
        f=np.arange(0, acquTime, 1)
        e=np.sin((((3.14159-sapo)*f)/acquTime)+sapo)
    elif(keyword=='sine-squared'):
        f=np.arange(0, acquTime, 1)
        e=(np.sin((((3.14159-sapo)*f)/acquTime)+sapo))**2
    else:
        e = 1
    x = np.arange(0, time*acquTime, time)
    y1 = (np.cos(x*3.14*2*newFreq))*inten
    y2 = (np.cos(x*3.14*2*newFreq1))*inten1
    y3 = (np.cos(x*3.14*2*newFreq2))*inten2
    y4 = (np.cos(x*3.14*2*newFreq3))*inten3
    y5 = (y1*2.718**(-x/hl1)+y2*2.718**(-x/hl2)+y3 *
          2.718**(-x/hl3)+y4*2.718**(-x/hl4))*(e)
    y6 = y1*2.718**(-x/hl1)
    freq = np.arange(0, frequ*4800, frequ)
    freqRad = freq/(2*3.1415927)
    y8 = np.array([])
    y9 = np.array([])
    y10 = np.array([])
    y12 = np.array([])
    y19 = np.array([])
    tot = 0
    for b in freq:
        y7 = y5*np.cos(b*x)*time
        for v in y7:
            tot = tot + v
        y8 = np.append(y8, [tot])
        tot = 0
    for b in freq:
        y7 = y5*np.sin(b*x)*time
        for v in y7:
            tot = tot + v
        y9 = np.append(y9, [tot])
        tot = 0
    for b in freq:
        y7 = y5*np.sin(b*x+phase)*time
        for v in y7:
            tot = tot + v
        y10 = np.append(y10, [tot])
        tot = 0
    for b in freq:
        y7 = y5*np.sin(b*x)*time
        for v in y7:
            tot = tot + v
        y19 = np.append(y19, [tot])
        tot = 0
    last = 0
    for b in y8:
        calc = b + last - cor
        last = calc
        y12 = np.append(y12, [calc])
    y13 = (y12/np.max(y8))*scale
    y14 = y13+shift
    y11 = np.sqrt(y8**2+y19**2)
    y18 = np.sqrt(y8**2+y10**2)
    y15 = np.array([])
    for b in y11:
        calc = b + last - cor1
        last = calc
        y15 = np.append(y15, [calc])
    y16 = (y15/np.max(y11))*scale1
    y17 = y16+shift1
    # f = open("absorption.txt", "w")
    # t = open("frequecy.txt", "w")
    # v = open("phased.txt", "w")
    # p = open("integral.txt", "w")
    # for y in y8:
    #     f.write(str(y))
    #     f.write('\n')
    # f.close()
    # for y in freq:
    #     t.write(str(y))
    #     t.write('\n')
    # t.close()
    # for y in y10:
    #     v.write(str(y))
    #     v.write('\n')
    # v.close()
    # for y in y12:
    #     p.write(str(y))
    #     p.write('\n')
    # p.close()
    # resets the data of the UI slider/UI that was changed
    d.set_ydata(y1)
    d.set_xdata(x)
    d1.set_ydata(y2)
    d1.set_xdata(x)
    d2.set_ydata(y3)
    d2.set_xdata(x)
    d3.set_ydata(y4)
    d3.set_xdata(x)
    d4.set_ydata(y5)
    d4.set_xdata(x)
    d5.set_ydata(y6)
    d5.set_xdata(x)
    d6.set_ydata(y8)
    d6.set_xdata(freqRad)
    d7.set_ydata(y9)
    d7.set_xdata(freqRad)
    d8.set_ydata(y14)
    d8.set_xdata(freqRad)
    d9.set_ydata(y11)
    d9.set_xdata(freqRad)
    d10.set_ydata(y18)
    d10.set_xdata(freqRad)
    d11.set_ydata(y17)
    d11.set_xdata(freqRad)
    # update ax.viewLim using the new dataLim
    axs[0, 0].set_xlim(0, 636*time)
    axs[0, 1].set_xlim(0, 636*time)
    axs[0, 0].set_ylim(-(inten), inten)
    axs[0, 1].set_ylim(-inten1, inten1)

    axs[1, 0].set_xlim(0, 636*time)
    axs[1, 1].set_xlim(0, 636*time)
    axs[1, 0].set_ylim(-inten2, inten2)
    axs[1, 1].set_ylim(-inten3, inten3)

    axs[2, 0].set_xlim(0, 636*time)
    axs[2, 1].set_xlim(0, 636*time)
    axs[2, 0].set_ylim(-inten, inten)
    axs[2, 1].set_ylim(min(y5), max(y5))

    # axs[3, 0].set_xlim(0,max(freqRad))
    # axs[3, 1].set_xlim(0,max(freqRad))
    # axs[3, 0].set_ylim(0, max(y9))
    # axs[3, 1].set_ylim(0, max(y14))

    # axs[4, 0].set_xlim(0,max(freqRad))
    # axs[4, 1].set_xlim(0,max(freqRad))
    # axs[4, 0].set_ylim(0, max(y11))
    # axs[4, 1].set_ylim(0, max(y18))






    # redrawing the figure
    fig.canvas.draw()


# these set of lines listen to when a UI component is changed and calls the update function if so
s_factor.on_changed(update)
s_factor1.on_changed(update)
s_factor2.on_changed(update)
s_factor3.on_changed(update)
s_factor4.on_changed(update)
s_factor5.on_changed(update)
s_factor6.on_changed(update)
s_factor7.on_changed(update)
s_factor8.on_changed(update)
s_factor9.on_changed(update)
s_factor10.on_changed(update)
s_factor11.on_changed(update)
s_factor12.on_changed(update)
text_box.on_submit(update)
text_box1.on_submit(update)
text_box2.on_submit(update)
text_box3.on_submit(update)
text_box4.on_submit(update)
text_box5.on_submit(update)
text_box6.on_submit(update)
text_box7.on_submit(update)
text_box8.on_submit(update)
text_box9.on_submit(update)
button.on_clicked(reset)
radio2.on_clicked(update)

# displays everything on the figures
plt.show()
