# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Dependency import Dependency


def is_valid_line(line: str):
    if line.startswith(" "):
        return is_valid_line(line.strip())
    else:
        return line.startswith("|") or line.startswith("+") or line.startswith("\\---")


def is_root_dependency(line: str):
    return line.startswith("+---") or line.startswith("\\---")


# noinspection PyPep8Naming
def parse(input: str):
    dependencies = []

    rootDependency: Dependency
    childDependency: Dependency
    childDependencyTree: list
    for line in input:
        if not is_valid_line(line):
            continue

        if is_root_dependency(line):
            # Root Level
            rootDependency = Dependency(line[len("+---"):], [])
            dependencies.append(rootDependency)
        else:
            # Child Level Processing
            childDependencyTree = dependencies
            trimmed = line
            tempDependency = rootDependency
            while True:
                if trimmed.startswith(" "):
                    # Case - Last Dependency
                    trimmed = trimmed.strip()
                    tempDependency = childDependencyTree[len(childDependencyTree) - 1]
                    childDependencyTree = tempDependency.children_dependencies
                elif trimmed.startswith("|    "):
                    # Case - Standard Dependency
                    trimmed = trimmed[len("|    "):]
                    tempDependency = childDependencyTree[len(childDependencyTree) - 1]
                    childDependencyTree = tempDependency.children_dependencies
                else:
                    break
            childDependencyTree.append(Dependency(trimmed[len("\\---"):], []))

    # for dep in dependencies:
    # print(dep.path)
    return dependencies
