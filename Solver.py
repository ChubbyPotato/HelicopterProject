from math import sin, cos, tan, sqrt, asin, radians, degrees,acos,atan

print("Group: Suhan Gui, Joseph Goff, Matthew Siegel\n")

Vert=float(input("Measure of Vertical Angle (E): "))
Aye=float(input("Measure of Azimuth Angle (A): "))
Z=float(input("Height (Z): "))
XL=float(input("X coordinate of the antenna: "))
YL=float(input("Y coordinate of the antenna: "))

while Z<=0:
    print("Error: Helicopter crashed")
    break

while Z>0:
    E1= 90-Vert
    A=radians(Aye) #conversion
    E=radians(E1)
    
    OP=Z/tan(E) #O is the orgin OP is distance between heli and person
    
    x=OP*cos(A)
    y=OP*sin(A)
    
    x1=x-XL
    y1=y-YL
    
    D=x1*x1+y1*y1
    bd=sqrt(D)
    
    Rcord=Z-61
    Range=sqrt(Rcord*Rcord+D)
    
    ele=atan(Rcord/bd)
    recon=degrees(ele)
    NA=90-recon
    
    xdist=x-XL
    Az=atan(y1/x1)
    As=degrees(Az)
    b=abs(As)

    if x1<0:
        if y1>0:
            buh=180-b
        else:
            buh=180+b
    else:
        if y1>0:
            buh=b
        else:
            buh=360-b
    
    print("\n\nThe vertical angle is {0:.{1}f} degrees".format(NA,2))
    print("The Azimuth angle is {0:.{1}f} degrees".format(buh,2))
    print("The range of the antenna is: {0:.{1}f} meters".format(Range,2))
    break