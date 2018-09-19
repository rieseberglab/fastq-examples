#!/usr/bin/env python3

"""
  Generate a smaller fastq sample from a pair of R1 and R2 files with user specified sizes.
  Randomly sampled entries from corresponding R1 and R2 data files are write and compressed to two
  new gunzip files 
  Input:
    -n : number of entries to be sampled from the input data files
    -R1: Gunzip file for the R1 data file
    -R2: Gunzip file for the R2 data file
  output:
    -R1.shorten and R2.shorten files are the compressed sampling files
    - Modified shortenedFastqSamples.yaml : where the newly produced shortened sample files are recorded

  Ex:
   ./generateFastqSample 100 DBGBHB_4360_R1.gz DBGBHB_4350_R2.gz

  More Help:
   ./generateFastqSample --help 

"""
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
