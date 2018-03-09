from typing import List, Iterator
import csv


class Observation(object):
    def __init__(self,
                 url_repository: str,
                 commit_bug: str,
                 build_url_bug: str,
                 commit_sha_fix: str,
                 build_url_fix: str):
        self.__url_repository = url_repository
        self.__commit_bug = commit_bug
        self.__build_url_bug = build_url_bug
        self.__commit_fix = commit_sha_fix
        self.__build_url_fix = build_url_fix

    @property
    def repository(self) -> str:
        return self.__url_repository

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
    @staticmethod
    def load(fn: str) -> 'ObservationCollection':
        observations = []
        with open(fn, 'r') as f:
            reader = csv.reader(f)
            for row in reader[1:]:
                observation = Observation(*row)
        return ObservationCollection(observations)

    def __init__(self, observations: List[Observation]):
        self.__observations = observations[:]

    def __iter__(self) -> Iterator[Observation]:
        return self.__observations.__iter__()

    def __len__(self) -> int:
        return len(self.__observations)

    def save(self, fn: str) -> None:
        with open(fn, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Repository URL",
                             "Bug Commit",
                             "Bug Build URL",
                             "Fix Commit",
                             "Fix Build URL"])
            for observation in self.__observations:
                row = [observation.repository,
                       observation.commit_bug,
                       observation.build_url_bug,
                       observation.commit_fix,
                       observation.build_url_fix]
                writer.writerow(row)
