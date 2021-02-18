import os


def chmod(path, mode, **kwargs):
    try:
        os.chmod(path, mode, **kwargs)
    except Exception as err:
        print("Failed to set permissions: {} on: {} - {}".format(mode, path, err))
        return False
    return True
