#!/usr/bin/env python3

import os
import argparse
import subprocess
import contextlib
import sys
import platform

DIR_OF_THIS_SCRIPT = os.path.dirname( os.path.abspath( __name__ ) )

parser = argparse.ArgumentParser()

def OnWindows():
  return platform.system() == 'Windows'

@contextlib.contextmanager
def TemporaryWorkingDirectory( d ):
  old_d = os.getcwd()
  print( '*** Entering direcory ' + d + ' *** ' )
  try:
    os.chdir( d )
    yield
  finally:
    os.chdir( old_d )


parser.add_argument( '--all', action='store_true' )
for d in os.listdir( DIR_OF_THIS_SCRIPT ):
  dirname = os.path.join( DIR_OF_THIS_SCRIPT, d )
  if os.path.isdir( dirname ):
    parser.add_argument( '--enable-' + d, action='store_true' )
    parser.add_argument( '--disable-' + d, action='store_true' )

args = parser.parse_args()

done = []
failed = []

for d in os.listdir( DIR_OF_THIS_SCRIPT ):
  dirname = os.path.join( DIR_OF_THIS_SCRIPT, d )
  if not os.path.isdir( dirname ):
    continue
  if not args.all and not getattr( args, 'enable_' + d ):
    continue
  if getattr( args, 'disable_' + d ):
    continue

  try:
    with TemporaryWorkingDirectory( dirname ):
      if not OnWindows() and os.path.exists( 'install' ):
        subprocess.check_call( [ 'bash', 'install' ] )
      elif os.path.exists( 'install.py' ):
        subprocess.check_call( [ sys.executable, 'install.py' ] )
    done.append( d )
  except Exception:
    failed.append( d )

vimrc = ''

if done:
  print( "** SUCCEEDED **: {}".format( ', '.join( done ) ) )

  vimrc = f"""
     let g:ycm_lsp_dir = '{ DIR_OF_THIS_SCRIPT }'
     let g:ycm_language_server = []
  """

  for d in done:
    snippet =  os.path.join( DIR_OF_THIS_SCRIPT, d, 'snippet.vim' )
    if os.path.exists( snippet ):
      with open( snippet, 'r' ) as f:
        vimrc += f.read()


if failed:
  print( "** FAILED **: {}".format( ', '.join( failed ) ) )

if not ( done + failed ):
  parser.print_help()

if vimrc:
  with open( os.path.join( DIR_OF_THIS_SCRIPT, 'vimrc.generated' ), 'w' ) as f:
    f.write( vimrc )

  print( "OK, now add the following to your vimrc:\n" )
  print( f"source { os.path.join( DIR_OF_THIS_SCRIPT, 'vimrc.generated' ) }" )
