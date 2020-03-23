# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_| and Zach
# Date:   2020-02-17 17:14:44
# Last Modified time: 2020-02-17 17:55:01

import RPi.GPIO as gpio
import time
import os
import cv2

#CONSTANTS
trig=16
echo=18

def distance():
	gpio.setmode(gpio.BOARD)
	gpio.setup(trig,gpio.OUT)
	gpio.setup(echo,gpio.IN)

	#ENSURE OUTPUT HAS NO VALUE
	gpio.output(trig,False)
	time.sleep(0.01)

	#Generate Trigger pulse
	gpio.output(trig, True)
	time.sleep(0.000001)
	gpio.output(trig,False)

	#Generate Echo time signal
	while gpio.input(echo)==0:
		pulse_start=time.time()

	while gpio.input(echo)==1:
		pulse_end=time.time()

	pulse_delta=pulse_end-pulse_start

	#Convert time to distance
	distance=pulse_delta*17150
	distance=round(distance,2)

	#Clean up GPIO pins and return distance estimate
	gpio.cleanup()
	return distance



if __name__=="__main__":
	dist=0
	for i in range(0,10):		
		dist+=distance()
		print(f'Distance: {distance()}cm')
		time.sleep(1)	
	dist=dist/10

	name="lecture.jpg"
	os.system("raspistill -w 640 -h 480 -o "+name)

	image=cv2.imread(name)
	font=cv2.FONT_HERSHEY_SIMPLEX
	image=cv2.flip(image,0)
	cv2.putText(image,f"dist is {round(dist,3)}",(50,400),font,1,(255,0,0),3)
	cv2.imwrite("output.png",image)

