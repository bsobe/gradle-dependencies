# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import testfile
from Dependency import Dependency
import DependencyParser as parser
import Exporter as Exporter
import GraphExporter


def printer(depier: list, prefix: str):
    dep: Dependency
    print(prefix + "{")
    for dep in depier:
        print(prefix + "\t" + dep.path)
        if len(dep.children_dependencies) != 0:
            printer(dep.children_dependencies, prefix + "\t")
    print(prefix + "}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # output = command.get_dependencies()
    output = testfile.testOutput.splitlines()
    # for line in output:
    # print(line)

    dependencies = parser.parse(output)
    #
    # printer(dependencies, "")
    Exporter.export_as_html(dependencies)
    GraphExporter.export_as_html(dependencies)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
