#!/usr/bin/env python3

import os
import platform
import shutil
import sys
import tempfile
import urllib.request
import zipfile


# On Windows, distutils.spawn.find_executable only works for .exe files
# but .bat and .cmd files are also executables, so we use our own
# implementation.
def FindExecutable( executable ):
  # Executable extensions used on Windows
  WIN_EXECUTABLE_EXTS = [ '.exe', '.bat', '.cmd' ]

  paths = os.environ[ 'PATH' ].split( os.pathsep )
  base, extension = os.path.splitext( executable )

  if platform.system() == 'Windows'  and extension.lower() not in WIN_EXECUTABLE_EXTS:
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

if not FindExecutable( 'dart' ):
  raise UserWarning( '`dart` is needed in $PATH for proper operation' )

ARCHIVE_URL = 'https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-{}-{}-release.zip'
IS_64BIT = sys.maxsize > 2**32

if platform.system() == 'Windows':
  system = 'windows'
  arch = 'x64' if IS_64BIT else 'ia32'
elif platform.system() == 'Darwin':
  system = 'macos'
  arch = 'x64'
elif platform.system() == 'Linux':
  system = 'linux'
  if platform.machine().lower().startswith( 'x86_64' ):
    arch = 'x64' if IS_64BIT else 'ia32'
  else:
    arch = 'arm'
    if IS_64BIT:
      arch += '64'
else:
  raise RuntimeError( 'No prebuilt archive for this operating system. Compile the SDK manually.' )


archive_response = urllib.request.urlopen( ARCHIVE_URL.format( system, arch ) )
with open( 'dart-sdk.zip', 'wb' ) as archive:
  archive.write( archive_response.read() )  


with zipfile.ZipFile( 'dart-sdk.zip', 'r' ) as dart_zip:
  with tempfile.TemporaryDirectory() as tmp_dir:
    # unzip to tmp_dir
    dart_zip.extractall( tmp_dir )
    path_to_lsp_server = os.path.join( tmp_dir, 'dart-sdk', 'bin', 'snapshots', 'analysis_server.dart.snapshot' )
    shutil.copy( path_to_lsp_server, 'analysis_server.dart.snapshot' )
