Shorten Fastq Examples and Script
================================

Current fastq sample size is too large to quickly verify the correctness of ehawke script.
Therefore,  we have created a script to create shorter fastq sample files from existing data files and uploaded the shorten data
files to current directory together with the yaml file descripting the data uploaded.

Contents in this Repo
-------------------
  -generateFastqSample.py: script to generate two shorten fastq examples files from two R1,R2 input files
  -./shortenedFastqFiles/ : folder containing shortened fastq files
  - shortenFastqFiles.yaml : the yaml file containing the relative address of all the shortened fastq files
    in the folder mentioned above
    
How to Add New Shortened Fastq Samples to the Collection
-----------------------------
  -Download the original fastq to be shortened (into the same folder with this script for example)
  eg:
   https://genomequebec.mcgill.ca/nanuqMPS/fileDownload/id/422935/type/READ_SET_FASTQ/filename/HI.4559.003.index_13.ANN0813_R1.fastq.g           https://genomequebec.mcgill.ca/nanuqMPS/fileDownload/id/422935/type/READ_SET_FASTQ_PE/filename/HI.4559.003.index_13.ANN0813_R2.fastq.gz
   
   -Decompress the gunzip files:
   
```bash
       less HI.4559.003.index_13.ANN0813_R1.fastq.gz >> HI.4559.003.index_13.ANN0813_R1
       less HI.4559.003.index_13.ANN0813_R1.fastq.gz >> HI.4559.003.index_13.ANN0813_R1
```
 
   -Run the Script to generate two new sample files : HI.4559.003.index_13.ANN0813_R1.shorten , HI.4559.003.index_13.ANN0813_R2.shorten

 ```bash
       python generateFastqSample.py 1000 HI.4559.003.index_13.ANN0813_R1 HI.4559.003.index_13.ANN0813_R2
       #first parameter "1000" : number of lines of data to be randomly sampled from the original fastq file and put into the new files
       #second, third parameter: path to the decompressed fastq files. In this example, the files are in the same folder with the script
```
  -Move the generated files and Modify .yaml file
   -Copy the generated files: R1Sample.shorten and R2Sample.shorten into the ./shortenedFastqSamples/ folder
   -open the generated file containing the sha1 values of two generated files: sha1Values
   -Add new entries to yaml files with their corresponding SHA-1 values:
```yaml
      - name: ANN0813_Shortened
        locations:
          fastq:
            ./shortenedFastqFiles/HI.4559.003.index_13.ANN0813_R1.shorten#sha1:xxxxxxxxxx
            ./shortenedFastqFiles/HI.4559.003.index_13.ANN0813_R2.shorten#sha1:xxxxxxxxxx
 ```
 
 To-Do:
 -------------------------
 - Automate the step of moving generated files and modify yaml files
   Note: This feature can only be implemented after ehawke supports getting SHA-1 from a relative path in the yaml file. The rationale of using local relative path is that shortened fastq files are supposed to be small enough to be downloaded together with source codes and may subject to constant changes from the users.
 - Add More shortened samples from ANN,PET and ARG 
   
