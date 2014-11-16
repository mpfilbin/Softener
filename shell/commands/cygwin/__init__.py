from shell.command_builders.PowerShellBuilder import PowerShellBuilder
import shell.commands.posix as posix
import re as regex


def unlink(file_path, force=True, recursive=True, contents=False):
    return posix.unlink(file_path, force, recursive, contents)


def link(source, target, symbolic=True):
    return posix.copy(source, target, symbolic, contents=True)


def copy(source, target, recursive=True):
    return posix.copy(source, target, recursive)


def mkdir(dir_name, parents=False):
    return posix.mkdir(dir_name, parents)


def untar(file_path, target_dir=None, gzipped=True, verbose=False):
    """
    Creates a shell command that represents un-packaging a tarball into the current directory
    :param file_path: The absolute file path of the file to be unpacked
    :param gzipped: True if the tarball has been gzipped
    :param verbose: True if you want verbose output
    :return: String representation of the command
    """
    return posix.untar(file_path, target_dir, gzipped, verbose)


def restart(service_name):
    if service_name is None:
        raise TypeError

    command = PowerShellBuilder('Restart-Service')
    command.add_argument("displayname \"{0}\"".format(service_name))

    return command.stringify()


def can_sudo(function):
    return function in _sodoable_


def __strip_trailing_slash(string):
    return regex.sub('/$', '', string)

_sodoable_ = []
