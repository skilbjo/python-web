'''

number = 1

while number < 11:
	print number
	number += 1
'''

balance = 1000
rate = 1.02
years = 0
while balance < 5000:
	balance *= rate
	years += 1
print "It takes " + str(years) + " years to reach $5000 with a balance of $1000"

def convertTemp(temp, scale):
	if scale == 'c':
		return (temp - 32.0) * (5.0/9.0)
	elif scale == 'f':
		return temp * 9.0 / 5.0 + 32

temp = int(input('Enter a temperature: '))
scale = input('Enter the scale to convert: ')
convert = convertTemp(temp, scale)
print 'The converted temp is :' + str(convert)