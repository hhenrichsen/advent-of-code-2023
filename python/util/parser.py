from abc import ABC, abstractmethod
from inspect import signature
import re
from typing import Callable, Iterable, List, Union, TypeVar


class Region(ABC):
    @abstractmethod
    def get_range(self, input, start=0, len=0) -> (int, int):
        pass


class RangeRegion(Region):
    def __init__(self, first: int, second: Union[None, int] = None):
        if second is None:
            self.__len = first
            self.__range = None
        else:
            self.__range = (first, second)
            self.__len = None

    def get_range(self, input, start, len):
        return self.__range if self.__range is not None else (start, start + self.__len)


class AfterRegion(Region):
    def __init__(self, matcher: Union[str, Callable[[str, int, str], bool]]):
        self.__matcher = matcher
        self.__matcher_params = (
            len(signature(matcher).parameters) if callable(matcher) else 0
        )

    def get_range(self, input: str, start=0, len=0):
        if isinstance(self.__matcher, str):
            return (start, input.index(self.__matcher, start, len) + 1)
        for i in range(start, len):
            if self.__matcher_params == 1:
                if self.__matcher(input[i]):
                    return (start, i + 1)
            elif self.__matcher_params == 2:
                if self.__matcher(input[i], i):
                    return (start, i + 1)
            elif self.__matcher(input[i], i, input):
                return (start, i + 1)
        return (start, len)


class UntilRegion(Region):
    def __init__(self, matcher: Union[str, Callable[[str, int, str], bool]]):
        self.__matcher = matcher
        self.__matcher_params = (
            len(signature(matcher).parameters) if callable(matcher) else 0
        )

    def get_range(self, input: str, start=0, len=0):
        if isinstance(self.__matcher, str):
            return (start, input.index(self.__matcher, start, len))
        for i in range(start, len):
            if self.__matcher_params == 1:
                if self.__matcher(input[i]):
                    return (start, i)
            elif self.__matcher_params == 2:
                if self.__matcher(input[i], i):
                    return (start, i)
            elif self.__matcher(input[i], i, input):
                return (start, i)
        return (start, len)


class RestRegion(Region):
    def get_range(self, input: str, start, len):
        return (start, len)


class InputParser:
    def __init__(self, regions: Union[None, List[Region]], parsers):
        self.regions = regions if regions is not None else []
        if regions is not None and parsers is None or len(parsers) != len(regions):
            raise ValueError(
                "parsers must be provided and must be the same length as regions"
            )
        self.parsers = parsers if parsers is not None else []

    def parse(self, input: str):
        start = 0
        for i, region in enumerate(self.regions):
            start, end = region.get_range(input, start, len(input))
            res = self.parsers[i](input[start:end])
            if res is not None:
                yield res
            start = end


A = TypeVar("A")


def whitespace_segmenter(
    child: Callable[[str], A],
    _filter: Callable[[str], bool] = None,
    transform: Callable[[Iterable[A]], A] = list,
):
    if filter:
        return lambda s: transform(
            map(child, filter(_filter, re.split("\s+", s.strip())))
        )
    return lambda s: transform(map(child, re.split("\s+", s.strip())))


def discard(_):
    return None
