#!/usr/bin/env python3
import subprocess
import platform
import sys
import os

PY_CMD = sys.executable
DIR_OF_THIS_SCRIPT = os.path.dirname( os.path.abspath( __name__ ) )

def OnWindows():
  return platform.system() == 'Windows'


def CreateVenvDir():
  print( "Creating venv" )
  cmd = [ PY_CMD, "-m", "venv", "venv" ]
  try:
    subprocess.check_call( cmd )
    return True
  except:
    return False


def InstallCMakeLanguageServer():
  bin_dir = "bin"
  if OnWindows():
    bin_dir = "Scripts"

  pip_cmd = os.path.join( DIR_OF_THIS_SCRIPT, "venv", bin_dir, "pip" )
  cmd = [ pip_cmd, "install", "cmake-language-server" ]
  try:
    subprocess.check_call( cmd )
    return True
  except:
    return False


def Main():
  if not CreateVenvDir():
    sys.exit( "Error, couldn't create the venv directory to be used" )

  if not InstallCMakeLanguageServer():
    sys.exit( "Error in install process of cmake-language-server" )


if __name__ == "__main__":
  Main()
