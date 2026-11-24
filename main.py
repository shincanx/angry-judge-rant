"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. The rant is capped at 400 characters.
"""

import os

RANT = (
    "The self-checkout just accused me of stealing my own groceries. "
    "'Unexpected item in the bagging area.' The item was the bag. "
    "I scanned it, I paid for it, I'm waving the receipt like a hostage "
    "negotiator \u2014 and this glowing box still flashes red at me like I "
    "smuggled a cucumber. I came in for milk. I left having been "
    "interrogated by a scale with trust issues."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(RANT)
    print(f"wrote {path} ({len(RANT)} characters)")


if __name__ == "__main__":
    main()
