from shell.commands import posix, cygwin
import re as regex
from shell.exceptions import UnSupportedShellException

shells = {"Linux": posix, "CYGWIN_NT-6.1": cygwin, "CYGWIN_NT": cygwin}


def from_unix_name(uname):
    """
    Attempt to determine the appropriate shell from  the unix name provided
    :param uname:
    :return:
    """
    system_name = __parse_uname(uname)
    return for_system(system_name)


def for_system(system_name):
    """
    Attemps to determine the appropriate shell from the system name provided
    :param system_name:
    :return: :raise UnSupportedProviderException:
    """

    if not system_name in shells:
        raise UnSupportedShellException("There are no providers available for environment: {0}".format(system_name))
    else:
        return shells[system_name]


def __parse_uname(uname):
    """
    Takes in a uname output and returns the environment
    :param uname: uname output
    :type uname: str
    :return:
    """
    matches = regex.match('^\w+', uname)

    if matches is None:
        return matches
    else:
        return matches.group(0).rstrip()
