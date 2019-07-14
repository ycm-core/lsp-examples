#!/usr/bin/env python

import os, urllib.request, platform, zipfile, tarfile

def OnWindows():
  return platform.system() == 'Windows'


def Main():
  if OnWindows():
    url = 'https://github.com/Pure-D/serve-d/releases/download/v0.4.1/serve-d_0.4.1-windows.zip'
    filename = 'serve-d.zip'
  else:
    url = 'https://github.com/Pure-D/serve-d/releases/download/v0.4.1/serve-d_0.4.1-linux-x86_64.tar.xz'
    filename = 'serve-d.tar.xz'

  urllib.request.urlretrieve( url, filename )

  if OnWindows():
    with zipfile.ZipFile( filename ) as zip_file:
      zip_file.extractall()
  else:
    with tarfile.open( filename ) as archive:
      archive.extractall()

  os.remove( filename )


if __name__ == '__main__':
  Main()
