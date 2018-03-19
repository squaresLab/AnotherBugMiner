import os
from typing import Tuple
from travispy import TravisPy
from urllib.parse import urlparse

# Project base directory. Assumes that this file is in src/abm/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# KeyError if doesn't exist

# Authorize with GitHub. Try to read from the GITHUB_TOKEN environment variable
# and then try to read from etc/token.txt if that doesn't work.
try:
    token = TravisPy.github_auth(os.environ['GITHUB_TOKEN'])
except KeyError:
    with open(os.path.join(BASE_DIR, 'etc/token.txt')) as f:
        token = TravisPy.github_auth(f.read().strip())
user = token.user()

def parse_github_url(github_url:str) -> str:
    """
    Accepts the URL of a (public) GitHub repository and returns the slug of the
    repository, which is used to identify the repo by both GitHub and Travis.
    """
    parsed = urlparse(github_url)
    return parsed.path[1:]


def parse_travis_build_url(travis_url:str) -> Tuple[str, str]:
    """
    Accepts the URL of a (public) Travis build and returns a pair of the form
    `(repo_slug, build_id)`, where `repo_slug` is the slug of the repo on
    both Travis and GitHub and `build_id` is the id of the build in the URL.
    """
    parsed = urlparse(travis_url)
    # path will be of the form /[repo_slug]/builds/[build_id]
    repo_slug, build_id = parsed.path.split('/builds/')
    # Drops the leading slash of repo_slug after the split
    return (repo_slug[1:], build_id)


def travis_build_url_to_github_commit(build_url: str) -> Tuple[str, str]:
    """
    Accepts the URL of a (public) Travis build
    (e.g., https://travis-ci.org/squaresLab/genprog-code/builds/336578196),
    and returns a pair of the form `(repo, sha)`, where `repo` is the name of
    URL of the corresponding GitHub project to which the build belongs, and
    `sha` is the hex. SHA (e.g., f9c6cb57e8ab2d8f07604946cd2cd570274ace04) of
    the commit associated with the given Travis build.
    """
    repo_slug, build_id = parse_travis_build_url(build_url)
    repo = token.repo(repo_slug)
    build = token.build(build_id)
    gh_url = 'https://github.com/' + repo_slug
    return (gh_url, build.commit.sha)


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
    repo_slug = parse_github_url(repo)
    repo = token.repo(repo_slug)
    last_build_num = int(repo.last_build_number)

    # From the TravisPy docs:
    # "There is no API endpoint for resolving commits, however commit data
    # might be included in other API entities, like Build or Job."
    # I think this means that we have to do a dumb linear search of all of
    # the builds in the repo to find the one that corresponds to this commit.
    current_build_num = last_build_num
    # Dumb linear search
    while True:
        builds = [build.id for build in
                  token.builds(slug=repo_slug, after_number=current_build_num + 1)
                  if build.commit.sha == commit]
        if builds:
            found_id = builds[0]
            break
        current_build_num -= 25
    return "https://travis-ci.org/" + repo_slug + "/builds/" + str(found_id)
