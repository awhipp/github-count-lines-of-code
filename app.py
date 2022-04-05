# Imports
import os
from dotenv import load_dotenv
from github import Github

# Load .env file
load_dotenv()

# Get GitHub SDK object using GIT_TOKEN
access_token = os.getenv('GIT_TOKEN')
g = Github(access_token)

# Get all repos (public and private)
organization = os.getenv('organization')
repos = g.get_organization(organization).get_repos()
repo_list = [i for i in repos]

files_count = 0

keyword = os.getenv('KEYWORD')

# Loop through and clone all the repos
for repo in repo_list:
    repo_name = repo.name
    if keyword in repo_name.lower():
        git_url = repo.git_url.replace('git://github.com/', 'git@github.com:')
        print(git_url)
        os.system('git clone %s repos/%s' % (git_url, repo_name))
        files_count = files_count + 1

# Count the lines
print('Counting lines...')
os.system('pygount --format=summary ./repos')
print('%s Repos counted...' % str(files_count))
