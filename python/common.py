from dataclasses import dataclass


def extract_desc(filename: str) -> (str, list):
    prefix = filename[: filename.rfind("[")]
    desc = filename[filename.rfind("[") + 1 : filename.rfind("]")]
    desc = desc.split(",")
    dict_data = {x[: x.find("=")]: x[x.find("=") + 1 :] for x in desc if "=" in x}
    desc = [x for x in desc if "=" not in x]
    desc.append(dict_data)
    return (prefix, desc)


@dataclass
class OutputLog:
    trace_path: str
    cache_size: int
    ignore_obj_size: bool
    miss_ratio: float
    n_req: int
    n_promoted: int


def ordinal(n):
    n = int(n)
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"
