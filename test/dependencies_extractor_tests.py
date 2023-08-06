import unittest
from npm_collector import depencencies_extractor


class ListDependenciesTest(unittest.TestCase):
    deps = dict()
    deps["@dep/withat"] = "^1.0"
    deps["dep"] = "^1.0"
    deps_dev = dict()
    deps_dev["@dev/withat"] = "^1.0"
    deps_dev["devdep"] = "^1.0"
    deps_peer = dict()
    deps_peer["peerdep"] = "^1.0 || ^2.0 || ^3.0"
    deps_all = dict()
    deps_all.update(deps)
    deps_all.update(deps_dev)
    deps_all.update(deps_peer)

    def test_list_dependencies_all(self):
        f = open("resources/package_all.json")
        given = depencencies_extractor.list_dependencies(f)
        f.close()
        expected = self.deps_all
        self.assertEqual(given, expected)

    def test_list_dependencies_deps_only(self):
        f = open("resources/package_deps.json")
        given = depencencies_extractor.list_dependencies(f)
        f.close()
        expected = self.deps
        self.assertEqual(given, expected)


if __name__ == '__main__':
    unittest.main()
