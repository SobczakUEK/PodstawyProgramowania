# Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:
#   You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
#   You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.


import math

h = int(input("Observer's height [m]: "))
d = 3.57 * math.sqrt(h)
print(f'Distance to the horizon [km]: {d}')
