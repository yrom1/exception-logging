import subprocess
from typing import TextIO

def write_markdown_block(file: TextIO, content: str, markup_language: str = "") -> None:
    file.write(f"\n```{markup_language}\n")
    file.write(content)
    file.write(f"\n```\n")

test_log_pair = [('test_logger.py', 'log.log'), ('test_cls.py', 'cls.log'), ('test_meta.py', 'meta.log')]

for test, log in test_log_pair:
    cmd = ["py", f"./tests/{test}"]
    process = subprocess.run(cmd, check=True, capture_output=True)

with open("README.md", "w") as README:
    README.write("# exception-logging-decorator\n")
    README.write('Exception logging decorator, class decorator and metaclass generator. Some example usages are show below, and the corresponding log files created.')

for test, log in test_log_pair:
    with open(f"./tests/{test}", "r") as f:
        test_file = "".join(f.readlines()[10:]).rstrip()

    with open(f"./tests/{log}", "r") as f:
        log_file = f.read().rstrip()

    with open("README.md", "a") as README:
        README.write("\n\n---\n\n")
        write_markdown_block(README, test_file, "py")
        README.write(f"Logs the following in {log}.")
        write_markdown_block(README, log_file)
