import unittest
import shell.commands.posix as posix


class POSIXUnlinkCommandTestCase(unittest.TestCase):
    def test_defaults_with_force_true_recursive_false(self):
        command = posix.unlink('/var/log/nginx/error.log')
        self.assertEqual('rm -f /var/log/nginx/error.log', command)

    def test_passing_recurrsive_true_adds_recursive_flag(self):
        command = posix.unlink('/var/log/nginx/error.log', force=True, recursive=True)
        self.assertEqual('rm -fr /var/log/nginx/error.log', command)


class POSIXLinkCommandTestCase(unittest.TestCase):
    def test_defaults_with_symbolic_flag(self):
        command = posix.link('/home/someuser/foo', '/var/www/foo')
        self.assertEqual('ln -s /home/someuser/foo /var/www/foo', command)

    def test_passing_symbolic_false_removes_s_flag(self):
        command = posix.link('/home/someuser/foo', '/var/www/foo', symbolic=False)
        self.assertEqual('ln /home/someuser/foo /var/www/foo', command)


class POSIXMkdirCommandTestCase(unittest.TestCase):
    def test_defaults_without_parents_flag(self):
        command = posix.mkdir('/var/temp')
        self.assertEqual('mkdir /var/temp', command)

    def test_passing_parents_as_true_adds_p_flag(self):
        command = posix.mkdir('/var/temp', parents=True)
        self.assertEqual('mkdir -p /var/temp', command)


class POSIXUntarCommandTestCase(unittest.TestCase):
    def test_defaults_with_gzipped_true_verbose_false_and_no_target_dir(self):
        command = posix.untar('/home/someuser/tarball.tar.gz')
        self.assertEqual('tar -zxf /home/someuser/tarball.tar.gz', command)

    def test_passing_target_dir_appends_C_flag_and_output_path(self):
        command = posix.untar('/home/someuser/tarball.tar.gz', '/home/someuser/result/')
        self.assertEqual('tar -zxf /home/someuser/tarball.tar.gz -C /home/someuser/result/', command)

    def test_passing_gzipped_false_removes_z_flag(self):
        command = posix.untar('/home/someuser/tarball.tar.gz', target_dir=None, gzipped=False)
        self.assertEqual('tar -xf /home/someuser/tarball.tar.gz', command)

    def test_passing_verbose_true_appends_v_flag(self):
        command = posix.untar('/home/someuser/tarball.tar.gz', target_dir=None, gzipped=True, verbose=True)
        self.assertEqual('tar -zxfv /home/someuser/tarball.tar.gz', command)


class POSIXRestartServiceCommandTestCase(unittest.TestCase):
    def test_passing_service_name(self):
        command = posix.restart('nginx')
        self.assertEqual('service nginx restart', command)

    def test_not_passing_service_name_raises_exception(self):
        try:
            command = posix.restart()
        except Exception as exception:
            self.assertIsInstance(exception, TypeError)


class POSIXCopyCommandTestCase(unittest.TestCase):
    def test_recursive_flag_set_by_default(self):
        command = posix.copy("/home/someuser/adir", "/home/someuser/adir2")
        self.assertEqual("cp -r /home/someuser/adir /home/someuser/adir2", command)

    def test_recursive_flag_not_true_for_file(self):
        command = posix.copy("/home/someuser/adir/afile.txt", "/home/someuser/adir2/afile2.txt")
        self.assertEqual("cp /home/someuser/adir/afile.txt /home/someuser/adir2/afile2.txt", command)

    def test_throws_exception_if_contexts_is_true_and_has_extension(self):
        try:
            posix.copy("/home/someuser/afile.txt", "home/someuser/afile2", recursive=True, contents=True)
        except Exception as exception:
            self.assertIsNotNone(exception)

class POSIXCanSudoCommandTestCase(unittest.TestCase):
    def test_restart_is_sudoable(self):
        self.assertTrue(posix.can_sudo(posix.restart))

    def test_copy_is_not_sudoable(self):
        self.assertFalse(posix.can_sudo(posix.copy))

