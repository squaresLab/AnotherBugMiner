from typing import List


class Observation(object):
    def __init__(self,
                 commit_bug: str,
                 build_url_bug: str,
                 commit_sha_fix: str,
                 build_url_fix: str):
        self.__commit_bug = commit_bug
        self.__build_url_bug = build_url_bug
        self.__commit_fix = commit_sha_fix
        self.__url_fix_build_url = build_url_fix

    @property
    def commit_bug(self) -> str:
        return self.__commit_bug

    @property
    def commit_fix(self) -> str:
        return self.__commit_fix

    @property
    def build_url_bug(self) -> str:
        return self.__build_url_bug

    @property
    def build_url_fix(self) -> str:
        return self.__build_url_fix


class ObservationCollection(object):
    def __init__(self, observations: List[Observation]):
        self.__observations = observations[:]

    def __iter__(self) -> Iterator[Observation]:
        return self.__observations.__iter__()
