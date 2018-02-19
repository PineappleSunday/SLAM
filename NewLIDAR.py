import numpy as np
from rplidar import RPLidar
import matplotlib.pyplot as plt
import math 
def Init():
	
	lidar = RPLidar('/dev/ttyUSB0')


	data = []
	
	
	lidar.connect()
	for i, scan in enumerate(lidar.iter_scans(500,10)):
		print('Scanning')
		if i > 40:
			break
	lidar.stop_motor()
	lidar.disconnect()	
	
	new_List=zip(*scan)
	angle_list=[]
	distance_list=[]
	
	for i in xrange(len(new_List[1])):
		angle_list.append(new_List[1][i])
		distance_list.append(new_List[2][i])
	
		


	


	
def main():

	Init()
if __name__ == "__main__":

	main()
