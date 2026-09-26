from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class PageContent:
    page_number: int
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass
class DocumentContent:
    filename: str
    file_path: Path
    page_count: int
    pages: list[PageContent]
    metadata: dict = field(default_factory=dict)