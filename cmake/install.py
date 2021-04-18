#!/usr/bin/env python3
import subprocess, platform, sys, os

PYCMD = sys.executable
DIR_OF_THIS_SCRIPT = os.path.dirname( os.path.abspath( __name__ ) )

def OnWindows():
    return platform.system() == 'Windows'


def ProcessRun(args):
    if len(args)>0:
        try:
            subprocess.run(args)
            return True
        except:
            return False
    return False


def CheckIfHavePipInstalled():
    print("Checking for pip")
    cmd=["pip","--version"]
    if ProcessRun(cmd):
        return "pip"

    cmd=["pip3","--version"]
    if ProcessRun(cmd):
        return "pip3"

    return None


def CreateVenvDir():
    print("Creating venv")
    cmd=[PYCMD,"-m","venv","venv"]
    if ProcessRun(cmd):
        return True

    return False


def InstallCMakeLanguageServer():
    binDir="bin"
    if OnWindows():
        binDir="Scripts"

    pipCMD = os.path.join(DIR_OF_THIS_SCRIPT,"venv",binDir,"pip")
    cmd=[pipCMD,"install","cmake-language-server"]
    if ProcessRun(cmd):
        return True
    return False


def Main():
    pipToUse=CheckIfHavePipInstalled()
    if pipToUse==None:
        print("Couldn't find pip in your system, please put it on path")
        return

    createdVenv=CreateVenvDir()
    if createdVenv==False:
        print("Error, couldn't create the venv directory to be used")
        return

    installCMake=InstallCMakeLanguageServer()
    if installCMake==False:
        print("Error in install process of cmake-language-server")
        return



if __name__ == "__main__":
    Main()
