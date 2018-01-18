#!/usr/bin/python

import sys

m = open("meta.bin","rb")
m.seek(0)

d = open("data.bin","rb")

count = 0

while 1:
	x = m.read(1)
	if not x:
		break

	count+=ord(x)
	d.seek(count)
	y = d.read(1)
	if not y:
		break

	z = m.read(1)

	xor = ord(y) ^ ord(z)

	sys.stdout.write(chr(xor))
print
m.close()
d.close()

