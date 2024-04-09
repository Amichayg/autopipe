from github import Github
import git
import yaml
import os

TOKEN = ''
REPO = ''
WORKFLOW_PATH = ''


g = Github(TOKEN)
repo = g.get_repo(REPO)
git_repo = git.Repo(os.getcwd())

if __name__ == '__main__':
    print('pass')