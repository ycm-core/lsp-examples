#!/usr/bin/env python

import subprocess, os, platform

def OnWindows():
  return platform.system == 'Windows'


def Main():
  url = 'https://github.com/fwcd/KotlinLanguageServer'
  subprocess.check_call( [ 'git', 'clone', '--depth', '1', url ] )
  os.chdir( 'KotlinLanguageServer' )
  if OnWindows():
    subprocess.check_call( [ './gradlew.bat', 'server:installDist' ] )
  else:
    subprocess.check_call( [ './gradlew', 'server:installDist' ] )


if __name__ == '__main__':
  Main()
