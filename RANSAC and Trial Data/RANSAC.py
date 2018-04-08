import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import sys
import csv

def main():
    with open('Angle_Dist_Box.txt') as f:
       data=[tuple(line) for line in csv.reader(f)]
    new_data = [tuple(convert(f) for f in t) for t in data]
    points = Convert_to_XY(new_data)
    
    RANSAC(points)

def convert(a_float):
    try:
        return float(a_float)
    except ValueError:
        return 0

def deg_to_rad(rad):
        return rad * (math.pi/180)

def Convert_to_XY(raw_data):
    
    x_list= []
    y_list=[]
    angle_list = []
    dist_list = []
    for i in xrange(len(raw_data)):
        angle_list.append(raw_data[i][0])
        dist_list.append(raw_data[i][1])

    for i in xrange(len(angle_list)):
        angle = angle_list[i]
        if( angle<=90): #Quad I
            x_list.append((math.cos(deg_to_rad(angle_list[i])) * dist_list[i])*0.001)
            y_list.append((math.sin(deg_to_rad(angle_list[i])) * dist_list[i])*0.001)
        
        elif ( angle >90 and angle <=180): #Quad IV
            x_list.append((math.cos(deg_to_rad(angle_list[i]-90)) * dist_list[i])*0.001)
            y_list.append(-(math.sin(deg_to_rad(angle_list[i]-90)) * dist_list[i])*0.001)

        elif ( angle >180 and angle <=270): #Quad III
            x_list.append(-(math.cos(deg_to_rad(270-angle_list[i])) * dist_list[i])*0.001)
            y_list.append(-(math.sin(deg_to_rad(270-angle_list[i])) * dist_list[i])*0.001)

        elif (angle > 270 and angle <= 360): #Quad II
            x_list.append(-(math.cos(deg_to_rad(angle_list[i]-270)) * dist_list[i])*0.001)
            y_list.append((math.sin(deg_to_rad(angle_list[i]-270)) * dist_list[i])*0.001)

        else:
            continue;

    points = zip(x_list,y_list)
 
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
 
    iterations = 100 #Amount of times RANSAC will run MAX
    threshold = 0.05 #This is in meters
    ratio = 0.35 #ratio of inliers required for good model
    for i in range(iterations):
                
        np.random.shuffle(points)

#Selects the first and last points of the set to check after random shuffle

        point_1 = points[0] 
        point_2 = points[len(points)-1]
        
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
        print("Need:")
        print(len(points)*ratio)
        if num/float(len(points)) > ratio:
            ratio = num/float(len(points))
            model_m = m
            model_c = c
        if num >= 1000:#len(points)*ratio:
            print('Model found')
            
            plot(x_list,y_list,points)
            return
        else:
            print("RANSAC Failed to find model on iteration:")
            print(i)
def plot(x_data,y_data,all_data):

    raw_input("Press <Enter> to continue")
    plt.plot(0.01,0.01,'*')
    t = 0
    for t in range(len(x_data)):
        plt.plot(x_data[t],y_data[t],'rx')
        plt.plot(all_data[t][0],all_data[t][1],'b+')
    
    plt.grid()
    plt.show()


if __name__ == "__main__":

    main()
