from abc import ABC, abstractmethod
from inspect import signature
from typing import Callable, List, Union


class Region(ABC):
    @abstractmethod
    def get_range(self, input, start=0, len=0) -> (int, int):
        pass


class RangeRegion(Region):
    def __init__(self, first: int, second: Union[None, int] = None):
        if second is None:
            self.__range = (0, first)
        else:
            self.__range = (first, second)

    def get_range(self, input, start, len):
        return self.__range


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
    def get_range(input: str, start, len):
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
            print(start, len(input))
            start, end = region.get_range(input, start, len(input))
            print(input[start:end])
            res = self.parsers[i](input[start:end])
            print(res)
            yield res
            start = end
