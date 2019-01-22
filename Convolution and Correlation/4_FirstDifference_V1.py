from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import mysignals as sigs

#to calculate running sum of a signal use numpy library with function cumsum
#output_signal = np.cumsum(sigs.InputSignal_1kHz_15kHz)

output_signal = np.diff(sigs.InputSignal_1kHz_15kHz)

        
#use ggplot for grids on graph
style.use("ggplot")
style.use('dark_background')

f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle("Running_Sum")

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz,color = 'cyan')
plt_arr[0].set_title("Input_Signal",color = "cyan")

plt_arr[1].plot(output_signal,color = 'magenta')
plt_arr[1].set_title("output_signal",color = "magenta")

plt.show()

#output_signal = [None]* 320
#calc_running_sum(sigs.InputSignal_1kHz_15kHz,output_signal)
