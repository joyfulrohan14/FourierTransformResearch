import matplotlib.pyplot as plt  # the graphing library con: limited UI components
import numpy as np  # libary to operate arrays
fig = plt.figure()
  
ax1 = plt.subplot2grid(shape=(5, 2), loc=(0, 0), colspan=2)
ax2 = plt.subplot2grid(shape=(5, 2), loc=(1, 0))
ax3 = plt.subplot2grid(shape=(5, 2), loc=(1, 1))
ax4 = plt.subplot2grid((5, 2), (2, 0))
ax5 = plt.subplot2grid((5, 2), (2, 1))


x = np.arange(0, 10, 0.1)
y = np.cos(x)
  
# plotting subplots
ax1.plot(x, y)
ax1.set_title('ax1')
ax2.plot(x, y)
ax2.set_title('ax2')
ax3.plot(x, y)
ax3.set_title('ax3')
ax4.plot(x, y)
ax4.set_title('ax4')
ax5.plot(x, y)
ax5.set_title('ax5')
  
# automatically adjust padding horizontally 
# as well as vertically.
  
# display plot
plt.show()