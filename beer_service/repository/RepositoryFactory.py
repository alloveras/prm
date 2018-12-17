from memory import InMemoryBeerRepository


class RepositoryFactory:

    def __init__(self, args):
        self._beer_repository = InMemoryBeerRepository()

    def create_beer_repository(self):
        return self._beer_repository
