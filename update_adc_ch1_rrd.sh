#!/bin/bash

event=`date +"%s"`

TEMPERATURE=`cat /sys/class/thermal/thermal_zone0/temp`
TEMPERATURE=`echo -n ${TEMPERATURE:0:2}; echo -n .; echo -n ${TEMPERATURE:2}`

/usr/bin/rrdtool update /var/scripts/rpi-logger/adc-ch1-log.rrd $event:$TEMPERATURE




