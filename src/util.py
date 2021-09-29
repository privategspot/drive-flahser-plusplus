import re


def is_path_correct(path):
    pattern = r"^['\"]?(?:/[^/\n]+)*['\"]?$"
    res = re.match(pattern, path)
    if res.group(0) is not None:
        return True
    return False
