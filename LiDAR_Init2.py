from breezyslam.algorithms import CoreSLAM
import numpy as np
from rplidar import RPLidar
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math 
import time
def Init():
	lidar = RPLidar('/dev/ttyUSB0')
		
	angle_list=[]
	distance_list=[]
	
	fig = plt.subplot()
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
		print("Size:")
		print(len(new_List))
		for i in xrange(len(new_List[1])):
			angle_list.append(new_List[1][i])
			distance_list.append(new_List[2][i])
		print(len(new_List))
		robX = 0
		robY = 0	
		plt.scatter(robX,robY,color='red') #Robots position	
		
		print('Plotting')	
	
		for i in xrange(len(new_List)):
			x_pos = (math.cos(new_List[1][i]*(math.pi/180))*new_List[2][i])*0.001
			y_pos = (math.sin(new_List[1][i]*(math.pi/180))*new_List[2][i])*0.001
			
			plt.scatter(x_pos,y_pos,color='green')
			#plt.scatter(angle_list[i],distance_list[i])
		plt.pause(0.001)
		
					


	
def main():

	Init()
if __name__ == "__main__":

	main()
