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


def FindExecutableOrDie( executable, message ):
  path = FindExecutable( executable )

  if not path:
    sys.exit( "ERROR: Unable to find executable '{0}'. {1}".format(
      executable,
      message ) )

  return path


def Main():
  npm = FindExecutableOrDie( 'npm', 'npm is required to set up Postgre LS.' )
  ## Note this is how we do because they use `"optionalDependencies"` under;
  ##   ./node_modules/@postgrestools/postgrestools/package.json
  ## ...  And `npm add` seems to auto-detect OS and architecture
  subprocess.check_call( [ npm, 'add', '--save-dev', '--save-exact', '@postgrestools/postgrestools' ] )


if __name__ == '__main__':
  Main()
