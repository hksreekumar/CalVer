# Software versioning example

The example contain scripts that generates version number for your software and can be used in a CI environment to tag your latest commit.
Currently the scripts support:
1. `tools/calver/cCalVer.py`: Calendar versioning of the form YY.MM.PATCH#[-BRANCHNAME]

## Usage

For calendar versioning `CalVer`:

    # install requirements
    python3 -m pip install -r tools/calver/requirements.txt
    # run calver - branch name defaults to master
    python3 tools/calver/cCalVer.py [branch_name] # generates a file version.txt with the new version tag
    # to use version.txt
    source version.txt
    echo $SOFTWARE_CALVER

## CI Setup

1. Incorporate jobs `tagging` from `.gitlab-ci.yml` in your project.
2. Create a access token (require read/write access) and save securely in CI variables with name `CI_KEY`.
3. [OPTIONAL] By default, tagging is activated only in the master or main branch. You may activate tagging for all branches by changing rules in the job `tagging`.

## License

See LICENSE file.