# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-03-09 18:07:40
# Last Modified time: 2020-03-09 19:45:22

import numpy as np
import RPi.GPIO as gpio

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31,gpio.OUT)
	gpio.setup(33,gpio.OUT)
	gpio.setup(35,gpio.OUT)
	gpio.setup(37,gpio.OUT)
	

def game_over():
	gpio.output(31,False)	#left 
	gpio.output(33,False)	#left
	gpio.output(35,False)	#right
	gpio.output(37,False)	#right

	gpio.cleanup()


init()
game_over()