import subprocess
from typing import TextIO

cmd = ["py", "./tests/test.py"]
process = subprocess.run(cmd, check=True, capture_output=True)


def write_readme_block(file: TextIO, content: str, markup_language: str = "") -> None:
    file.write(f"\n```{markup_language}\n")
    file.write(content)
    file.write(f"\n```\n")


with open("./tests/log.log", "r") as log:
    LOG_CONTENTS = log.read().rstrip()

with open("./tests/test.py", "r") as f:
    TEST_FUNCTION = "".join(f.readlines()[10:]).rstrip()


with open("README.md", "w") as README:
    README.write("# exception-logging-decorator\n")
    README.write("The following function:")
    write_readme_block(README, TEST_FUNCTION, "py")
    README.write("Logs the following exception in `log.log`.")
    write_readme_block(README, LOG_CONTENTS)
