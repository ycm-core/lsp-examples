#!/usr/bin/env python3

import subprocess, os, platform

def OnWindows():
  return platform.system() == 'Windows'


def Main():
  url = 'https://github.com/prominic/groovy-language-server'
  if not os.path.isdir( 'groovy-language-server' ):
    subprocess.check_call( [ 'git', 'clone', '--depth', '1', url ] )

  os.chdir( 'groovy-language-server' )
  subprocess.check_call( [ 'git', 'pull' ] )

  if OnWindows():
    subprocess.check_call( [ 'gradlew.bat',
                             '--no-daemon',
                             'build' ] )
  else:
    subprocess.check_call( [ './gradlew',
                             '--no-daemon',
                             'build' ] )


if __name__ == '__main__':
  Main()
