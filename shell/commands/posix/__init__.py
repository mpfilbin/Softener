__author__ = 'mfilbin'

from shell.command_builders.POSIXShellBuilder import POSIXShellBuilder
import re as regex

file_extension = regex.compile('.+(\.\w+)+$')


def unlink(file_path, force=True, recursive=False, contents=False):
    command = POSIXShellBuilder('rm')

    if force is True:
        command.add_flag('f')
    if recursive is True:
        command.add_flag('r')
    if contents is True:
        file_path = __strip_trailing_slash(file_path)
        file_path += '/*'
        command.add_argument(file_path)
    else:
        command.add_argument(file_path)

    return command.stringify()


def rm(file_path, force=True, recursive=False, contents=False):
    return unlink(file_path, force, recursive, contents);


def link(source, target, symbolic=True):
    command = POSIXShellBuilder('ln')

    if symbolic is True:
        command.add_flag('s')

    command.add_argument(source)
    command.add_argument(target)

    return command.stringify()


def ln(source, target, symbolic=True):
    return link(source, target, symbolic)


def copy(source, target, recursive=True, contents=False):
    command = POSIXShellBuilder('cp')

    if recursive is True and not __has_file_extension(source):
        command.add_flag('r')
    if contents is True:
        if __has_file_extension(source):
            raise Exception("cannot copy contents of a file, only directories")
        else:
            source = __strip_trailing_slash(source)
            source += '/*'
            command.add_argument(source)
    else:
        command.add_argument(source)

    command.add_argument(target)
    return command.stringify()


def cp(source, target, recursive=True, contents=False):
    return copy(source, target, recursive, contents)


def mkdir(dir_name, parents=False):
    command = POSIXShellBuilder('mkdir')

    if parents is True:
        command.add_flag('p')

    command.add_argument(__strip_trailing_slash(dir_name))

    return command.stringify()


def untar(file_path, target_dir=None, gzipped=True, verbose=False):
    """
    Creates a shell command that represents un-packaging a tarball into the current directory
    :param file_path: The absolute file path of the file to be unpacked
    :param gzipped: True if the tarball has been gzipped
    :param verbose: True if you want verbose output
    :return: String representation of the command
    """
    command = POSIXShellBuilder('tar')

    if gzipped is True:
        command.add_flag('z')

    command.add_flag('x')
    command.add_flag('f')

    if verbose is True:
        command.add_flag('v')

    command.add_argument(file_path)

    if target_dir is not None:
        command.add_argument("-C {0}/".format(__strip_trailing_slash(target_dir)))

    return command.stringify()


def restart(service_name):
    if service_name is None:
        raise TypeError("service name is required")
    command = POSIXShellBuilder('service')
    command.add_argument(service_name)
    command.add_argument('restart')
    return command.stringify()


def can_sudo(method_name):
    return method_name in _sudoable_


def __strip_trailing_slash(string):
    return regex.sub('/$', '', string)


def __has_file_extension(path):
    match = file_extension.match(path)
    return match is not None


_sudoable_ = [restart]
