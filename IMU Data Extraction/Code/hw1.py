# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-02-05 05:06:27
# Last Modified time: 2020-02-05 06:12:14

import numpy as np
import matplotlib.pyplot as plt

#Load data into python/numpy
data = np.loadtxt("../Init/imudata.txt",dtype={
	'names': ('date','time','x','y','pitch','col 6','col 7'),
	'formats' : ('S10','S10','f8','f8','f8','f8','f8')
	})
pitch_data=data['pitch']

#plot raw data for 5th column
x=np.arange(len(pitch_data))
plt.plot(x,pitch_data,label='raw data')
#label the axes and add title and legend
plt.xlabel('Time [sec]')
plt.ylabel('Pitch [degrees]')
plt.title('Original IMU Pitch data')
plt.legend(loc=1)
plt.savefig(f'../Output/Raw data')
plt.show()

#Calculating moving averages
moving_avg=[2,4,8,16,64,128]
for i in moving_avg:
	
	#plot raw data
	plt.plot(x,pitch_data,label='raw data')

	#Calculating the moving averages
	x_moving_average=[sum(range(j, j + i)) / i for j in range(len(pitch_data) - i + 1)]
	y_moving_average = [sum(pitch_data[j:j + i]) / i for j in range(len(pitch_data) - i + 1)]
	
	#plotting moving averages
	plt.plot(x_moving_average, y_moving_average,label=f'{i}-pt Moving Average')

	#calculating mu and sigma
	mu = float(np.mean(y_moving_average))
	sig = float(np.std(y_moving_average))
	print(f"i: {i} | mu: {mu} | sigma: {sig}")
	x_limits = plt.xlim()
	
	#plotting mu and sigma
	plt.plot(x_limits, (mu, mu), 'g--',label= f'Mu = {mu}')
	plt.plot(x_limits, (mu + sig, mu + sig), 'r--',label=f'STD = {sig}')
	plt.plot(x_limits, (mu - sig, mu - sig), 'r--')

	#adding labels, legend and title
	plt.title(f"IMU Pitch Data with {i}-pt Moving Average")
	plt.xlabel("Time [sec]")
	plt.ylabel("Pitch [degrees]")
	plt.legend(loc=1)
	plt.savefig(f'../Output/{i}-pt_Moving_Average')
	plt.show()