#!python
#
# mileage reimbursement calculator
#

#imports
import math


def main():
	miles = float (input('Total miles driven: '))
	rate = float(.535)
	calc = (miles * rate) 
	total = round(calc)
	print ('Your reimbursement total is: $',total)  
    
if __name__ == "__main__":
  main()

##version debug info
import platform
#print ()
#print ()
#print ('P Y T H O N  D E B U G')
#print ('----------------------')
#print ('Current platform is: ', (platform.python_version()))
#print ('Running on:', (platform.platform()))

