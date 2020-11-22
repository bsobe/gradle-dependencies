from dataclasses import dataclass


@dataclass
class Dependency:
    path: str
    children_dependencies: list
