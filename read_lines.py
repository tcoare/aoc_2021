def read_lines(path: str, type=None) -> list:
    with open(path) as f:
        return [type(num).strip() for num in f.readlines()] if type else [line.strip() for line in f.readlines()]
