import inspect


def log(msg: str) -> str:
    return msg + " - " + inspect.getmodule(inspect.stack()[1][0]).__name__
