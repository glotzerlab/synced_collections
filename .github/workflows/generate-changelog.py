import os
import re

include = False
lines = []

workspace = os.environ["GITHUB_WORKSPACE"]
with open(os.path.join(workspace, "changelog.txt")) as f:
    for line in f:
        if re.search(r"\[\d+\.\d+\.\d+\] -- \d{4}-\d{2}-\d{2}", line):
            if include:
                # We're now encountering the second header, so break
                break
            else:
                # First header, start including lines
                include = True
                lines.append(line)
        elif include:
            lines.append(line)

print("".join(lines))
