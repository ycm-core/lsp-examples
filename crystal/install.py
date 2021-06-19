#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from sys import platform
import sys
import requests
import gzip
import shutil
import os.path

# Credit goes to Sumit Ghosh: https://sumit-ghosh.com/articles/python-download-progress-bar/
def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

if platform == "linux" or platform == "linux2":
    known_versions = {
        b"0.35.1" : "https://github.com/elbywan/crystalline/releases/download/v0.1.9/crystalline_linux.gz",
        b"0.36"   : "https://github.com/elbywan/crystalline/releases/download/v0.2.1/crystalline_x86_64-unknown-linux-gnu.gz",
        b"1.0.0"  : "https://github.com/elbywan/crystalline/releases/download/v0.3.0/crystalline_x86_64-unknown-linux-gnu.gz"
        }
elif platform == "darwin":
    known_versions = {
        b"0.35.1" : "https://github.com/elbywan/crystalline/releases/download/v0.1.9/crystalline_darwin.gz",
        b"0.36"   : "https://github.com/elbywan/crystalline/releases/download/v0.2.1/crystalline_x86_64-apple-darwin.gz",
        b"1.0.0"  : "https://github.com/elbywan/crystalline/releases/download/v0.3.0/crystalline_x86_64-apple-darwin.gz"
        }
else:
    print("Unable to probe OS version, or your OS is not supported")
    exit(1)

# result = subprocess.Popen('/opt/crystal-0.36/bin/crystal --version', shell=True, stdout=subprocess.PIPE)
result = subprocess.Popen('crystal --version', shell=True, stdout=subprocess.PIPE)
result.wait()
if result.returncode:
    print("There is an error looking for Crystal version. Possibly, Crystal is not installed")
    exit(2)

versionline = result.stdout.readlines()
if not (versionline and versionline[0][:7] == b"Crystal"):
    print("Unable to find Crystal version in crystal output")
    exit(3)

versionline = versionline[0]
sspace = versionline.index(b' ', 8)
version = versionline.split()[1]
print(f"Found Crystal version {version.decode('utf-8')}")


url = ""
for v in known_versions:
    if version >= v:
        url = known_versions[v]

if not url:
    print("Unable to find crystalline URL for your Crystal version")
    exit(4)

print(f"Using URL {url}")
if os.path.isfile("/tmp/crystalline.gz"):
    print("Re-using downloaded file")
else:
    download(url, "/tmp/crystalline.gz")

with gzip.open("/tmp/crystalline.gz", "rb") as z:
    with open("/tmp/crystalline", "wb") as f:
        f.write(z.read())
subprocess.check_call( ("chmod", "+x", "/tmp/crystalline") )

try:
    try:
        os.mkdir("bin")
    except FileExistsError:
        pass
    shutil.move("/tmp/crystalline", "bin/crystalline")
except OSError:
    print("Error writing bin/crystalline. Possibly, you don't have permissions")
