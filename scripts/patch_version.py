# !/usr/bin/env python3
import toml

toml_path='code/pyproject.toml'

with open(toml_path, 'r') as f:
    toml_data = toml.load(f)

current_version = toml_data['project']['version']

# Assuming the current version is in the format "x.y.z"
major, minor, patch = current_version.split('.')
patch = int(patch) + 1
new_version = f"{major}.{minor}.{patch}"

toml_data['project']['version'] = new_version

with open(toml_path, 'w') as f:
    toml.dump(toml_data, f)

print(new_version)