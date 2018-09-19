import argparse
import random
import pdb
from datetime import datetime

#
#parse Command line input
#
def main():
   parser = argparse.ArgumentParser()
   parser.add_argument( "sampleCount", \
     help = "Number of entries to be write into the sample file" )
   parser.add_argument( "r1", \
     help = "Full Address to decompressed R1 file" ) 
   parser.add_argument( "r2", \
     help = "Full Address to decompressed R2 file" )
   args = parser.parse_args()
   R1 = args.r1
   R2 = args.r2
   SAMPLECOUNT = int(args.sampleCount)
   print( "R1 file is :", R1 )
   print( "R2 file is :", R2 )
   random.seed(datetime.now())
   ROWSPerEntry = 4

   #Address to decompressed sample files
   sampleIndexes = []
   POSTFIX = ".shorten"
   fR1New = open( "./shortenedSamples/" + R1 + POSTFIX, "w+")
   fR2New = open( "./shortenedSamples/" + R2 + POSTFIX, "w+")
   #
   #Read and Parse the compressed files
   #
   with open( R1,'r' ) as fR1:
     flines = fR1.readlines()
     rowCount = len( flines )
     dataCount = int(rowCount/ROWSPerEntry)
     #Generate array of Random Indexes# 
     assert SAMPLECOUNT <= dataCount, "Sampling size is bigger than input file size"
     sampleIndexes = random.sample( range(0,dataCount-1),SAMPLECOUNT )
     for i in sampleIndexes:
       for j in range( ROWSPerEntry ):
         lineNumToWrite = i*ROWSPerEntry + j
         fR1New.write( flines[lineNumToWrite] ) 

   with open( R2,'r' ) as fR2:
     flines = fR2.readlines()
     rowCount = len( flines )
     dataCount = int(rowCount/ROWSPerEntry)
     #Generate array of Random Indexes# 
     assert SAMPLECOUNT <= dataCount, "Sampling size is bigger than input file size"
     for i in sampleIndexes:
       for j in range( ROWSPerEntry ):
         lineNumToWrite = i*ROWSPerEntry + j
         fR2New.write( flines[lineNumToWrite] ) 
     
   #
   #Wrap-Up
   #
   fR1New.close()
   fR2New.close()

if __name__ == "__main__":
    main()
    sys.exit(0)
