#!/usr/bin/env python3
import subprocess, platform, sys, os

PY_CMD = sys.executable
DIR_OF_THIS_SCRIPT = os.path.dirname( os.path.abspath( __name__ ) )

def OnWindows():
    return platform.system() == 'Windows'


def ProcessRun( args ):
    subprocess.check_call( args )


def isPipInstalled():
    print( "Checking for pip" )
    try:
        cmd = [ "pip" , "--version" ]
        ProcessRun( cmd )
        return "pip"
    except:
        cmd=[ "pip3" , "--version" ]
        ProcessRun( cmd )
        return "pip3"

    return None


def CreateVenvDir():
    print( "Creating venv" )
    cmd = [ PY_CMD , "-m" , "venv" , "venv" ]
    try:
        ProcessRun( cmd )
        return True
    except:
        return False


def InstallCMakeLanguageServer():
    bin_dir = "bin"
    if OnWindows():
        bin_dir = "Scripts"

    pip_cmd = os.path.join( DIR_OF_THIS_SCRIPT , "venv" , bin_dir , "pip" )
    cmd=[ pip_cmd , "install" , "cmake-language-server" ]
    try:
        ProcessRun( cmd )
        return True
    except:
        return False


def Main():
    pip_to_use = isPipInstalled()
    if pip_to_use == None:
        sys.exit( "Couldn't find pip in your system, please put it on path" )

    created_venv = CreateVenvDir()
    if created_venv == False:
        sys.exit( "Error, couldn't create the venv directory to be used" )

    install_cmake = InstallCMakeLanguageServer()
    if install_cmake == False:
        sys.exit( "Error in install process of cmake-language-server" )


if __name__ == "__main__":
    Main()
