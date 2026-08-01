#!/usr/bin/env python3

import os
import subprocess

HERE = os.path.dirname( os.path.abspath( __file__ ) )

subprocess.check_call( [
  'npm',
  'install',
  '--save-dev',
  'tombi'
] )
