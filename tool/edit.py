from github import Github
import git
import yaml
import os

TOKEN = os.environ['GITHUB_TOKEN']
REPO = os.environ['GITHUB_REPOSITORY']
#WORKFLOW_PATH = '.github'


g = Github(TOKEN)
repo = g.get_repo(REPO)
git_repo = git.Repo(os.getcwd())

if __name__ == '__main__':
    print('pass')