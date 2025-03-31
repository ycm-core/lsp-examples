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
  git_dir = 'erlang_ls'
  if FindExecutable( 'erlang_ls' ) is not None and os.path.isdir(os.curdir + os.sep + git_dir) is not True:
    sys.exit( "Error: Erlang Language Server already installed by unknown means" )

  git = FindExecutableOrDie( 'git', 'git is required' )
  make = FindExecutableOrDie( 'make', 'make is required to set up Erlang LS.' )

  url = 'https://github.com/erlang-ls/erlang_ls'

  if os.path.isdir(os.curdir + os.sep + git_dir):
    print("erlang_ls already cloned into directory")
    print("Going to update and upgrade")
    os.chdir(git_dir)
    subprocess.check_call( [ git, 'pull' ] )
    subprocess.check_call( [ git, 'submodule', 'update', '--recursive' ] )
  else:
    subprocess.check_call( [ git, 'clone', '--recurse-submodules', '--depth=1', url ] )
    os.chdir(git_dir)

  subprocess.check_call( [ make ] )


if __name__ == '__main__':
  Main()
