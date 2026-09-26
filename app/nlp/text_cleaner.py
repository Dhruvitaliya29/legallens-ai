import re


class TextCleaner:
    """Normalize extracted PDF text without changing its meaning."""

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove trailing whitespace from each line
        text = "\n".join(line.rstrip() for line in text.split("\n"))

        # Collapse excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Normalize repeated spaces/tabs
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()