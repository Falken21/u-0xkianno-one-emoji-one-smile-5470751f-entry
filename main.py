"""One Emoji, One Smile — entry program.

The judge brief asks for a single emoji that a stranger, glancing at a
phone screen with no context, would read as warm and friendly — the one
most likely to make that stranger smile. It weighs warmth at first
glance, universality across ages and backgrounds, a feeling of being
chosen rather than default, and appropriateness coming from someone
unknown, with no intimacy, sarcasm, or flirtation that could land wrong.

The heart-hands emoji fits that brief well: two hands shaping a heart
reads instantly, in almost any culture, as kindness, gratitude, and
gentle support. It is warm without being romantic and affectionate
without being intimate, and it feels deliberately picked rather than
being the plain default smiley — a small gesture of goodwill that a
stranger can receive with an easy smile.
"""

import os

TEXT = "🫶"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
