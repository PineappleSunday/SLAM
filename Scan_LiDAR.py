import numpy as np
from rplidar import RPLidar
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math 
import time


def deg_to_rad(rad):
    return rad * (math.pi/180)

def init():
    lidar = RPLidar('/dev/ttyUSB0')
    plt.plot(0,0,'r*')
    while(1):
        lidar.connect()
        lidar.start_motor()
        time.sleep(1)
        
        #begins the sampling of data and places it into scan list
        try:
            for scan in lidar.iter_scans():
                for quality, angle, distance in scan:
                    x_pos = (math.cos(deg_to_rad(angle)) * distance) * 0.001 #Conversion 
                    y_pos = (math.sin(deg_to_rad(angle)) * distance) * 0.001 #Conversion 
                    plt.scatter(x_pos, y_pos, color='green')
                plt.pause(0.5)
        except Exception as e:
            pass
        else:    
            print(e)
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
            
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
def main():

	init()
if __name__ == "__main__":

	main()
