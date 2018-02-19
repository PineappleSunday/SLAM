
from rplidar import RPLidar
def main():
	

	
	lidar = RPLidar('/dev/ttyUSB0')
	
	lidar.stop_motor()
	lidar.disconnect()
	print('I got here')


if __name__ == "__main__":

	main()
