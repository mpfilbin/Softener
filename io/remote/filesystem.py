from fabric.api import run, puts, put, sudo
import fabric.colors as colors
from shell.commands import factory

_shell_ = None


def get_shell():
    global _shell_
    if _shell_ is None:
        _shell_ = factory.for_system(run('uname -s'))
    return _shell_


def symlink(source, target):
    """
    Creates a symbolic linkage between the source file and the target file
    :param source:
    :param target:
    """
    shell = get_shell()
    puts(colors.cyan("Symlinking {0} to {1}".format(target, source)))
    run(shell.unlink(target))
    run(shell.link(source, target))


def remove_directory(source):
    """
    Removes a directory from the remote machine at the path provided
    :param source: the absolute path to the directory to be removed
    :type source: str
    """
    shell = get_shell()
    puts(colors.cyan("Removing directory at {0}".format(source)))
    run(shell.unlink(source, force=True, recursive=True))


def unpackage(tarball, target=None):
    shell = get_shell()
    puts(colors.cyan("Un-packaging {0}".format(tarball)))
    if target is None:
        output_dir = tarball.split('.')[0]
        run(shell.mkdir(output_dir))
    else:
        output_dir = target
    run(shell.untar(tarball, output_dir, gzipped=True))
    return output_dir


def cleanup_artifacts(file_extension):
    shell = get_shell()
    puts(colors.cyan("Removing all files with the following extension {0}".format(file_extension)))
    run(shell.unlink("*.{0}".format(file_extension)))


def restart_service(service):
    shell = get_shell()
    puts(colors.cyan("Restarting service: {0}".format(service)))
    if shell.can_sudo(shell.restart):
        sudo(shell.restart(service))
    else:
        run(shell.restart(service))


def upload_file(from_location, to_location=None):
    if to_location is None:
        to_location = __parse_file_from_path(from_location)

    puts(colors.cyan("Uploading file at {0} to {1}".format(from_location, to_location)))
    put(from_location, to_location)


def __parse_file_from_path(path):
    return path.split('/')[-1]