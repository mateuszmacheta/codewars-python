# 2 kyu One Line Task: Circle Intersection
# https://www.codewars.com/kata/5908242330e4f567e90000a3

from math import*;circleIntersection=lambda a,b,r:dist(a,b)<2*r and r*r*(2*acos(dist(a,b)/2/r)-sin(2*acos(dist(a,b)/2/r)))//1

print(circleIntersection([0, 0],[7, 0],5))
print(circleIntersection([-5, 0],[5, 0],3))
