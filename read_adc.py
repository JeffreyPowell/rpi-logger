#!/usr/bin/python

from ABElectronics_ADCPi import ADCPi
import time
import datetime
import os

# Sample rate can be 12,14, 16 or 18
adc = ADCPi(0x68, 0x69, 12)

refvolts = 12.91

raw1 = 769.0
raw2 = 773.0
raw3 = 768.0

x1 = raw1/refvolts
x2 = raw2/refvolts
x3 = raw3/refvolts

#x1=x2=x3=1

y = 1.00
z = 1.00

rate = 0.1 # seconds
samples = 10 # samples

def writetofile(texttowrite):
	f = open('/ABElectronics_Python_Libraries/ABElectronics_ADCPi/log_raw.txt', 'a')
	f.write(str( texttowrite ) )
	f.closed

for i in range(0, 50):

	t1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	v1 = 0
	v2 = 0
	v3 = 0
	v4 = 0
	v5 = 0
	v6 = 0
	v7 = 0

	v8 = 0

	for j in range(0, samples):

		v1 = v1 + adc.readRaw(1)
		v2 = v2 + adc.readRaw(2)
		v3 = v3 + adc.readRaw(3)
		#v4 = v4 + adc.readRaw(4)
		#v5 = v5 + int("%8.0f" % (adc.readRaw(5)/3))
		#v6 = v6 + int("%8.0f" % (adc.readRaw(6)/3))
		#v7 = v7 + int("%8.0f" % (adc.readRaw(7)/3))
		#v8 = v8 + int("%8.0f" % (adc.readRaw(8)/3))
		time.sleep(rate)

	v1 = v1 / samples
	v2 = v2 / samples
	v3 = v3 / samples
	#v4 = v4 / samples
	#v5 = v5 / samples
	#v6 = v6 / samples
	#v7 = v7 / samples
	#v8 = v8 / samples

	s1 = "%2.3f" % (   v1    /x1 )
	s2 = "%2.3f" % (   v2    /x2 )
	s3 = "%2.3f" % (   v3    /x3 )
	#s4 = "%2.4f" % (   v4    /x4 )
	#s5 = "%4.4f" % ( ( v5-z )/y )
	#s6 = "%4.4f" % ( ( v6-z )/y )
	#s7 = "%4.4f" % ( ( v7-z )/y )
	#s8 = "%4.4f" % ( ( v8-z )/y )

	t2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	#s = t1+", "+s1+", "+s2+", "+s3+", "+s4+", "+s5+", "+s6+", "+s7+", "+s8 +", "+t2
	s = t1+", "+s1+", "+s2+", "+s3

	print ( s )
	#writetofile(s + '\n')

	time.sleep(2.0)

