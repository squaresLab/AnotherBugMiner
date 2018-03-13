import os
import tempfile

import pytest

from abm.observation import Observation, ObservationCollection


def test_properties():
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


def check_bugs_collection(observations: ObservationCollection):
    assert len(observations) == 1

    contents = list(observations)
    entry = contents[0]
    assert entry.repository == 'https://github.com/IQSS/dataverse'
    assert entry.commit_bug == 'ba64c543701f1942bff3ee39677d1a4932b32c25'
    assert entry.build_url_bug == 'https://travis-ci.org/IQSS/dataverse/jobs/289573808'
    assert entry.commit_fix == '5a53fa0f42b88b614685ebfd72ad47428f1c2028'
    assert entry.build_url_fix == 'https://travis-ci.org/IQSS/dataverse/builds/289591312'


def test_load():
    fn = os.path.join(os.path.dirname(__file__), 'observation/bugs.csv')
    observations = ObservationCollection.load(fn)
    check_bugs_collection(observations)


def test_save():
    fn_original = os.path.join(os.path.dirname(__file__), 'observation/bugs.csv')
    observations_original = ObservationCollection.load(fn_original)

    fn_temp = tempfile.NamedTemporaryFile('w')
    try:
        observations_original.save(fn_temp.name)
        observations_loaded = ObservationCollection.load(fn_temp.name)
        check_bugs_collection(observations_loaded)
    finally:
        fn_temp.close()
