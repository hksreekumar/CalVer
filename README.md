# Software versioning example

The example contain scripts that generates version number for your software and can be used in a CI environment to tag your latest commit.
Currently the scripts support:
1. `tools/calver/cCalVer.py`: Calendar versioning of the form YY.MM.PATCH#[-BRANCHNAME]

## Usage

For calendar versioning `CalVer`:

    # install requirements
    python3 -m pip install -r tools/calver/requirements.txt
    # run calver
    python3 tools/calver/cCalVer.py # generates a file version.txt with the new version tag
    # to use version.txt
    source version.txt
    echo $SOFTWARE_CALVER

## CI Setup

Coming soon.

## License

See LICENSE file.