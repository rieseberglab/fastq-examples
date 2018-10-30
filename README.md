Small Fastq Examples
================================

Contents in this Repo
-------------------
  - generateFastqSample.py: script to generate two shorten fastq examples files from two Paired-end fastq read files.

  - ./data/ : folder containing shortened fastq example files
    
Generating new files
-----------------------------

Large FastQ files can be reduced in size using the provided script.

  - Download the original fastq to be shortened (into the same folder with this script for example). eg: 

        wget https://example.org/full_R1.fastq.gz
        wget https://example.org/full_R2.fastq.gz

  - Decompress the gunzip files:

  - Run the Script to generate two new sample files which preserve 5% of the original reads:

     ```bash
        ./generateFastqSample.py 5  <(gzip -d full_R1.fastq.gz) \
                                    <(gzip -d full_13.ANN0813_R2.fastq.gz) \
                                   3> >(gzip -c short_R1.fastq.gz) \
                                   4> >(gzip -c short_R2.fastq.gz)

        md5sum short_R1.fastq.gz > short_R1.fastq.gz.md5
        md5sum short_R2.fastq.gz > short_R2.fastq.gz.md5
     ```
   
