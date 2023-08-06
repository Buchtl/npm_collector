import subprocess
import unittest

from npm_collector import tarball_utils


class TarballUtilsTests(unittest.TestCase):

    @staticmethod
    def deleteJest() -> None:
        subprocess.getoutput("rm -rf jest*")

    def setUp(self) -> None:
        self.deleteJest()

    def tearDown(self) -> None:
        self.deleteJest()

    def test_list_dependencies_all(self):
        tarball_utils.downlaod_tar("jest@latest")
        given = "jest"
        actual = subprocess.getoutput("ls | grep jest")
        self.assertTrue(actual.startswith(given))


if __name__ == '__main__':
    unittest.main()
