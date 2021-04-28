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
  subprocess.check_call( cmd )


def InstallCMakeLanguageServer():
  bin_dir = "bin"
  if OnWindows():
    bin_dir = "Scripts"

  pip_cmd = os.path.join( DIR_OF_THIS_SCRIPT, "venv", bin_dir, "pip" )
  cmd = [ pip_cmd, "install", "cmake-language-server" ]
  subprocess.check_call( cmd )


def Main():
  CreateVenvDir()
  InstallCMakeLanguageServer()


if __name__ == "__main__":
  Main()
