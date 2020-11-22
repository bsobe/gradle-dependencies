from Dependency import Dependency
import HtmlContainer as container


def export_dependency(dependency: Dependency):
    if len(dependency.children_dependencies) == 0:
        return f"""
        <li><span class="circle">{dependency.path}</span></li>
        """
    else:
        childrenOutput = ""
        for dep in dependency.children_dependencies:
            childrenOutput += export_dependency(dep)
        return f"""
        <li><span class="caret">{dependency.path}</span>
            <ul class="nested">
                {childrenOutput}
            </ul>
        </li>
        """


def export_as_html(depedencies: list):
    dependencyTreeOutput = ""
    current: Dependency
    for current in depedencies:
        dependencyTreeOutput += export_dependency(current)
    html_tree = f"""
        <ul id="myUL">
            <li><span class="caret">Dependency Tree</span>
                <ul class="nested">
                {dependencyTreeOutput}
            </ul>
        </ul>
    """

    html_output = container.html.replace(container.replacementText, html_tree)
    file = open("output.html", "w")
    file.write(html_output)
    file.close()
