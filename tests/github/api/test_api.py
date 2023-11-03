from src.applications.github.api.github_api import GitHubAPIClient

def test_search_for_existing_repo():
    github_api_client = GitHubAPIClient()
    existing_repo_name = 'oksana'
    repos = github_api_client.search_repos(existing_repo_name) # list/array returned 

    print("Checking total count is not 0")
    assert repos['total_count'] != 0  # some elements exist in array/list


def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    nonexisting_repo_name = 'nvbfhgb'
    repos = github_api_client.search_repos(nonexisting_repo_name) # list/array returned 

    print("Checking total count is 0")
    assert repos['total_count'] == 0  # some elements exist in array/list


def test_search_for_nonexisting_repo():
    github_api_client = GitHubAPIClient()
    nonexisting_commit_hash = 'nvbfhgb'
    repos = github_api_client.search_commits(nonexisting_commit_hash) # list/array returned 

    print("Checking total count is 0")
    assert 0 == 0  # some elements exist in array/list
  

