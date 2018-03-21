import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import sys
import csv

def main():
    with open('XY_Raw.txt') as f:
       data=[tuple(line) for line in csv.reader(f)]
    new_data = [tuple(convert(f) for f in t) for t in data]
    RANSAC(new_data)
def convert(a_float):
    try:
        return float(a_float)
    except ValueError:
        return 0
def deg_to_rad(rad):
        return rad * (math.pi/180)
def extract_X_Y(raw_data):
    coverted_list = zip(*raw_data)
    x_list= []
    y_list=[]
    angle_list = []
    dist_list = []

    for i in xrange(len(converted_list)):
        angle_list.append(converted_list[1][i])
        dist_list.append(converted_list[2][i])

    for i in xrange(len(angle_list)):
        x_list.append((math.cos(deg_to_rad(angle_list[i])) * dist_list[i]))
        y_list.append((math.cos(deg_to_rad(angle_list[i])) * dist_list[i]))
    points = zip(x,y)
    return points

def find_line_model(point_1, point_2):
#Slope of the line
#sys.float_info.epsilon is the value 2.2204460492e-16
    m = (point_2[1] - point_1[1])/ (point_2[0] -point_1[0] + sys.float_info.epsilon)
    #y intercept
    c = point_1[1] - m*point_1[0]

    return m,c
def find_intercept_point(m, c, x0, y0):
    
    x = (x0 + m*y0 - m*c)/(1 + m**2)
    y = (m*x0 + (m**2)*y0 - (m**2)*c)/(1 + m**2) + c

    return x, y
def RANSAC(points):
    #Paramaters
    iterations = 50 #Amount of times RANSAC will run MAX
    threshold = 0.05
    ratio = 0.2 #ratio of inliers required for good model
    for i in range(iterations):
                
        np.random.shuffle(points)
        np.random.shuffle(points)
        #Selects the first and last points of the set to check after random shuffle
        point_1 = points[0] 
        point_2 = points[len(points)-1]
        print("Point 1:")
        print(point_1)
        print("Point 2:")
        print(point_2)
        #find the line of best fit paramaters via points above
        m, c = find_line_model(point_1, point_2)
        x_list = [] #List of x values that are within linear fit
        y_list = [] #List of y values that are within linear fit
        num = 0
#Build potential model x,y coordinates by finding orthogonal lines
        for k in range(len(points)-1):
            x0 = points[k][0]
            y0 = points[k][1]

            x1, y1 = find_intercept_point(m, c, x0, y0)

            distance = math.sqrt((x1-x0)**2 + (y1 - y0)**2)
            
            if (float(distance) < threshold):
                x_list.append(x0)
                y_list.append(y0)
                num+=1
        print("Size of model")
        print(num)
        if num/float(len(points)) > ratio:
            print("Found a better model:")
            print("num")
            ratio = num/float(len(points))
            model_m = m
            model_c = c
        if num >= len(points)*ratio:
            print('Model found')
            
            plot(x_list,y_list,points)
            return
        else:
            print("RANSAC Failed to find model on iteration:")
            print(iterations)
def plot(x_data,y_data,all_data):
    print(len(x_data))
    print(x_data)
    raw_input("Press <Enter> to continue")
    plt.plot(0.01,0.01,'*')
    t = 0
    for t in range(len(x_data)):
#plt.plot(max(x_data),max(y_data),min(x_data),min(y_data),'ro-')
        plt.plot(x_data[t],y_data[t],'rx')
        plt.plot(all_data[t][0],all_data[t][1],'b+')
#       plt.pause(0.05)
    plt.show()


if __name__ == "__main__":

    main()
