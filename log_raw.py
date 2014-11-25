#!/usr/bin/python

from ABElectronics_ADCPi import ADCPi
import time
import datetime
import os

# Sample rate can be 12,14, 16 or 18
adc = ADCPi(0x68, 0x69, 18)

rate = 0.001 # seconds
samples = 10 # samples

def writetofile(texttowrite):
	f = open('/ABElectronics_Python_Libraries/ABElectronics_ADCPi/log_raw.txt', 'a')
	f.write(str( texttowrite ) )
	f.closed

for i in range(0, 1):

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
		v4 = v4 + adc.readRaw(4)
		v5 = v5 + int("%8.0f" % (adc.readRaw(5)/300))
		v6 = v6 + int("%8.0f" % (adc.readRaw(6)/300))
		v7 = v7 + int("%8.0f" % (adc.readRaw(7)/300))
		v8 = v8 + int("%8.0f" % (adc.readRaw(8)/300))
		time.sleep(rate)

	v1 = v1 / samples
	v2 = v2 / samples
	v3 = v3 / samples
	v4 = v4 / samples
	v5 = v5 / samples
	v6 = v6 / samples
	v7 = v7 / samples
	v8 = v8 / samples

	s1 = "%8.0f" % v1
	s2 = "%8.0f" % v2
	s3 = "%8.0f" % v3
	s4 = "%8.0f" % v4
	s5 = "%8.0f" % v5
	s6 = "%8.0f" % v6
	s7 = "%8.0f" % v7
	s8 = "%8.0f" % v8

	t2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	s = t1+", "+s1+", "+s2+", "+s3+", "+s4+", "+s5+", "+s6+", "+s7+", "+s8 +", "+t2

	#print ( s )
	writetofile(s + '\n')

 

