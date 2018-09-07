Top-Level Script to Run SNP Calling in Isolated Folders
============================
Currently, Snakemake is invoked directly with targets chosen on the command line. Users are unable to run multiple experiments simultanously as
because files such as config.yaml, Snakefiles etc are occupied by the current experiment. Therefore, a top-level script, SnpCallingScript.py is created to copy input files
needed for the experiment into a new folder and store the results in the new folder such that multiple experiments could be run without interferencing with 
each other.

SnpCallingScript.py is a module called by ehawke.py to run multiple experiments parallelly but it could also be invoked directly.

Functionality of SnpCallingScript.py
==============================
  - Copy Snakefiles, config.yaml, environment.yaml, ./snake/scripts folder , ./compute-canada/profile folder and a generated script to run the experiment into a new folder called:
  ./ExperimentName
  - Run the experiments in the new folder and store the generated temporary files in the same folder
  - Generate a start-up script for users to run the experiment again directly from the generated folder
  - Interpret following command line options passed through ehawke:
```bash
    #Example of Calling ehawke.py:
    ehawke.py --samples <my list of sample files> --experiment my_experiment_name --config <my config> --snpOption
    
    #--snpOption should be empty or be replaced by one of following options:
    #    --export filePath: save experiment files and settings to a zip file with filePath specified. If no path filePath presents, 
    #save the zip file under the experiment name.
    #    --test: Launch quick test run of ehawke.py using the shortened fastq samples previously stored to verify the sanity of 
    the top-level scripts and ehawke.py.
    #    --help: display help messages  
```
Design of the Script
===============================
  - Entry point of the module is : 
  ```python
  class SnpCallSeparateExecutioner
  ```
  - upper level ehawke.py instantiates the class with parsed information from command line input
    Instance of one experiment cannot be reused for other experiments as it contains metadata of the initial experiment.
  ```python
  def __init__( self, sampleList, expName, config, options)
  ```
  - Overarching member Function is 
  ```python
  def runExperiment( self )
  ```
  Where based on the user's options, some combinations of followingg functions will be called:
  ```python
  def SetUpEnvironment( self )
  def ExecuteExperiment( self )
  def ExportResults( self )
  def TestRun( self )
  ```
  Note: TestRun( self ) deals with "--test" option but it is just a wrapper of a non-member function TestRunWithShortenedFastq() where
  the experiments and data to be run on is pre-coded to the folder containing the shortened fastq samples.
  
To-Do:
================================
    - Integrate with ehawke.py where each experiment is instantiated as a SnpCallingExperiment variable such that ehawke.py could
    owns all the meta-data of each separated experiments.
    - Test with shortened fastq samples files to finish the --test option.
