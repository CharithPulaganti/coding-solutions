import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan2(AB, BC))

print(math.floor(angle + 0.5), chr(176), sep="")
