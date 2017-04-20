'''
(Sum a series) Write a program to sum the following series:
'''

sumseries=0

for i in range(1,98):
    print(sumseries, i, ((2*i-1)/(2*i+1)))
    sumseries=sumseries+ ((2*i-1)/(2*i+1))

print("****sum os series is ****",round(sumseries,2))