class BuilderBase:
    def __init__(self, command):
        self.flags = []
        self.args = []
        self.command = command

    def add_flag(self, flag):
        """
        Append a commandline flag
        :param flag: flag value
        :type flag: str
        """
        self.flags.append(flag)

    def add_argument(self, arg):
        """
        appends an argument to the command
        :param arg: the argument to be appended
        :type arg: str
        """
        self.args.append(arg)

    def stringify(self):
        """
        returns a string representation of the command

        Example:
            command = POSIXBuilder("mkdir")
            command.add_flag("p")
            command.add_arg("/home/me/new_dir")
            command.stringify => "mkdir -p /home/me/new_dir"

        :return: str
        """
        flags = self._compile_flags()
        arguments = self._compile_arguments()

        return "".join([self.command, flags, arguments]).strip()

    def _compile_flags(self):
        raise NotImplemented("Abstract Method - Implement in concrete class")

    def _compile_arguments(self):
        raise NotImplemented("Abstract Method - Implement in concrete class")
