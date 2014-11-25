#!/usr/bin/python

infilename = "log_adc"
infiletype = "txt"
indirectory = "/ABElectronics_Python_Libraries/ABElectronics_ADCPi/"

outfilename = "log_adc"
outfiletype = "csv"
outdirectory = "/ABElectronics_Python_Libraries/ABElectronics_ADCPi/arch/"

infile = open( indirectory+infilename+"."+infiletype )
inlines = infile.readlines()
infile.close()

infile = open( indirectory+infilename+"."+infiletype,"w" )
infile.write("")
infile.close()

sortedlines = sorted( inlines, key=str )

for item in sortedlines:

  outfiledate = item[:10]
  outfile = open( outdirectory+outfilename+"_"+outfiledate+"."+outfiletype, "a")
  outfile.write( item )
  outfile.close()