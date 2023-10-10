# python imports
import git
from datetime import datetime

# @brief Class to handle calendar versioning
# @date 10.10.2023
# @author Harikrishnan Sreekumar
class CalVerYYYYMM:
    def __init__(self) -> None:
        pass

    # @brief Function to return the pretext in format YY.MM
    # @note unit-tested
    def getTagPreText(self):
        # returns in format YYYY.MM
        yy = str(datetime.now().year)[2:]
        mm = str(datetime.now().month).zfill(2)
        return yy + '.' + mm
    
    # @brief Function to return the existing tags available in the repository
    def getRepositoryTags(self):
        repo = git.Repo('./')
        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
        return tags
    
    # @brief Function to return the current branch name
    def getRepositoryCurrentBranchName(self):
        repo = git.Repo('./')
        return repo.active_branch.name

    # @brief Function to append the last patch
    # @param new_tag: the pre_text: string
    # @param existing_tags: all existing tags: list of strings
    # @param branch_name: current branch name: string
    # @note unit-tested
    def addLastPatch(self, new_tag, existing_tags, branch_name):
        if len(existing_tags):
            print(f'> Latest tag: {existing_tags[-1]}')
        else:
            print('> No tags yet defined for this project')
        
        # filter branches
        existing_patches = [int(str(every_tag).split('.')[2]) for every_tag in existing_tags if new_tag in str(every_tag) and '-' not in str(every_tag)]
        
        next_patch = '1'
        if len(existing_patches):
            next_patch = str(max(existing_patches) + 1)

        branch_tag = ''        
        if not (branch_name == 'master' or branch_name == 'main'):
            branch_tag = f'-{branch_name}'

        return new_tag + '.' + next_patch + branch_tag

    # @brief Function to bump the current version
    def bump(self):
        new_tag_pre_text = self.getTagPreText()
        repos_existing_tags = self.getRepositoryTags()
        #repos_branch_name = self.getRepositoryCurrentBranchName()
        new_tag = self.addLastPatch(new_tag_pre_text, repos_existing_tags, 'master')
        print(f'New tag is {new_tag}')
        return new_tag

    # @brief Creates a file with the new calendar versioning
    def create_setup(self, new_tag):
        f = open("version.txt", "w")
        f.write(f"SOFTWARE_CALVER={new_tag}")

if __name__ == '__main__':
    my_versioning = CalVerYYYYMM()
    new_tag = my_versioning.bump()
    my_versioning.create_setup(new_tag)