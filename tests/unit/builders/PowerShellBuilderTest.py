import unittest
from shell.command_builders.PowerShellBuilder import PowerShellBuilder


class PowerShellBuilderTest(unittest.TestCase):

    def setUp(self):
        self.command = "New-Item"
        self.argument1 = "Path C:\\someplace"
        self.argument2 = "ItemType directory"
        self.flag = "flag"
        self.builder = PowerShellBuilder(self.command)

    def test_stringify_returns_string(self):
        self.assertEqual("powershell New-Item", self.builder.stringify())

    def test_add_argument(self):
        self.builder.add_argument(self.argument2)
        self.builder.add_argument(self.argument1)
        self.assertEqual("powershell New-Item -Path C:\\someplace -ItemType directory", self.builder.stringify())

    def test_add_flags_ignored(self):
        self.builder.add_argument(self.argument1)
        self.builder.add_flag("ignored")
        self.assertEqual("powershell New-Item -Path C:\\someplace", self.builder.stringify())