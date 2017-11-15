#!/usr/bin/python

a = input("input an number")
x = a
print "  |%1|%2|%3|%4|%5|%6|%7|%8|%9|%10"
print "---------------------------------"
while x < (a+10):
	print "%s|"%(x),
	count = 1
	count2 = 0
	while count < 11:
		z = x%count
		print "%s|"%(z),
		count += 1
		count2 += 1
	print " "
	x += 1
