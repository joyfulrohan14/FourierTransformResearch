#Read Fourier Data from text file

#2820 Hz - starting point multiplied by 2*pi
#2900-4000 52 micro-seconds
#add offsets


#phase correction
#apodiztion (sine and exponential)

#width of frequency
#carrier of frequency
#fft

#remove FID, the sprectrums (reduce the points)

#imports
from bokeh.plotting import figure, show # the graphing library con: limited UI components
from bokeh.io import output_file, show
from bokeh.layouts import column, gridplot, row
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.plotting import figure
import numpy as np  # libary to operate arrays
import math

#code starts
fileName = "ascii-fid.txt"#input("Please enter file name with data (format point number, number): ")
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
# for x in fid:
#     print (x)

# 

y5 = (fid)#np.array(fid, dtype=np.int32)
y5= [float(x) for x in y5]
print(type(y5[0]))
time = float(float(acquTime)/len(fid))
x = np.arange(0, float(acquTime), time) 
frequ = 1.5
freq = np.arange(2820, 2820 + frequ*len(fid), frequ)
freqRad = freq/(2*3.1415927)

# set the empty arrays for the next graphs
y8 = np.array([])
y9 = np.array([])
y10 = np.array([])
y12 = np.array([])
y19 = np.array([])

# counter for the total sum
tot = 0
# Absorption Spectrum, Dispersion Spectrum, and combined Calculations
print(len(freq))
# make a fft toggle and only effects the for statements
for b in freq:
    y7 = y5*np.cos(b*x)*time
    for v in y7:
        tot = tot + v
    y8 = np.append(y8, [tot])
    tot = 0
print("h")
for b in freq:
    y7 = y5*np.sin(b*x)*time
    for v in y7:
        tot = tot + v
    y9 = np.append(y9, [tot])
    tot = 0
for b in freq:
    y7 = y5*np.sin(b*x)*time
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
    calc = b + last
    last = calc
    y12 = np.append(y12, [calc])
y13 = (y12/np.max(y8))
y14 = y13
y11 = np.sqrt(y8**2+y19**2)

y18 = np.sqrt(y8**2+y10**2)
    
y15 = np.array([])
for b in y11:
    calc = b + last
    last = calc
    y15 = np.append(y15, [calc])
y16 = (y15/np.max(y11))
y17 = y16


p = figure(title="Combined FID", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
p.line(n, y5,line_width=1)


p1 = figure(title="Absorption Spectrum", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
p1.line(freqRad, y8,line_width=1)

p2 = figure(title="Dispersion Spectrum", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
p2.line(freqRad, y9,line_width=1)
p2.line(freqRad, y14,line_width=1)

p3 = figure(title="Combined Phased Absorption and Dispersion", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
p3.line(freqRad, y18,line_width=1)
p3.line(freqRad, y17,line_width=1)

# p4 = figure(title="Combined FID", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
# p4.line(n, fid,line_width=1)

# p5 = figure(title="Combined FID", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
# p5.line(n, fid,line_width=1)


# make a grid
grid = gridplot([[p, p1], [p2, p3]], plot_width=700, plot_height=500)
print(len(freqRad))
# show the results
show(grid)