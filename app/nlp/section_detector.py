import re


class SectionDetector:
    """Detect likely section headings in extracted document text."""

    HEADING_PATTERNS = [
        r"^(?:SECTION|ARTICLE|CHAPTER)\s+[A-Z0-9IVXLC]+.*$",
        r"^\d+(?:\.\d+)*[\.\)]?\s+[A-Z][A-Za-z0-9 ,&'()/-]{2,}$",
        r"^[A-Z][A-Z0-9 ,&'()/-]{3,}$",
    ]

    def detect(self, text: str) -> list[dict]:
        sections = []

        for line_number, raw_line in enumerate(text.splitlines(), start=1):
            line = raw_line.strip()

            if not line:
                continue

            if self._is_heading(line):
                sections.append(
                    {
                        "title": line,
                        "line_number": line_number,
                    }
                )

        return sections

    def _is_heading(self, line: str) -> bool:
        return any(
            re.match(pattern, line)
            for pattern in self.HEADING_PATTERNS
        )