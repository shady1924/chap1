##Sharad:  print if circles intersect or not
#x, y,radius  = 0, 40, 20
x,y,radius=eval(input("Enter Circle's 1 center x-,y-coordinates, and radius:"))   
# Circle 2 
#x2, y2, radius2 = 0, 0, 80 
x2,y2,radius2=eval(input("Enter Circle's 1 center x-,y-coordinates, and radius:"))

# # enter the distance between points 
distance = int(((x2 - x) ** 2 + (y2 - y) ** 2) ** (1 / 2))

## Logic to print the text 
txt="blank"
# Two point intersection 
if abs(radius - radius2) < distance   and  distance < abs(radius + radius2)  :
    txt="Circles 1 and Circle2 intersect at 2 points"
## One point intersection
elif abs(radius - radius2) == distance or abs(radius + radius2) == distance:
    txt="Circles 1 and Circle2 intersect at one point and circle 1 is outside circle2" if abs(radius - radius2) == distance \
    and radius > radius2 else "Circles 1 and Circle2 intersect at one point and circle 2 is outside circle 1"
## Non Intersection condition 
elif distance > abs(radius + radius2)  or   distance < abs(radius - radius2) :
    txt="Circle do not intersect and circle 1 is outside circle 2" if distance > abs(radius + radius2) else \
    "Circle do not intersect and circle 1 is inside circle 2"  if radius2 > radius else \
    "Circle do not intersect and circle 2 is inside circle 1" 
elif radius==radius2 and x==x2 and y==y2  :
    txt="Circles Overlap Each Other"    
else:
    txt="Error: Something Wrong"

print(txt)