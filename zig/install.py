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


def Main():
  url = 'https://github.com/zigtools/zls'
  git = FindExecutableOrDie('git', 'git is required to setup Zig language server')
  zig = FindExecutableOrDie('zig', 'zig compiler is required to setup Zig language server')

  print("Building zig lsp from source ",url)

  if os.path.isdir(os.curdir+os.sep+'zls'):
    print("zls alread cloned into directory")
    print("Going to update and upgrade")
    os.chdir('zls')
    subprocess.check_call( [ git, 'pull' ] )
    subprocess.check_call( [ git, 'submodule', 'update', '--recursive' ] )
  else:
    subprocess.check_call( [ git, 'clone', '--recurse-submodules', '--depth=1', url ] )
    os.chdir('zls')

  # The flag '-Doptimize=ReleaseSafe' is specified in the zls source code Documentation
  # https://github.com/zigtools/zls/blob/master/README.md
  # The other flag '-Dversion-string=<Semantic Version>' was being required by the build automation process
  # When it was failing to run git for the description and resolution of the ZLS Version and Tags from 
  # the source code repository
  # The assigned Version of '0.14.0-dev.390+188a4c04' was obtained from a separately built zls binary 
  # for x86_64 Linux
  # A more permanent and prettier solution is required, but this should suffice in the interim
  subprocess.check_call( [ zig, 'build', '-Doptimize=ReleaseSafe', '-Dversion-string=0.14.0-dev.390+188a4c04'])


if __name__ == '__main__':
  Main()
