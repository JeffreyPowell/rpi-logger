<?php

	// requires php5-rddtool package 

$options = array(
 "--step", "60",		// Use a step-size of 1 minutes
 "--start", "now",		// this rrd started now xxx1 day ago
 "DS:ch1:GAUGE:120:0:30",	// DataSource : Channel1, Heartbeat 120 sec, min 0, max 30
 "RRA:AVERAGE:0.5:1:1440",	// RR Archive :  1 min - 1 day
 "RRA:AVERAGE:0.5:5:8640",	// RR Archive :  5 min - 1 month
 "RRA:AVERAGE:0.5:60:8760",	// RR Archive : 60 min - 1 year
 );

$ret = rrd_create("/var/scripts/rpi-logger/adc-ch1-log.rrd", $options, count($options));
if (! $ret) {
 echo "<b>Creation error: </b>".rrd_error()."\n";
}

?>
