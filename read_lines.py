def read_lines(path: str, type=None) -> list:
    with open(path) as f:
        return [type(num) for num in f.read().split()] if type else [line for line in f.read().split()]
