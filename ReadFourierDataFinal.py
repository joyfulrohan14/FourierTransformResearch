import matplotlib.pyplot as plt  # the graphing library con: limited UI components
import numpy as np  # libary to operate arrays
import math
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons



#take away x number of points
# fix the dashboard
#display only 200 points 

fileName = "ascii-fid1.txt"#input("Please enter file name with data (format point number, number): ")
acquTime = input("Enter the time (s) that it took to acquire your data: ")
fid = []
n = []
f = open("test.txt", "w")
with open(fileName, "r") as fp:
    line = fp.readline()
    while line:
        x = line.split(", ")
        n.append(x[0])
        fid.append(x[1])
        f.write(x[1])
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
f.close()

time = float(float(acquTime)/len(fid))
y5 = (fid)

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


# sets the apodization variable to 0, but need this for the divide by 0 error thrown
if (apo != 0):
    e = np.arange(0, apo*acquTime, apo)

else:
    e = 1
frequ = 1.5
freq = np.arange(2820, 2820 + frequ*len(fid), frequ)
freqRad = freq/(2*3.1415927)
y5= [float(x) for x in y5]
x = np.arange(0, float(acquTime), time) 

# set the empty arrays for the next graphs
y8 = np.array([])
y9 = np.array([])
y10 = np.array([])
y12 = np.array([])
y19 = np.array([])

# counter for the total sum
tot = 0
# Absorption Spectrum, Dispersion Spectrum, and combined Calculations



# make a fft toggle and only effects the for statements
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

# Write the y values to a text document as labeled below-uncomment if you would like to see values on a text document
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

# Makes the second figure and makes 10 seperate smaller graphs
fig = plt.figure()
# Take the x and y values found above and plot them on the figure
ax6 = plt.subplot2grid((2, 2), (0, 0))
ax7 = plt.subplot2grid((2, 2), (0, 1))
ax8 = plt.subplot2grid((2, 2), (1, 0))
ax9 = plt.subplot2grid(shape=(2, 2), loc=(1, 1))
d4, = ax6.plot(x, y5, 'tab:blue')
d6, = ax7.plot(freqRad, y8, 'tab:blue')
ax7.set_title('Absorption Spectrum')
d7, = ax8.plot(freqRad, y9, 'tab:blue')
d8, = ax8.plot(freqRad, y14, 'tab:orange')
ax8.set_title('Dispersion Spectrum')
d10, = ax9.plot(freqRad, y18, 'tab:orange')
d11, = ax9.plot(freqRad, y17, 'tab:red')
ax9.set_title('Combined Phase Absorption and Dispersion')
ax9.set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
ax7.set(xlabel='Frequency(Hz)', ylabel='Intensity(A.I.)')
ax8.set(xlabel='Frequency(Hz)', ylabel='Intensity(A.U.)')
ax6.set(xlabel='Time', ylabel='Relative Intensity(A.I.)')
ax6.axhline(y=0, color='k')
ax6.axvline(x=0, color='k')
ax6.grid(True, which='both')
ax7.axhline(y=0, color='k')
ax7.axvline(x=0, color='k')
ax7.grid(True, which='both')
ax8.axhline(y=0, color='k')
ax8.axvline(x=0, color='k')
ax8.grid(True, which='both')
ax9.axhline(y=0, color='k')
ax9.axvline(x=0, color='k')
ax9.grid(True, which='both')

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
    d4.set_ydata(y5)
    d4.set_xdata(x)
    d6.set_ydata(y8)
    d6.set_xdata(freqRad)
    d7.set_ydata(y9)
    d7.set_xdata(freqRad)
    d8.set_ydata(y14)
    d8.set_xdata(freqRad)
    d10.set_ydata(y18)
    d10.set_xdata(freqRad)
    d11.set_ydata(y17)
    d11.set_xdata(freqRad)
    # update ax.viewLim using the new dataLim

    ax6.set_ylim(min(y5), max(y5))

    ax7.set_xlim(0,max(freqRad))
    ax8.set_xlim(0,max(freqRad))
    ax7.set_ylim(0, max(y9)+1)
    ax8.set_ylim(0, max(y14)+1)

    ax9.set_xlim(0,max(freqRad))
    ax9.set_ylim(0, max(y18)+1)


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
#plt.tight_layout(pad=0, w_pad=-2, h_pad=-2)
plt.show()
