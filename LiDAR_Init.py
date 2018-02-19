from breezyslam.algorithms import CoreSLAM
import numpy as np
from rplidar import RPLidar
import matplotlib.pyplot as plt
import math 
import time
def Init():
	lidar = RPLidar('/dev/ttyUSB0')
	
#	lidar.connect()
#	for i, scan in enumerate(lidar.iter_scans(500,10)):
#		print('Scanning')
#		if i > 40:
#			break
#	lidar.stop_motor()
#	lidar.disconnect()	
	
	angle_list=[]
	distance_list=[]
	fig = plt.subplot()#projection='polar')
	plt.ion
	fig.grid(True)
	plt.plot([-.05,.05,.05,-.05,-.05],[.05,.05,-.05,-.05,.05])

	while(1):
		lidar.connect()
		lidar.start_motor()
		time.sleep(1)
		for i, scan in enumerate(lidar.iter_scans()):
			print('Scanning')
			if i >2:
				break
		lidar.stop()
		lidar.stop_motor()
		lidar.disconnect()
		new_List=zip(*scan)
		
		for i in xrange(len(new_List[1])):
			angle_list.append(new_List[1][i])
			distance_list.append(new_List[2][i])
		
		robX = input("X Pos: ")
		robY = input("Y Pos: ")	
		plt.scatter(robX,robY,color='red') #Robots position	
		
		print('Plotting')	
	
		for i in xrange(len(angle_list)):
			x_pos = (math.cos(angle_list[i]*(math.pi/180))*distance_list[i])*0.001
			y_pos = (math.sin(angle_list[i]*(math.pi/180))*distance_list[i])*0.001
			
			plt.scatter(x_pos,y_pos,color='green')
			#plt.scatter(angle_list[i],distance_list[i])
		plt.pause(0.5)
			


	
def main():

	Init()
if __name__ == "__main__":

	main()
