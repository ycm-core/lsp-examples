#!/usr/bin/env python3

from urllib import request
import os
import contextlib
import functools
import time
import ssl
import zipfile
import shutil
import platform
import re
import tarfile

VERSION = '3.6.11'
URL = (
  'https://github.com/LuaLS/lua-language-server/releases/download/{version}'
  '/{package_name}'
)
PACKAGE_NAME = 'lua-language-server-{version}-{platform}-{arch}.{ext}'

@contextlib.contextmanager
def CurrentWorkingDir( d ):
  cur_d = os.getcwd()
  try:
    os.chdir( d )
    yield
  finally:
    os.chdir( cur_d )


def MakeExecutable( file_path ):
  # TODO: import stat and use them by _just_ adding the X bit.
  print( 'Making executable: {}'.format( file_path ) )
  os.chmod( file_path, 0o755 )


def WithRetry( f ):
  retries = 5
  timeout = 1 # seconds

  @functools.wraps( f )
  def wrapper( *args, **kwargs ):
    thrown = None
    for _ in range( retries ):
      try:
        return f( *args, **kwargs )
      except Exception as e:
        thrown = e
        print( "Failed - {}, will retry in {} seconds".format( e, timeout ) )
        time.sleep( timeout )
    raise thrown

  return wrapper


@WithRetry
def UrlOpen( *args, **kwargs ):
  return request.urlopen( *args, **kwargs )


def DownloadFileTo( url,
                    destination,
                    file_name = None,
                    check_certificate = True ):
  if not file_name:
    file_name = url.split( '/' )[ -1 ]

  file_path = os.path.abspath( os.path.join( destination, file_name ) )

  if not os.path.isdir( destination ):
    os.makedirs( destination )

  if os.path.exists( file_path ):
    print( "Removing existing {}".format( file_path ) )
    os.remove( file_path )

  r = request.Request( url, headers = { 'User-Agent': 'Vimspector' } )

  print( "Downloading {} to {}/{}".format( url, destination, file_name ) )

  if not check_certificate:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    kwargs = { "context":  context }
  else:
    kwargs = {}

  with contextlib.closing( UrlOpen( r, **kwargs ) ) as u:
    with open( file_path, 'wb' ) as f:
      f.write( u.read() )

  return file_path


# Python's ZipFile module strips execute bits from files, for no good reason
# other than crappy code. Let's do it's job for it.
class ModePreservingZipFile( zipfile.ZipFile ):
  def extract( self, member, path = None, pwd = None ):
    if not isinstance( member, zipfile.ZipInfo ):
      member = self.getinfo( member )

    if path is None:
      path = os.getcwd()

    ret_val = self._extract_member( member, path, pwd )
    attr = member.external_attr >> 16
    os.chmod( ret_val, attr )
    return ret_val


def RemoveIfExists( destination ):
  if os.path.exists( destination ) or os.path.islink( destination ):
    if os.path.islink( destination ):
      print( "Removing file {}".format( destination ) )
      os.remove( destination )
    else:
      print( "Removing dir {}".format( destination ) )
      shutil.rmtree( destination )


def ExtractZipTo( file_path, fmt, destination ):
  print( "Extracting {} to {}".format( file_path, destination ) )
  RemoveIfExists( destination )

  if fmt == 'zip':
    with ModePreservingZipFile( file_path ) as f:
      f.extractall( path = destination )
  elif fmt == 'tar':
    with tarfile.open( file_path ) as f:
      f.extractall( path = destination )


OUTPUT_DIR = os.path.join( os.path.dirname( os.path.abspath( __file__ ) ) ,
                           'lua-language-server' )
if os.path.isdir( OUTPUT_DIR ):
  shutil.rmtree( OUTPUT_DIR )

os.makedirs( OUTPUT_DIR )
os.chdir( OUTPUT_DIR )


def GetPlatform():
  if 'YCM_PLATFORM' in os.environ:
    return os.environ[ 'YCM_PLATFORM' ]

  if platform.system() == 'Darwin':
    return 'darwin'
  if platform.system() == 'Windows':
    return 'win32'
  return 'linux'


def GetArch():
  if 'YCM_ARCH' in os.environ:
    return os.environ[ 'YCM_ARCH' ]

  machine = platform.machine()
  if re.match( '^arm', machine.lower() ):
    return 'arm64'

  return 'x64'

package = {
  'platform': GetPlatform(),
  'arch': GetArch(),
  'ext': 'zip' if GetPlatform() == 'win32' else 'tar.gz',
  'version': VERSION,
}
package_name = PACKAGE_NAME.format( **package )
url = URL.format( package_name = package_name, **package )
file_name = DownloadFileTo( url, OUTPUT_DIR, package_name )
ExtractZipTo( file_name,
              'zip' if package['ext'] == 'zip' else 'tar',
              os.path.join( OUTPUT_DIR, 'root' ) )
