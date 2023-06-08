# !/bin/bash
new_version=`python3 ./scripts/patch_version.py`
git add .
git commit -m "auto version patch"
git push
git tag -a v$new_version -m "auto tag v$new_version"
git push origin v$new_version