import pytest

from abm.util import travis_build_url_to_github_commit, \
                     github_commit_to_travis_build_url


@pytest.mark.xfail(reason='unimplemented functionality')
def test_travis_build_url_to_github_commit():
    f = travis_build_url_to_github_commit
    assert f('https://travis-ci.org/aerogear/aerogear-unifiedpush-server/builds/219758017') \
        == ('https://github.com/aerogear/aerogear-unifiedpush-server',
            'ad3b7a94838f4808f51c25e07717709f97f41cb1')


@pytest.mark.xfail(reason='unimplemented functionality')
def test_github_commit_to_travis_build_url():
    f = github_commit_to_travis_build_url

    repo = 'https://github.com/aerogear/aerogear-unifiedpush-server',
    sha = 'ad3b7a94838f4808f51c25e07717709f97f41cb1'
    assert f(repo, sha) == 'https://travis-ci.org/aerogear/aerogear-unifiedpush-server/builds/219758017'
