# AnotherBugMiner

## Approach

It would be easiest to implement using Python 3 and [requests](http://docs.python-requests.org/en/master/).

1.  Use the GitHub API to find the N-most popular projects on GitHub.
2.  For each project, use the GitHub API to obtain a list of pull requests.
    Write the list to a JSON file (e.g., `data/pull-requests/php.json`),
    where each pull request is described as a JSON object (pulled from
    GitHub).
3.  For each pull request (PR), determine whether that PR represents a bug fix.
    There are several ways to go about this:
      * look for an issue number in the PR description (e.g., "fixes #238").
      * use regex to look for indicative keywords (e.g., "bug" and "fix").
      * use Travis to find regressions (does the build change from failing
        to passing?)
