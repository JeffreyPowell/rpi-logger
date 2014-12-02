#!/bin/bash

# apt-get install rrdtool

/usr/bin/rrdtool create /var/scripts/rpi-logger/adc-ch1-log.rrd --step 60 --start now \
DS:ch1:GAUGE:120:0:30 \
RRA:AVERAGE:0.5:1:1400 \
RRA:AVERAGE:0.5:5:8640 \
RRA:AVERAGE:0.5:60:8760

chown www-data:www-data /var/scripts/rpi-logger/adc-ch1-log.rrd

