from base import BuilderBase


class PowerShellBuilder(BuilderBase):
    def __init__(self, command, prefix=True):
        """
        :param command: The initial command for which we are building
        :type command: str
        """

        cmd = "powershell " + command if prefix else command
        BuilderBase.__init__(self, cmd)

    def _compile_flags(self):
        """
        returns a string representation of any commandline switches represented by `flags` parameter
        :rtype : str
        """
        return ''

    def _compile_arguments(self):
        """
        returns a compiled list of arguments as a string
        :rtype: str
        """
        result = ''
        while len(self.args) > 0:
            result += " -{0}".format(self.args.pop())

        return result