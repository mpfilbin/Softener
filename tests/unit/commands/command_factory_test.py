import unittest
from shell.exceptions import UnSupportedShellException
import shell.commands.factory as subject


class CommandFactoryTest(unittest.TestCase):
    def test_when_passed_unsupported_system_raises_exception(self):
        try:
            subject.for_system('Darwin')
        except Exception as exception:
            self.assertIsInstance(exception, UnSupportedShellException)

    def test_when_pass_supported_system(self):
        shell = subject.for_system('Linux')
        self.assertIsNotNone(shell)

    def test_when_pass_supported_uname_value(self):
        cygwing_shell = subject.from_unix_name('CYGWIN_NT-6.1 WIN-JV4B6REP3D1 1.7.32(0.274/5/3) 2014-08-13 23:06 x86_64 Cygwin')
        posix_shell = subject.from_unix_name('Linux ip-172-31-35-192 3.13.0-29-generic #53-Ubuntu SMP Wed Jun 4 21:00:20 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux')
        self.assertIsNotNone(cygwing_shell)
        self.assertIsNotNone(posix_shell)

    def test_when_passed_unsupported_uname_value(self):
        try:
            subject.from_unix_name('Darwin Kernel Version 11.3.0: Thu Jan 12 18:47:41 PST 2012; root:xnu-1699.24.23~1/RELEASE_X86_64')
        except Exception as exception:
            self.assertIsInstance(exception, UnSupportedShellException)
