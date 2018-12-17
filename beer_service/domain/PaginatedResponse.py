import json

from google.protobuf.json_format import MessageToDict


class PaginatedResponse:

    def __init__(self, previous_page, next_page, results, page_count, total_count):
        self._next_page = next_page
        self._previous_page = previous_page
        self._results = results
        self._page_count = page_count
        self._total_count = total_count

    def get_previous_page(self):
        return self._previous_page

    def get_next_page(self):
        return self._next_page

    def get_results(self):
        return self._results

    def get_total_count(self):
        return self._total_count

    def get_page_count(self):
        return self._page_count

    @staticmethod
    def _proto_to_dict(proto_object):
        return MessageToDict(
            proto_object,
            including_default_value_fields=True,
            preserving_proto_field_name=True,
            use_integers_for_enums=False
        )

    def __str__(self):
        contents = json.dumps({
            "previous_page": self.get_previous_page(),
            "next_page": self.get_next_page(),
            "results": map(self._proto_to_dict, self.get_results()),
            "page_count": self.get_page_count(),
            "total_count": self.get_total_count()
        })
        return "<%s, %s>" % (self.__class__.__name__, contents)
