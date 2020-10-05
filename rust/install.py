#!/usr/bin/env python3

import subprocess, os, platform

def OnWindows():
  return platform.system == 'Windows'


def Main():
  url = 'https://github.com/rust-analyzer/rust-analyzer'
  if not os.path.isdir( 'rust-analyzer' ):
    subprocess.check_call( [ 'git', 'clone', '--depth', '1', url ] )

  os.chdir( 'rust-analyzer' )
  subprocess.check_call( [ 'git', 'pull' ] )

  subprocess.check_call( [ 'cargo',
                           'build',
                           '--release' ] )


if __name__ == '__main__':
  Main()
