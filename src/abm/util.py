import os
from typing import Tuple
from travispy import TravisPy
from urllib.parse import urlparse

# Project base directory. Assumes that this file is in src/abm/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Authorize with GitHub
with open(os.path.join(BASE_DIR, 'etc/token.txt')) as f:
    token = TravisPy.github_auth(f.read().strip())
    user = token.user()


def parse_travis_url(travis_url:str) -> Tuple[str, str]:
    """
    Accepts the URL of a (public) Travis build and returns a pair of the form
    `(repo_name, build_id)`, where `repo_name` is the name of the repo on
    Travis and `build_id` is the id of the build in the URL.
    """
    parsed = urlparse(travis_url)
    # path will be of the form /[repo_name]/builds/[build_id]
    repo_name, build_id = parsed.path.split('/builds/')
    # Drops the leading slash of repo_name after the split
    return (repo_name[1:], build_id)

def travis_build_url_to_github_commit(build_url: str) -> Tuple[str, str]:
    """
    Accepts the URL of a (public) Travis build
    (e.g., https://travis-ci.org/squaresLab/genprog-code/builds/336578196),
    and returns a pair of the form `(repo, sha)`, where `repo` is the name of
    URL of the corresponding GitHub project to which the build belongs, and
    `sha` is the hex. SHA (e.g., f9c6cb57e8ab2d8f07604946cd2cd570274ace04) of
    the commit associated with the given Travis build.
    """
    raise NotImplementedError


def github_commit_to_travis_build_url(repo: str, commit: str) -> str:
    """
    Returns the URL for the Travis build that corresponds to a given commit to
    a specified public repository on GitHub.

    Params:
        repo:      the URL of the GitHub repository.
        commit:    the SHA for the commit.

    Returns:
        The URL to the Travis build for the given commit.
    """
    raise NotImplementedError
