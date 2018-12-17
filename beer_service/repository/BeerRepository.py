from abc import ABCMeta, abstractmethod


class BeerRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list_all(self, page=0, size=50):
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, beer_id):
        raise NotImplementedError()

    @abstractmethod
    def store(self, beer):
        raise NotImplementedError()
