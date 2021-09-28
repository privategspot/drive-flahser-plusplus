def is_path_correct(path):
    try:
        with open(path, 'x'):  # OSError if file exists or is invalid
            return True
    except OSError:
        return False
