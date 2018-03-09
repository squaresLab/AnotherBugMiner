import pytest

from abm.observation import Observation, ObservationCollection


def test_getters():
    url_repository='http://github.com/squaresLab/genprog-code'
    commit_bug = '3cd6c6e6a1f20b41fc5ef928f80d9e54151c96d9'
    build_url_bug='https://travis-ci.org/squaresLab/Houston/builds/349623956'
    commit_fix='04b2a1196198390a4e8791bf5ea21ecc457e2ab4'
    build_url_fix='https://travis-ci.org/squaresLab/Houston/builds/349626339'

    observation = Observation(url_repository,
                              commit_bug,
                              build_url_bug,
                              commit_fix,
                              build_url_fix)

    assert observation.repository == url_repository
    assert observation.commit_bug == commit_bug
    assert observation.build_url_bug == build_url_bug
    assert observation.commit_fix == commit_fix
    assert observation.build_url_fix == build_url_fix
