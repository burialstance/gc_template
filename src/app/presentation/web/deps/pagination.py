from dataclasses import dataclass

from litestar.params import Parameter


@dataclass
class Pagination:
    limit: int
    offset: int


def provide_limit_offset_pagination(
        limit: int = Parameter(query="limit", ge=1, default=100, required=False),
        offset: int = Parameter(query="offset", ge=0, default=0, required=False),
) -> Pagination:
    return Pagination(limit=limit, offset=offset)
