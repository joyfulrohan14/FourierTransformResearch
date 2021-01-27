import matplotlib.pyplot as plt
import numpy as np
import math

print("Enter Time Increment for all four periods")
time = input("Enter your value: ")
time = float(time)
print("Enter Frequency for Period 1")
frequency = float(input("Enter your value: "))
print("Enter Intensity for Period 1")
intensity = float(input("Enter your value: "))
print("Enter Frequency for Period 2")
frequency1 = float(input("Enter your value: "))
print("Enter Intensity for Period 2")
intensity1 = float(input("Enter your value: "))
print("Enter Frequency for Period 3")
frequency2 = float(input("Enter your value: "))
print("Enter Intensity for Period 3")
intensity2 = float(input("Enter your value: "))
print("Enter Frequency for Period 4")
frequency3 = float(input("Enter your value: "))
print("Enter Intensity for Period 4")
intensity3 = float(input("Enter your value: "))
print("Enter Half Life for Period 1")
hl1 = float(input("Enter your value: "))
print("Enter Half Life for Period 2")
hl2 = float(input("Enter your value: "))
print("Enter Half Life for Period 3")
hl3 = float(input("Enter your value: "))
print("Enter Half Life for Period 4")
hl4 = float(input("Enter your value: "))


# Some example data to display
x = np.arange(0,0.35,time)
y1 = (np.cos(x*3.14*2*frequency))*intensity
y2 = (np.cos(x*3.14*2*frequency1))*intensity1
y3 = (np.cos(x*3.14*2*frequency2))*intensity2
y4 = (np.cos(x*3.14*2*frequency3))*intensity3
y5 = y1*2.718**(-x/hl1)+y2*2.718**(-x/hl2)+y3*2.718**(-x/hl3)+y4*2.718**(-x/hl4)
y6 = y1*2.718**(-x/hl1)
#(I2*EXP(-$A2/$D$6)+(J2*EXP(-$A2/$E$6)+K2*EXP(-$A2/$F$6)+L2*EXP(-$A2/$G$6)

fig, axs = plt.subplots(nrows=3, ncols=2)
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

for ax in axs.flat:
    ax.set(xlabel='time', ylabel=' ')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
    ax.grid(True, which='both')
plt.show()