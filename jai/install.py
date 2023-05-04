#!/usr/bin/env python3

import subprocess, os, platform, sys

def OnWindows():
  return platform.system() == 'Windows'

# On Windows, distutils.spawn.find_executable only works for .exe files
# but .bat and .cmd files are also executables, so we use our own
# implementation.
def FindExecutable( executable ):
  # Executable extensions used on Windows
  WIN_EXECUTABLE_EXTS = [ '.exe', '.bat', '.cmd' ]

  paths = os.environ[ 'PATH' ].split( os.pathsep )
  base, extension = os.path.splitext( executable )

  if OnWindows() and extension.lower() not in WIN_EXECUTABLE_EXTS:
    extensions = WIN_EXECUTABLE_EXTS
  else:
    extensions = [ '' ]

  for extension in extensions:
    executable_name = executable + extension
    if not os.path.isfile( executable_name ):
      for path in paths:
        executable_path = os.path.join( path, executable_name )
        if os.path.isfile( executable_path ):
          return executable_path
    else:
      return executable_name
  return None


def FindExecutableOrDie( executable, message ):
  path = FindExecutable( executable )

  if not path:
    sys.exit( "ERROR: Unable to find executable '{0}'. {1}".format(
      executable,
      message ) )

  return path



def Main():
  url = 'https://github.com/SogoCZE/Jails'
  jai = FindExecutableOrDie(
    'jai',
    "You have to add jai to your path, e.g."
    "ln -s /path/to/jai/bin/jai-linux /usr/local/bin/jai" )
  git = FindExecutableOrDie( 'git', 'Need git to download source' )

  if not os.path.isdir( 'Jails' ):
    subprocess.check_call( [ git, 'clone', '--depth', '1', url ] )

  os.chdir( 'Jails' )
  subprocess.check_call( [ git, 'pull' ] )
  subprocess.check_call( [ git, 'submodule', 'update', '--init', '--recursive' ] )

  subprocess.check_call( [ jai, 'build.jai', '-import_dir', 'metaprogram_modules/' ] )


if __name__ == '__main__':
  Main()
