#Questions:
#1.James: Error Handling?
#2.James: One instance per experiment or one instance for all tests?
#3.James: How do you wanna parse the command line input? I could offer a 
#   a parse function
#4.Will Ehawke support only one or more experiment?
#5. --test , store sample results
#6. go Error: what about a log?
import argparse
import os
import shutil
import subprocess
import shlex 
from datetime import datetime
import pdb

#Global Variable related to Setup
#TODO: the relative address of fastq Sample
fastqTSampleList = []
fastqTSampleResultList = []
fastqTConfig1 = []
#Store List of cmd options whose arguement is the file path that should be copied by the script
CMDOptionsForFileCopy=["--contiglist", "--config","--samplefiles"]

#Return a Parser for CMD input as a string
#TO-Do: as argparse will force the formatting, it's better to be moved to upper level script

def ConstructCmdParser():
  parser = argparse.ArgumentParser()
  parser.add_argument('--samplefiles', action = 'append', nargs="+",help='List of sample files separated by spaces')
  parser.add_argument('--config', action='append', nargs="+", help='Store database name')
  parser.add_argument('--contiglist', action='append', nargs="+")
  return parser

#Parse an String as a command string and return
def ParseStringAsCmdInput(cmdStr):
  #argparse only take cmd as a list of words
  cmdList = shlex.split(cmdStr)
  parser = ConstructCmdParser()
  args = parser.parse_args(cmdList)
  return args  

class SnpCallSeparateExecutioner():

  def __init__( self, sampleList, expName, config, options):
    self.sampleList = sampleList
    self.expName = expName
    self.config = config
    self.options = options
    self.verifyInputParam()

  def SetUpEnvironment( self, cmdArgs):

    #assume working directory is current directory
    #assume sample is in the same directory
    #assume destination directory is named by programmer for now
    cwd = os.getcwd()
    sampleDir = cwd

    #Set up destination Folder
    startTime = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    destFolderName = expName + startTime
    destDir = os.path.join(cwd,destFolderName)

    parsedCmd = ParseStringAsCmdInput(cmdArgs)
    fileList = GenerateFileCopyList(parsedCmd)
    
    for currentFile in fileList:
        destPath = os.path.join(destDir,currentFile)
        srcPath  = os.path.join(cwd, currentFile)
        if (os.path.isfile(srcPath)):
            shutil.copy(srcPath, destPath)

    self.checkResult( self.verifyCopiedFiles( fileList, destDir ) )
    #TO-DO: need to return a collection of meta-info for PrepareCmd to use
    return []

  def GenerateFileCopyList(self, parsedCmd):
    #To-Do: determine the relative path and add the snake file    #To-Do: Verfiy that data sample files from yaml file will be downloaded automatically.
    fileList = []
    for arg in vars(parsedCmd):
      #Convert Namespace elements into a list 
      fileList = fileList + getattr(parsedCmd, arg)
    return fileList    

  #Main function to run the program in separate folder
  #Interface TO-DO: For now, cmdArgs is treated as a string representing the command, however it would be better if it is already parsed
  def RunExperiment( self, cmdArgs ):
    #help and test options are overshadowing other commands
    self.checkResult( self.verifyInputParam() )
    if options[ '--help' ] != None :

      self.printHelpMsg()

    elif options [ '--test' ] != None :

      self.checkResult( self.fastqTest() )

    elif options[ '--export' ] != None:

      #TODO: Error Handling:
      cmdInfo = self.SetUpEnvironment( sampleList, expName, config, options)
      newCmd = self.PrepareCmd( cmdInfo )
      checkResult( self.runCmd( newCmd ) )
      self.exportResults( options[ '--export' ] )
    #Assume the verify input parameters has already verify the validity of the program
    else:
      self.SetUpEnvironment( sampleList, expName, config, options)
      newCmd = self.PrepareCmd()
      checkResult( self.runCmd( newCmd ) )
    # TODO
    def verifyInputParam ( self ):

      return True
    def verifyCopiedFiles ( self, fileList, destDir ):
      return True
    def checkResult( self, TruthValue ):
      return True
    def PrepareCmd ( self ):
      #To-Do: Create the new command with changed file paths
      #Store the new command
 
      return None
    def printHelpMsg ( self ):
      return True
    def fastqTest ( self ):
      cmdInfo = self.SetupEnvironment( fastqSampleList, "fastq-Test", fastqTConfig1 )
      newCmd = self.PrepareCmd( cmdInfo )
      checkResult( self.runCmd( newCmd ))
      #TODO: Error Handling
      #check : exitcode, output-size, existence of .bam, .bai file for alignment
      return True
    def exportResultTo ( self, exportDir ):
      return True
    #Input: String Containing the Full Command
    #output: True if successfully finished, otherwise returned error
    def runCmd ( self, cmdString ):
      subprocess.check_call( cmdString.split() )






