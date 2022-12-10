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

  subprocess.check_call( [ zig, 'build', '-Drelease-safe'])


if __name__ == '__main__':
  Main()
