from git import Repo

repo_dir = ''
repo = Repo(repo_dir)
file_list = [
    'ticker.csv',
    'historical_price.csv'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()