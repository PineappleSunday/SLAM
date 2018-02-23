import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import sys

def main():

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

    m = (point_2[1] - point_1[1]/ (points_2[0] - point_1[0] + sys.float_info.epsilon)
    #y intercept
    c = point_1[1] - m*point_1[0]

    return m,c
def find_intercept_point(m, c, x0, y0):
    
    x = (x0 + m*y0 - m*c)/(1 + m**2)
    y = (m*x0 + (m**2)*y0 - (m**2)*c)/(1 + m**2) + c

    return x, y
def RANSAC(points):
    #Paramaters
    iterations = 20
    threshold = 3
    ratio = 0.6 #ratio of inliers required for good model

    for i in range(interations):
        
        num_points = 2 #Select how many points
        np.random.shuffle(points)
        #Selects the first and last points of the set to check after random shuffle
        point_1 = points[0] 
        point_2 = points[len(points)]
        
        #find the line of best fit paramaters via points above
        m, c = find_line_model(point_1, point_2)
        x_list = [] #List of x values that are within linear fit
        y_list = [] #List of y values that are within linear fit
        num = 0

        for k in range(points):
            x0 = points[i][0]
            y0 = points[i][1]

            x1, x2 = find_intercept_point(m, c, x0, y0)

            distance = math.sqrt((x1-x0)**2 + (y1 - y0)**2)
            
            if (distance < threshold):
                x_list.append(x0)
                y_list.append(y0)
                num+=1
        if num/float(len(points)) > ratio:
            ratio = num/float(len(points))
            model_m = m
            model_c = c
        if num > len(points)*ratio:
            print('Model found')
            return x_list, y_list

if __name__ == "__main__":

    main()
