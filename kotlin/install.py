#!/usr/bin/env python3

import subprocess, os, platform

def OnWindows():
  return platform.system == 'Windows'


def Main():
  url = 'https://github.com/fwcd/KotlinLanguageServer'
  if not os.path.isdir( 'KotlinLanguageServer' ):
    subprocess.check_call( [ 'git', 'clone', '--depth', '1', url ] )

  os.chdir( 'KotlinLanguageServer' )
  subprocess.check_call( [ 'git', 'pull' ] )

  if OnWindows():
    subprocess.check_call( [ './gradlew.bat',
                             '--no-daemon',
                             'server:installDist' ] )
  else:
    subprocess.check_call( [ './gradlew',
                             '--no-daemon',
                             'server:installDist' ] )


if __name__ == '__main__':
  Main()
