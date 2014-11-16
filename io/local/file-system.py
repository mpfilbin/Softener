from os import path
import StringIO

from io import open


def read_file(file_path):
    """
    Returns the contents of a file at the `file_path` parameter. Expects a file path to be absolute
    :param file_path:
    :return:
    """
    with __get_file_descriptor(file_path, 'r') as descriptor:
        content = descriptor.read().rstrip('\n')
        descriptor.close()
        return content


def write_file(file_path, contents):
    """
    Writes the contents of the 'contents' vaiable to the file at 'file_path'
    :param file_path: String value of the absolute path to the file to be written
    :param contents: String
    """
    with __get_file_descriptor(file_path, 'r') as descriptor:
        file_contents = contents.getvalue() if isinstance(contents, StringIO) else contents
        descriptor.write(file_contents)


def __ensure_file_exists(file_path):
    if not path.isfile(file_path):
        raise IOError("No such file: {0}".format(file_path))


def __get_file_descriptor(file_path, mode='r+'):
    __ensure_file_exists(file_path)
    return open(file_path, mode)
