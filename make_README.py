from typing import TextIO


def write_readme_block(file: TextIO, content: str, markup_language: str = "") -> None:
    file.write(f"\n```{markup_language}\n")
    file.write(content)
    file.write(f"\n```\n")


with open("log.log", "r") as log:
    LOG_CONTENTS = log.read().rstrip()

with open('test.py', 'r') as f:
    TEST_FUNCTION = f.read().rstrip()

# TEST_FUNCTION = """@log
# def no_return() -> NoReturn:
#     raise Exception("DO NOT PASS GO DO NOT COLLECT $200.")"""

with open("README.md", "w") as README:
    README.write("# exception-logging-decorator\n")
    README.write("The following function:")
    write_readme_block(README, TEST_FUNCTION, "py")
    README.write("Logs the following exception in `log.log`.")
    write_readme_block(README, LOG_CONTENTS)
