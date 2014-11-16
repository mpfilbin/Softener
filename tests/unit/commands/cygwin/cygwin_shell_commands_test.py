import shell.commands.cygwin as cygwin
import shell.commands.posix as posix
import unittest


class CygwinUnlinkCommandUnitTest(unittest.TestCase):
    def test_delegates_to_posix_implementation(self):
        cygwin_command = cygwin.unlink("/var/log/test.log", force=True, recursive=False, contents=False)
        posix_command = posix.unlink("/var/log/test.log")
        self.assertEqual(cygwin_command, posix_command)


class CygwinLinkCommandUnitTest(unittest.TestCase):
    def test_delegates_to_posix_copy_impementation(self):
        cygwin_command = cygwin.link('/home/someuser/', '/home/someuser/syslinked-files')
        posix_command = posix.copy('/home/someuser/', '/home/someuser/syslinked-files', recursive=True, contents=True)
        self.assertEqual(cygwin_command, posix_command)


class CygwinMkdirCommandUnitTest(unittest.TestCase):
    def test_delegates_to_posix_implementation(self):
        cygwin_command = cygwin.mkdir('/home/someuser/newdir/')
        posix_command = posix.mkdir('/home/someuser/newdir')
        self.assertEqual(cygwin_command, posix_command)


class CygwinUntarCommandUnitTest(unittest.TestCase):
    def test_delegates_to_posix_implementation(self):
        cygwin_command = cygwin.untar('/home/someuser/mytarball.tar.gz')
        posix_command = posix.untar('/home/someuser/mytarball.tar.gz')
        self.assertEqual(cygwin_command, posix_command)


class CygwinRestartCommandUnitTest(unittest.TestCase):
    def test_passing_no_arguments_raises_TypeError(self):
        try:
            cygwin.restart()
        except Exception as exception:
            self.assertIsInstance(exception, TypeError)

    def test_passing_service_name(self):
        command = cygwin.restart('some service')
        self.assertEqual('powershell Restart-Service -displayname "some service"', command)

