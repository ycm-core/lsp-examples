#!/usr/bin/env python3

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

if '--newtype' in sys.argv:
  args = ['--git', 'https://github.com/puremourning/capnprotols', '--branch', 'newtype']
else:
  args = ['capnprotols']

subprocess.check_call([
    'cargo',
    'install',
    *args,
    '--root', os.path.join(HERE, 'root')
])
