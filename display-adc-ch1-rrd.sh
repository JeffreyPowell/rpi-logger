#!/bin/bash

/usr/bin/rrdtool graph /var/www/adc-ch1-day.png \
--start -1h \
--width 400 \
DEF:volts=/var/scripts/rpi-logger/adc-ch1-log.rrd:ch1:AVERAGE \
AREA:volts#00FF00:"Battery Volts" 

