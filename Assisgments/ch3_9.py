'''
Sharad:  Write a program that reads the information and prints a payroll statement:
'''

##Enter input 
empname = input("Enter employees name:")
hrsworked = eval(input("Enter Number of hours worked:"))
hrpayrate = eval(input("Enter hourly pay rate:"))
fedtax = eval(input("Enter federal tax withholding rate:"))
statetax=eval(input("Enter state tax withholding rate:"))
##fix current money symbol
currsymbol="$"
##print calculated output 
print("Employee Name:", empname)
print("Hours Worked:",format(hrsworked,'.1f') )
print('{0}{1}{2}'.format("Pay Rate: ",currsymbol, hrpayrate)    )
print('{0}{1}{2}'.format("Gross Pay: ",currsymbol, round(hrsworked*hrpayrate,2))  )
print("Deductions:")
print('{0}{1}{2}{3}{4}'.format("\tFederal Withholding (",format(fedtax*100,'3.1f'),"%): ",currsymbol,round(hrsworked*hrpayrate*fedtax,2) ) )
print('{0}{1}{2}{3}{4}'.format("\tState Withholding (",format(statetax*100,'3.1f') ,"%): ",currsymbol,round(hrsworked*hrpayrate*statetax,2) ) )
print('{0}{1}{2}'.format("\tTotal Deduction: ", currsymbol, round(hrsworked*hrpayrate*statetax + hrsworked*hrpayrate*fedtax,2 ) ) )
print('{0}{1}{2}'.format("\tNet Pay: ", currsymbol, round(hrsworked*hrpayrate - (hrsworked*hrpayrate*statetax + hrsworked*hrpayrate*fedtax)  ,2) ) )

