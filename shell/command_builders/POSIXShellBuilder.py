from base import BuilderBase


class POSIXShellBuilder(BuilderBase):
    def __init__(self, command):
        """
        :param command: The initial command for which we are building
        :type command: str
        """
        BuilderBase.__init__(self, command)

    def _compile_flags(self):
        """
        returns a string representation of any commandline switches represented by `flags` parameter
        :rtype : str
        """
        result = ''
        if len(self.flags) > 0:
            result += " -{0}".format("".join(self.flags))
        return result

    def _compile_arguments(self):
        """
        returns a compiled list of arguments as a string
        :rtype: str
        """
        result = ' '
        if len(self.args) > 0:
            result += ' '.join(self.args)
        return result