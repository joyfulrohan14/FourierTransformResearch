#Read Fourier Data from text file

#2820 Hz - starting point multiplied by 2*pi
#2900-4000 52 micro-seconds
#add offsets


#apply numpys fft function before graphing (cuts down on time)

#imports
from bokeh.plotting import figure, show  # the graphing library con: limited UI components
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.plotting import figure
import numpy as np  # libary to operate arrays
import math

#code starts
fileName = "ascii-fid.txt"#input("Please enter file name with data (format point number, number): ")
acquTime = input("Enter the time (s) that it took to acquire your data: ")
fid = []
f = open("test.txt", "w")
with open(fileName, "r") as fp:
    line = fp.readline()
    while line:
        x = line.split(", ")
        fid.append(x[1])
        f.write(x[1])
        line = fp.readline()
f.close()
# for x in fid:
#     print (x)
print(len(fid))
# print (lineNum)


time = float(float(acquTime)/len(fid))
x = np.arange(0, float(acquTime), time) 
frequ = 1.5
freq = np.arange(2820, 2820 + frequ*len(fid), frequ)
freqRad = freq/(2*3.1415927)
print(len(freqRad))
p = figure(title="Combined FID", x_axis_label="Frequency(Hz)", y_axis_label="Intensity(A.U.)")
p.line(freqRad, fid,line_width=1)
# show the results
show(p)



