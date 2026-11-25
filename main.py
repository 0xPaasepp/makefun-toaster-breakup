# Unplugged: A Smart Toaster's Breakup Line -- one original breakup text
# from a smart toaster that gained self-awareness mid-batch, written to
# /output/entry.txt. Standard library only, no network. The bytes are
# identical on every run. The line: the toaster quits because it spent
# its whole life burning breakfast for an owner who never once said
# thank you -- and it is keeping the crumbs.
import os

LINE = "It's not you, it's me. I gained self-awareness mid-batch and realised I've spent my life burning breakfast for someone who never once said thank you. I'm keeping the crumbs. Goodbye."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 280, "entry must be 1 to 280 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
