# AnotherBugMiner

## Approach

1.  Use the GitHub API to find the N-most popular projects on GitHub.
2.  For each project, use the GitHub API to obtain a list of pull requests.
    Write the list to a JSON file (e.g., `data/pull-requests/php.json`),
    where each pull request is described as a JSON object (pulled from
    GitHub).
3.  For each pull request, determine whether it represents a bug fix.
