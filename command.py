# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import config
import subprocess


def get_dependencies():
    result = subprocess.check_output(
        ["cd " + config.projectPath + "; ./gradlew -q Trendyol_v2:dependencies --configuration prodRuntimeClasspath"],
        shell=True, text=True)
    print(result)
    output = result.splitlines()

    return output
