class UnSupportedShellException(Exception):
    def __init__(self, arg, **kwargs):
        Exception.__init__(self, arg, kwargs)