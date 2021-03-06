import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal

b,a=signal.cheby2(4,40,100,'low',analog=True)
w,h=signal.freqs(b,a)

#style.use('dark_background')
plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Chebyshev Type 2 Frequency Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Amplitude in dB')
plt.margins(0,0.1)
plt.grid(which='both',axis='both')
plt.axvline(100,color = 'teal')
plt.axhline(-40,color= 'green')
plt.show()
         
