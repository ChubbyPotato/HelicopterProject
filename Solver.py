from math import sin, cos, tan, sqrt, asin, radians, degrees,acos,atan

Vert=float(input("Measure of Vertical Angle (E): "))
Aye=float(input("Measure of Azimuth Angle (A): "))
Z=float(input("Height (Z): "))

E1= 90-Vert
A=radians(Aye) #conversion
E=radians(E1)

OP=Z/tan(E) #O is the orgin OP is distance between heli and person

x=OP*cos(A)
y=OP*sin(A)

x1=x-40.6
y1=y+106

D=x1*x1+y1*y1
bd=sqrt(D)

Rcord=Z-61
Range=sqrt(Rcord*Rcord+D)

ele=atan(Rcord/bd)
recon=degrees(ele)
NA=90-recon

xdist=x-40.6
Az=acos(xdist/bd)
As=degrees(Az)
Duh=Aye%360
if Duh <=180:
    buh=As
else:
    buh=360-As

print("\n\nThe vertical angle is {0:.{1}f} degrees".format(NA,2))
print("The Azimuth angle is {0:.{1}f} degrees".format(buh,2))
print("The range of the antenna is: {0:.{1}f} meters".format(Range,2))