import math
# from math import pi 

def sphere(h, r=10):
  vol = (4 * math.pi * (r ** 3)) / 3
  oth = (math.pi * (h**2) * ((3*r)-h)) / 3 
  return vol-oth

print(sphere(2))