import uuid

from domain import PaginatedResponse
from repository import BeerRepository


class InMemoryBeerRepository(BeerRepository):

    def __init__(self):
        self._beers = []
        self._beers_count = 0
        self._beers_id_index = {}
        self._beers_name_index = {}

    def get_by_id(self, beer_id):
        if beer_id in self._beers_id_index:
            beer_position = self._beers_id_index.get(beer_id)
            return self._beers[beer_position]
        else:
            raise LookupError("Beer (" + beer_id + ") doesn't exist")

    def list_all(self, page=0, size=50):
        previous_page = None if page <= 0 else page - 1

        if (page + 1) * size >= self._beers_count:
            results = self._beers[page * size:]
            next_page = None
        else:
            results = self._beers[page * size: (page + 1) * size]
            next_page = page + 1

        return PaginatedResponse(previous_page, next_page, results, len(results), self._beers_count)

    def store(self, beer):
        if self._has_unique_name(beer.id, beer.name):
            if self._beer_exists(beer.id):
                beer_position = self._beers_id_index.get(beer.id)
                self._beers_name_index.update({beer.name: beer_position})
                self._beers[beer_position] = beer
            else:
                beer.id = str(uuid.uuid4())
                self._beers.append(beer)
                self._beers_id_index.update({beer.id: self._beers_count})
                self._beers_name_index.update({beer.name: self._beers_count})
                self._beers_count += 1
            return beer
        else:
            raise ValueError("Beer named (" + beer.name + ") already exists")

    def _has_unique_name(self, beer_id, beer_name):
        if beer_name not in self._beers_name_index:
            return True
        elif self._beer_exists(beer_id):
            return self._beers_name_index.get(beer_name) == self._beers_id_index.get(beer_id)
        else:
            return False

    def _beer_exists(self, beer_id):
        return beer_id in self._beers_id_index
