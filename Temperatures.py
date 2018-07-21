import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
base_value = 5527
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
        
    if abs(t) < abs(base_value):
            base_value = t
    if t < 0 :
        print(t,  file=sys.stderr)
        base_value = abs(t)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if base_value == 5527:
    base_value = 0
print(base_value)