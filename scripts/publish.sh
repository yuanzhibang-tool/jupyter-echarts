# !/bin/bash
out=`python3 ./scripts/patch_version.py`
echo out
cd code
flit build
flit publish    # This will ask for username and password
