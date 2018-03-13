from typing import Tuple


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
