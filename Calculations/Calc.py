import math
import random as rand
from scipy import constants
import matplotlib.pyplot as plt

yard_30=27.432

def power(speed_1,speed_2):
    return speed_2-speed_1

def max_height(velocity, theta):
    h = (math.pow(velocity,2)*math.pow(math.sin(theta*math.pi/180),2))/(2*constants.g)
    return round(abs(h),1)

def ball_range(v, theta):
    sr=0
    if (theta <= 45):
        sr = (math.pow(v,2)*math.cos((90-theta)*math.pi/180))/(constants.g)
    if (theta >45 and theta<=90):
        sr = (math.pow(v,2)*math.cos(theta*math.pi/180))/(constants.g)
    if (theta >90 and theta<135):
        sr = (math.pow(v,2)*math.cos((180-theta)*math.pi/180))/(constants.g)
    if (theta>=135 and theta<180):
        sr = (math.pow(v,2)*math.cos((theta+90)*math.pi/180))/(constants.g)
    
    return round(abs(sr),1)

def shot_region(theta, hand):
    # Longon and Longoff
    if theta>=0 and theta<30:
        if hand == 'R':
            return "Long-on"
        else:
            return "Long-off"
    if theta>=330 and theta<360:
        if hand == 'L':
            return "Long-on"
        else:
            return "Long-off"

    # thirdman and fineleg
    if theta>=135 and theta<180:
        if hand == 'R':
            return "Fine-leg"
        else:
            return "Third-Man"
    if theta>=180 and theta<225:
        if hand == 'R':
            return "Third-Man"
        else:
            return "Fine-leg"

    # Covers and Middon
    if theta>=30 and theta<70:
        if hand == 'R':
            return "Min-on"
        else:
            return "Covers"
    if theta>=290 and theta<330:
        if hand == 'R':
            return "Covers"
        else:
            return "Mid-on"
    
    # Point and Square Leg
    if theta>=70 and theta<135:
        if hand == 'R':
            return "Square-Leg"
        else:
            return "Point"
    if theta>=225 and theta<290:
        if hand == 'R':
            return "Point"
        else:
            return "Square-leg"

    return 0



h = 180
angle = [0 for x in range(h)]
height = [0 for x in range(h)]
distance = [0 for x in range(h)]
shot_angle = [None for x in range(h)]
shot = [None for x in range(h)]
for i in range(0,h):
    p = rand.randint(0, 360)
    angle[i] = i
    height[i] = max_height(120*5/18, i)
    distance[i] = ball_range(120*5/18, i)
    shot_angle[i] = p
    shot[i] = shot_region(p, 'L')
    print(angle[i], height[i], distance[i],shot_angle[i], shot[i])


plt.plot(angle, height, label = 'height')
plt.plot(angle, distance, label = 'distance')
plt.xlabel('x - axis : Height and Distance')
# naming the y axis
plt.ylabel('y - axis : Angle')
 
# giving a title to my graph
plt.title('Comparison of height and distance vs angle of deflection')
plt.legend()
 
# function to show the plot
# plt.show()