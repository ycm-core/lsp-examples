#!/usr/bin/env python3

import subprocess, os, sys, platform

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


def FindExecutableOrDie( executables, message ):
  for executable in executables:
    path = FindExecutable( executable )
    if path:
      break

  if not path:
    sys.exit( "ERROR: Unable to find any executable from '{0}'. {1}".format(
      executables,
      message ) )

  return path


def Main():
  pip = FindExecutableOrDie( [ 'pip', 'pip3' ],
                             'pip is required to install fortls.' )
  subprocess.check_call( [ pip,
                           'install',
                           '--user',
                           '--upgrade',
                           'fortran-language-server' ] )


if __name__ == '__main__':
  Main()
