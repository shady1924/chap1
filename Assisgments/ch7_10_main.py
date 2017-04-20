from Assisgments.ch7_10 import Time

def main():
#     create object for current time 
    t1 = Time()
    print('Current time is {0}:{1}:{2}'.format(t1.getHour(),t1.getMinute(),t1.getSecond()) )
#     get input from the user 
    setseconds=eval(input("Enter the elapsed time:"))  ##  55550505
#     set the new time for the object
    t1.setTime(setseconds)
    print('The hour:minute:second for the elapsed time is {0}:{1}:{2}'.format(t1.getHour(),t1.getMinute(),t1.getSecond()) ) 
main()