import unittest
from shell.command_builders.POSIXShellBuilder import POSIXShellBuilder


class POSIXShellBuilderTest(unittest.TestCase):

    def setUp(self):
        self.command = "mkdir"
        self.flag = "p"
        self.argument = "/home/test/some_dir"
        self.builder = POSIXShellBuilder(self.command)

    def test_stringify_returns_string(self):
        self.assertEqual("mkdir", self.builder.stringify())

    def test_add_flag(self):
        self.builder.add_flag(self.flag)
        self.assertEqual("mkdir -p", self.builder.stringify())

    def test_add_parameter(self):
        self.builder.add_argument(self.argument)
        self.assertEqual("mkdir /home/test/some_dir", self.builder.stringify())

    def test_add_parameter_and_flag(self):
        self.builder.add_argument(self.argument)
        self.builder.add_flag(self.flag)
        self.assertEqual("mkdir -p /home/test/some_dir", self.builder.stringify())




if __name__ == '__main__':
    unittest.main()