#!/usr/bin/env python3

"""Select a subset of read from the input fastq files R1 and R2.
   This script assumes that the two files provide homologous reads in the same order.

  Generate a smaller fastq sample from a pair of R1 and R2 files with user specified sizes.

     generateFastqSample PCT R1 R2 3>R3 4>R4

  Parameters:

     PCT size of output in relation to input, in percent. e.g. `5`
         means keep 5%%, i.e. 1 out of every 20 reads is kept.

     R1  is the forward reads (input)
     R2  reverse reads (input)

  output:

     Selected reads from R1 are output to FD 3
     Selected reads from R2 are output to FD 4

  Ex:
   ./generateFastqSample 10  <(gzip -d -c DBGBHB_4360_R1.gz) \
                             <(gzip -d -c DBGBHB_4350_R2.gz) \
                          3> >(gzip > smaller_R1.gz) \
                          4> >(gzip > smaller_R2.gz)
"""
import argparse
import os
import sys

def each_read(filename):
    ROWSPerEntry = 4
    with open(filename, "r") as fil:
        buf = []
        for line in fil:
            if not line: break
            buf.append(line)
            if len(buf) == ROWSPerEntry:
                yield buf
                buf = []
        if len(buf) != 0:
            raise Exception("Input doesn't have multiple of %d lines." % ROWSPerEntry)


def show_progress(total, kept):
    sys.stderr.write("Processed %12d reads. Kept %12d reads.\n" % (total, kept))

def main():
    #
    #parse Command line input
    #
    parser = argparse.ArgumentParser()
    parser.add_argument("PCT", help="Size of output in percentage, relative to input size.")
    parser.add_argument("r1",  help="Fast Q paired end forward stream.")
    parser.add_argument("r2",  help="Fast Q paired end reverse stream.")

    args = parser.parse_args()
    R1 = args.r1
    R2 = args.r2
    PCT = float(args.PCT)
    if PCT < 0.0 or PCT > 100.0:
        raise Exception("Invalid percentage.")
    
    every_n = PCT / 100.00
    progress = 0.0

    fR1New = os.fdopen(3, "w")
    fR2New = os.fdopen(4, "w")
    fR1 = each_read(R1)
    fR2 = each_read(R2)

    count = 0
    kept = 0
    for r1_read in fR1:
        r2_read = next(fR2)
        count +=1
        if count % 10000 == 0:
            show_progress(count, kept)

        progress += every_n
        if progress >= 1.0:
            # keep
            fR1New.write("".join(r1_read))
            fR2New.write("".join(r2_read))
            progress -= 1.0
            kept += 1

    show_progress(count, kept)
    
    #
    #Wrap-Up
    #
    fR1New.close()
    fR2New.close()

if __name__ == "__main__":
    main()
    sys.exit(0)
