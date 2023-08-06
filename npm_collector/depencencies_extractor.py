import json


# returns a dict of dependencies where key = package name and value = semantic version
def list_dependencies(file) -> dict:
    all_deps = dict()
    package_json = json.load(file)
    deps_tag = "dependencies"
    deps_dev_tag = "devDependencies"
    deps_peer_tag = "peerDependencies"

    all_deps.update(set_of_deps(deps_tag, package_json))
    all_deps.update(set_of_deps(deps_dev_tag, package_json))
    all_deps.update(set_of_deps(deps_peer_tag, package_json))
    return all_deps


def set_of_deps(tag: str, json_object: any) -> set:
    result = dict()
    if tag in json_object:
        for key in json_object[tag]:
            result[key] = json_object[tag][key]
    return result


if __name__ == "__main__":
    deps = list_dependencies(open("../test/resources/package_all.json"))
    for dep in deps:
        print("npm pack " + dep + "@\"" + deps[dep] + "\"")


