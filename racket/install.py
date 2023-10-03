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
        if path.startswith('~'):
          path = os.path.expanduser('~')+path[1:]

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

def InstallRacoPackage( racoExecutable, packageName ):
  print("Installing " + packageName + " from raco")
  try: 
    subprocess.check_call( [ racoExecutable, 'pkg', 'install', packageName] )
  except subprocess.CalledProcessError as calledProcessError:
    # package is already installed if return code is 1
    if calledProcessError.returncode != 1:
      raise

def Main():
  raco = FindExecutableOrDie('raco', 'raco is required to setup Racket language server')

  InstallRacoPackage(raco, 'racket-langserver')
  # Used by Vim when it recognizes racket filetype 
  InstallRacoPackage(raco, 'fmt')


if __name__ == '__main__':
  Main()
