import csv
import typing as T


class Obj:
    ObjID: int
    Time: int
    ObjSize: int
    ClockFlag: bool
    ClockFreq: int
    TimeBetween: int


ObjIDCounter = 0
TimeCounter = 0

path = "../trace/simple.csv"
size = 100
cache_size = 0.1

cache_q: T.List[Obj] = []
cache_h: T.Dict[int, Obj] = {}


# clock_freq
# lifetime_freq
# clock_time_between

# Only promote that has clock_freq > X, clock_time_between < Y,
# Shouldn't be called again after promotion
# decide 0.5 promotion that required.


def Generate() -> int:
    return 0


def Get(id: int) -> bool:
    return False


header = ["time-col", "obj-id-col", "obj-size-col"]

out_data: T.List[T.List[int]]
data: T.Dict[int, Obj]


def main() -> None:
    id = Generate()
    Get(id)


if __name__ == "__main__":
    main()
