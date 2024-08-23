from typing import Generic, List, TypeVar
from pydantic import BaseModel, conint
from pydantic.generics import GenericModel

class PageParams(BaseModel):
    """ Request query params for paginated API. """
    page: conint(ge=1) = 1 # type: ignore
    size: conint(ge=1, le=100) = 10 # type: ignore


T = TypeVar("T")

class PagedResponseSchema(GenericModel, Generic[T]):
    """Response schema for any paged API."""

    total: int
    page: int
    size: int
    results: List[T]