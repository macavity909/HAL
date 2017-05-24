import argparse
import numpy as np
import math 
import serial
from matplotlib import pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('COM4', 9600)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

thefile = open('test.txt', 'w')

arr = []

cnt=0
x=[]
y=[]
graph_data = 0.0
def animate(cnt):
	graph_data = ser.readline().rstrip()
	graph_data = 0.0853*float(graph_data)/1000
	x.append(cnt)
	y.append(graph_data)
	arr.append(graph_data)
	if(graph_data>1.79 and graph_data<1.845):thefile.write("%sb" % graph_data) 
	
	
	ax1.clear()
	plt.ylim([1.7,2.0])
	ax1.plot(x,y)
	cnt = cnt+1
	print(graph_data)
	
ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()

 
""" 
if __name__=='__main__':
	 
	
	 
	
	
	
	
	
if __name__=='__maicn__':
	args = argument_parser().parse_args()
	cap = cv2.VideoCapture(0) 
 
	if not cap.isOpened():
		print 'not'
	cur_char = -1
	prev_char = -1
	
	while True: 
		ret, frame = cap.read()
		frame = cv2.resize(frame, None, fx=1.5,fy=1.5, interpolation = cv2.INTER_AREA)
		c = cv2.waitKey(1)
		 
		if c == 27:
			break 
		
		#if c == 255:
			#raise IOError(c)
		
		if c < 255: # and c != prev_char:
			cur_char = c
		#prev_char = c
		
		if cur_char == ord('g'):
			output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		elif cur_char == ord('y'):
			output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
		elif cur_char == ord('h'):
			output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		else:
			output = frame
			
		cv2.imshow('Webcam', output)
	cap.release()
	cv2.destroyAllWindows()
					
	 
"""
  


